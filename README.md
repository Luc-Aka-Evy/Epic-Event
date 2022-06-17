# Epic-Event
Epic-Event is a client relation management (CRM) application built to help companies who organise events in BtoB.

## Install
-Donwload this repository in your local machine by run `git clone https://github.com/Luc-Aka-Evy/Epic-Event.git`

-Create a virtaul environment by run `python3 venv env`

-Activate your virtual env with the command `source env/bin/activate`

-Install all dependecies by run `pip install -r requirements.txt`

-Go in the app directory with the command `cd epic-event`

-Run `python3 manage.py runserver`

This app work with the admin site interface be sure to create a superuser with the command `python3 manage.py createsuperuser` and follow the instructions.

## How to use
There is 4 models availale in this application:

User, Company, Contract, Event

### User
The fields required for an user are (username, first_name, last_name, email, password, is_staff).

you can also add a profile for the user fields are (birth_date, phone_number and gender). 

### Company
A company is define by (name, adress, phone, email, type).

### Contract
A contract is define by (company, created_time, update_time, signed, seller).

created_time and update_time are auto_field, signed is a boolen field to know if the contract is signed or not and seller is an user instance who represent the user who negotiate and create the contract.

### Event
An event is define by (company, contract, description, date, adress, created_time, update_time, support).

support is also a user instance who represent the person in charge of the event.

## API documentation

you can use request with our API to CRUD the models of the application [here](https://documenter.getpostman.com/view/17653278/UzBjsTma) the list of request available
