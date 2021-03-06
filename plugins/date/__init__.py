#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import date
import locale 
from plugin import *

class talkToMe(Plugin):  
        
    @register("en-GB", ".*Your.*Status.*")    
    @register("de-DE", ".*Dein.*Status.*")
    @register("en-US", ".*Your.*Status.*")
    @register("fr-FR", ".*Votre.*Statut.*")
    def ttm_uptime_status(self, speech, language):
        uptime = os.popen("uptime").read()
        if language == 'de-DE':
            self.say('Hier ist der Status:')
            self.say(uptime, ' ')
        elif language == 'fr-FR':
            self.say('Voici votre statut:')
            self.say(uptime, ' ')
        else:
            self.say('Here is the status:')
            self.say(uptime, ' ')
        self.complete_request()


    @register("de-DE", "(Welcher Tag.*)|(Welches Datum.*)")
    @register("en-GB", "(What Day.*)|(What.*Date.*)")
    @register("en-US", u".*今天星期.*")
    def ttm_say_date(self, speech, language):
        now = date.today()
        if language == 'de-DE':
            locale.setlocale(locale.LC_ALL, 'de_DE')
            result=now.strftime("Heute ist %A, der %d.%m.%Y (Kalenderwoche: %W)")
            self.say(result)
        elif language == 'en-US':
            locale.setlocale(locale.LC_ALL, "zh_TW")
            result=now.strftime("今天是 %Y 年 %m 月 %d . %A (第 %W 周)")
            self.say(unicode(result, "utf8"))
        else:
            locale.setlocale(locale.LC_ALL, 'en_US')
            result=now.strftime("Today is %A the %d.%m.%Y (Week: %W)")
            self.say(result)
        self.complete_request()
