# Titanic Survival Prediction Project
## Project Overview
This machine learning project aims to predict the survival chances of passengers aboard the RMS Titanic, which famously sank after colliding with an iceberg in 1912. By analyzing various factors such as age, sex, social status, and more, we develop models that can estimate survival probabilities for individuals under similar circumstances.

Features and Dataset
The dataset used for this project is derived from the Titanic passenger manifest and includes the following key features:
```
PassengerId: Unique identifier for each passenger
Survived: Survival (0 = No, 1 = Yes)
Pclass: Ticket class as a proxy for socio-economic status (1 = 1st, 2 = 2nd, 3 = 3rd)
Name: Passenger name
Sex: Passenger's sex
Age: Passenger's age in years
SibSp: Number of siblings/spouses aboard
Parch: Number of parents/children aboard
Ticket: Ticket number
Fare: Passenger fare
Cabin: Cabin number
Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
```

## Installation
To run this project, you will need Python and several libraries including NumPy, pandas, scikit-learn, and Matplotlib. You can install the dependencies with:
```
pip install numpy pandas scikit-learn matplotlib
```

## Usage
To use this model to predict Titanic survival chances:
1. Clone this repository to your local machine.
2. Ensure you have all the necessary dependencies installed.
3. Run the main script (e.g., python titanic_survival_prediction.py) to train the model and make predictions.


## Models and Training
This project utilizes Decision Tree and Logistic Regression for prediction. The model is trained on a split of the original dataset, with a certain percentage allocated for training and the remainder for testing to validate the model's performance.

We perform data preprocessing to handle missing values and convert categorical variables into a suitable form for modeling. Feature engineering is also applied to improve model accuracy.



## Results



## Contact
Linkai Lu - linkai.lu8579@gmail.com
