## Learn Database

### Connect with a database
~~~
sqlite_connection = sqlite3.connect(<"NAME_OF_DATABASE>)
cursor = sqlite3.cursor()
~~~
### Create Query
INSERT, UPDATE, SELECT, ...
Example Query
~~~ query = '''CREATE TABLE SqliteDb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''
~~~

### Execute Query
```
cursor.execute(query)
```
### Handling Error
Always write code in trry-except-finally block and use print statement