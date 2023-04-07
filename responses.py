import cohere, config


class AIResponse:
    prompt = "write a reply that is very passive aggressive to the question just asked "

    def __init__(self, api_key) -> None:
        self.co = cohere.Config(config.COHERE_API_KEY)




    def reply(self):
        response = co.generate(
            model="command-xlarge-nightly",
            prompt=AIResponse.prompt,
            max_tokens=40,
            temperature=0.6,
            stop_sequences=["--"],
        )
        
        returned = response.generations[0].text
        return returned
    


