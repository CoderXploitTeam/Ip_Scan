#!/usr/bin/python
# coding: UTF-8
# Coded by Tegar ID
# 8 november 2020
# 08:00 pm - 08:30 pm
# dunia kode all right reverse

import requests, time, sys, json, os
os.system('clear')
def login():
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + Token
    }
    user = requests.get('https://afara.my.id/api/user', headers = headers).json()
    return user

def main():
    user = login()

    if 'message'in user:
        print('\033[37;1mInvalid API token, get API token at "https://afara.my.id"')
    else:
        print('Name:', user['data']['name'])
        print('Email:', user['data']['email'])
        ipgeolocation()

def ipgeolocation():
    ipaddress = input('\033[31;1mMasukan IP Address \033[37;1m: ')

    res = requests.get('https://afara.my.id/api/ip-geolocation', data = '{"ipaddress": "'+ ipaddress +'"}', headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + Token
    }).json()

    if 'error' in res:
        print(res['error'])
        x = input('\033[37;1m[\033[43;1mEnter To Try again\033[00;1m]')
        if x == '':
            main()
        else:
            main()
    else:
        print('')
        print('\033[31;1mIP\033[37;1m:', res['query'])
        print('\033[31;1mSTATUS\033[37;1m:', res['status'])
        print('\033[31;1mNEGARA\033[37;1m:', res['country'])
        print('\033[31;1mPROVINSI\033[37;1m:', res['regionName'])
        print('\033[31;1mKOTA\033[37;1m:', res['city'])
        print('\033[31;1mISP\033[37;1m:', res['isp'])
        print('\033[31;1mZIPCODE\033[37;1m:', res['zip'])
        print('\033[31;1mTIMEZONE\033[37;1m:', res['timezone'])
        print('')

    x = input('\033[37;1m[\033[41;1m1.Exit, 2.Try again\033[00;1m] \033[37;1m: ')
    if x == '1':
        sys.exit()
    elif x == '2':
        ipgeolocation()
    else:
        sys.exit()

print('\033[37;1m[\033[41;1mTools Lacak Lokasi\033[00;1m\033[37;1m]')
print('\033[37;1m[\033[44;1mAUTHOR : TEGAR ID\033[00;1m\033[37;1m]')
print('\033[37;1m[\033[43;1mTEAM : DUNIA KODE\033[00;1m\033[37;1m]')
print('\033[31;1mApakah Sudah Memiliki token?')
print('1.Sudah\n2.Belum')
pilih = input('>> \033[37;1m')
if pilih == "1":
    Token = input('\033[31;1mMASUKAN TOKEN \033[37;1m: ')
    main()
elif pilih == "2":
    print('dapatkan token di https://afara.my.id/login\nDengan cara loginkan dulu email anda')
    buka = input('Enter Untuk Membuka Browser\n')
    os.system("xdg-open 'https://afara.my.id/login'")
    Token = input('\033[31;1mMASUKAN TOKEN \033[37;1m: ')
    main()
