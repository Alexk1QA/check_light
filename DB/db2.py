import sqlite3

# connect = sqlite3.connect("/Users/macbook/Desktop/check_light_home/DB/eng_bot.accdb")
connect = sqlite3.connect("/home/ubuntu/check_light/DB/eng_bot.accdb")
cursor = connect.cursor()


class DB:
    def __init__(self, id_user):

        self.id_user = f"id_{id_user}"

# -------------------------------------------------   CREATE DATA  ---------------------------------------------------#

    def create_table(self):
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.id_user}(
                                         id INTEGER PRIMARY KEY autoincrement,
                                          mode TEXT,
                                          sleep_time TEXT 
                                          )''')
        connect.commit()

# -------------------------------------------------   INSERT DATA  ---------------------------------------------------#

    def insert_settings(self, data, column_):

        cursor.execute(
            f"INSERT INTO {self.id_user} ( {column_})"
            f"VALUES ( ? )", [data])
        connect.commit()

# -------------------------------------------------   SELECT DATA  ---------------------------------------------------#

    def select_data_(self, column_=None, where_clmn="id", where_data=1):

        if column_ is not None:
            cursor.execute(f"""SELECT {column_} FROM {self.id_user} WHERE {where_clmn} = '{where_data}' """)
            return cursor.fetchall()

# -------------------------------------------------   UPDATE DATA  ---------------------------------------------------#

    def update_data_(self, column_=None, where_clmn="id", where_data=1, data_updating=None):

        cursor.execute(
            f""" UPDATE {self.id_user} SET '{column_}' = '{data_updating}' WHERE {where_clmn} = '{where_data}' """)
        connect.commit()
