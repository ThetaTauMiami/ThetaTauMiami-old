# The Website for Theta Tau - Miami University Colony

## Requirements

This website runs on Django and it requires the following: 

* Python 2.7
* Django 1.6
* dj_static
* dj_database
* django-htmlmin
* BigLittlePairing

If you are running this locally on a Unix-based machine (Linux, Mac OS X) these can be installed via pip

Run the following commands at the shell

    sudo pip install django dj_database dj_static django-htmlmin
    
and clone the repository for BigLittlePairing

	git clone https://github.com/rogerskw/BigLittlePairing.git
	
and configure your project to reference the BigLittlePairing project.

The project should be able to be run locally by running

	python manage.py runserver

If you are running locally on a Windows machine, you will still need to install each component.
Pip is available for Windows and should be able to install each of these components