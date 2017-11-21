# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re
import requests,urllib3,json
from bs4 import BeautifulSoup
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token='EndslhIKR5Gzdnn05Vg4.DHXpkDdyaO/DtIfPmUBera.qFkxxeDifN5W9sZt5vJK3yOGPmhnK3VSuyJZUn47o/k=')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token='EmooosfCHbWVFR4tlxfc.VtgXGjIJDrrBFO4BZvLaFa.JOL+4INUUuxq0j/tQ2SYCu3KFG66AkAHdqMgpIARjW0=')
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token='Eme9w0KFycduOlG1qMR9.CRhlPdHdLTQp5g3uSWl2Uq.9VSeEy3NS71iOX3tM9HPJje/zTXryV5pDgYfEHdNwmI=')
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token='EmMmLEHvtfcpeiGN1vy9.uULGkUIl0ONt8zYQL4u2Qq.IRUVEaGpIEQTLCCAs9N75DnmqNxJyt8/E4x83SQdo58=')
kc.loginResult()

kg = LINETCR.LINE()
kg.login(token='Em1eycm35u2jPjPA60Ne.1rFEk2BZ1o9wIMGV4VJ8RG.hQ5HeiDH3WovBvFOh1l7z02AgX63woKfyJkXiWMfL50=')
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token='Em7nF3cRsFCbdT4fNZP9.kCQ9e+EiEyuTdBPhDocscq.Gj3kv4liyMveN0gXjFJCXfti6IdNkDHX0jVMiy5Auzo=')
kh.loginResult()

ka = LINETCR.LINE()
ka.login(token='EmOAwd5muMSCFH956SX4.F1GZEmdX2M9RevMY8lqlXa.mpC27BTI1esV7vfuSqpC2oI3bEe9VmDVqVyAKIGL274=')
ka.loginResult()

kb = LINETCR.LINE()
kb.login(token='Emit4q5Q4MyD4EvU3eXb.I7sddP8milAoqDcuA7OXcW.kobBI5aSpOizpFbfm3Yg4uzTApFJYnFP4ZnjWGFXs3M=')
kb.loginResult()

kd = LINETCR.LINE()
kd.login(token='EmUyMp8wVYQAWy39wv88.7SeUasXJX0AnRykeg9Tica.5nZAOAss5DQCchHk158S4GtJSd0fqHBFlBLjTsVe4mA=')
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token='EmMhBz1J76qhzjiEFqKb.VW5GlhMJ47jM9VAkC5by6W.6skCXbOOgzY31+9s9kBetuL/HcTefCC0tfH0i2ZbezI=')
ke.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" Command Selfbot Rayhan✍Ŧ€₳M ж Ħ₳₵₭฿❂Ŧ✈
✍[Id︎]
✍[Mid]
✍[Me︎]
✍[TL︎:「Text」]
✍[Mc 「mid」]
✍[K on/off]
✍[Join︎ on/off]
✍[Gcancel:︎「Number of people」]
✍[Group cancelalll︎]
✍[Leave︎ on/off]
✍[Add on/off]
✍[Share on/off]
✍[Message change:「text」]
✍[Message check]
✍[Confirm]
✍[Jam on/off]
✍[Change clock:「name」]
✍[Up]Memperbaharui Jam
✍[Han join 「Han1-9」]
✍[Han bye 「Han1-9」]
✍[Han:version]
✍[Han:creator]

[*] Command in the groups [*]

🗡[Curl]Menutup Url Grup
🗡[Ourl]Membuka Url Grup
🗡[url]Url Grup
🗡[url:「Group ID」]
🗡[Invite：「mid」]
🗡[Kick：「mid」]
🗡[Ginfo]Info Grup
🗡[jointicket]
🗡[Cancel]Membatalkan undangan grup
🗡[Gn 「group name」]
🗡[Nk 「name」]
🗡[Tag]
🗡[Setlastpoint]
🗡[Viewlastseen]
🗡[Han:groupcreator]

[*] Command kicker only [*]

