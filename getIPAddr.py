import network
import os
import ubinascii

def healthCheck():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.active():
        if sta_if.isconnected():
            ipAddr = sta_if.ifconfig()
            mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
        else:
            print("ESP8266 is not connected.")
    else:
        print("Activate the ESP8266 STA Mode.")
    return(mac, ipAddr[0])


if __name__ == "__main__":
    print(healthCheck())
    
