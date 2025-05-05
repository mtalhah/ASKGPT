🚀 INTRODUCING ASK GPT
A smarter way to visualize ChatGPT responses

🧠 Overview
Ask GPT is an interactive application that visualizes responses from ChatGPT, transforming them into a more data-centric, insightful, and easy-to-understand format. The application highlights key topics, relevance, sentiment, and even provides voice narration of the results.

⚙️ Setup Instructions
🔑 API Key
To use this application, you need an active OpenAI API key.
👉 Open GPT_func.py and add your API key in the specified section.

🏁 Run the Application
The main file is QT7.py.

bash
Copy
Edit
python QT7.py
💬 How to Use
Enter your prompt in the input field.

Click the 🔍 Search button to:

Receive a full GPT response

View an interactive knowledge graph

Get sentiment analysis and relevance analysis

Click the 🔊 Speaker button to enable voice narration of the response.

📚 About the Application
The app receives a user query and fetches a response using ChatGPT.

The SciTopic.py module extracts key topics from the response using NLP techniques.

Each topic is then queried to build a mini knowledge base, which is summarized and displayed as a concise description.

pyvis_kg.py uses ChatGPT’s JSON responses to generate an interactive knowledge graph using PyVis:

🟢 Nodes represent key topics

🔗 Edges represent relationships between them

🖱️ Hovering displays brief topic descriptions

The graph is shown in a WebView using nx.html

📊 Analysis Features
Sentiment Analysis
Displays sentiment scores via radar charts using sentiment_scores.py

Relevance Analysis
Scores topic relevance and visualizes it with radar charts using relevance_scores.py

Feel free to contribute, raise issues, or suggest improvements! ✨
Happy exploring with Ask GPT!
