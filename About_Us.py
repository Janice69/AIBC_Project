import streamlit as st

# Title with a suitable logo
st.markdown("# **About Us**")

# Project Scope with Icon
st.markdown("### 🎯 **Project Scope**")
st.markdown("""
**HDB Resale Insights** comprises two main modules:

1. **Ask the Resale Genie**: An AI-powered chatbot that offers instant and accurate responses to your inquiries about HDB resale procedures.
2. **HDB PricePulse**: A predictive analytics tool that estimates resale prices and visualizes market trends to support informed decision-making.
""")

# Objectives with Icon
st.markdown("### 🏆 **Objectives**")
st.markdown("""
- **Empower Users**: Provide easy access to comprehensive information on HDB resale procedures and eligibility criteria.
- **Predictive Analytics**: Utilize machine learning models to deliver accurate resale price predictions based on historical data.
- **Data-Driven Decisions**: Present market trends and comparisons through interactive charts, enabling users to stay informed about the HDB resale landscape.
- **User-Friendly Interface**: Develop an intuitive and secure platform with password protection to ensure a personalized user experience.
""")

# Data Sources with Icon
st.markdown("### 📊 **Data Sources**")
st.markdown("""
Our application leverages data from the following sources:

1. **HDB Official Website**: We scrape and process information from the HDB website to ensure our chatbot accesses the latest and most accurate resale procedure guidelines and eligibility criteria.
- **URLs Scraped**:
  - [Buying Procedure for Resale Flats](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats)
  - [Overview of Buying Procedure](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/overview)
  - [Eligibility and Housing Loan Options](https://www.hdb.gov.sg/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter)
  - [Plan, Source, and Contract](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract)
  - [Planning Considerations](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations)
  - [Mode of Financing](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/mode-of-financing)
  - [Option to Purchase](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/option-to-purchase)
  - [Request for Value](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/request-for-value)
  - [Resale Application](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/application)
  - [Acceptance and Approval](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/acceptance-and-approval)
  - [Resale Completion](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-completion)
  - [Conditions After Buying](https://www.hdb.gov.sg/residential/buying-a-flat/conditions-after-buying)

2. **Resale Dataset**: A comprehensive CSV dataset containing historical resale prices, flat types, town locations, and other pertinent features essential for training our predictive models.
- **Dataset Source**: Downloaded from [Data.gov.sg](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view) and hosted locally.
""")

# Features Section with Icon
st.markdown("### ✨ **Features**")

# 1. Ask the Resale Genie
st.markdown("#### 1. **Ask the Resale Genie**")
st.markdown("""
- **AI-Powered Chatbot**: Implements the Retrieval-Augmented Generation (RAG) approach by integrating LangChain, Chroma Vector Store, and OpenAI's Language Models. This chatbot understands and processes user queries to provide concise and accurate responses, ensuring you receive the information you need promptly.
- **Contextual Understanding**: Leverages context from scraped HDB data to deliver relevant and reliable answers, minimizing the risk of misinformation.
""")

# 2. HDB PricePulse
st.markdown("#### 2. **HDB PricePulse**")
st.markdown("""
- **Resale Price Prediction**: Utilizes a Linear Regression model to forecast resale prices based on inputs such as town, flat type, storey range, floor area, remaining lease years, and temporal factors.
- **Interactive Input Fields**: Allows users to input specific details about their desired flat to receive personalized price estimates.
- **Real-Time Predictions**: Provides instant price predictions, assisting users in making informed buying or selling decisions.
""")

# 3. Market Trend Visualizations
st.markdown("#### 3. **Market Trend Visualizations**")
st.markdown("""
- **Resale Price Trend Over Years**: Displays the average resale prices over the years, highlighting market fluctuations and growth patterns.
- **Average Resale Price by Flat Type (2024)**: Compares the average resale prices across different flat types for the current year, helping users identify the most valuable options.
- **Average Resale Price by Town (2024)**: Presents a comparative analysis of average resale prices across various towns, enabling users to determine the best locations for investment.
""")

if __name__ == "__main__":
    # Removed the unwanted section
    pass
