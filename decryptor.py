import os, re

os.system("apktool d decryptor.apk -o decryptor")

try:
	os.mkdir("decryptor/res/drawable/")
except:
	pass
input("Please place encrypted bmp in decryptor/res/drawable/ and then press enter to continue")

os.system("apktool b decryptor -o decryptor.new.apk")
os.system("apktool d decryptor.new.apk -o decryptor -f")

draws = ""
o = open("decryptor/res/values/public.xml").read()
for line in o.split("\n"):
	d = re.match(r'(.*?)<public type="drawable" name="(.*?)" id="(.*?)" \/>', line)
	if d:
		draws += ".field public static final {}:I = {}\n".format(d.group(2), d.group(3))

smali = open("decryptor/smali/com/convert/spr/R$drawable.smali").read()
smali = smali.replace("name = \"drawable\"\n.end annotation", "name = \"drawable\"\n.end annotation\n\n" + "# static fields\n" + draws)

os.system("apktool b decryptor -o decryptor.new.apk")

print("Everything is done!")