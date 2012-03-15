#!/usr/bin/python
# -*- coding: utf-8 -*-
#by Joh Gerna thanks for help to john-dev
#updated by Mike Pissanos (gaVRoS) for SiriServerCore

import re,os

config_file="plugins.conf"
pluginPath="plugins"
from plugin import *
tline_answer_de = ''
tline_answer_en = ''

with open(config_file, "r") as fh:
    for line in fh:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        try:
            with open(pluginPath+"/"+line+"/__init__.py", "rU") as fd:
                for tline in fd:
                    tline=tline.strip()
                    if tline.startswith("@register(\"de-DE\", "):
                        tline = tline.replace('@register','').replace('(','').replace(')','').replace('\"','').replace('.','').replace('de-DE, ','').replace('[a-zA-Z0-9]+','').replace('\w','').replace('|',' oder ')
                        tline_answer_de = tline_answer_de +'\n' + "".join(tline)

                    elif tline.startswith("@register(\"en-US\", "):
                        tline = tline.replace('*','').replace('u','').replace('@register','').replace('(','').replace(')','').replace('\"','').replace('.','').replace('en-US, ','').replace('[a-zA-Z0-9]+','').replace('\w','').replace('|',' or ')
                        tline_answer_en = tline_answer_en + '\n' + "".join(tline)
        except:
            tline = "Plugin loading failed"

class help(Plugin):
    
    @register("de-DE", "(Hilfe)|(Befehle)")
    @register("en-US", u"(.*你會做什麼.*)|(.*你能做什麼.*)")
    def st_hello(self, speech, language):
        if language == 'de-DE':
            self.say("Das sind die Befehle die in Deiner Sprache verfügbar sind:")
            self.say("".join(tline_answer_de ),' ')
        else:
            self.say(u"以下是我能做的事情")
            EnabledCommnd = u"功能性項目：" + '\n' +\
                            u"今天星期幾" + '\n' +\
                            u"找附近的XX or 搜尋附近的XX" + '\n' +\
                            u"XX在哪裡 or XX怎麼走 or XX怎麼去" + '\n' +\
                            u"新增備忘錄" + '\n' +\
                            u"打給 or 撥給 or 電話給" + '\n' +\
                            u"現在幾點 or 的時間" + '\n' +\
                            u"今天天氣 or 天氣預報" + '\n' +\
                            u"我的位置 or 我在哪" + '\n' +\
                            u"網頁搜尋 or Google搜尋" + '\n' +\
                            '\n' +\
                            u"閒聊項目：" + '\n' +\
                            u"你會說中文嗎" + '\n' +\
                            u"吉米丘是誰" + '\n' +\
                            u"皮樂是誰" + '\n' +\
                            u"皮樂是男生 or 女生" + '\n' +\
                            u"你叫什麼名字" + '\n' +\
                            u"你好嗎" + '\n' +\
                            u"謝謝" + '\n' +\
                            u"嫁給我" + '\n' +\
                            u"說笑話" + '\n' +\
                            u"魔鏡誰美 or Siri誰美" + '\n' +\
                            u"穿什麼" + '\n' +\
                            u"生命終極意義" + '\n' +\
                            u"測試123" + '\n' +\
                            u"生日快樂" + '\n' +\
                            u"我很累" + '\n' +\
                            u"埋屍體" + '\n' +\
                            u"到底是什麼" + '\n' +\
                            u"誰深海鳳梨" + '\n' +\
                            u"喜歡顏色" + '\n' +\
                            u"越獄 or JB or jailbreak or Cydia" + '\n'
            self.say(EnabledCommnd,u"部分功能可能會暫時失效,請見諒")
        self.complete_request()