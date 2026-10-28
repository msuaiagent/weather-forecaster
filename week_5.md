# Week 5: Autoregressive Predictions and Streamlit Deployment

Welcome back to the Weather Forecaster project! Last week, we explored some methods to improve our model's performance by visualizing feature importance, conducting hyperparameter tuning, and performing feature selection. This week, we will be focusing on two main topics: implementing autoregressive predictions and deploying our model using Streamlit.

## 1. Autoregressive Predictions

Currently, our model is trained to make predictions for the next timestep based on the input features provided for a current timestep. However, in many real-world scenarios, we may want to make predictions for multiple future timesteps (like predicting the weather for the next 24 hours). This is where autoregressive predictions come into play. Autoregressive predictions involve using the model's previous predictions as input features for making future predictions.

### 1.1 Understanding Autoregressive Predictions

Let's say we have features X at a current timestep t, and we want to predict the target features Y for the next timestep t+1. Once we have made the prediction for Y at t+1, we can use that prediction as the input features for predicting Y at t+2, and so on. This allows us to make predictions for multiple future timesteps by iteratively using the model's previous predictions.

We start with the features at timestep t, denoted as X_t, and want to predict the target features Y at an upcoming timestep t+k (and all the timesteps in between), and we represent our model as a function f that takes in the features X and outputs the predictions Y. The process can be represented as follows:

$$Y_{t+1} = f(X_t)$$

$$X_{t+1} \leftarrow Y_{t+1}$$

$$Y_{t+2} = f(X_{t+1}) = f(Y_{t+1})$$

$$X_{t+2} \leftarrow Y_{t+2}$$

$$Y_{t+3} = f(X_{t+2}) = f(f(Y_{t+1}))$$

In general, for any step $k \ge 1$:

$$Y_{t+k} = f(X_{t+k-1}) \quad \text{where} \quad X_{t+k-1} = Y_{t+k-1}$$

I hope you don't get confused with all the notation and how we're setting X and Y for each timestep. The main idea is that we are using the model's previous predictions as input features for making future predictions, which allows us to make predictions for multiple future timesteps while only having a model that is trained to make predictions for the next timestep!

### 1.2 Implementing Autoregressive Predictions

Now that we understand the concept of autoregressive predictions, let's actually implement it in our project! We'll create a function that takes in the model, the current weather data (this will be implemented later), and the number of future timesteps we want to predict, and returns the predictions for those future timesteps. The function will iteratively use the model's previous predictions as input features for making future predictions (autoregressive!).

Inside the *src* directory, create a new file called *autoregressive.py* and implement the function as follows:

```python
def predict_autoregressive(model, current_weather, steps=1):
```

Now, we'll want to create a list to store the predictions for each future timestep. We'll also want to create a variable X to store the current input features. Because we're starting with raw weather data (again, we'll get into this more later), we'll need to process it using the function we defined in Week 3 to turn it into the desired input features.

```python
    predictions = []
    
    X = process_data(current_weather)
    X_drops = ["date", "year"]
    X = X.drop(columns=X_drops)
```

*Note: Make sure to import the process_data() function at the top of your file. (Hint: from src.data_processor import process_data). Also, notice how we're dropping the "date" and "year" columns from the input features like we did when prepping the data for training.*

Next, we'll need to setup a day of the year variable and hour of the day variable to keep track of the current timestep as we iterate through the future timesteps (this is because we used those two variables as features in our model). We're also going to setup a variable to track the current weather state, which will be updated with the model's previous predictions as we iterate through the future timesteps.

```python
    day_of_year = X["day_of_year"].values[0]
    hour_of_day = X["hour_of_day"].values[0]
    
    X_input = X.copy()
    X_index = X_input.index[0]
```

*Note: Because we're working with pandas DataFrames, we need to be careful about how we reference the index of the DataFrame. In this case, we're using the index of the first row of the DataFrame and updating it as we iterate through the future timesteps. This is important because it ensures that we're always working with the correct row of the DataFrame.*

As the last part of the setup before the loop, we need to create a list of the target columns that we want to predict. This will be used to update the input features with the model's previous predictions as we iterate through the future timesteps. If you remember, we did something similar when we were prepping the data for training, where we created a list of the target columns that we wanted to predict. We'll do the same thing here since the input and output features are the same except for the "day_of_year" and "hour_of_day" columns, which are used as features in the model input but not output.

```python
    target_cols = [col for col in X_input.columns if col not in ["day_of_year", "hour_of_day"]]
```

*Note: This code uses a list comprehension to create a list of the target columns that we want to predict. It iterates through the columns of the input DataFrame and adds them to the list if they are not "day_of_year" or "hour_of_day".*

