# Week 2: Downloading the Data and Exploratory Data Analysis

Welcome back to the Weather Forecaster project! Last week, we set up our environment and the tools needed to get started. This week, we will be downloading the data from the Open-Meteo API that we need for our project and performing some exploratory data analysis (EDA) to understand the data better.

## 0. Installing Dependencies

Now that your environment is completely set up after last week's instructions, we can move on to the actual project! To start off, download a copy of the **requirements.txt** file in the root of this repository and replace the old one. This file contains all the dependencies that you will need to install in order to run the code for this project. You can install these dependencies by running the following command in your terminal (as explained in the previous week's instructions):

```bash
pip install -r requirements.txt
```

## 1. Downloading the Data

### 1.1 Setting Up the Directories and Files

Next, we'll work on the downloading functionality to gather the data needed for the project. From the root repository, create a new directory named *data*. We'll leave this empty for now as this is our destination folder for our download script. Note: remember to add the *data* directory to your *.gitignore* file so that it is not tracked by Git. This is important because we don't want to track large data files in our repository for a variety of performance and storage reasons.

Next, create another new directory named *utils*. This is where we'll place our download script. Inside the *utils* directory, create a new Python file named *download.py*. This is where we'll write the code to download the data.

### 1.2 Using Open-Meteo

Alright, now that we have our directories and files set up, we can use a resource called **Open-Meteo** to download all the weather data we need.

Open-Meteo is a free weather API that provides historical weather data for any location in the world. It has a variety of different API (application programming interface) endpoints that allow you to access different types of weather data. For this project, we will be using the **Historical Weather API** endpoint. Feel free to look around the Open-Meteo website to understand the different endpoints and the data they provide as it's a great resource for weather data! (However, for this project, we will only be using the Historical Weather API endpoint as that is how the format for the data is structured for this project and the competition at the end of the semester)

Link: [https://open-meteo.com/en/docs/historical-weather-api](https://open-meteo.com/en/docs/historical-weather-api)

There's a lot of different options to pick from, but for this project and its instructions, we will stick to the following parameters for our API request initially (however, as we advance through the project later on, you may want to explore other data options available on the page to improve your model's performance!):

- Latitude: 42.7234
- Longitude: -84.4814
- Start Date: 2016-01-01
- End Date: 2025-12-31
- Hourly Weather Variables:
    - Temperature (2 m)
    - Relative Humidity (2 m)
    - Dewpoint (2 m)
    - Apparent Temperature
    - Precipitation (rain + snow)
    - Sea Level Pressure
    - Surface Pressure
    - Cloud Cover Total
    - Cloud Cover Low
    - Wind Speed (10 m)
    - Wind Direction (10 m)
    - Wind Gusts (10 m)
    - Soil Temperature (0-7 cm)
    - Soil Moisture (0-7 cm)
- Solar Radiation Variables:
    - Shortwave Solar Radiation GHI

Without changing any other settings, these options should create the request to download 10 years of data for the location of East Lansing, MI with 15 different weather variables. Note: We are choosing hourly variables at the moment because our goal is to predict hourly weather data, thus that is the kind of data we should work with. It is possible to implement daily or other time intervals into hourly prediction, but that's something you can try to figure out if you want to once we finish building the initial model!

Now if you scroll down, you should find a section named **API Response**. Select the **Python** option and copy the entire code snippet under **Usage**. This gives you an incredibly convenient way to download all the data using Python.

### 1.3 Creating the Download Script

Go back to your *download.py* file and paste the code snippet you copied from the Open-Meteo website. Then, add on this code snippet to the end of the file to actually save the data to a CSV file in the *data* directory:

```python
# Save the weather data to a CSV file
from pathlib import Path

data_path = Path("data/weather_data.csv")
data_path.parent.mkdir(parents=True, exist_ok=True)
hourly_dataframe.to_csv(data_path, index=False)
```

Note: We are using and will continue to use the pathlib library to handle file paths in this project. This is a great library to use as it makes it easy to work with file paths across different operating systems (Windows, Mac, Linux, etc.) without having to worry about the differences in how file paths are structured on each OS!

