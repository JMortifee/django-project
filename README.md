# NLS Art (Django Milestone Project) 

# Table of Contents
1. [Introduction](#intro) 
2. [UX](#UX)
3. [Features](#features)
4. [Technologies](#tech)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. <a href="https://kujoskombucha.herokuapp.com" target="_blank">Site</a>

## Introduction <a name="intro"></a>
For this project, I have decided to develop a website for a recipe and community site for kombucha home brewers. The overall goal of the project will be to create an attractive and intuitive website that is easy to use for community members to visit and share their recipe ideas.

The website will have an account creation function so that you can create edit and delete recipes for other users to view and tryout.

## UX <a name="UX"></a>

This website will be viewed by community members who are both knowledgable, and completely new to the kombucha process. To ensure both parties, and all of those in between, have a positive emotional reaction to the site, the information must be informative without being jargon-filled. Images will be placed in each section to inform the user, at a glance what the section is about.

### User Stories

Below are four user stories that have been extrapolated out of 2 epics:

#### Epic 1: Users want to be able to learn about what kombucha is and how to make it as well as community support in creating their own kombucha at home.

__User story 1:__ The user wants to find out how to make kombucha.

__Solution to user story 1:__ When the user loads the website the landing page will display a friendly fluffy character that says he is going to teach the user how to make kombucha.

__User story 2:__ Once the user has read through the information about how to make kombucha they may want to view some recipes to try out for themselves.

__Solution for user story 2:__  at the end of the get started page there is a button that directs the user to the community recipes page that are all created by other users.

#### Epic 2: Existing community members or users who have been to the site before can log in and interact with thier own, as well as othe rcommunity members recipes.

__User story 3:__ The user knows how to make kombucha but just wants to log in to update or create a new recipe they have come up with.

__Solution for user story 3:__  In the navbar there will be a login button that existing users can click to imediatly direct them towards logging in to their account.

__User story 4:__ The User just wants to see if there have been any new recipes added to the page.

__Solution to user story 4:__ In the nav bar there will be a button that directs the user straight to the recipe page where they can see if any new recpes have been added.

## Features <a name="features"></a>

### Existing Features

__Navbar:__ The navbar is used to easily navigate between the pages of the site, by selecting which page the user wants.

__Landing Images and Button:__ The landing page gives the user a breif but descriptive paragraph about the website and directs the user to the next section.

__Recipes Page:__ The recipes page gives a first time or one off user access to community created recipes to use as research or try out for themselves giving them a taste of the website and its community without having to sign up.

__Individual Recipe Page:__ The individual recipe page allows the user to view the ingredients and the steps required to make the recipeat home. The url routing allows for the user so save the recipe as a favorite on their browser so that they can revisit the recipe, as long as the recipe name hasn't been changed or the recipe deleted. 

__Sign Up:__ A user who wants to interact with the community or share their recipe ideas can create an account the user needs to provide a unique username, email and password to create an account.

__Log In:__ An existing user can log in using their username and password to imediatly access the member only content.

__Profile Page:__ when the user has created an account or logged in they will be directed to their own profile page. this page is where they can create, edit and delete their recipes. trying to render this page without logging in will direct the user to the login page.

__Recipe Creation:__ Once logged in the user will see the create recipe button on their profile, once clicked they will be directed to the recipe creation page where they can add a name, ingredients, and a method for the recipe. once submited the recipe will be posted to the database along with a fourth field of the authors unique username. This will be displayed on the recipe screen along with the recipe name giving credit to the author.

__Recipe Edit Page:__ If a user would like to edit their recipes they can easily click edit recipe. this will take them to a page similar to the recipe creation page however it will load into the fields the values they entered when creating this. if the user changes their mind they can cancel the edit and go back to thier profile page, but if the click on submit the changed fields will be updated in the database.

__Recipe Delete Button:__ if the user is not happy with their recipe and would like to remove it from the site they can easily click on the delete button removing their recipe permanently from the database.

### Features Left to Implement

__Recipe Comments/ Rating:__ I would have liked to implement a comments section under each recipe so that the author or other users could read about how good/ easy the recipe was to do at home. A rating system may have been easier to implement but not with my current knowledge and time.

__Blog/ Chat Area:__ I would have liked to have an area on the site wher new and existing users could ask other community members questions about the subject. I felt this was not possible for me to implement at this time.

__Emails to Users:__ I would have liked to set up an email system with users hence the sign up requiring an email address. This was so that I could send newsletters and updates to current users directly as well as allow users who forgot their account details to retrieve them via a secure location.

__User Profile Pictures:__ user profile pictures would allow community members to have a face to the name making the site feel more like a community. I didnt implement this because I didnt want lots of images to use all of the space on my database.

## Technologies <a name="tech"></a>
### HTML5
I Used HTML5 because it is the best language for creating static webpages to be displayed on browsers. it is the most efficient and simple to use and understand.

### CSS3
I Used CSS3 because it is the best language for styling HTML5 webpages

### Materialize
I used Materialize because it uses CSS3 to implement styles into HTML documents via class names. This greatly increases the speed in which a webpage can be generated without having to style every single element on the page. The CSS code can then be overwritten by a custom CSS file or inline styling.

<a href="https://materializecss.com/getting-started.html" target="_blank">Here is a link to the Materialize website</a>

### Fontawesome
I used Font Awesome because it has a lot of aesthetically pleasing icons that can be easily implemented with a quick copy and paste. they can turn a webpage from being just lines of text to a more interesting minimalist style with small simplistic images to enhance the text.

<a href="https://fontawesome.com/" target="_blank">Here is a link to the Fontawesome website</a>

### Google Fonts
I used Google fonts because it is a great way to implement different fonts into an HTML document with very little effort.

<a href="https://fonts.google.com/" target="_blank">Here is a link to the Google Fonts website</a>

### Javascript
I used javascript because it is a great tool for accessing and manipulating HTML. Linked with jQuery javascript adds great functionality to sites with relativey easy code.

<a href="https://www.javascript.com/" target="_blank">Here is a link to the Javascript website</a>

### jQuery
I used jQuery because it allows you to very easily and quickly write javascript that implements interactivity into a site by easily creating event listener functions.

<a href="https://jquery.com/" target="_blank">Here is a link to the jQuery website</a>

### Python
I used Python because it works great with SQL and NoSQL databases CRUD funtionality and has lots of libraries such as Flask and PyMongo to make these processes easier to implement.

<a href="https://www.python.org/download/releases/3.0/" target="_blank">Here is a link to the Python website</a>

### MONGO DB
I used Mongo DB because I felt its NoSQL structure complemented the type of information I was going to be storing on the database.

<a href="https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongo%20db&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=EAIaIQobChMIoZrj5pf57wIV4-jtCh0p-AF8EAAYASAAEgJyB_D_BwE" target="_blank">Here is a link to the Mongo DB website</a>

### PyMongo
I used the PyMongo library in my project because it allowed me to very easily write CRUD operations in my python app.

<a href="https://pymongo.readthedocs.io/" target="_blank">Here is a link to the PyMongo website</a>

### Flask
I used Flask because it allowed me to create a mini framework for my site by using methods in my code such as templates and password hashing by combining other libraries such as jinja and Werkzueg. 

<a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Here is a link to the Flask website</a>
<a href="https://jinja.palletsprojects.com/en/2.11.x/" target="_blank">Here is a link to the Jinja website</a>
<a href="https://werkzeug.palletsprojects.com/" target="_blank">Here is a link to the Werkzueg website</a>

## Testing <a name="testing"></a>

### Code Validation
I started by running my files through the HTML and CSS validator service provided by W3C to ensure there were no coding issues.

I then manualy tested all of the links and CRUD operations to check they worked correctly. 

I then roped some family and friends into creating an account and some recipes and deleting them to ensure that the operations didn't ever break or return errors.

### Responsivity
Because I used Materialize, it's built in, mobile first, design allowed me to create a site that only needed a few adjustments for the site to work well on mobile and tablet devices. 

## Deployment <a name="deployment"></a>

I used heroku to deploy my project as git hub pages who I had previously used only allows for static sites.

Deploying to heroku was very simple and painless I linked my git hub repository to the app on heroku so that it would automatically update any changes I commited.

To deploy I needed a requirements.txt file so that heroku knew what libararies the project needed to run. As well as a procfile to specify the type of app and the app file name and language.

After doing this I pressed deploy and the app was deployed to the site.

## Credits <a name="credits"></a>

##### Home

All of the art on the site was created by me and Natalie Lauren Smith.

Click <a href="https://kujoskombucha.herokuapp.com" target="_blank">here</a> to view the site.