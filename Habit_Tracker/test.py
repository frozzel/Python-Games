import requests 
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import date

pixela_endpoint = "https://pixe.la/v1/users"

def create_user():
    user_params = {
        "token": os.getenv("PIXELA_TOKEN"),
        "username": os.getenv("USERNAME"),
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)
    
# create_user()

graph_endpoint = f"{pixela_endpoint}/{os.getenv('USERNAME')}/graphs"

def create_graph():
    graph_params = {
        "id": "graph1",
        "name": "Work Out Graph",
        "unit": "Minutes",
        "type": "int",
        "color": "ichou",
    }
    headers = {
        "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
    }
    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)
    
# create_graph()

pixel_creation_endpoint = f"{pixela_endpoint}/{os.getenv('USERNAME')}/graphs/graph1"

def create_pixel(minutes):
    pixel_params = {
        "date": date.today().strftime("%Y%m%d"),
        "quantity": minutes,
    }
    headers = {
        "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
    }
    
    response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
    print(response.text)

# minutes = input("How many minutes did you work out today? ")  
# create_pixel(minutes)

pixel_update_endpoint = f"{pixela_endpoint}/{os.getenv('USERNAME')}/graphs/graph1/{date.today().strftime('%Y%m%d')}"
def update_pixel(minutes):
    pixel_params = {
        "quantity": minutes,
    }
    headers = {
        "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
    }       
    response = requests.put(url=pixel_update_endpoint, json=pixel_params, headers=headers)
    print(response.text)
    
# minutes = input("How many minutes did you work out today? ")
# update_pixel(minutes)

pixel_delete_endpoint = f"{pixela_endpoint}/{os.getenv('USERNAME')}/graphs/graph1/{date.today().strftime('%Y%m%d')}"
def delete_pixel():
    headers = {
        "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
    }
    response = requests.delete(url=pixel_delete_endpoint, headers=headers)
    print(response.text)
    
# delete_pixel()    

print("https://pixe.la/v1/users/frozzel2/graphs/graph1.html")