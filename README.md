# Fish Weight Prediction Model

## Overview

This repository contains code for a machine learning model trained to predict the weight of fish based on various features such as length, height, and width. The model is implemented using scikit-learn in Python and exposed through a Flask web application for easy access.

## Project Structure

- `app.py`: Contains the Flask web application code.
- `templates/index.html`: HTML template for the user interface.
- `fish_market_model.pkl`: Serialized trained machine learning model.
- `README.md`: This file, providing an overview and instructions for the project.

## Usage

### Prerequisites

- Python 3.x
- Flask
- scikit-learn
- numpy

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/programmer-sp/Fish-Market-ML-Model
   ```

2. Navigate to the project directory:

    ```bash
    cd fish-weight-prediction
    ```

### Running the Web Application

1. Run the Flask web application:

    ```bash
    python app.py
    ```

2. Open a web browser and go to http://localhost:5000 to access the application.

### Making Predictions

- Enter the fish features (length1, length2, length3, height, and width) into the form and click "Predict".
- The predicted weight of the fish will be displayed on the page.