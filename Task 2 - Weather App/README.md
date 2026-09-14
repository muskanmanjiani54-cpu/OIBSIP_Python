# Task 2 - Weather App

## Objective

The objective of this task was to build a weather application in Python that retrieves and displays real-time weather information for a user-specified city using a weather API.

## Features

- Accepts a city name from the user.
- Retrieves current weather information using OpenWeatherMap API.
- Displays temperature in Celsius and Fahrenheit.
- Displays humidity.
- Displays weather description.
- Displays wind speed.
- Handles empty city input.
- Handles city not found errors.
- Handles invalid API key errors.
- Includes a request timeout for better error handling.

## Technologies Used

- Python
- Requests
- JSON
- OpenWeatherMap API

## Implementation

The application takes a city name as input and sends a request to the OpenWeatherMap API.

The API response is processed and the required weather information is extracted and displayed to the user.

Error handling is included for invalid input, unavailable cities, invalid API keys, and connection timeouts.

## Outcome

A functional weather application was successfully developed and tested. The application retrieves and displays current weather information for valid city names.
