"""
MIT License
Copyright (c) 2022 TecnoPlayZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
'''
~ TecnoPlayZ#1337
~ https://discord.gg/codez
'''
import discord
import asyncio
import requests
import threading
import sys
import os
from typing import Optional
from colorama import Fore
import time

def Clear():
  if sys.platform in ["linux", "linux2"]:
    os.system("clear")
  else:
    os.system("cls")

Clear()

def setTitle(title: Optional[any]=None):
  os.system(f"title {title}")

setTitle("Multiple Token Hoster - [TecnoPlayZ#1337]")

session = requests.Session()
tokens = []
with open("tokens.txt", "r") as f:
  tokens_ = f.read().split("\n")

if len(tokens_) == 0:
  print("TecnoPlayZ#1337 | There Are No Tokens, Please Add Some Tokens To Host In tokens.txt File.")
  exit()

def Check_Token(Token):
  response = requests.get(f"https://discord.com/api/v9/users/@me", headers={"Authorization": Token})
  if response.status_code in [204, 200, 201]:
    print(f"TecnoPlayZ#1337 | {Token} Is Valid.")
    tokens.append(Token)
  if "need to verify" in response.text:
    print(f"TecnoPlayZ#1337 | {Token} Is On Verification.")
  elif response.status_code in [404, 401, 400]:
    print(f"TecnoPlayZ#1337 | {Token} Invalid Token Or Rate Limited.")

for tk in tokens_:
  Check_Token(tk)


if len(tokens) == 0:
  print("TecnoPlayZ#1337 | All Tokens Were Invalid, Try Again Later With Working Tokens.")
  exit()

time.sleep(2)
Clear()
menu = f"""{Fore.RED}[-]{Fore.RESET} Created by TecnoPlayZ#1337\n"""

print(menu)

#st = input('TecnoPlayZ#1337 | Accounts Status Idle, Dnd, Online, Mobile: ')
st = "Idle"
akks = []
stl = st.lower()
if stl == "dnd":
  status = discord.Status.dnd
elif stl == "idle":
  status = discord.Status.idle
elif stl == "online":
  status = discord.Status.online
#ty = input("TecnoPlayZ#1337 | Activity Type Playing, Streaming, Listening, Watching: ")
ty = "Streaming"
name = "TecnoPlayZ On Top"
tyy = ty.lower()
if tyy == "streaming":
 # name = input("TecnoPlayZ#1337 | Streaming Name: ")
  acttt = discord.Streaming(name=name, url="https:/twitch/TecnoPlayZ")
elif tyy == "playing":
  #name = input("TecnoPlayZ#1337 | Playing Name: ")
  acttt = discord.Game(name=name)
elif tyy == "listening":
#  name = input("TecnoPlayZ#1337 | Listening Name: ")
  acttt=discord.Activity(type=discord.ActivityType.listening, name=name)
elif tyy == "watching":
 # name = input("TecnoPlayZ#1337 | Watching Name: ")
  acttt=discord.Activity(type=discord.ActivityType.watching, name=name)
loop = asyncio.get_event_loop()
for tk in tokens:
  client = discord.Client(status=status, activity=acttt)
  loop.create_task(client.start(tk, bot=False))
  akks.append(client)
  print(" ")
  print("TecnoPlayZ#1337 | {} Is Hosted.\n".format(tk))

threading.Thread(target=loop.run_forever).start()

while True:
  idk = 0
  idk += 1
