``<branches>``
======================

Représente une bifurcation ou un embranchement.

Cette balise est à ajouter en cas de besoin selon la ligne. Elle est un enfant de la balise ``<line>`` ou de la balise ``<branches>``.

.. attention::
    La balise ``<branches>`` admet EXACTEMENT **deux** enfants. Ces enfants peuvent être des balises ``<branch>`` et/ou ``<branches>``.
    Le non-respect à cette règle entraîne une erreur.

*Cette balise n'attend pas des attributs. Les attributs spécifiés seront simplement ignorés.*