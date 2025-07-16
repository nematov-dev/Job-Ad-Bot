from database.db import cursor,conn

#Create table

def create_users_table():
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL,
        name VARCHAR(50),
        surname VARCHAR(50),
        username VARCHAR(50),
        created_at TIMESTAMP DEFAULT now(),
        UNIQUE(telegram_id)
        )"""
        cursor.execute(sql)
        conn.commit()

    except Exception as e:
        print(f"Xatolik mavjud: {e}")

#Create Worker Ads Table

def create_worker_ads_table():
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS worker_ads (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        name VARCHAR(100) NOT NULL,
        description TEXT,
        status BOOLEAN DEFAULT TRUE,
        chat_message_id BIGINT
        )"""
        cursor.execute(sql)
        conn.commit()

    except Exception as e:
        print(f"Xatolik: {e}")


# Creat Job Ads Table

def create_jobs_ads_table():
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS job_ads (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        chat_message_id BIGINT
        )"""
        cursor.execute(sql)
        conn.commit()

    except Exception as e:
        print(f"Xatolik: {e}")


#Add user

def add_user(telegram_id: int,name:str,surname: str,username: str):
    try:
        sql = """
        INSERT INTO users (telegram_id,name,surname,username)
        VALUES (%s,%s,%s,%s)"""
        cursor.execute(sql,(telegram_id,name,surname,username))
        conn.commit()
        return True
    
    except Exception as e:
        print(f"Xatolik mavjud: {e}")
        return False

#Check id

def check_id(telegram_id: int):
    try:
        sql = """
        SELECT * FROM users WHERE telegram_id = (%s)"""
        cursor.execute(sql,(telegram_id,))
        return cursor.fetchone()
    
    except Exception as e:
        print(f"Xatolik mavjud: {e}")
        return False
    
#Get all users id

def get_all_users_id():
    try:
        sql = """
        SELECT telegram_id FROM users"""
        cursor.execute(sql)
        result = cursor.fetchall()
        return [r[0] for r in result]
    
    except Exception as e:
        print(f"Xatolik mavjud: {e}")
        return False
    
# Get user_id By telegram_id

def get_user_id_by_telegram_id(telegram_id):
    try:
        sql = """
        SELECT id FROM users WHERE telegram_id = (%s)"""
        cursor.execute(sql,(telegram_id,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Create Worker Ad

def create_worker_ad(user_id: int,name:str,description:str):
    try:
        sql = """
        INSERT INTO worker_ads(user_id,name,description)
        VALUES(%s,%s,%s)"""
        cursor.execute(sql,(user_id,name,description))
        conn.commit()
        return True
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
# Delete Worker Ad

def del_worker_ad(user_id: int):
    try:
        sql = """
        DELETE FROM worker_ads
        WHERE id = (
        SELECT id FROM worker_ads
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
        )
    """
        cursor.execute(sql,(user_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Add chat message id by user_id

def add_chat_message_id_by_user_id(user_id: int,chat_message_id: int):
    try:
        sql = """
        UPDATE worker_ads SET chat_message_id = %s
        WHERE id = (
        SELECT id FROM worker_ads
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
        )
        """
        cursor.execute(sql,(chat_message_id,user_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Update worker ad status by user_id

def update_worker_status_by_user_id(user_id, worker_ad_id):
    try:
        sql = """
        UPDATE worker_ads
        SET status = FALSE
        WHERE user_id = %s AND id = %s AND status = TRUE
        RETURNING status
        """
        cursor.execute(sql, (user_id, worker_ad_id))
        result = cursor.fetchone()
        conn.commit()
        return result is not None  # agar yangilangan bo‘lsa True, bo‘lmasa False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
# # Check worker ad status

# def check_worker_ad_status(id):
#     try: 
#         sql = """
#         SELECT status FROM worker_ads WHERE id = %s"""
#         cursor.execute(sql,(id,))
#         return cursor.fetchone([0])
    
#     except Exception as e:
#         print(f"Xatolik: {e}")
#         return False


# Search worker ad'

def search_worker_ad(name:str):
    try:
        pattern = f"%{name}%"
        sql = """
            SELECT * FROM worker_ads
            WHERE (name ILIKE %s)
            AND status = TRUE
            """
        cursor.execute(sql,(pattern,))
        return cursor.fetchall()
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False


# Get worker ad chat_message_id by id

def get_worker_ad_chat_message_id_by_id(id):
    try:
        sql = """
        SELECT chat_message_id FROM worker_ads WHERE id = %s"""
        cursor.execute(sql,(id,))
        return cursor.fetchone()
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Get Worker ad description by id

def get_worker_description_by_id(id):
    try:
        sql = """
        SELECT description FROM worker_ads WHERE id = %s"""
        cursor.execute(sql,(id,))
        return cursor.fetchone()
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# My Worker ads 

def my_ads_worker(user_id):
    try:
        sql = """
        SELECT * FROM worker_ads WHERE user_id = (%s) AND status = TRUE """
        cursor.execute(sql,(user_id,))
        return cursor.fetchall()

    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
    
# Create Job ads

def create_job_ads(user_id: int,chat_message_id: int):
    try:
        sql = """
        INSERT INTO job_ads (user_id,chat_message_id) 
        VALUES(%s,%s)
        """
        cursor.execute(sql,(user_id,chat_message_id))
        conn.commit()
        return True
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
# My Job ads

def get_my_job_ads(user_id):

    try:
        sql = """
        SELECT * FROM job_ads WHERE user_id = (%s)"""
        cursor.execute(sql,(user_id,))
        return cursor.fetchall()

    except Exception as e:
        print(f"Xatolik: {e}")
        return False