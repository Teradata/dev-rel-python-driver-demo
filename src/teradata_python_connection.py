import teradatasql

DB_URL = ""                                 #Add Host
USER = ""                                   #Add Username
PASS = ""                                   #Add Password
QUERY = "SELECT * FROM dbc.dbcinfo"         #Sample query

try:
    # Establish a connection to the Teradata database
    with teradatasql.connect(host=DB_URL, user=USER, password=PASS) as con:
        # Create a cursor to execute queries
        with con.cursor() as cur:
            print("Final contents of table")

            try:
                # Execute the query
                cur.execute(QUERY)

                # Extract data from the result set and print it
                for row in cur:
                    print(f"setting: {row[0]}, value: {row[1]}")
            except teradatasql.DatabaseError as db_err:
                # Handle any errors that occur during query execution
                print("Error while executing the query:", db_err)

except teradatasql.DatabaseError as db_err:
    # Handle any errors that occur during the database connection
    print("Error while connecting to the Teradata database:", db_err)
