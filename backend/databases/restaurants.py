from databases.share_functions import connect
from flask import request, jsonify

def get_restaurants():
    data = request.get_json()

    cuisine_type = data.get("CuisineType")
    price_min = data.get("PriceMin", 0.0)
    price_max = data.get("PriceMax", 1e9)
    mood = data.get("Mood")

    conn, cursor = connect()

    # 基礎查詢
    query = """
        SELECT DISTINCT r.RstrntID AS RestaurantID, r.RstrntName AS RestaurantName
        FROM Restaurant r
        JOIN Menu m ON r.RstrntID = m.RstrntID
        JOIN `Option` o ON m.OptID = o.OptID
        WHERE m.Price BETWEEN %s AND %s
    """
    params = [price_min, price_max]

    # 加入條件
    if cuisine_type:
        query += " AND o.CuisineType = %s"
        params.append(cuisine_type)

    if mood is not None:
        query += " AND o.Mood = %s"
        params.append(mood)

    cursor.execute(query, params)

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
        JOIN `Option` o ON m.OptID = o.OptID
        WHERE m.RstrntID = %s
    """
    cursor.execute(query, (restaurant_id,))

    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return jsonify(results)