Project Description:

1. Created Blog Webpage along with user authentication (registration, login, edit profile, change password).
2. In this normal user can add new blogs and able to edit his own blogs. 
3. While admin/superuser can view all the blogs and able to edit and delete them. 
4. Without login/registration user cannot add new blog but on the home page he will able to see all the blogs added by other users.

To run the project, follow the given steps as below.

1. Select Version of Python to Install (greate than 3.5)
2. Download Python Executable Installer from internet --> 'https://www.python.org/downloads/'
3. Run Executable Installer downloaded in step 2
4. Add Python Path to Environment Variables (optional if pip is not working)
5. Verify Python is Installed On Windows by typing 'python --version' in cmd
6. Verify Pip is Installed by typing coomand 'pip --version' in cmd
7. Install django using command 'pip install django'
8. Verify django installation by executing 'django-admin --version' in the command prompt.
9. Download the zip file
10. Extract the downloaded zip file in one directory OR You can clone the git repository using 'git clone' command
11. Open the command prompt and cd into the directory where project(zip file) is extracted
12. Then cd into inner project folder named as 'project1'
13. Execute a command 'pip install django-crispy-forms' (as we have added functionality of crsipy form in project)
14. Type a command 'python manage.py makemigrations'
15. Then execute a command 'python manage.py migrate'
16. Create superuser/admin using command 'python manage.py createsuperuser' and by giving username and password
17. Type a command 'python manage.py runserver' in cmd
18. Copy the link of development server and paste into the browser--> 'http://127.0.0.1:8000/'
19. You will see the homepage
20. Using credentials of superuser, you can login into the system.
21. You can also create user using singup form.(Link can be found below login page)