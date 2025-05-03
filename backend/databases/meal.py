from databases.share_functions import connect
from flask import request, jsonify
import random

def available_meal_option():
    input_data = request.get_json()

    eatOut = input_data.get("eatOut")
    mood = str(input_data.get("mood"))
    cuisine = input_data.get("CuisineType")

    db, cursor = connect()
    query = '''
        SELECT 
            OptID
        FROM `Option`
        WHERE EatOut = %s AND Mood = %s AND CuisineType = %s
    '''

    cursor.execute(query, (eatOut, mood, cuisine))
    result = [row[0] for row in cursor.fetchall()]

    db.close()

    return result

def available_meal_option_content():
    input_data = request.get_json()

    eatOut = input_data.get("eatOut")
    mood = input_data.get("mood")
    cuisine = input_data.get("CuisineType")

    db, cursor = connect()
    query = '''
        SELECT OptID, MealName, EatOut, CuisineType, Mood
        FROM `Option`
        WHERE EatOut = %s AND Mood = %s AND CuisineType = %s
    '''
    cursor.execute(query, (eatOut, mood, cuisine))
    rows = cursor.fetchall()
    db.close()

    result = []
    for row in rows:
        result.append({
            "OptID": row[0],
            "MealName": row[1],
            "EatOut": row[2],
            "CuisineType": row[3],
            "Mood": int(row[4])
        })

    return jsonify(result)


def next_meal(option_list):
    if not option_list:
        return jsonify({"error": "No available meal options"}), 404

    # Randomly select one meal from the option list
    selected = random.choice(option_list)

    return jsonify(selected)

