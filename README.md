# The Gram
Author: Vivvianne Kimani
26th July 2019

## Description 

This application was built by Django version 2.2.3 a python framework.

The gram is an application that lets you display your photos for others to view,others are supposed to comment,like,follow and unfollow.

## User Stories

As a user of the application i should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

## Setup/Installation Requirements

* Install python version 3.6.3

* Install Heroku that helps to deploy your application.

* Clone https://github.com/Vivvianne/TheGram.git

* Have an internet connection

* Install Django

* Create a virtual environment

    - $ sudo apt-get install python3.6-venv

    - $ python3.6 -m venv virtual

    - $ source virtual/bin/activate

    - Install gunicorn: (virtual)

## Live site 

One can view the live site here https://vivthegram.herokuapp.com/


## BDD
| Behavior | Input | Output|
| -------|-------|-------|
| Display homepage when user visits the site | NA | NA |
| Create an account | Click on register | Create an account and profile for the user and log the user into the site |
| View profile | Click on the profile link on the navbar and update profile if a user wishes| Updated profile |
| View a post | Click on the descriptin link | Can view the chosen post |
| Create new post | Click on New post | One can create a post |
| Update a post | Click on the post to be updated and click on update button | Then update the field of the form |
| Delete a post | Choose the post to be deleted , click on the delete button | Post deleted |
| Update profile | Once logged in you can click on the profile link on the navbar update the fields, click on update | Profile will be updated |


## Technologies Used
Python version 3.6.3
Django version 2.2.3
Bootstrap 3 and 4 on cdn
Postgres Database
HTML & CSS
Heroku

## Known bugs
One cannot be able to add a comment
One cannot be able to like or follow a user


## Licence
[MIT]  https://github.com/Vivvianne/TheGram/blob/master/LICENSE
