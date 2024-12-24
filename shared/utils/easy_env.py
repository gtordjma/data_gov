from easyenvi import EasyEnvironment

easy_env = EasyEnvironment(
    local_path='',
    gcloud_project_id='va-sdh-hq-staging',
    GCS_path='gs://va-sdh-hq-staging-lab/generative-analytics/',
    gcloud_credential_path='GCP_credentials.json'
)
