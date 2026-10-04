import xml.etree.ElementTree as xET
from constants.constants import IDFM_COLORS
# les thèmes
from themes import *


def xmlparser(input_file:str):
    try:
        # vérifie que c'est correct
        root = xET.parse(input_file).getroot()
        if root.tag!='svg_generation':
            raise FileExistsError("The file is not understable. Format SoftVertexGenerator expected.")
        
        # récupère l'output
        output = root.get('output')
        if output is None:
            output = "output.svg"

        # récupère le thème
        theme = root.get('type')
        if theme is None:
            raise AttributeError("Generation type not found. Please provide a type attribute")

        # récupère la couleur
        keyclr = root.get("color")
        if keyclr is None:
            raise AttributeError("Color not found. Please provide a color attribute")
        if keyclr not in IDFM_COLORS.keys():
            raise AttributeError(f"Invalid color : {keyclr} is not a valid IDFM color")
        clr = IDFM_COLORS[keyclr]

        # calcul du nombre maximal de branches parallèles
        # >>> on améliorera la logique pour prendre en compte un vrai calcul
        maxpb = root.get('maxpb')
        if maxpb is None:
            raise AttributeError("maxpb attribute was not found")
        maxpb = int(maxpb)
        if maxpb<=0:
            raise ValueError

        # récupère l'embedding
        base = root[0]

        # recherche de la largeur du SVG
        cwidth = root.get("cwidth")
        if cwidth is None:
            cwidth = 500

        ###" UNIQUEMENT POUR LA PRODUCTION (CONSERVATION HORS BRACKET)"
        try:
            xput = root.get("savetime")
            if xput is not None:
                with open(input_file,'r',encoding='utf-8') as file:
                    data = file.read()
                rahs = output.split('.')
                with open(xput+rahs[0]+'.xml','w',encoding='utf-8') as file:
                    file.write(data)
        except:
            pass

    except FileExistsError as f3err:
        raise f3err
    except AttributeError as aerr:
        raise aerr
    except ValueError:
        raise AttributeError("Cannot convert maxpb into a valid integer")
    except Exception:
        raise Exception("An unknown exception occured")
    
    else:
        # la GÉNÉRATION
        if theme=='BUS':        
            bus_generator(base,clr,output,maxpb,width=int(cwidth))
            return output
        else:
            raise AttributeError(f"Theme {theme} is not allowed")