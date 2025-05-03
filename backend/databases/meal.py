from databases.share_functions import connect
from flask import request, jsonify

def available_meal_option():
    input_data = request.get_json()

    eatOut = input_data.get("eatOut")
    mood = str(input_data.get("mood"))
    cuisine = input_data.get("CuisineType")

    db, cursor = connect()
    query = '''
        SELECT 
            OptID,
            MealName,
            EatOut,
            CuisineType,
            Mood
        FROM `Option`
        WHERE EatOut = %s AND Mood = %s AND CuisineType = %s
    '''

    cursor.execute(query, (eatOut, mood, cuisine))
    columns = [desc[0] for desc in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]

    db.close()

    return jsonify(result)

def next_meal(optID):
    db, cursor = connect()

    query = '''
        SELECT OptID, MealName, EatOut, CuisineType, Mood
        FROM `Option`
        WHERE OptID = %s
    '''
    cursor.execute(query, (opt_id,))
    row = cursor.fetchone()
    db.close()

    if not row:
        return jsonify({"error": "Meal not found"}), 404

    result = {
        "OptID": row[0],
        "MealName": row[1],
        "EatOut": row[2],
        "CuisineType": row[3],
        "Mood": int(row[4])
    }

    return jsonify(result)

