# Note
This code once supported the fraternity website for the Miami University Colony of Theta Tau.
The website has moved from being powered by Django to being powered by Jekyll as Jekyll allows for significantly easier maintanence and hosting.
The new website repository can be found at github.com/ThetaTauMiami/thetataumiami.github.io.
This repository is kept purely for archival purposes. 
The remainder of this README is kept unchanged from the website's final state.

# The Website for Theta Tau - Miami University Colony

## Requirements

This website runs on Django and it requires the following: 

* Python 2.7
* Django 1.6
* dj_static
* dj_database
* django-htmlmin

If you are running this locally on a Unix-based machine (Linux, Mac OS X) these can be installed via pip

Install pip with
	
	sudo easy_install pip

Run the following commands at the shell

    sudo pip install django dj_database_url dj_static django-htmlmin

The project should be able to be run locally by running

	python manage.py runserver

If you are running locally on a Windows machine, you will still need to install each component.
Pip is available for Windows and should be able to install each of these components
