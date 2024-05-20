from dotenv import load_dotenv

import azure.functions as func

import logging
import random
import string
import os
import requests

API_BASE_URL = "https://kosrmwmkgbpwcmqsvffr.supabase.co/rest/v1/rpc/"
API_ENDPOINT = "_custom_property"

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="SetSnUuid")
def SetSnUuid(req: func.HttpRequest) -> func.HttpResponse:
  logging.debug('HTTP trigger function processed a request.')

  try:
      req_body = req.get_json()

      if not validate_event(req_body):
        logging.debug("Invalid event data.")
        return func.HttpResponse(
          "The event data has the wrong type or no custom properties.", 
          status_code=400
        )
      
      sn = req_body['data']['id']
      uuid = generate_random_string(12)
      
      if set_uuid(sn, uuid):
        return func.HttpResponse(
          f"Set UUID: {uuid} for SN: {sn}",
          status_code=200
        )
      else:
        return func.HttpResponse(
          f"Failed to set UUID: {uuid} for SN: {sn}",
          status_code=400
        )


  except ValueError as e:
    logging.debug("Invalid JSON request: {}", e)
    return func.HttpResponse(
      "An error occurred while parsing the request body.",
      status_code=400)


def generate_random_string(length):
  characters = string.ascii_letters + string.digits
  similar_chars = [('I', 'l', '1'), ('0', 'O'), ('5', 'S'), ('2', 'Z'), ('8', 'B')]

  while True:
    random_string = ''.join(random.choice(characters) for _ in range(length))
    if not any(all(char in random_string for char in group) for group in similar_chars):
      return random_string


def validate_event(event_body):
  if 'type' not in event_body or 'custom_properties' not in event_body['data']:
    return False
  
  event_type = event_body['type']
  custom_properties = event_body['data']['custom_properties']
  if 'insert' in event_type.lower() or 'update' in event_type.lower() and 'uuid' in custom_properties:
    return True
  return False


def set_uuid(sn, uuid):
  load_dotenv()
  api_key = os.getenv("API_KEY")
  bearer_token = os.getenv("BEARER_TOKEN")

  headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",
    "apikey": api_key
  }
  payload = {
    "tag_id": sn,
    "custom_tag_field": "uuid",
    "value": uuid
  }

  url = API_BASE_URL + "update" + API_ENDPOINT
  response = requests.post(url, headers=headers, json=payload)

  if 200 <= response.status_code < 300:
    logging.debug(f"UUID set successfully for id: {sn}")
    return True
  else:
    logging.debug(f"Failed to set UUID for id: {sn}. Error: {response.text}")
    return False