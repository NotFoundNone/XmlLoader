import xml.etree.ElementTree as ET
import logging
from db_config import get_db_connection
from process_response import process_response

# Настройка ведения журнала
logging.basicConfig(filename='import_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Парсинг XML-файл
tree = ET.parse('data.xml')
root = tree.getroot()

# Подключение к PostgreSQL
conn = get_db_connection()
cur = conn.cursor()

try:
    for return_element in root.findall('.//return'):
        try:
            process_response(cur, return_element)
            conn.commit()
        except Exception as e:
            logging.error(f"Ошибка обработки return_element: {e}")
            conn.rollback()
finally:
    cur.close()
    conn.close()
