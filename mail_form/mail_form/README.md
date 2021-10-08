This site contains:

Model "Mail" created with class
This model is a table name in the database

Once we create object (sending our data) on the start page, we creating a new row in DB with form data as attributes

Form handled with class name "Credentials" that defines in forms.py, every attribute is the field that rendered on the start page

After sending data you will be redirected on the page with ID of your mail.

There are several methods:

-thanks - handles the page with ID of sended mail, gives the template some context
-index - this method handles the page with all objects form DB with 10 objects per page
-get_mail - (it's not over yet) the template for getting the attributes of choosed object on the one page

Project had been created in virtual environment
To startup print "py manage.py runserver" in the command shell to start the server  
