# LifeUp: Anomaly Detection in Fitness Data

LifeUp is a project aimed at detecting anomalies in fitness data obtained from Google Fit. The primary goal is to identify potential cheating by comparing the user's activity data against typical patterns.

The project uses an autoencoder model to analyze time series data consisting of speed, distance, and step count measurements. The model is trained to recognize normal patterns in the data. When the model encounters data that deviates significantly from these patterns, it flags it as an anomaly, potentially indicating cheating.

The LifeUp anomaly detection system is deployed as an API on Hugging Face https://huggingface.co/spaces/solo-driven/lifeup. The API receives the Google Fit data, runs the anomaly detection algorithm, and returns the result. This setup allows for easy integration with other systems and applications.

In addition, we have created our own model API using FastAPI, which has been dockerized (available at `solodriven/pedometer_anomaly_detection` on Docker Hub) https://hub.docker.com/r/solodriven/pedometer_anomaly_detection and deployed on Google Kubernetes Engine (GKE). This provides a scalable and robust platform for serving our anomaly detection model.

To interact with the API and see it in action, check it out on Hugging Face Spaces.

## Project Steps

1. **Data Visualization:** The first step in the project was to visualize the data obtained from Google Fit. This helped us understand the patterns and trends in the data.

2. **Data Interpolation:** The data obtained from Google Fit was not recorded at the same time intervals. To handle this, we interpolated the data to fill in the missing values and create a continuous time series.

3. **Model Training:** We trained an autoencoder model on the interpolated data. The model was trained to recognize normal patterns in the data and flag any significant deviations as anomalies.

4. **Model Deployment:** The trained model was saved and deployed as an API on Hugging Face. The API receives the Google Fit data, runs the anomaly detection algorithm, and returns the result.

5. **FastAPI and Dockerization:** We created our own model API using FastAPI. The API was dockerized (available at `solodriven/pedometer_anomaly_detection` on Docker Hub) for easy deployment and scalability.

6. **Deployment on GKE:** The dockerized API was deployed on Google Kubernetes Engine (GKE), providing a robust and scalable platform for serving our anomaly detection model.
