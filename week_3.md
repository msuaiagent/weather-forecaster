# Week 3: Building a Baseline Model

Welcome back to the Weather Forecaster project! Last week, we downloaded the data we'll be using to train our model from the Open-Meteo API and conducted some exploratory data analysis. This week, we'll focus on building a baseline machine learning model that can predict weather conditions based on the data we collected.

## 1. Processing the Data

First, make sure you're currently in the root directory of your project. In this directory, create a new folder called *src*. This will contain the primary code for our project that handles data processing, model training, and inference. Inside the *src* folder, create a new file called *data_processor.py*. This file will contain the code for processing the data we collected from the Open-Meteo API.

### 1.1 data_processor.py Imports

At the top of the file, import the **pandas** library, which we'll use for data manipulation since it can easily read and write CSV files as well as perform various data transformations.

```python
import pandas as pd
```

### 1.2 Processing Function

We'll need to define a function named *process_data()* that takes in a pandas DataFrame object called df and returns a processed DataFrame. This function will handle any necessary data cleaning, feature engineering, and transformations required to prepare the data for training our model.

To start off, let's add feature data for the day of the year and the hour of the day since that information can be useful for predicting weather conditions. We'll also want to gather the year as a separate variable for future steps. You can use the following code snippet to add these features to the DataFrame (or try it yourself first!).

```python
def process_data(df):
    print("Processing weather data...")
    
    date = pd.to_datetime(df["date"])
    year = date.dt.year
    day_of_year = date.dt.dayofyear
    hour_of_day = date.dt.hour
    
    df["year"] = year
    df["day_of_year"] = day_of_year
    df["hour_of_day"] = hour_of_day
    
    return df
```

Analyzing the code, we first convert the "date" column in the DataFrame to a pandas datetime object. Then, we extract the year, day of the year, and hour of the day from this datetime object and add them as new columns to the DataFrame. Finally, we return the processed DataFrame to be used by the next steps in our project.

*Note: This is a section where you may want to come back after training a baseline model to add more features to the data. For example, you may want to add features for the previous hour's weather state or the average weather state over the past few hours. These features can help the model learn patterns in the data and improve its predictions!*

### 1.3 Splitting the Data

Next, we need to split the data into training and testing sets. This is an important step in machine learning, as it allows us to evaluate the performance of our model on data it hasn't seen yet. If we trained our model on all the data we have and then tested it on that exact same data, we wouldn't get an accurate measure of how well our model can generalize its predictions to new, unseen data (this is a very important concept to understand!). So, we'll split the data into two sets: one for training our model and one for testing it.

One important thing to note in our project is that we want to split the data based on the year. This is a common practice in time series forecasting when the order of the data matters, as it allows us to evaluate how well our model can predict future weather conditions based on past data. For instance, if we randomly split the data, we might end up trying to predict weather in the past based on weather in the future, which doesn't make sense. By splitting the data based on the year, we ensure that our model is trained on data from the past and tested on data from the future, which is a more realistic scenario for weather forecasting. Because we downloaded 10 years worth of data, this means that we'll use 8 of the years for training and 2 for testing (following an 80/20 train/test split).

*Note: The year-based splitting ensures that our model is evaluated on data that is consistent and makes sense for time-series problems. For other problems or models, different splitting strategies may be more appropriate or require different approaches.*

