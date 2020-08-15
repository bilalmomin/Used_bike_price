USED BIKE PRICE PREDICTOR: Project Overview

 * Created a model that predicts price ( MAE~ 3000) of the used bike by evaluating the features like bike model, cubic capacity, distance travelled etc.
 * The data required for the training of model is scraped from droom(https://droom.in/).
 * New features like bike model,cubic capacity,year of the bike were created using existing feature.
 * Location feature is created by merging the existing information and census data of 2001. Name of the cities,districts are converted into their state's name.
 * Used XGBoost Regressor for prediction. Optimized XGBoost Regressor
using RandomizedSearchCV to get the best parameters for to build model.
 * Built a client facing API using Flask.

RESOURCES

 * Data collected from - (https://droom.in/).
 * Webpage background image source - (https://images.unsplash.com/photo-1547549082-6bc09f2049ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1051&q=80).
 * A special thanks to Krish Naik ("https://www.linkedin.com/in/naikkrish/")  for sharing his amazing knowledge and teaching. A thanks to Corey Schafer for his tutorials.

DATA COLLECTION

 * The data is scraped from droom(https://droom.in/).
 * Information like bike name, price, location, owner, distance travelled have been extracted.
 * The page contains "Load More" button therefore used session to scrape through all the pages.
 

DATA CLEANING

 * Filled the NaN values for one categorical feature and dropped the NaN values for some other features.
 * Replaced the unnecesasary symbols by blank space.
 * Converted the data-type object to numeric where ever required.
 * Created multiple new features from the column 'Name' using different techniques (regular expressing,spliting). This requires some domain knowledge.
 * Used the census data of India from the year 2001.
 * Location feature is created by merging the existing information and census data of 2001. Name of the cities, districts are converted into their state's name. This took little smart coding in pandas and working with dictionary. Update some data using domain knowledge.
 * For encoding of categorical features 'Count Frequency Encoding' and 'One Hot Encoding' are used.
 * For count frequency encoding the entry in a column is replaced by the number of time it has occured in the dataset.
 * Dropped few records to maintain the count of each category.

EDA

 * All the features in the dataframe are used so therefore not much analysis is done.
 * Used heatmap to find the correlation.

MODEL BUILDING

 * Baseline Model - XGBoost Regressor
 * RandomForestRegressor with best parmeters is used after doing a RandomizedSearchCV on the baseline model.
 * Used pickel to save the model.

MODEL PERFORMANCE

 * MAE ~ 3000
 * R^2 score = 0.92

DEPLOYMENT

 Built a Flask API endpoint that was hosted on a local webserver. The API endpoint takes the list of values and return the predicted fare price

MOTIVATION
 
 The whole purpose of doing this project is to learn th Data Science and Machine Learning and to get the hands on experience in order to get ready for the industry.

FUTURE SCOPE 

 * Real time scrapper and data processing code can be used to collect the data and train the model on that data for more accurate perditions.
 * More effficient feature engineering is possible with categorical features.
 * Different algorithm can be used to improve the accuracy.

 







