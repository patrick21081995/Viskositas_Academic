# import packages
import numpy
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

# loading preprocessing database
dados = pickle.load(open('preprocessing_data.d', 'rb'))

# partitioning training, validation and test data
x_total = dados.iloc[0:len(dados), 0:len(dados.columns) - 1]
y_total = dados.iloc[0:len(dados), len(dados.columns) - 1:len(dados.columns)]
x, xt, y, yt = train_test_split(x_total, y_total, test_size = 0.1, random_state = 376)

# pipeline to standardize the input and trainning the neural network 
pipeline = make_pipeline(StandardScaler(),
MLPRegressor(hidden_layer_sizes=(4), activation='relu', solver='adam', batch_size=64, learning_rate_init=0.001,
tol=0.0001, random_state=549, validation_fraction=0.1, early_stopping=True, max_iter=100000, n_iter_no_change=50000, verbose=True))
pipeline.fit(x.values, y.values)

# printing the: 
print(sum(abs(pipeline.predict(xt.values).reshape(-1,1) - yt.values))/len(yt.values))  # MAE (mean absolute error)
print(abs(pipeline.predict(xt.values).reshape(-1,1) - yt.values).std())  # standard deviation of error between model and data 
print(pipeline.score(xt.values, yt.values))  # coefficient of determination (R-squared)

# save the model 
pickle.dump(pipeline, open('viskositas_academic_pipeline.s', 'wb'))

