import sqlite3

def save_data(data):
    connection = sqlite3.connect("web_scraping_app.db")
    cursor = connection.cursor()
    # Assuming data has been cleaned and structured
    cursor.executemany("INSERT INTO scraped_data (col1, col2) VALUES (?, ?)", data)
    connection.commit()
    connection.close()
