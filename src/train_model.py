# Script to train machine learning model.

from sklearn.model_selection import train_test_split

from train_model.data import import_data, process_data
# from train_model.model import train_model, compute_model_metrics, inference

# load in the data.
data = import_data("../data/census_cleaned.csv")

# Optional enhancement,
# use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.

# Train and save a model.