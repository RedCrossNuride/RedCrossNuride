
from komekci.aykhan import Ekber
import base64
from mesajlar.mesaj import salam, necesen, sagol, getdim, geldim, qargis, am, ozun, hi, bax, hara, ds, nazli, bc, sd, ny,ax, nrs, sev, gul1, gul2, brs, yuxu, haralisan, can, yas, nermin, ban
from mesajlar.bot import yeni_user, start
from telethon import events, Button
import random

# Yeni istifadəçi mesajı
@Ekber.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")

Ekber_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67"
@Ekber.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}")

@Ekber.on(events.NewMessage(pattern='(?i)salam+'))
@Ekber.on(events.NewMessage(pattern='(?i)Salam+'))
@Ekber.on(events.NewMessage(pattern='(?i)Selam+'))
@Ekber.on(events.NewMessage(pattern='(?i)selam+'))
@Ekber.on(events.NewMessage(pattern='(?i)a.salam+'))
@Ekber.on(events.NewMessage(pattern='(?i)A.salam+'))
@Ekber.on(events.NewMessage(pattern='(?i)A.Salam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

@Ekber.on(events.NewMessage(pattern='(?i)necəsən+'))
@Ekber.on(events.NewMessage(pattern='(?i)necesen+'))
@Ekber.on(events.NewMessage(pattern='(?i)Necəsən+'))
@Ekber.on(events.NewMessage(pattern='(?i)Necesen+'))
@Ekber.on(events.NewMessage(pattern='(?i)Necəsiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)Necəsiiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)necəsiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)nətərsən+'))
@Ekber.on(events.NewMessage(pattern='(?i)Nətərsən+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

@Ekber.on(events.NewMessage(pattern='(?i)Sağol+'))
@Ekber.on(events.NewMessage(pattern='(?i)sagol+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

@Ekber.on(events.NewMessage(pattern='(?i)Hapşu+'))
@Ekber.on(events.NewMessage(pattern='(?i)Hapsu+'))
@Ekber.on(events.NewMessage(pattern='(?i)Xəsdələnmişəm+'))
@Ekber.on(events.NewMessage(pattern='(?i)xəsdələnmişəm+'))
@Ekber.on(events.NewMessage(pattern='(?i)Xəsdə+'))
@Ekber.on(events.NewMessage(pattern='(?i)Xesdelenmisem+'))
@Ekber.on(events.NewMessage(pattern='(?i)xesdelenmisem+'))
@Ekber.on(events.NewMessage(pattern='(?i)Soyuğ dəyib+'))
@Ekber.on(events.NewMessage(pattern='(?i)hapsu+'))
@Ekber.on(events.NewMessage(pattern='(?i)hapşu+'))
@Ekber.on(events.NewMessage(pattern='(?i)soyuğ dəyib+'))
@Ekber.on(events.NewMessage(pattern='(?i)Soyug deyib+'))
@Ekber.on(events.NewMessage(pattern='(?i)soyug deyib+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sd)}")

@Ekber.on(events.NewMessage(pattern='(?i)getdim+'))
@Ekber.on(events.NewMessage(pattern='(?i)gedim+'))
@Ekber.on(events.NewMessage(pattern='(?i)gedirəm+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

@Ekber.on(events.NewMessage(pattern='(?i)Bacım+'))
@Ekber.on(events.NewMessage(pattern='(?i)bacım+'))
@Ekber.on(events.NewMessage(pattern='(?i)Bacı+'))
@Ekber.on(events.NewMessage(pattern='(?i)bacı+'))
@Ekber.on(events.NewMessage(pattern='(?i)Bacim+'))
@Ekber.on(events.NewMessage(pattern='(?i)bacim+'))
@Ekber.on(events.NewMessage(pattern='(?i)Baci+'))
@Ekber.on(events.NewMessage(pattern='(?i)baci+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(bc)}")

@Ekber.on(events.NewMessage(pattern='(?i)Öl+'))
@Ekber.on(events.NewMessage(pattern='(?i)öl+'))
@Ekber.on(events.NewMessage(pattern='(?i)sən öl+'))
@Ekber.on(events.NewMessage(pattern='(?i)Sən öl+'))
@Ekber.on(events.NewMessage(pattern='(?i)Öl Elə+'))
@Ekber.on(events.NewMessage(pattern='(?i)Ol elə+'))
@Ekber.on(events.NewMessage(pattern='(?i)ol elə+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ozun)}")

@Ekber.on(events.NewMessage(pattern='(?i)Niyə yatmırsız+'))
@Ekber.on(events.NewMessage(pattern='(?i)niyə yatmırsız+'))
@Ekber.on(events.NewMessage(pattern='(?i)Niyə yatmırsan+'))
@Ekber.on(events.NewMessage(pattern='(?i)niyə yatmırsan+'))
@Ekber.on(events.NewMessage(pattern='(?i)Niye yatmirsiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)niye yatmırsiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)Niye yatmirsan+'))
@Ekber.on(events.NewMessage(pattern='(?i)niye yatmırsan+'))
@Ekber.on(events.NewMessage(pattern='(?i)Yatmırsız+'))
@Ekber.on(events.NewMessage(pattern='(?i)yatmırsız+'))
@Ekber.on(events.NewMessage(pattern='(?i)Yatmırsan+'))
@Ekber.on(events.NewMessage(pattern='(?i)yatmırsan+'))
@Ekber.on(events.NewMessage(pattern='(?i)Yatmirsiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)yatmırsiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)Yatmirsan+'))
@Ekber.on(events.NewMessage(pattern='(?i)yatmırsan+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(am)}")

@Ekber.on(events.NewMessage(pattern='(?i)Neyniyirsən+'))
@Ekber.on(events.NewMessage(pattern='(?i)neyniyirsən+'))
@Ekber.on(events.NewMessage(pattern='(?i)Neyniyirsen+'))
@Ekber.on(events.NewMessage(pattern='(?i)neyniyirsen+'))
@Ekber.on(events.NewMessage(pattern='(?i)Neyniyirsiz+'))
@Ekber.on(events.NewMessage(pattern='(?i)neyniyirsiz+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ny)}")

@Ekber.on(events.NewMessage(pattern='(?i)👀+'))
@Ekber.on(events.NewMessage(pattern='(?i)👀👀+'))
@Ekber.on(events.NewMessage(pattern='(?i)👀👀👀+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(brs)}")


@Ekber.on(events.NewMessage(pattern='(?i)😁+'))
@Ekber.on(events.NewMessage(pattern='(?i)😁😁+'))
@Ekber.on(events.NewMessage(pattern='(?i)😁😁😁+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ds)}")

@Ekber.on(events.NewMessage(pattern='(?i)gəldim+'))
@Ekber.on(events.NewMessage(pattern='(?i)geldim+'))
@Ekber.on(events.NewMessage(pattern='(?i)men geldim+'))
@Ekber.on(events.NewMessage(pattern='(?i)Men geldim+'))
@Ekber.on(events.NewMessage(pattern='(?i)Mən gəldim+'))
@Ekber.on(events.NewMessage(pattern='(?i)mən gəldim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

@Nermin.on(events.NewMessage(pattern='(?i)gül+'))
@Nermin.on(events.NewMessage(pattern='(?i)gülümsə+'))
@Nermin.on(events.NewMessage(pattern='(?i)Gülümsə+'))
@Nermin.on(events.NewMessage(pattern='(?i)balam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(nermin)}")

@Nermin.on(events.NewMessage(pattern='(?i)ban+'))
@Nermin.on(events.NewMessage(pattern='(?i)kick+'))
@Nermin.on(events.NewMessage(pattern='(?i)mute+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")

@Nermin.on(events.NewMessage(pattern='(?i)Hi+'))
@Nermin.on(events.NewMessage(pattern='(?i)hi+'))
@Nermin.on(events.NewMessage(pattern='(?i)Hii+'))
@Nermin.on(events.NewMessage(pattern='(?i)hii+'))
@Nermin.on(events.NewMessage(pattern='(?i)hiii+'))
@Nermin.on(events.NewMessage(pattern='(?i)Hiii+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hi)}")

@Nermin.on(events.NewMessage(pattern='(?i)Hardandasan+'))
@Nermin.on(events.NewMessage(pattern='(?i)hardandasan+'))
@Nermin.on(events.NewMessage(pattern='(?i)haralısan+'))
@Nermin.on(events.NewMessage(pattern='(?i)Haralısan+'))
@Nermin.on(events.NewMessage(pattern='(?i)Harda yaşıyırsan+'))
@Nermin.on(events.NewMessage(pattern='(?i)Harda yasiyirsan+'))
@Nermin.on(events.NewMessage(pattern='(?i)Eslen haralısan+'))
@Nermin.on(events.NewMessage(pattern='(?i)eslen haralısan+'))
@Nermin.on(events.NewMessage(pattern='(?i)Əslən haralısan+'))
@Nermin.on(events.NewMessage(pattern='(?i)əslən haralısan+'))
@Nermin.on(events.NewMessage(pattern='(?i)haralısan sən canı+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(haralisan)}")

@Nermin.on(events.NewMessage(pattern='(?i)Can+'))
@Nermin.on(events.NewMessage(pattern='(?i)can+'))
@Nermin.on(events.NewMessage(pattern='(?i)Cannn+'))
@Nermin.on(events.NewMessage(pattern='(?i)cannn+'))
@Nermin.on(events.NewMessage(pattern='(?i)Cann+'))
@Nermin.on(events.NewMessage(pattern='(?i)cann+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(can)}")

@Nermin.on(events.NewMessage(pattern='(?i)Hardasan+'))
@Nermin.on(events.NewMessage(pattern='(?i)hardasan+'))
@Nermin.on(events.NewMessage(pattern='(?i)Haradasan+'))
@Nermin.on(events.NewMessage(pattern='(?i)haradasan+'))
@Nermin.on(events.NewMessage(pattern='(?i)hara+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hara)}")

@Nermin.on(events.NewMessage(pattern='(?i)Nazlı+'))
@Nermin.on(events.NewMessage(pattern='(?i)nazlı+'))
@Nermin.on(events.NewMessage(pattern='(?i)Nazli+'))
@Nermin.on(events.NewMessage(pattern='(?i)nazli+'))
@Nermin.on(events.NewMessage(pattern='(?i)@nazlisohbetbot+'))
@Nermin.on(events.NewMessage(pattern='(?i)Nazlım+'))
@Nermin.on(events.NewMessage(pattern='(?i)nazlım+'))
@Nermin.on(events.NewMessage(pattern='(?i)Nazlim+'))
@Nermin.on(events.NewMessage(pattern='(?i)nazlim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(nazli)}")

@Nermin.on(events.NewMessage(pattern='(?i)Qarğış+'))
@Nermin.on(events.NewMessage(pattern='(?i)qarğış+'))
@Nermin.on(events.NewMessage(pattern='(?i)@qargisbot+'))
@Nermin.on(events.NewMessage(pattern='(?i)Qargış+'))
@Nermin.on(events.NewMessage(pattern='(?i)qargış+'))
@Nermin.on(events.NewMessage(pattern='(?i)Qargiş+'))
@Nermin.on(events.NewMessage(pattern='(?i)qargiş+'))
@Nermin.on(events.NewMessage(pattern='(?i)Qarğiş+'))
@Nermin.on(events.NewMessage(pattern='(?i)qarğiş+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(qargis)}")

@Nermin.on(events.NewMessage(pattern='(?i)Neçə yaşın var+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yaş+'))
@Nermin.on(events.NewMessage(pattern='(?i)yaş+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yas+'))
@Nermin.on(events.NewMessage(pattern='(?i)yas+'))
@Nermin.on(events.NewMessage(pattern='(?i)neçə yaşın var+'))
@Nermin.on(events.NewMessage(pattern='(?i)Neçe yaşin var+'))
@Nermin.on(events.NewMessage(pattern='(?i)neçe yaşin var+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yaşın Neçədi+'))
@Nermin.on(events.NewMessage(pattern='(?i)yaşın neçədi+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yaşın neçədi+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yaşin və adın+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yaşin və Adın+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yaşın və adın+'))
@Nermin.on(events.NewMessage(pattern='(?i)yaşın və adın+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(yas)}") 

@Nermin.on(events.NewMessage(pattern='(?i)Sevgilim+'))
@Nermin.on(events.NewMessage(pattern='(?i)Ömrüm+'))
@Nermin.on(events.NewMessage(pattern='(?i)Sevdiyim+'))
@Nermin.on(events.NewMessage(pattern='(?i)Canım+'))
@Nermin.on(events.NewMessage(pattern='(?i)Sevmək+'))
@Nermin.on(events.NewMessage(pattern='(?i)sevmək+'))
@Nermin.on(events.NewMessage(pattern='(?i)Sevmek+'))
@Nermin.on(events.NewMessage(pattern='(?i)sevmek+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sev)}")


@Nermin.on(events.NewMessage(pattern='(?i)Axşamınız xeyir+'))
@Nermin.on(events.NewMessage(pattern='(?i)Axsaminiz xeyir+'))
@Nermin.on(events.NewMessage(pattern='(?i)axşamınız xeyir+'))
@Nermin.on(events.NewMessage(pattern='(?i)axsaminiz xeyir+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ax)}")

@Nermin.on(events.NewMessage(pattern='(?i)Nə+'))
@Nermin.on(events.NewMessage(pattern='(?i)nə+'))
@Nermin.on(events.NewMessage(pattern='(?i)Nəə+'))
@Nermin.on(events.NewMessage(pattern='(?i)nə+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(nrs)}")

@Nermin.on(events.NewMessage(pattern='(?i)😅+'))
@Nermin.on(events.NewMessage(pattern='(?i)😅😅+'))
@Nermin.on(events.NewMessage(pattern='(?i)😅😅😅+'))
@Nermin.on(events.NewMessage(pattern='(?i)😅😅😅😅+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gul1)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)😳+'))
@Nermin.on(events.NewMessage(pattern='(?i)😳😳+'))
@Nermin.on(events.NewMessage(pattern='(?i)😳😳😳+'))
@Nermin.on(events.NewMessage(pattern='(?i)😳😳😳😳+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(bax)}")

@Nermin.on(events.NewMessage(pattern='(?i)😂+'))
@Nermin.on(events.NewMessage(pattern='(?i)😂😂+'))
@Nermin.on(events.NewMessage(pattern='(?i)😂😂😂+'))
@Nermin.on(events.NewMessage(pattern='(?i)😂😂😂😂+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gul2)}")

@Nermin.on(events.NewMessage(pattern='(?i)Şirin yuxular+'))
@Nermin.on(events.NewMessage(pattern='(?i)şirin yuxular+'))
@Nermin.on(events.NewMessage(pattern='(?i)Sirin yuxular+'))
@Nermin.on(events.NewMessage(pattern='(?i)sirin yuxular+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yuxun şirin olsun+'))
@Nermin.on(events.NewMessage(pattern='(?i)yuxun şirin olsun+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yuxu şirin olsun+'))
@Nermin.on(events.NewMessage(pattern='(?i)yuxun şirin olsun+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yuxun sirin olsun+'))
@Nermin.on(events.NewMessage(pattern='(?i)yuxun sirin olsun+'))
@Nermin.on(events.NewMessage(pattern='(?i)yatıram+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yatıram+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yatmağa gedirəm+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yatmaga gedirəm+'))
@Nermin.on(events.NewMessage(pattern='(?i)Yatmaga gedirem+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(yuxu)}")
    
@Ekber.on(events.NewMessage(pattern='(?i)Sikdir+'))
@Ekber.on(events.NewMessage(pattern='(?i)sikdir+'))
@Ekber.on(events.NewMessage(pattern='(?i)Siktir+'))
@Ekber.on(events.NewMessage(pattern='(?i)siktir+'))
@Ekber.on(events.NewMessage(pattern='(?i)seks+'))
@Ekber.on(events.NewMessage(pattern='(?i)Seks+'))
@Ekber.on(events.NewMessage(pattern='(?i)Sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)Sikim sənin ağzıvı+'))
@Ekber.on(events.NewMessage(pattern='(?i)sikim sənin ağzıvı+'))
@Ekber.on(events.NewMessage(pattern='(?i)Peyser+'))
@Ekber.on(events.NewMessage(pattern='(?i)peyser+'))
@Ekber.on(events.NewMessage(pattern='(?i)Anavı sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)Anavi sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)anavı sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)anavui sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)Bacivi sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)bacivi sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)Bacıvı sikim+'))
@Ekber.on(events.NewMessage(pattern='(?i)bacıvı sikim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.delete()
    
Ekber_run = Ekber_start.decode("utf8")
print(">> Grup Cavab Botu Aktivdi ♿<<")
print(f"{Ekber_run}")
Ekber.run_until_disconnected()
