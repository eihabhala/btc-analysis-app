import streamlit as st
import openai
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="BTC Technical Analysis",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF9500;
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
        border-left: 4px solid #FF9500;
        margin: 20px 0;
    }
    .stButton>button {
        background-color: #FF9500;
        color: white;
        font-weight: bold;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header">📊 BTC Perpetual Contract Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Powered Technical Analysis for BTCUSDT 5-Minute Timeframe</div>', unsafe_allow_html=True)

# API Key section
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Enter your OpenAI API key"
    )
    
    st.divider()
    
    st.info("""
    **Current Price**: $67,259.8
    
    **Session Change**: +$1,269.1 (+1.92%)
    
    **Status**: Session green but fading
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📷 Upload Chart Image")
    uploaded_file = st.file_uploader(
        "Upload BTCUSDT chart screenshot",
        type=["png", "jpg", "jpeg"],
        help="Upload a screenshot of your BTCUSDT perpetual contract chart"
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
                    # Initialize OpenAI client
                    client = openai.OpenAI(
                        api_key=api_key,
                    )
                    
                    # Prepare the analysis prompt
                    analysis_prompt = """You are a professional crypto trader and BTC analyst. Analyze this BTCUSDT Perpetual Contract chart on 5-minute timeframe from Bybit. 

Current market context:
- Current price: $67,259.8
- OHLC: O:67,316.5 H:67,344.6 L:67,255.0 C:67,259.8
- Change: +$1,269.1 (+1.92%)
- Session green but fading — BTC dropped from $67,540 (14:15) to $67,260 now, a $280 slide
- Red candle (C < O by $56.7) closing near low
- MACD near zero at +0.1, momentum stalling
- BTC session gains are being given back — from +2.35% peak to +1.92% now
- Price broke below 67,348 support zone (now resistance)

Key Levels:
- Nearest resistance at 67,348.2 (red level just above)
- 67,482.2 (green dotted) and 67,620.6 are higher barriers
- Support at 67,037.4 (red level) is the next floor
- 64,928.2 as major support far below
- Major resistance at 68,199.9 (red level above)

Recent signals:
- Long entry near 67,037.4 (support)
- Short entry near 67,482.2 (resistance)
- Buy zone at 64,928.2
- Sell zone at 68,199.9 (major resistance)

Provide a concise analysis covering:
1) Current trend and momentum
2) Key support/resistance levels
3) Signal quality assessment
4) Short-term outlook and suggested action

Keep it under 200 words and be direct."""

                    # Make API call
                    chat = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{
                            "role": "user",
                            "content": analysis_prompt
                        }]
                    )
                    
                    analysis_result = chat.choices[0].message.content
                    
                    # Display results
                    st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                    st.markdown(analysis_result)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.success("✅ Analysis completed!")
                    
                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")
                    st.info("Please check your API key and try again.")
    
    elif not api_key:
        st.warning("⚠️ Please enter your API key in the sidebar to proceed.")
    else:
        st.info("👆 Upload a chart image to get started")

# Additional info section
st.divider()
st.markdown("""
### 📌 How to Use:
1. **Upload** a screenshot of your BTCUSDT perpetual contract chart (5-minute timeframe recommended)
2. **Click** "Analyze Chart" to get AI-powered technical analysis
3. **Review** the analysis for trading decisions

**Note**: This tool provides analytical insights only. Always do your own research and manage risk appropriately.
""")

# Footer
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    Powered by OpenAI API • For Educational Purposes Only
</div>
""", unsafe_allow_html=True)
