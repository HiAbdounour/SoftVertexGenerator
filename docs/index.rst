.. Soft Vertex Generator documentation master file, created by
   sphinx-quickstart on Sun Aug 30 16:15:49 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Soft Vertex Generator
===================================

Le Soft Vertex Generator est un outil de génération de plans de ligne verticaux, interactifs et simples, au format SVG.

Le Soft Vertex Generator (abrégé SVG – oui c'est un jeu de mots –) a été avant tout développé dans le cadre du projet `IDFMwiki`_.
Grâce au Soft Vertex Generator, vous pourrez concevoir des plans simples, accessibles aux utilisateurs mobiles. Ces plans seront interactifs dans la mesure où chaque arrêt est un lien vers une page du wiki. Vous pourrez également personnaliser votre wiki.

Le Soft Vertex Generator vous permet de vous simplifier la vie, en gérant toutes les productions artistiques automatiquement ! Tout ce que vous avez à faire, c'est lister tous les arrêts dans un fichier XML. Et c'est tout !

Alors, êtes-vous prêts à créer des SVG avec SVG ?

=======================================
Mais, c'est quoi un vertex au juste ?
=======================================

Un **vertex** est un couple de deux informations :
- un document image (PNG ou SVG) qui correspond à votre plan de ligne
- une couche de liens appelée :code:`ImageMap` qui permet de rendre votre plan interactif

Le Soft Vertex Generator propose donc de produire ces deux éléments pour une intégration facilitée dans l'IDFMwiki.

.. tip::
   Vous pouvez consulter des exemples de plans de ligne produits directement sur l':ref:`_IDFMwiki`.

=======================================
Commencer à concevoir son premier vertex
=======================================
- :ref:`Obtenir le SVG _installguide`
- :ref:`Rédiger le fichier XML _redactxml`
- :ref:`Lancer la génération _launch_gen`
- :ref:`Importer dans l'IDFMwiki _importwiki`


.. _IDFMwiki: https://idfmwiki.miraheze.org
.. _repo GitHub: https://github.com/HiAbdounour/SoftVertexGenerator

.. toctree::
   :maxdepth: 3

   :ref:`Obtenir le SVG _installguide`
   Créer son premier vertex
      :ref:`Rédiger le fichier XML _redactxml`
      :ref:`Lancer la génération _launch_gen`
      :ref:`Importer dans l'IDFMwiki _importwiki`
   Personnaliser son vertex
      :ref:`Thèmes de ligne _thememainpage`
      :ref:`Couleurs de ligne _colors`
      :ref:`Liens hypertextes vers l'IDFMwiki _lienwiki`
   :ref:`Ressources utiles _ressources`
   :ref:`Exemples de fichiers XML _exagogo`
   :ref:`Comment faire pour ? _more`
   :ref:`FAQ _faq`
   :ref:`Licence et utilisation commerciale _licence`