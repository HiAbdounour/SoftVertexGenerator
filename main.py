from core.xmlparser import xmlparser
from core.imap import imap_converter

REF = "bracket.xml"
FOS = xmlparser(REF)
if FOS is not None:
    print(f'Fichier SVG généré : {FOS}.') # à ce stade, ne pas modifier le fichier !
    c = input("Souhaitez-vous transformer le plan SVG en ImageMap ? (oui=Y/y)")
    if c=='Y' or c=='y':
        imap_converter(FOS)
    print("FIN DE SESSION")