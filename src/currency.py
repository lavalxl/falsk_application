import requests
import src.config as conf


def currency_request(frm, t):
    frm = frm.upper()
    t = t.upper()
    currency_response = requests.get(conf.currency_url.format(frm + t + ',' + t + frm, conf.currency_api_key)).json()
    currency = {}
    if currency_response['status'] == 200:
        currency = {
            "from": frm,
            "to": t,
            "from_to": currency_response['data'][frm + t],
            "to_from": currency_response['data'][t + frm]
        }
    else:
        currency = {
            "from": frm,
            "to": t,
            "from_to": currency_response['message'],
            "to_from": currency_response['message']
        }

    return currency
