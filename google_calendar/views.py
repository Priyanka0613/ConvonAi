from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# Google Calendar Init View
class GoogleCalendarInitView(View):
    def get(self, request):
        flow = Flow.from_client_secrets_file(
            "C:\\Users\\Dell\\ConvonAiassignment\\ConvonAiassignment\\json file\\client_secret_1091150141238-7m6g89r5h8c0bmqrkm7ous5g8vhvniu4.apps.googleusercontent.com.json",

            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri=request.build_absolute_uri(reverse('calendar-redirect'))
        )
        authorization_url, state = flow.authorization_url(prompt='consent')

        # Store the OAuth state in the session
        request.session['oauth_state'] = state

        return HttpResponseRedirect(authorization_url)


# Google Calendar Redirect View
class GoogleCalendarRedirectView(View):
    def get(self, request):
        state = request.session.pop('oauth_state', '')
        flow = Flow.from_client_secrets_file(
            "C:\\Users\\Dell\\ConvonAiassignment\\ConvonAiassignment\\json file\\client_secret_1091150141238-7m6g89r5h8c0bmqrkm7ous5g8vhvniu4.apps.googleusercontent.com.json",
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri=request.build_absolute_uri(reverse('calendar-redirect'))
        )

        # Exchange the authorization code for an access token
        flow.fetch_token(authorization_response=request.build_absolute_uri(), state=state)

        # Create the Google Calendar API service using the access token
        credentials = flow.credentials
        service = build('calendar', 'v3', credentials=credentials)

        # Use the service to interact with the user's calendar (e.g., retrieve events)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        # Process the events as needed
        # ...

        return HttpResponse("Events retrieved successfully")


# def google_calendar_redirect_view(request):
#     # Specify the state when creating the flow in the callback so that it can
#     # verify in the authorization server response.
#     state = request.session['state']
#     if state is None:
#         return Response({"error": "State parameter missing."})

#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
#         CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
#     flow.redirect_uri = REDIRECT_URL

#     # Use the authorization server's response to fetch the OAuth 2.0 tokens.
#     authorization_response = request.get_full_path()
#     flow.fetch_token(authorization_response=authorization_response)

#     # Save credentials back to session in case access token was refreshed.
#     # ACTION ITEM: In a production app, you likely want to save these
#     # credentials in a persistent database instead.
#     credentials = flow.credentials
#     request.session['credentials'] = credentials_to_dict(credentials)

#     # Check if credentials are in session
#     if 'credentials' not in request.session:
#         return redirect('v1/calendar/init')

#     # Load credentials from the session.
#     credentials = google.oauth2.credentials.Credentials(
#         **request.session['credentials'])

#     # Use the Google API Discovery Service to build client libraries, IDE plugins,
#     # and other tools that interact with Google APIs.
#     # The Discovery API provides a list of Google APIs and a machine-readable "Discovery Document" for each API
#     service = googleapiclient.discovery.build(
#         API_SERVICE_NAME, API_VERSION, credentials=credentials)

#     # Returns the calendars on the user's calendar list
#     calendar_list = service.calendarList().list().execute()

#     # Getting user ID which is his/her email address
#     calendar_id = calendar_list['items'][0]['id']

#     # Getting all events associated with a user ID (email address)
#     events = service.events().list(calendarId=calendar_id).execute()

#     events_list_append = []
#     if not events['items']:
#         print('No data found.')
#         return Response({"message": "No data found or user credentials invalid."})
#     else:
#         for events_list in events['items']:
#             events_list_append.append(events_list)

#     # return Response({"error": "calendar event aren't here"})
#     return Response({"events": events_list_append})


# def credentials_to_dict(credentials):
#     return {'token': credentials.token,
#             'refresh_token': credentials.refresh_token,
#             'token_uri': credentials.token_uri,
#             'client_id': credentials.client_id,
#             'client_secret': credentials.client_secret,
#             'scopes': credentials.scopes}