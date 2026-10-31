Rédiger le fichier XML
=============================

Le Soft Vertex Generator contient un fichier nommé ``bracket.xml``. C'est à partir de ce fichier que sont générés les plans de ligne.
Il faut donc **modifier le fichier ``bracket.xml``** pour obtenir le plan que l'on souhaite.

Dans cette page, vous allez découvrir comment éditer ce fichier.

Quelques rappels sur le XML
--------------------------------

.. note::
    Vous pouvez créer un fichier XML avec un éditeur complexe tout comme avec votre bloc-notes par défaut !

Le fichier à modifier est rédigé en **XML**. C'est une façon particulière d'écrire les éléments.

En XML, on utilise des **balises**. Il existe deux types de balises :
- les **balises ouvrante et fermante** : ils sont de la forme ``<balise>`` et ``</balise>``.
  On peut écrire du texte entre les deux balises ou mettre d'autres balises.
- les **balises auto-fermantes** : ils sont de la forme ``<balise/>``

.. tip::
    Pour différencier les types de balises, repérez la position du slash (``\``) !

Contrairement à d'autres langages, le XML **n'impose pas** le nom des balises : on peut tout utiliser !

Par exemple, on peut rédiger sa liste de courses en XML (et en français !) sans aucun problème :

.. code-block:: xml

    <ma_liste_de_courses>
        <important>
            <note>à acheter en priorité</note>
            <œufs/>
            <farine/>
        </important>
        <sardines_en_boîte/>
        <huile/>
    </ma_liste_de_courses>

.. tip::
    Remarquez comment nous avons indenté les balises. Ce n'est pas obligatoire en XML mais ça facilite grandement la visibilité pour nous les humains !

Il est également possible d'ajouter des **attributs**. Un attribut permet de donner des informations supplémentaires sur une balise.
Les attributs ont l'avantage d'être utilisables pour tous les types de balises.

Un attribut s'écrit **dans la balise, après le nom** est se présente sous la forme suivante : ``<balise attribut="valeur">``.
Comme les balises, le XML n'impose pas le nom des attributs.

Reprenons l'exemple de notre liste de courses précédente :

.. code-block:: xml

    <ma_liste_de_courses>
        <important>
            <note>à acheter en priorité</note>
            <œufs nombre="60" format="2 plaquettes de 30"/>
            <farine nombre_de_paquets="3"/>
        </important>
        <sardines_en_boîte precision="à l'huile de tournesol"/>
        <huile volume="3L"/>
    </ma_liste_de_courses>

Et voilà ! Vous avez désormais les bases pour rédiger votre premier XML !

Rédiger son premier ``bracket.xml``
-----------------------------------

Si le XML n'impose rien sur les noms des balises et des attributs, le Soft Vertex Generator **attend une organisation bien spécifique** pour fonctionner correctement.

.. important::
    En théorie, vous pouvez toujours donner les noms que vous souhaitez aux balises et attributs.

    En pratique, les noms non reconnus par le Soft Vertex Generator seront ignorés ou provoqueront une erreur.

Nous allons donner les règles importantes à respecter pour une génération réussie !

Je suis un XML
^^^^^^^^^^^^^^^^

Tout fichier XML quel qu'il soit débute par la **balise spéciale** suivante : ``<?xml version="1.0" encoding="UTF-8"?>``. Les fichiers que nous allons écrire ne font pas exception.

La balise préliminaire
^^^^^^^^^^^^^^^^^^^^^^^^

Les fichiers XML destinés au Soft Vertex Generator doivent **commencer par la balise ``<svg_generation>``**. Cette balise indique au Soft Vertex Generator que le fichier XML est
conforme aux règles.

.. code-block:: xml

    <svg_generation>
    </svg_generation>

C'est aussi grâce à cette balise que nous allons fournir les paramètres globaux pour notre génération.

Il y a trois **paramètres obligatoires** à spécifier, sinon quoi, le Soft Vertex Generator renverra une erreur. Ces paramètres doivent être renseignés sous forme d'**attributs** à la balise ``<svg_generation>``.

