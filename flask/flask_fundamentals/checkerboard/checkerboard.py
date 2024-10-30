from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', defaults={'rows': 8, 'columns': 8, 'color1': "black", 'color2': "white"})
@app.route('/<int:rows>/', defaults={'columns': 8, 'color1': "black", 'color2': "white"})
@app.route('/<int:rows>/<int:columns>/', defaults={'color1': "black", 'color2': "white"})
@app.route('/<int:rows>/<int:columns>/<color1>', defaults={'color2': "white"})
@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def render_board(rows, columns, color1, color2):
    boxes= rows * columns
    colors = [color1 if (i + j) % 2 == 0 else color2 for i in range(rows) for j in range(columns)]
    return render_template("checkerboard.html", num_of_rows=rows, num_of_columns=columns,boxes_count=boxes, colors=colors)

if __name__=="__main__":
    app.run(debug=True)