import asyncio
from collections import defaultdict
from datetime import datetime
from functools import partial
import re
from .easy_env import easy_env


async def get_quality_data(use_case: str, asset: str, year: str, month: str):
    try:
        query = f"""
        SELECT *
        FROM `va-sdh-hq-staging.monitoring.sdh_file_status`
        WHERE use_case = '{use_case}'
              AND asset = '{asset}'
              AND EXTRACT(YEAR FROM reception_time) = {year}
              AND EXTRACT(MONTH FROM reception_time) = {month}
        """
        loop = asyncio.get_event_loop()
        query_job = await loop.run_in_executor(None, partial(easy_env.gcloud.BQ.query, query))
        results = await loop.run_in_executor(None, query_job.result)
        rows = [dict(row) for row in results]
        return rows
    except Exception as e:
        print(e)
        return []
    
async def get_quality_data_formatted_from_ingestion(use_case: str, asset: str, year: str, month: str):
    # Exécution de get_quality_data dans un thread pour ne pas bloquer
    quality_data = await get_quality_data(
        use_case, 
        asset, 
        year, 
        month
    )
    
    # Formatage des données
    for entry in quality_data:
        if entry["landing_url"] and entry["landing_url"] != "None":
            final_filename = entry["landing_url"].split("/")[-1]
            entry["final_filename"] = final_filename
            
            date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', final_filename)
            entry["date"] = {
                "year": date_match.group(1),
                "month": date_match.group(2),
                "day": date_match.group(3)
            } if date_match else None
        else:
            entry["final_filename"] = None
            entry["date"] = None

    # Groupement par file_type
    grouped_data = defaultdict(list)
    for entry in quality_data:
        grouped_data[entry["file_type"]].append(entry)

    # Garder l'entrée la plus récente pour chaque type
    result = []
    for entries in grouped_data.values():
        most_recent = max(entries, key=lambda x: (
            x["reception_time"] if isinstance(x["reception_time"], datetime)
            else datetime.strptime(x["reception_time"], '%Y-%m-%d %H:%M:%S')
        ))
        result.append(most_recent)

    return result