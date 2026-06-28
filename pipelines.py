import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_ece_features(signal_array):
    """
    Compresses a raw 1D array of 20,480 sensor samples into
    the primary statistics taught in signal processing.
    """
    # Root Mean Square tracks overall kinetic energy/friction
    rms = np.sqrt(np.mean(signal_array**2))
    
    # Kurtosis identifies transient peaks or crack impacts
    kurtosis = pd.Series(signal_array).kurtosis()
    
    # Peak-to-Peak tracks extreme deviations
    peak_to_peak = np.ptp(signal_array)
    
    # Skewness measures asymmetry in the signal, which can indicate wear patterns
    skewness = pd.Series(signal_array).skew()
    
    return rms, kurtosis, peak_to_peak, skewness

def build_feature_matrix(data_directory):
    # Get all files and sort them chronologically by name
    all_files = sorted(os.listdir(data_directory))
    
    extracted_features = []
    labels = []
    
    print(f"Found {len(all_files)} data snapshots. Beginning feature extraction...")
    
    for index, filename in enumerate(all_files):
        file_path = os.path.join(data_directory, filename)
        
        # Skip hidden system files if they exist (like .DS_Store)
        if filename.startswith('.'):
            continue
            
        try:
            # Load the file. Set 2 uses tab separation and has no column headers
            df = pd.read_csv(file_path, sep='\t', header=None)
            
            # Focus on Bearing 1 (Column 0)
            bearing_1_signal = df[0].values
            
            # Compute our ECE features
            rms, kurt, p2p, skewness = calculate_ece_features(bearing_1_signal)
            extracted_features.append([rms, kurt, p2p, skewness])
            
            # Label Strategy: Mark the final 15% of the machine's life as 
            # 'Failing' (1), and the early operational life as 'Healthy' (0)
            if index > int(len(all_files) * 0.85):
                labels.append(1)
            else:
                labels.append(0)
                
        except Exception as e:
            print(f"Error processing file {filename}: {e}")
            continue
            
        # Print progress updates every 100 files so I know the script is running
        if index % 100 == 0:
            print(f"Processed {index}/{len(all_files)} files.")
            
    # Convert lists into clean structured pandas structures
    feature_names = ['RMS', 'Kurtosis', 'Peak_to_Peak', 'Skewness']
    X = pd.DataFrame(extracted_features, columns=feature_names)
    y = np.array(labels)
    
    print("Feature extraction complete!")
    return X, y


if __name__ == "__main__":

    DATA_DIR = "data/2nd_test" 
    
    X, y = build_feature_matrix(DATA_DIR)
    
    # Verify the final data shapes match expectations
    print(f"Feature Matrix X Shape: {X.shape} (Rows represent snapshots, Columns represent features)")
    print(f"Label Array y Shape: {y.shape}")
    
    # Save these metrics locally so I don't have to re-run the loop later
    X.to_csv("extracted_features.csv", index=False)
    np.save("labels.npy", y)
    print("Saved features to extracted_features.csv and labels.npy successfully.")