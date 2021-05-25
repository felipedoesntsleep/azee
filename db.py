import sqlite3
import requests

table = "STD4P2"

 # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
# conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
# c = conn.cursor()

# c.execute('''CREATE TABLE ?
#              ([generated_id] INTEGER PRIMARY KEY, [p1] text, [p2] text, [p3] text, [p4] text, [winner] text, [link] text)''', (table, ))


def insert_game(p1, p2, p3, p4, winner, link):
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    print("winner: ", winner)
    print(get_wins(winner))
    c.execute('''INSERT INTO STD4P2 (p1, p2, p3, p4, winner, link) values (?, ?, ?, ?, ?, ?)''', (p1, p2, p3, p4, winner, link))
    conn.commit()
    print(get_wins(winner))

def get_rung(rung):
    print("----------------")
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    result = c.execute('''SELECT WINNER, COUNT(*) as count FROM STD4P2 GROUP BY winner HAVING count == ?''', (rung-1,))
    store = result.fetchone()
    while store != None:
        print(store)
        store = result.fetchone()

def get_win_percent(player):
    print("----------------")
    print(player)
    print(get_wins(player))
    print(p1_games(player) + p2_games(player) + p3_games(player) + p4_games(player))
    win = get_wins(player)/(p1_games(player) + p2_games(player) + p3_games(player) + p4_games(player))
    print(win)
    return win

def p1_games(player):
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    result = c.execute('''SELECT COUNT(*) as count FROM STD4P2 WHERE p1 == ?''', (player,))
    store = result.fetchone()
    return store[0]

def p2_games(player):
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    result = c.execute('''SELECT COUNT(*) as count FROM STD4P2 WHERE p2 == ?''', (player,))
    store = result.fetchone()
    return store[0]

def p3_games(player):
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    result = c.execute('''SELECT COUNT(*) as count FROM STD4P2 WHERE p3 == ?''', (player,))
    store = result.fetchone()
    return store[0]

def p4_games(player):
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    result = c.execute('''SELECT COUNT(*) as count FROM STD4P2 WHERE p4 == ?''', (player,))
    store = result.fetchone()
    return store[0]

def get_wins(player):
    print(player)
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    result = c.execute('''SELECT COUNT(*) as count FROM STD4P2 WHERE winner == ?''', (player,))
    store = result.fetchone()
    return store[0]

def get_games():
    conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor()
    result = c.execute('''SELECT * FROM STD4P2''')
    results = []
    store = result.fetchone()
    while store != None:
        print(store)
        results.append(store)
        store = result.fetchone()
    return results


# def p2_games(player):


# def p1_games(player):
# insert_game("mfrazer17", "arreed7", "Trial_4", "ArieyaLora", "mfrazer17")
# get_rung(2)
# get_rung(3)
# get_win_percent("ArieyaLora")
# get_win_percent("mfrazer17")
# # Create table - COUNTRY
# c.execute('''CREATE TABLE COUNTRY
#              ([generated_id] INTEGER PRIMARY KEY,[Country_ID] integer, [Country_Name] text)''')
        
# # Create table - DAILY_STATUS
# c.execute('''CREATE TABLE DAILY_STATUS
#              ([Client_Name] text, [Country_Name] text, [Date] date)''')
                 


# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table/s at the end of the code). 
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)