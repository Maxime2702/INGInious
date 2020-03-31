#! /usr/bin/python3
# -*- coding: utf-8 -*-

class Piece :

    def __init__(self,description,prix_unitaire,poids_unitaire = 0,fragile = False,tva_reduit=False):
        """
        Crée une pièce avec une description, p.ex. 'souris bluetooth';
        un prix unitaire, p.ex. 15,99 Euro; 
        un poids unitaire en kg, p.ex. 0,154 kg;
        un indicateur booléen indiquant si la pièce est fragile, p.ex. un disque dur est fragile mais pas une souris;
        un indicateur booléen indiquant si la pièce est à taux de TVA réduit, p.ex. les livres bénéficient de TVA réduite;
        """
        self.__description = description
        self.__prix = prix_unitaire
        self.__poids = poids_unitaire
        self.__fragile = fragile
        self.__tva_reduit = tva_reduit

    def description(self):
        """
        Retourne la description de cette pièce.
        """
        return self.__description

    def prix(self):
        """
        Retourne le prix de cette pièce.
        """
        return self.__prix

    def poids(self):
        """
        Retourne le poids unitaire en kg de cette pièce.
        """
        return self.__poids
        
    def fragile(self):
        """
        Retourne si cette pièce est fragile ou non.
        """
        return self.__fragile

    def tva_reduit(self):
        """
        Retourne si cette pièce est à taux de TVA réduit.
        """
        return self.__tva_reduit

    def __eq__(self,other):
        if type(other) is Piece :
            return self.description() == other.description() and self.prix() == other.prix()
        return False

