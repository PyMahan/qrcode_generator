#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 00:43:54 2023

@author: amir
"""
from qrcode_generator import get_string,create_qrcode,save_qrcode
import time
import os


class Handler:

    def get_string_2():
        text = input(str("ENTER THE STRING FOR CONVERT TO THE QRCODE (PRESS ESC AND ENTER TO EXIT) :"))
        return text

    
    @staticmethod
    def run(get=get_string):
        name = get()
        qr = create_qrcode(string=name)
        try:
            os.mkdir("Saved")
        except:
            pass
        try:
            save_qrcode(filename=f"Saved/{name[0:20]}",qrcode=qr)
        except:
            save_qrcode(filename="Default",qrcode=qr)
            
        finalTxt = "QRCode created!"
        print("\n".center(55," "),end="",flush=True)
        for char in finalTxt:
            print(char,end="",flush=True)
            time.sleep(0.05)
        print("\n")
        Handler.retry()
    def retry():
        Handler.run(Handler.get_string_2)



            
if __name__ == "__main__":
    Handler.run()
    

