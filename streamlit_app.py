from phi.model.groq import Groq
from phi.agent import Agent 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()


st.title("Stock Market Analyst AI-Agent")
chat_placeholder = st.container()


# Creating web search agent

web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for th information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],  # Can have multiple tools 
    instructions = ["Always include sources"],
    show_tool_calls= True,
    markdown=True
    
)


# Creating Finance agent

finance_agent = Agent(
    name = "Finance Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price= True, analyst_recommendations= True ,stock_fundamentals=True )] , # Can have multiple tools 
    instructions = ["Always display the data in the form of Tables"],
    show_tool_calls= True,
    markdown=True  
)


#Multi AI Agent ( Combining two or more agents make a Multi Model AI Agent)



multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "display the data in the form of Tables"],
    show_tool_calls=True,
    markdown=True,
)

# if "message" not in st.session_state:
#     st.session_state.message = []

if query := st.chat_input("Please Enter your query here!"):
    # st.session_state.message.append(query)
    with st.chat_message("user"):
        st.markdown(query)
        
    with st.chat_message("assistant"):
        # response = multi_ai_agent.print_response(query)
        # print(response)
        st.markdown(multi_ai_agent.run(query).content)
        

