import requests
from datetime import date

USERNAME = "arun-dvlpr01123"
TOKEN = "gfyuuihkjh9u98789"
GRAPH_ID = "codinggraph01123"
TODAY = date.today().strftime('%Y%m%d')
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


json_param = {
    "token": "gfyuuihkjh9u98789",
    "username": "arun-dvlpr01123",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=ENDPOINT, json=json_param)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
post_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint =f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
graph_config = {
    "id":"codinggraph01123",
    "name":"Coding Habit Tracker",
    "unit":"minutes",
    "type":"int",
    "color":"momiji"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
#
# response = requests.post(url= graph_endpoint,json=graph_config,headers=headers)
# print(response.status_code)

post_config = {
    "date":TODAY,
    "quantity":input("HOw many minutes did you Practice coding"),
    "optionalData":"{\"ChapterCompleted\":\"1\"}"
}

update_config = {
    "quantity":"60",
    "optionalData":"{\"ChapterCompleted\":\"0.8\"}"
}

response = requests.post(url=post_graph_endpoint,json=post_config,headers=headers)
print(response.json())

# response = requests.put(url=update_endpoint,json=update_config,headers=headers)
# print(response.text)
