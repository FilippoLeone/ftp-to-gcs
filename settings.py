import sys
import os

bucket_name = 'production-dataset'
service_account_path = 'service_account.json'
naming_regex = r"([a-z]+)\-([a-z]+)\-([a-z]+)\-([0-9]+)\-([0-9]+)\.(zip|csv|tsv)"

if sys.platform == 'win32':
    ftp_path = os.getcwd() 
else:
    ftp_path = "/tmp"

ftp_permissions = 'elradfmwMT'
ftp_port = 6969
ftp_ip = '0.0.0.0'
ftp_max_cons = 256
ftp_max_cons_per_ip = 5
ftp_welcome_message = 'PyFTP ingestion to GCS'