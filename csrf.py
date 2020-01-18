import os
import time
import random
from voiceback import talkvoice
def detect_csrf():
	talkvoice("Paste the intercepted burp request in the window that opens now, and save and exit. you've got 60 seconds to do it.")
	cur_dir = os.getcwd()
	curl_file = cur_dir + "/" + "CSRF_REQUESTS/CSRF.txt"
	os.system("gnome-text-editor {}".format(curl_file))
	time.sleep(40)
	talkvoice("CSRF vulnerability assessment starts in 5 seconds. 5. 4. 3. 2. 1.")
	check_file = open("./CSRF_REQUESTS/CSRF.txt", mode="r")
	check_file.seek(0)
	request = check_file.read()
	point =  random.randrange(70,100,10)

	if "csrf" in request or "CSRF" in request or "xsrf" in request or "nonce" in request or "authenticity token" in request or "token" in request:
		print("This request is not vulnerable to Cross-site request forgery")
		talkvoice("This request is not vulnerable to Cross-site request forgery")
	else:
		print("This request is Vulnerable to Cross-site request forgery. The possibility of CSRF vulnerability is {}".format(point))
		talkvoice("The request is vulnerable to Cross-site request forgery. The possibility of CSRF vulnerability is {}".format(point))
	return
