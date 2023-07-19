import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append("/get_data")
from sklearn.linear_model import LinearRegression
from get_data.nhl_data import NHLData
from get_data.team_data import TeamData
from get_data.utility_data import UtilityData
from constants import CONDITIONALS

nhl_data = NHLData()
team_data = TeamData()
utility_data = UtilityData()

# info: TESTS
# game_id = "2023-04-13FLACAR"
# mp_game_id = 2022021299
# conditions = [{"header": string, "conditional": CONDITIONALS[i], "value": any}]
""" conditions = [
        {"header": "team", "conditional": "=", "value": "CAR"},
        {"header": "situation", "conditional": "=", "value": "5on5"},
        {"header": "season", "conditional": ">=", "value": 2021},
    ]
"""

res = nhl_data.conditional_data(
    "team_x_game",
    [
        {"header": "team", "conditional": "=", "value": "CAR"},
        {"header": "situation", "conditional": "=", "value": "5on5"},
        {"header": "season", "conditional": ">=", "value": 2021},
    ],
)

df = pd.DataFrame(res)
print(df)


"""
# Extract the features (X) and target variable (y) from the fetched data
X = np.array([row[:-1] for row in rows])  # Assuming the last column is the target variable
y = np.array([row[-1] for row in rows])   # Assuming the last column is the target variable

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions on new data
new_data = np.array([[1, 2, 3], [4, 5, 6]])  # Example new data to make predictions
predictions = model.predict(new_data)

# Print the predictions
print(predictions)

 """
