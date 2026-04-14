import sqlite3
import json

# ================= CONFIG =================
DB_NAME = "nox.db"

# ================= INIT DATABASE =================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        input_data TEXT,
        prediction REAL,
        top_features TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# ================= INSERT DATA =================
def insert_prediction(email, input_data, prediction, top_features=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO predictions (user_email, input_data, prediction, top_features)
        VALUES (?, ?, ?, ?)
        """, (
            email,
            json.dumps(input_data),            # store full input as JSON
            float(prediction),                 # ensure numeric
            json.dumps(top_features) if top_features else None
        ))

        conn.commit()

    except Exception as e:
        print("❌ DB Insert Error:", e)

    finally:
        conn.close()


# ================= FETCH USER DATA =================
def get_user_predictions(email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT input_data, prediction, top_features, timestamp
    FROM predictions
    WHERE user_email = ?
    ORDER BY timestamp DESC
    """, (email,))

    rows = cursor.fetchall()

    conn.close()
    return rows


# ================= OPTIONAL: DELETE USER HISTORY =================
def delete_user_history(email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        DELETE FROM predictions
        WHERE user_email = ?
        """, (email,))

        conn.commit()

    except Exception as e:
        print("❌ Delete Error:", e)

    finally:
        conn.close()


# ================= OPTIONAL: CLEAR ALL DATA =================
def clear_all_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM predictions")
        conn.commit()
    except Exception as e:
        print("❌ Clear Error:", e)
    finally:
        conn.close()