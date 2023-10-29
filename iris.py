from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

clf = DecisionTreeClassifier()

epochs = 10
hits = 0

for epoch in range(epochs):
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    epoch_hits = sum(y_pred == y_test)
    hits += epoch_hits

    print(f"Época {epoch + 1}: {epoch_hits} acertos.")

print(f"Total de acertos ao longo de {epochs} épocas: {hits}")

print("\n--------------------------------------\n")

# Novas flores para previsão
new_flowers = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.7, 3.1, 4.7, 1.5],
    [6.0, 3.0, 4.8, 1.8],
    [7.7, 3.8, 6.7, 2.2],
    [6.3, 2.5, 5.0, 1.9],
    [5.8, 2.7, 5.1, 1.9],
    [5.6, 2.8, 4.9, 2.0],
    [6.4, 3.2, 5.3, 2.3],
    [6.1, 2.6, 5.6, 1.4]
]

species_names = iris.target_names

for i, flower in enumerate(new_flowers, start=1):
    predicted_species = clf.predict([flower])
    predicted_species_name = species_names[predicted_species[0]]
    print(f"Flor {i}: Espécie prevista: {predicted_species_name}")
