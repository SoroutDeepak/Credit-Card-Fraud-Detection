# -*- coding: utf-8 -*-
"""Knn0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ig6pcFExfJX6AJlGbx7uONfTccE_A5h6

# KNN
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

!unzip -qq /content/archive.zip

credit_card_data = pd.read_csv('/content/creditcard.csv')

credit_card_data.isnull().sum()

features = credit_card_data[['V1', 'V2']]

labels = credit_card_data['Class']

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

"""Prediction"""

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

"""Ploting"""

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', cmap=plt.cm.coolwarm, s=20)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', cmap=plt.cm.coolwarm, marker='x', s=50)

plt.title('k-NN Decision Boundary (n_neighbors=5)')
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()

