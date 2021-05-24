import json

from requests import get, post

data = {
        "app_id": "443810",
        "nickname": "jholxpert",
        "comment": "Yes"
        }
response = post("https://game-store-processing-endpoint.azurewebsites.net/api/recordcomment",
                 headers={"x-functions-key": "FamztMfa9LYuTCrY2/PmZ9pN/NB5a8khmaeLREIIYlfBjiA9edf1oQ=="},
                 data=json.dumps(data))
print(response)