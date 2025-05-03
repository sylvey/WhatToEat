from flask import Flask, jsonify, render_template, request
from databases.databases import connect, recipeIngredients, fridgeContents, get_menu, get_restaurants, buy, use, useRecipe, available_meal_option, available_meal_option_content, next_meal


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

@app.route('/getRestaurants', methods=['POST'])
def route_get_restaurants():
    return get_restaurants()

@app.route('/getAvailableMealOption', methods=['POST'])
def getAvailableMealOption():
    return available_meal_option()

@app.route('/getAvailableMealOptionContent', methods=['POST'])
def getAvailableMealOptionContent():
    return available_meal_option_content()

@app.route('/getNextMeal', methods=['POST'])
def getNextMeal():
    option_list = available_meal_option()
    return next_meal(option_list)

@app.route('/getMenu', methods=['POST'])
def route_get_menu():
    return get_menu()

@app.route('/postBuy', methods=['POST'])
def postBuy():
    data = request.get_json()
    ingredientName = data.get("IngredientName")
    qty = data.get("Qty")
    return buy(ingredientName, qty)

@app.route('/postUse', methods=['POST'])
def postUse():
    data = request.get_json()
    ingredientName = data.get("IngredientName")
    qty = data.get("Qty")
    return use(ingredientName, qty)

@app.route('/postUseRecipe', methods=['POST'])
def postUseRecipe():
    data = request.get_json()
    recipeID = data.get("RecipeID")
    IncludeOptional = data.get("IncludeOptional")
    return useRecipe(recipeID, IncludeOptional)


if __name__ == '__main__':
    app.run('0.0.0.0', 8081, debug=True)


