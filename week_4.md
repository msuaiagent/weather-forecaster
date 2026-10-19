# Week 4: Model Optimization and Finetuning

Welcome back to the Weather Forecaster project! Last week, we created our first baseline weather model to predict the next hour of weather variables given the current state of the weather. This week, we will focus on improving our model's performance by optimizing its hyperparameters and finetuning it to achieve better results. We will also explore techniques for feature selection and engineering to enhance our model's predictive capabilities.

## 1. Visualizing Feature Importance

The first part of this week's instructions will be about selecting the most important features for our model. To do this, we will visualize the importance of each feature in our dataset. This will help us understand which features contribute the most to our model's predictions and which ones you might want to remove to simplify the model. While having a more complex model can sometimes lead to better performance, it can also make the model more difficult to interpret and deploy (or even cause overfitting). By selecting the most important features, we can create a more efficient and effective model that is easier to understand and use.

We'll start off by obtaining and plotting the features our baseline model used. Go to your *model.py* file inside the *src* folder and add the following starter function to visualize the feature importance of your model:

```python
def plot_feature_importances(model, feature_names):
    print("Plotting average feature importances for the weather model...")
```

Now, inside the function, we will obtain the feature importance values from our XGBoost model. One benefit of using XGBoost is that it provides a built-in method to calculate feature importance! We can access the feature importance values using the `feature_importances_` attribute of the model. Add the following code inside the *plot_feature_importance()* function:

```python
    all_importances = [estimator.feature_importances_ for estimator in model.estimators_]
    avg_importances = np.mean(all_importances, axis=0)
```

You may be wondering why we are averaging the feature importance values across all the estimators in our model! This is because we used the **MultiOutputRegressor** wrapper. While our primary intention was to allow our model to predict multiple weather variables at once, the way it actually does this is by creating a separate model for each weather variable. This means that we really have multiple XGBoost models under the hood, each with its own feature importance values. So in order to get a single set of feature importance values for our entire model, we will average the feature importance values across all the estimators from the multi-output model.

So looking at the code, we first use a list comprehension to obtain the feature importance values from each estimator in our model. Then, we use the `np.mean()` function to calculate the average feature importance values across all the estimators. The resulting `avg_importances` variable will contain a single set of feature importance values that we can use for visualization.

Next, we'll want to actually plot the feature importance values. We can use the **matplotlib** library to create a bar chart that shows the importance of each feature. Add the following code inside the *plot_feature_importance()* function:

```python
    importances_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": avg_importances
    }).sort_values(by="Importance", ascending=True)
    
    plt.figure(figsize=(10, 6))
    plt.barh(importances_df["Feature"], importances_df["Importance"])
    plt.title("Average Feature Importances From All Estimators")
    plt.xlabel("Avg. Relative Importance (Gain)")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.show()
```

This will create a horizontal bar chart that shows the average feature importance values for each feature in our dataset. The features will be sorted in ascending order of importance, so the most important features will be at the top of the chart. The x-axis will show the average relative importance values, while the y-axis will show the feature names.

*Note: Make sure to import the necessary libraries (numpy and matplotlib) at the top of your model.py file if you haven't already! If you need, feel free to search for the correct import statements online.*

Now, go back to your *main.py* file and call the *plot_feature_importance()* function after the validation function we implemented last week. Pass in your trained model and the list of feature names as arguments (Hint: you can use X_train.columns). Run your main.py file to see the feature importance plot.

*Note: Make sure to import the plot_feature_importance() function from your model.py file at the top of your main.py file if you haven't already! You can do this similarly to how we imported the other functions last week.*

Hopefully, this visualization will help you identify which features are the most important for your model's predictions and which ones you might want to remove to simplify the model! Now, because the removal of features might depend on the specific weather variable you are trying to predict, we will leave it up to you to decide which features to keep and which ones to remove. Here are a couple of things to keep in mind when selecting features:
- One of the common ways to decide which features to remove is by using a "threshold" value for feature importance. For example, you might decide to remove any features with an average importance value below 0.01. This means that any features that contribute less than 1% to the model's predictions will be removed. You can experiment with different threshold values to see how they affect your model's performance.
- Keep in mind that removing variables you actually want to display to someone using the model might not be the best idea. For example, if you want to display the wind speed in your app, but the wind speed variable has a low feature importance value, you might still want to keep it in your model so that you can display it in your app. For example, do not remove the temperature variable from your model! As a reminder, this is the variable we will be testing in the final competition.
- Finally, when retraining the model after removing features, make sure to update your training and validation datasets to only include the selected features. For example, if you remove the "wind speed" feature, make sure to remove it from both your training and validation datasets before retraining the model. This is because we made our model so that it predicts the next weather state based on the current weather state (where both the input and output have the same features), so if we remove a feature from the input data, we also need to remove it from the output data.

## 2. Hyperparameter Tuning

Next, we will focus on hyperparameter tuning to improve our model's performance. Hyperparameters are parameters that are set before training the model and can significantly impact its performance. Some examples include all the different parameters when we set up our XGBoost model, such as the learning rate, number of estimators, and maximum depth of the trees. By tuning these hyperparameters, we can find the optimal combination that leads to better predictions!

*Note: Make sure to import the necessary libraries as well! For reference, here are all the import statements you should have at the top of your model.py file:*
```python
import joblib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.multioutput import MultiOutputRegressor
from xgboost import XGBRegressor
```

We'll start again by adding a function to our *model.py* file that will allow us to tune the hyperparameters of our model. Add the following starter function to your *model.py* file:

