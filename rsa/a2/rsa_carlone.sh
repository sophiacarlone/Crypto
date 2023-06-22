#!/bin/sh
rm message.txt
python3 reciever.py
sleep 2
python3 sender.py
sleep 2
python3 decrypt.py
