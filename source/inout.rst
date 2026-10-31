Configuration des entrée et sortie
============================================

Le Soft Vertex Generator vous offre la possibilité de changer l'entrée et la sortie du flux habituel.

L'entrée : c'est le fichier utilisé par le Soft Vertex Generator pour générer le plan interactif. Par défaut, ce fichier est ``bracket.xml``.

La sortie : c'est le nom du fichier SVG généré. Par défaut, ce nom est ``output.svg``.

Changer l'entrée
------------------------

Pour changer le nom du fichier de référence, il faut **modifier la variable ``REF``** dans le fichier ``main.py`` (celui exécuté pour lancer la génération).

.. code-block:: python
    :linenos:

    # fichier main.py
    from core.xmlparser import xmlparser
    from core.imap import imap_converter

    REF = "bracket.xml" # ← modifier ici
    FOS = xmlparser(REF)

Remplacez ``bracket.xml`` par le nom de votre fichier XML.

Changer la sortie
---------------------------

Changer le nom du fichier SVG généré est beaucoup plus simple : indiquez le nom que vous souhaitez donner à votre fichier comme **valeur de l'attribut ``output``**
de la balise ``<svg_generation>``.

.. important::
    Le nom du fichier texte de sauvegarde de l'ImageMap est aussi modifié !

Par exemple, si je veux que mon fichier SVG ait pour nom "Mon super plan.svg", alors j'écris :

.. code-block:: xml

    <svg_generation type="METRO" color="jaune_vif" maxpb="1" output="Mon super plan.svg">
        ...
    </svg_generation>

.. tip::
    Avec ``output``, vous pouvez aussi faire en sorte que le plan SVG apparaîsse dans un autre dossier que celui du projet.