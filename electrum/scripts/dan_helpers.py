import requests
import json


def get_address_from_domain(domain):
    try:
        if '.' not in domain:
            url = 'http://app.domx.io/api/Identity?identity={}'.format(domain)
            response = requests.get(url)
            response_str = response.content.decode('utf-8')
            response_obj = json.loads(response_str)
            addresses = response_obj['BtcAddresses']
        else:
            if '@' in domain:
                # Add support for email
                pass

            else:
                url = 'http://app.domx.io/api/Domain?domainName={}'.format(domain)
                response = requests.get(url)
                response_str = response.content.decode('utf-8')
                response_obj = json.loads(response_str)
                if response_obj['owner'] == '0x0000000000000000000000000000000000000000':
                    raise Exception
                addresses = [response_obj['owner']]


    except Exception as e:
        addresses = []

    return addresses