import requests

api_key = "YOUR_OPENWEATHERMAP_API_KEY"
city = input("Enter city name: ").strip()

if not city:
    print("Error: City name cannot be empty.")
    exit()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout:
    print("Error: Request timed out. Please try again.")

if response.status_code == 404:
    print("Error: City not found.")
    exit()

if response.status_code == 401:
    print("Error: Invalid API key.")
    exit()

data = response.json()

temperature_c = data["main"]["temp"]
temperature_f = (temperature_c * 9/5) + 32
humidity = data["main"]["humidity"]
condition = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]

print("\n--- Weather Information ---")
print("City:", city)
print("Temperature:", temperature_c, "°C")
print("Temperature:", round(temperature_f, 2), "°F")
print("Humidity:", humidity, "%")
print("Condition:", condition)
print("Wind Speed:", wind_speed, "m/s")