import datetime
import os
import tempfile
from typing import Optional, Tuple

from fastapi import HTTPException
import requests
import re

from ..DataGouvException import DataGouvException
from ..types.AssetTypes import AssetTypes

from google.cloud import storage
from google.oauth2 import service_account

class GCSClient:
    """Client pour gérer les opérations Google Cloud Storage."""
    
    def __init__(self, credentials_path: str = 'GCP_credentials.json'):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.storage_client = storage.Client(credentials=self.credentials)
    
    def _get_blob(self, bucket_name: str, blob_name: str):
        """Récupère un blob GCS."""
        bucket = self.storage_client.bucket(bucket_name)
        return bucket.blob(blob_name)
    
    def generate_signed_url(self, bucket_name: str, blob_name: str, 
                          method: str = "GET", 
                          expiration_minutes: int = 15,
                          content_type: Optional[str] = None) -> str:
        """
        Génère une URL signée v4 pour un blob.
        
        Args:
            bucket_name: Nom du bucket
            blob_name: Nom du blob
            method: Méthode HTTP ("GET" ou "PUT")
            expiration_minutes: Durée de validité en minutes
            content_type: Type de contenu pour les uploads
        """
        blob = self._get_blob(bucket_name, blob_name)
        
        url_params = {
            "version": "v4",
            "expiration": datetime.timedelta(minutes=expiration_minutes),
            "method": method,
        }
        
        if content_type:
            url_params["content_type"] = content_type
            
        return blob.generate_signed_url(**url_params)

class GCSFileHandler:
    """Gestionnaire de fichiers pour Google Cloud Storage."""
    
    def __init__(self, gcs_client: GCSClient):
        self.gcs_client = gcs_client
    
    @staticmethod
    def parse_gcs_url(gs_url: str) -> Tuple[str, str]:
        """Parse une URL GCS et retourne le bucket et le blob."""
        if not gs_url.startswith("gs://"):
            raise ValueError("Invalid GCS URL format")
        return gs_url[5:].split("/", 1)
    
    def download_file(self, signed_url: str, file_name: str) -> str:
        """Télécharge un fichier depuis une URL signée."""
        response = requests.get(signed_url)
        if response.status_code != 200:
            raise ValueError(f"Download failed: {response.status_code} - {response.text}")
        
        local_path = os.path.join(tempfile.gettempdir(), file_name)
        with open(local_path, 'wb') as temp_file:
            temp_file.write(response.content)
        return local_path
    
    def upload_file(self, signed_url: str, file_path: str) -> None:
        """Upload un fichier vers une URL signée."""
        with open(file_path, 'rb') as file_data:
            headers = {'Content-Type': 'application/octet-stream'}
            response = requests.put(signed_url, data=file_data, headers=headers)
            
            if response.status_code != 200:
                raise ValueError(f"Upload failed: {response.status_code} - {response.text}")

class BucketHandler:
    """Gestionnaire pour le bucket 'safe'."""
    
    def __init__(self, gcs_client: GCSClient, gcs_handler: GCSFileHandler):
        self.gcs_client = gcs_client
        self.gcs_handler = gcs_handler
        
    def extract_etl_info(self, file_path: str) -> str:
        """Extrait les informations ETL du chemin du fichier."""
        match = re.search(r"etl_ds=\d{4}-\d{2}-\d{2}/ingestionId=[A-Z]+", file_path)
        if not match:
            raise ValueError(f"Invalid file path format: {file_path}")
        return match.group(0)
    
    def get_etl_info(self, running_date: str, asset: str) -> str:
        return f"etl_ds={running_date}/ingestionId={asset.upper()}"
    
    def get_parquet_url(self, bucket_type: str, use_case: str, file_source: str, etl_info: str) -> str:
        bucket_prefix = "va-sdh-hq-staging-safe" if bucket_type == "safe" else "va-sdh-hq-staging-apps"
        return f"gs://{bucket_prefix}/{use_case}/{file_source}/{etl_info}/output.parquet"
    
    
def generate_signed_url_and_download(gs_url: str, download_locally: bool = False) -> Tuple[str, Optional[str]]:
    try:
        gcs_client = GCSClient()
        file_handler = GCSFileHandler(gcs_client)
        
        bucket_name, blob_name = file_handler.parse_gcs_url(gs_url)
        file_name = blob_name.split('/')[-1]
        signed_url = gcs_client.generate_signed_url(bucket_name, blob_name)

        if download_locally:
            local_path = file_handler.download_file(signed_url, file_name)
            return signed_url, local_path
        
        return signed_url, None
    except Exception as e:
        raise DataGouvException(
            title="Fetching Document Error",
            description=f"Error generating signed URL or downloading file.<br/>Reason: {e}"
        )
        
def generate_upload_signed_url_v4(bucket_name: str, blob_name: str, file_path: str):
    try:
        """Génère une URL signée v4 et upload un fichier."""
        gcs_client = GCSClient()
        file_handler = GCSFileHandler(gcs_client)

        signed_url = gcs_client.generate_signed_url(
            bucket_name=bucket_name,
            blob_name=blob_name,
            method="PUT",
            content_type="application/octet-stream"
        )

        file_handler.upload_file(signed_url, file_path)
        return signed_url
    except Exception as e:
        raise("An error occurred during file upload:", e)

def insert_file_into_bucket(bucket_type: str, asset: AssetTypes, use_case: str, file_name: str, file_source: str, parquet_file_path: str) -> str:
    try:
        gcs_client = GCSClient()
        file_handler = GCSFileHandler(gcs_client)
        bucket_handler = BucketHandler(gcs_client, file_handler)
        
        etl_info = bucket_handler.extract_etl_info(parquet_file_path)
        url = bucket_handler.get_parquet_url(bucket_type, use_case, file_source, etl_info)
        print("insert_file_into_bucket", url)
        
        bucket_name, blob_name = file_handler.parse_gcs_url(url)
        signed_url = gcs_client.generate_signed_url(
            bucket_name, blob_name, 
            method="PUT", 
            content_type="application/octet-stream"
        )
        
        file_handler.upload_file(signed_url, parquet_file_path)
        return url
    except Exception as e:
        raise DataGouvException(
            title="Bucket Upload",
            description=f"Bucket Upload Error: {str(e)}"
        )

def insert_file_into_safe_bucket(asset: AssetTypes, use_case: str, file_name: str, file_source: str, parquet_file_path: str) -> str:
    return insert_file_into_bucket("safe", asset, use_case, file_name, file_source, parquet_file_path)

def insert_file_into_tmp_bucket(asset: AssetTypes, use_case: str, file_name: str, file_source: str, parquet_file_path: str) -> str:
    return insert_file_into_bucket("tmp", asset, use_case, file_name, file_source, parquet_file_path)

def download_file_from_tmp_bucket(asset: AssetTypes, use_case: str, file_source: str, running_date: str) -> Tuple[str, str]:
    try:
        gcs_client = GCSClient()
        file_handler = GCSFileHandler(gcs_client)
        bucket_handler = BucketHandler(gcs_client, file_handler)
        
        etl_info = bucket_handler.get_etl_info(running_date, asset.value)
        tmp_url = bucket_handler.get_parquet_url("tmp", use_case, file_source, etl_info)
        print("download_file_from_tmp_bucket", tmp_url)
        bucket_name, blob_name = file_handler.parse_gcs_url(tmp_url)
        
        signed_url = gcs_client.generate_signed_url(bucket_name, blob_name)
        local_path = file_handler.download_file(signed_url, "output.parquet")
        
        return local_path
    except Exception as e:
        return None