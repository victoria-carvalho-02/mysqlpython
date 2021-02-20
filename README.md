# mysqlpython
Using MySQL Databases with Python

## Steps -

1.	Install Python 
2.	Install Sublime Text Editor – Open after installation. Go to View in menu> Syntax>Python as language
3.	Install Git (Default Settings)
4.	Download MySQL - https://www.mysql.com/  Download from the same website the MySQLworkbench
  a.	Now it’s best to have both in a same package then downloading separately
  b.	So, https://www.mysql.com/ > Downloads > At the end of the page > MySQL Community (GPL) Downloads » Then go to MySQL Community Server > Select Windows> go to the Download      page
 
  c.	From here DON’T DOWNLOAD THE SMALL SIZE VERSION OF MYSQL – what it does it after installing is, it will carry out other installations to download other stuff required for       it and has a lot of bugs in it.
 
  d.	Then on the next page – “No thanks……..”
 
5.	Install MySQL and Workbench
 
  a.	Now select the default setting- Developer Default. It contains Workbench and other details.
  b. Remember the Username and Password
      Username = root
      Password = somepassword
      This password must be remembered as it will be required later in the configuration of SQL and when connecting Python to SQL.
      Now we don’t need to add any other user. The root user is fine.
  c. Click Finish and then other remaining things to configure will be displayed. Complete the configurations.
 

6.	Install MySQL Connector
  a.	Go to Git bash
    i.	Check the current path using $pwd command
    ii.	It should be the default path
    iii.	Now let’s make a directory to store the python code which we are going to perform in this course $mkdir mysqlpython
 
  b.	Go to the path where mysqlpython is by using cd /c/mysqlpython
      Note – use clear to clear the terminal/bash
  c.	Install the connector by using the command (in order to connect python with sql later)
    i.	1st command that mostly works –
         pip install mysql-connector 
         if "Successful" no need to download 2 or 3

   ii.	2nd command in case 1st doesn’t work
    Pip install mysql-connector-python
 
   iii. 3rd command in case 2nd doesn’t download or work
    Pip install mysql-connector-python-rf
 
7.	Connect to DB in python - Let's code!
    Check the database.py file

