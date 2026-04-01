# BTC Technical Analysis App

AI-powered cryptocurrency chart analysis tool using Poe API.

## Features

- 📷 **Image Upload**: Upload BTCUSDT chart screenshots
- 🤖 **AI Analysis**: Professional technical analysis powered by Poe's GPT-5.2
- 📊 **Real-time Insights**: Get support/resistance levels, trend analysis, and trading signals
- 🎨 **Clean UI**: Modern Streamlit interface with responsive design

## Installation

1. **Install Python 3.8+** if not already installed

2. **Navigate to the app directory**:
   ```bash
   cd btc-analysis-app
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to the URL shown (usually `http://localhost:8501`)

3. **Upload a chart image**:
   - Take a screenshot of your BTCUSDT perpetual contract chart
   - Upload it through the web interface

4. **Click "Analyze Chart"** to get AI-powered technical analysis

## Configuration

The API key is pre-configured in the app. You can modify it in the sidebar settings if needed.

## Current Market Context

The app is configured with current market data:
- Price: $67,259.8
- Session Change: +1.92%
- Key resistance: 67,348.2, 67,620.6, 68,199.9
- Key support: 67,037.4, 64,928.2

## Requirements

- Python 3.8 or higher
- Streamlit
- OpenAI Python client
- Pillow (for image processing)

## Disclaimer

This tool provides analytical insights only. Always do your own research and trade responsibly. Cryptocurrency trading involves significant risk.
