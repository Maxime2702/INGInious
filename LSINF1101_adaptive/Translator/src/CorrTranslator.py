#!/usr/bin/python3
# -*- coding: utf-8 -*-


fr = {
"test" : "test",
"i" : "je",
"you" : "tu",
"elephant" : "éléphant",
"this" : "ceci",
"is" : "est",
"a" : "un",
"shot" : "ai tiré",
"an" : "un",
"in" : "dans",
"my" : "mon",
"pajama" : "pyjama"
}

es = {
"test" : "prueba",
"i" : "yo",
"you" : "te",
"elephant" : "elefante",
"this" : "esta",
"is" : "es",
"a" : "un",
"shot" : "disparo",
"an" : "un",
"in" : "en",
"my" : "mi",
"pajama" : "pijama"
}

def translate(text, lan):
    trad = ""
    for c in text.split(' '):
        if c.lower() in lan:
            trad += lan[c.lower()] + ' '
        else:
            trad += c + ' '
    return trad