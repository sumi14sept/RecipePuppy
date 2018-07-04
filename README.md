 
⦁    Use-Case: 
The Recipe Puppy is an ingredient-based recipe search engine. The Recipe Puppy API gives developers access to a database of different recipes, searching by ingredient or keyword. Access is gained via HTTP and results can be returned in JSON or XML

Homepage :  http://www.recipepuppy.com/about/api/

API Endpoint: http://www.recipepuppy.com/api/

⦁    Tools and Libraries: 
Programming Language: Python
Libraries/Packages:

       a.  urilib : This is a package  used to fetch Json data from RecipePuppy  Api. 
       b.  sqlite3: This library provides a disk based light weight database. It is used to store the data that is fetched from the   RecipePuppy  Api.
       c.  flask: This is a microframework for Python to support web  based development. This is used to show the data in browser.
IDE: 
Spyder,Microsoft Visual Studio

Steps to run the application:

1.Run PythonFiles/createDB.py to create the database dbRecipes.db

2.Run PythonFiles/projFetchSave.py to fetch data from RecipePuppy Api and save it to the dbRecipes.db database.

3.Open ProjRecipePuppy.sln and run to view saved data in the browser.

Important Note: 

The variable 'DATABASE' in views.py contains the path of the dbRecipes.db database.Thus this path should be altered according to the database location.

 
 
 
 
 
 
 
 
 
