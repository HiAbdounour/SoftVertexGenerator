``<under>``
================

.. note::
    Balise inutilisable avec le thème BUS

    Pour le thème BUS, la balise ``<note>`` remplace la balise ``<under>``. Néanmoins, le paramètre ``cultural`` n'y existe pas.

Affiche du texte en-dessous du nom de l'arrêt.

Cette balise est un *enfant optionnel* de la balise ``<stop>``.

On indique le texte inférieur de la manière suivante : ``<under>Mon texte</under>``

.. note::
    Souvent utilisé pour les notions supplémentaires. Par exemple : "Maison des Examens", "Grande Arche", "Le Mandinet".

``cultural``
--------------
    Indique un lieu culturel. *Optionnel*

    En utilisant cet attribut, le texte en-dessous utilise la signalétique des lieux d'intérêts : texte blanc sur fond marron.

    À spécifier de la sorte : ``<under cultural="true">``