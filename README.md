# Retail-Data-Analysis
This is a data science assignment that explores the concept of; Git/GitHub, Numpy and Pandas, 
Answers to Theoretical Questions

1. NumPy ndarray faster than Python lists
NumPy arrays store data in a continuous block of memory and use optimized code but 
python lists store references to objects, which takes more memory and is slower.

2. Broadcasting vs Vectorization
Vectorization is doing operations on entire arrays at once without using loops whiles 
Broadcasting is allowing operations between arrays of different sizes.

3. If you subtract a mean from an array (array - mean), 
NumPy automatically subtracts the mean from every value in the array.

4. Git Conflict
in such a situation, Git shows a merge conflict.

5. Resolving Git Conflict
a.Open the file
b.Select the correct code
c.Run this in the terminal: git add .
git commit - m "fix: resolving Git merge conflict"

6. Pandas vs Numpy 
Numpy is used for fast calculations while Pandas is used when working with tables and data analysis
In the professional pipeline, I would use numpy for heavy maths calculations and pandas for data manipulation and alalysis.


# **Modeling**
## Modeling Strategy

A Random Forest Classifier was selected for this project.

Why Random Forest?

The warehouse sales data contained non-linear relationships between variables such as:
* Sales trends
* Revenue after tax
* Monthly demand patterns

Random Forest was chosen because:

1. It performs well on structured tabular data
2. It handles non-linear patterns effectively
3. It reduces overfitting through ensemble learning
4. It provides feature importance analysis
5. It is reliable for classification tasks

The prediction objective was framed as a Classification problem.

**Prediction Goal**
The model predicts:
Restock, Do Not Restock

A target column called Restock was created using sales thresholds.


### Feature Selection
The following features were selected because they were expected to influence inventory demand:
Feature | Reason

Rev_after_tax | Represents actual revenue trends
Month  | Captures seasonality and demand fluctuation

Sales | Direct indicator of inventory movement.

The selected features formed the input matrix X, while the Restock column formed the target variable y.


### Training and Testing Split
The dataset was split using the standard 80/20 rule.
* 80% of the data was used for training
* 20% of the data was used for testing
This allowed the model to learn historical warehouse behavior before predicting unseen outcomes.


### Evaluation
#### Evaluation Strategy

The project emphasized business-focused evaluation instead of relying only on mathematical accuracy.
The following metrics were used:
* Precision
* Recall
* F1-Score
* Confusion Matrix


### Confusion Matrix Analysis
The confusion matrix helped identify:

1. False Positives:
The model predicts a restock when it is unnecessary.
Business Impact:
* Increased storage costs
* Excess inventory
* Capital tied up in slow-moving products

2. False Negatives:
The model predicts no restock when inventory is actually needed.
Business Impact:
* Stock shortages
* Lost sales opportunities
* Customer dissatisfaction

Most Expensive Error:
For this business scenario, False Negatives are considered more expensive because running out of high-demand products directly affects revenue and customer trust.


### Performance Report
Metric | Meaning
Precision | Measures how many predicted restocks were actually correct
Recall | Measures how many actual restocking situations the model successfully identified
F1-Score | Balances precision and recall

To put it in simple terms the model is designed to identify low-stock situations early while minimizing unnecessary inventory purchases.
This helps reduce stock shortages and improves operational efficiency.


### Feature Importance and Logic Validation
Feature importance analysis was used to verify whether the model learned meaningful business patterns.
For example:
* Sales trends influencing restock decisions is logical
* Monthly demand influencing inventory is logical

If unrelated features such as product color became dominant predictors, 
this could indicate that the model learned misleading or coincidental patterns.
This process helps validate model reliability.

### Deployment
#### Model Serialization

The trained model was serialized using joblib and saved as:
**model_inventory.plk.** 
This allows the trained model to be reused without retraining every time the system starts.

#### Prediction Function (API Simulation)
The function is shown below is a lightweight prediction function. It was designed to simulate how a warehouse might interact with the designed model
This enables instant inventory predictions based on incoming warehouse data.:

def predict_restock(sales, rev_after_tax, month):
    data = [[sales, rev_after_tax, month]]
    prediction = model.predict(data)
    if prediction[0] == 1:
        return "Restock"
    else:
        return "Do Not Restock"




# Deployment Guide
## Quick Start

Step 1: Clone the repository,
"https://github.com/SiegfredAkanson/Retail-Data-Analysis.git"

Step 2: Intall the necessary dependencies 
(numpy, pandas, scikit-learn and joblib,). Use pip install followed by the name of the dependency or ,
you can equally put them all on the same line

Step 3: Load the saved model by importing joblib (import joblib)
and run: model = joblib.load("model_inventory.plk")

Step 4: Now run the prediction code below:
prediction = model.predict([[4000, 3400, 7]])
print(prediction)


# Final Project Conclusion

This project helped show how raw and unorganized sales data can be turned into useful business information using the CRISP-DM process. 
Starting from generated sales data, the project went through data cleaning, analysis, 
modeling, evaluation, and deployment stages to build a simple predictive inventory system.

The final model can help predict when products may need restocking, 
which can support better warehouse decisions and reduce inventory problems. 
Overall this project helped demonstrate how data can be transformed 
from “messy data” into a more useful and predictive business asset.
