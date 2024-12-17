import requests

base_path = 'https://ganesh-doc-translator.cognitiveservices.azure.com'
key =  '3djuPfw6BZcdQyiD2GoNTupwkHrxs52azvJhQleOqJddskZadoodJQQJ99AKACYeBjFXJ3w3AAAbACOGWkUn'
# route = '?api-version={date}'
constructed_url = base_path
print(constructed_url)
payload= {
    "inputs": [
        {
            "source": {
                "sourceUrl": "https://ganeshtranslatorsa.blob.core.windows.net/ganeshk?sp=racwdli&st=2024-12-06T09:59:05Z&se=2024-12-27T17:59:05Z&spr=https&sv=2022-11-02&sr=c&sig=WG2BsbtaCccYPGG3astRx8pHNZVNDCkan5lwOda2Mog%3D",
                "storageSource": "AzureBlob",
                "language": "en"
            },
            "targets": [
                {
                    "targetUrl": "https://ganeshtranslatorsa.blob.core.windows.net/ganeshk-out?sp=racwdli&st=2024-12-06T10:00:04Z&se=2024-12-27T18:00:04Z&spr=https&sv=2022-11-02&sr=c&sig=W%2BWgz4n5MPpgtoQyb%2Bo4UlB0UU%2Frn4z3KQw8PJgdcW8%3D",
                    "storageSource": "AzureBlob",
                    "category": "general",
                    "language": "es"
                }
            ]
        }
    ]
}
headers = {
  'Ocp-Apim-Subscription-Key': key,
  'Content-Type': 'application/json'
}

response = requests.post(constructed_url, headers=headers, json=payload)

print(f'response status code: {response.status_code}\nresponse status: {response.reason}\nresponse headers: {response.headers}')