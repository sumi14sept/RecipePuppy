import sqlite3
conn = sqlite3.connect('dbRecipes.db')
c = conn.cursor()
try:
 # Create table
    c.execute('''CREATE TABLE tblRecipePuppy
             (Recipe Name, URL, Ingredients,Image)''')



 # Save (commit) the changes
    conn.commit()
except Exception as e:
    print(str(e))

#closing the connection
conn.close()

print("Database creation successfull")