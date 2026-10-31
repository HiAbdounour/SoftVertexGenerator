Conventions pour l'IDFMwiki
===============================

Si vous générez un vertex pour l':ref:`IDFMwiki`, vous devez impérativement respecter certaines conventions.

.. _conv_theme:
Convention du thème
----------------------------

Chaque mode de transport francilien est associé à un thème à utiliser en particulier.

+-------------------+------------------+
| Mode de transport | Thème à utiliser |
+===================+==================+
|       RER         |       RER        |
+-------------------+------------------+
|    Transilien     |       RER        |
+-------------------+------------------+
|      Métro        |      METRO       |
+-------------------+------------------+
|     Tramway       |       TRAM       |
+-------------------+------------------+
|      Câble        |       TRAM       |
+-------------------+------------------+
|       Bus         |       BUS        |
+-------------------+------------------+
|   Tzen et BHNS    |       TRAM       |
+-------------------+------------------+
|     Noctilien     |       BUS        |
+-------------------+------------------+
|        VIF        |      à venir     |
+-------------------+------------------+
|    Covoiturage    |       BUS        |
+-------------------+------------------+
|    Tram-train     |       TRAM       |
+-------------------+------------------+
|    Funiculaire    |      METRO       |
+-------------------+------------------+
|   Navettes (VAL)  |      METRO       |
+-------------------+------------------+
|       Ferry       |       (1)        |
+-------------------+------------------+

*(1) : en attente de confirmation du déploiement de ce mode de transport*

.. _conv_color:
Convention des couleurs
------------------------------

L'IDFMwiki traite des lignes actuelles mais aussi des lignes anciennes.

Pour les lignes actuelles
    Il est évident que le plan sera généré de la même couleur que celle de la ligne.

Pour les lignes anciennes
    Ces lignes ont des couleurs qui ne font pas partie de la charte graphique d'Île-de-France Mobilités. Dans ce cas, il existe trois possiblités :
    - il est possible de retrouver la couleur de la ligne : dans ce cas, on définira la nouvelle couleur ou on utilisera une couleur pré-définie proche
    - il n'est pas possible de retrouver la couleur de la ligne : engagez une discussion avec la communauté de l':ref:`IDFMwiki` pour savoir quelle couleur utilisée

.. _conv_stop:
Convention de nommage des arrêts
----------------------------------

Les pages associées aux arrêts (= ce qu'on écrit dans ``<wikiref>``) suivent des règles très précises que vous pouvez consulter `ici <https://idfmwiki.miraheze.org/wiki/Aide:Nommer_un_arrêt>`__.
