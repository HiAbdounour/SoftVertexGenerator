Importer dans l'IDFMwiki
=================================

.. note::
    Il est nécessaire d'avoir le vertex complet, c'est-à-dire le fichier SVG **ET** l'ImageMap.

Si vous souhaitez importer votre vertex dans l':ref:`IDFMwiki`, il faut réaliser deux étapes + une.

Première étape : importer le fichier SVG
---------------------------------------------

Le fichier SVG généré doit être présent dans l'IDFMwiki. Pour cela, rendez vous sur la `page de téléversement de l'IDFMwiki <https://idfmwiki.miraheze.org/wiki/Spécial:Téléverser>`__
et déposez votre fichier SVG. La licence à choisir est ``CC BY-SA 4.0 avec attribution à la communauté IDFMwiki``.

.. attention::
    Ne modifiez pas le nom du fichier SVG une fois généré, y compris dans l'IDFMwiki. L'ImageMap est relié au fichier SVG par son nom !

Deuxième étape : renseigner l'ImageMap
-------------------------------------------

Consultez ensuite la page où vous souhaitez insérer le plan interactif.

Pour insérer le plan interactif, utilisez le modèle ``{{DoublePlans}}`` ou ``{{OnlySVG}}``. Ces deux modèles contiennent un paramètre ``imap`` réservé pour l'ImageMap.
Collez l'ImageMap obtenu comme valeur pour ce paramètre.

.. tip::
    Pour savoir lequel des deux modèles utilisé, référez-vous à la `documentation du wiki <https://idfmwiki.miraheze.org/wiki/Modèle:OnlySVG/doc#Lequel%20utiliser%20?>`__.

Troisième étape : Conserver le fichier XML
---------------------------------------------------

Afin de faciliter les opérations de maintenance et les modifications en cas d'erreurs, nous vous recommandons de **téléverser le fichier XML dans ce ``dossier <https://github.com/HiAbdounour/SoftVertexGenerator_IDFM>``__**.
Cette opération nécessite un compte sur GitHub (il faut ouvrir une Pull Request). Si vous ne voulez pas en créer un, vous pouvez partager le fichier XML sur le Discord officiel de l':ref:`IDFMwiki` ou à quelqu'un qui veut bien le faire pour vous.

