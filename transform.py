import re
import zipfile
import settings
from gcs import GCS as cloudstorage
import os 

def process_file(file):
    try:
        GCS = cloudstorage()
        if settings.naming_regex:
            rgx = re.compile(settings.naming_regex)
            bucket_name = file[(settings.ftp_path.__len__() + 1):]
            # Apply naming 
            if rgxresult:=rgx.match(bucket_name):
                if rgxresult.group(6) == 'zip':
                    with zipfile.ZipFile(file) as zipf:
                        zipinformation = zipf.infolist()
                        zipf.extractall()
                    for zipfile in zipinformation:
                        return GCS.upload_blob(f"{rgxresult.group(1)}/{rgxresult.group(3)}/{rgxresult.group(4)}-{rgxresult.group(5)}/{zipfile.filename}", os.path.join(settings.ftp_path, zipfile.filename))
                else:
                    return GCS.upload_blob(f"{rgxresult.group(1)}/{rgxresult.group(3)}/{rgxresult.group(4)}-{rgxresult.group(5)}/{bucket_name}", file)
            else:
                print("Uploading to GCS")
                return GCS.upload_blob(f"other/{file[(settings.ftp_path.__len__() + 1):]}", file)
    except:
        return False