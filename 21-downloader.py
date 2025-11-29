import requests

file_url = "https://raw.githubusercontent.com/vishwasks32/ey-we-workspace/refs/heads/main/data.csv"
local_fname = "data.csv"

response = requests.get(file_url)

if response.status_code == 200:
    with open(local_fname, "wb") as fle:
        fle.write(response.content)
    
    print(f"File Downloaded successfully")
else:
    print("Failed to download")