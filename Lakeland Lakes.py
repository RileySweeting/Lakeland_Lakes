# TEAM NAMES: Mitch Brown & Riley Sweeting

# Import SQLite Package
import sqlite3

# Mandatory Setup (DO NOT EDIT)
connection = sqlite3.connect("lakeland-lakes.db")
cursor = connection.cursor()

# Functions --------------------------------------------------------------------------

# Get Biggest Surface Area
def get_biggest_area_lake(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    maxSA = ['', lakes[0][1]] # Max Surface Area (SA) Tuple
    for lake in lakes: # Loop Through Each Lake
        try:
            if lake[1] > maxSA[1]: # If this Lake's SA is bigger than the MAX SA
                maxSA[1] = lake[1] # Updates maxSA
                maxSA[0] = lake[0] # Updates Name of maxSA
        except: # Exception Handling: Catches NULL Error in case SA is NULL
            pass
    return maxSA[0]
# Get Deepest Lake
def get_deepest_lake(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    maxDepth = ['', 0] # Max Depth Variable
    for lake in lakes: # Loop Through Each Lake
        try: # Try comparing maxDepth to possible NULL value
            if lake[3] > maxDepth[1]:
                maxDepth[1] = lake[3]
                maxDepth[0] = lake[0]
        except: # Exception Handling: In Case Lake[3] is NULL
            pass
    return maxDepth[0]
# Get Biggest Volume Lake
def get_biggest_volume_lake(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    maxVolume = ['', 0] # Max Volume Variable
    for lake in lakes: # Loop Through Each Lake
        try: # Try comparing maxVolume to possible NULL value
            if lake[2] > maxVolume[1]:
                maxVolume[1] = lake[2]
                maxVolume[0] = lake[0]
        except: # Exception Handling: In Case Lake[2] is NULL
            pass
    return maxVolume[0]
# Get Highest Average Depth Lake (AVG DEPTH = VOLUME / SURFACE AREA)
def get_highest_average_depth_lake(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    maxDepth = ['', 0] # Max Depth Variable/Placeholder (Contains AVG Depth AND Name)
    for lake in lakes: # Loop Through Each Lake
        try: # Try Performing Calculations on Possible NULL values
            depth = lake[2] / lake[1] # Divide VOLUME by SURFACE AREA to find AVG DEPTH
            if depth > maxDepth[1]:
                maxDepth[1] = depth # If Current Depth is bigger than maxDepth, update maxDepth
                maxDepth[0] = lake[0] # Save Name of Lake to Max Depth as well
        except: # Exception Handling: In Case Lake is NULL
            pass
    return maxDepth[0]
# Get Most Southern Lake
def get_most_southern_lake(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    maxSouth = ['', 100] # Max South Variable
    for lake in lakes: # Loop Through Each Lake
        try: # Try comparing maxSouth to possible NULL value
            if lake[4] < maxSouth[1]:
                maxSouth[1] = lake[4]
                maxSouth[0] = lake[0]
        except: # Exception Handling: In Case Lake[5] is NULL
            pass
    return maxSouth[0]
# Get Number of Big Lakes
def get_number_of_big_lakes(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    count = 0 # Num of BIG Lakes
    for lake in lakes: # Loop Through Each Lake
        try: # Try seeing if lake volume is over 100,000
            if lake[2] > 100000000:
                count += 1
        except: # Exception Handling: In Case Lake[2] is NULL
            pass
    return count
# Number of Western Lakes
def get_number_west(connection, longitude):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    count = 0 # Num of Western Lakes
    for lake in lakes: # Loop Through Each Lake
        try: # Try seeing if lake volume is West from parameter
            if lake[5] < longitude:
                count += 1
        except: # Exception Handling: In Case Lake[5] is NULL
            pass
    return count
# Deepest Western Lakes
def get_deepest_western_lakes(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lakes;") # Select All Lakes
    lakes = cursor.fetchall() # Tuple of Lakes
    # Make a Sorted List of Lakes based on Longitude
    sortedList = sorted(lakes, key = lambda x: x[5])
    # Remove Null Depth Lakes
    for lake in sortedList:
        try: # Check if Lake is Null
            lake[5] + 0 # Depth Valid
            pass
        except: # Depth Null, so remove
            sortedList.remove(lake)
    maxDepth = sortedList[0][5] # Max Depth Used to compare deepest lake
    currentDepth = 0
    answerList = [] # The Return List of names of requested lakes
    for lake in sortedList: # Loop through every Sorted Lake (W to E)
        currentDepth = lake[3] # Current Depth
        try: # Values may be Null
            if maxDepth >= currentDepth: # These are in order of West to East since Lakes are sorted
                continue # Bigger lake exists
            maxDepth = currentDepth # Update Max Depth
            answerList.append(lake[0]) # Appends name of currentDepth Lake
        except: # Exception Handling: Catches Null Error
            pass
    return answerList

# Try to Drop Table
try: # Exception Handling: Handles Exception of Table Not Existing
    sql = "DROP TABLE lakes;"
    cursor.execute(sql)
except:
    pass

# Save TXT Command into Variable
sql = """CREATE TABLE lakes (
    name TEXT,
    surface_area INTEGER,
    volume INTEGER,
    max_depth INTEGER,
    latitude REAL,
    longitude REAL);"""
cursor.execute(sql)

# Insert Values
lBentley = """INSERT into lakes VALUES ('Lake Bentley', 53, 124035911, 12, 28.014167, -81.926389);"""
cursor.execute(lBentley)
# Insert Values
lBeulah = """INSERT into lakes VALUES ('Lake Beulah', 18, 93577666, 28, 28.040556, -81.968333);"""
cursor.execute(lBeulah)
# Insert Values
lBonnet = """INSERT into lakes VALUES ('Lake Bonnet', 79, 99725980, 13, 28.048056, -81.976667);"""
cursor.execute(lBonnet)
# Insert Values
lBonny = """INSERT into lakes VALUES ('Lake Bonny', 203, 389902099, 11, 28.034807, -81.931176);"""
cursor.execute(lBonny)
# Insert Values
lCrago = """INSERT into lakes VALUES ('Lake Crago', 51, 222446869, 35, 28.092778, -81.947778);"""
cursor.execute(lCrago)
# Insert Values
lGibson = """INSERT into lakes VALUES ('Lake Gibson', 490, 1027345827, 20, 28.108611, -81.959167);"""
cursor.execute(lGibson)
# Insert Values
lHollingsworth = """INSERT into lakes VALUES ('Lake Hollingsworth', 354, 792833452, 14, 28.025000, -81.945556);"""
cursor.execute(lHollingsworth)
# Insert Values
lHolloway = """INSERT into lakes VALUES ('Lake Holloway', 25, 54542283, 12, 28.034444, -81.916944);"""
cursor.execute(lHolloway)
# Insert Values
lHorney = """INSERT into lakes VALUES ('Lake Horney', 7, 8566835, 10, 28.033056, -81.938889);"""
cursor.execute(lHorney)
# Insert Values
lHunter = """INSERT into lakes VALUES ('Lake Hunter', 91, 178620197, 9, 28.032778, -81.965833);"""
cursor.execute(lHunter)
# Insert Values
lJohn = """INSERT into lakes VALUES ('Lake John', 99, 294848504, 20, 28.000405, -81.943395);"""
cursor.execute(lJohn)
# Insert Values
lMeadowView = """INSERT into lakes VALUES ('Meadow View Lake', 55, NULL, NULL, 28.098611, -81.984167);"""
cursor.execute(lMeadowView)
# Insert Values
lMirror = """INSERT into lakes VALUES ('Lake Mirror', 19, 52154960, 17, 28.043889, -81.951667);"""
cursor.execute(lMirror)
# Insert Values
lMorton = """INSERT into lakes VALUES ('Lake Morton', 40, 152250543, 22, 28.038056, -81.953056);"""
cursor.execute(lMorton)
# Insert Values
lParker = """INSERT into lakes VALUES ('Lake Parker', 2109, 5365756287, 25, 28.067778, -81.931389);"""
cursor.execute(lParker)
# Insert Values
lSomerset = """INSERT into lakes VALUES ('Lake Somerset', 45, 123846764, 25, 28.003889, -81.931111);"""
cursor.execute(lSomerset)
# Insert Values
lWire = """INSERT into lakes VALUES ('Lake Wire', 22, 80120478, 22, 28.046667, -81.960556);"""
cursor.execute(lWire)
# Insert Values
lBlanton = """INSERT into lakes VALUES ('Lake Blanton', 1, NULL, NULL, 28.042911, -82.001834);"""
cursor.execute(lBlanton)
# Insert Values
lBonnyLittle = """INSERT into lakes VALUES ('Little Lake Bonny', 18, NULL, NULL, 28.030711, -81.921556);"""
cursor.execute(lBonnyLittle)
# Insert Values
lCanyon = """INSERT into lakes VALUES ('Lake Canyon', 11, NULL, NULL, 27.992535, -81.943816);""" #E
cursor.execute(lCanyon)
# Insert Values
lCharles = """INSERT into lakes VALUES ('Lake Charles', 3, NULL, NULL, 28.044794, -82.004842);"""
cursor.execute(lCharles)
# Insert Values
lErnest = """INSERT into lakes VALUES ('Lake Ernest', 5, NULL, NULL, 28.049137, -82.006980);"""
cursor.execute(lErnest)
# Insert Values
lFish = """INSERT into lakes VALUES ('Fish Lake', 27, NULL, NULL, 28.086448, -81.920549);"""
cursor.execute(lFish)
# Insert Values
lGeorge = """INSERT into lakes VALUES ('George Lake', 10, NULL, NULL, 28.051051, -82.004591);"""
cursor.execute(lGeorge)
# Insert Values
lGlen = """INSERT into lakes VALUES ('Lake Glen', 8, NULL, NULL, 28.045615, -82.009342);"""
cursor.execute(lGlen)
# Insert Values
lHoward = """INSERT into lakes VALUES ('Lake Howard', 6, NULL, NULL, 28.050953, -81.999985);"""
cursor.execute(lHoward)
# Insert Values
lJim = """INSERT into lakes VALUES ('Lake Jim', 5, NULL, NULL, 28.047580, -82.005745);"""
cursor.execute(lJim)
# Insert Values
lKelly = """INSERT into lakes VALUES ('Kelly Lake', 7, NULL, NULL, 27.997257, -81.963273);"""
cursor.execute(lKelly)
# Insert Values
lLarch = """INSERT into lakes VALUES ('Lake Larch', 9, NULL, NULL, 28.101056, -81.944508);"""
cursor.execute(lLarch)
# Insert Values
lMack = """INSERT into lakes VALUES ('Lake Mack', 3, NULL, NULL, 28.046754, -82.014570);"""
cursor.execute(lMack)
# Insert Values
lMeridian = """INSERT into lakes VALUES ('Meridian Lake', 5, NULL, NULL, 27.987198, -81.923040);"""
cursor.execute(lMeridian)
# Insert Values
lMiriam = """INSERT into lakes VALUES ('Lake Miriam', 23, NULL, NULL, 27.977833, -81.953706);"""
cursor.execute(lMiriam)
# Insert Values
lPollock = """INSERT into lakes VALUES ('Lake Pollock', 16, NULL, NULL, 27.986503, -81.926611);"""
cursor.execute(lPollock)
# Insert Values
lSanGully = """INSERT into lakes VALUES ('San Gully Lake', 2, NULL, NULL, 28.011813, -81.981900);"""
cursor.execute(lSanGully)
# Insert Values
lSherwoodForest = """INSERT into lakes VALUES ('Sherwood Forest Lake', 79, NULL, NULL, 28.137311, -81.912880);"""
cursor.execute(lSherwoodForest)
# Insert Values
lWaterview = """INSERT into lakes VALUES ('Waterview Lake', 8, NULL, NULL, 27.988672, -81.925902);"""
cursor.execute(lWaterview)
# Insert Values
lWatkins = """INSERT into lakes VALUES ('Lake Watkins', 2, NULL, NULL, 28.021402, -81.930256);"""
cursor.execute(lWatkins)
# Insert Values
lWood = """INSERT into lakes VALUES ('Wood Lake', 4, NULL, NULL, 27.997741, -81.931913);"""
cursor.execute(lWood)

# Connection Commit
connection.commit()