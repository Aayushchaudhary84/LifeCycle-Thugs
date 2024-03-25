import sqlite3

class populateDb:
    """
    Populates the database from data file.
    """    
    def __init__(self, dbFileLocation, txtFileLocation):
        """
        Initialize the class.

        Args:
            dbFileLocation (string): File location for the database.
            txtFileLocation (string): File location for the txt file.
        """        
        self.dbFileLocation = dbFileLocation
        self.txtFileLocation = txtFileLocation 

    def populateAllTxtData(self, databaseTableName):
        """
        Gets data from the text file and places it in the database.

        Args:
            databaseTableName (string): Name of the database table where results will go.
        """          
        con = sqlite3.connect(self.dbFileLocation)
        cursor = con.cursor()

        with open(self.txtFileLocation, 'r') as f:
            lines = f.readlines()

            for line in lines:
                split = line.split(';') # split into array of 7
                title = split[0]
                time = split[1]
                magnitude = split[2]
                latitude = split[3]
                longitude = split[4]
                depth = split[5]
                url = split[6].strip() # remove \n character
                sql = 'INSERT INTO {} (title, eventTime, magnitude, latitude, longitude, depth, url) VALUES(?, ?, ?, ?, ?, ?, ?)'.format(databaseTableName)

                cursor.execute(sql, (title, time, magnitude, latitude, longitude, depth, url))

            con.commit()

            f.close()

x = populateDb("flaskr/main.db", 'flaskr/eventData/2022-03_to_2024-02.txt')
x.populateAllTxtData('earthquake')