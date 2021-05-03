import hashlib, os, time
os.system("color 0c")
flag = 0
pass_hash = input("Enter MD5 hash: ")
wordlist = input("Enter wordlist file: ")
try:
	pass_file = open (wordlist, "r")
except:
	print("File not found")
	time.sleep(2)
	exit()
for word in pass_file:
	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	if digest == pass_hash:
		print("Password found")
		print("Password is: " + word)
		flag = 1
		break
if flag == 0:
	print("Password wasn't found")
	time.sleep(2)
	exit()
input()