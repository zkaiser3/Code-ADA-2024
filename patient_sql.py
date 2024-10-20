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
        with sqlite3.connect('patients.db') as conn:
            cursor = conn.cursor()
            patient_info = (self._availability, self._reason, self._insurance, self._price_range, self._gender_preference)

            try:
                cursor.execute("INSERT INTO patients (availability, reason, insurance, price_range, gender_preference) VALUES (?, ?, ?, ?);", patient_info)
                print("Patient has been added")
                conn.commit()
            except sqlite3.Error as e:
                print(f"SQL query error: {e}")

    @property
    def availability(self):
        return self._availability
    
    @availability.setter
    def availability(self, newavailability):
        with sqlite3.connect('patients.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE users SET username = ? WHERE username = ?;', (newusername, self._username))
                conn.commit()
                self._username = newusername
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, newfirstname):
        with sqlite3.connect('MangaAppTest.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE users SET first_name = ? WHERE username = ?;', (newfirstname, self._username))
                conn.commit()
                self._first_name = newfirstname 
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, newlastname):
        with sqlite3.connect('MangaAppTest.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE users SET last_name = ? WHERE username = ?;', (newlastname, self._username))
                conn.commit()
                self._last_name = newlastname
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, newpassword):
        with sqlite3.connect('MangaAppTest.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('UPDATE users SET password = ? WHERE username = ?;', (newpassword, self._username))
                conn.commit()
                self._password = newpassword
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    @classmethod
    def find_user(cls, username):
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