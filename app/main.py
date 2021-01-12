from flask import Flask
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from base64 import b64encode
import time
app = Flask(__name__)
key = RSA.generate(1024)

@app.route("/")
def hello():
	current_time = time.strftime("%H:%M:%S")
	return "Hello World from Flask - %s" % current_time

@app.route("/sign/<message>")
def sign(message):
	digest = SHA256.new()
	digest.update(message.encode('utf-8'))
	signer = PKCS1_v1_5.new(key)
	sig = signer.sign(digest)
	encoded = b64encode(sig)
	return "Signature %s" % encoded

@app.route("/hi/<username>")
def hi(username):
	return "Hi {}".format(escape(username))

@app.route("/foo")
def foo():
	return "FOO!"

if __name__ == "__main__":
	# Only for debugging while developing
	app.run(host='0.0.0.0', debug=True, port=80)
