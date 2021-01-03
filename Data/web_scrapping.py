import requests
from bs4 import BeautifulSoup
import re
import shutil
import os


URL = "http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit/"


def download_data(from_url, local_path):
    r = requests.get(from_url, stream=True)
    with open(local_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

def batch_download(matches):
    for match in matches:
        file_url = os.path.join(URL, match['href'])
        file_local = os.path.join('raw_data', match['href'])
        download_data(file_url, file_local)

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
matches = soup.find_all('a', attrs={"href": re.compile("tgz")})
matches = matches[5758:]
os.chdir(r'Data')
#print(len(matches))
batch_download(matches)
