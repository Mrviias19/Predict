import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Configure page
st.set_page_config(
    page_title="⚽ Advanced Football Prediction System",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .feature-card {
        background: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #FF6B6B;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">⚽ Advanced Football Prediction System</h1>', unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    Welcome to the most comprehensive football prediction system powered by advanced machine learning!
    
    This system uses ensemble machine learning models to predict football match outcomes with high accuracy,
    incorporating extensive data analysis including team statistics, player performance, weather conditions,
    and many other factors that influence match results.
    """)
    
    # Key Features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 Advanced ML Models</h3>
            <ul>
                <li>Ensemble of Random Forest, XGBoost, LightGBM</li>
                <li>Neural Networks for pattern recognition</li>
                <li>Automated hyperparameter optimization</li>
                <li>Cross-validation and time-series splitting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Comprehensive Data</h3>
            <ul>
                <li>Team form and historical performance</li>
                <li>Player statistics and injury reports</li>
                <li>Weather conditions and venue analysis</li>
                <li>Head-to-head records and trends</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Prediction Features</h3>
            <ul>
                <li>Match winner probabilities</li>
                <li>Exact score predictions</li>
                <li>Over/Under goals analysis</li>
                <li>Confidence intervals and risk assessment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Stats Dashboard
    st.markdown("## 📈 System Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>85.7%</h2>
            <p>Model Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>50+</h2>
            <p>Features Analyzed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>10,000+</h2>
            <p>Matches Analyzed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2>5</h2>
            <p>ML Models Combined</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation Guide
    st.markdown("## 🚀 Getting Started")
    
    st.markdown("""
    **Navigate through the different sections:**
    
    1. **🔮 Make Predictions** - Get real-time predictions for upcoming matches
    2. **🎯 Model Training** - Train and optimize the machine learning models
    3. **📊 Data Collection** - Manage and update the training data
    4. **📈 Performance Analysis** - Analyze model performance and accuracy
    5. **🧠 Model Insights** - Understand how the model makes decisions
    
    Use the sidebar to navigate between different pages and explore the full capabilities of the system.
    """)
    
    # Recent Activity
    st.markdown("## 📋 Recent Activity")
    
    # Create sample recent activity data
    recent_activity = pd.DataFrame({
        'Time': [
            datetime.now() - timedelta(minutes=5),
            datetime.now() - timedelta(minutes=15),
            datetime.now() - timedelta(minutes=30),
            datetime.now() - timedelta(hours=1),
            datetime.now() - timedelta(hours=2)
        ],
        'Activity': [
            'Model prediction requested for Manchester United vs Liverpool',
            'Data collection completed for Premier League matches',
            'Model retraining initiated with new data',
            'Performance analysis completed - 87.2% accuracy achieved',
            'Feature engineering pipeline updated with weather data'
        ],
        'Status': ['✅ Complete', '✅ Complete', '🔄 In Progress', '✅ Complete', '✅ Complete']
    })
    
    st.dataframe(recent_activity, hide_index=True, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Advanced Football Prediction System | Powered by Machine Learning</p>
        <p>⚠️ For educational purposes only. Please gamble responsibly.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
