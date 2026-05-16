import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="lucky",
        database="biometric_db"
    )


def insert_data(patient_hash, encrypted_data, key):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO patient_scans (patient_hash, encrypted_scan, aes_key) VALUES (%s, %s, %s)"
    cursor.execute(query, (patient_hash, encrypted_data, key))

    conn.commit()
    conn.close()


def get_data(record_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT encrypted_scan, aes_key FROM patient_scans WHERE id=%s"
    cursor.execute(query, (record_id,))

    result = cursor.fetchone()
    conn.close()

    return result


def get_all_data():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id, patient_hash FROM patient_scans"
    cursor.execute(query)

    results = cursor.fetchall()
    conn.close()

    return results