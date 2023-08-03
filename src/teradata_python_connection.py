import teradatasql

DB_URL = ""                                 #Add Host
USER = ""                                   #Add Username
PASS = ""                                   #Add Password

try:
    # Establish a connection to the Teradata database
    with teradatasql.connect(host=DB_URL, user=USER, password=PASS) as con:
        # Create a cursor to execute queries
        with con.cursor() as cur:
            try:
                # Creating the table
                cur.execute (f"CREATE SET TABLE {USER}.SampleEmployee \
                            (Associate_Id     INTEGER, \
                            Associate_Name   CHAR(25), \
                            Job_Title        VARCHAR(25)) \
                            UNIQUE PRIMARY INDEX (Associate_Id);")
                
                print(f"Sample table {USER}.SampleEmployee created.")

                # Adding sample data into SampleEmployee table
                cur.execute (f"INSERT INTO {USER}.SampleEmployee VALUES (1, 'Richard Hendricks','CEO')")
                cur.execute (f"INSERT INTO {USER}.SampleEmployee VALUES (2, 'Jared Dunn','CFO')")
                cur.execute (f"INSERT INTO {USER}.SampleEmployee VALUES (3, 'Jian Yang','Intern')")

                print("Sample data added to table demo_user.SampleEmployee.")

                # Execute the SELECT query to get the results from DBC.SampleEmployee table 
                cur.execute(f"SELECT * FROM {USER}.SampleEmployee")

                # Extract data from the result set and print it
                for row in cur:
                    print(f"Associate ID: {row[0]}, Associate_Name: {row[1]}, Job_Title:{row[2]}")

                

            except teradatasql.DatabaseError as db_err:
                # Handle any errors that occur during query execution
                print("Error while executing the query:", db_err)

except teradatasql.DatabaseError as db_err:
    # Handle any errors that occur during the database connection
    print("Error while connecting to the Teradata database:", db_err)
