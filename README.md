# NLS Art (Django Milestone Project) 

# Table of Contents
1. [Introduction](#intro) 
2. [UX](#UX)
3. [Features](#features)
4. [Technologies](#tech)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. <a href="https://nlsart.herokuapp.com" target="_blank">Site</a>

## Introduction <a name="intro"></a>
For this project, I have decided to develop a website for an artist so that potential clients can learn about the artist and purchase works via the e-commerce website. The goal of this project will be to create an attractive and intuitive website. It will give potential customers an interesting and easy experience while being able to contact the artist, and purchase their art.

## UX <a name="UX"></a>

This website will be visited by users who already know in the artist, as well as those who would like to learn about the artist. To ensure both parties, and all of those in between, have a positive emotional reaction to the site, the information must be informative without being jargon-filled. Images will be placed in each section to inform the user, at a glance what the section is about.

### User Stories

Below are four user stories that have been extrapolated out of 2 epics:

#### Epic 1: Users want to be able to learn about the artist and their inspirations and processes.

__User story 1:__ The user wants to learn about the artist's background.

__Solution to user story 1:__ When the user loads the website, an about/ home page is rendered. This contains the background information and life history of the artist.

__User story 2:__ Once the user has read through the information about the artist, they will then want to see more of their work.

__Solution for user story 2:__ At the end of the about section, there will be a button that directs the user to the artist's portfolio.

#### Epic 2: People who are already aware of the artist but would like to purchase some work or contact them for a commission.

__User story 3:__ The user wants to log in and see if any new work has been uploaded to the shop.

__Solution for user story 3:__  In the navbar there will be a portfolio button. this is so that the user does not need to scroll to the bottom of the page to find the portfolio button. This link will take them to a year's page where they can select the year of the artist's work they would like to view, or an all button that calls all years. The next view rendered will be a media template where they can filter what type of work they would like to view, as well as a view all button.

__User story 4:__ The User wants to get in contact with the artist to commission a piece of art.

__Solution to user story 4:__ In the page's footer will be all of the information required to get in contact.

## Features <a name="features"></a>

### Existing Features

__Navbar:__ The navbar is used to easily navigate between the pages of the site, by selecting which page the user wants.

__Landing Images and Button:__ The landing page gives the user a brief but descriptive paragraph about the artist and directs the user to the next section.

__Portfolio Page:__ The portfolio page gives users access to view all of the artwork available to purchase.

__Product Detail Page:__ The product detail page allows the user to read more about the product, view a larger image of the product, and add it to the cart if there are any in stock.

__Bag Page:__ 

__Sign Up:__ A user who is likely to return and possibly purchase more can sign up using a unique username, email, and password to create an account. The authentication and security of this feature is handled by Allauth. The users can also save their default billing information for a faster checkout in the future.

__Log In:__ An existing user can log in using their username and password to immediately access their order history.

__Profile Page:__ When the user has created an account or logged in, they will be directed to their profile page. This page is where they can view their order history and default payment information. Trying to render this page without logging in will direct the user to the login page.

__Superuser:__ Within the Django framework, users can be set to staff or "Superusers". allowing us to create product management views within the website without having to go into the Django admin.

__Add Product:__ Once the superuser has logged in, the user will see the product management link in the profile dropdown menu. Once clicked the add product page will be rendered. This page will have a form that can be filled in to add a new object, with all of the fields required to render it in the products template. The superuser can then either cancel the product creation or upload it to the database via clearly labeled buttons.

__Edit Product:__ If the superuser is logged in, the user will see the edit and delete buttons on every product that is rendered in the product's view. Selecting edit will render the edit product page. This renders a form with the fields already completed from the products database model. These fields can be edited to add or remove information. There will also be cancel and submit buttons at the bottom of the form.

__Recipe Delete Button:__ The delete button will take the product's id and delete the object from the database with that id.

### Features Left to Implement

__Reviews and Ratings:__ I would have liked to implement a page consisting of customer reviews of the artwork they received. A rating system may have been easier to implement but not with my current knowledge and time.

__Upcoming Events:__ I would have liked to have an area on the site where users could see if the artist had any upcoming shows or exhibitions.

## Technologies <a name="tech"></a>
### HTML5
I Used HTML5 because it is the best language for creating static webpages to be displayed on browsers. it is the most efficient and simple to use and understand.

### CSS3
I Used CSS3 because it is the best language for styling HTML5 webpages

### Bootstrap4

### Fontawesome
I used Font Awesome because it has a lot of aesthetically pleasing icons that can be easily implemented with a quick copy and paste. they can turn a webpage from being just lines of text to a more interesting minimalist style with small simplistic images to enhance the text.

<a href="https://fontawesome.com/" target="_blank">Here is a link to the Fontawesome website</a>

### Google Fonts
I used Google fonts because it is a great way to implement different fonts into an HTML document with ease.

<a href="https://fonts.google.com/" target="_blank">Here is a link to the Google Fonts website</a>

### Javascript
I used javascript because it is a tool for accessing and manipulating HTML. Linked with jQuery javascript allows you to implement complex functionality.

<a href="https://www.javascript.com/" target="_blank">Here is a link to the Javascript website</a>

### jQuery
I used jQuery because it allows you to write javascript that implements interactivity into a site by easily creating event listener functions.

<a href="https://jquery.com/" target="_blank">Here is a link to the jQuery website</a>

### Python
I used Python because it works with SQL and NoSQL databases CRUD functionality and has many libraries such as Django, and Allauth which have been used extensively across the project.

<a href="https://www.python.org/download/releases/3.0/" target="_blank">Here is a link to the Python website</a>

### Djando
I used Django for this project because it allows you to create robust, complex and scalable apps quickly.

### AWS
AWS was used to host the static files so that Heroku didnt have to do all of the hard work loading in the large amount of images.

### Heroku
I used Heroku to deploy this app because it is simple to use and allows you to host a whole framework rather than just a static page.

## Testing <a name="testing"></a>

### Code Validation
I started by running my files through the HTML and CSS validator service provided by W3C to ensure there weren't any coding issues.

I then manually tested all of the links and CRUD operations to check they worked correctly. 

I then ensured all of the bag and checkout functionality was working by using stripe's test payment method.

### Responsivity
Because I used Bootstrap, with it's built-in mobile-first design, it allowed me to create a site that minimal CSS for the site to work well on mobile and tablet devices.

## Deployment <a name="deployment"></a>

### Deployment Process
This deployment process was quite complex due to the use of AWS to host the static and media files.

#### 1. I used pip3 to install dj_database_url, psycopg2, and gunicorn. these packages are required to deploy a Django app to Heroku.

####2. created an if statement in the settings.py file at the project level to determine what database to use depending on certain environment variables.

####3. Then create a Procfile to pass to Heroku the type of app and where to run it from. For this app it required:
	web: gunicorn django_nlsart.wsgi:application

####4. I then created the app on the Heroku dashboard and passes in the config var:
	DISABLE_COLLECTSTATIC = 1
This stops Heroku from deploying the static files so that we can host them with AWS later.
During this phase, we also used the database plugin Postgres. Then created config vars for a secret key and a database key.

####5. In the created app dashboard I the selected deploy from Github repo. searched for the repo I wanted to deploy, enabled auto-deploy so that it would redeploy every time that I pushed to git, and then ran the deployment.

####6. The next step was to link AWS S3 to this project so that it could host the static and media files for the project. 

Once I had signed up, I created an S3 bucket, allowing public access and enabling static web hosting.

####7. I then proceeded to generate a bucket policy using the built-in generator, passing in my 'arn' key.

This Policy is then copied and pasted into the bucket policy editor. I added '/*' to the end of the resource to allow access to all resources in the bucket. I then pressed save.

####8. The next step is to create an IAM group to access the S3 resources.

To do this I navigated to the IAM section of AWS and clicked on create a group. I then added the policies for my S3 bucket so that the group has full access to just this bucket. Then created a user within that group to manage the bucket. 

####9. I received a .csv file containing my secret keys to link to my bucket from Heroku. I created some config vars so that these keys would remain hidden. Then linked them to the database in settings.py

####10. I then created a custom storage file to define where static and media files will be stored.

####11. Then in settings.py I created a link to the custom storage file that I just created.

####12. I then Overrode the static and media URLs so that they would send and receive from the files stored in the S3 bucket.

####13. I then pushed all of my changes to git so that Heroku would redeploy with the updated information.


## Bugs

AWS media file would not load all of my images onto the site which is really frustrating as they are what give the home page its clean and nice aesthetic.

I have spent a long time trying to work out how to handle multiple categories in the URL parameters as well as creating functionality around the quantity value of the products in the datbase, which meant that i ran out of time in the end.

## Credits <a name="credits"></a>

All of the art on the site was created by Natalie Lauren Smith.

Click <a href="https://nlsart.herokuapp.com" target="_blank">here</a> to view the site.