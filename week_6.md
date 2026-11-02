# Week 6: Model Improvement and Novelty

Welcome back to the Weather Forecaster project! Last week, we learned how to implement autoregressive inferencing to actually use our model and host the app on Streamlit. This week, we will continue to work on creating a better model by going over some methods to improve the data and model performance, as well as coming up with a novel idea for our weather forecaster.

## 1. Improving Your Model

Now that you've done the full run through of all the steps to create a weather forecaster, it's time to go back and improve each step! The reason why I structured the project in this way is so that you can first get a better understanding of how to create a model from scratch and then go back and improve it on the second go around, while hopefully realizing how each step contributes to the overall performance of the model and how you can make it better.

### 1.1 Improving the Data

One major thing that can improve your model is improving the data. This can be done in a number of ways, such as adding more features, removing irrelevant features, or even collecting more data. You can also try different methods of feature engineering to create new features from the existing data. The goal is to create a dataset that is as informative and relevant as possible for the model to learn from. You can utilize your previous knowledge of exploratory data analysis, feature importance, and feature selection to help you with this process. Here are a few ideas to get you started:
- Try increasing the number of training samples by collecting more data from the Open-Meteo API. You can do this by changing the date range of the data you are collecting.
- Try adding more features to your dataset. This could be done by adding more weather variables from the Open-Meteo API, or by creating new features from the existing data (such as rolling averages, differences between variables, etc.).
- If you feel confident in your skills, you could even try adding more locations to your data. This could be a great way to make your model more robust and able to generalize better to different locations or glean more insight using nearby locations. You can do this by changing the latitude and longitude parameters in the Open-Meteo API request along with lots of engineering within the code to make sure that the data is being collected and processed correctly.

*Note: When downloading all this new data, you may need to find creative ways to adhere to Open-Meteo's API limits while still getting everything you need!*

### 1.2 Feature Selection

Another step you can take to improve your model is to perform feature selection. This involves selecting the most relevant features from your dataset to use in your model, and removing any irrelevant or redundant features as we discussed previously. This can help improve the performance of your model by reducing overfitting and improving generalization. You can use the feature importance plot that we created in Week 4 to help you with this process. You can also research and try different methods of feature selection.

*Note: Remember that as you create more complicated pipelines and models, it's important to ensure that you're code is still doing what you expect it to do. For instance, make sure that when you're adding or removing features or data, you're correctly changing the relevant parts of your code to accommodate the differences in structure. It's very important when coding that you know exactly what sort of data every part of your code is taking in and also spitting out.*

### 1.3 Hyperparameter Tuning

The third step you can take to improve your model is to perform hyperparameter tuning. This involves finding the best values for the hyperparameters of your model, such as the learning rate, batch size, or number of layers. You can use techniques like grid search to find the optimal combination of hyperparameters as discussed in Week 4 as well. Try more varying numbers or ranges within the grid search to see if you can find a better combination of hyperparameters that improves your model's performance.

*Note: While they are listed sequentially, feature selection and hyperparameter tuning aren't necessarily steps that need to be completed in order. It is not uncommon to perform both simultaneously or in a different order depending on the specific needs of your model.*

## 2. Coming Up with an Idea

While creating a weather forecaster is a great project to learn some of the fundamentals of machine learning, it's always a good idea to try and come up with a novel idea to make your project stand out. The main reason I say this is because quite literally anyone can find a weather forecast online (and one that is probably more accurate than what we can create in this project), so it's important to try and create something that is unique and interesting. This could be something as simple as adding a new feature to your weather forecaster, narrowing the scope of your project to a specific region or time period within the world, or even creating a new application that uses the weather data in a unique way. The goal is to create something that is unique and interesting, while still being feasible to complete within the time frame of the project.

Here are some vague potential ideas that may help you get started brainstorming:
- Look at downstream applications or specific niches that could benefit from a weather forecaster. For example, this could be looking at how likely an outdoor event could be affected by the weather, or how likely a specific crop could be affected by the weather. This could be a great way to create a unique application that uses the weather data in a specific way.
- Try to create a unique feature or functionality within your weather forecaster. For example, this could be adding a new visualization to the app, or creating a new way to interact with the data. This could be a great way to make your project stand out and show off your creativity.
- Think about specific use cases that you or others may have for a weather forecaster. For example, this could be looking at how the weather affects your daily routine, such as how likely you are to go for a run or what clothes you should wear based on the weather. This could be a great way to create a unique application that is tailored to your (or someone else's) specific needs.

Importantly, this will be one of the criteria used for the final competition, so it's important to start thinking about this now and come up with an idea that you can work on over the next couple of weeks!

## 3. Next Steps

This week's instructions are a bit more open-ended than previous weeks, as the goal is to give you some time to improve your model and come up with a novel idea for your project. I would recommend starting by looking at your current model and seeing where you can improve it, whether that be through improving the data, performing feature selection, or tuning the hyperparameters. Once you have a better understanding of your model's performance, you can start brainstorming ideas for how to make your project unique and interesting.

Plan to work on the more open-ended parts of the project over the next couple of weeks, as this will give you more time to iterate and improve your model and idea. Next week's instructions will also be relatively short and plan to focus on finalizing your project and preparing for the competition, so it's important to make sure that you have a solid model and idea before then! Your primary goal by the final competition should be to create the best model you can, while also coming up with a unique and interesting idea for your project that can be implemented into either your model or the Streamlit app or both! Great job so far, and keep up the good work (we're almost there)!

Feel free to reach out if you have any questions or need any help with the instructions. Also, make sure to attend the guided project checkpoint to get any help or get any questions answered, work with others also doing the same project, and be eligible for the competition at the end of the semester!
