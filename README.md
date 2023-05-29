# ConvonAi
Google calendar integration using Django REST API using OAuth2 mechanism to get users calendar access

1. Add the virtual environment >myenv in a folder.
2. In the directory where folder is present, open command prompt and run the following:
```
myenv\Scripts\activate
```
3. In the same folder where >myenv is present, upload the ConvonAiassignment
4. Further run:
```
cd ConvonAiassignment
```
5. When entered the main ConvonAiassignment directory, run:
```
python manage.py runserver
```
6. In the browser open the developemnt server + /rest/v1/calendar/init/
RUN:***http://127.0.0.1:8000/rest/v1/calendar/init/***

After confirming the email id, a smilar screen would appear:

<img width="280" alt="image" src="https://github.com/Priyanka0613/ConvonAi/assets/95872454/ef11508e-3db8-4a7e-b560-4f8839279bff">

7. Click "Allow", list of events in users calendar would be retrieved successfully.
