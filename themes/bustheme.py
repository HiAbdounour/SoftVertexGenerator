"""
BUS THEME
Le thème utilisé pour les lignes de bus.
"""
from typing import Literal
from xml.etree.ElementTree import Element
from core.utils import xml_characters


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

def terminus(cx:int,cy:int,dx:int,clr:str,isOp:bool):
    """
    Un terminus de ligne de bus
    """
    color = "#9e9e9e" if isOp else clr
    return f'<circle cx="{cx+dx}" cy="{cy}" r="8" fill="white" stroke-width="1" stroke="black"/>\n<circle cx="{cx+dx}" cy="{cy}" r="5" fill="{color}" stroke-width="1" stroke="black"/>'

def unidirectional_terminus(cx:int,cy:int,dx:int,direction:Literal['up','down'],clr:str,isOp:bool):
    """
    Un terminus desservi uniquement dans un seul sens
    """
    if direction=='up':
        tri = f"{cx-5+dx},{cy-10} {cx+5+dx},{cy-10} {cx+dx},{cy-20}"
    elif direction=='down':
        tri = f"{cx-5+dx},{cy+10} {cx+5+dx},{cy+10} {cx+dx},{cy+20}"
    else:
        raise ValueError(f"Direction {direction} is not valid. Please state 'up' or 'down' or use the terminus() function instead.")

    return f'<polygon points="{tri}" fill="black"/>\n{terminus(cx,cy,dx,clr,isOp)}'

def stop_name(cx:int,cy:int,step:int,txt:str,link:str,bold:bool,NB:str|None):
    """
    Ajouter le nom de l'arrêt avec un lien vers sa page wiki
    Le paramètre NB permet d'ajouter un Nota Bene (une note)
    """
    bx = 'font-weight:800;' if bold else ""
    if NB is None:
        addum = ""
    else:
        addum = f'<text x="{cx+step}" y="{cy+25}" style="cursor:pointer;{bx};font-style:italic;font-size:12px;">({xml_characters(NB)})</text>'
    return f'<a href="https://idfmwiki.miraheze.org/wiki/{xml_characters(link)}" target="_self">\n<text x="{cx+step}" y="{cy+6}" style="cursor:pointer;{bx}">{xml_characters(txt)}</text>{addum}\n</a>'

def crosssection(cx:int,cy:int,dx:int,clr:str,from_active:bool=False,to_active:bool=False):
    """
    Construis une bifurcation entre deux branches
    >> from : la bifurcation passe de deux branches à une branche (regroupement)
    >> to : la bifurcation passe d'une branche à deux branches (séparation)
    """
    AX = cx-7+dx
    AY = cy
    if to_active:
        ddd = -1
    elif from_active:
        ddd = 1
    else:
        raise RuntimeError('from or to crosssection ?')
    p = f'<polygon points="{AX+14},{AY} {AX},{AY} {AX+16},{AY+20*ddd} {AX+30},{AY+20*ddd} {AX+46},{AY} {AX+32},{AY} {AX+23},{AY+10*ddd}" fill="{clr}"/>'
    return p


