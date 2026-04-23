from datetime import datetime, timezone


def kelvin_to_fahrenheit(temp_kelvin: float) -> float:
    return round((temp_kelvin - 273.15) * 9 / 5 + 32, 2)


def transform_weather_data(data: dict) -> dict:
    city = data["name"]
    weather_description = data["weather"][0]["description"]

    timezone_offset = data.get("timezone", 0)

    transformed_data = {
        "City": city,
        "Description": weather_description,
        "Temperature (F)": kelvin_to_fahrenheit(data["main"]["temp"]),
        "Feels Like (F)": kelvin_to_fahrenheit(data["main"]["feels_like"]),
        "Minimum Temp (F)": kelvin_to_fahrenheit(data["main"]["temp_min"]),
        "Maximum Temp (F)": kelvin_to_fahrenheit(data["main"]["temp_max"]),
        "Pressure": data["main"]["pressure"],
        "Humidity": data["main"]["humidity"],
        "Wind Speed": data["wind"]["speed"],
        "Time of Record": datetime.fromtimestamp(
            data["dt"] + timezone_offset, tz=timezone.utc
        ).isoformat(),
        "Sunrise (Local Time)": datetime.fromtimestamp(
            data["sys"]["sunrise"] + timezone_offset, tz=timezone.utc
        ).isoformat(),
        "Sunset (Local Time)": datetime.fromtimestamp(
            data["sys"]["sunset"] + timezone_offset, tz=timezone.utc
        ).isoformat(),
    }

    return transformed_data
