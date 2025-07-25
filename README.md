# Module Code-barres Produit sur Facture (Product Barcode on Invoice)

Ce module pour Odoo 18 permet d'afficher le code-barres des produits directement sur les lignes de facture et sur les documents de facturation imprimés.

## Fonctionnalités

*   **Colonne Code-barres :** Ajoute une nouvelle colonne "Code-barres" dans la vue des lignes de facture, affichant le code-barres de chaque produit.
*   **Rapport de Facture :** Intègre la colonne "Code-barres" dans le rapport de facture PDF, la rendant visible sur les documents imprimés ou envoyés aux clients.
*   **Champ Calculé :** Le code-barres est récupéré dynamiquement depuis la fiche produit associée à la ligne de facture.

## Installation

1.  Copiez le dossier `product_barcode_invoice` dans le répertoire de vos addons Odoo.
2.  Redémarrez le service Odoo.
3.  Allez dans le menu `Apps` (Applications).
4.  Cliquez sur `Mettre à jour la liste des applications`.
5.  Recherchez le module "Product Barcode on Invoice Lines" et cliquez sur `Installer`.

## Utilisation

Une fois le module installé, la colonne "Code-barres" apparaîtra automatiquement sur les lignes de facture et les rapports de facturation. Aucune configuration supplémentaire n'est nécessaire.

## Compatibilité

*   Odoo 18.0

## Auteur
Charlie Rostant YOSSA (Shermine237)
