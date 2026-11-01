``<loopdown>``
================

.. note::
    Balise inutilisable avec le thème RER

Contient les arrêts d'une boucle desservie vers le terminus du bas.

**Balise obligatoire si ``<loop>`` est utilisé**. Elle est un enfant de la balise ``<loop>``.

*Cette balise n'attend pas des attributs. Les attributs spécifiés seront simplement ignorés.*

La balise ``<loopdown>`` gère automatiquement les noms d'arrêts : pas besoin d'utiliser une balise ``<branch>`` intermédiaire.

.. note::
    Tous les arrêts présents dans la balise ``<loopdown>`` sont automatiquement affectés du sens "down" (vers le bas).