.. _color_lines:
Couleurs de ligne
=====================

Le Soft Vertex Generator fournit **19 couleurs** pour la génération du plan de ligne. Ces 19 couleurs sont tirées de la charte graphique officielle
d'Île-de-France Mobilités, autorité organisatrice des transports en Île-de-France.

Ces 19 couleurs sont les suivantes : ::

    'rouge_coquelicot':'#FF1400',
    'orange':'#FF5A00',
    'jaune_vif': '#FFBE00',
    'jaune_ocre':'#DC9600',
    'marron': '#6E491E',
    'olive_clair': '#D2D200',
    'olive_fonce': '#6E6E00',
    'vert_fonce': '#00643C',
    'vert_clair': '#82DC73',
    'turquoise': '#00A092',
    'bleu_clair': '#82C8E6',
    'bleu_outremer':'#0055C8',
    'bleu_fonce':'#0055C8',
    'violet':'#640082',
    'magenta':'#A0006E',
    'lilas':'#D282BE',
    'rose':'#FF82B4',
    'rouge_framboise':'#A50034',
    'bleu_nuit':'#0A0082'

Vous avez toutefois la possibilité d'ajouter de nouvelles couleurs.

Pour cela, repérez le fichier **``constants.py``**, situé dans le dossier ``constants``. Vous trouverez la liste des couleurs définies sous forme de dictionnaire et stockée dans
la variable ``IDFM_COLORS``. Ajoutez vos couleurs dans ce dictionnaire pour pouvoir les utiliser.

.. tip::
    Il faut donc un nom et une valeur en code RGB hexadécimal. Le nom que vous donnez à cette couleur est le nom à utiliser dans votre fichier XML.
