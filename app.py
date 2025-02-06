import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined questions and answers
qa_pairs = {
    "what is ccc": "This is a Controlling & Planning CoE Analyst position located in Bengaluru, India...",
    "who is nrupesh mastakar": "Nrupesh Mastakar is the Head of Controlling Capability Centers in Bangalore.",
    "who is debadutta rath": "Debadutta Rath is the Global Practice Head & Owner - Digital & Artificial Intelligence Lab.",
    "who is the head of digital and ai labs": "Debadutta Rath.",
    "who is senior delivery manager in ai and digital team": "Saneesh.",
    "who is the solution architect in ai and digital labs": "Sanjay Chandra.",
    "who is the tech lead in ai and digital team": "Ramya Lingraj.",
    "expand ccc": "Controlling Capabilities Centers.",
    "ccc belongs to which vertical of hitachi group": "Green Energy and Mobility.",
}

# Function to clean user input (remove punctuation and lowercase it)
def clean_text(text):
    text = text.lower().strip()  # Convert to lowercase and remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    user_question = request.json.get("question", "")
    user_question = clean_text(user_question)  # Normalize input

    answer = qa_pairs.get(user_question, "Sorry, I don't have an answer for that.")
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
