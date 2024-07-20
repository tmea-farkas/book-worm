# Welcome to Read.it - the happy place for bookworms

## Introduction

Read.it (similar pronunciation to 'reddit') is a website built in Django, using HTML, CSS, Bootstrap, Javascript and Python.
The projects' target audience are people who love to immerse themselves in the World of books.
This reddit-style blog is essentially a personalised, virtual library where the user can upload, summarize, review and discuss book they've read. Users can make posts, delete or edit them, write and delete comments under posts and up/downvote a post.


![Site image](image.jpg)

To visit the deployed site on Heroku, click [here](https://www.example.com).

In the following chapters, I will detail all aspects of production.

## Contents
- UX Design
  - The Strategy Plane
    - User Stories
  - The Scope Plane
  - The Structure Plane
  - The Skeleton Plane
    - Wireframes
  - The Surface Plane
- Features
  - Existing Features
  - Future implementations
- Technologies used
- Deployment
- Testing
- Credits

# UX Design

## The Strategy Plane

Read.it is a virtual library where users can upload books they've read, create posts about them, leave comments, up/downvote on others posts, search for book-related posts and delete their own posts or comments. Graphics and design has been carefully curated to ensure a fun and engaging experience.

### User Stories

**As a User**
1. 
2. 
3. 
4.  
5. 
6. 

**As a Developer**
1. 
2. 
3. 
4. 
5. 
6. 

## The Scope Plane

### Planned Features:

- user log in / log out
- make a post
- like/dislike a post
- leave a comment
- request admin privileges
- light/dark mode
- choose a genre
- search bar
- birthday greetings
- private message other users

### Future Implementations

- 
- 

### Technologies used

Django:
Django==3.2
django-allauth==0.48.0
gunicorn==20.1.0 - web dyno
dj-database-url~=0.5 - Python package utility to connect Django to a database using a URL
psycopg2~=2.9 - driver for intercating with PostgreSQL using Python


- Django was used as the main Python framework in the development of this project. 

- Heroku - was used as the cloud based platform to deploy and host the project

- HTML

- CSS 

- Bootstrap

- Font Awesome

- 



### Deployment

**Deploying to Heroku**
- Started by navigating to my Heroku dashboard
- Create new app
- Added DISABLE_COLLECTSTATIC to config.vars
- Got my code ready for deployment by:
  - installed gunicorn~=20.1 webserver
  - created a Procfile in the root directory where I declared a process and added a start command
  - changed DEBUG to False
  - added Heroku to ALLOWED_HOSTS
  - commited and pushed my code to GitHub
- Connecting my GitHub Repository to the app
- Chose manual deployment


### Testing

### Credits
