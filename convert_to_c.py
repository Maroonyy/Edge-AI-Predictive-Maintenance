import joblib
import m2cgen as m2c

def translate_model_to_c():
    print("Loading the trained model...")
    
    # Load the trained model
    try:
        model = joblib.load("predictive_maintenance_model.pkl")
    except FileNotFoundError:
        print("Error: Could not find the model file. Please run train_model.py first.")
        return
    
    print("Translating the model to C code...")
    
    # Use m2cgen to translate the model to C code
    c_code = m2c.export_to_c(model)
    
    # Save the C code to a file
    with open("model.c", "w") as f:
        f.write(c_code)
    
    print("Model successfully translated to 'model.c'")
    
if __name__ == "__main__":
    translate_model_to_c()