from database.db import conn

#Create table

def create_users_table():
    try:
        with conn:
            with conn.cursor() as cursor:
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
    except Exception as e:
        print(f"Xatolik mavjud: {e}")

#Create Worker Ads Table

def create_worker_ads_table():
    try:
        with conn:
            with conn.cursor() as cursor:
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
    except Exception as e:
        print(f"Xatolik: {e}")


# Creat Job Ads Table

def create_jobs_ads_table():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                CREATE TABLE IF NOT EXISTS job_ads (
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id),
                chat_message_id BIGINT
                )"""
                cursor.execute(sql)
    except Exception as e:
        print(f"Xatolik: {e}")


#Add user

def add_user(telegram_id: int,name:str,surname: str,username: str):
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO users (telegram_id,name,surname,username)
                VALUES (%s,%s,%s,%s)"""
                cursor.execute(sql,(telegram_id,name,surname,username))
                return True
    
    except Exception as e:
        print(f"Xatolik mavjud: {e}")
        return False
    

#Check id

def check_id(telegram_id: int):
    try:
        with conn:
            with conn.cursor() as cursor:
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
        with conn:
            with conn.cursor() as cursor:
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
        with conn:
            with conn.cursor() as cursor:
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
        with conn:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO worker_ads(user_id,name,description)
                VALUES(%s,%s,%s)"""
                cursor.execute(sql,(user_id,name,description))
                return True
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
# Delete Worker Ad

def del_worker_ad(user_id: int):
    try:
        with conn:
            with conn.cursor() as cursor:
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
                return True
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Add chat message id by user_id

def add_chat_message_id_by_user_id(user_id: int,chat_message_id: int):
    try:
        with conn:
            with conn.cursor() as cursor:
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
                return True
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Update worker ad status by user_id

def update_worker_status_by_user_id(user_id, worker_ad_id):
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                UPDATE worker_ads
                SET status = FALSE
                WHERE user_id = %s AND id = %s AND status = TRUE
                RETURNING status
                """
                cursor.execute(sql, (user_id, worker_ad_id))
                result = cursor.fetchone()
                return result is not None  # agar yangilangan bo‘lsa True, bo‘lmasa False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    

# Search worker ad

def search_worker_ad(name:str):
    try:
        with conn:
            with conn.cursor() as cursor:
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
        with conn:
            with conn.cursor() as cursor:
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
        with conn:
            with conn.cursor() as cursor:
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
        with conn:
            with conn.cursor() as cursor:
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
        with conn:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO job_ads (user_id,chat_message_id) 
                VALUES(%s,%s)
                """
                cursor.execute(sql,(user_id,chat_message_id))
                return True
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
# My Job ads

def get_my_job_ads(user_id):

    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT * FROM job_ads WHERE user_id = (%s)"""
                cursor.execute(sql,(user_id,))
                return cursor.fetchall()

    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    

# Stat users

# Users all count
def stat_user_count():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT COUNT(*) FROM users"""
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Users today count
def stat_user_today():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT COUNT(*) FROM users WHERE DATE(created_at) = CURRENT_DATE"""
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
#Users 7 day count

def stat_user_7day():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT COUNT(*) FROM users
                WHERE created_at >= NOW() - INTERVAL '7 days'
                """
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
    
# Users month count
def stat_user_month():
    try:
        with conn:
            with conn.cursor() as cursor:
            sql = """
            SELECT COUNT(*) FROM users
            WHERE created_at >= NOW() - INTERVAL '1 month'
            """
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False


# Stat Worker ads

#Worker ads all count
def stat_worker_ads_count():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT COUNT(*) FROM worker_ads"""
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

#Worker ads status active count
def stat_worker_ads_active_count():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT COUNT(*) FROM worker_ads WHERE status = TRUE"""
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    
#Worker ads status deactive count
def stat_worker_ads_deactive_count():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT COUNT(*) FROM worker_ads WHERE status = FALSE"""
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
    

# Stat Job Ads

#Job ads all count
def stat_job_ads_count():
    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT COUNT(*) FROM job_ads"""
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0] if result else False
    
    except Exception as e:
        print(f"Xatolik: {e}")
        return False