**type**
""""""""""""""
    L'attribut **type** permet de définir le thème du plan.

    Un thème est une manière de représenter la ligne; par exemple, le thème TRAM produit un trait rayé pour représenter la ligne tandis que le thème RER augmente la largeur du trait.

    Actuellement, il existe quatre thèmes supportés :
    * le thème RER
    * le thème METRO
    * le thème TRAM
    * le thème BUS

    Un cinquième thème sera disponible ultérieurement (le thème VELO).

    Le nom du thème est à indiquer tel quel. Par exemple : ``type="METRO"``

    .. note::
        Certaines options ne sont disponibles que sur certains thèmes. Choisir son thème définit donc également les possibilités de représentation.

    .. important::
        Dans le cadre de l'IDFMwiki, il existe des :ref:`conventions <conv_theme>` pour le thème à choisir selon la ligne représentée.

    Il est également possible de construire son propre thème mais cela demande des connaissances sur le SVG et sur la librairie ``xml.etree`` utilisée.

**color**
""""""""""""""
    L'attribut **color** permet de définir la couleur utilisée pour tracer la ligne.

    Il existe **19 couleurs pré-définies** qui peuvent être utilisées directement. Ces couleurs font écho aux couleurs officielles utilisées dans la signalétique d'Île-de-France Mobilités,
    l'autorité organisatrice des transports en Île-de-France.

    Voici les 19 noms de couleurs avec leur valeur correspondante :::

        'rouge_coquelicot':'#FF1400',
        'orange':'#FF5A00',
        'jaune_vif': '#FFBE00',
        'jaune_ocre':'#DC9600',
        'marron': '#6E491E',
        'olive_clair': '#D2D200',
        'olive_fonce': '#6E6E00',
        'vert_fonce': '#00643C',
        'vert_clair': '#82DC73',
        'turquoise': '#00A092',
        'bleu_clair': '#82C8E6',
        'bleu_outremer':'#0055C8',
        'bleu_fonce':'#0055C8',
        'violet':'#640082',
        'magenta':'#A0006E',
        'lilas':'#D282BE',
        'rose':'#FF82B4',
        'rouge_framboise':'#A50034',
        'bleu_nuit':'#0A0082'

    Les underscores (tirets du 6) font partie du nom de la couleur. Par exemple : ``color="bleu_outremer"``

    .. important::
        Dans le cadre de l'IDFMwiki, il existe des :ref:`conventions <conv_color>` pour la couleur à choisir selon la ligne représentée.

    Il est également possible d'ajouter des :ref:`couleurs supplémentaires <color_lines>`.

