# Analyse de Performance Supply Chain : Calcul et Visualisation des KPI

## 📝 Description

Ce projet propose un outil Python permettant de calculer et de visualiser les principaux KPI logistiques pour évaluer la performance de la Supply Chain. À partir de données spécifiques (commandes, ventes, stock, transport, etc.), l'outil offre des insights critiques pour soutenir la prise de décision stratégique.

## 🎯 Objectifs
1. **Calcul des KPI** : Utiliser les formules adaptées pour générer des indicateurs clairs.
2. **Analyse des points faibles** : Identifier les domaines nécessitant des améliorations.
3. **Visualisation intuitive** : Créer des graphiques (barres ou radar) pour faciliter la communication avec les parties prenantes.
4. **Recommandations stratégiques** : Proposer des actions basées sur l’analyse des résultats.

## 🚀 Fonctionnalités
- **Calcul des KPI logistiques** :
  - Ponctualité des commandes clients.
  - Ratio Stock / Ventes.
  - DSI (Durée Moyenne de Rotation des Stocks).
  - Coût de possession du stock.
  - Coût transport par tonne expédiée.
  - Ponctualité des livraisons fournisseurs.
  - Taux de commandes parfaites.
- **Visualisation des résultats** :
  - Diagrammes en barres pour une vue globale.
  - Graphique radar pour une visualisation comparative.
- **Recommandations concrètes** basées sur des seuils acceptables du secteur.

## 📊 Aperçu des Calculs

### Données d’entrée
Les données brutes utilisées dans ce projet incluent :
- Nombre de commandes totales et livrées à temps.
- Valeur du stock moyen (en €).
- Ventes nettes (en €).
- Coût des biens vendus.
- Coût total du transport et tonnage total.
- Historique des délais de livraisons fournisseurs.

### Exemples de KPI Calculés
- **Ponctualité Clients** = (Commandes livrées à temps / Commandes totales) * 100
- **Ratio Stock / Ventes** = Stock moyen / Ventes nettes
- **Coût Transport / Tonne** = Coût total transport / Tonnage total
- **DSI** = (Stock moyen / Coût des biens vendus) * 365

## 📈 Exemple de Visualisation
Le projet inclut un graphique radar pour comparer les performances des KPI :

![Graphique Radar](https://placeholder_for_visualisation_image)

Le radar met en évidence les forces et faiblesses des opérations logistiques sur plusieurs axes clés.

## 🛠️ Technologies Utilisées
- **Python** : Langage principal pour les calculs et visualisations.
- **Pandas** : Analyse et structuration des données.
- **Matplotlib & Seaborn** : Création des graphiques.
- **NumPy** : Support pour les calculs numériques.

## 💡 Comment Utiliser
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-repo/supply-chain-kpi.git
   cd supply-chain-kpi
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Exécutez le script principal :
   ```bash
   python main.py
   ```
4. Explorez les résultats affichés dans la console et les graphiques générés.

## 🛠️ Recommandations
- **Optimisation des livraisons** : Si la ponctualité clients est inférieure à 95 %, améliorer la gestion des expéditions.
- **Réduction des coûts** : Si le coût transport/tonne dépasse les seuils acceptables, envisagez des solutions logistiques alternatives.
- **Amélioration des commandes parfaites** : Si le taux de commandes parfaites est inférieur à 90 %, renforcer les processus de contrôle qualité.

## 🤝 Contribuer
Les contributions sont les bienvenues pour enrichir ce projet ! Pour signaler des problèmes ou proposer des fonctionnalités, veuillez ouvrir une issue.

---

Ce fichier README est prêt à être utilisé et peut être enrichi avec vos graphiques ou exemples. N'hésitez pas à me dire si vous souhaitez d'autres modifications ou ajouts ! 🚀
