# eventbrite_api_app
A small Django app that consumes part of the Eventbrite API for fun.

Eventbrite has a pretty awesome API setup and they make it really easy to use (find out more here: https://www.eventbrite.com/developer/v3/quickstart/). While preparing for a job interview with them, I decided to build a Django app that uses their API.

Users can enter terms into the search box on the main page and hit the submit button. The app will connect to Eventbrite's API endpoint for searching events and return a JSON response. The name of each event is then displayed on the page, with a link to a detail page about the event.

When a user clicks the link to the detail page, the app first checks the local database to see if that event is already stored, and if so it grabs the location from the parsed json as well as the html description and renders them to the template. If the event is not already in the database, the app connects to the Eventbrite API endpoint for that event, saves the event id to the database along with the full JSON response as the body (including venue info from the linked 'venue' table) and then displays the location and the html description on the page for the user.
