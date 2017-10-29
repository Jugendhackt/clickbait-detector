import requests
import urllib
import json

def mc_request(txt):

	url = "https://api.meaningcloud.com/class-1.1"
	#add api key and model name below
	payload = "key=<YOUR-API_KEY>&txt="+urllib.quote(txt)+"&model=<YOUR-MODEL-NAME>"
	headers = {'content-type': 'application/x-www-form-urlencoded'}

	response = requests.request("POST", url, data=payload, headers=headers)

	data = json.loads(response.text)
	if not data['category_list']:
		return False
	else:
		return True
	# print(data['category_list'])
	# print(data)
	# return response.text


if __name__ ==  '__main__':
	# print(mc_request("nothing"))
	print(mc_request("extreme prank"))
