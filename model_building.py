import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import pickle

data_df = pd.read_csv('data/processed/tracks.csv')

data_df: pd.DataFrame = shuffle(data_df)
data_df.reset_index(inplace=True, drop=True)

data_df.drop_duplicates(keep='first', inplace=True)

X = data_df.drop(labels='target', axis=1, inplace=False)
y = data_df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)

numeric_features = ['danceability','energy','loudness','speechiness',
                    'acousticness','instrumentalness','liveness',
                    'valence','tempo','duration_ms','chorus_hit',
                    'sections', 'num_artists']

categorical_features = ['artist','key','mode','time_signature','release_type']

X_train = X_train[[*numeric_features, *categorical_features]]
X_test = X_test[[*numeric_features, *categorical_features]]

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features),
    ]
)

clf_mlp = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('clf', MLPClassifier(max_iter=1000))
])

param_grid_mlp = {
    'clf__hidden_layer_sizes': [(10,), (20,), (10, 10), (20, 20)],
    'clf__activation': ['identity', 'logistic', 'tanh', 'relu'],
    'clf__solver': ['lbfgs', 'sgd', 'adam'],
    'clf__learning_rate': ['constant', 'invscaling', 'adaptive'],
    'clf__alpha': [0.0001, 0.001, 0.01, 0.1]
}

grid_mlp = RandomizedSearchCV(clf_mlp, param_grid_mlp, cv=5, n_jobs=-1, verbose=0, scoring='accuracy')

grid_mlp.fit(X_train, y_train)

print(f'Best score = {grid_mlp.best_score_}')

y_pred = grid_mlp.predict(X_test)

conf_mat = confusion_matrix(y_pred, y_test)
acc = np.sum(conf_mat.diagonal()) / np.sum(conf_mat)
print(f'Overall accuracy: {acc*100}%')

pickle.dump(grid_mlp, open('model.pkl', 'wb'))
