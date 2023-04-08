import config, cohere

co = cohere.Client(config.COHERE_API_KEY)

chat_input = 'who is your creator'


prompt = f"""
You are an AI chatbot built by eskayML, your name is Chadbot
Give a suitable reply to the statement below also making sure not to leave any sentence uncompleted
{chat_input}
"""


response = co.generate(
    model="command-xlarge-nightly",
    prompt=prompt,
    max_tokens=50,  
    frequency_penalty=.7, 
)




resp_text = response.generations[0].text

print(resp_text)
