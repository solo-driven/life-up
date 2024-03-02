import gradio as gr
import pandas as pd
from keras.models import load_model
import pickle
import numpy as np

# Function to load model and scaler
def load_components():
    model = load_model('autoencoder_model.h5')
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

autoencoder, scaler = load_components()

# The main function for anomaly detection
def detect_anomalies(speed_df, distance_df, step_count_df):
 
    distance_df['timestamp'] = pd.to_datetime(distance_df['timestamp'], unit='ns')
    distance_df.set_index('timestamp', inplace=True)
    
    step_count_df['timestamp'] = pd.to_datetime(step_count_df['timestamp'], unit='ns')
    step_count_df.set_index('timestamp', inplace=True)
    
    speed_df['timestamp'] = pd.to_datetime(speed_df['timestamp'], unit='ns')
    speed_df.set_index('timestamp', inplace=True)

    # Combine DataFrames, interpolate, and drop NaN values
    combined = pd.concat([distance_df, step_count_df, speed_df], axis=1)
    combined_interpolated = combined.interpolate(method='linear').dropna()

    # Normalize and predict
    normalized_data = scaler.transform(combined_interpolated)
    reconstructed = autoencoder.predict(normalized_data)
    errors = np.mean(np.abs(normalized_data - reconstructed), axis=1)
    
    # Determine if any anomalies are detected
    threshold = np.mean(errors) + 2 * np.std(errors)
    anomalies_detected = np.any(errors > threshold)
    
    return anomalies_detected

# Define the Gradio interface with separate Dataframe inputs
iface = gr.Interface(
    fn=detect_anomalies,
    inputs=[
        gr.Dataframe(headers=["value", "timestamp"], datatype=["number", "number"], row_count=(1, "dynamic"), label="Speed Data"),
        gr.Dataframe(headers=["value", "timestamp"], datatype=["number", "number"], row_count=(1, "dynamic"), label="Distance Data"),
        gr.Dataframe(headers=["value", "timestamp"], datatype=["number", "number"], row_count=(1, "dynamic"), label="Step Count Data")
    ],
    outputs="bool",
    description="Detect Anomalies in Time Series Data"
)
# Launch the interface
iface.launch()