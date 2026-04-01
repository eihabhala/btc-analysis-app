import streamlit as st
import openai
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Chart Explorer",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E86DE;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .analysis-box {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #2E86DE;
        margin: 20px 0;
    }
    .stButton>button {
        background-color: #2E86DE;
        color: white;
        font-weight: bold;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header">📊 Chart Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Powered Technical Analysis for Any Market & Timeframe</div>', unsafe_allow_html=True)

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Enter your OpenAI API key"
    )

    st.divider()
    st.subheader("📋 Chart Details")

    asset_name = st.text_input(
        "Asset / Symbol",
        placeholder="e.g. AAPL, EURUSD, BTCUSDT, Gold",
        help="Enter the ticker or name of the asset in your chart"
    )

    timeframe = st.selectbox(
        "Timeframe",
        options=["1m", "5m", "15m", "30m", "1h", "4h", "1D", "1W", "Custom"],
        index=1,
        help="Select the chart timeframe"
    )

    if timeframe == "Custom":
        timeframe = st.text_input("Custom Timeframe", placeholder="e.g. 2h, 3D")

    market_type = st.selectbox(
        "Market Type",
        options=["Crypto", "Stocks", "Forex", "Commodities", "Indices", "Other"],
        help="Select the market type for context"
    )

    extra_context = st.text_area(
        "Additional Context (optional)",
        placeholder="e.g. price levels, news events, indicators visible on chart",
        help="Any extra context to help the AI give a more accurate analysis"
    )

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📷 Upload Chart Image")
    uploaded_file = st.file_uploader(
        "Upload your chart screenshot",
        type=["png", "jpg", "jpeg"],
        help="Upload a screenshot of any trading chart (stocks, forex, crypto, commodities, etc.)"
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Chart", use_container_width=True)

        # Convert image to base64 for API
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

with col2:
    st.subheader("📈 Analysis Results")

    if uploaded_file and api_key:
        if st.button("🔍 Analyze Chart"):
            with st.spinner("Analyzing chart with AI..."):
                try:
                    client = openai.OpenAI(api_key=api_key)

                    # Build dynamic prompt from user inputs
                    asset_line = f"Asset: {asset_name}" if asset_name else "Asset: Unknown (identify from chart if possible)"
                    timeframe_line = f"Timeframe: {timeframe}"
                    market_line = f"Market Type: {market_type}"
                    context_line = f"\nAdditional context provided by user:\n{extra_context}" if extra_context.strip() else ""

                    analysis_prompt = f"""You are a professional technical analyst with expertise across all financial markets including stocks, forex, crypto, commodities, and indices.

Analyze the uploaded trading chart with the following details:
- {asset_line}
- {timeframe_line}
- {market_line}{context_line}

Based on what you can see in the chart, provide a concise technical analysis covering:
1) Current trend and momentum
2) Key support and resistance levels
3) Notable chart patterns or indicator signals (if visible)
4) Short-term outlook and suggested action (long / short / wait)

Keep the response under 250 words. Be direct, specific, and actionable."""

                    chat = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": analysis_prompt},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/png;base64,{img_base64}"
                                        }
                                    }
                                ]
                            }
                        ]
                    )

                    analysis_result = chat.choices[0].message.content

                    st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                    st.markdown(analysis_result)
                    st.markdown('</div>', unsafe_allow_html=True)

                    st.success("✅ Analysis completed!")

                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")
                    st.info("Please check your API key and try again.")

    elif not api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to proceed.")
    else:
        st.info("👆 Upload a chart image to get started")

# How to use section
st.divider()
st.markdown("""
### 📌 How to Use:
1. **Enter** your OpenAI API key and fill in the chart details in the sidebar
2. **Upload** a screenshot of any trading chart (stocks, forex, crypto, commodities, indices)
3. **Click** "Analyze Chart" to receive AI-powered technical analysis
4. **Review** the analysis to support your trading decisions

**Supported Markets:** Crypto · Stocks · Forex · Commodities · Indices · Any chart you can screenshot

**Note**: This tool provides analytical insights only. Always do your own research and manage risk appropriately.
""")

# Footer
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    Powered by OpenAI GPT-4o Vision • For Educational Purposes Only
</div>
""", unsafe_allow_html=True)
