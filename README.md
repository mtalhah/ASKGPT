INTRODUCING ASK GPT !!

This project aims to visualise the responses 
received form chatGPT , making the responses
more data centric and easier to draw conclusions
from .

STEPS TO INITIALIZE 

1. API KEY : the use of this application requires
an active openai API key, modify GPT_func.py to
specify API key

2. MAIN : QT7.py is the main file, run QT7.py

3. PROMPT: enter your prompt and click search button
to receive full response , knowledge graph of the response
, sentiment analysis and relevance analysis .
voice narration can be avtivated using the speaker button


ABOUT THE APPLICATION 

The application takes in a user query and analyses the response from chatgpt , 
the SciTopic.py module is used to retrieve "topics" from the initial response from chatGPT using language processing concepts.
Then the "topics" are sent as queries and their responses are compiled to create a knowledge base. 
this knowledge base is them summarised to be displayed as "description".
To visualize the data we use the pyvis_kg.py , which uses the json response from chatGPT to structure the knowledge graph. The knowledge graph is interactive , as in hovering over it would display a short description , it contains nodes and edges describing the relationship between each topic .
to display the knowledge graph we use nx.html and dsplay it in webview.

Then the we perform sentiment and relevance analysis on the knowledge base and use radar charts to display sentiment and relevance , we use a scoring system to represent this data , which can be found in sentiment_scores.py and relevance_scores.py


