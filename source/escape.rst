Caractères d'échappement
===============================

Les fichiers XML, les fichiers SVG et les noms de pages sur MediaWiki ont des encodings très différents. MediaWiki est très permissif mais ce n'est
pas le cas des XML et des SVG. Ainsi, il est possible qu'en utilisant le Soft Vertex Generator, vous rencontrez des erreurs dues à un caractère "illicite".

Le Soft Vertex Generator permet de remédier à ces caractères problématiques en remplaçant ces derniers par leur **équivalent HTML**. Concrètement, ça ne change rien pour nous,
mais les programmes manipulant ces caractères comprennent ce qu'ils signifient.

Le Soft Vertex Generator est équipé d'une **liste prédéfinie par les premiers besoins**. Cette liste se situe dans le fichier ``constants.py`` (dans le dossier ``constants``) :
la variable ``XML_ESCAPING``.

Actuellement, cette liste contient les caractères suivants (à gauche le caractère, à droite son équivalent) :::

    "à": "&#224;",
    "á": "&#225;",
    "â": "&#226;",
    "ã": "&#227;",
    "ä": "&#228;",
    "å": "&#229;",
    "æ": "&#230;",
    "ç": "&#231;",
    "è": "&#232;",
    "é": "&#233;",
    "ê": "&#234;",
    "ë": "&#235;",
    "ì": "&#236;",
    "í": "&#237;",
    "î": "&#238;",
    "ï": "&#239;",
    "ñ": "&#241;",
    "ò": "&#242;",
    "ó": "&#243;",
    "ô": "&#244;",
    "õ": "&#245;",
    "ö": "&#246;",
    "ø": "&#248;",
    "œ": "&#339;",
    "ù": "&#249;",
    "ú": "&#250;",
    "û": "&#251;",
    "ü": "&#252;",
    "ý": "&#253;",
    "ÿ": "&#255;",
    "À": "&#192;",
    "Á": "&#193;",
    "Â": "&#194;",
    "Ã": "&#195;",
    "Ä": "&#196;",
    "Å": "&#197;",
    "Æ": "&#198;",
    "Ç": "&#199;",
    "È": "&#200;",
    "É": "&#201;",
    "Ê": "&#202;",
    "Ë": "&#203;",
    "Ì": "&#204;",
    "Í": "&#205;",
    "Î": "&#206;",
    "Ï": "&#207;",
    "Ñ": "&#209;",
    "Ò": "&#210;",
    "Ó": "&#211;",
    "Ô": "&#212;",
    "Õ": "&#213;",
    "Ö": "&#214;",
    "Ø": "&#216;",
    "Œ": "&#338;",
    "Ù": "&#217;",
    "Ú": "&#218;",
    "Û": "&#219;",
    "Ü": "&#220;",
    "Ý": "&#221;",
    "–": "&#8211;",
    "/": "&#47;"

Vous pouvez donc utiliser les caractères précédents sans vous soucier de quoi que ce soit.

Si un caractère problématique particulier n'est pas présent dans cette liste, vous devez l'**ajouter à cette liste**. Pour trouver son équivalent, 
cherchez sur Internet ``code HTML pour <caractère>`` ou ``HTML entity for <caractère>``.