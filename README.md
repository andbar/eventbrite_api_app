# eventbrite_api_app
A small Django app that consumes part of the Eventbrite API for fun.

Eventbrite has a pretty awesome API setup and they make it really easy to use (find out more here: https://www.eventbrite.com/developer/v3/quickstart/). I decided to build a Django app that uses their API, just to play around with it for a bit and get more familiar with it.

Users can enter terms into the search box on the main page and hit the submit button. The app will connect to Eventbrite's API endpoint for searching events and return a JSON response. The name of each event from the response is then displayed on the page, with a link to a detail page about the event. The event is also saved in the local database if it's not already there, with the event id and the body of the JSON response.

When a user clicks the link to the detail page for a specific event, the app gets the details from the local database. It renders the venue location along with the html description of the event to the template.
