import streamlit as st
import google.genai as genai
import json

# Configure page settings
st.set_page_config(page_title="AI Scam Detector", page_icon="🛡️")

# Initialize Gemini Client
# TODO: Replace with your actual Gemini API Key
client = genai.Client(api_key="client = genai.Client(api_key="YOUR_AI_API_KEY")")

def analyze_message(text: str) -> dict:
    """
    Analyzes the input text for potential phishing and scam indicators using Gemini.
    Returns a structured JSON response with risk score, flags, and explanation.
    """
    prompt = f"""
    Analyze the following message as a cybersecurity expert and evaluate the risk of phishing or scamming.
    Provide the response ONLY in the following JSON format, with no additional text or formatting:
    {{
        "risk_score": 92,
        "flags": ["Urgency Manipulation Detected", "Financial Request Detected"],
        "explanation": "Detailed professional analysis explaining why this text is suspicious or safe."
    }}

    Message to analyze:
    "{text}"
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config={'response_mime_type': 'application/json'}
    )
    
    return json.loads(response.text)

# --- UI Layout ---
st.title("🛡️ AI Scam Detector")
st.write("Paste a suspicious email or message below to perform an automated AI risk analysis.")

user_input = st.text_area("Message Text:", height=150, placeholder="e.g., Congratulations! You won a cash prize. Click here to claim now...")

if st.button("Analyze 🔍"):
    if user_input.strip():
        with st.spinner("Analyzing message indicators..."):
            try:
                # Execute security analysis
                analysis_result = analyze_message(user_input)
                risk_score = analysis_result["risk_score"]
                
                # Render risk status metric
                if risk_score > 70:
                    st.error(f"🚨 High Risk! Score: {risk_score}/100")
                elif risk_score > 40:
                    st.warning(f"⚠️ Medium Risk! Score: {risk_score}/100")
                else:
                    st.success(f"✅ Low Risk. Score: {risk_score}/100")
                
                # Render detected threat indicators
                st.subheader("Detected Indicators")
                for flag in analysis_result["flags"]:
                    st.markdown(f"• **{flag}**")
                
                # Render technical breakdown
                st.subheader("Technical Analysis")
                st.write(analysis_result["explanation"])
                
            except Exception as e:
                st.error(f"Analysis failed. Please verify API configuration. Error: {e}")
    else:
        st.warning("Please enter a valid message to analyze.")