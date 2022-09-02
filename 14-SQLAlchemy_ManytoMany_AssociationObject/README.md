

-----------------------
### Notes
-----------------------
Add the `TeachingAssistant` model and create a *many-to-many* relationship from `Course` to `TeachingAssistant` by creating the *association object* `TA_Assignment`.

-----------------------
#### Running the application
-----------------------

To run this example:
- Start the application with the following command:

Windows:    set FLASK_DEBUG=1 && python -m flask run
Mac/Linux:   export FLASK_DEBUG=1 && python -m flask run

pip install WTForms-SQLAlchemy