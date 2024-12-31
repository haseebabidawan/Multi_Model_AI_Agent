 # 💼 Stock Market Analyst AI-Agent

This project is a Stock Market Analyst AI-Agent built using **Groq** and **Phidata**. The application integrates multiple AI agents to provide real-time stock information, analyst recommendations, and market trends. It leverages web search tools, financial data, and various APIs to generate detailed reports and insights.

### Project Overview
The AI-Agent combines two core functionalities:
1. **Web Search Agent**: Searches the web for up-to-date stock information using DuckDuckGo.
2. **Finance Agent**: Retrieves stock-related data such as stock prices, analyst recommendations, and stock fundamentals using Yahoo Finance APIs.

The AI-Agent utilizes **Groq** for its model and **Streamlit** for the user interface. The application provides an interactive, easy-to-use web interface where users can query stock information and receive detailed reports in a dynamic, user-friendly format.

## Features
- **Stock Information**: Get real-time stock prices, analyst recommendations, and stock fundamentals.
- **Web Search**: Retrieve up-to-date market data from the web.
- **Interactive UI**: Built with **Streamlit** for a simple yet effective interface.
- **Multi-Agent System**: Combines multiple agents for a comprehensive analysis of stock queries.

## Requirements
- Python 3.7 or higher
- Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
streamlit
phidata
dotenv
pandas
yfinance
duckduckgo
groq
```

## Setup Instructions
- **Clone the repository**:
```bash
  git clone https://github.com/your-username/stock-market-analyst.git
cd stock-market-analyst
```
- **Set up environment variables**:
1. Create a .env file in the root directory.
2. Add your API keys for Groq, DuckDuckGo, and Yahoo Finance (YFinance).

- **Run the Streamlit App: To run the application, use the following command**:
  ```bash
  streamlit run app.py
  ```
## How to Use the Application

1. **Start the app**: After running the app, it will open a web interface in your browser.
2. **Enter your query**: In the chat box, type the stock query you're interested in (e.g., "TSLA stock price", "NVDA analyst recommendations").
3. **View the results**: The AI-Agent will process your request, retrieve relevant data, and display the results in a table format if applicable.
4. **Clear Chat History**: You can clear the chat history by clicking the "Clear Chat History" button. This will reset the conversation and allow you to start fresh.

## Code Explanation

### Streamlit UI

- **Title**: The title of the app is set to “💼 Stock Market Analyst AI-Agent” and a brief description is displayed below.
- **Session State**: The session state is used to store and manage the conversation history.
- **Clear Chat History**: The "Clear Chat History" button clears the session state and triggers a balloon animation.

### Creating the Agents

1. **Web Search Agent**:
   - Uses the **Groq** model to search the web for stock-related information.
   - Utilizes **DuckDuckGo** as a search tool to gather real-time data from the web.

2. **Finance Agent**:
   - Uses the **Groq** model to fetch financial data from Yahoo Finance.
   - Can retrieve stock prices, analyst recommendations, and other fundamental data.

3. **Multi-Agent System**:
   - Combines the capabilities of both agents (Web Search and Finance) to provide comprehensive responses to stock-related queries.

### Streamlit Components and Interactivity

- **Chat Input**: A chat input box allows users to type in queries and communicate with the AI-Agent.
- **Displaying Responses**: The assistant’s response is displayed in the chat interface. If the response is in JSON format (like stock data), it is parsed and displayed as a table.
- **Session Management**: The conversation history is managed in the session state, ensuring that the conversation context is retained.

## Example Interaction

**User Query**:

**User**: "What are the analyst recommendations for TSLA?"

**AI Response**:

The AI-Agent will query the **Yahoo Finance API** and **DuckDuckGo** for relevant information and display the analyst recommendations in a table format:

| Stock | Strong Buy | Buy | Hold | Sell | Strong Sell |
|-------|------------|-----|------|------|-------------|
| TSLA  | 6          | 13  | 15   | 8    | 5           |

## How It Works

The AI-Agent utilizes the **Groq** model to process natural language queries. For finance-related queries, it accesses **Yahoo Finance** for stock prices, analyst ratings, and other relevant financial data. The **DuckDuckGo** tool helps gather additional data from the web, ensuring the AI-Agent stays up-to-date with real-time information.

## Troubleshooting

- **Environment Variables**: Ensure all API keys are correctly set in the `.env` file.
- **Missing Dependencies**: If you encounter errors regarding missing libraries, ensure all dependencies are installed via `pip install -r requirements.txt`.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Please make sure to follow the coding standards and write tests for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshots

### Running the Application
![Running App](Capture.png)

### Sample Query and Response
![Sample Query](Capture2.png)

---

### Notes:
1. Replace the placeholders like `https://github.com/your-username/stock-market-analyst.git` and `your-email@example.com` with your actual information.
2. Include images (like the ones referenced under **Screenshots**) in the `images/` folder in your repository.

Let me know if you need any other modifications!
