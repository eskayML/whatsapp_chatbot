import config , cohere


co = cohere.Client(config.COHERE_API_KEY)


prompt = 'Give a  name for a plant based restaurant'


response = co.generate(  
    model='command-xlarge-nightly',  
    prompt = prompt,  
    max_tokens=40,  
    temperature=0.6,  
    stop_sequences=["--"])


print(response)
