# Module Code-barres Produit sur Documents (Factures, Devis, Commandes, Bons de livraison)

Ce module pour Odoo 18 permet d'afficher le code-barres des produits directement :

* sur les lignes de **facture**
* sur les lignes de **devis / commandes clients**
* sur les lignes de **demandes de prix / bons de commande**
* sur les lignes de **bons de livraison**

Le code-barres apparaît aussi bien en vue formulaire qu'au sein des PDF générés.

## Fonctionnalités

* **Colonne Code-barres :** Ajoute une colonne "Code-barres" dans les vues liste / formulaire des lignes des documents (factures, devis, commandes, RFQ/PO, bons de livraison).
* **Rapports PDF :** Intègre la colonne "Code-barres" dans les PDF des factures, devis, bons de commande et bons de livraison.
* **Champ calculé :** Le code-barres est récupéré dynamiquement depuis la fiche produit associée à la ligne de document.

## Installation

1.  Copiez le dossier `product_barcode_invoice` dans le répertoire de vos addons Odoo.
2.  Redémarrez le service Odoo.
3.  Allez dans le menu `Apps` (Applications).
4.  Cliquez sur `Mettre à jour la liste des applications`.
5.  Recherchez le module "Product Barcode on Documents" et cliquez sur `Installer`.

## Utilisation

Une fois le module installé, la colonne "Code-barres" apparaîtra automatiquement sur les documents cités ci-dessus, ainsi que dans leurs rapports PDF. Aucune configuration supplémentaire n'est nécessaire.

## Compatibilité

*   Odoo 18.0

## Auteur
Charlie Rostant YOSSA (Shermine237)