🔫[Copy 「@」] By Tag
🔫[Backup]
🔫[Han]
🔫[Han:bye]
🔫[Mid 「@」] By Tag
🔫[Bye 「@」] By Tag
🔫[Bye]
🔫[Kill ban]Kick user yang ada dalam daftar Ban
🔫[Kill 「@」]
🔫[Ban 「@」] By Tag
🔫[Unban 「@」] By Tag
🔫[Ban︎] Share Contact
🔫[Unban︎] Share Contact
🔫[Banlist︎]Cek Daftar Ban
🔫[Cleanse]
🔫[Cek ban]
🔫[Han mid]
🔫[Han ︎invite:「mid」]
🔫[Han ︎rename:「name」]
🔫[Han ︎gift]
🔫[Hallo Han]
🔫[Bot cancel]
🔫[Title:]

[*] Command Protect [*]

🚀[Protect kick on]
🚀[Protect kick off]
🚀[Set:blockinvite:on]
🚀[Set:blockinvite:off]
🚀[Protect qr on]
🚀[Protect qr off]
🚀[Protect cancel on]
🚀[Protect cancel off]

Created By Rayhan
✍Ŧ€₳M ж Ħ₳₵₭฿❂Ŧ✈
"""
helpsMessage =""" Command Bot++
✈[Setlastpoint]
✈[Viewlastseen]
✈[Clear]
✈[Clearall]
✈[Cancel on/off]
✈[Kick on/off]
✈[Cancel]
✈[Kickall]
✈[Speed+]
✈[Buka]
✈[Tutup]
✈[Join]
✈[Ip]

