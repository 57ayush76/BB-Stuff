import re
import requests

domain = input("Enter domain: ")
headers = {'APIKEY': 'YOUR-API-KEY-HERE'}
response = requests.get(f"https://api.securitytrails.com/v1/domain/{domain}/subdomains", headers=headers)
text = response.text

pattern = r'"([a-z0-9-]+)"'
subdomains = re.findall(pattern, text)
count = len(subdomains)
print("Total subdomains found:", count)
for i in range(len(subdomains)):
    print(f"{subdomains[i]}.{domain}")
with open("security-tr-subs.txt", "w") as file:
    for i in range(len(subdomains)):
        file.write(f"{subdomains[i]}.{domain}\n")
