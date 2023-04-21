import hashlib 
import colorama
from hashlib import *
colorama.init(autoreset=True)
style = '''\033[31m
       *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******        
   **********         ************         **********
  ****************************************************
 ******************************************************   \033[31mHasing Tools
********************************************************   \033[35m @ZAkaria
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***
            **             *              **
'''
print(style)
print("============================================")
print("\033[31m1]-Hash chacker\n 2]-Hash length\n 3]-Hash type")
print("\033[31m4]-MD5 Encrypte\n""5]-MD5 Decrypte\033[31m")
print("============================================")
choose = input("Please choose option : ")
if choose == '1':
    print("This option For Hash chacker ")
    hash1=input("Enter Hash [1] :")
    hash2 = input("Enter Hash [2] :")
    if hash1 == hash2 :
        print('The Hash is clean')
    else :
        print("The Hash is virus ")
if choose == '2' :
    print("This option For Lenghth Hash")
    lenght = input("Enter your Hash : ")
    print("Length Hash is : " , len(lenght))
    # len for calc
    # md5 : 32 , sha1 : 40 , sha256 : 64
if choose == '3' :
    print("The is option For Know Hash type ") 
    hash = input("Enter the Hash : ")
    lenght = len(hash)
    if lenght == 32 :
        print('The hash is [MD5]')
        if lenght == 40 :
            print("The hash is [sha1]")
            if lenght ==  64     :
                print("The hash is [sha256]")
if choose  == '4' :
    print("This option For text to MD5 :")
    word = input("Enter your text : ")
    md5 = hashlib.md5(word.encode())
    print(md5.hexdigest())
if choose == '5' : 
    print("This option For decryption ")
    hash = input("Enter your Hash : ")
    file = input(" write file name : ")
    with open(file , mode ='r') as f :
        for line in f : 
            line = line.strip()
            if md5(line.enncode()).hexdigest() == hash :
                print("[-] Password Found : " +line )


