import xml.etree.ElementTree as xET

def imap_converter(filename:str,saving:bool):
    """
    Convertit le plan SVG généré en un couple (plan PNG,ImageMap) plus facilement compatible
    avec MediaWiki
    """
    try:
        errflag = False

        # ouverture du SVG (comme fichier XML)
        root = xET.parse(filename).getroot()
        if root.tag!='{http://www.w3.org/2000/svg}svg':
            raise BufferError # juste pour isoler le comportement (flemme de créer une classe pour ça)

        # conversion en PNG
        png_converter(filename)

        # conversion en ImageMap
        imap = imap_builder(root,filename)

        # sauvegarde
        if saving:
            with open(f"ImageMap_{filename}.txt",'w',encoding='utf-8') as file:
                file.write(imap)

    except BufferError:
        errflag = True
        raise FileExistsError("A problem occured with the file.\nPlease remember to not alter the generated SVG while the process is still running.")

    except Exception as err:
        errflag = True
        raise err

    else:
        print(f"\nFichier PNG prêt.\nVoici votre ImageMap :")
        if saving:
            print(f">>> ImageMap sauvegardé : ImageMap_{filename}.txt")
        else:
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
        if svg[i].tag=='{http://www.w3.org/2000/svg}circle' and svg[i].get('fill')=='white':
            CORPUS = CORPUS+f'\ncircle {svg[i].get('cx')} {svg[i].get('cy')} {svg[i].get('r')}'
            if svg[i+1].tag=='{http://www.w3.org/2000/svg}a':
                href = svg[i+1].get('href')
                txt = svg[i+1][0].text
                txt_dim = [svg[i+1][0].get('x'),svg[i+1][0].get('y')]
                i+=2
            elif svg[i+2].tag=='{http://www.w3.org/2000/svg}a':
                href = svg[i+2].get('href')
                txt = svg[i+2][0].text
                txt_dim = [svg[i+2][0].get('x'),svg[i+2][0].get('y')]
                i+=3
            else:
                i+=1
                continue
            if href is None or txt is None or txt_dim[0] is None or txt_dim[1] is None:
                raise AttributeError("Are you sure the SVG file was not altered ?")
            CORPUS = CORPUS+f' [[{href.split('/')[-1]}|{txt}]]'
            CORPUS = CORPUS+f'\nrect {txt_dim[0]} {txt_dim[1]} 500 {int(txt_dim[1])+12} [[{href.split('/')[-1]}|{txt}]]'
        else:
            i+=1

    # renvoi formatté
    return f"<imagemap>\n{FRONT}\n{CORPUS}</imagemap>"
