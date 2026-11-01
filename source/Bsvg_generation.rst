``<svg_generation>``
==========================

Permet d'identifier le fichier XML comme un fichier valide pour le Soft Vertex Generator.

**Balise obligatoire**

``type``
---------------
    Définit le thème à utiliser pour le plan. **Obligatoire**

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

``color``
------------
    Définit la couleur de la ligne. **Obligatoire**

    Il existe 19 couleurs pré-définies. Ces couleurs font écho aux couleurs officielles utilisées dans la signalétique d'Île-de-France Mobilités,
    l'autorité organisatrice des transports en Île-de-France.

    Voici les 19 noms de couleurs avec leur valeur correspondante : ::

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

``maxpb``
------------
    *maximum parallele branches*, indique le nombre maximum de branches pouvant être tracées parallèlement. **Obligatoire**

    Cet attribut, bien que vilain, est essentiel pour permettre au Soft Vertex Generator de prendre les écarts horizontaux nécessaires au tracé du plan, mais également
    de régler la largeur maximale du plan généré.

    Par exemple :
    - ``maxpb="1"`` indique que la ligne n'a pas d'embranchement
    - ``maxpb="2"`` indique qu'au maximum, la ligne a deux branches en parallèle (donc au maximum, une seule bifurcation)

    .. note::
        À terme, cette valeur sera calculée automatiquement. Pour le moment, il est nécessaire de le spécifier.

``output``
----------------
    Change le nom du fichier SVG généré. *Optionnel*

    Le nom par défaut est : ``output.svg``

    Par exemple, en indiquant ``output="Plan A.svg"``, le fichier SVG généré sera appelé "Plan A.svg".

    .. note::
        Il peut être utilisé pour changer le dossier où le fichier SVG apparaît après la génération.

``savetime`` *(production)*
----------------
    Permet d'enregistrer automatiquement le fichier XML utilisé pour la génération. *Optionnel*

    .. note::
        On utilise cet attribut pour modifier le dossier mais aussi pour changer le nom du fichier XML (qui est ``bracket.xml`` par défaut).

    .. tip::
        Utiliser ``savetime`` conjointement avec ``output`` !

    Par exemple, je spécifie ``savetime="../Bureau/Dossier des plans/" output="nouveauplan.svg"``. En lançant le Soft Vertex Generator, deux choses se produisent :
    * le fichier SVG généré a pour nom "nouveauplan.svg" à cause de l'attribut ``output``
    * mon fichier XML ``bracket.xml`` a été dupliqué; la copie se nomme **nouveauplan.xml** et se situe dans le dossier "Dossier des plans" sur mon Bureau.

``cwidth``
----------------
    Change la largeur du fichier SVG généré. *Optionnel*

    Par défaut, le fichier SVG a une largeur de 500.

    Peut-être utile si certains arrêts ont des noms très longs. A priori, pour les branches multiples, le Soft Vertex Generator gère de lui-même la largeur.

    Ne pas mettre d'unité. Par exemple : ``cwidth="1000"``.