Alright, now for the interesting part! We'll create a loop that iterates through the number of future timesteps we want to predict. Inside the loop, we'll set the "day_of_year" and "hour_of_day" columns in the input features to the current timestep, make a prediction using the model, and then add the model's prediction to the list of predictions.

```python
    for _ in range(steps):
        X_input.loc[X_index, "day_of_year"] = day_of_year
        X_input.loc[X_index, "hour_of_day"] = hour_of_day
        
        Y_pred = model.predict(X_input)
        Y_pred_values = Y_pred[0]
        predictions.append(Y_pred_values)
```

*Note: The .loc indexer is used to access and modify specific cells in the DataFrame. This is where the X_index is used to reference the specific row in the DataFrame.*

Then, we'll update the input features with the model's previous predictions for the next iteration of the loop. This is where the autoregressive part comes into play, as we're using the model's previous predictions as input features for making future predictions.

```python
        for i, col in enumerate(target_cols):
            X_input.loc[X_index, col] = Y_pred_values[i]
        
        hour_of_day += 1
        if hour_of_day > 23:
            hour_of_day = 0
            day_of_year += 1
            if day_of_year > 365:
                day_of_year = 1
    
    return predictions
```

*Note: The hour_of_day and day_of_year variables are updated to keep track of the current timestep as we iterate through the future timesteps. If the hour_of_day exceeds 23, it is reset to 0 and the day_of_year is incremented by 1. If the day_of_year exceeds 365, it is reset to 1.*

### 1.3 Testing Autoregressive Predictions

Alright, that was some pretty complicated code! Now, let's test it! But instead of using some random weather data, let's use the most recent weather data from the Open-Meteo API. This will allow us to see how our model performs on real-world data that it has never seen before. We'll also be able to see how well our model can make predictions for multiple future timesteps using autoregressive predictions.

What's nice is that we'll basically be using the exact same download.py script that we used in Week 2 to download the weather data, but instead of downloading a large amount of data, we'll just download the most recent weather data (the last hour) and use that as the input features for our autoregressive predictions. Now, the thing is that the Open-Meteo API doesn't allow us to download the most recent weather data, but it does allow us to download the weather data for the previous day. So, we'll just download the weather data for the previous day and use that as the input features for our autoregressive predictions.

What you'll need to do is create a new function in your *autoregressive.py* script called *get_current_weather()*. This function will download the weather data for the previous day and return the most recent hour of weather data as a pandas DataFrame. The function should look something like this (this is using the default download.py script that was used in Week 2, but with some modifications to download the weather data for the previous day and return the most recent hour of weather data). You should adjust yours accordingly to match your download.py script, but the main idea is to download the weather data for the previous day and return the most recent hour of weather data as a pandas DataFrame.:

```python
def get_current_weather():
    yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
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
        "start_date": yesterday_date,
        "end_date": yesterday_date,
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
```

*Note: Remember to import the datetime module at the top of your file! The changes you should make to your download script are to add the yesterday_date variable at the top and calculate it using the datetime module functions, use the yesterday_date variable in your API request, and return the last row of the resulting DataFrame (most recent hour).*

Now, go back to your *main.py* file and import the *predict_autoregressive()* and *get_current_weather()* function from the *autoregressive.py* file similar to how you imported the other functions. Then, call the *get_current_weather()* function to get the most recent weather data from the Open-Meteo API, and pass that data to the *predict_autoregressive()* function along with your trained model and the number of future timesteps you want to predict. Finally, print out the predictions for each future timestep (in this example, we only looked at temperature).

```python
    current_weather = get_current_weather()
    predictions = predict_autoregressive(model, current_weather, steps=72)
    
    print("Predictions for the next 72 hours (t2m):")
    for i, pred in enumerate(predictions):
        print(f"Hour {i + 1}: {pred[0]} °C")
```

Hopefully you should see some predictions for the next 72 hours (3 days) of temperature! You can also try changing the number of future timesteps to predict and see how your model performs on different time horizons. You can also try predicting other weather variables by changing the index of the prediction array (pred[0] is temperature, pred[1] is apparent temperature, etc.). Now, if you compare these values with weather data from other sources, you may notice that the predictions seem like they're either delayed or ahead. One thing to keep in mind is that the Open-Meteo API provided weather data based on the UTC timezone, so you may need to adjust the predictions based on your local timezone.

## 2. Streamlit Deployment

Instead of just running our model in a Python script, we can deploy it using Streamlit to make it accessible to users through a web application. Streamlit is an open-source app framework that allows us to create interactive web applications for machine learning and data science projects with minimal effort! That way, we don't need to deal with the complexities of web development, and we can just focus on building a user-friendly interface for our weather forecaster project.

### 2.1 Introduction to Streamlit

