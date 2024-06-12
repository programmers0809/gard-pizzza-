from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # For now, we'll just return a success message
    return jsonify({'message': f'Thank you, {name}! Your message has been sent.'})

if __name__ == '__main__':
    app.run(debug=True)
