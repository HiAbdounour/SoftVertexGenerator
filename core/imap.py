import xml.etree.ElementTree as xET

def imap_converter(filename:str):
    """
    Convertit le plan SVG généré en un couple (plan PNG,ImageMap) plus facilement compatible
    avec MediaWiki
    """
    try:
        errflag = False

        # ouverture du SVG (comme fichier XML)
        root = xET.parse(filename).getroot()
        if root.tag!='svg':
            raise AttributeError

        # conversion en PNG
        png_converter(filename)

        # conversion en ImageMap
        imap = imap_builder(root,filename)

    except AttributeError:
        errflag = True
        raise FileExistsError("A problem occured with the file.\nPlease remember to not alter the generated SVG while the process is still running.")

    except Exception as err:
        errflag = True
        raise err

    else:
        print(f"\nFichier PNG prêt. Voici votre ImageMap :")
        print(imap)

    finally:
        if errflag:
            print("An error occured but your SVG was already generated.")
        


def png_converter(filename:str):
    """
    Convertit l'image SVG en image PNG
    """
    # actuellement pas de support (monde PyPI pas encore à la hauteur)
    # on se reposera sur une conversion via un outil externe
    print("=======================")
    print("ATTENTION !")
    print("Un outil n'est pas encore disponible : png_converter()")
    print("Vous devez donc obligatoirement convertir VOUS-MÊMES votre plan SVG en image PNG.")
    print("Vous pouvez utiliser des outils de conversion en ligne.")
    print("=======================")
    return

def imap_builder(svg:xET.Element,filename:str):
    """
    Construit l'ImageMap à partir du fichier SVG parsé
    """
    CORPUS = ""

    # en-tête
    FRONT = f'File:{filename.split('.')[0]}.png|alt=Plan pour {{PAGENAME}}'

    # corps
    i = 0
    while i<len(svg):
        x = svg[i]
        if x.tag=='circle' and x.get('fill')=='white':
            CORPUS = CORPUS+f'\ncircle {x.get('cx')} {x.get('cy')} {x.get('r')}'
            if svg[i+1].tag=='a':
                i+=1
                href = svg[i+1].get('href')
                txt = svg[i+2].text
                txt_dim = [svg[i+2].get('x'),svg[i+2].get('y')]
            elif svg[i+2].tag=='a':
                i+=1
                href = svg[i+2].get('href')
                txt = svg[i+3].text
                txt_dim = [svg[i+3].get('x'),svg[i+3].get('y')]
            else:
                raise AttributeError("Are you sure the SVG file was not altered ?")
            if href is None or txt is None or txt_dim[0] is None or txt_dim[1] is None:
                raise AttributeError("Are you sure the SVG file was not altered ?")
            CORPUS = CORPUS+f' [[{href.split('/')[-1]}|{txt}]]'
            CORPUS = CORPUS+f'\nrect {txt_dim[0]} {txt_dim[1]} 500 {int(txt_dim[1])+12} [[{href.split('/')[-1]}|{txt}]]'

    # renvoi formatté
    return f"<imagemap>\n{FRONT}\n{CORPUS}</imagemap>"
