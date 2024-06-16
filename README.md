# Credit-card-Fraud-Detection-System
### Summary of the Credit Card Fraud Detection Project

#### Overview

This project involves creating a system to detect credit card fraud using a dataset that includes various features related to credit card transactions. The approach combines data preprocessing, model training, and deployment through a graphical user interface (GUI) using Tkinter.

#### Data Handling

1. **Loading the Dataset**:
   - The dataset is loaded using `pandas`, and the columns include features like `distance_from_home`, `distance_from_last_transaction`, `ratio_to_median_purchase_price`, and others, with the `class` column indicating legitimate (0) or fraudulent (1) transactions.

2. **Exploring the Dataset**:
   - The dataset comprises 1,000,000 entries, with a significant imbalance: 912,597 legitimate transactions and 87,403 fraudulent ones.

3. **Data Statistics**:
   - Descriptive statistics reveal that legitimate transactions have lower means and standard deviations in features compared to fraudulent transactions. 

#### Data Balancing

- **Generating Synthetic Data**:
  - A synthetic dataset is created to balance the number of legitimate and fraudulent transactions. The mean and standard deviation for each feature are defined, and 1,000 samples for each class are generated using normal distribution.

#### Model Training

1. **Feature Engineering**:
   - Features are separated from the target variable, and the dataset is split into training and testing sets with a 80-20 split, ensuring class distribution is maintained.

2. **Model Selection and Training**:
   - A Random Forest Classifier is initialized and trained on the training set. The model achieves 100% accuracy on both training and testing sets.

3. **Evaluation**:
   - The model's performance is evaluated using accuracy and a classification report, showing perfect precision, recall, and F1-score for both classes.

#### Deployment

1. **Saving the Model**:
   - The trained model is saved to a file using `pickle` for later use.

2. **Creating a GUI with Tkinter**:
   - A Tkinter GUI is designed to allow users to input transaction details and predict fraud. The GUI includes:
     - Input fields for each feature.
