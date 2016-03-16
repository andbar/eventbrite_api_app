import requests
import json

from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.db.models.base import ObjectDoesNotExist

from eventbrite_api_app.models import Event

# Create your views here.

def event_search_view(request):
    if request.GET.get('category'):
        response = requests.get(
            "https://www.eventbriteapi.com/v3/events/search/?q={}&expand=venue".format(request.GET.get('category')),
            headers = {
                "Authorization": "Bearer ----------",
            },
            verify = True,  # Verify SSL certificate
        )
        list_of_events = []

        for event in response.json()['events']:
            try:
                db_event = Event.objects.get(evb_id=event['id'])
                body = json.loads(db_event.body)
                list_of_events.append({'name': body['name']['text'], 'id': db_event.evb_id})
            except ObjectDoesNotExist:
                Event.objects.create(evb_id=event['id'], body=json.dumps(event))
                list_of_events.append({'name': event['name']['text'], 'id': event['id']})

        context = {'context': list_of_events, 'message': 'Please search for an event'}
    else:
        context = {'message': 'Please search for an event'}
    return render_to_response('index_template.html', context)


class EventDetailView(View):

    def get(self, request, id):
        event = Event.objects.get(evb_id=id)
        body = json.loads(event.body)
        context = {
            'description': body['description']['html'],
            'city': body['venue']['address']['city'],
            'state': body['venue']['address']['region'],
            'country': body['venue']['address']['country']
        }
        return render_to_response('detail_template.html', context)
