Présentation
===============

Bienvenue dans la documentation officielle du Soft Vertex Generator !

.. note::
    Vous lisez actuellement la documentation pour la version **v1.1.0** !

Dans cette documentation, vous trouverez un guide complet pour utiliser le Soft Vertex Generator, accompagné d'exemples et de ressources intéressantes.
Vous trouverez à la fin toutes les options existantes (onglet *API*).

Une FAQ est également disponible et est complétée au fur et à mesure.

Mais, c'est quoi le Soft Vertex Generator ?
-----------------------------------------------------

Le **Soft Vertex Generator** est un outil permettant de construire facilement des plans de ligne interactif. Il a été conçu dans le cadre du projet `IDFMwiki`_ .
Le principe est de **fournir un fichier XML** décrivant la structure voulue du plan. Le Soft Vertex Generator s'occupe ensuite de la génération du plan de ligne.

Les plans de ligne générés sont **simples**, **verticaux** et **interactifs**; autrement dit, cliquez sur un arrêt permet d'ouvrir la page de l'`IDFMwiki`_ associée à l'arrêt.

Le nom *Soft Vertex Generator* a été trouvé de sorte à rendre compte de ce rôle (en gros, "générateur de vertex simples") mais aussi pour évoquer *SVG*, le format de fichier généré.

Parfois, on abrège le Soft Vertex Generator en **SVG**.

Quelques définitions
----------------------------

**vertex**
""""""""""""
    Un **vertex** est le nom donné aux éléments produits par le Soft Vertex Generator, c'est-à-dire au couple (fichier SVG,ImageMap).

**ImageMap**
""""""""""""""
    L'**ImageMap** est le format spécial utilisé par MediaWiki (le moteur derrière Wikipedia et l'IDFMwiki) pour rendre une image interactive.



.. Barre latérale de navigation

.. toctree::

    index
    install

.. toctree::
    :caption: Créer son premier vertex

    fichierxml
    generation
    wikimport

.. toctree::
    :caption: Personnaliser son vertex

    themes
    colors

.. toctree::
    :caption: Pour aller plus loin

    inout
    escape
    autosave
    conv

.. toctree::
    :caption: Ressources utiles

    examples
    help
    links

.. toctree::
    :caption: API

    Bsvg_generation
    Bline
    Bbranch
    Bbranches
    Bloop
    Bloopup
    Bloopdown
    Bstop
    Bname
    Bwikiref
    Babove
    Bnote
    Bunder


.. Liens utiles et définis
    pour toutes les pages

.. _IDFMwiki: https://idfmwiki.miraheze.org