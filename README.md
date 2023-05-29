# ConvonAi
Google calendar integration using Django REST API using OAuth2 mechanism to get users calendar access

1. Add the virtual environment >myenv in a folder.

2. In the directory where folder is present, open command prompt and run the following:
```
myenv\Scripts\activate
```

3. In the same folder where >myenv is present, upload the ConvonAiassignment

4. Run the following:
```
pip install Django
pip install django-allauth requests
pip install google-auth google-auth-oauthlib google-auth-httplib2
```
5. Add Sqlite to your path in environment variables to run the database sqlite.

6. Further run:
```
cd ConvonAiassignment
```

7. When entered the main ConvonAiassignment directory, run:
```
python manage.py runserver
```

8. In the browser open the developemnt server + /rest/v1/calendar/init/
RUN:***http://127.0.0.1:8000/rest/v1/calendar/init/***

After confirming the email id, a smilar screen would appear:

<img width="280" alt="image" src="https://github.com/Priyanka0613/ConvonAi/assets/95872454/ef11508e-3db8-4a7e-b560-4f8839279bff">

9. Click "Allow", list of events in users calendar would be retrieved successfully.