I think the best way that you can get started with Streamlit is to watch a video tutorial. [This video](https://www.youtube.com/watch?v=d7fnzDQ5qM8) is a great guide to get started with Streamlit. It covers the basics of how to create a simple web application using Streamlit, some of the syntax, and how to actually deploy the app. It's a bit long, but there are definitely some sections you don't need to watch if you just want to get started with Streamlit. I would mainly look at the parts where they go over the syntax and format for your app as well as the parts where they go over how to deploy your app.

The official documentation for Streamlit is also a great resource to learn more about the different components and features that Streamlit offers. You can find the documentation [here](https://docs.streamlit.io/). Other than that, I'd highly recommend just playing around with Streamlit and trying to create your own web application. The best way to learn is by doing!

### 2.2 Approaching the UI

When approaching the UI for our Streamlit application, we should consider the user experience and make sure that the application is easy to use and provides a good visual representation of the weather forecast data. We can use various Streamlit components such as text elements, metrics, dataframes, and charts to display the information in a clear and organized manner.

Because the UI is very subjective, I would recommend that you try to come up with your own design for the UI. However, I will provide some rough tips and suggestions for how to approach the UI design and implementation:
- First, mockup a rough sketch of what you want your UI to look like. This can be done on paper or digitally. The goal is to have a visual representation of what you want your UI to look like before you start coding. For example, here's a rough sketch of what my UI looks like (this is just an example, feel free to come up with your own design!):
![UI Sketch](./../imgs/streamlit_mockup.png)
- Next, think about the different components that you want to include in your UI. For example, you may want to include a text element that displays the current weather conditions, a metric that displays the temperature, a dataframe that displays the weather forecast for the next 72 hours, and a chart that visualizes the temperature over time. You can use various Streamlit components to achieve this.
- As for the actual coding of the UI, there are some things you can do that would help especially for this project:
    - Use helper functions before the main() function to organize your code and make it more readable. For example, you can use some of the helper functions like *get_current_weather()* and *predict_autoregressive()* that we defined earlier to download the weather data and make predictions. You can also create a function to load the model and return it.
    - You can use the *st.cache_data* decorator to cache the results of your functions that download and process the weather data as well as loading the model. This will help speed up your application and reduce the number of API calls made to the Open-Meteo API.

Here's some example code that shows how to load the model and import the necessary functions from the *autoregressive.py* file. One important thing to note is that because the *main.py* file is in the root directory and the *autoregressive.py* file is in the *src* directory, we need to add the root directory to the system path so that we can import the functions from the *autoregressive.py* file.

```python
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.autoregressive import get_current_weather, predict_autoregressive
```

And here's an example of how to load the model using the *st.cache_resource* decorator to cache the model and speed up the application.

```python
@st.cache_resource
def get_model():
    local_path = Path("models/weather_model.pkl")
    root_model_path = ROOT_DIR / "models" / "weather_model.pkl"

    model_path = local_path if local_path.exists() else root_model_path

    return joblib.load(model_path)
```

*Note: Make sure to always import everything you need at the top of your file!*

From there, I wish you luck with implementing your own Streamlit application! Remember to keep the user experience in mind and make sure that the application is easy to use and provides a good visual representation of the weather forecast data. Personally, I think it's also fine to use other online resources and LLMs to help you with the implementation of your Streamlit application. There are many resources available online that can help you with the different components and features that Streamlit offers. You can also use LLMS to help you with the coding and implementation of your Streamlit application.

*Warning: Always make sure you know what you're code is doing when you use AI to assist with your development. It can be an extremely helpful tool to learn and implement some of the stuff you might not be familiar with, however, it's important to always double-check the code and make sure it's doing what you expect it to do. It's very easy to just go with whatever the AI model says and accept it without question, but this can lead to problems if you aren't closely monitoring the exact implementation details. In my opinion, if you aren't able to explain what a piece of code does on your own, you shouldn't use it in your project.*

## 3. Next Steps

Great job this week! This week had some really important concepts for how we actually use our model to make predictions for multiple future timesteps, as well as how to deploy our model using Streamlit make it accessible to users. Hopefully you have a fully working Streamlit application that allows users to forecast weather for multiple future timesteps! Next week, we will be focusing on improving our model's performance as much as possible and discuss coming up with a novel idea for your weather forecaster project!

If you have some extra time this week, I would recommend trying to add more features or functionality to your Streamlit website. This could be adding more visualizations, adding more interactivity, or even adding more information about the weather forecast. The goal is to make your Streamlit website as user-friendly and informative as possible!

Feel free to reach out if you have any questions or need any help with the instructions. Also, make sure to attend the guided project checkpoint to get any help or get any questions answered, work with others also doing the same project, and be eligible for the competition at the end of the semester!
