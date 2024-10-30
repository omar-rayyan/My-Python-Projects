from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/', defaults={'times': 5, 'color': '#9fc5f8'})
@app.route('/play/<int:times>/', defaults={'color': '#9fc5f8'})
@app.route('/play/<int:times>/<color>')
def render_boxes(times, color):
    return render_template("playground.html", num_of_boxes=times, color_of_boxes=color)

if __name__=="__main__":
    app.run(debug=True)