Now in your terminal at the root directory of your project, run the *download.py* script to download the data and save it to a CSV file in the *data* directory. You can do this by running the following command:

```bash
python utils/download.py
```

## 2. Exploratory Data Analysis

Alright, now that we have our data downloaded, let's take a look at it and perform some exploratory data analysis (EDA) to understand the data better. EDA is an important step in any data science project as it allows us to understand the structure of the data, identify any potential issues or anomalies, and gain insights that can help us build better models.

[This video](https://www.youtube.com/watch?v=Liv6eeb1VfE&list=PLXhX6b6y_bWTegYvt-ed5SKTmQUtzwOn4&index=4) is a great resource to learn more about EDA and how to perform it in Python. You should watch at least the first 12 minutes of the video to get a good understanding of EDA and the rest of it if you have time as well.

Start by creating a file named *eda.py* in the *utils* directory. This is where we will write the code for our EDA. Copy the following code snippets into your *eda.py* file to get started with EDA. This will be an incredibly simple analysis to start off with to get an idea of what you may be looking for, but I highly recommend that you explore the data further on your own as you will likely find some interesting insights that can help you improve your model's performance later on in the project!

```python
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


data_path = Path("data/weather_data.csv")
df = pd.read_csv(data_path)


# Look at the first day of temperature_2m
df_day1 = df[df["date"] < "2016-01-02"]

print(len(df_day1))

plt.plot(df_day1["date"], df_day1["temperature_2m"])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature 2m for the first day")
plt.show()


# Look at the first week of temperature_2m
df_week1 = df[df["date"] < "2016-01-08"]

print(len(df_week1))

plt.plot(df_week1["date"], df_week1["temperature_2m"])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature 2m for the first week")
plt.show()


# Look at the first month of temperature_2m
df_month1 = df[df["date"] < "2016-02-01"]

print(len(df_month1))

plt.plot(df_month1["date"], df_month1["temperature_2m"])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature 2m for the first month")
plt.show()
```

You should be able to run the *eda.py* script in your terminal just like you did with the *download.py* script. This will generate three plots showing the temperature at 2 meters for the first day, first week, and first month of the data. You can modify the code to look at other variables or different time intervals as you explore the data further.

## 3. Next Steps

Congrats! You've reached the end of this week's instructions. You should now have a good understanding of how to download the data from the Open-Meteo API and perform some basic exploratory data analysis (EDA) on it. In the next week's instructions, we will be focusing on cleaning and preprocessing the data to get it ready for modeling and building our first machine learning model to predict the weather.

This week's instructions are a bit shorter than usual just so that you can focus on truly getting started. However, next week's will be much more dense as there's a lot of ground to cover! But since there's less covered this week, I highly recommend that you do some extra steps to explore the data available further. This will help tremendously as we move into the later parts of the project and will help you build a better model in the end! Here are some suggestions and points to consider as you explore the data further:
- Look at the other variables available from Open-Meteo's database and see if you can find any other interesting variables that you think may help improve your model's performance later. (You may want to hold off on downloading them just yet since the instructions will have assumed you are just using the ones listed earlier. But it's still a great idea to understand what might be available!)
- Examine how the weather variables are actually measured, displayed, and recorded. Understanding how the data is collected and structured can help you make better decisions when it comes to cleaning and preprocessing the data later on.
- Take time to do more EDA on the data. Look for any patterns, trends, or anomalies that may be present in the data. Again, the example in the instructions is very rudimentary and will not capture all the nuances of the data. Consider looking at different time intervals, different variables, and different visualizations to get a better understanding.
- If you still have time, try playing around with the software development tools we're using (Git, your IDE, the terminal, etc.). These are incredibly useful skills to have in any programming environment and can be a great way to improve your workflow and productivity as you work on this project and future projects. For instance, make sure you can understand how to use Git ([here's](https://learngitbranching.js.org/) a great resource I've found to learn some of the more advanced Git commands) and how you can use the terminal to navigate your file system and run different kinds of scripts in different locations.

Great job this week and keep up the good work! Feel free to reach out if you have any questions or need any help with the instructions. Also, make sure to attend the guided project checkpoint to get any help or get any questions answered, work with others also doing the same project, and be eligible for the competition at the end of the semester!
