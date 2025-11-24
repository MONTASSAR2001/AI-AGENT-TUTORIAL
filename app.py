from flask import Flask, render_template, request, jsonify
from main import ask_agent

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    if not user_input:
        return jsonify({"response": "Please send a message!"})
    
    ai_response = ask_agent(user_input)
    
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)