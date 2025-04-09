import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
from tqdm import tqdm
import logging

# === CONFIGURATION ===
USERNAME = "..." #DataCite Username
PASSWORD = "..." #DataCite Password
CSV_FILE = "dois_to_update.csv"  # must contain 'doi' and 'url' columns
DATACITE_API_BASE = "https://api.datacite.org/dois"
LOG_FILE = "doi_update_log.txt"
DRY_RUN = True  # Set to False to actually send updates

# === SET UP LOGGING ===
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === LOAD CSV ===
df = pd.read_csv(CSV_FILE, sep=';')

# === FUNCTION TO UPDATE DOI ===
def update_doi_url(doi, new_url):
    payload = {
        "data": {
            "id": doi,
            "type": "dois",
            "attributes": {
                "url": new_url
            }
        }
    }

    if DRY_RUN:
        logging.info(f"DRY RUN: Would update {doi} → {new_url}")
        return 200, "Dry run – no request sent"

    response = requests.put(
        f"{DATACITE_API_BASE}/{doi}",
        json=payload,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers={"Content-Type": "application/vnd.api+json"}
    )

    return response.status_code, response.text

# === MAIN LOOP ===
print("Starting DOI updates...\n")
for index, row in tqdm(df.iterrows(), total=len(df), desc="Updating DOIs"):
    doi = row["doi"]
    new_url = row["url"]
    status_code, response_text = update_doi_url(doi, new_url)

    log_message = f"{doi} → {new_url} | Status: {status_code}"
    if status_code != 200:
        logging.error(f"{log_message} | Error: {response_text}")
        print(f"❌ {log_message}")
    else:
        logging.info(log_message)
        print(f"✅ {log_message}")

print("\nDone! Check the log file for full details:", LOG_FILE)