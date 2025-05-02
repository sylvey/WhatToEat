from databases.share_functions import connect
from flask import request, jsonify

def get_restaurants():
    data = request.get_json()

    cuisine_type = data.get("CuisineType")
    price_min = data.get("PriceMin")
    price_max = data.get("PriceMax")
    mood = data.get("Mood")

    conn, cursor = connect()

    query = """
        SELECT DISTINCT r.RstrntID AS RestaurantID, r.RstrntName AS RestaurantName
        FROM Restaurant r
        JOIN Menu m ON r.RstrntID = m.RstrntID
        JOIN Option o ON m.OptID = o.OptID
        WHERE o.CuisineType = %s
          AND o.Mood = %s
          AND m.Price BETWEEN %s AND %s
    """
    cursor.execute(query, (cuisine_type, mood, price_min, price_max))

    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return jsonify(results)


def get_menu():
    data = request.get_json()
    restaurant_id = data.get("RestaurantID")

    conn, cursor = connect()

    query = """
        SELECT o.OptID AS MealID, o.MealName
        FROM Menu m
        JOIN Option o ON m.OptID = o.OptID
        WHERE m.RstrntID = %s
    """
    cursor.execute(query, (restaurant_id,))

    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return jsonify(results)