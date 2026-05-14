from flask import Flask, jsonify, request
from flask_cors import CORS
from db import connect_db

app = Flask(__name__)
CORS(app)

# 📊 Get all data
@app.route('/data')
def get_data():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM records ORDER BY cycle ASC")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "cycle": row[1],
            "sunlight": row[2],
            "moisture": row[3],
            "power": row[4],
            "pump": row[5]
        })

    cursor.close()
    db.close()

    return jsonify(data)

# ➕ Add data
@app.route('/add', methods=['POST'])
def add_data():
    db = connect_db()
    cursor = db.cursor()

    data = request.json

    query = """
    INSERT INTO records (cycle, sunlight, moisture, power, pump)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        data['cycle'],
        data['sunlight'],
        data['moisture'],
        data['power'],
        data['pump']
    ))

    db.commit()
    cursor.close()
    db.close()

    return {"message": "Data added successfully"}

if __name__ == '__main__':
    app.run(debug=True)