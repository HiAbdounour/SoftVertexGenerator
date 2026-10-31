Sauvegarde automatique du XML
===================================

Vous avez la possibilité de **sauvegarder automatiquement votre fichier XML** dans un autre endroit grâce à l'attribut **``savetime``** de la balise ``<svg_generation>``.
Cela peut être très utile si vous êtes amenés à modifier plusieurs fois le même fichier (``bracket.xml`` par exemple) mais que vous souhaitez conserver les fichiers XML de chaque
génération (par exemple, pour le push dans la `base commune <https://github.com/HiAbdounour/SoftVertexGenerator_IDFM>`__).

Par exemple, si vous avez téléchargé le Soft Vertex Generator dans votre dossier Téléchargements et que vous commencez votre fichier XML par 

.. code-block:: xml

    <svg_generation type="METRO" color="jaune_vif" maxpb="1" savetime="../Bureau/">
        ...
    </svg_generation>

alors le fichier SVG sera généré dans votre Bureau.

.. important::
    N'oubliez pas le slash (``\``) à la fin du ``savetime``, sinon vous modifiez le nom de votre fichier !