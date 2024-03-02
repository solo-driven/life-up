# LifeUp: Anomaly Detection in Fitness Data

LifeUp is a project aimed at detecting anomalies in fitness data obtained from Google Fit. The primary goal is to identify potential cheating by comparing the user's activity data against typical patterns. 

The project uses an autoencoder model to analyze time series data consisting of speed, distance, and step count measurements. The model is trained to recognize normal patterns in the data. When the model encounters data that deviates significantly from these patterns, it flags it as an anomaly, potentially indicating cheating.

The LifeUp anomaly detection system is deployed as an API on Hugging Face. The API receives the Google Fit data, runs the anomaly detection algorithm, and returns the result. This setup allows for easy integration with other systems and applications.

To interact with the API and see it in action, check it out on [Hugging Face Spaces](https://huggingface.co/spaces/solo-driven/lifeup).

## Usage

The project includes a Gradio interface for easy usage. The interface allows you to input the speed, distance, and step count data as separate DataFrames, and it displays the result of the anomaly detection.