For our model, we will want to try to predict the next weather state based on the current weather state. This means that we will want to shift our target weather state by one hour (since that's the timestep size in the data we downloaded), so that the model is trained to predict the next hour's weather state based on the current hour's weather state. You can use the following code snippet to split the data into training and testing sets (or try it yourself first!).

```python
def split_data(df):
    print("Splitting weather data into training and testing sets...")
    
    X_drops = ["date", "year"]
    Y_drops = ["date", "year", "day_of_year", "hour_of_day"]
    
    X_train = df[df["year"] <= 2023].drop(columns=X_drops)[:-1]
    Y_train = df[df["year"] <= 2023].drop(columns=Y_drops)[1:]
    
    X_val = df[df["year"] >= 2024].drop(columns=X_drops)[:-1]
    Y_val = df[df["year"] >= 2024].drop(columns=Y_drops)[1:]
    
    return X_train, Y_train, X_val, Y_val
```

We make sure to drop the "date" and "year" columns from the input features (X) since they are probably not relevant for predicting the weather state. We also drop the "day_of_year" and "hour_of_day" columns from the target features (Y) since they are not needed for the prediction part of the model since the model will be predicting the next hour's weather state based on the current hour's weather state, and these features are already included in the input features (X). We only want to try to learn relationships between the weather state features and not the time features, since the time features are already known.

Analyzing the code, we first define two lists of columns to drop from the input features (X) and target/output features (Y). We then create the training and validation sets by filtering the DataFrame based on the year and dropping the specified columns. Finally, we return the training and validation sets for both input features and target features.

The reason we drop the last row of the input features and the first row of the target features is because we want to align the input features with the corresponding target features. Since we're trying to predict the next hour's weather state based on the current hour's weather state, we need to shift the target features by one hour. By dropping the last row of the input features and the first row of the target features, we ensure that each input feature corresponds to its correct target feature.

## 2. Training the Model

Now that we have processed and split the data, we can move on to training our baseline model. In this project, we'll be using the XGBoost algorithm, which is a popular and powerful machine learning algorithm for regression and classification tasks. We'll be using the **XGBRegressor** class from the **xgboost** library to create our model. If you'd like to learn more about XGBoost, you can check out [this article](https://www.geeksforgeeks.org/machine-learning/xgboost/) or look at the official documentation.

In the *src* folder, create a new file called *model.py*. This file will contain the code for training our model.

### 2.1 model.py Imports

At the top of the file, import the necessary libraries and dependencies that we'll be using.

```python
import joblib
from sklearn.metrics import root_mean_squared_error
from sklearn.multioutput import MultiOutputRegressor
from xgboost import XGBRegressor
```

### 2.2 Training Function

Inside of the *model.py* file, define a function named *train_model()* that takes in a path to a model and the training sets of input features and target features and returns a trained model. This function will handle the training process for our model.

There are two important parts to creating the model in this project: Creating an instance of the **XGBRegressor** class and wrapping it in a **MultiOutputRegressor** class. The **XGBRegressor** class is used to create an instance of the XGBoost algorithm for regression tasks, while the **MultiOutputRegressor** class is used to handle multi-output regression problems, which is what we have in this project since we are trying to predict multiple weather state features at once. To clarify, if we were only trying to predict one weather state feature (like temperature), we would not need to use the **MultiOutputRegressor** class. However, since we are trying to predict multiple weather state features at once, we need to use the **MultiOutputRegressor** class to handle the prediction of multiple outputs.

The **XGBRegressor** class has many hyperparameters that can be tuned to improve the performance of the model. However, for our baseline model, we will look at just a few of them at the moment.
- **n_estimators**: This hyperparameter controls the number of boosting rounds (or trees) to be built. A higher number of estimators can lead to better performance, but it can also increase the risk of overfitting. For our baseline model, we will set this hyperparameter to 100.
- **learning_rate**: This hyperparameter controls the step size at each iteration while moving toward a minimum of the loss function. A lower learning rate can lead to better performance, but it can also increase the training time. For our baseline model, we will set this hyperparameter to 0.1.
- **max_depth**: This hyperparameter controls the maximum depth of the trees. A higher max depth can lead to better performance, but it can also increase the risk of overfitting. For our baseline model, we will set this hyperparameter to 5.
- **random_state**: This hyperparameter controls the random seed used for reproducibility. You can set this to any number you like. For my implementation, I set this hyperparameter to 42.

Here's a code snippet to create the *train_model()* function (or try it yourself first!). We first need to create the model, train it, and then save it to the specified path using the **joblib** library.

```python
def train_model(model_path, X_train, Y_train):
    print("Training weather model...")
    
    base_model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
    multi_model = MultiOutputRegressor(base_model)
    
    multi_model.fit(X_train, Y_train)
    
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(multi_model, model_path)
    
    return multi_model
```

Analyzing the code, we first create an instance of the **XGBRegressor** class with the specified hyperparameters. We then wrap this instance in a **MultiOutputRegressor** class to handle the multi-output regression problem. Next, we fit the model to the training data using the *fit()* method. Finally, we save the trained model to the specified path in the function input using the **joblib** library (which will save the model in Python's .pkl format) and return the trained model.

### 2.3 Validation Function

Congrats! You've successfully trained your baseline model. Now, we need to evaluate its performance on the validation set. In the *model.py* file, define a function named *validate_model()* that takes in a trained model and the validation sets of input features and target features and returns the root mean squared error (RMSE) of the model's predictions on the validation set (specifically for temperature).

*Note: The RMSE is a common metric used to evaluate the performance of regression models. It measures the average magnitude of the errors between the predicted and actual values (with weighting towards larger errors), with lower values indicating better performance. While we could compute the RMSE for all target features, we will focus on just the temperature feature for this exercise so we don't need to deal with the standardization of values (and since the final competition will primarily measure temperature). If we did measure all target features, we would need to standardize them to ensure that they are on the same scale since different features may have different units and ranges.*

Here's a code snippet to create the *validate_model()* function (or try it yourself first!). We first need to make predictions on the validation set using the trained model and then compute the RMSE between the predicted and actual values of temperature (which if everything is correct is the first column of the validation target set).

```python
def validate_model(model, X_val, Y_val):
    print("Validating weather model...")
    
    Y_pred = model.predict(X_val)
    
    rmse = root_mean_squared_error(Y_val.iloc[:, 0], Y_pred[:, 0])
    
    return rmse
```

## 3. Creating a main.py Entry Point

Awesome job so far! Now that we have processed the data and trained our baseline model, we need to create an entry point for our project. This will allow us to run the code and see how well our model performs on the validation set. In the root directory of your project, create a *main.py* file that will serve as the entry point for our project. This file will contain the main logic for orchestrating the loading of the data, processing it, and training our model. It's important to have a clear entry point for your project, as it will make it easier to run and test your code.

### 3.1 main.py Imports

Within the *main.py* file, we'll start by importing the necessary libraries and dependencies that we'll be using.

```python
import joblib
import pandas as pd
from pathlib import Path

from src.data_processor import process_data, split_data
from src.model import train_model, validate_model
```

*Note: The `from src.data_processor import process_data, split_data` and `from src.model import train_model, validate_model` lines import the necessary functions from the `src` directory. However, one thing to keep in mind is that the paths to these modules should be correct relative to the location of the current directory you're running the code from. For instance, if you're running the code from the root directory of your project, the paths should be correct. If you're running the code from a different directory, you may need to adjust the paths accordingly or change the working directory.*

### 3.2 Loading the Data

In the *main.py* file, we'll now start by loading the weather data and setting up the paths for the model files. We'll again use the **Path** class from the **pathlib** library to create paths for the data and model files. This will make it easier to manage file paths in a platform-independent way.

Here's a code snippet to setup the initial *main.py* format.

```python
if __name__ == "__main__":
    data_path = Path("data/weather_data.csv")
    model_path = Path("models/weather_model.pkl")

    df = pd.read_csv(data_path)
```

*Note: The `if __name__ == "__main__":` line is a common Python idiom that allows us to run the code in the block only when the script is executed directly, and not when it is imported as a module in another script. This is important for ensuring that the code in the block is only executed when we want it to be, and not when we import the functions from this script into another script. While not strictly necessary, it's a good practice to include this line in your main scripts to avoid unexpected behavior when the script is imported as a module.*

Next, we'll process the data and split it into training and validation sets using the functions we defined earlier in the *data_processor.py* file. We'll then check if a trained model already exists at the specified path. If it does, we'll load the model using **joblib**. If it doesn't, we'll train a new model using the training data and save it to the specified path.

```python
    df = pd.read_csv(data_path)
    
    df_processed = process_data(df)
    
    X_train, Y_train, X_val, Y_val = split_data(df_processed)
    
    print("Loading weather model...")
    if not model_path.exists():
        model = train_model(model_path, X_train, Y_train)
    else:
        model = joblib.load(model_path)
```

Finally, we'll validate the model on the validation set and print the RMSE to the console. This will give us an idea of how well our baseline model is performing on the validation set.

```python
    rmse = validate_model(model, X_val, Y_val)
    print(f"Root Mean Squared Error: {rmse}")
```

Analyzing the code, we first load the weather data from the specified path using **pandas**. We then process the data and split it into training and validation sets. Next, we check if a trained model already exists at the specified path. If it does, we load the model using **joblib**. If it doesn't, we train a new model using the training data and save it to the specified path. Finally, we validate the model on the validation set and print the RMSE to the console.

## 4. Next Steps

Hopefully, after running the *main.py* file, you should see an RMSE value printed to the console. This value represents the average magnitude of the errors between the predicted and actual values of temperature on the validation set. I got around 0.6298, so hopefully you got a similar value! This is a good starting point for our baseline model, and we can work on improving it next week!

Congratulations! You've successfully built a baseline model for predicting weather conditions based on the data we collected from the Open-Meteo API. In the next week, we'll focus on improving the performance of our model by tuning hyperparameters, adding more features, and learning about feature importance. Keep up the great work!

If you have some extra time this week, it may be a good idea to look over some of the more conceptual topics we discussed this week, as they are important for understanding how to improve the performance of our model in the future. Maybe take a look at some of the documentation for the functions we used or look up and read about anything that you found confusing or interesting. This will help you better understand the concepts and techniques used in this project and improve your skills as a machine learning practitioner (and make better models!).

Feel free to reach out if you have any questions or need any help with the instructions. Also, make sure to attend the guided project checkpoint to get any help or get any questions answered, work with others also doing the same project, and be eligible for the competition at the end of the semester!
