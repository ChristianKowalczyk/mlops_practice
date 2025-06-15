# Use the official TensorFlow Serving base image (adjust version if needed)
FROM tensorflow/serving:latest

# Create the model directory structure
RUN mkdir -p /models/my_tf_model/1

# Copy the saved model into the correct directory for TensorFlow Serving
COPY tf_serving_model/1/saved_model.pb /models/my_tf_model/1/
COPY tf_serving_model/1/variables /models/my_tf_model/1/variables/
COPY tf_serving_model/1/assets /models/my_tf_model/1/assets/

# Add a debug command to verify the files are there
RUN ls -la /models/my_tf_model/1/