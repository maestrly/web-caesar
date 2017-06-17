from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method= 'POST'>
            <label for="rotateby">Rotate by: </label>
            <input id= "rotateby" type='text' name="rot"/><br>
            <textarea name="text" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    num = int(request.form["rot"])
    words = request.form["text"]
    new_text = rotate_string(words, num)
    return "<h1>" + new_text + "</h1>"


app.run()
