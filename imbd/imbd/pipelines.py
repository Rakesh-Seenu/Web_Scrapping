import sqlite3

class PracticePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('movie_t.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS movie_tb (
            durations TEXT,              
            movie_ratings TEXT,
            movie_titles TEXT,
            movie_year TEXT   
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        try:
            durations = item['durations']
            movie_ratings = item['movie_ratings']
            movie_titles = item['movie_titles']
            movie_year = item['movie_year']

            for duration, rating, title, year in zip(durations, movie_ratings, movie_titles, movie_year):
                self.curr.execute("""INSERT INTO movie_tb (durations, movie_ratings, movie_titles, movie_year) 
                                     VALUES (?, ?, ?, ?)""",
                                  (duration, rating, title, year))
            self.conn.commit()
            print("Stored items in database:", item)
        except Exception as e:
            print("Error storing items in database:", e)


if __name__ == "__main__":
    # Mock items and spider
    mock_items = {
        'durations': ["2:22", "2:55", "2:32"],
        'movie_ratings': [9.3, 9.2, 9.0],
        'movie_titles': ["The Shawshank Redemption", "The Godfather", "The Dark Knight"],
        'movie_year': [1994, 1972, 2008]
    }
    mock_spider = None

    # Create pipeline instance and process mock items
    movie_db = PracticePipeline()
    movie_db.process_item(mock_items, mock_spider)

