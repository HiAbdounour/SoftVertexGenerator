Lancer la génération
==========================

*Cette page part du principe que vous avez un fichier ``bracket.xml`` à exploiter.*

Pour lancer la génération du plan interactif, deux possibilités s'offrent à vous : utiliser un IDE ou le terminal de commande.
Les deux options sont détaillées dans la suite.

Générer à partir de l'IDE
-------------------------------

Depuis votre IDE (VS Code, PyCharm, PyDev, etc), lancer l'exécution du fichier **``main.py``**. Puis :ref:`next_event`.


Générer à partir du terminal
--------------------------------

Lancer un terminal de commande (cmd, Powershell, Bash) depuis le dossier du Soft Vertex Generator. Écrivez ensuite ``python main.py``. Puis :ref:`next-event`.

.. _next_event:
La suite des évènements
-----------------------------------

Une fois le fichier exécuté et sous condition que le fichier XML est bien formatté, le fichier SVG généré apparaît directement dans le même dossier que le fichier ``main.py`` (hors personnalisation) avec le nom par défaut ``output.svg``
(ou votre nom personnalisé).

Ensuite, le Soft Vertex Generator vous demande si vous souhaitez l'ImageMap associée au fichier SVG. L'ImageMap est le code qui va permettre de rendre le plan interactif sur l':ref:`IDFMwiki`.
Si vous n'en avez pas besoin, appuyez simplement sur la touche Entrée (ou toute autre touche différente de la lettre ``y``).

Si vous voulez l'ImageMap, appuyez sur la touche **``y``** de votre clavier. Le Soft Vertex Generator vous demande ensuite si vous souhaitez enregistrer ou non l'ImageMap, c'est-à-dire exporter
le code de l'ImageMap dans un fichier texte (extension ``.txt``).

Si vous souhaitez l'enregistrement, pressez la touche ``s``. Un fichier ``ImageMap_output.txt`` (ou ``ImageMap_mon_nom_personnalise.txt``) sera créé avec l'ImageMap à l'intérieur.

Si vous ne souhaitez pas l'enregistrement, cliquez sur Entrée (ou une autre touche différente de la lettre ``s``). L'ImageMap sera alors affichée pour que vous puissez le copier-coller.

Et voilà, vous avez produit votre tout premier vertex !

.. note::
    Si vous voulez importer votre vertex dans l':ref:`IDFMwiki`, lisez la dernière page du tutoriel.