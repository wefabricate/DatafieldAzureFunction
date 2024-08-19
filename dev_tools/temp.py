from dotenv import load_dotenv

import os
import requests

def create_custom_property(sn, field_name, field_value):
  load_dotenv()

  API_ENDPOINT = "https://kosrmwmkgbpwcmqsvffr.supabase.co/rest/v1/rpc/update_custom_property"
  api_key = os.getenv("API_KEY")
  bearer_token = os.getenv("BEARER_TOKEN")

  headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",
    "apikey": api_key
  }
  payload = {
    "tag_id": sn,
    "custom_tag_field": field_name,
    "value": field_value
  }

  response = requests.post(API_ENDPOINT, headers=headers, json=payload)

  if 200 <= response.status_code < 300:
    print(f"Custom property set successfully for id: {sn}")
    return True
  else:
    print(f"Failed to create custom property for id: {sn}. Error: {response}")
    return False

def delete_custom_property(sn, field_name):
  load_dotenv()

  API_ENDPOINT = "https://kosrmwmkgbpwcmqsvffr.supabase.co/rest/v1/rpc/delete_custom_property"
  api_key = os.getenv("API_KEY")
  bearer_token = os.getenv("BEARER_TOKEN")

  headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",
    "apikey": api_key
  }
  payload = {
    "tag_id": sn,
    "custom_tag_field": field_name
  }

  response = requests.post(API_ENDPOINT, headers=headers, json=payload)

  if 200 <= response.status_code < 300:
    print(f"Custom property deleted successfully for id: {sn}")
    return True
  else:
    print(f"Failed to delete custom property for id: {sn}. Error: {response}")
    return False

delete_custom_property("SN97WMNMX7", "test")
