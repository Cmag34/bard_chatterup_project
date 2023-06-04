from flask import Flask, request, jsonify,  render_template
import requests
from bardapi import Bard
import os

#setting my licenjse key (your unique password to acess api )
os.environ['_BARD_API_KEY']="XAgr0MttfUyCjcTgtg_5GOhDz8ohfLedNK_BZjYfmuyvW2kGiR_N0A0L0TMEemZx_HCWKg."

# creating bard object variable 
bard = Bard()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    # get user question
    user_message = request.values.get('message')
    # get api response from bard 
    server_message = bard.get_answer(user_message)['content']

    return jsonify({'message': server_message})

if __name__ == '__main__':
    app.run(debug=True)
