import sqlite3


class SQLite3Database:
    def __init__(self):
        # Initialize SQLite DB
        self.DB_NAME = "database/history.db"
        self.__init_db()

    def __init_db(self):
        """Create table if it does not exist."""
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS requests_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                response TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def save_request(self, question, response):
        """Save a request in db."""
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO requests_history (question, response)
            VALUES (?, ?)
        """, (question, response))
        conn.commit()
        conn.close()

    def get_history(self, limit=20):
        """Get 10 last requests."""
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT question, response, timestamp FROM requests_history
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))
        history = cursor.fetchall()
        conn.close()
        return history
