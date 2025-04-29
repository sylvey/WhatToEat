from databases.share_functions import connect


def recipeIngredients(recID):
    db, cursor = connect()

    cursor.execute(f'''
        Select `Ingredient`.IngrdID as IngredientID, `Ingredient`.IngrdName as IngredientName, `Fridge`.Qty >= Recipe.Qty as Avalibility, `Fridge`.Qty as FridgeQty, `Recipe`.Qty as RequiredQty, `Recipe`.Optional
        from `Recipe`
        join `Option` on `Option`.OptID = `Recipe`.OptID
        join `Ingredient` on `Ingredient`.IngrdID = `Recipe`.IngrdID
        join `Fridge` on `Fridge`.IngredID = `Recipe`.IngrdID
        where `Recipe`.OptID = {recID}
    ''') ## put your schema here
    columns = [desc[0] for desc in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]

    
    return result