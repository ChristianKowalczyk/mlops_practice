import tensorflow as tf
import numpy as np
import json
import requests

# Load a sample image from the test set
(_, _), (test_images, _) = tf.keras.datasets.fashion_mnist.load_data()
sample_image = test_images[0] / 255.0 # Normalize and pick first image
sample_image_reshaped = sample_image.reshape(1, 28, 28).tolist() # Reshape for batch and convert to list

# Define the endpoint and model name
EXTERNAL_IP = "YOUR_EXTERNAL_IP" # Replace with the IP from Step 1
MODEL_NAME = "my_tf_model"
API_PORT = "8501" # REST API port

predict_url = f"http://{EXTERNAL_IP}:{API_PORT}/v1/models/{MODEL_NAME}:predict"

# Create the JSON payload
data = json.dumps({"instances": sample_image_reshaped})

# Send the request
headers = {"content-type": "application/json"}
response = requests.post(predict_url, data=data, headers=headers)

if response.status_code == 200:
    predictions = response.json()['predictions']
    predicted_class = np.argmax(predictions[0])
    print(f"Prediction for sample image: {predicted_class}")
else:
    print(f"Error: {response.status_code} - {response.text}")