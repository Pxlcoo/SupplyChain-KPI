import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Données fournies
data = {
    'commandes': 500,
    'commandes_livrees_a_temps': 420,
    'stock_moyen': 120000,  # en €
    'ventes_net': 600000,   # en €
    'cout_biens_vendus': 450000,
    'taux_possession': 0.25,
    'commandes_parfaites': 385,
    'cout_total_transport': 75000,  # en €
    'tonnage_total': 1500,  # en tonnes
    'delais_livraisons_fournisseurs': [True, True, False, True, False, True, True, True, False, True],
}

# Calculs des KPI
kpi = {}

# Ponctualité des commandes clients (%)
kpi['ponctualite_clients'] = (data['commandes_livrees_a_temps'] / data['commandes']) * 100

# Ratio stock / ventes
kpi['ratio_stock_ventes'] = data['stock_moyen'] / data['ventes_net']

# DSI (Durée Moyenne de Rotation des Stocks)
kpi['dsi'] = (data['stock_moyen'] / data['cout_biens_vendus']) * 365

# Coût de possession du stock (en €)
kpi['cout_possession_stock'] = data['stock_moyen'] * data['taux_possession']

# Coût de transport par tonne (en €/tonne)
kpi['cout_transport_par_tonne'] = data['cout_total_transport'] / data['tonnage_total']

# Ponctualité des livraisons fournisseurs (%)
ponctualite_fournisseurs = data['delais_livraisons_fournisseurs']
kpi['ponctualite_fournisseurs'] = (sum(ponctualite_fournisseurs) / len(ponctualite_fournisseurs)) * 100

# Taux de commandes parfaites (%)
kpi['taux_commandes_parfaites'] = (data['commandes_parfaites'] / data['commandes']) * 100

# Affichage des résultats
df_kpi = pd.DataFrame([kpi])
print("Résumé des KPI calculés :")
print(df_kpi)

# Visualisation des KPI
plt.figure(figsize=(10, 6))
kpi_labels = [
    'Ponctualité Clients (%)', 'Ratio Stock / Ventes', 'DSI (jours)',
    'Coût de possession du stock (€)', 'Coût Transport / Tonne (€)',
    'Ponctualité Fournisseurs (%)', 'Commandes Parfaites (%)'
]
kpi_values = list(kpi.values())

sns.barplot(x=kpi_labels, y=kpi_values, palette="viridis")
plt.title("Performance des KPI Logistiques")
plt.ylabel("Valeurs")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Recommandations basées sur les KPI
print("\nRecommandations :")
if kpi['ponctualite_clients'] < 95:
    print("- Améliorer la gestion des livraisons aux clients pour augmenter la ponctualité.")

if kpi['ratio_stock_ventes'] > 0.5:
    print("- Optimiser les niveaux de stock pour réduire les coûts liés au surstockage.")

if kpi['cout_transport_par_tonne'] > 50:
    print("- Réévaluer les solutions logistiques pour réduire les coûts de transport.")

if kpi['taux_commandes_parfaites'] < 90:
    print("- Renforcer la qualité opérationnelle pour assurer davantage de commandes parfaites.")
