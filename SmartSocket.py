from PyP100 import PyP100

# 啟動或關閉智能插座 
# ip 要用中華電信全屋通查
def SetP100(isOn):
    p100 = PyP100.P100("192.168.1.102", "yourMail@gmail.com", "yourPassword") #Creates a P100 plug object
    p100.handshake()
    p100.login()

    if isOn == True:
        p100.turnOn() #Turns the connected plug on
    else:
        p100.turnOff() #Turns the connected plug off
    