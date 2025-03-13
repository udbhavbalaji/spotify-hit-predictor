# Spotify Hit Predictor

**This repo holds the magic behind song-savvy! All the data preprocessing, data building, model exploration, model building and optimization are above.**

## Snapshot Info:

1. Dataset size: ~24,500 rows of data.
2. Models Tested: Logistic Regression, Random Forest Classifier, Multi-Layered Perceptron
3. Best Testing Accuracy: 89.99% -> MLPClassifier
4. Best Model Params: 
    * **solver**: *lbfgs*
    * **learning_rate**: *invscaling*
    * **hidden_layer_sizes**: *(20,)*
    * **alpha**: *0.01*
    * **activation**: *logistic*

## Documentation

* **Dataset (Kaggle)**: [https://www.kaggle.com/datasets/theoverman/the-spotify-hit-predictor-dataset]
* **Logistic Regression (scikit-learn)**: [https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html]
* **Logistic Regression (scikit-learn)**: [https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html]
* **Random Forest Classifier (scikit-learn)**: [https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html]
* **Multi-Layered Perceptron (scikit-learn)**: [https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html]

Any feedback is welcome and appreciated!

