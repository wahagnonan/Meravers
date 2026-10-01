# Note de vérification des sources

*Contrôle qualité effectué le 1ᵉʳ octobre 2026 — traçabilité de la fiabilité du dossier « Métavers cross-plateforme et sobriété matérielle ».*

---

## 1. Contrôles de cohérence entre les quatre rapports

| Point de tension | Version A | Version B | Résolution retenue |
|---|---|---|---|
| Durée d'une session VR | « ~52 min » (`01`, T4, Treeview/SQ Magazine 05/2026) | « 20-40 min » (`04`, T1, Meta blog développeurs 07/2025) | **Retenir 20-40 min (T1)** : donnée publiée par l'éditeur du leader du marché. Le « 52 min » est une estimation tierce non confirmée — signalée comme telle, jamais citée seule. |
| Part mobile dans Roblox | 10-K : **80 % des DAU, 46 % des revenus Robux** (T1, ex. 2024) | Panel GameAnalytics : 40,8 % PC seul (T2) ; médias : « 72 % » | **Retenir le 10-K (T1)** : périmètre « tous utilisateurs ». Les panels mesurent un échantillon d'appareils connectés aux SDK — méthodes différentes, chiffres non contradictoires. Le « 72 % » n'a pas été retrouvé à la source primaire : ne pas citer. |
| Chronologie Horizon Worlds | Annonce d'arrêt VR le 17/03/2026 | Rétractation de Bosworth le 18/03 ; arrêt effectif de la création VR le **15/06/2026** | **Chaîne complète retenue** : rebond mobile 2025 (×4) → séparation Quest/Horizon (20/02/2026) → annonce 17/03 → rétractation 18/03 → arrêt réel 15/06. L'« arrêt » n'est pas une fausse information mais une annonce partiellement annulée : le développement VR a cessé, l'app a été maintenue en mode maintenance. |
| Ventes de casques VR 2025 | « −42,8 % » (IDC, estimé « once final numbers are in ») | Livraisons XR totales **+41,6 %** (14,5 M, lunettes AI incluses) | **Périmètres distincts** : −42,8 % = casques MR/VR seuls ; +41,6 % = tout le XR tiré par les lunettes AI (+211 %). Toujours préciser le périmètre. Le −42,8 % reste une **estimation provisoire IDC**. |
| Pénétration VR sur Steam | 1,77 % des utilisateurs Steam (janv. 2026, dossier « Métavers & IA ») | **1,49 %** (août 2026, présent dossier) | **Baisse mesurée entre deux dates** : citer la date à chaque fois. Les deux chiffres sont T1 (Steam Hardware Survey). |
| Heures Roblox 2025 | « 124 Md d'heures » (`01`) | « 123,9 Md d'heures » (`04`) | Même donnée, arrondis différents — harmoniser à **~124 Md heures (2025)**. |
| Apple Vision Pro | ~45 000 unités en 2025 (IDC) | 390 000 en 2024 | Cohérent avec le dossier « Métavers & IA » (03-adoption.md) : confirmation croisée T1. |
| Record de concert virtuel | « Travis Scott 12,3 M (2020) jamais dépassé » (version initiale de `03`, reprise par `00` et le rapport) | **Bruno Mars × Steal a Brainrot : 12,8 M de spectateurs simultanés (17/01/2026), homologation Guinness févr. 2026** | **Le record de concert a été dépassé** (Roblox via GamesIndustry.biz, MBW, Uproxx/Guinness — T1 relayé). Nuances conservées : concert dans un jeu-tycoon existant (pic propre du jeu : 25,4 M CCU, oct. 2025) vs expérience Fortnite dédiée ; hors catégorie « concert », *Galactus* (Fortnite, 2020) reste à 15,3 M. Correction appliquée à `00`, `03`, le rapport et la ligne « non trouvée » ci-dessous (§3). |

## 2. Hiérarchie de confiance du dossier

| Niveau | Contenu | Confiance |
|---|---|---|
| Tier 1 | Résultats financiers publiés (Roblox 10-K, Meta, Epic), Steam Hardware Survey, pages officielles (W3C, Khronos, Meta, Microsoft), ADEME, UIT | Élevée — faits vérifiables |
| Tier 2 | Instituts et études (IDC, Newzoo, GSMA, GameAnalytics, AIE, USENIX NSDI'25, PwC) | Forte — à lire en tenant compte du commanditaire |
| Tier 3 | Projections de cabinets (Valuates, TBRC, Statista Market Insights, prévisions cloud gaming) | Faible en précision — l'écart entre estimations (×6 pour le cloud gaming) est l'information principale ; jamais présenter comme des faits |
| Tier 4 | Presse secondaire, estimations reconstituées (parc Quest 26,76 M, « 13 % ménages US », Durée « 52 min ») | Précaution — signalées comme incertaines dans le texte |

## 3. Chiffres recherchés et non trouvés (lacunes reconnues)

1. **YouGov sur les freins d'achat VR** : aucune publication localisée (le chiffre « prix = 29 % » du dossier antérieur n'a pas été revérifié ici).
2. **Coût d'un casque VR en mois de revenu** dans les pays à faible revenu : non chiffré — empêche de quantifier précisément la barrière VR dans le Sud global.
3. **Prix moyen mondial d'un smartphone d'entrée de gamme** : non trouvé (proxys disponibles : ASP Xiaomi/Oppo/vivo 152-274 $ ; smartphone d'entrée 39 $ en Afrique subsaharienne — GSMA).
4. **Part mobile actualisée des bookings Roblox** (2025-2026) : le 46 % est daté de l'exercice 2024.
5. **Install base officielle Meta Quest** : Meta ne publie plus ce chiffre depuis des années — tout parc Quest cité (≈ 26,76 M) est une reconstitution Tier 4.
6. **Événement culturel virtuel dépassant le record de Travis Scott (12,3 M simultanés, 2020)** : ~~aucun dépassé officiellement à ce jour~~ **record de concert dépassé — Bruno Mars × Steal a Brainrot, 12,8 M de simultanés (17/01/2026, homologation Guinness, févr. 2026)** ; correction appliquée après échange n°1 du dialogue inter-agents (`courant.md`). Le record des expériences *Fortnite* dédiées reste Travis Scott ; hors catégorie « concert », *Galactus* (2020) reste à 15,3 M. |

## 4. Limites reconnues

1. La comparaison des durées d'usage (VR vs mobile) repose sur des méthodes de mesure différentes (panels vendeurs vs panels analytiques) : elle est indicative, pas un rapport de force exact.
2. Les pages web évoluent : citer avec date d'accès. Plusieurs chiffres 2026 (Roblox T2, Meta Connect 2026) seront revus aux prochains résultats trimestriels.
3. Les données de session VR « Goldilocks » proviennent de Meta lui-même (intérêt éditeur) — crédible sur ses propres plateformes, pas généralisable à toute la VR.
4. Sources anciennes assumées comme telles : PwC (2020-2022), AFD (2018), UNESCO (2014), The Shift Project *Lean ICT* (2018) — toujours datées dans le texte.
5. Aucun chiffre du dossier n'est inventé : chaque valeur est attribuée à une source nominative avec URL ; les non-trouvés sont listés ci-dessus.

## 5. Recommandations d'usage

- **Citation académique** : privilégier Tier 1-2, mentionner « projection » pour Tier 3, ajouter la date de consultation.
- **Contestation possible** : vérifier la source primaire via l'URL citée avant toute correction ; commencer par les points de la section 1.
- **Mise à jour** : les chiffres Tier 1 (Roblox, Meta, IDC, Steam Survey) évoluent chaque trimestre — dater toute republication.
