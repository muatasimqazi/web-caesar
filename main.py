from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = False

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Caesar Encryption</title>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>

          <form method="POST">
          <label for="rot">Rotate by: </label>
          <input type="text" name="rot" value="0">

          <textarea name="text">{0}</textarea>
          <br>
          <input type="submit" value="Submit Query">
          </form>
        </body>
    </html>
"""

@app.route('/', methods=['POST'])
def encrypt():
    str_1 = request.form['rot']
    str_2 = request.form['text']
    encrypted_str = rotate_string(str_2,int(str_1))

    return form.format(encrypted_str)

@app.route("/")
def index():
    return form.format('')

app.run()
