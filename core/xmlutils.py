from constants.constants import CHARACTERS

def xml_characters(txt:str):
    """
    Remplace les caractères UTF-8 en trucs &#xxx; compréhensibles en XML
    """
    txtS = list(txt)
    for i in range(len(txtS)):
        if txtS[i] in CHARACTERS.keys():
            txtS[i] = CHARACTERS[txtS[i]]
    return "".join(txtS)