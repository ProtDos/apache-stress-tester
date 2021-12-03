import sys
import platform
import subprocess

if sys.platform() != "linux":
  print("[-] You need a linux system")
  exit()
else:
  continue
  
site = input("Enter the site you want to test: ")
if not site.startswith("http"):
  print("[-] Site has to start with 'http://' or 'https://'")
  exit()
else:
  continue
out = subprocess.check_output(["ab"], ["-n"], ["1000"], ["-c"], ["10"], ["-k"], ["-H"], ['"Accept-Encoding: gzip, deflate"'], [site])
try
  splitted1 = out.split("Requests per second:    ")
except Exception as e:
  print(f"[-] Unknown error: {e}")
  exit()
splitted2 = splitted1.split(" [#/sec]")
print(f"The site can handle: {splitted1} users per second.")