**maxpb**
""""""""""
    L'attribut **maxpb** pour *maximum parallele branches* indique au Soft Vertex Generator le nombre maximum de branches pouvant être tracées parallèlement. 

    Cet attribut, bien que vilain, est essentiel pour permettre au Soft Vertex Generator de prendre les écarts horizontaux nécessaires au tracé du plan, mais également
    de régler la largeur maximale du plan généré.

    .. note::
        À terme, cette valeur sera calculée automatiquement. Pour le moment, il est nécessaire de le spécifier.

    Par exemple :
    - ``maxpb="1"`` indique que la ligne n'a pas d'embranchement
    - ``maxpb="2"`` indique qu'au maximum, la ligne a deux branches en parallèle (donc au maximum, une seule bifurcation)

Pour continuer notre exemple, nous allons utiliser la couleur ``jaune_vif`` sur une ligne de métro toute simple : pas d'embranchement.

.. code-block:: xml

    <svg_generation type="METRO" color="jaune_vif" maxpb="1">
    </svg_generation>

.. tip::
    N'oubliez pas d'enregistrer régulièrement votre travail !

Le conteneur
^^^^^^^^^^^^^^^

Ensuite, nous allons utiliser une deuxième balise, **``<line>``**. Cette balise est le conteneur de la structure de notre ligne.

.. code-block:: xml

    <svg_generation type="METRO" color="jaune_vif" maxpb="1">
        <line>
        </line>
    </svg_generation>

.. tip::
    Prenez l'habitude d'indenter (= mettre plusieurs espaces). Ce sera plus facile pour vous repérer et vous relire !

La branche
^^^^^^^^^^^^^^

Chaque branche de la ligne à représenter est associée à une balise **``<branch>``**. Cette balise contiendra tous les arrêts de la branche en question.

.. code-block:: xml

    <svg_generation type="METRO" color="jaune_vif" maxpb="1">
        <line>
            <branch>
            </branch>
        </line>
    </svg_generation>

Les arrêts
^^^^^^^^^^^^^

Un arrêt est matérialisé par une balise **``<stop>``**. Cette balise doit obligatoirement englober deux balises qui permettent de donner les informations cruciales sur l'arrêt :
- la balise ``<name>`` qui indique le nom de l'arrêt
- la balise ``<wikiref>`` : c'est le lien interne vers la page de l'arrêt sur l':ref:`IDFMwiki`.

La balise ``<name>`` contient le nom (sous forme de texte) qui sera affiché pour cet arrêt sur le plan généré.

Puisque le Soft Vertex Generator a été développé dans le cadre de l'IDFMwiki, la balise ``<wikiref>`` est obligatoire, et ce même si votre vertex n'est pas destiné à l'IDFMwiki.
Nous vous recommandons (si ce n'est une obligation) de spécifier ``Accueil`` comme texte pour toutes les balises ``<wikiref>`` de votre fichier XML si votre vertex n'est pas destiné à l'IDFMwiki.

.. attention::
    Si vous spécifiez une valeur aléatoire, par exemple, ``sdbnjsfskjuf``, cela risque de créer la page ``sdbnjsfskjuf`` sur l'IDFMwiki, notamment en cas de clic accidentel sur l'arrêt.

    En spécifiant ``Accueil``, vous supprimez ce risque puisqu'un clic sur l'arrêt renverra seulement sur la page d'accueil de l':ref:`IDFMwiki`.

Si votre vertex est destiné à l'IDFMwiki, le texte à indiquer pour la balise ``<wikiref>`` doit être le nom de la page associée sur l'IDFMwiki **en remplaçant les espaces par un underscore (tiret du 6)**.
Veillez à vérifier le nom de la page, notamment les :ref:`conventions <conv_stop>` de nommage employées dans l'IDFMwiki.

À titre d'exemple, l'arrêt Joliot Curie dans la ville de Gif-sur-Yvette est associée à la page ``Joliot Curie (Gif-sur-Yvette)`` sur l'IDFMwiki.
Dans le fichier XML, on doit donc écrire : ``<wikiref>Joliot_Curie_(Gif-sur-Yvette)</wikiref>``.

Ainsi, a minima, un arrêt est représenté dans notre fichier XML de la manière suivante :

.. code-block:: xml

    <stop>
        <name>Nom de l'arrêt</name>
        <wikiref>la_page_sur_le_wiki</wikiref>
    </stop>

Mais ce n'est pas tout ! On peut également indiquer un **terminus** en spécifiant la valeur ``true`` à l'attribut **``terminus``**. Un graphisme particulier est réservé aux arrêts terminus, qu'ils soient terminus en bout de ligne
ou terminus partiels. Cependant, pour "forcer" la fin de ligne, il faut ajouter un autre attribut : **``curz``**. Avec cet argument, on peut indiquer au Soft Vertex Generator si le terminus correspond au "début" de la ligne (``curz="start"``),
à la "fin" de la ligne (``curz="end"``) ou à un terminus partiel (ne pas utiliser ``curz``). Les notions de "début" et de "fin" font référence à la génération du plan qui est vertical : le début, c'est le haut; la fin, c'est le bas.

Complétons notre exemple avec quelques arrêts aléatoires. Comme les noms d'arrêts sont aléatoires, nous prendrons bien soin de spécifier ``Accueil`` pour les ``<wikiref>``.

.. code-block:: xml

    <svg_generation type="METRO" color="jaune_vif" maxpb="1">
        <line>
            <branch>
                <stop terminus="true" curz="start">
                    <name>Gare Centrale</name>
                    <wikiref>Accueil</wikiref>
                </stop>
                <stop>
                    <name>Paquetta</name>
                    <wikiref>Accueil</wikiref>
                </stop>
                <stop>
                    <name>Pic Grandchamp</name>
                    <wikiref>Accueil</wikiref>
                </stop>
                <stop terminus="true" curz="end">
                    <name>Plage Bleue</name>
                    <wikiref>Accueil</wikiref>
                </stop>
            </branch>
        </line>
    </svg_generation>

Et voilà ! Notre premier ``bracket.xml`` est terminé ! Nous pouvons désormais passer à la génération !

.. note::
    Ce tutoriel donne les bases pour produire un fichier XML correct. Il ne fournit pas l'ensemble des options disponibles.
    Pour cela, renseignez-vous sur les autres pages de la documentation, notamment l'onglet API.