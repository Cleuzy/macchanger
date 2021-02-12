#-*- coding: UTF-8 -*-
import subprocess
import optparse
from random import randint
import random
def get_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface")
    #parse_object.add_option("-m", "--mac", dest="macadresi")
    return parse_object.parse_args()
def manuel_mac_changer(u_interface):
    u_mac_adress = input("Mac adresi giriniz: ")
    subprocess.call(["ifconfig", u_interface, "down"])
    subprocess.call(["ifconfig", u_interface, "hw", "ether", u_mac_adress])
    subprocess.call(["ifconfig", u_interface, "up"])
    print("Yeni Mac Adresiniz: "+u_mac_adress)
def random_mac_changer(u_interface):
    mac_list = list()
    list1 = list(range(10, 100, 2))
    mac1 = random.choice(list1)
    mac2 = random.choice(list1)
    mac_list.append(mac1)
    mac_list.append(mac2)
    x = 1
    while x < 5:
        y = randint(10, 100)
        mac_list.append(y)
        x += 1
        if (mac_list[0] % 2 == 0 and mac_list[1] % 2 == 0):
            random_mac = ':'.join(map(str, mac_list))
            subprocess.call(["ifconfig", u_interface, "down"])
            subprocess.call(["ifconfig", u_interface, "hw", "ether", random_mac])
            subprocess.call(["ifconfig", u_interface, "up"])
            print("new mac adress: " + random_mac)
        else:
            print("Interface is could not set")
(user_input,args) = get_inputs()
while True:
    print("1- Manuel Mac Changer")
    print("2- Random Mac Changer")
    operation = input("Select a operation: ")
    try:
        operation = int(operation)
    except:
        print("WRONG: Only enter 1 or 2")
    else:
        if(operation == 1):
            manuel_mac_changer(user_input.interface)
            break
        elif(operation == 2):
            random_mac_changer(user_input.interface)
            break
        else:
            print("WRONG: Only enter 1 or 2")