Created By ✍Ŧ€₳M ж Ħ₳₵₭฿❂Ŧ✈
"""
KAC=[cl,ki,kk,kc,kg,kh,ka,kb,kd,ke]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kh.getProfile().mid
Emid = kg.getProfile().mid
Fmid = ka.getProfile().mid
Gmid = kb.getProfile().mid
Hmid = kd.getProfile().mid
Imid = ke.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
admin=["u761c4f29d0d8028f9d4e216932e6c444"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Nah Lho Ketauan Ngeadd :p",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"x‮nahyaR.",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectKick":False,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":False,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def CloneContactProfile(self, mid):
  contact = self.getContact(mid)
  profile = self.getProfile()
  profile.displayName = contact.displayName
  profile.statusMessage = contact.pictureStatus
  self.updateProfilePicture(profile.pictureStatus)
  return self.updateProfile(profile)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if op.param2 not in Bots:
                return
            ki.sendText(op.param1,cl.getContact(op.param2).displayName + "Please don't open qr")
            print "Update group"

        #------Open QR Kick start------#
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
                    if op.param2 in mid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)

                if op.param3 in Emid:
                    if op.param2 in mid:
                        X = ka.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)

                if op.param3 in Fmid:
                    if op.param2 in mid:
                        X = kb.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)

                if op.param3 in Gmid:
                    if op.param2 in mid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)

                if op.param3 in Hmid:
                    if op.param2 in mid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)

                if op.param3 in Imid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 15:
            if op.param2 in Bots:
                return
            ki.sendText(op.param1,cl.getContact(op.param2).displayName + " Good Bye\n(´･ω･`)")
            print "MEMBER OUT GROUP"

        if op.type == 17:
            if op.param2 in Bots:
                return
            ginfo = cl.getGroup(op.param1)
            ki.sendText(op.param1,cl.getContact(op.param2).displayName + " Welcome\n(´･ω･`)")
            ki.sendText(op.param1, "Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
            print "MEMBER HAS JOIN THE GROUP"

        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("·",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
            if wait["ProtectKick"] == True:
                if op.param2 not in admin:
                    random.choice(KAC).kickoutFromGroup(op.param2)
                    random.choice(KAC).findAndAddFriendbyMid(op.param3)
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                else:
                    pass

        if op.type == 19:
                if op.param3 in admin:
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kh.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kh.updateGroup(G)
                    Ticket = kh.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kg.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kg.updateGroup(G)
                    Ticket = kg.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kd.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kd.updateGroup(G)
                    Ticket = kd.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u761c4f29d0d8028f9d4e216932e6c444":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")

        #------Cancel User Kick start------#
        if op.type == 32:
            if wait["Protectcancel"] == True:
              if op.param2 not in admin:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","command","Command","cmd"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,helpMessage)
                        cl.sendText(msg.to,helpsMessage)
                    else:
                        cl.sendText(msg.to,helpt)
                        cl.sendText(msg.to,helpst)
            elif ("Gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Han1 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Han1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Han2 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Han2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Han3 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Han3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.kickoutFromGroup(msg.to,[midd])
            elif "Han1 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han1 kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Han2 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han2 kick ","")
                    kk.kickoutFromGroup(msg.to,[midd])
            elif "Han3 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han3 kick ","")
                    kc.kickoutFromGroup(msg.to,[midd])
            elif "Han4 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han4 kick ","")
                    kh.kickoutFromGroup(msg.to,[midd])
            elif "Han5 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han5 kick ","")
                    kg.kickoutFromGroup(msg.to,[midd])
            elif "Han6 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han6 kick ","")
                    ka.kickoutFromGroup(msg.to,[midd])
            elif "Han7 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han7 kick ","")
                    kb.kickoutFromGroup(msg.to,[midd])
            elif "Han8 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han8 kick ","")
                    kd.kickoutFromGroup(msg.to,[midd])
            elif "Han9 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han9 kick ","")
                    ke.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Invite ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
            elif "Han1 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han1 invite ","")
                    ki.findAndAddContactsByMid(midd)
                    ki.inviteIntoGroup(msg.to,[midd])
            elif "Han2 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han2 invite ","")
                    kk.findAndAddContactsByMid(midd)
                    kk.inviteIntoGroup(msg.to,[midd])
            elif "Han3 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han3 invite ","")
                    kc.findAndAddContactsByMid(midd)
                    kc.inviteIntoGroup(msg.to,[midd])
            elif "Han4 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han4 invite ","")
                    kh.findAndAddContactsByMid(midd)
                    kh.inviteIntoGroup(msg.to,[midd])
            elif "Han5 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han5 invite ","")
                    kg.findAndAddContactsByMid(midd)
                    kg.inviteIntoGroup(msg.to,[midd])
            elif "Han6 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han6 invite ","")
                    ka.findAndAddContactsByMid(midd)
                    ka.inviteIntoGroup(msg.to,[midd])
            elif "Han7 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han7 invite ","")
                    kb.findAndAddContactsByMid(midd)
                    kb.inviteIntoGroup(msg.to,[midd])
            elif "Han8 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han8 invite ","")
                    kd.findAndAddContactsByMid(midd)
                    kd.inviteIntoGroup(msg.to,[midd])
            elif "Han9 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Han9 invite ","")
                    ke.findAndAddContactsByMid(midd)
                    ke.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
            elif msg.text in ["Han1"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Amid}
                    ki.sendMessage(msg)
            elif msg.text in ["Han2"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Bmid}
                    kk.sendMessage(msg)
            elif msg.text in ["Han3"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Cmid}
                    kc.sendMessage(msg)
            elif msg.text in ["Han4"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Dmid}
                    kh.sendMessage(msg)
            elif msg.text in ["Han5"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Emid}
                    kg.sendMessage(msg)
            elif msg.text in ["Han6"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Fmid}
                    ka.sendMessage(msg)
            elif msg.text in ["Han7"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Gmid}
                    kb.sendMessage(msg)
            elif msg.text in ["Han8"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Hmid}
                    kd.sendMessage(msg)
            elif msg.text in ["Han9"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Imid}
                    ke.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift","Nih"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han1 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han2 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han3 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '10'}
                    msg.text = None
                    kc.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han4 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    kh.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han5 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    kg.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han6 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    ka.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han7 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '10'}
                    msg.text = None
                    kb.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han8 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    kd.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han9 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    ke.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '12'}
                    msg.text = None
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
                    kc.sendMessage(msg)
                    kh.sendMessage(msg)
                    kg.sendMessage(msg)
                    ka.sendMessage(msg)
                    kb.sendMessage(msg)
                    kd.sendMessage(msg)
                    ke.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han cancel","Bot cancel"]:
                if msg.from_ in admin:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han1 ourl","Han1 link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Han")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han2 ourl","Han2 link on"]:
                if msg.from_ in admin:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Han")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han3 ourl","Han3 link on"]:
                if msg.from_ in admin:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Han")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han1 curl","Han1 link off"]:
                if msg.from_ in admin:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Han")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han2 curl","Han2 link off"]:
                if msg.from_ in admin:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Han")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han3 curl","Han3 link off"]:
                if msg.from_ in admin:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Han")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,mid)
                    ki.sendText(msg.to,Amid)
                    kk.sendText(msg.to,Bmid)
                    kc.sendText(msg.to,Cmid)
                    kh.sendText(msg.to,Dmid)
                    kg.sendText(msg.to,Emid)
                    ka.sendText(msg.to,Fmid)
                    kb.sendText(msg.to,Gmid)
                    kd.sendText(msg.to,Hmid)
                    ke.sendText(msg.to,Imid)
            elif "Mid" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,mid)
            elif "Han1 mid" == msg.text:
                if msg.from_ in admin:
                    ki.sendText(msg.to,Amid)
            elif "Han2 mid" == msg.text:
                if msg.from_ in admin:
                    kk.sendText(msg.to,Bmid)
            elif "Han3 mid" == msg.text:
                if msg.from_ in admin:
                    kc.sendText(msg.to,Cmid)
            elif "Han4 mid" == msg.text:
                if msg.from_ in admin:
                    kh.sendText(msg.to,Dmid)
            elif "Han5 mid" == msg.text:
                if msg.from_ in admin:
                    kg.sendText(msg.to,Emid)
            elif "Han6 mid" == msg.text:
                if msg.from_ in admin:
                    ka.sendText(msg.to,Fmid)
            elif "Han7 mid" == msg.text:
                if msg.from_ in admin:
                    kb.sendText(msg.to,Gmid)
            elif "Han8 mid" == msg.text:
                if msg.from_ in admin:
                    kd.sendText(msg.to,Hmid)
            elif "Han9 mid" == msg.text:
                if msg.from_ in admin:
                    ke.sendText(msg.to,Imid)
            elif msg.text in ["Wkwk"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "100",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "10",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "9",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["You"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "7",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "6",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "4",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "3",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "110",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "101",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "247",
                                         "STKPKGID": "3",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["TL:"]:
                if msg.from_ in admin:
                    tl_text = msg.text.replace("TL:","")
                    cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                if msg.from_ in admin:
                    string = msg.text.replace("Cn ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Han1 rename "]:
                if msg.from_ in admin:
                    string = msg.text.replace("Han1 rename ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile_B = ki.getProfile()
                        profile_B.displayName = string
                        ki.updateProfile(profile_B)
                        ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Han2 rename "]:
                if msg.from_ in admin:
                    string = msg.text.replace("Han2 rename ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile_B = kk.getProfile()
                        profile_B.displayName = string
                        kk.updateProfile(profile_B)
                        kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                if msg.from_ in admin:
                    mmid = msg.text.replace("Mc ","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":mmid}
                    cl.sendMessage(msg)
            elif msg.text in ["Set:blockinvite:on","set:blockinvite:on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite On")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite On")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Set:blockinvite:off","set:blockinvite:off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Protect qr on","protect qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["ProtectQR"] == True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Protect qr off","protect  qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["ProtectQR"] == False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Protect cancel on","protect cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"Sudah On")
                else:
                    wait["Protectcancel"] == True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"Sudah On")
            elif msg.text in ["Protect cancel off","protect cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"Sudah Off")
                else:
                    wait["Protectcancel"] == False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"Sudah Off")
            elif msg.text in ["Protect kick on","protect kick on"]:
              if msg.from_ in admin:
                if wait["ProtectKick"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectKick"] == True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect kick off","protect kick off"]:
                if msg.from_ in admin:
                  if wait["ProtectKick"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already on")
                      else:
                          cl.sendText(msg.to,"done")
                  else:
                      wait["ProtectKick"] == False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already on")
                      else:
                          cl.sendText(msg.to,"done")
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to, "Backup Succes")
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if msg.from_ in admin:
                  if wait["contact"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already on")
                      else:
                          cl.sendText(msg.to,"done")
                  else:
                      wait["contact"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already on")
                      else:
                          cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if msg.from_ in admin:
                  if wait["contact"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already off")
                      else:
                          cl.sendText(msg.to,"done ")
                  else:
                      wait["contact"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already off")
                      else:
                          cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if msg.from_ in admin:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if msg.from_ in admin:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set:check"]:
                if msg.from_ in admin:
                    md = ""
                    if wait["ProtectKick"] == True: md+=" Protect Kick : on\n"
                    else: md+=" Protect Kick : off\n"
                    if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                    else: md+=" Protect Cancel : off\n"
                    if wait["ProtectQR"] == True: md+=" Protect Qr : on\n"
                    else: md+=" Protect Qr : off\n"
                    if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                    else: md+=" Block Invite : off\n"
                    if wait["contact"] == True: md+=" Contact : on\n"
                    else: md+=" Contact : off\n"
                    if wait["autoJoin"] == True: md+=" Auto join : on\n"
                    else: md +=" Auto join : off\n"
                    if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                    else: md+= " Group cancel : off\n"
                    if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                    else: md+=" Auto leave : off\n"
                    if wait["timeline"] == True: md+=" Share : on\n"
                    else:md+=" Share : off\n"
                    if wait["autoAdd"] == True: md+=" Auto add : on\n"
                    else:md+=" Auto add : off\n"
                    if wait["commentOn"] == True: md+=" Comment : on\n"
                    else:md+=" Comment : off\n"
                    cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("album ","")
                    album = cl.getAlbum(gid)
                    if album["result"]["items"] == []:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"There is no album")
                        else:
                            cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                    else:
                        if wait["lang"] == "JP":
                            mg = "The following is the target album"
                        else:
                            mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                        for y in album["result"]["items"]:
                            if "photoCount" in y:
                                mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                            else:
                                mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("album remove ","")
                    albums = cl.getAlbum(gid)["result"]["items"]
                    i = 0
                    if albums != []:
                        for album in albums:
                            cl.deleteAlbum(gid,album["id"])
                            i += 1
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,str(i) + "Deleted albums")
                    else:
                        cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All invitations have been refused")
                    else:
                        cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("album removeâ†’","")
                    albums = cl.getAlbum(gid)["result"]["items"]
                    i = 0
                    if albums != []:
                        for album in albums:
                            cl.deleteAlbum(gid,album["id"])
                            i += 1
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,str(i) + "Albums deleted")
                    else:
                        cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["autoAdd"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["autoAdd"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message change: ","")
                    cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message add: ","")
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message changed")
                    else:
                        cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                    else:
                        cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"message changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Add comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"String that can not be changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already on")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han1 gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han2 gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han3 gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                if msg.from_ in admin:
                    wait["wblack"] = True
                    cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                if msg.from_ in admin:
                    wait["dblack"] = True
                    cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if msg.from_ in admin:
                    if wait["commentBlack"] == {}:
                        cl.sendText(msg.to,"confirmed")
                    else:
                        cl.sendText(msg.to,"Blacklist")
                        mc = ""
                        for mi_d in wait["commentBlack"]:
                            mc += "" +cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        cl.sendText(msg.to,"already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if msg.from_ in admin:
                    if wait["clock"] == False:
                        cl.sendText(msg.to,"already off")
                    else:
                        wait["clock"] = False
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                if msg.from_ in admin:
                    n = msg.text.replace("Change clock ","")
                    if len(n.decode("utf-8")) > 13:
                        cl.sendText(msg.to,"changed")
                    else:
                        wait["cName"] = n
                        cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Jam Update")
                    else:
                        cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "Setlastpoint":
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Viewlastseen":
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")


#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["Han"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        ki.sendText(msg.to,"Hallo %s" % str(group.name))
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                        cl.sendText(msg.to,"Hallo %s" % str(group.name))

            elif msg.text in ["Han1 join"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Han2 join"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Han3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)

            elif msg.text in ["Han4 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kh.updateGroup(G)

            elif msg.text in ["Han5 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kg.updateGroup(G)

            elif msg.text in ["Han6 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ka.updateGroup(G)

            elif msg.text in ["Han7 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kb.updateGroup(G)

            elif msg.text in ["Han8 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)

            elif msg.text in ["Han9 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ke.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Han:bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        kg.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han1 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han2 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han3 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han4 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kh.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han5 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kg.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han6 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ka.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han7 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kb.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han8 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kd.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han9 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 2"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv1 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv2 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv3 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------
            elif "Copy " in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                   targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                  for target in targets:
                      try:
                          contact = cl.getContact(target)
                          X = contact.displayName
                          profile = cl.getProfile()
                          profile.displayName = X
                          cl.updateProfile(profile)
                          cl.sendText(msg.to, "Success")
                          #------------------------------------------------
                          Y = contact.statusMessage
                          lol = cl.getProfile()
                          lol.statusMessage = Y
                          cl.updateProfile(lol)
                          #------------------------------------------------
                          P = contact.pictureStatus
                          cl.updateProfilePicture(P)
                      except Exception as e:
                          cl.sendText(msg.to, "failed")
                          print e
#----------------------------------------
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f,sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#----------------------------------------
            elif ("Unban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f,sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes UnBanned")
                   except:
                      pass
#----------------------------------------
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#----------------------------------------
            elif "Mid @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Mid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            cl.sendText(msg.to, g.mid)
                        else:
                            pass
#----------------------------------------
            elif "Spam " in msg.text:
               if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                 #@rid1bdbx
                if txt[1] == "on":
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#----------------------------------------
            elif "Han:groupcreator" == msg.text:
                if msg.from_ in admin:
                            try:
                                group = cl.getGroup(msg.to)
                                GS = group.creator.mid
                                M = Message()
                                M.to = msg.to
                                M.contentType = 13
                                M.contentMetadata = {'mid': GS}
                                cl.sendMessage(M)
                            except:
                                W = group.members[0].mid
                                M = Message()
                                M.to = msg.to
                                M.contentType = 13
                                M.contentMetadata = {'mid': W}
                                cl.sendMessage(M)
                                cl.sendText(msg.to,"old user")

#----------------------------------------
            elif msg.text in ["Backup","backup"]:
                try:
                   cl.updateDisplayPicture(backup.pictureStatus)
                   cl.updateProfile(backup)
                except Exception as e:
                   cl.sendText(msg.to, str(e))
#----------------------------------------
            elif msg.text in ["Han:creator"]:
                if msg.toType == 2:
                      msg.contentType = 13
                      Creatorbot = "u761c4f29d0d8028f9d4e216932e6c444"
                      try:
                          msg.contentMetadata = {'mid': Creatorbot}
                      except:
                        Creatorbot = "Error"
                      ki.sendText(msg.to, "My Creator : Rayhan")
                      ki.sendMessage(msg)
#----------------------------------------
            elif msg.text in ["Tag"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error

#-----------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.from_ in admin:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Fuck You")
                        kc.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,kh,kg,ka]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Cleanse" in msg.text:
                if msg.from_ in admin:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    ki.sendText(msg.to,"ASSASSIN PLAYER WAS HARE")
                    kk.sendText(msg.to,"JANGAN DI LIATIN DOANG")
                    kc.sendText(msg.to,"YAH RATA NIH KAYA TETE LU RATA")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                        kc.sendText(msg.to,"Not found.")
                        kh.sendText(msg.to,"Not found.")
                        kg.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            if not target in admin:
                                try:
                                    klist=[ki,kk,kc,kh,kg,ka,kb,kd,ke]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group Bersih")
                                    kk.sendText(msg.to,"Group Bersih")
                                    kc.sendText(msg.to,"Group Bersih")
                                    kh.sendText(msg.to,"Group Bersih")
                                    kg.sendText(msg.to,"Group Bersih")
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc,kh,kg]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes Han")
                                    kk.sendText(msg.to,"Fuck You")
#-------------------------------------------------------------------------------
            elif "/say " in msg.text.lower():
                 if msg.from_ in admin:
                     query = msg.text.replace("/say ","")
                     with requests.session() as s:
                         s.headers['user-agent'] = 'Mozilla/5.0'
                         url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                         params = {'language': 'id', 'speed': '1', 'query': query}
                         r = s.get(url, params=params)
                         mp3 = r.url
                         cl.sendAudioWithURL(msg.to, mp3)

            elif ".music " in msg.text.lower():
                if msg.from_ in admin:
                    songname = msg.text.lower().replace(".music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                     cl.sendAudioWithURL(to, song[3])
#-------------------------------------------------------------------------------
            elif "Blacklist @ " in msg.text:
                 if msg.from_ in admin:
                     _name = msg.text.replace("Blacklist @ ","")
                     _kicktarget = _name.rstrip(' ')
                     gs = ki2.getGroup(msg.to)
                     targets = []
                     for g in gs.members:
                         if _kicktarget == g.displayName:
                            targets.append(g.mid)
                            if targets == []:
                                cl.sendText(msg.to,"Not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        k3.sendText(msg.to,"Succes Han")
                                    except:
                                        ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Han")
                        kk.sendText(msg.to,"Not found Han")
                        kc.sendText(msg.to,"Not found Han")
                        kh.sendText(msg.to,"Not found Han")
                        kg.sendText(msg.to,"Not found Han")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes Han")
                                ki.sendText(msg.to,"Succes Han")
                                kk.sendText(msg.to,"Succes Han")
                                kc.sendText(msg.to,"Succes Han")
                                kh.sendText(msg.to,"Succes Han")
                                kg.sendText(msg.to,"Succes Han")
                            except:
                                ki.sendText(msg.to,"Error")
                                kk.sendText(msg.to,"Error")
                                kc.sendText(msg.to,"Error")
                                kh.sendText(msg.to,"Error")
                                kg.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Han")
                        kk.sendText(msg.to,"Not found Han")
                        kc.sendText(msg.to,"Not found Han")
                        kh.sendText(msg.to,"Not found Han")
                        kg.sendText(msg.to,"Not found Han")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes Han")
                                ki.sendText(msg.to,"Succes Han")
                                kk.sendText(msg.to,"Succes Han")
                                kc.sendText(msg.to,"Succes Han")
                                kh.sendText(msg.to,"Succes Han")
                                kg.sendText(msg.to,"Succes Han")
                            except:
                                ki.sendText(msg.to,"Succes Han")
                                kk.sendText(msg.to,"Succes Han")
                                kc.sendText(msg.to,"Succes Han")
                                kh.sendText(msg.to,"Succes Han")
                                kg.sendText(msg.to,"Succes Han")
#-----------------------------------------------
            elif msg.text in ["Han:version"]:
                ki.sendText(msg.to,"Versi saat ini 4.0.7\nlast updated 20 November 2017 18:20\n-----------------------------\nAuto Like:on\n-----------------------------\nIP Admin:10.23.34.69\nAdmin Location:Jakarta Barat,Indonesia\n-----------------------------\nServer:Singapura")
#-----------------------------------------------
            elif msg.text in ["Hallo Han"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Hallo Bos Rayhan")
                    kk.sendText(msg.to,"Hallo Bos Rayhan")
                    kc.sendText(msg.to,"Hallo Bos Rayhan")
                    kh.sendText(msg.to,"Hallo Bos Rayhan")
                    kg.sendText(msg.to,"Hallo Bos Rayhan")
                    ka.sendText(msg.to,"Hallo Bos Rayhan")
                    kb.sendText(msg.to,"Hallo Bos Rayhan")
                    kd.sendText(msg.to,"Hallo Bos Rayhan")
                    ke.sendText(msg.to,"Hallo Bos Rayhan")
#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
                                kh.sendText(msg.to,(bctxt))
                                kg.sendText(msg.to,(bctxt))
                                ka.sendText(msg.to,(bttxt))
                                kb.sendText(msg.to,(bctxt))
                                kd.sendText(msg.to,(bctxt))
                                ke.sendText(msg.to,(bttxt))
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                ki.sendText(msg.to,jawaban)
#-----------------------------------------------

            elif msg.text in ["Cv say hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Han say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Han 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Han 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Have a nice dream Han 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Rayhan Family Room")
                kk.sendText(msg.to,"Jangan nakal ya!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Protect On","protect on"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"Loading...")
                    ki.sendText(msg.to,"20%")
                    kk.sendText(msg.to,"40%")
                    kc.sendText(msg.to,"60%")
                    kh.sendText(msg.to,"80%")
                    kg.sendText(msg.to,"100%")
                    ka.sendText(msg.to,"Waiting...")
                    cl.sendText(msg.to,"protection is on")
#-----------------------------------------------
            elif msg.text in["Translate","Penerjemah"]:
                if msg.from_ in admin:
                    T = """╔═══¤|| List Translate ||¤════
                    ║tr-in ->Indonesia
                    ║tr-en ->English
                    ║tr-de ->Deutsch
                    ║tr-kr ->Korea
                    ║tr-ar ->Arab
                    ║tr-fr ->France
                    ║tr-cn ->Chinse
                    ║tr-jp ->Japan
                    ║tr-th ->Thailand
                    ║tr-hi ->Hindia
                    ║tr-jw ->Jawa
                    ╚═══════════════"""
                    cl.sendText(msg.to, T)
            elif "tr-en " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-en ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
            elif "tr-de " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-de ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
            elif "tr-kr " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-kr ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kr')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to, "Progress...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    ki.sendText(msg.to,"Kirim Komtak Nya Han")
            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Kirim Kontak Nya Han")
            elif msg.text in ["Banlist"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to,"Gak Ada")
                    else:
                        cl.sendText(msg.to,"Blacklist user")
                        mc = ""
                        for mi_d in wait["blacklist"]:
                            mc += "->" +cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Gak Ada blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        kh.kickoutFromGroup(msg.to,[jj])
                        kg.kickoutFromGroup(msg.to,[jj])
                        ka.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Good Bye")
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                cl.sendText
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True


def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kh.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kh.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kg.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kg.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kd.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kd.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)


