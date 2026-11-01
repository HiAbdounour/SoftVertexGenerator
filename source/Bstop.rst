``<stop>``
================

Représente un arrêt

**Balise devant être présente au moins une fois**

Cette balise est un enfant de la balise ``<branch>``, de la balise ``<loopup>`` ou de la balise ``<loopdown>``.

``terminus``
---------------
    Indique un terminus. *Optionnel*

    Spécifier un arrêt en tant que terminus permet de faire ressortir l'arrêt grâce à un graphisme particulier et à un nom d'arrêt en gras.

    Il s'indique de la manière suivante : ``<stop terminus="true">``

``curz``
--------------
    Stoppe la ligne. *Optionnel*

    Cet attribut permet de raccourcir la ligne. Il est à utiliser conjointement avec l'attribut ``terminus`` lorsque la ligne ne continue pas au-delà
    de ce terminus.

    Il y a deux valeurs possibles :
    * ``start``, si le terminus est situé en haut de la branche
    * ``end``, si le terminus est situé en bas de la branche

    Il s'utilise comme ceci : ``<stop terminus="true" curz="start">``

``isOp``
--------------
    .. note::
        Balise présente uniquement pour les thèmes BUS et METRO

    Indique un terminus opérationnel. *Optionnel*

    Un terminus opérationnel est un terminus présent pour des raisons d'exploitation mais où les passagers ne peuvent pas y descendre. Ces derniers descendent à l'arrêt
    précédent, qui est alors le terminus commercial.

    En spécifiant l'arrêt comme étant un terminus opérationnel, une couleur grise sera utilisée pour représenter l'arrêt.

    L'attribut est à utiliser conjointement avec l'attribut ``terminus``, comme ceci : ``<stop terminus="true" isOp="true">``

``only``
--------------
    .. note::
        Balise inutilisable avec le thème RER

    Indique une direction pour un arrêt. *Optionnel*

    Cet attribut est à utiliser pour les arrêts à sens unique (= desservis par un seul sens).
    En rappelant que le plan généré est vertical, il y a deux sens possibles : 
    * ``up``, vers le(s) terminus situé(s) en haut
    * ``down``, vers le(s) terminus situé(s) en bas

    .. tip::
        Si la balise ``<stop>`` est située dans une balise ``<loopup>`` ou ``<loopdown>``, il n'est pas nécessaire d'utiliser l'attribut ``only``.
        Les sens sont automatiquement affectés.

    Exemple d'utilisation : ``<stop only="down">``

``closed``
---------------
    Ferme l'arrêt. *Optionnel*

    En spécifiant que l'arrêt est fermé (= non desservi), une croix rouge est tracée sur l'arrêt.

    L'attribut s'utilise de la sorte : ``<stop closed="true">`` 