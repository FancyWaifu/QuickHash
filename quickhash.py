from bs4 import BeautifulSoup
import requests
import argparse
import os

parser = argparse.ArgumentParser(description='[*] Quick hash, This program uses the hashtoolkit.com database to return hashes')
parser.add_argument('-hv', help="Provide only a single hash")
parser.add_argument('-hl', help="Provide file location of hash(s)")
parser.add_argument('-w', help="Write discoverted hashes to a file, must provide a name for the file")
args = parser.parse_args()

#Creates user agent
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

if args.hl:
	try: 
		path_to_file = args.hl
		f = open(path_to_file, "r")
		for x in f:
			sha1 = x.split(":")
			r = requests.get("https://hashtoolkit.com/decrypt-hash/?hash=" + sha1[0], headers=headers).content
			soup = BeautifulSoup(r, 'html.parser')
			if soup.find_all('div', class_="alert alert-warning"):
				print("Could not find value: " + sha1[0])
			else:
				print(sha1[0] + ":" + soup.find_all('a')[10].get_text())
				if args.w:
					t = open(args.w, "a")
					t.write(sha1[0] + ":" + soup.find_all('a')[10].get_text() + "\n")
	except KeyboardInterrupt:
		f.close()
		if args.w:
			t.close()
		print("[*] Quit by user")

if args.hv:
	try:
		hash_value = args.hv
		sha1 = hash_value.split(":")
		r = requests.get("https://hashtoolkit.com/decrypt-hash/?hash=" + sha1[0], headers=headers).content
		soup = BeautifulSoup(r, 'html.parser')
		if soup.find_all('div', class_="alert alert-warning"):
			print("Could not find value: " + sha1[0])
		else:
			print(sha1[0] + ":" + soup.find_all('a')[10].get_text())
			if args.w:
				t = open(args.w, "a")
				t.write(sha1[0] + ":" + soup.find_all('a')[10].get_text() + "\n")
	except KeyboardInterrupt:
		f.close()
		if args.w:
			t.close()
		print("[*] Quit by user")