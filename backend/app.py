from flask import Flask, jsonify, render_template, request
from databases.databases import connect, recipeIngredients, fridgeContents


app = Flask(__name__, static_folder="build/static", template_folder="build")

app.config['JSON_AS_ASCII'] = False

# CORS(app, resources={r"/.*": {"origins": ["*"]}})

@app.route('/')
@app.route("/helloWorld", methods=['GET'])
def helloWorld():
    conn = connect()
    print(conn)
    return 'hello world'

@app.route("/getRecipeIngredients/<OptionID>", methods=['GET'])
def getRecipeIngredients(OptionID):  
    return recipeIngredients(OptionID) 

@app.route("/getFridgeContent", methods=['GET'])
def getFridgeContent():
    return fridgeContents()


if __name__ == '__main__':
    app.run('0.0.0.0', 8081, debug=True)