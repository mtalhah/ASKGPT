import openai


#init GPT ENGINE
openai.api_key = ''# API KEY REQUIRED


def Ask(query):

    conversation = [{"role": "system", "content": "You are a knowledge database ,response must be information oriented"}]
    conversation.append({"role": "user", "content": query})
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )
    return response['choices'][0]['message']['content']

def text2json(text):
    conversation = [{"role": "system", "content": "You are a helpful assistant"}]
    conversation.append({"role": "user", "content": 'Elaborate on:'+text+'''.represent the response for the given query as knowledge graph with JSON format (min. 5 nodes):
{
  "nodes": [
    {
      "id": "<non-numeric only>",
      "type": "",
      "description": ""                
    }],
 "edges": [
    {
      "source": "",
      "target": "",
      "relationship": ""
    }]
 }'''})
    
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )
    return response['choices'][0]['message']['content']


