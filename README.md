# 🍷 Wine Quality Prediction Using Decision Tree

## 📌 Project Overview

This project predicts **wine quality** using Machine Learning.

A **Decision Tree Classifier** is used to train the model based on different chemical properties of wine.

The project includes:

* Data preprocessing
* Missing value checking
* Exploratory Data Analysis (EDA)
* Feature selection
* Train-test splitting
* Decision Tree model training
* Model evaluation
* Saving the trained model
* Streamlit web application for prediction

---

## 🎯 Objective

The main objective of this project is to build a Machine Learning model that can predict the quality of wine based on its chemical characteristics.

The trained model is connected to a **Streamlit application**, where users can enter wine properties and get a prediction.

---

## 📊 Dataset

The project uses the **Wine Quality Dataset**.

### Dataset Files

```text
Wine dataset.csv
winequality-red.csv
```

The dataset contains chemical properties of red wine.

### Important Features

Some of the features include:

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

The target variable is:

```text
Quality
```

---

## 🔄 Machine Learning Workflow

The project follows this workflow:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Missing Value Checking
     ↓
Exploratory Data Analysis (EDA)
     ↓
Feature Selection
     ↓
X and y
     ↓
Train-Test Split
     ↓
Decision Tree Classifier
     ↓
Model Evaluation
     ↓
Save Model as .pkl
     ↓
Streamlit Application
     ↓
Wine Quality Prediction
```

---

## 🧹 Data Preprocessing

The dataset was checked for:

* Missing values
* Duplicate records
* Incorrect data types
* Unnecessary columns

The data was prepared before training the Machine Learning model.

---

## 📈 Exploratory Data Analysis

EDA was performed to understand the dataset and relationships between different wine properties.

The analysis included:

* Dataset information
* Statistical summary
* Missing value checking
* Correlation analysis
* Data visualization
* Distribution of wine quality

---

## 🤖 Machine Learning Algorithm

### Decision Tree Classifier

A **Decision Tree** is a supervised Machine Learning algorithm.

It makes predictions by creating a tree-like structure of decision rules.

For example:

```text
          Alcohol
         /       \
      Low         High
      /             \
   Lower          Higher
   Quality        Quality
```

The Decision Tree model learns patterns from the training data and uses them to predict wine quality.

---

## 📊 Model Evaluation

The trained model is evaluated using:

* Accuracy
* Confusion Matrix
* Precision
* Recall
* F1 Score

Example:

```python
from sklearn.metrics import accuracy_score, confusion_matrix
```

These metrics help to understand how well the model performs on unseen test data.

---

## 💾 Saved Model

The trained Decision Tree model is saved using Python Pickle.

Model file:

```text
wine_quality_dt_model.pkl
```

The saved model is loaded into the Streamlit application for making predictions.

---

## 🌐 Streamlit Application

A Streamlit web application was created to make the Machine Learning model easy to use.

Users can enter the required wine properties through the web interface.

The application then:

```text
User Input
     ↓
Input Processing
     ↓
Loaded Decision Tree Model
     ↓
Prediction
     ↓
Wine Quality Result
```

### Run the Streamlit Application

First, open PowerShell in the project folder:

```powershell
cd "C:\Users\nisha\OneDrive\Desktop\Documents\ExcelR_Python Practic\DT"
```

Then run:

```powershell
streamlit run app.py
```

The Streamlit application will open in the browser.

---

## 📁 Project Structure

```text
Wine-Quality-Prediction-using-ML/
│
├── .gitignore
│
├── app.py
│
├── Untitled.ipynb
│
├── Wine dataset.csv
│
├── winequality-red.csv
│
├── wine_quality_dt_model.pkl
│
└── README.md
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Pickle

### Machine Learning Algorithm

* Decision Tree Classifier

### Development Tools

* Jupyter Notebook
* Visual Studio Code
* Git
* GitHub

---

## 📦 Installation

Install the required Python libraries:

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```powershell
git clone https://github.com/Nis-hanth/Wine-Quality-Prediction-using-ML.git
```

### Step 2: Open the Project Folder

```powershell
cd Wine-Quality-Prediction-using-ML
```

### Step 3: Install Libraries

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

### Step 4: Run Streamlit

```powershell
streamlit run app.py
```


## 📚 Learning Outcomes

Through this project, I learned:

* How to work with a real-world dataset
* Data cleaning
* Missing value checking
* Exploratory Data Analysis
* Feature selection
* Train-test splitting
* Decision Tree Classification
* Model evaluation
* Saving Machine Learning models using Pickle
* Loading a trained model
* Building a Streamlit application
* Connecting a Machine Learning model with a web application
* Using Git and GitHub for project management

---

## 🚀 Future Improvements

Some possible improvements are:

* Try Random Forest and other classification algorithms
* Perform hyperparameter tuning
* Improve model accuracy
* Add more visualizations
* Add probability/confidence scores
* Improve the Streamlit user interface
* Deploy the application online

---

## ⚠️ Disclaimer

This project is created for **educational and learning purposes**.

The prediction should not be considered a professional wine-quality assessment.

---

## 👨‍💻 Author

**Nishanth**

BCA Student
Bharatesh College of Computer Applications
Belagavi, Karnataka

---

## ⭐ GitHub Repository

**Wine Quality Prediction Using Machine Learning**

Built using **Python, Scikit-learn, Decision Tree and Streamlit**.
