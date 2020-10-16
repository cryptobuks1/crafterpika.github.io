from upload_py import *
import os
import random
import shutil

try:
  os.mkdir("spam")
except:
  shutil.rmtree("spam")
  os.mkdir("spam")
  
try:
  os.remove("logs.txt")
except:
  pass
  

while True:
  arg1 = "test"
  arg2 = random.randint(0,2647647826487642784626427462786427864276478264287647826472846)
  
  with open(f"./spam/{arg1}-{arg2}.txt", "w") as f:
    f.write("testing stuff")
  
  star = starfiles()
  star.upload(f"{os.getcwd()}/spam/{arg1}-{arg2}.txt")
  print(star.url_file())
  
  f = open("logs.txt", "+a")
  f.write(f"{star.url_file()}\n")
  f.close()