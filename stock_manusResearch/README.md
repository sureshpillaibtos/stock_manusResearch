# Stock Research Platform Dashboard

The **Stock Research Platform Dashboard** is a comprehensive analytical tool designed for investors and financial analysts. Developed using **Streamlit** and **Python**, the application leverages the **Yahoo Finance API** to provide real-time market insights and historical data analysis. The platform is structured to support complex financial research through a modular and scalable architecture.

## Core Capabilities

The platform provides a robust **Market Overview** that tracks major global indices, including the S&P 500, NASDAQ, and Dow Jones. Users can perform deep-dive **Stock Analysis** on individual tickers, accessing current pricing metrics, daily performance changes, and high-resolution interactive charts. The system supports multiple visualization formats, such as **Candlestick** and **Line** charts, integrated with essential technical indicators like **Simple Moving Averages (SMA)**, **Relative Strength Index (RSI)**, and **MACD**.

To facilitate specialized research, stocks are organized into strategic categories. These include **Standard Tech**, **AI Infrastructure**, **Traditional Semiconductors**, and **Networking**. The built-in **Comparison Engine** allows users to evaluate multiple securities side-by-side, normalizing performance data to identify relative strength and weakness across different market cycles.

## Project Architecture

The application is built with a focus on **Single Responsibility Principle**, ensuring each component is maintainable and extensible. The following table outlines the primary directory structure and their respective functions:

| Directory | Description |
| :--- | :--- |
| **modules/** | Contains the core business logic for dashboard components and UI sections. |
| **services/** | Manages data acquisition from Yahoo Finance and handles caching mechanisms. |
| **charts/** | Houses reusable Plotly-based visualization functions for financial charting. |
| **indicators/** | Implements technical analysis calculations using the `pandas_ta` library. |
| **utils/** | Provides shared helper functions for formatting, currency conversion, and metrics. |
| **config/** | Stores application constants, stock category definitions, and global settings. |

## Deployment and Usage

### Local Deployment
To initialize the environment locally, users should install the necessary dependencies using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Streamlit Cloud Deployment
When deploying to **Streamlit Cloud**, ensure that the Python version is set to **3.11** or **3.12** for optimal compatibility. The project includes a `packages.txt` file for necessary system-level dependencies and an updated `requirements.txt` that includes `setuptools` to prevent common installation errors in newer Python environments.

> **Note:** The platform uses public financial APIs and requires an active internet connection to fetch the latest market data.
