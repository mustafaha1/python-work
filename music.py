from win32com.client import Dispatch

wmp = Dispatch('WMPlayer.OCX')

liste = [r"F:\Mp3\rep\6.Evinden Uzakta.mp3",
         r"F:\Mp3\rep\07___SAGOPA_KAJMER___BIR__I.MP3",
         r"F:\Mp3\rep\7.Terzi.mp3",
         r"F:\Mp3\rep\08. Rüya.mp3",
         r"F:\Mp3\rep\8.Battle Edebiyatı.mp3",
         r"F:\Mp3\rep\09_AUDIOTRACK_09.MP3",
         r"F:\Mp3\rep\02. Sagopa Kajmer - Uzun Yollara Devam.mp3",
         r"F:\Mp3\rep\2Pac_-_CHANGE.mp3",
         r"F:\Mp3\rep\03. Herkes.mp3",
         r"F:\Mp3\rep\06. Sagopa Kajmer - Istakoz.mp3"]


for x in liste:
    mp3 = wmp.newMedia(x)
    wmp.currentPlaylist.appendItem(mp3)

wmp.controls.play()