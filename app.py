from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import config  ,cohere

app = Flask(__name__)


# Your Twilio account SID and auth token
account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_TOKEN
client = Client(account_sid, auth_token)

# The WhatsApp phone number assigned to your Twilio account
whatsapp_number = 'whatsapp:+14155238886'



@app.route('/', methods = ['GET'])
def index():
    return 'Welcome to chatbot page'


@app.route('/bot', methods=['POST'])
def bot():
    # Get the incoming message from the user
    incoming_msg = request.values.get('Body', '').lower()

    # Create a response object
    resp = MessagingResponse()
    print(incoming_msg)
    

    # # If the user sends "hello", respond with a greeting
    # if 'hello' in incoming_msg:
    #     resp.message('Hello! How can I assist you today?')

    # # If the user sends "bye", respond with a farewell
    # elif 'bye' in incoming_msg:
    #     resp.message('Goodbye! Have a nice day.')

    # # If the user sends anything else, respond with an error message
    # else:
    #     resp.message('I\'m sorry, I don\'t understand. Please try again.')

    # # Send the response back to the user
    # return str(resp)




DEBUG_MODE  = True
if __name__ == '__main__':
    app.run(debug=DEBUG_MODE)

