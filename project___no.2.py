import requests
# import os
# from datetime import datetime

# usar_api= os.environ['6b2c453784f528b0c9cff410e71bd9fd']
usar_api="6b2c453784f528b0c9cff410e71bd9fd"
location=("Enter the city name:")

#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

compile_api_link = "https://api.openweathermap.org/data/2.5/weather?"+"&q="+location+"&appid="+usar_api

api_link= requests.get(compile_api_link)
api_data= api_link.json()

print(api_data)
