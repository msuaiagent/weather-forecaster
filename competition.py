import datetime
import joblib
from pathlib import Path
from sklearn.metrics import root_mean_squared_error

from src.autoregressive import predict_autoregressive


COMPETITION_DATE_START = datetime.datetime(2026, 11, 15, 0, 0, 0).strftime("%Y-%m-%d")
COMPETITION_DATE_END = datetime.datetime(2026, 11, 17, 0, 0, 0).strftime("%Y-%m-%d")
INITIAL_DATE = datetime.datetime(2026, 11, 14, 0, 0, 0).strftime("%Y-%m-%d")


def get_true_weather(start_date, end_date):
    import openmeteo_requests
    
    import pandas as pd
    import requests_cache
    from retry_requests import retry
    
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 42.7234,
        "longitude": -84.4814,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m"],
    }
    responses = openmeteo.weather_api(url, params = params)
    
    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
    
    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    
    hourly_data = {
        "date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )
    }
    
    hourly_data["temperature_2m"] = hourly_temperature_2m
    
    hourly_dataframe = pd.DataFrame(data = hourly_data)
    print("\nHourly data\n", hourly_dataframe)
    
    return hourly_dataframe


def score(true_weather, predicted_weather):
    print(f"True weather timeseries length: {len(true_weather)}, Predicted weather timeseries length: {len(predicted_weather)}")
    
    # print("True weather:\n", true_weather)
    # print("Predicted weather:\n", predicted_weather)
    
    # TODO: If you changed the order of the features in your model, make sure to change the index below from 0 to match the column index of the target variable (t2m) in your predicted_weather list
    rmse = root_mean_squared_error(true_weather.iloc[:, 1], [variables[0] for variables in predicted_weather])
    
    print(f"RMSE (Root Mean Squared Error) between true and predicted weather: {rmse:.4f}")
    print(f"Congrats! Your final competition score is {rmse:.4f}. Please submit this score to Jack Gunn via Discord along with a description or link to your novel idea and/or website for judging!")


### EDIT THE TODOs BELOW TO USE YOUR MODEL AND DATA PROCESSING FOR THE COMPETITION SCRIPT ###
### Also, remember to run this script from the root of the repository so that the imports work correctly ###


# TODO: Edit this path to point to your trained model
MODEL_PATH = Path("models/weather_model_tuned.pkl")


# TODO: Edit this function to match whatever your get_current_weather() function from autoregressive.py is
#       except be sure that the start_date and end_date is equal to INITIAL_DATE
def get_current_weather():
    import openmeteo_requests
    
    import pandas as pd
    import requests_cache
    from retry_requests import retry
    
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 42.7234,
        "longitude": -84.4814,
        "start_date": INITIAL_DATE,
        "end_date": INITIAL_DATE,
        "hourly": ["temperature_2m", "apparent_temperature", "relative_humidity_2m", "dew_point_2m", "precipitation", "cloud_cover", "cloud_cover_low", "soil_temperature_0_to_7cm", "soil_moisture_0_to_7cm", "surface_pressure", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m", "pressure_msl", "shortwave_radiation"],
    }
    responses = openmeteo.weather_api(url, params = params)
    
    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
    
    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_apparent_temperature = hourly.Variables(1).ValuesAsNumpy()
    hourly_relative_humidity_2m = hourly.Variables(2).ValuesAsNumpy()
    hourly_dew_point_2m = hourly.Variables(3).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(4).ValuesAsNumpy()
    hourly_cloud_cover = hourly.Variables(5).ValuesAsNumpy()
    hourly_cloud_cover_low = hourly.Variables(6).ValuesAsNumpy()
    hourly_soil_temperature_0_to_7cm = hourly.Variables(7).ValuesAsNumpy()
    hourly_soil_moisture_0_to_7cm = hourly.Variables(8).ValuesAsNumpy()
    hourly_surface_pressure = hourly.Variables(9).ValuesAsNumpy()
    hourly_wind_speed_10m = hourly.Variables(10).ValuesAsNumpy()
    hourly_wind_direction_10m = hourly.Variables(11).ValuesAsNumpy()
    hourly_wind_gusts_10m = hourly.Variables(12).ValuesAsNumpy()
    hourly_pressure_msl = hourly.Variables(13).ValuesAsNumpy()
    hourly_shortwave_radiation = hourly.Variables(14).ValuesAsNumpy()
    
    hourly_data = {
        "date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )
    }
    
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["apparent_temperature"] = hourly_apparent_temperature
    hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
    hourly_data["dew_point_2m"] = hourly_dew_point_2m
    hourly_data["precipitation"] = hourly_precipitation
    hourly_data["cloud_cover"] = hourly_cloud_cover
    hourly_data["cloud_cover_low"] = hourly_cloud_cover_low
    hourly_data["soil_temperature_0_to_7cm"] = hourly_soil_temperature_0_to_7cm
    hourly_data["soil_moisture_0_to_7cm"] = hourly_soil_moisture_0_to_7cm
    hourly_data["surface_pressure"] = hourly_surface_pressure
    hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
    hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
    hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m
    hourly_data["pressure_msl"] = hourly_pressure_msl
    hourly_data["shortwave_radiation"] = hourly_shortwave_radiation
    
    hourly_dataframe = pd.DataFrame(data = hourly_data)
    print("\nHourly data\n", hourly_dataframe)
    
    return hourly_dataframe.tail(1)


if __name__ == "__main__":
    model = joblib.load(MODEL_PATH)
    X = get_current_weather()

    Y_predicted = predict_autoregressive(model, X, steps=72)
    Y_actual = get_true_weather(COMPETITION_DATE_START, COMPETITION_DATE_END)
    score(Y_actual, Y_predicted)
