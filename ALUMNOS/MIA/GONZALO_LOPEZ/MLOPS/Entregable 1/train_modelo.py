from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# 1️⃣ Cargar el dataset de Iris
iris = load_iris()
X, y = iris.data, iris.target  # Features (X) y etiquetas (y)

# 2️⃣ Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ Entrenar el modelo de clasificación
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4️⃣ Guardar el modelo entrenado en un archivo .pkl
joblib.dump(model, "model.pkl")

print("✅ Modelo entrenado y guardado como 'model.pkl'")
