from databases.share_functions import connect
from flask import request, jsonify

def buy():
    data = request.get_json()
    ingredientName = data.get("IngredientName")
    qty = data.get("Qty")

    db, cursor = connect()

    sql = f'''
        select IngrdID
        from Ingredient
        where IngrdName = '{ingredientName}'
    '''
    cursor.execute(sql)

    row = cursor.fetchone()
    # print('here 3')
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
    # print(sql)
    
    cursor.execute('SELECT * FROM Fridge WHERE IngredID = %s', (ingrdID,))
    columns = ['IngredientID', 'FridgeQty']
    row = dict(zip(columns, cursor.fetchone())) 


    return row