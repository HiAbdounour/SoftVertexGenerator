``<loop>``
================

.. note::
    Balise inutilisable avec le thème RER

Représente une boucle.

Cette balise est à ajouter en cas de besoin selon la ligne. Elle est un enfant de la balise ``<line>``.

.. attention::
    La balise ``<loop>`` admet EXACTEMENT **deux** enfants bien défini : un ``<loopup>`` et un ``<loopdown>``.
    Le non-respect à cette règle entraîne une erreur.

*Cette balise n'attend pas des attributs. Les attributs spécifiés seront simplement ignorés.*

La balise ``<loop>`` gère automatiquement les espacements.

Importance du sens
--------------------------
Notez que le code suivant 

.. code-block:: xml

    <loop>
        <loopup>
            ...
        </loopup>
        <loopdown>
            ...
        </loopdown>
    </loop>

ne produit pas le même résultat que celui-ci

.. code-block:: xml

    <loop>
        <loopdown>
            ...
        </loopdown>
        <loopup>
            ...
        </loopup>
    </loop>

Entre ``<loopup>`` et ``<loopdown>`` : la première des deux rencontrée sera affichée en premier et sur la branche gauche de la boucle, tandis que la deuxième sera affichée
ensuite et sur la branche droite de la boucle.