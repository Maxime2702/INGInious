class Duree:

    def __init__(self, hours, minutes, seconds):
        """
        Crée une nouvelle durée en heures, minutes et secondes.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        """
        Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return '{:02}:{:02}:{:02}'.format(self.hours, self.minutes, self.seconds)

    def toSecondes(self):
        """
        Retourne le nombre total de secondes de cette durée (self).
        """
        return self.seconds + 60 * (self.minutes + 60 * self.hours)

    def delta(self, other_duree):
        """
        Retourne la différence entre cette durée (self) et la durée other_duree passée en paramètre,
        en secondes (positif si ce temps-ci est plus grand).
        """
        return self.toSecondes() - other_duree.toSecondes()

    def apres(self, other_duree):
        """
        Retourne True si cette durée (self) est plus grand que la durée other_duree passée en paramètre;
        retourne False sinon.
        """
        return ( self.delta(other_duree) > 0 )

    def ajouter(self, other_duree):
        """
        Ajoute une autre durée other_duree à cette durée (self).
        Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
        en reportant au besoin les valeurs hors limites sur les unités supérieures
        (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        time = self.toSecondes() + other_duree.toSecondes()
        self.seconds = time % 60
        self.minutes = (time//60) % 60
        self.hours = (time//3600) % 24

class Chanson:
    
    def __init__(self, title, author, duree):
        """
        Créez une nouvelle chanson, caractérisée par un titre (string), un auteur (string) et une durée (Duree).
        """
        self.title = title
        self.author = author
        self.duree = duree

    def __str__(self):
        """
        Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return '{} - {} - {}'.format(self.title, self.author, self.duree)

class Album:
    
    def __init__(self, number):
        self.number = number
        self.chansons = []
        self.duree = Duree(0,0,0)

    def __str__(self):
        rep = 'Album {} ({} chansons, {})\n'.format(str(self.number), str(len(self.chansons)), str(self.duree))
        for i in range(1, len(self.chansons)+1):
            rep += '{:02}: {}\n'.format(i, self.chansons[i-1])
        return rep

    def add(self, music):
        successful = False
        if (self.duree.toSecondes() + music.duree.toSecondes()) <= 75*60 and len(self.chansons) <= 99:
            self.chansons.append(music)
            self.duree.ajouter(music.duree)
            successful = True
        return successful

with open('music-db.txt', 'r') as file:
    album = Album(1)
    for line in file.readlines():
        chansonline = line.split()
        chanson = Chanson(chansonline[0], chansonline[1], Duree(0, int(chansonline[2]), int(chansonline[3])))
        if not album.add(chanson):
            print(album)
            album = Album(album.number+1)
            album.add(chanson)
    print(album)

