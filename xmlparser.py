import xml.etree.ElementTree as xET
from constants import IDFM_COLORS
# les thèmes
from bustheme import bus_generator


def xmlparser(input_file:str):
    try:
        # vérifie que c'est correct
        root = xET.parse(input_file).getroot()
        if root.tag!='svg_generation':
            raise FileExistsError("The file is not understable. Format SoftVertexGenerator expected.")
        
        # récupère l'output
        output = root.get('output')
        if output is None:
            output = "output.xml"

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

        # récupère l'embedding
        base = root[0]

    except FileExistsError as f3err:
        raise f3err
    except AttributeError as aerr:
        raise aerr
    except Exception:
        raise Exception("An unknown exception occured")
    
    else:
        # la GÉNÉRATION
        if theme=='bus':        
            bus_generator(base,clr,output)
        else:
            raise AttributeError(f"Theme {theme} is not allowed")