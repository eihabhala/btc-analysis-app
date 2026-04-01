# Chart Explorer

AI-powered technical analysis tool for **any trading chart** — stocks, forex, crypto, commodities, and indices.

## Features

- 📷 **Image Upload**: Upload a screenshot of any trading chart
- 🤖 **AI Analysis**: Professional technical analysis powered by OpenAI GPT-4o Vision
- 🌐 **Any Market**: Works with crypto, stocks, forex, commodities, indices, and more
- 🕐 **Any Timeframe**: 1m, 5m, 15m, 1h, 4h, 1D, 1W, or custom
- 📋 **Custom Context**: Add asset name, timeframe, market type, and optional notes
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

3. **Fill in the sidebar**:
   - Enter your OpenAI API key
   - Type the asset/symbol (e.g. AAPL, EURUSD, BTCUSDT, Gold)
   - Select the timeframe
   - Select the market type
   - Optionally add extra context (price levels, visible indicators, news)

4. **Upload a chart image**:
   - Take a screenshot of any trading chart
   - Upload it through the web interface

5. **Click "Analyze Chart"** to receive AI-powered technical analysis

## Requirements

- Python 3.8 or higher
- OpenAI API key (with GPT-4o access)
- Streamlit
- OpenAI Python client
- Pillow (for image processing)

## Disclaimer

This tool provides analytical insights only. Always do your own research and manage risk appropriately. Trading financial instruments involves significant risk of loss.