#### CONTROLE
def bus_generator(line:Element[str],clr:str,output:str,maxpb:int,sub:bool=False,presety:int|None=None,way:Literal["from",'to']|None=None,width:int=500):
    """
    Génère le SVG selon le thème BUS
    """
    # GLOBAL PARAMETERS
    SVG = ""
    J = presety if presety is not None else 25
    dTEXT = 45*(maxpb-1)

    # Disjonction de cas : <branch> ou <branches> ou <loop>
    for cmpx in range(len(line)):
        cpmxtag = line[cmpx].tag

        # balise <branch>
        if cpmxtag == 'branch':
            dx = 15*(maxpb-1)
            if sub and cmpx%2==0:
                dx-=15
            if sub and cmpx%2==1:
                dx+=15
            if not sub:
                A,dj = unibranch_generator(line[cmpx],clr,dx,J,dTEXT)
                SVG = SVG+'\n'+A
                J = dj+25
            else:
                if (cmpx==0 and way=='to') or (cmpx==1 and way=='from'):
                    cur = 0 if way=='to' else 1
                    A,dj = unibranch_generator(line[cur],clr,dx,J,dTEXT)
                    SVG = SVG+'\n'+A
                    if way=='from':
                        J+=len(line[cur])*50
                elif (cmpx==1 and way=='to') or (cmpx==0 and way=='from'):
                    cur = 1 if way=='to' else 0
                    oth = (cur+1)%2
                    if way=='from':
                        A,dj = unibranch_generator(line[cur],clr,dx,J,dTEXT)
                        SVG = SVG+'\n'+A
                        J+=dj-25 # why?
                    for i in range(len(line[oth])):
                        A = tranch(15,J+i*50,clr,dx,None)
                        SVG = SVG+'\n'+A
                    if way=='to':
                        A,dj = unibranch_generator(line[cur],clr,dx,J+len(line[oth])*50,dTEXT)
                        SVG = SVG+'\n'+A
                        J+=dj
                else:
                    if way in ['from','to']:
                        raise AttributeError(f"A <branches> tag can only have 2 children, not {len(line)}")
                    raise AttributeError(f'{way} is an invalid value for way. Can only accept "from" or "to".')

        # balise <branches>
        elif cpmxtag == "branches":

            # la bifurcation
            dx = 15*(maxpb-1)-1
            if cmpx!=0 and line[cmpx-1].tag=='branch':
                A = crosssection(0,J-30,dx,clr,to_active=True)
                way = 'to'
                SVG = SVG+A
                J-=6
            elif cmpx!=len(line)-1 and line[cmpx+1].tag=='branch':
                # la crosssection vient plus loin
                way = 'from'
            else:
                raise AttributeError("A <branches> tag cannot follow another <branches> tag")
            # les sous-branches
            A,dj = bus_generator(line[cmpx],clr,output,maxpb,True,J,way=way)
            SVG = SVG+'\n'+A
            J+=dj
            # crosssection pour les "from"
            if cmpx!=len(line)-1 and line[cmpx+1].tag=='branch':
                A = crosssection(0,J-50,dx,clr,from_active=True)
                SVG = SVG+'\n'+A
                J-=6

        # balise <loop>
        elif cpmxtag == "loop":
            # checkings complets
            if len(line[cmpx])!=2:
                raise AttributeError("<loop> tags must exactly have 2 children !")
            for loopchild in line[cmpx]:
                if loopchild.tag != "loopup" and loopchild.tag != "loopdown":
                    raise AttributeError("A <loop> tag was found with unauthorized children.")

            loop1 = line[cmpx][0]
            loop2 = line[cmpx][1]

            # crosssection "to"
            dx = 15*(maxpb-1)-1
            A = crosssection(0,J-30,dx,clr,to_active=True)
            SVG = SVG+A
            J-=6

            # première balise :: ATTENTION ! <loopup><loopdown> et <loopdown><loopup> donnent des résultats différents !
            dx = 15*(maxpb-1)-15
            fway = "up" if loop1.tag=="loopup" else "down"
            A,dj = unibranch_generator(loop1,clr,dx,J,dTEXT,fway)
            SVG = SVG+'\n'+A
            for i in range(len(loop2)):
                A = tranch(15,dj+i*50,clr,dx,None)
                SVG = SVG+'\n'+A

            # seconde balise :: ATTENTION ! <loopup><loopdown> et <loopdown><loopup> donnent des résultats différents !
            dx = 15*(maxpb-1)+15
            fway = "up" if loop2.tag=="loopup" else "down"
            for i in range(len(loop1)):
                A = tranch(15,J+i*50,clr,dx,None)
                SVG = SVG+'\n'+A
            A,dj = unibranch_generator(loop2,clr,dx,dj,dTEXT,fway)
            SVG = SVG+'\n'+A
            J = dj+25

            # crosssection "from"
            dx = 15*(maxpb-1)-1
            A = crosssection(0,J-50,dx,clr,from_active=True)
            SVG = SVG+'\n'+A
            J-=6


        # balise non reconnue
        else:
            raise AttributeError(f"Unrecognised <{cpmxtag}> tag !")

    # enregistrement
    if not sub:
        save_file(SVG,output,J,width)
        return (None,None)
    else: # cas des sous-branches
        return (SVG,J)

def save_file(SVG:str,output:str,J:int,width:int):
    """
    S'occupe de l'enregistrement du fichier .svg
    """
    # Headers
    HEADER1 = '<?xml version="1.0" encoding="UTF-8"?>\n'
    HEADER2 = f'<svg width="{width}" height="{J+10}" xmlns="http://www.w3.org/2000/svg">\n<style>\ntext{{\n\tfont-family: sans-serif;\n}}\n</style>'

    # Enregistrement
    with open(output,"w") as svgfile:
        svgfile.write(HEADER1+HEADER2+SVG+'\n</svg>')
    return


def unibranch_generator(branch:Element[str],clr:str,dx:int,j:int,dTEXT:int,forceway:Literal['up','down']|None=None):
    """
    Génère une seule branche pour le thème BUS
    """
    # Paramètres
    BUILD = ""
    i = 15
    TEXT_STEP = 15+dTEXT

    # Corps
    for x in range(len(branch)):
        stopx = branch[x]
        stopx_name = stopx.find('.//name')
        stopx_ref = stopx.find('.//wikiref')
        if stopx_ref is None or stopx_name is None:
            raise Warning(f"Missing info for stop number {x+1}")
        stopx_name = stopx_name.text
        stopx_ref = stopx_ref.text
        if stopx_ref is None or stopx_name is None:
            raise Warning(f"Missing info for stop number {x+1}")
        if ' ' in list(stopx_ref):
            raise Warning(f"Link for stop number {x+1} contain spaces. Make sure wikiref tags respect the MediaWiki links syntax")
        stopx_curz = stopx.get('curz')

        BUILD = BUILD + '\n' + tranch(i,j,clr,dx,stopx_curz) + '\n'

        term = stopx.get("terminus")=='true'
        if forceway is None:
            uni = stopx.get("only")
        else:
            uni = forceway
        op = stopx.get('isOp')=='true'
        stopx_note = stopx.find('.//note')
        if stopx_note is not None:
            stopx_note = stopx_note.text

        if term and uni is None:
            BUILD = BUILD + terminus(i,j,dx,clr,op)
        elif term:
            BUILD = BUILD + unidirectional_terminus(i,j,dx,uni,clr,op)
        elif uni is None:
            BUILD = BUILD + stop(i,j,dx)
        else:
            BUILD = BUILD + unidirectional_stop(i,j,dx,uni)
        BUILD = BUILD + '\n' + stop_name(i,j,TEXT_STEP,stopx_name,stopx_ref,term,stopx_note)

        j+=50

    return (BUILD,j)
