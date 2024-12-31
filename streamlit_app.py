from phi.model.groq import Groq
from phi.agent import Agent 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()


# Streamlit UI Tittle
st.title("💼 Stock Market Analyst AI-Agent")
st.markdown("This the stock finance AI agent built using Open source **Groq** and **Phidata** 📊🚀📈")
st.divider()

#Creating a session state for messages
if "messages" not in st.session_state.keys():
    st.session_state.messages = []
    
    
    
    
    
# Creating web search agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for th information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],  # Can have multiple tools 
    instructions = ["Always include sources"],
    # show_tool_calls= True,
    # markdown=True
    
)


# Creating Finance agent

finance_agent = Agent(
    name = "Finance Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price= True, analyst_recommendations= True ,stock_fundamentals=True )] , # Can have multiple tools 
    instructions = ["Always display the data in the form of Tables"],
    # show_tool_calls= True,
    # markdown=True  
)


#Multi AI Agent ( Combining two or more agents make a Multi Model AI Agent)



multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "display the data in the form of Tables"],
    # show_tool_calls=True,
    # markdown=True,
)


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.balloons()
         
         
prompt = st.chat_input("Please Enter your query here!")



if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user", "content" : prompt})
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = multi_ai_agent.run(prompt)
        response_content = response.content if hasattr(response, "content") else str(response)
       
        
        try:
            # If response content is JSON, attempt to display it as a table
            import pandas as pd

            # Try to parse the response as JSON (for example, if it's tabular data like stock data)
            data = pd.read_json(response_content)
            st.dataframe(data)  # Display as a dataframe (for tabular data)
        except Exception as e:
            # If it's not in JSON format, just display the response content as markdown
            st.markdown(response_content)
            
        st.session_state.messages.append({"role":"assistant", "content" : response_content})


