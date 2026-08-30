from core.xmlparser import xmlparser
from core.imap import imap_converter

REF = "bracket.xml"
FOS = xmlparser(REF)
if FOS is not None:
    print(f'Fichier SVG généré : {FOS}.') # à ce stade, ne pas modifier le fichier !
    c = input("Souhaitez-vous obtenir l'ImageMap associée ? (Y/y) ")
    if c=='Y' or c=='y':
        sx = input("Souhaitez-vous sauvegarder l'ImageMap dans un fichier ? (S/s) ")
        imap_converter(FOS,sx=='S' or sx=='s')