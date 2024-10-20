import sqlite3

class Patient:
    def __init__(self, availability, reason, insurance, price_range, gender_preference):
        self._availability = availability
        self._reason = reason
        self._insurance = insurance
        self._price_range = price_range 
        self._gender_preference = gender_preference
        self.add_patient_to_db() #adds patient to database

    def add_patient_to_db(self):
        """
        Adds the patient to the SQL "patients" table. Automatically called when a Patient class is created
        """
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            patient_info = (self._availability, self._reason, self._insurance, self._price_range, self._gender_preference)

            try:
                cursor.execute("INSERT INTO patients (availability, reason, insurance, price_range, gender_preference) VALUES (?, ?, ?, ?, ?);", patient_info)
                print("Patient has been added")
                conn.commit()
            except sqlite3.Error as e:
                print(f"SQL query error: {e}")
    
    #availability property
    @property
    def availability(self):
        return self._availability
    
    @availability.setter
    def availability(self, new_availability):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE patients SET availability = ? WHERE availability = ?;', 
                               (new_availability, self._availability))
                conn.commit()
                self._availability = new_availability
            except sqlite3.Error as e:
                print(f"Database error (availability): {e}")

    # Reason property
    @property
    def reason(self):
        return self._reason
    
    @reason.setter
    def reason(self, new_reason):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE patients SET reason = ? WHERE reason = ?;', 
                               (new_reason, self._reason))
                conn.commit()
                self._reason = new_reason
            except sqlite3.Error as e:
                print(f"Database error (reason): {e}")

    # Insurance property
    @property
    def insurance(self):
        return self._insurance
    
    @insurance.setter
    def insurance(self, new_insurance):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE patients SET insurance = ? WHERE insurance = ?;', 
                               (new_insurance, self._insurance))
                conn.commit()
                self._insurance = new_insurance
            except sqlite3.Error as e:
                print(f"Database error (insurance): {e}")

    # Price Range property
    @property
    def price_range(self):
        return self._price_range
    
    @price_range.setter
    def price_range(self, new_price_range):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE patients SET price_range = ? WHERE price_range = ?;', 
                               (new_price_range, self._price_range))
                conn.commit()
                self._price_range = new_price_range
            except sqlite3.Error as e:
                print(f"Database error (price range): {e}")

    # Gender Preference property
    @property
    def gender_preference(self):
        return self._gender_preference
    
    @gender_preference.setter
    def gender_preference(self, new_gender_preference):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE patients SET gender_preference = ? WHERE gender_preference = ?;', 
                               (new_gender_preference, self._gender_preference))
                conn.commit()
                self._gender_preference = new_gender_preference
            except sqlite3.Error as e:
                print(f"Database error (gender preference): {e}")

    @classmethod
    def find_patient(cls, name):
        with sqlite3.connect('MangaAppTest.db') as conn:
            cursor = conn.cursor()

            try:
                cursor.execute('SELECT first_name, last_name, username, password FROM "users" WHERE username = ?;', (username,))
                user_row = cursor.fetchone()

                if user_row:
                    first_name, last_name, username, password = user_row
                    return cls(first_name, last_name, username, password)
                else:
                    print("User not found")  # You can change this to any logging mechanism you prefer
                    return None
                    
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return None


def create_user_table() -> None:
    '''
    Creates "users" in MangaAppTest.db.

    "users" table contains basic user information   
    '''

    users = sqlite3.connect('MangaAppTest.db')
    cursor = users.cursor()

    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS "users" (
            "id" INTEGER AUTO_INCREMENT,
            "first_name" TEXT NOT NULL,
            "last_name" TEXT NOT NULL,
            "username" TEXT NOT NULL UNIQUE,
            "password" TEXT NOT NULL,
            PRIMARY KEY("id")
        );
        '''
        )
        print("Table have been created")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally: 
        users.commit()
        users.close()


def view_users_table() -> None:
    '''
    Displays the "users" table using SQL commands
    '''
    import pandas as pd
    users = sqlite3.connect('MangaAppTest.db')

    try:
        df = pd.read_sql_query('SELECT * FROM "users"', users)
        
        print(df.to_string(index=False)) 
    except sqlite3.Error as e:
        print(f"SQL error: {e}")

    except pd.errors.SqlQueryError as e:
        print(f"SQL query error: {e}")

    finally:
        users.close()


def delete_users_table() -> None: 
    '''
    deletes the "users" table off SQL
    only should be used for testing or debugging purposes
    '''
    users = sqlite3.connect('MangaAppTest.db')
    cursor = users.cursor()

    try: 
        cursor.execute("DROP TABLE 'users';")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        users.commit()
        users.close()


class LoginError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def user_login(username: str, password: str) -> None:
    """
    Checks the user's credentials when logging in

    Parameters:
        username (str): the username that the user entered when at the login page
        password (str): the password that the user entered when at the login page

    Raises:
        - sqlite3.Error: There is a problem with SQL commands
        - LoginError: Either Username does not exist or password does not match username
    """
    users = sqlite3.connect('MangaAppTest.db')
    cursor = users.cursor()

    try: 
        cursor.execute('SELECT "password" FROM "users" WHERE "username" = ?' , (username, ))
        user = cursor.fetchone()

        if user is None:
            raise LoginError("User does not exist")

        check_password = user[0]

        if password != check_password:
            raise LoginError("Incorrect password")

        print("Login Sucessful")

    except sqlite3.Error as e:
        print(f"SQL error: {e}")

    except LoginError as le: 
        print(le.message)

    finally:
        users.close()