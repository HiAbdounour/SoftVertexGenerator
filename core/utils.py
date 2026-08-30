from constants.constants import XML_ESCAPING,MEDIAWIKI_ESCAPING

def xml_characters(txt:str):
    """
    Remplace les caractères UTF-8 en trucs &#xxx; compréhensibles en XML
    """
    txtS = list(txt)
    for i in range(len(txtS)):
        if txtS[i] in XML_ESCAPING.keys():
            txtS[i] = XML_ESCAPING[txtS[i]]
    return "".join(txtS)

def imap_characters(txt:str):
    """
    Remplace les trucs &#xxx; en caractères compréhensibles par MediaWiki
    """
    txtS = list(txt)
    for i in range(len(txtS)):
        if txtS[i] in MEDIAWIKI_ESCAPING.keys():
            txtS[i] = MEDIAWIKI_ESCAPING[txtS[i]]
    return "".join(txtS)
