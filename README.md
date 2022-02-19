![Luke's Animé Base Responsive Image](static/images/amiresp.png)

# Luke's Animé Character Base

## # Table of contents:

1. [Link To Live Site](#linktolivesite)
2. [LucidChart ERD Diagram](#lucidcharterddiagram)
3. [Wireframes](#wireframes)
3. [Overview](#overview)
4. [User Stories](#userstories)
6. [Features](#features)
    1. [Index Page](#indexpage)
    2. [Character View Page](#characterviewpage)
    3. [View/Add Series List Page](#serieslist)
    4. [Suggestions Page](#suggestionspage)
    5. [Sign In/Out/Up Pages](#signin/out/uppages)
    6. [Create/edit Character Page](#createcharacterpage)
7. [Features to Implement](#featurestoimplement)
8. [Testing](#testing)
    1. [Lighthouse Reports](#lighthousereports)    
9. [Unfixed Bugs](#unfixedbugs)
10. [Deployment](#deployment)
    1. [Forking and Cloning](#forkingandcloning)
    2. [Local Deployment](#localdeployment)
    3. [Remote Deployment](#remotedeployment)
11. [Credits](#credits)


## Link to live site

https://lukeanimebase.herokuapp.com/

## LucidChart ERD Diagram

[Luke's Animé Base ERD Diagram](static/images/lukeanimebaseERD.png)

## Wireframes

In order to bring my idea to life, I have knocked up some wireframes in order to help me make my app and how to structure the content. I have made these for each relevant page (some i have grouped together as content and forms are going to look so similar):

[Index page](static/images/index.png)

[Character Detail](static/images/character_detail.png)

[Series List](static/images/series_list.png)

[Suggestions](static/images/suggestions_wireframe.png)

[Create/Edit Character/Series/Suggestion](static/images/add_edit_char_series_sug.png)

[Sign In/Up](static/images/sign_in_up.png)

[Sign Out](static/images/sign_out.png)

## Overview

Luke's Animé Character Base is a site that will allow the Owner of the site to manage their favourite characters from their favourite animé shows.

The owner of the site can create a series and then list their favourite characters. Users will then be able to rate their favourite characters and leave comments on them for the Owner to review.

If a character that the users like doesn't appear on the site, then they can send a suggestion to the Owner and other people can see the suggestions too.

## User Stories

When people visit my site, I want them to be able to engage with the content; View their favourite characters, rate them, see the list of series that the admin has viewed and added as well as see and leave suggestions for the admin to review and implement at their leisure.

In order for my site to maximise the engagement, this is the list of user stories to address my problem statement - "How do I create a site that allows the maximum engagement from users to interact with my content"

1. Display characters list
2. Add character
3. Edit character
4. Delete character
5. Display series
6. Add series
7. Edit series
8. Delete series
9. Display suggestions
10. Add suggestions
11. Delete Suggestions
12. Rate characters
13. Comment on characters
14. Delete Comments

## Features

For my Animé Character Base, I have chosen a very simple color scheme that is consistant throughout my site;

- I chose dark base colors for the main content to be displayed on.
- Recurring themes in some animé is the color orange (Naruto's suit and Ichigo's hair etc) which will be the prominant color for text and icons.
- I though card style for the displaying of characters with simple functions through the use of buttons for each character or series. I went with the nice white background to help it stand out against the darker background.
- My list of suggestions is a simple collapsible list so that people can see what is suggested, but open up the suggestions to find out why people are suggesting them.
- My Main nav bar is responsive to the size of the screen and allows fo a drop down in case of smaller screen sizes. It is also adaptable depending on if you are logged in (able to see suggestions and leave comments) or are a superuser (capable of adding character and series and deleting items). The darker colour scheme is to separate it from the main body of the site whilst still leaving the contract between elements clear.
- My footer is consistant across all pages as well; orange banner with a couple of pieces of writing. The amount of writing is different depending on the size of the screen as we dont want to bar to suddenly increase in height and obstruct any of the other elements for nav or viewing/editing/deleting.

These are the pages that I have set up in order to make the site as functionable as the Owner may need. This is what I have made: -

### Index


### Displaying Characters



### Create/Edit Characters/Series/Suggestions




### Views Series List Page


### Suggestion Page


### Sign In/Out/Up Pages




## Features to Implement

This is a list of things that I would like too implement if I had more time

## Testing

### Lighthouse Reports

[Create character page](static/images/lighthouse-reps/add-character-lighthouse.png)

[Character details](static/images/lighthouse-reps/char-details-lighthouse.png)

[Deleting objects page](static/images/lighthouse-reps/delete-lighthouse.png)

[Index page](static/images/lighthouse-reps/index-lighthouse.png)

[Series list page](static/images/lighthouse-reps/series-list-lighthouse.png)

[Signout page](static/images/lighthouse-reps/signout-lighthouse.png)

[Signup/in page](static/images/lighthouse-reps/signup-in-lighthouse.png)

[Suggestions page](static/images/lighthouse-reps/suggestions-lighthouse.png)

html testing

css testing

python testing

### Site Tests

## Unfixed Bugs

Anythng that doesn't work properly

## Deployment

To deploy the project, allow other people to run the app and see it working, there are 3 methods to allow you to complete these actions:

### Forking and Cloning

Accessing GitHub and navigating to my repositories will allow users to copy my code directly from the source, either by forking or cloning: Accessing the animé character base repository and clicking on the code button next to Gitpod link will bring up a drop-down to create a repository of your own in your own GitHub repo. You can also download a zip file and copy the information into a new file of your own making to continue working on it.

### Local Deployment

### Local Deployment

For my local deployment, I use Gitpod to edit and run my terminal;
- From GitHub, once the repository has been created (either as a new project or by forking/cloning) I will then click on the Gitpod button to implement the creation of a workspace to edit the promotional sales review system.

***The workspace should not be closed due to the env.py file - as it is never added to GitHub, if you create a new workspace you will need to re-add the env.py file and reinstall all libraries used each time. Pinning a workspace and accessing it from Gitpod workspaces rather than GitHub button would prevent this loss of information each time***

### Remote Deployment

For this project, the remote deployment is a complex procedureand I will list out the complete steps in order to make your site work on a separate hosting service; For my project I will be using Heroku.

- This first step, once we are in Gitpod, is to install our required packages and libraries:
    - Using Command Line Interface (CLI) in the terminal, type:

            pip3 install Django==3.2 gunicorn
            pip3 install dj_database_url psycopg2
            pip3 install dj3-cloudinary_storage

    - we need to add these to our requirements.txt file using the CLI:

            pip3 freeze --local > requirements.txt

- We now need to build our Project structure using he CLI:

        django-admin startproject PROJ_NAME .
***The trailing full stop is very important so please don't forget to include it in your command***
    - For my project I named it lukeanimebase, but you can choose anything.

- Once we have the project, we need to create an actual app to handle our individual functions:
    
        python3 manage.py startapp APP_NAME

    - My app is called collection as it is designed to handle my collection of character, comments, series and suggestions.

- Now we have an app, we need to add it t our approved INSTALLED_APPS in the Project settings.py file

- Once they are linked, we have to migrate changes to our database - by creating the app we have created a models.py file which handles our database designs and these have to be migrated over to the database in order to fucntion. To do this, in the CLI terminal, type:

        python3 manage.py migrate

- To test if this is correctly built, in CLI, type:

        python3 manage.py runserver

This has built the foundation for our project, now we need to get th Heroku App built to receive the information from Github.

- In Heroku.com create/sign in to account and then navigate to the dashboard and create a new app with an appropriate APP_NAME and set the region to whicever is most appropriate - for myself it was Europe.
- We need to add a database to the app to store our uploaded record entries: For this, we need to go to the Rsources tab and run a search for the Add-on called 'Heroku Postgres'
- in the Settings tab, we can now click Reveal Config Vars and we have a new KEY/VALUE pair for our DATABASE_URL with a postgres:// address. Copy the Value in its entirety.

We will now be swapping between our Dev Environment as well as Heroku to complete deployment.

- In our Dev Environment, we need to create a new env.py file to handle all our values that we need to keep secret. This must be in the top level of our file structure. We need to import a library and define some details into this file:

        import os

        os.environ["DATABASE_URL"] = "paste postgres:// here"

        os.environ["SERCRET_KEY"] = "input a secret key"

***There are secret key generators online to help you generate one, or you can siply put a random string of letters together***

- Take the secret key value and head to the Heroku dashboard reveal config vars again.
    - This time add a new key called SECRET_KEY
    - Paste in the value you copied from the env.py file

- In our settings.py file, we now need to make sure our project references the new variables from the env.py file, so we need to add below the current imports Path line:

        import os
        import dj_database_url

        if os.path.isfile("env.py"):
           import env

- There is already a secret_key variable, but we need to replace the existing value with os.environ.get("SECRET_KEY")
- We have a databases variable already assigned as well, but we are going to comment out this existing section and replace it with our own:

        DATABASES_URL = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }

- Now we have linked up a new Database, we nee to migrate our files again to make sure they are linked - In CLI type:

        python3 manage.py migrate

Along with our DevEnv and Heroku, we also need one additional facility to handle our static and mdeia files: Cloudinary

- In a browser, navigate to Cloudinary.com and sign in/up for an account.
- Once in, you will have, on your dashboard, a set of informations for linking your DevEnv and Heroku to it.
    - Copy the CLOUDINARY_URL (also known as the API Environement Variable) value and head over to the env.py file:

            os.environ["CLOUDINARY_URL"] = "cloudinary:// pasted here"

    - Back in Heroku, settings, reveal config vars, add new Key/Value pair called CLOUDINARY_URL with the "cloudinary:// value"
    - The last thing we need to add to our Heroku for now is the DISABLE_COLLECTSTATIC Key with the value set to 1.

- In our INSTALLED_APPS in the setting.py file, we must now add a couple of new lines:

        'cloudinary_storage',    //this must go above staticfiles
        'django.contrib.staticfiles',    //this already exists
        'cloudinary',    //this must go below the staticfiles

***The order of these lines is very important so make sure they are in the correct order!!!***

- In order for our app to use the correct storage location, we need to tell our settings.py file the correct Cloudinary information. Below the STATIC_URL = "/static/", add:

        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

- We now need to link the file to the templates directory in Heroku. Under the BASE_DIR line, add:

        TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

- We need to tell the templates directory where we will find the templates we will be using, so in TEMPLATES, in the 'DIRS' variable list, we need to add 

        'DIRS': [TEMPLATES_DIR],

- The last thing in our settings.py file we need to include, is the host  locations for running our app. We need one for Heroku and one for our local DevEnv, so we just need to adjust the following:

        ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]

- So now we have a storage for our fies, we need to add our folders to the correct locations - in our top level of the directory, we now need to add media, static and templates.

- We need to create a file that tells Heroku exactly how we expect the app to be run, so we need to create the Procfile (The initial cap is intentional) in the top level of the directory.
- In Procfile, we need to add:

        web: gunicorn PROJ_NAME.wsgi

We now need to save the files and structure we have created in gitpod to our GitHub repository using the CLI:

        git add .
        git commit -m "deployment commit"
        git push

Once this has been pushed to our main branch, we need to get our main branch deployed to Heroku.

- In Heroku, Deploy tab, we can add our Github repository to the deployment method. Once this is linked, we can scroll down and deploy the main branch.

At this point, the same screen from our 'runserver' test should now be displayed in the deployed webpage. This is the basic deployment of the app completed.

## Credits

I would like to thank the dedicated team of tutors at Code Institute for helping me to overcome certain issues with the project regarding a number of different problems that arose.
My mentor Chris Quinn was amazing at helping me to understand the project and guide me to create the best possible project.
The Slack community helped me with user stories and quick fixes that allowed me to progress with my project when I became stumped.

