import logging

logging.basicConfig(filename='import_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_element_text(element, tag, default=None, data_type=str):
    try:
        value = element.find(tag).text.strip()
        return data_type(value)
    except AttributeError:
        return default

def insert_into_table(cur, table, data, returning_id=False):
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    if returning_id:
        query += " RETURNING id"
    cur.execute(query, list(data.values()))
    if returning_id:
        return cur.fetchone()[0]
