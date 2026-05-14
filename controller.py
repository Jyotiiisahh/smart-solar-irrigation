from flask import jsonify

@app.route("/data")
def get_data():
    raw_data = fetch_from_db()  # your current array-of-arrays
    formatted = []
    for row in raw_data:
        formatted.append({
            "cycle": row[0],
            "sunlight": row[2],
            "moisture": row[3],
            "power": row[4],
            "pump": row[5]
        })
    return jsonify(formatted)