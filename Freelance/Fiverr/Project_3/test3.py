import os
import json
import hashlib
import requests
import time
from requests.auth import HTTPBasicAuth
import urllib3
from sentence_transformers import SentenceTransformer

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize the sentence transformer model
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def file_md5_checksum(file_path):
    """Compute the MD5 checksum of a file."""
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

def is_file_uploaded(file_path, checksum, uploaded_files):
    """Check if the file has already been uploaded or modified."""
    return file_path in uploaded_files and uploaded_files[file_path] == checksum

def update_uploaded_files(file_path, checksum, uploaded_files):
    """Update the uploaded files dictionary with the file path and its checksum."""
    uploaded_files[file_path] = checksum

def load_log_data_to_opensearch(folder_path, opensearch_url, index_name, doc_type="_doc", interval=60):
    uploaded_files = {}

    while True:
        for file in os.listdir(folder_path):
            if file.endswith(".log"):
                file_path = os.path.join(folder_path, file)
                file_checksum = file_md5_checksum(file_path)

                # Check if the file is not uploaded or modified
                if not is_file_uploaded(file_path, file_checksum, uploaded_files):
                    with open(file_path, "r") as log_file:
                        for line_number, line in enumerate(log_file, start=1):
                            try:
                                # Compute the log line embedding
                                embedding = model.encode(line.strip())
                                
                                log_data = {
                                    "message": line.strip(),
                                    "meta": {
                                        "file_name": file,
                                        "line_number": line_number,
                                    },
                                    "embedding": embedding.tolist()
                                }

                                # Generate a unique ID based on the file name and line number
                                log_id = f"{file}-{line_number}"
                                auth = HTTPBasicAuth('admin', 'admin')
                                response = requests.put(
                                    f"{opensearch_url}/{index_name}/{doc_type}/{log_id}",
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps(log_data),
                                    verify=False,
                                    auth=auth
                                )
                                response.raise_for_status()

                                # Print the uploaded document's details
                                print(f"Uploaded document: {file} - Line {line_number}")

                            except Exception as e:
                                print(f"Error while loading data: {e}")
                    update_uploaded_files(file_path, file_checksum, uploaded_files)

        # Sleep for the specified interval before checking for new or modified files
        time.sleep(interval)



if __name__ == "__main__":
    data_folder = "Project_3/data/"
    opensearch_url = "https://127.0.0.1:9200"
    index_name = "log-index"
    check_interval = 60  # Check for new or modified files every 60 seconds
    load_log_data_to_opensearch(data_folder, opensearch_url, index_name, interval=check_interval)