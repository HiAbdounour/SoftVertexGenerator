``<wikiref>``
=====================

Contient la référence de l'arrêt

Cette balise est un **enfant obligatoire** de la balise ``<stop>``.

On indique la page de l':ref:`IDFMwiki` associée à l'arrêt de la manière suivante : ``<wikiref>Nom_de_mon_arrêt</wikiref>``
Le nom de la page doit respecter des :ref:`conventions <conv_stop>`.

.. caution::
    Les espaces doivent être remplacés par des underscores (tirets du 6).
    Le non-respect à cette règle provoque un Warning qui empêche la génération du plan.

    Ce dispositif a été mis en place pour éviter les étourderies et éveiller le fait qu'il y ait des conventions à respecter.