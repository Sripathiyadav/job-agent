import sqlite3

DB_NAME = "jobs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        url TEXT,
        source TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS saved_jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_user_id INTEGER,
        job_id INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_user_id INTEGER,
        job_id INTEGER,
        status TEXT,
        applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized")

def add_job(title, company, location, url, source):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO jobs
        (title, company, location, url, source)
        VALUES (?, ?, ?, ?, ?)
    """, (title, company, location, url, source))

    conn.commit()
    conn.close()


def get_jobs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, company, location
        FROM jobs
        ORDER BY id DESC
        LIMIT 10
    """)

    jobs = cursor.fetchall()

    conn.close()

    return jobs

def get_job_by_id(job_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, company, location, url, source
        FROM jobs
        WHERE id = ?
    """, (job_id,))

    job = cursor.fetchone()

    conn.close()

    return job

def save_job(telegram_user_id, job_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO saved_jobs
        (telegram_user_id, job_id)
        VALUES (?, ?)
    """, (telegram_user_id, job_id))

    conn.commit()
    conn.close()

def get_saved_jobs(telegram_user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT jobs.id,
               jobs.title,
               jobs.location
        FROM saved_jobs
        JOIN jobs
        ON saved_jobs.job_id = jobs.id
        WHERE saved_jobs.telegram_user_id = ?
    """, (telegram_user_id,))

    jobs = cursor.fetchall()

    conn.close()

    return jobs

if __name__ == "__main__":
    init_db()