import json
from requests import get

# define list with values
dataList = []
params = {}

for i in range(2):
    print(f"Loading {i} page")
    headers = {'x-functions-key': 'eh03n3FOz2KD3JhliTzY1WsORxr2vSbCJiGWYuKPSoAQKbkJz1ylJw=='}
    response = get('https://game-store-core-endpoint.azurewebsites.net/api/ListGames',
                   headers=headers,
                   params=params).json()
    params = {'pagingState': response['pagingState']}
    dataList.append(response)
    print(f"End loading {i} page")
# open output file for writing
with open('db_local_data.txt', 'w') as filehandle:
    json.dump(dataList, filehandle)