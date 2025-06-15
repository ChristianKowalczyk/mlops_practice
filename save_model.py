import tensorflow as tf
import os

# Load a pre-trained model (e.g., ResNet50 for image classification)
model = tf.keras.applications.ResNet50(weights='imagenet')

# Define the path to save the model
model_version = "1"
export_path = os.path.join("tf_serving_model", model_version)

# Save the model in SavedModel format for TensorFlow Serving
model.export(export_path)

print(f"Model saved to: {export_path}")
print("To verify, run: ls -l tf_serving_model/1")