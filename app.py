from flask import Flask, request, jsonify,  render_template
import requests
from bardapi import Bard
import os
import re

#setting my licenjse key (your unique password to acess api )
os.environ['_BARD_API_KEY']="XAgr0MttfUyCjcTgtg_5GOhDz8ohfLedNK_BZjYfmuyvW2kGiR_N0A0L0TMEemZx_HCWKg."

# creating bard object variable 
bard = Bard()

app = Flask(__name__)

# This is the new function for formatting server responses
def format_server_response(raw_response):
    # Replace "\r\n" with "<br>" for line breaks in HTML
    raw_response = raw_response.replace('\r\n', '<br>')

    # Replace asterisks with list items
    raw_response = raw_response.replace('* ', '<li>') + '</li>'

    # Wrap list items with <ul> tags
    raw_response = '<ul>' + raw_response + '</ul>'

    # Remove image references
    raw_response = re.sub(r'\[Image of [^\]]*\]', '', raw_response)

    return raw_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    # get user question
    user_message = request.values.get('message')
    # get api response from bard 
    server_message = bard.get_answer(user_message)['content']

    formatted_response = format_server_response(server_message)
    
    return jsonify({'message': formatted_response})

if __name__ == '__main__':
    app.run(debug=True)
