# 📈 Stock Market Prediction App

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.21.0-green.svg)
![PyChart](https://img.shields.io/badge/PyChart-1.39.0-blue.svg)
![AngelOne API](https://img.shields.io/badge/AngelOne-API-yellow.svg)

## Overview

Welcome to the Stock Market Prediction App! This application leverages mathematical indicators and real-time market data to predict stock movements and help you make informed trading decisions. With this app, you can:

- 📊 **Predict stock movements** using mathematical indicators.
- 💹 **Buy, sell, and hold stocks** based on predictions.
- 📈 **Manage your portfolio** by adding and removing stocks.
- 📡 **View live market feed** including real-time data and indicators.

## Features

- **Stock Prediction**: Utilizes mathematical indicators to forecast stock prices.
- **Trading Actions**: Execute buy, sell, and hold actions on stocks.
- **Portfolio Management**: Add or remove stocks from your portfolio.
- **Live Market Data**: Fetches live market data using the AngelOne API and displays it alongside mathematical indicators.

## Tech Stack

- **Jupyter Notebook**: For interactive development and data analysis.
- **Python 3.8**: The core programming language used.
- **NumPy**: For numerical computations.
- **PyChart**: For creating and displaying charts.
- **AngelOne Live Market Data API**: To fetch real-time market data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/stock-market-prediction-app.git
   cd stock-market-prediction-app
   ```

2. **Create a virtual environment**:
   ```bash
   python3.8 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.yaml
   ```

## Usage

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open the notebook**:
   Open the `stock_prediction.ipynb` file in the Jupyter interface.

3. **Run the app**:
   Execute the cells in the notebook to fetch live market data, perform predictions, and manage your portfolio.
