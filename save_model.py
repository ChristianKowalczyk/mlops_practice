import tensorflow as tf
import os

# Load Fashion MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
train_images = train_images / 255.0
test_images = test_images / 255.0

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Compile and train
model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)

# Define the path to save the model (versioned)
model_version = "1"
export_path = os.path.join("tf_serving_model", model_version, "model.keras")

# Create directory if it doesn't exist
os.makedirs(os.path.dirname(export_path), exist_ok=True)

# Save the model
tf.keras.models.save_model(model, export_path)

print(f"Model saved to: {export_path}")
print("To verify, run: ls -l tf_serving_model/1")