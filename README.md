# Air Quality Index
In this project, the data is extracted from a website, cleaned and fed into different model to make the AQI predictions with deployment.
With the help of certain envornmental factors such as Average Temperature,Maximum and Minimum Temperature,Average relative humidity,Average visibility and wind speed we are trying to pridict Atmospheric Particulate Matter.
Atmospheric Particulate Matter is the one of the important measument for checking quality of air.It Atmospheric Particulate Matter value is less than 2.5 then we are having good quality of air.

# Data extraction
Data is extracted from a website and is stored in the form of html files. Later by using beautiful soup, data from the html file is extracted and is converted to proper csv files.

# EDA
Most of the data cleaning is done while creating the csv files itself. Some of the missing values are also fixed. Checked the correlation using pearson correlation co-effient and also visualized the same.

# Model selection
Used various regression techniques to find which is the best model for this perticular problem statement. RandomForestRegressor and XGBoostRegressors are the models that are performing well

# Model evaluation
Evaluation metrics used for checking the model's strength is R2score and loss functions used are Mean Absolute Error (mae), Mean Sqaured Error (mse) and Root Mean Sqaured Error (rmse)

# Model Deployment
Using Flask framework proper web GUI is created.
