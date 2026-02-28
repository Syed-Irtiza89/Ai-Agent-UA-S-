import sqlite3
import json
from datetime import datetime

class LongTermMemory:
    """Persistent storage for user preferences and past outcomes."""
    
    def __init__(self, db_path: str = "memory.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TIMESTAMP
            )
        """)
        self.conn.commit()

    def store(self, key: str, value: Any):
        """Rule 6.1: Store user preferences and confirmed outcomes."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO memory (key, value, updated_at) VALUES (?, ?, ?)",
            (key, json.dumps(value), datetime.now())
        )
        self.conn.commit()

    def retrieve(self, key: str) -> Optional[Any]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM memory WHERE key = ?", (key,))
        row = cursor.fetchone()
        return json.loads(row[0]) if row else None
