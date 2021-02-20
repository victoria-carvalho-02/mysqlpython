# mysqlpython
## Using MySQL Databases with Python

#### Steps -



##### 1. Install Python 
##### 2. Install Sublime Text Editor – Open after installation. Go to View in menu> Syntax>Python as language
##### 3. Install Git (Default Settings)
##### 4. Download MySQL - https://www.mysql.com/  Download from the same website the MySQLworkbench
          1. Now it’s best to have both in a same package then downloading separately
          2. So, https://www.mysql.com/ > Downloads > At the end of the page > MySQL Community (GPL) Downloads » Then go to MySQL Community Server > Select Windows> go to the Download   page
          3. From here DON’T DOWNLOAD THE SMALL SIZE VERSION OF MYSQL – what it does it after installing is, it will carry out other installations to download other stuff required for it and has a lot of bugs in it.
          4. Then on the next page – “No thanks……..”
 
##### 5. Install MySQL and Workbench
          1. Now select the default setting- Developer Default. It contains Workbench and other details.
          2. Remember the Username and Password, Username = root and Password = somepassword
          This password must be remembered as it will be required later in the configuration of SQL and when connecting Python to SQL. Now we don’t need to add any other user. The root user is fine.
          3. Click Finish and then other remaining things to configure will be displayed. Complete the configurations.

##### 6. Install MySQL Connector
          a. Go to Git bash
            i. Check the current path using $pwd command
            ii. It should be the default path
            iii. Now let’s make a directory to store the python code which we are going to perform in this course $mkdir mysqlpython
            iv. Go to the path where mysqlpython is by using cd /c/mysqlpython (Note – use clear to clear the terminal/bash)

##### 7. Install the connector by using the command (in order to connect python with sql later)
          a. 1st command that mostly works –
            i.	pip install mysql-connector 
            ii.	if "Successful" no need to download 2 or 3

          b.	2nd command in case 1st doesn’t work
            i.	Pip install mysql-connector-python

          c.	3rd command in case 2nd doesn’t download or work
            i.	Pip install mysql-connector-python-rf

##### 8. Connect to DB in python - Let's code! Check the database.py file
