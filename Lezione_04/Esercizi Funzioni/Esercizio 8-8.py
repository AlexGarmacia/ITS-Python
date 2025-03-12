def make_album (artista,album, numero_brani=None):
    album= {"artista":artista, "album":album, "numero_brani":numero_brani}
    print(album)

i=0
while i<5:
    print(make_album(artista=input("inserisci artista"), album=input("inserisci album", numero_brani=input("inserisci numero brani"))))
    i+=1

