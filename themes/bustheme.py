"""
BUS THEME
Le thème utilisé pour les lignes de bus.
"""
from typing import Literal
from xml.etree.ElementTree import Element
from core.constants import CHARACTERS

# Un util
def xml_characters(txt:str):
    """
    Remplace les caractères UTF-8 en trucs &#xxx; compréhensibles en XML
    """
    txtS = list(txt)
    for i in range(len(txtS)):
        if txtS[i] in CHARACTERS.keys():
            txtS[i] = CHARACTERS[txtS[i]]
    return "".join(txtS)

# fin de l'util

def stop(cx:int,cy:int,dx:int):
    """
    Un arrêt de bus normal
    """
    return f'<circle cx="{cx+dx}" cy="{cy}" r="8" fill="white" stroke-width="1" stroke="black"/>'

def unidirectional_stop(cx:int,cy:int,dx:int,direction:Literal['up','down']):
    """
    Un arrêt de bus desservi uniquement dans un seul sens
    """
    if direction=='up':
        tri = f"{cx-5+dx},{cy-10} {cx+5+dx},{cy-10} {cx+dx},{cy-20}"
    elif direction=='down':
        tri = f"{cx-5+dx},{cy+10} {cx+5+dx},{cy+10} {cx+dx},{cy+20}"
    else:
        raise ValueError(f"Direction {direction} is not valid. Please state 'up' or 'down' or use the stop() function instead.")

    return f'<polygon points="{tri}" fill="black"/>\n{stop(cx,cy,dx)}'

def tranch(cx:int,cy:int,clr:str,dx:int,curz:Literal["start","end"]|None):
    """
    Une branche colorée autour de l'arrêt
    """
    if curz is not None:
        if curz=="start":
            val = 25
            dy = 0
        elif curz=='end':
            val = 25
            dy = -25
        else:
            curz = None
    if curz is None:
        val = 50
        dy = -25
    return f'<rect width="14" height="{val}" x="{cx-7+dx}" y="{cy+dy}" fill="{clr}"/>'

def terminus(cx:int,cy:int,dx:int,clr:str):
    """
    Un terminus de ligne de bus
    """
    return f'<circle cx="{cx+dx}" cy="{cy}" r="8" fill="white" stroke-width="1" stroke="black"/>\n<circle cx="{cx+dx}" cy="{cy}" r="5" fill="{clr}" stroke-width="1" stroke="black"/>'

def unidirectional_terminus(cx:int,cy:int,dx:int,direction:Literal['up','down'],clr:str):
    """
    Un terminus desservi uniquement dans un seul sens
    """
    if direction=='up':
        tri = f"{cx-5+dx},{cy-10} {cx+5+dx},{cy-10} {cx+dx},{cy-20}"
    elif direction=='down':
        tri = f"{cx-5+dx},{cy+10} {cx+5+dx},{cy+10} {cx+dx},{cy+20}"
    else:
        raise ValueError(f"Direction {direction} is not valid. Please state 'up' or 'down' or use the terminus() function instead.")

    return f'<polygon points="{tri}" fill="black"/>\n{terminus(cx,cy,dx,clr)}'

def stop_name(cx:int,cy:int,step:int,txt:str,link:str,bold:bool,dx:int):
    """
    Ajouter le nom de l'arrêt avec un lien vers sa page wiki
    """
    bx = 'font-weight:800;' if bold else ""
    return f'<a href="https://idfmwiki.miraheze.org/wiki/{xml_characters(link)}" target="_self">\n<text x="{cx+step+dx}" y="{cy+6}" style="cursor:pointer;{bx}">{xml_characters(txt)}</text>\n</a>'

def crosssection(cx:int,cy:int,dx:int,clr:str,from_active:bool=False,to_active:bool=False):
    """
    Construis une bifurcation entre deux branches
    >> from : la bifurcation passe de deux branches à une branche (regroupement)
    >> to : la bifurcation passe d'une branche à deux branches (séparation)
    """
    AX = cx-7+dx
    AY = cy
    if from_active:
        ddd = -1
    elif to_active:
        ddd = 1
    else:
        raise RuntimeError('from or to crosssection ?')
    p = f'<polygon points="{AX+14},{AY} {AX},{AY} {AX+16},{AY+20*ddd} {AX+30},{AY+20*ddd} {AX+46},{AY} {AX+32},{AY} {AX+23},{AY+10*ddd}" fill="{clr}"/>'
    return p


#### CONTROLE
def bus_generator(line:Element[str],clr:str,output:str,maxpb:int):
    """
    Génère le SVG selon le thème BUS
    """
    # GLOBAL PARAMETERS
    SVG = ""
    J = 25

    # Disjonction de cas : <branch> ou <branches> ou <cross>
    for cmpx in range(len(line)):
        cpmxtag = line[cmpx].tag

        pass

    # Headers
    HEADER1 = '<?xml version="1.0" encoding="UTF-8"?>\n'
    HEADER2 = f'<svg width="500" height="{J+10}" xmlns="http://www.w3.org/2000/svg">\n<style>\ntext{{\n\tfont-family: sans-serif;\n}}\n</style>'

    # Enregistrement
    with open(output,"w") as svgfile:
        svgfile.write(HEADER1+HEADER2+SVG+'\n</svg>')
    return


def unibranch_generator(branch:Element[str],clr:str,output:str,dx:int,j:int):
    """
    Génère une seule branche pour le thème BUS
    """
    # Paramètres
    BUILD = ""
    i = 15
    TEXT_STEP = 15

    # Corps
    for x in range(len(branch)):
        stopx = branch[x]
        stopx_name = stopx[0].text
        stopx_ref = stopx[1].text
        if stopx_ref is None or stopx_name is None:
            raise Warning(f"Missing info for stop number {x}")
        if ' ' in list(stopx_ref):
            raise Warning(f"Link for stop number {x+1} contain spaces. Perhaps you swapped name and wikiref tags")
        stopx_curz = stopx.get('curz')

        BUILD = BUILD + '\n' + tranch(i,j,clr,dx,stopx_curz) + '\n'

        term = stopx.get("terminus")=='true'
        uni = stopx.get("only")
        if term and uni is None:
            BUILD = BUILD + terminus(i,j,dx,clr)
        elif term:
            BUILD = BUILD + unidirectional_terminus(i,j,dx,uni,clr)
        elif uni is None:
            BUILD = BUILD + stop(i,j,dx)
        else:
            BUILD = BUILD + unidirectional_stop(i,j,dx,uni)
        BUILD = BUILD + '\n' + stop_name(i,j,TEXT_STEP,stopx_name,stopx_ref,term,dx)

        j+=50

    return (BUILD,j)
