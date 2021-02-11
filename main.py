import requests
import datetime as dt
import webbrowser

# time
current_time = dt.datetime.now()
formatted_date = current_time.strftime("%d/%m/%Y")
formatted_current_time = current_time.strftime("%X")
# API ID & KEY for exercise
API_ID = "883b0700"
API_KEY = "fb685c9aca5a9fa2e39737e96360a08b"

# Exercise params constant
MY_GENDER = "male"
MY_WEIGHT_KG = 70
MY_HEIGHT_CM = 170
MY_AGE = 28

# header
header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

# query input, you input the answer of the question.
query = input("What exercise did you do today? ")

# the nutritionix endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# parameters of the exercise endpoint
parameters = {
 "query": query,
 "gender": MY_GENDER,
 "weight_kg": MY_WEIGHT_KG,
 "height_cm": MY_HEIGHT_CM,
 "age": MY_AGE
}
# accessing the nutritionix to use their API with their required parameters
response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
print(response.raise_for_status())
exercise_data = response.json()
print(exercise_data)

# workout params

workout_params = {
    "workout": {
        "date": formatted_date,
        "time": formatted_current_time,
        "exercise": exercise_data["exercises"][0]["user_input"].title(),
        "duration": exercise_data["exercises"][0]["duration_min"],
        "calories": exercise_data["exercises"][0]["nf_calories"]
    }
}

sheety_header = {
    "Authorization": "Bearer watafaktoken"
}

# SHEETY API
sheety_endpoint = "https://api.sheety.co/6288f0e11d039597689a7563340a0c39/workoutTracking/workouts"
sheety_response = requests.post(url=f"{sheety_endpoint}", json=workout_params, headers=sheety_header)
print(sheety_response.raise_for_status())
print(sheety_response.json())

# webbrowser.open("https://docs.google.com/spreadsheets/d/1W0GxRZS4QQpXQW0N8pXTDOKaLqnJGz2BWIwoZMOyxfo/edit#gid=0")