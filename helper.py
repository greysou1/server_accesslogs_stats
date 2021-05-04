import requests
import json
import ipinfo
import os 
# User Agent API info
# https://accounts.whatismybrowser.com
api_key = os.environ.get('USR_AGNT_API_KEY')
api_url = "https://api.whatismybrowser.com/api/v2/user_agent_parse"
# -- Set up HTTP Headers
headers = {
    'X-API-KEY': api_key,
}

# IP Address API info
# https://github.com/ipinfo/python
IP_access_token = os.environ.get('IP_INFO_API_KEY')

def parse_useragent(user_agent):
    # -- prepare data for the API request
    # This shows the `parse_options` key with some options you can choose to enable if you want
    # https://developers.whatismybrowser.com/api/docs/v2/integration-guide/#user-agent-parse-parse-options
    post_data = {
        'user_agent': user_agent,
        "parse_options": {
            #"allow_servers_to_impersonate_devices": True,
            #"return_metadata_for_useragent": True,
            #"dont_sanitize": True,
        },
    }

    # -- Make the request
    result = requests.post(api_url, data=json.dumps(post_data), headers=headers)


    # -- Try to decode the api response as json
    result_json = {}
    try:
        result_json = result.json()
    except Exception as e:
        print(result.text)
        print("Couldn't decode the response as JSON:", e)
        exit()


    # -- Check that the server responded with a "200/Success" code
    if result.status_code != 200:
        print("ERROR: not a 200 result. instead got: %s." % result.status_code)
        print(json.dumps(result_json, indent=2))
        exit()


    # -- Check the API request was successful
    if result_json.get('result', {}).get('code') != "success":
        print("The API did not return a 'success' response. It said: result code: %s, message_code: %s, message: %s" % (result_json.get('result', {}).get('code'), result_json.get('result', {}).get('message_code'), result_json.get('result', {}).get('message')))
        #print(json.dumps(result_json, indent=2))
        exit()

    # Now you have "result_json" and can store, display or process any part of the response.

    # -- print the entire json dump for reference
    return (result_json["parse"])

def get_IP_details(ip_address):
    handler = ipinfo.getHandler(IP_access_token)
    details = handler.getDetails(ip_address)

    return details.all