```python
def tune_hyperparameters(model_path, X_train, Y_train):
    print("Tuning hyperparameters for the weather model...")

    base_model = XGBRegressor(random_state=42)
    multi_model = MultiOutputRegressor(base_model)
```

Notice how we are creating a new instance of our model inside the function. This is because we want to tune the hyperparameters of a fresh model, rather than the one we trained earlier. This instance will then be passed into the next phase of the tuning process.

In this project, we will use a technique called "grid search" to find the best hyperparameters for our model. Grid search involves specifying a set of hyperparameter values to try and then training and evaluating the model for each combination of hyperparameters. This can be a time-consuming process, but it can lead to significant improvements in model performance. The specific tool we will use for grid search is called **GridSearchCV**, which is a built-in function in the **sklearn** library. This function will automatically perform the grid search for us and return the best hyperparameters based on the model's performance.

We'll start by defining a grid of hyperparameter values to try. Add the following code inside the *tune_hyperparameters()* function:

```python
    param_grid = {
        "estimator__n_estimators": [50, 100, 200],
        "estimator__learning_rate": [0.03, 0.1, 0.3],
        "estimator__max_depth": [3, 5, 7]
    }
```

This tells the grid search to try every combination of the specified hyperparameter values. For example, it will try a model with 50 estimators, a learning rate of 0.03, and a maximum depth of 3, as well as a model with 100 estimators, a learning rate of 0.1, and a maximum depth of 5, and so on. This is what makes grid search a powerful (and sometimes slow) technique for hyperparameter tuning, as it allows us to explore a wide range of hyperparameter values and find the best combination for our model.

Next, we'll create an instance of the **GridSearchCV** class and pass in our model, the hyperparameter grid, and the number of cross-validation folds to use. Add the following code inside the *tune_hyperparameters()* function:

```python
    grid_search = GridSearchCV(
        estimator=multi_model,
        param_grid=param_grid,
        scoring="neg_root_mean_squared_error",
        n_jobs=-1,
        cv=TimeSeriesSplit(n_splits=3),
        verbose=1
    )
```

To break down each component more specifically:
- `estimator`: This is the model we want to tune, which is our multi-output XGBoost model.
- `param_grid`: This is the grid of hyperparameter values we defined earlier.
- `scoring`: This is the metric we want to use to evaluate the model's performance. In this case, we are using the negative root mean squared error (RMSE) as our scoring metric. The negative sign is used because GridSearchCV tries to maximize the scoring metric, and we want to minimize the RMSE.
- `n_jobs`: This specifies the number of CPU cores to use for parallel processing. Setting it to -1 means that all available cores will be used.
- `cv`: This specifies the cross-validation strategy to use. In this case, we are using time series cross-validation with 3 splits. This is important because our data is time series data, and we want to make sure that we are not using future data to predict past data (similar to how we defined our train/test split earlier).

Finally, we'll add the last few lines of code for this grid search function:

```python
    grid_search.fit(X_train, Y_train)
    
    print(f"Best parameters found: {grid_search.best_params_}")
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(grid_search.best_estimator_, model_path)
    
    return grid_search.best_estimator_
```

This code fits the grid search to our training data, prints the best hyperparameters found, saves the best model, and returns the best model. The `grid_search.best_params_` attribute contains the best hyperparameters found during the grid search, while the `grid_search.best_estimator_` attribute contains the best model trained with those hyperparameters.

Now, back in the *main.py* file, we will call the *tune_hyperparameters()* function after the validation function we implemented last week. Pass in the path to save the best model, as well as your training data (X_train and Y_train) as arguments. Run your main.py file to see the hyperparameter tuning process in action!

```python
    print("Loading tuned weather model...")
    
    if not tuned_model_path.exists():
        tuned_model = tune_hyperparameters(tuned_model_path, X_train, Y_train)
    else:
        tuned_model = joblib.load(tuned_model_path)
    
    rmse_tuned = validate_model(tuned_model, X_val, Y_val)
    print(f"Root Mean Squared Error (Tuned): {rmse_tuned}")
```

*Note: Similar to before, we check first to see if the tuned model already exists. If it does, we load it. If not, we tune the hyperparameters and save the best model (this is done to avoid re-running the tuning process every time). Also, make sure to define the `tuned_model_path` variable before calling the function (this should be similar to how you defined the `model_path` variable earlier). Finally, remember to import the function again at the top of the file!*

## 3. Next Steps

Awesome! Now that we have tuned our model's hyperparameters, we can compare the performance of the tuned model to our baseline model. You should hopefully see a decrease in the RMSE value, indicating that our tuned model is performing better than our baseline model. If you want to further improve your model's performance, you can experiment with different hyperparameter values (maybe try larger or smaller ranges for each parameter in the grid) and feature selection techniques to see how they affect your model's predictions.

Well done! You have successfully learned how to tune the hyperparameters of a machine learning model and implement feature selection. In the next week, we will focus on making autoregressive predictions and deploying our model using Streamlit. This will allow us to create a user-friendly interface for our weather forecaster and make it accessible to others. Keep up the great work!

If you have some extra time, I'd recommend making sure you know how to fully execute feature selection as that's something that I gave more of an outline for instead of the entire instructions. It may involve some experimenting and looking back on earlier parts of the project, but it will be worth it to have a more optimized model for the final competition!

Feel free to reach out if you have any questions or need any help with the instructions. Also, make sure to attend the guided project checkpoint to get any help or get any questions answered, work with others also doing the same project, and be eligible for the competition at the end of the semester!
