from databases.share_functions import connect
from flask import request, jsonify
from databases.ingredients import recipeIngredients

def buy(ingredientName, qty):
    db, cursor = connect()

    sql = f'''
        select IngrdID
        from Ingredient
        where IngrdName = '{ingredientName}'
    '''
    cursor.execute(sql)

    row = cursor.fetchone()
    ingrdID = row[0] if row else None

    
    if ingrdID is None:
        
        sql = f'''
            INSERT INTO `Ingredient` (`IngrdName`) VALUES ('{ingredientName}');
        '''
        cursor.execute(sql)
        
        ingrdID = cursor.lastrowid


    sql = f'''
        INSERT INTO Fridge (IngredID, Qty)
        VALUES ({ingrdID}, {qty})
        ON DUPLICATE KEY UPDATE Qty = Qty + VALUES(Qty)
    '''
    cursor.execute(sql)
    db.commit()
    
    cursor.execute('SELECT * FROM Fridge WHERE IngredID = %s', (ingrdID,))
    columns = ['IngredientID', 'FridgeQty']
    row = dict(zip(columns, cursor.fetchone())) 


    return row


def use(ingredientName, qty):
    db, cursor = connect()

    sql = f'''
        select IngrdID
        from Ingredient
        where IngrdName = '{ingredientName}'
    '''
    cursor.execute(sql)

    row = cursor.fetchone()
    ingrdID = row[0] if row else None
    
    print('ingrdID1:', ingrdID)
    
    if ingrdID is None:
        return f"There's no {ingredientName} in your fridge."
    
    sql = f'''
        select IngredID
        from Fridge
        where IngredID = {ingrdID}
    '''
    print(sql)
    cursor.execute(sql)
    row = cursor.fetchall()
    if len(row) == 0:
        print('row:', row)
        return f"There's no {ingredientName} in your fridge."

    sql = f'''
        UPDATE Fridge
        SET Qty = GREATEST(Qty - {qty}, 0)
        WHERE IngredID = {ingrdID}
    '''
    cursor.execute(sql)
    db.commit()
    
    cursor.execute('SELECT * FROM Fridge WHERE IngredID = %s', (ingrdID,))
    columns = ['IngredientID', 'FridgeQty']
    row = dict(zip(columns, cursor.fetchone())) 


    return row


def useRecipe(recipeID, includeOptional):
    all_ingred = recipeIngredients(recipeID)

    results = []
    for ingred in all_ingred:
        if includeOptional:
            results.append({"IngredientName": ingred['IngredientName'], **use(ingred['IngredientName'], ingred['RequiredQty'])})
        else:
            if ingred['Optional'] == False:
                results.append({"IngredientName": ingred['IngredientName'], **use(ingred['IngredientName'], ingred['RequiredQty'])})
    

    return results