class Article :

    __taux_tva = 0.21   # TVA a 21%
    
    def __init__(self,d,p):
        """
        Cree un article avec description d et prix p.
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        Retourne la description de cet article.
        """
        return self.__description
        
    def prix(self):
        """
        Retourne le prix (HTVA) de cet article.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        Retourne le taux de TVA (même valeur pour chaque article)
        """    
        return self.__taux_tva

    def tva(self):
        """
        Retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        Retourne le prix de l'article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        Retourne un texte decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f}".format(self.get_description, self.get_prix())

class ArticlePiece(Article) :

    __taux_tva_reduit = 0.06   # TVA réduit a 6%

    def __init__(self,nombre,piece):
        """
        Cree un article représente l'achat d'un nombre donné d'une pièce donnée.        
        """
        self.__nombre = nombre
        self.__piece = piece

    def piece(self):
        """
        Retourne la pièce de cet article.
        """
        return self.__piece

    def nombre(self):
        """
        Retourne le nombre de pièces dans cet article.
        """
        return self.__nombre

    def description(self):
        """
        Retourne une description de cet article, mentionnant la pièce, le nombre et le prix unitaire, par exemple: 3 * souris bluetooth @ 15.99
        """
        return "{0} * {1} @ {2:5.2f}".format(self.nombre(),self.piece().description(),self.piece().prix())

    def prix(self):
        """
        Retourne le produit du prix unitaire de la pièce par le nombre de pièces.
        """
        return self.piece().prix() * self.nombre()
        
    def taux_tva(self):
        """
        Retourne le taux de TVA.
        Le taux de TVA réduit est appliqué pour des pièces à taux réduit.
        Le taux de TVA normal est appliqué aux autres pièces.
        """    
        if self.piece().tva_reduit() :
            return self.__taux_tva_reduit
        else :
            return super().taux_tva()

class ArticleReparation(Article) :

    def __init__(self,duree):
        """
        Crée une prestation de réparation de durée donnée (un float, en heures).
        """
        self.__duree = duree

    def duree(self):
        """
        Retourne la durée de cet prestation de réparation.
        """
        return self.__duree
        
    def description(self):
        """
        Retourne la description de cet prestation de réparation.
        """
        return "Réparation ({0:4.2f} heures)".format(self.duree())

    def prix(self):
        """
        Retourne le prix (HTVA) de cet article.
        """
        cout_fixe = 20.0   # coût fixe de 20 euro
        cout_variable = 35 #coût variable de 35 euro/h
        return 20 + self.duree() * cout_variable

class Facture :

    __numero_facture = 0    # This line was added during Etape 4 of the mission

    def __init__(self, description, articles):
        """
        Crée une facture avec une description (titre) et un liste d'articles.
        """
        self.__reference = description
        self.__articles = articles

    def description(self):
        """
        Retourne la description de cette facture.
        """
        return self.__reference

    def articles(self):
        """
        Retourne la liste des articles de cette facture.
        """
        return self.__articles
        
    def __str__(self):
        """
        Retourne la représentation string d'une facture, à imprimer avec la méthode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles() :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        Facture.__numero_facture += 1                           # This line was added during Etape 4 of the mission
        e = "Facture No {} : ".format(Facture.__numero_facture) # This line was added during Etape 4 of the mission
        e += "Facture " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string représentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
        Retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())
    
    def totaux_str(self, prix, tva):
        """
        Retourne un string représentant une ligne de facture avec les totaux prix et tva, à imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva)
        b += self.barre_str()
        return b

    # This method was added during Etape 4 of the mission
    def nombre(self, pce) :
        """
        Retourne le nombre d'exemplaires de la pièce pce dans la facture, en totalisant sur tous les articles qui concernent cette pièce.
        """
        nbr = 0
        for art in self.articles():
            if (type(art) is ArticlePiece) and (pce == art.piece()) :
                nbr += art.nombre()
        return nombre
        
    # This method was added during Etape 5 of the mission
    def printLivraison(self) :
        """
        Imprime une liste de livraison, comprenant toutes les pièces facturées avec leur poids.
        """
        print(self.livraision_str())

    # This method was added during Etape 5 of the mission
    def livraision_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        s = self.entete_livraision_str()        # une en-tête avec la description de la facture;
        totalArt = 0                 # compteur du nombre d'articles
        totalPce = 0                 # compteur du nombre de pièces
        totalPds = 0.0               # compteur du poids total
        fragiles = False             # indicateur s'il y a des pièces fragiles
        for art in self.articles() :
            if type(art) is ArticlePiece :
                s += self.article_livraison_str(art)
                totalArt += 1
                totalPce += art.nombre()
                totalPds += art.piece().poids()*art.nombre()
                fragiles = fragiles or art.piece().fragile()
        s += self.totaux_livraison_str(totalArt, totalPce,totalPds)
        if fragiles:                 # imprime un message supplémentaire si la livraison contient des pièces fragiles.
            s += "(!) *** livraison fragile ***"
        return s

    # This method was added during Etape 5 of the mission
    def entete_livraision_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode livraison_str
        Imprime l'entête de la livraison, comprenant le descriptif et les têtes de colonnes.
        """
        Facture.__numero_facture += 1                           
        e = "Livraison - Facture No {} : ".format(Facture.__numero_facture)
        e += self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids")
        e += self.barre_str()
        return e

    # This method was added during Etape 5 of the mission
    def article_livraison_str(self, art):
        """
        Cette méthode est une méthode auxiliaire pour la méthode livraison_str
        Retourne un string correspondant à une ligne de livraison pour l'article art
        """
        descr = art.description()
        if art.piece().fragile() :
            descr += " (!)"
        piece_poids = art.piece().poids()
        art_poids = piece_poids * art.nombre()
        return "| {0:40} | {1:8.3f}kg | {2:10} | {2:8.3f}kg |\n".format(descr, piece_poids, art.nombre(), art_poids)
        
    # This method was added during Etape 5 of the mission
    def totaux_livraison_str(self, arts, pces, pds):
        """
        Cette méthode est une méthode auxiliaire pour la méthode livraison_str
        Retourne un string représentant une ligne de facture avec les nombres totaux d'articles, de pièces et leurs poids total, à imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:31} articles |            | {1:10} | {2:8.3f}kg |\n".format(arts, pces, pds)
        b += self.barre_str()
        return b

