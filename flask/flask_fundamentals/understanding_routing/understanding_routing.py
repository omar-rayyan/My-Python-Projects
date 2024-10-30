from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Champion')
def champion():
    return 'Champion!'

@app.route('/say/<name>')
def greet(name):
    return 'Hi' + name

@app.route('/repeat/<int:times>/<repeat_word>')
def repeat_word(times, repeat_word):
    return ' '.join([repeat_word] * times)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404
    
if __name__=="__main__":
    app.run(debug=True)