# **Active-Spring Swimming Pool** 
![Screenshot 2022-12-21 at 02 15 52](https://user-images.githubusercontent.com/98041941/208894245-75c3027a-e7ce-451e-872b-78648fdc27f3.png)


---


## **Introduction**
Welcome to my fourth project, a Full-Stack website that was created with HTML, CSS, JavaScript, and Python + Django. This swimming pool website was created using business logic that was utilised to manage a centrally maintained dataset. The website is set up to let users make bookings and  use the pool and have to ability to creating, reading, updating, and deleting (CRUD) their bookings.

In this README I will detail the steps I took to develop and create this project, with the use of  screen photos, images, links, charts and more.
This project is for education purposes only.

Thank you for viewing my project.

I hope you find the application useful!

---

# UXD - User Experience Design

##  **Strategy**

My plan of action was to build and produce a website that would be the most useful and beneficial to my targeted audience, employing the UX principles strategy.

### **Target Audience**
- This website is targeted to people age 16 or older providing personnel is a competent swimmer. 

- This website is not gender specific. 

- This website is targeted to swimming pool users.

- This website is targeted to people who has a passion for swimming.

- This website is targeted to athletes.

- This website is targeted to people who live healthy lifestyle.

- This website is targeted to anyone looking for pool-related information.

- This website is targeted to holiday makers. 

- This webiste is targeted to the citizens of the United Kingdom. 

### **Creator Goals**

- As a creator, I want the website to be easy to navigate.

- As a creator, I want the allow users to create, view, update and delete bookings (CRUD) pool bookings.

- As a creator,  I want admin to log in to access the website's backend when needed.

- As a creator, I want to allow admins to create, view, update and delete bookings (CRUD) pool bookings.

- As a creator, I want provide admin with the ability to approve or reject bookings in order to effectively manage all bookings.


### **User Stories**
- As a user of the website, I want information that is clear and concise.
- As a user of the website, I want to easily navigate around without difficulty.
- As a user of the website, I want to be made aware of any invalid data input and how to rectify it.
- As a user of the website, I want to have a way of contacting someone if I have any problems or questions.
- As a user of the website, I want to have the option to create an account if I want to.
- As a user of the website, I want to have the option to sign into my existing account.
- As a user of the website, I want to ability to create, view, update and delete booking for the pool.

- As a user of the website, 

### **Site owner goals**
- As the site owner I would like customer to have information that is clear and concise.
- As the site owner I would like customer to have ability sign in if they have an existing account or able to sign up for an account.
- As the site owner I would like customer to have ability make, view, update and delete their booking if required.
- As the site owner I would like  customer to have ability make, view, update and delete their booking as well as the ability to approve or reject booking if required. 

---

##  **Scope**

I tried to design the best strategy to accomplish certain functionality for the website and its business objectives by using the principles of the Scope plane. 

Plan of phased deployment:

#### **Phase 1**

- A project that would align with User Stories
    - A responsive home page with information that is clear and concise.
    - A responsive navigation bar which would aid customers when navigating the website
    - A contact page for users to contact someone if they have a problem or question.
    - Sign In or Sign Up feature for customers to sign in or create an account
    - The ability for customers to create, view, update, and delete pool bookings.

#### **Phase 2**

- Building on Phase one and implementing additional features
    - Authentication system to perform certain functions.
    - Add alert messaging system to give users guidance when interacting with specific elements of the website.
    - Customers have the ability to view, update and delete their own bookings when logged in.

#### **Phase 3**

- The final phase would focus on user feedback
    - Gather as much feedback and work-on points to improve website.

##  **Structure**
The following standards were established during the creation of this website. They are the primary components of the website's structure and functionality.
These milestones were :

1. Website Structure and Content
2. The Admin Panel
3. System Administration
4. Booking System

This website is make up of two apps and one model:
1. Bookings - contains the main components of the website such as the Model, index.html and booking.html.
2. Webpages - contains the contact-us.html and sauna-steam.html.

#### **Database**

The website uses Heroku and ElephantSQL Postgres relation database to store data. The Booking model requires a database to save customers data for example when they make a booking
or they create an accounts.

The Booking Model is made up of the following fields:

1. booking_id = This is an AutoField which creates a booking Id for each time some creates a booking,
2. name = This is a CharField which takes in and displays a customer name.
3. full_name = This is a ForeignKey which takes in and displays a customer full name
4. email = This is an EmailField which takes a user email and displays a customer email.
5. no_of_persons = This is an IntegerField which take in the number of people booking to swim.
6. booking_date = This is a DateField which allow customers a date to book swimming.
7. booking_time = This is a CharField which gives the customers a list of times they can book their swimming on.
8. phone_number = This is a PhoneNumberField which takes in customers phone numbers.
9. booking_status = This is a CharField which give displays customers booking status.
10. booked_on = This is a DateTimeField which displays the date and time the customer made a booking.
11. approved = This is a BooleanField which is used to approve/reject bookings.

#### **Database Design**

#### **Fonts**

Google Fonts - Russo One
- This font was chosen because I think it goes well with the aqua theme I was trying to create for the website. I think is font is also simple and legiable. This font was used throughout the entire website which changed in size and weight when utilized with different elements, such as a h1 tag or a p tag.

#### **Images**
The images used throughout this project came from my researching online and as well as a few of my own. These images were picked to complement the website's other information, and I thought they were appropriate for the way the site looks.

#### **Colours**

![color-pallette](https://user-images.githubusercontent.com/98041941/208894848-d309fc31-6d28-472f-9fa1-db209ec47f6d.png)


#D9D9D9
- In several places on the website, including the header, footer, and form backgrounds, this colour was utilized.

#001435
- This colour was used for most of the website's font.

#17A2B8

- This colour was used in nearly all of the website's buttons.

#FFFFFF

- The majority of the website's pages by default used this colour.

##  **Skeleton**
These wireframes were made during the planning stage to help me with the layout and design of specific page elements and content. They also assisted me in choosing how to implement particular functionalities.

## **Surface**

### **Features**

#### **Home page**

**Logo:** 
- This website has a logo which can be seen across all pages and it is full responsive. Click the link before to view the website logo.

![wb-logo](https://user-images.githubusercontent.com/98041941/208895879-e30c774a-cd84-4a68-9ad6-9bb5150d70f3.png)

**Navigation Bar:**
- Every page has access to the Navbar, and links to all pages of the website. This navbar is fully responsive in all resolutions.
![Screenshot 2022-12-21 at 04 23 24](https://user-images.githubusercontent.com/98041941/208895295-9d3ce5d2-2e4e-4d2a-a883-2b97607e9cd1.png)

**Pool Opening Hours Tabel**
- The Home page has a tabel which provides customer with the pool opening and closing hours.

![Screenshot 2022-12-21 at 04 24 10](https://user-images.githubusercontent.com/98041941/208895328-e34166a2-96d6-4782-8672-5ebda5626b48.png)

**Footer**
- The website footer can been seen across all pages of the website. The footer is made up of the website copyrights information, pool address and the websites social media links.

#### **Booking page**

**Make booking**
- Once users have been authenticated, they can view every booking that has been made on the booking page. It has a make booking button which allows customers to make a booking and an update or delete booking button which allow a user to update or deleted bookings.

**Sign In or Sign Up Modal**

- The booking page has a Modal which get toggles when there is no user signed in. The Modal prompt users to Sign In or Sign Up for an account.


**Create booking**
- The Create booking page has a booking form which allows customer to make a booking by filling out the form and submiting it.

**Update booking**
- The Update booking page has a booking form which allows customers to update a booking by filling out the form and submiting it.

**Contact us page**
- The Contact us page has a form which alllows customers to send an email to the website if they have any problems or questions. When this form is submitted it send an email to my gmail account which was link using email.JS.

**Sauna Steam page**

- The Sauna Steam page give customers information about the pool's sauna and steam room facilities with supporting images.


---

## **Technologies Used**
 - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - This was used for the structure of the web page and it's content.

- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
    - This was used to style the HTML document.

- [Bootstrap](https://getbootstrap.com/)
    - This was use to implement help with the mobile first feature of the website.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - This was the main tool used to build this project.

- [PEP8 Python Validator](http://pep8online.com/)
    - This was used to check the python code for any errors or warnings.
- [Heroku](https://heroku.com/)
    - This was used to deploy this application.
- [Heroku Postgres](https://www.heroku.com/postgres)
- [Gitpod](https://gitpod.io/)
    - This was the development environment used to build this project.
- [Git](https://git-scm.com/)
    - This is a version control system which I used to handle my project throughout the development stages, to save and push my work from gitpod to github.
- [Github](http://github.com/)
    - This was used to store my project after it was saved and pushed from gitpod.
- [jQuery](https://jquery.com/)
    - This was used for the interactivity, behaviors of the web.

- [JavaScript](https://www.javascript.com/)
    - This was used for the interactivity, behaviors of the web.

- [Google Fonts](https://fonts.google.com/)
    - The main font of the web site was found on Google Fonts.

- [Font Awesome](https://fontawesome.com/)
    - The icons that was used in this project was found on Font Awesome.

- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - This was one of the most used tool throughout the development of this project, as it can be used for tasks like testing, debugging and showing where elements are positioned on the web page.

- [Balsamiq](https://balsamiq.com/)
    - This was used to design the wireframe created for this project.
---

## **Testing**
I started working on automated testing, but when I tried to execute the test I wrote, I got an error. I tried resolving this problem in a few different ways, but I was unable to come up with a workable solution, so I was forced to move on due to lack of time. However I hope you take the timeout to view the test I wrote, it would be much appreciated. Here is the error I encountered [.py:304: RuntimeWarning: Normally Django will use a connection to the 'postgres' database to avoid running initialization queries against the production database when it's not needed (for example, when running tests). Django was unable to create a connection to the 'postgres' database and will use the first PostgreSQL database instead.
  warnings.warn(
Got an error creating the test database: permission denied to create database].
This project was tested manually by using the following methods:

### **Manual Testing**

**Navigation Bar**

- The nav bar is fully responsive on all resolutions and collapses into a hamburger menu as the resolution is adjusted.
- All link in nav bar is working and navigates to the correct pages.
- Signing in and out work as it should with messages being displayed to users.

**Footer**

- The footer is fully responsive on all resolutions.
- All social media links are navigates to correct page. 

**Booking page**
- Creating, reading, updating and deleting bookings are working as this should with message being displayed to users base on their interactions
- All buttons are working and navigates to correct pages
- All buttons are working and performs required tasks
- Booking page is fully responsive which allows users to carry out booking functionalities on different resolutions

**Create Booking page**
- Creating bookings are working as this should with message being displayed to users base on their interactions
- All buttons are working and navigates to correct pages
- All buttons are working and performs required tasks
- Creating-booking page is fully responsive which allows users to view the form to create bookings on any resolution.
- Tested all input fields by intentionally entering invalid data. For example:
    - Entering integers where strings are required and vice versa.
    - Entering special characters where only numbers and letters are required.
    - Entering data that's not specific to inputs fields that requests specific data.
    - Entering the same input numerous times.
    - I asked three family members to use the app to monitior if they would encounter any errors which was good for the testing.

**Update Booking page**
- Updating bookings are working as this should with message being displayed to users base on their interactions
- All buttons are working and navigates to correct pages
- All buttons are working and performs required tasks
- Booking page is fully responsive which allows users to view the form to update bookings on any resolution.
- Tested all input fields by intentionally entering invalid data. For example:
    - Entering integers where strings are required and vice versa.
    - Entering special characters where only numbers and letters are required.
    - Entering data that's not specific to inputs fields that requests specific data.
    - Entering the same input numerous times.
    - I asked three family members to use the app to monitior if they would encounter any errors which was good for the testing.


**Delete Booking**
- Delete bookings are working as this should with message being displayed to users base on their interactions
- All buttons are working and navigates to correct pages
- All buttons are working and performs required tasks
- Delete booking modal work as it should which challenges users when trying to delete a booking.

**Contact-us**
- Contact us page is working as this should with message being displayed to users base on their interactions
- All buttons are working and navigates to correct page.
- Contact us page modal is working whena user submits the form.
- Email get's send successfully to my gmail when the for is filled out correctly
- The webpage is fully responsive which allows users to view the form on any resolution.
- Tested all input fields by intentionally entering invalid data. For example:
    - Entering integers where strings are required and vice versa.
    - Entering special characters where only numbers and letters are required.
    - Entering data that's not specific to inputs fields that requests specific data.
    - Entering the same input numerous times.
    - I asked three family members to use the app to monitior if they would encounter any errors which was good for the testing.
- 

**Admin**
- Admin panel is working as this should with message being displayed to users base on their interactions
- All buttons are working and navigates to correct page.
- The admin  is fully responsive which allows users to view the form on any resolution.
- The admin has the ability to create, view,  update, and delete bookings is working.
- The admin has the ability to approve bookings is working.

**Modals**

- All modal are working base on user interactions
- All modal buttons are working and carrying out required tasks.
- Modal links navigates to correct pages.
- Modal gets toggled on booking page if user is not authenticated.
-Modal works when customers fills out the contact us form.

**Validators**

[W3C HTML Validator](https://validator.w3.org/#validate_by_uri)

- 8 Error
- 3 Warnings

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

- 2 Errors
- 11 Warnings

[JSHint JavaScript Validator](https://jshint.com/)

- 0 Errors
- Undefined variable stripe
    - This varible is being used
    - Used varible which was rectified after calling the function

During the development of the project, the buildt in python extention in the work space was used to test my python code for Pep8 compliance
- Most of the errors were fixed during the development of the project as I resolved the errors when I ever I saw any.
- Alot of the error were meant to do with line spacing and length of characters on each line.
- Some of the errors can not be rectified because of some of the code and there tasks. For example the datababe url and cloudinary url.
- I can confirm that I thoroughly went through all the pythons files and resolved the errors that could be resolved



**Testing with Chrome Dev Tools**
I used Chrome developer tools to test the responsiveness of the website. The website was viewed on several different devices such as:

-Desktop
-Laptop
-Iphone SE
-Iphone XR
-Iphone 12 Pro
-Pixel 5
-Samsung Galaxy 8+
-Samsung Galaxy S20 Ultra
-Ipad Air
-Ipad Mini
-Surface Pro 7
-Surface Duo
-Galaxy Fold
-Samsung Galaxy A51/71
-Nest Hub
-Nest Hub Max
-Iphone 6/7/8
-phone 6/7/8 Plus
-Iphone X
-Ipad
-Ipad Pro

**Browser Testing**
The website was tested in different browsers such as:
- Firefox
- Google Chrome
- Safari
- Opera.


### **Bugs and Errors found**

**Solved Bugs**

**Remaining Bugs**
- No remaining bugs

**Validator Testing**
- W3C HTML Validator
    -  When the W3C HTML Validator first checked base.html code, errors were found. There was 1 HTML error and 13 Django errors.
    - However, I rectified the HTML error by performing the following:
        1. The (Stray end tag </i>) was found and removed. Then the code was retested to check that errors and warnings were rectified.

    - When the W3C HTML Validator first checked contact-us.html code, and error and warnings were found. There was 1 HTML warning, 1 Javascript warnings and 1 Django error.
    - However, I rectified the HTML error and javascript warnings by performing the following:
        1. The (Warning: The type attribute is unnecessary for JavaScript resources) was found and resolved. These files were cut and pasted in base.html Head tags. Then the code was retested to check that errors and warning were rectified.
        2. The (Warning: Empty heading.) was found and resolved. Value was added to empty heading. Then the code was retested to check that errors and warning were rectified.

    - When the W3C HTML Validator first checked sauna-steam.html code, an error was found. There was 1 HTML warning.
    - However, I rectified the HTML error by performing the following:
        1. The (Error: Element ul not allowed as child of element small in this context.) was found and resolved by removing small tags. Then the code was retested to check that errors and warning were rectified.

    - When the W3C HTML Validator first checked booking.html code, 2 errors were found. There were 2 HTML errors.
    - However, I rectified the HTML errors by performing the following:
        1. (The Error: Bad value button for attribute type on element a: Subtype missing.) was found and resolved by removing removing the button attribute type from a tag.
        2. (Error: Element a is missing required attribute href) was found and resolved by adding a href attribute to a tag. Then the code was retested to check that errors and warning were rectified.

    - When the W3C HTML Validator first checked create-booking.html code, no errors or warnings were found.

    - When the W3C HTML Validator first checked update-booking.html code, no errors or warnings were found.

    - When the W3C HTML Validator first checked index.html code, 4 errors were found. There were 4 HTML errors.
    - However, I rectified the HTML errors by performing the following:
        1. (Error: End tag section seen, but there were open elements.) this was causing 2 of the errors with was found and resolved by add the missing div tag.
        2. (Error: Stray end tag div) this was causing 2 of the errors which was found and resolved by removing 2 stray div tags. Then the code was retested to check that errors and warning were rectified.

- W3C CSS Validator
![Screenshot 2022-12-21 at 07 28 26](https://user-images.githubusercontent.com/98041941/208895509-786b283b-5ae3-40c6-94b8-da2959960db4.png)

-  When the W3C CSS Validator to check style.css code, 2 errors and 10 warnings were found.
    - However, I rectified the CSS 2 errors by performing the following:
        1. The (Deprecated media feature min-device-width) was found and resolved by removing the words "only" and "device" from the current value. Then the code was retested to check that errors were rectified.
        2. The (1.1 is out of range) was found and resolved by setting the opacity value to 1. The follow 9 warnings are relation to a unknow vendor extentions that are added by CSS Autoprefixer for cross browser support.


---

## **Deployment**

### **Using GitHub and GitPod**
The main branch of this repository has been used for the deployed version of this application.

The following steps were used to create a repository, setup a workspace and use Github and Gipod.
- Click the Use this Template button.
- Give your repository a name, and description is you wish.
- Click the Create repository from template button to create your repository.
- Click the Gitpod button to create a Gitpod workspace, this could take a few minutes.
- When working on the project using Gitpod, it is best to open the workspace from Gitpod as this will open your previous workspace instead of creating a new one.
    - You can commit your work using the following commands:
        1. git add . - adds all updated files to a staging area.
        2. git commit -m " Add short message explaining your commit" - commits all changes to a local repository.
        3. git push - pushes all your commmited changes to your Github repository.

### **Forking the GitHub Repository**
By forking a GitHub repository you can make a copy of the original repository to your own GitHub account to view and make changes without making any changes to the original repository.

1. Log in to GitHub and local the GitHub repository.
2. At the top right of the page, locate "fork button" which is just below the bell icon.
3. You should now have a copy of the original repository in your GitHub account.

### **Deployment to Heroku**

For the project to run on Heroku, there is a list of dependencies that needed to be installed before deploying the project.

First you need to install the support libraries:

- pip3 install 'django<4' gunicorn
- pip3 install dj_database_url==0.5.0 psycopg2
- pip3 install dj3-cloudinary-storage

The list of dependencies goes into the requirements.txt file by using the following:
-  pip3 freeze > requirements.txt

Create your django project using the following:
- django-admin startproject YOURprojectname .

Then create an app using the following:
- python3 manage.py startapp YOURappname

Next addy your app to the list of installed app in settings.py
- 'YOURappname'

Then you migrate the changes using the following:
- python3 manage.py migrate

Finally try opening your project in the browser using the following:
- python3 manage.py runserver
- Skeleton of the project should be up and running.

**Linking to  a Heroku Database**



**Creating a Heroku account and Heroku app**
- Go to [Heroku.com](https://heroku.com/) and create an account.
- From the Heroku dashboard click Create New App button.
- Enter a name for the project and select your region.
- Click the Create App button.

**Creating a Database**
These steps will create a new PostgreSQL database instance for use with your project. If you don't have an ElephantSQL.com account yet, create one.
- Log in to ElephantSQL.com to access your dashboard.
- Click “Create New Instance”
- Set up your plan
- Give your plan a Name (this is commonly the name of the project)
- Select the Tiny Turtle (Free) plan
- You can leave the Tags field blank

**Create an env.py file**
Keeping things secret
- In your project workspace, create a file called env.py. It’s a good idea to check that this file is included in the .gitignore file too. If you are using the Code Institute provided GitHub template, then the env.py file is already in the .gitignore file.

- In your env.py file add the following line of code. 
    - import os
- Next we need to set some environment variables. First, add a blank line, then set a DATABASE_URL variable, with the value you just copied from ElephantSQL as follows
    - os.environ["DATABASE_URL"]="<copiedURL>"
    - Replace <copiedURL> with the relevant string from ElephantSQL.
- As this is a Django application it has a SECRET_KEY, which it uses to encrypt session cookies. The secret key can be whatever you like.
We need to include this string in the env.py file. So, just like before, add the variable by pasting in the string as follows.
    - os.environ["SECRET_KEY"]="my_super^secret@key"
    - We don't want to share our secrets either, so this documentation shows you a made up key. Just replace my_super^secret@key with your key
- Make sure you save the file.
This secret file isn’t much good on its own. Carry on to edit your settings.py file on the next page, including connecting up your workspace to the new database.

**Modifying settings.py**

- Now you have created an env.py file, you need to make your Django project aware of it. Open up your settings.py file and add the following code below your Path import
    - import os
    import dj_database_url
    if os.path.isfile('env.py'):
     import env
    - The if statement here acts as a little protection for the application in case you try to run it without an env.py file present. You will use the other import in a moment.
- A little further down, remove the insecure secret key provided by Django. Instead, we will reference the variable in the env.py file, so change your SECRET_KEY variable to the following
    - SECRET_KEY = os.environ.get('SECRET_KEY')

- Now that is taken care of, we need to hook up your database. We are going to use the dj_database_url import for this, so scroll down in your settings file to the database section.Comment out the original DATABASES variable and add the code below, as shown
    - (# DATABASES = {
    (#     'default': {
    (#         'ENGINE': 'django.db.backends.sqlite3',
    (#         'NAME': BASE_DIR / 'db.sqlite3',
    (#     }
    (# }
    
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
The code that has been commented out connects your Django application to the created db.sqlite3 database within your repo. However, as we know, that database is not suitable for production. This line of code separates the database URL stored by your env.py file into the relevant name and password etc.

- With those changes in place, make sure to save your file. Your application will now connect to your remote database hosted on ElephantSQL. Not convinced? Let’s prove it.Run the migration command in your terminal to migrate your database structure to the newly-connected ElephantSQL database
    - python manage.py migrate
Once the migrations have completed, head back over to your ElephantSQL dashboard, select your database instance and then select the “Browser” tab on the left.

Click “Table queries” to reveal a dropdown list, you can see your database structure here. You may not recognise all of the tables in the list, many are generated by the authorisation apps used, the important thing is that this list has been populated from your Django migrations.

- Take a moment to add, commit and push your project to GitHub if you haven’t done so already.

**Heroku Config Vars**
With a new database created and the settings.py file set up to connect to it, we will need to connect our new database to Heroku.
- Go back to the Heroku dashboard open the Settings tab
- Add two config vars:
    - DATABASE_URL, and for the value, copy in your database URL from ElephantSQL, no need to add quotation marks.
    - SECRET_KEY containing your secret key.
So now we have created and connected a remote database, configured our settings.py file (for now…) and created some secrets, we have a few more tasks to complete before we deploy. We’ll go through these in the next:

To improve compatibility with various Python libraries, we have updated the deployment template since this video was made. As a result, you must now add another Config Var in Heroku's Settings.
The key is PORT and the value is 8000

Cloudinary Setup
Visit the Cloudinary website
Click on the Sign Up For Free button
Provide your name, email address and choose a password
For Primary interest, you can choose Programmable Media for image and video API
Optional: edit your assigned cloud name to something more memorable
Click Create Account
Verify your email and you will be brought to the dashboard

- On the dashboaord copy API Environment varible : CLOUDINARY_URL=cloudinary://

Then go back to IDE and in your env.py add the following:
- os.environ["CLOUDINARY_URL"] = "YOUR API Environment varible"

After go back to Heroku Config Vars and add the same variable:
- CLOUDINARY_URL    "YOUR API Environment varible"
- DISABLE_COLLECTSTATIC     1

Then go to setting.py and input the following:
- STATIC_URL = '/static/'
- STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
- STATICFILES_DIRS = [os.path.join(BASE_DIR), 'static']
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

- MEDIA_URL = '/media/'
- DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

Then scroll back up to the top of the setting.py under base Directory add the following:
- TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

Scroll down to the middle and in TEMPLATES add the following:
- 'DIRS': [TEMPLATES_DIR],

Scroll back up to ALLOWED_HOSTS add the following code:
- ALLOWED_HOSTS = ["YOURappname.herokuapp.com", "localhost"]

Then in your directory create a Procfile and add the following code:
- web: gunicorn YOURappname.wsgi

Then in the terminal save and commit to GitHub.

**Final Deployment**

- Make sure DEBUG mode is set to False

- git add . and commit -m changes

Head back over to Heroku and go to Config Vars
- Remove DISABLE_COLLECTSTATIC    1


**Deploy section**
- On the same horizontal nav bar, click the Deploy button.
- Scroll to Deloyment methods and click the GitHub button.
- Go to Connect GitHub and search for your repository name in the search bar.
- Then click the Search button.
- When the repository pop's up below the search bar click the Connect button.
- Scroll down to Automatic and Manual deploys
- Click on the Deploy Branch button to deploy project, which would start building the project, and there is also the Automatic Deploys option which updates the project code everytime
  you push work to the GitHub repository.
- Click on the View button to view app and test to see if it works when the app is successfully deployed.

---

## **Credits**

**Code**

I also found a youtube videos that demonstrated how to implement certain functionalities. Code was used from some the websites and the videos. A link to the websites and the videos can be found below. 

These online resources were really helpful when I needed to refamiliarize myself with a specific topic or syntax. They were really education as well.

- [Code Institute](https://codeinstitute.net/)
- [W3Schools](https://www.w3schools.com/default.asp)
- [programiz](https://www.programiz.com/)
- [PyPI](https://pypi.org/)
- [Digital Ocean](https://www.digitalocean.com/)
- [Geeksforgeeks](https://www.geeksforgeeks.org/)

**Content**



### Acknowledgments

- Harry Dhillon - I want to say thank you to my mentor for his time and help throughout the developement of this project.
- Code Institute - I want to say thank you to Code Institute for the support and resources they have provided which facilitated me throughtout the development of this project.
- CI Slack Community - I want to say thank you to the Code Institute Slack community which had alot of supportive content about the modules and coding challenges.

I want to say thank you to my family and friend who have supported and helped me throughout the development of this project.

Finally, thank you for viewing this project and I hope you like it!

---




