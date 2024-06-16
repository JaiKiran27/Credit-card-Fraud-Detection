import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pickle

# Load the trained model using pickle
with open('C:/Users/Asus/OneDrive/Desktop/Credit Fraud/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create the Tkinter window
window = tk.Tk()
window.title("Credit Card Fraud Detection")
window.state('zoomed')  # Start in full-screen mode

# Add background color
window.config(bg="#ffffff")

# Add a custom font
custom_font = ("Arial", 12)

# Create a frame to center everything
main_frame = tk.Frame(window, bg="#ffffff")
main_frame.pack(expand=True)

# Create label for dataset information
dataset_info_label = tk.Label(main_frame, text="Credit Card Fraud Detection System", font=("Times new roman", 34, "bold"), bg="#ffffff", fg="#333333")
dataset_info_label.pack(pady=10)

# Load the dataset
data = pd.read_csv('C:/Users/Asus/OneDrive/Desktop/Credit Fraud/Credit_Card_Fraud_Detection_Dataset.csv')

# Assume the first 7 columns are the features required by the model
required_features = data.columns[:7]

# Display dataset information
dataset_info_text = "Number of Records: {}\nNumber of Features: {}".format(data.shape[0], len(required_features))
dataset_info_display = tk.Label(main_frame, text=dataset_info_text, font=custom_font, bg="#ffffff", fg="#333333")
dataset_info_display.pack(pady=10)

# Create input fields frame
input_frame = tk.Frame(main_frame, bg="#ffffff")
input_frame.pack(pady=10)

input_entries = {}
for i, column in enumerate(required_features):
    lbl = tk.Label(input_frame, text=column + ":", font=custom_font, bg="#ffffff", fg="#333333", anchor='e')
    lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(input_frame, font=custom_font, width=35, bg="#f1f1f1", fg="#333333", bd=1, relief="solid")
    entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
    input_entries[column] = entry

# Create entry field for pasting values
paste_frame = tk.Frame(main_frame, bg="#ffffff")
paste_frame.pack(pady=10)

label_list = tk.Label(paste_frame, text="Paste values separated by commas:", font=custom_font, bg="#ffffff", fg="#333333")
label_list.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_list = tk.Entry(paste_frame, font=custom_font, width=60, bg="#f1f1f1", fg="#333333", bd=1, relief="solid")
entry_list.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Apply values button
def apply_values():
    try:
        values_str = entry_list.get()
        input_values = [float(x.strip()) for x in values_str.split(',') if x.strip()]
        
        # Check if the number of values matches the number of required features
        if len(input_values) != len(required_features):
            messagebox.showerror("Error", f"Number of values should be exactly {len(required_features)}.")
            return
        
        # Populate individual entry fields
        for key, value in zip(input_entries.keys(), input_values):
            input_entries[key].delete(0, tk.END)
            input_entries[key].insert(0, str(value))
            
        print(f"Values successfully applied: {input_values}")
    except ValueError as e:
        print(f"Error applying values: {e}")
        messagebox.showerror("Error", "Please enter valid numeric values separated by commas.")

apply_button = tk.Button(main_frame, text="Apply", command=apply_values, font=custom_font, bg="#4285f4", fg="#ffffff", bd=0, relief="flat")
apply_button.pack(pady=10)

# Create predict button
def predict_fraud():
    try:
        # Get input values from the user
        input_values = []

        # If entry list is not empty, use it
        if entry_list.get():
            values_str = entry_list.get()
            input_values = [float(x.strip()) for x in values_str.split(',') if x.strip()]
            print(f"Input values from entry list: {input_values}")

            # Check if the number of values matches the number of required features
            if len(input_values) != len(required_features):
                messagebox.showerror("Error", f"Number of values should be exactly {len(required_features)}.")
                return
        else:
            # Use individual entry fields
            input_values = [float(entry.get()) for entry in input_entries.values() if entry.get()]
            print(f"Input values from individual fields: {input_values}")

        # Ensure input_values has exactly the expected number of features
        if len(input_values) != len(required_features):
            messagebox.showerror("Error", f"Number of values should be exactly {len(required_features)}.")
            return

        # Make the prediction
        prediction = model.predict([input_values])[0]
        print(f"Prediction: {prediction}")

        # Display the prediction
        if prediction == 1:
            result_label.config(text="Fraudulent Transaction", fg="red")
        else:
            result_label.config(text="Non-Fraudulent Transaction", fg="green")
            
        # Display feature importances if available
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            feature_importance_text = "Feature Importances:\n"
            for feature, importance in zip(required_features, importances):
                feature_importance_text += f"{feature}: {importance:.4f}\n"
            feature_importance_label.config(text=feature_importance_text)
        else:
            feature_importance_label.config(text="Feature importances not available for this model.")
            
    except ValueError as e:
        print(f"Error predicting values: {e}")
        messagebox.showerror("Error", "Please enter valid numeric values for all fields.")

predict_button = tk.Button(main_frame, text="Predict", command=predict_fraud, font=custom_font, bg="#34a853", fg="#ffffff", bd=0, relief="flat")
predict_button.pack(pady=10)

# Create label to display result
result_label = tk.Label(main_frame, text="", font=custom_font, bg="#ffffff", fg="#333333")
result_label.pack(pady=10)

# Create label to display feature importances
feature_importance_label = tk.Label(main_frame, text="", font=custom_font, bg="#ffffff", fg="#333333")
feature_importance_label.pack(pady=10)

window.mainloop()
