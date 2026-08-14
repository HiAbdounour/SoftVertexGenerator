from core.xmlparser import xmlparser
from core.imap import imap_converter

REF = "bracket.xml"
FOS = xmlparser(REF)
if FOS is not None:
    print(f'Fichier SVG généré : {FOS}.') # à ce stade, ne pas modifier le fichier !
    c = input("Souhaitez-vous transformer le plan SVG en ImageMap ? (Y/y) ")
    if c=='Y' or c=='y':
        sx = input("Sauvegarder l'ImageMap ? (S/s) ")
        imap_converter(FOS,sx=='S' or sx=='s')