import random
import string

from typing import List

def generate_random_password(password_len=10):
    chars = string.digits + \
            string.ascii_letters + \
            string.punctuation

    result = ''
    for _ in range(password_len):
        result += random.choice(chars)
    return result

def exec_query(query: str) -> List[tuple]:
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result
