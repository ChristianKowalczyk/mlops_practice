# Use the official TensorFlow Serving base image (adjust version if needed)
FROM tensorflow/serving:latest

# Copy the saved model into the correct directory for TensorFlow Serving
# TF Serving expects models to be under /models/<model_name>/<version_number>
COPY tf_serving_model /models/my_tf_model