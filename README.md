# Recherches sur le Métavers

Trois dossiers de recherche documentés :

1. **Métavers et Intelligence Artificielle** — « innovations, transformation des secteurs d'activité, adoption par les utilisateurs et impacts économiques, sociaux et technologiques sur le monde de demain »
2. **Métavers cross-plateforme et sobriété matérielle** — « Le rôle des smartphones et ordinateurs dans la démocratisation, l'adoption massive et les modèles économiques des univers virtuels de demain »
   > Problématique : *« Dans quelle mesure l'accès au métavers via les écrans du quotidien (téléphones mobiles et ordinateurs) affranchit-il les univers virtuels de la contrainte des casques VR, et comment ce métavers « accessible » redéfinit-il les usages, la technologie et l'économie numérique mondiale ? »*
3. **Métavers et projets open source** — « Comment exploiter les projets open source au service du développement et de l'adoption du métavers ? » (standards ouverts, moteurs et outils, IA générative ouverte, leviers d'adoption)

Toutes les affirmations chiffrées sont adossées à des sources datées et vérifiables (McKinsey, IDC, Gartner, PwC, WEF, AIE, Newzoo, GSMA, UIT, ADEME, Roblox, Meta, publications scientifiques, presse spécialisée). Les projections de marché sont systématiquement distinguées des données constatées (hiérarchie Tier 1-4 dans chaque note de vérification).

## 📄 Articles PDF téléchargeables

Un article complet (rapport principal) est disponible en PDF pour **chaque sujet** — générés depuis les fichiers `.md` du dépôt, prêts à être lus, imprimés ou partagés :

| Article | Sujet | Pages | Téléchargement |
|---|---|---|---|
| 📕 **Métavers et Intelligence Artificielle** | Innovations, secteurs, adoption, impacts, prospective 2035 | 14 pages | **[⬇️ Télécharger le PDF](pdf/rapport-metavers-ia.pdf)** |
| 📗 **Métavers cross-plateforme et sobriété matérielle** | Rôle des smartphones/ordinateurs : démocratisation, technologies, secteurs, économie | 10 pages | **[⬇️ Télécharger le PDF](pdf/rapport-metavers-crossplateforme.pdf)** |
| 📙 **Métavers et projets open source** | Standards ouverts, moteurs/outils, IA générative ouverte, leviers d'adoption et limites | 5 pages | **[⬇️ Télécharger le PDF](pdf/rapport-metavers-opensource.pdf)** |

> Les PDF reflètent les versions `.md` du 7 octobre 2026. Pour les régénérer : `python3 tools/md2pdf.py rapport_metavers_ia.md pdf/rapport-metavers-ia.pdf "<titre>"` (dépendances : `markdown`, `reportlab` ; script : [`tools/md2pdf.py`](tools/md2pdf.py)).

## Contenu du dépôt

| Fichier | Description |
|---|---|
| [`rapport_metavers_ia.md`](rapport_metavers_ia.md) | **Rapport principal** (~7 000 mots) : cadrage, innovations, secteurs, adoption, impacts, prospective 2035, recommandations — 43 sources |
| [`metavers-ia/00-synthese.md`](metavers-ia/00-synthese.md) | Synthèse du dossier de recherche (4 rapports thématiques) |
| [`metavers-ia/01-innovations.md`](metavers-ia/01-innovations.md) | Innovations technologiques 2024-2026 (matériel XR, IA générative 3D, plateformes, 32 sources) |
| [`metavers-ia/02-secteurs.md`](metavers-ia/02-secteurs.md) | Transformation de 8 secteurs d'activité + projets abandonnés (42 sources) |
| [`metavers-ia/03-adoption.md`](metavers-ia/03-adoption.md) | Adoption utilisateurs : statistiques, démographie, freins, prévisions (26 sources) |
| [`metavers-ia/04-impacts.md`](metavers-ia/04-impacts.md) | Impacts économiques, sociaux, technologiques et réglementaires |
| [`metavers-ia/05-besoins-et-classification.md`](metavers-ia/05-besoins-et-classification.md) | Évaluation critique : besoins réels vs artificiels, classification des sources par fiabilité (tiers 1-4) |
| [`metavers-ia/06-verification-des-sources.md`](metavers-ia/06-verification-des-sources.md) | Note de vérification : contrôle qualité des sources critiques et limites reconnues |
| [`rapport_metavers_crossplateforme.md`](rapport_metavers_crossplateforme.md) | **Rapport principal, dossier 2** : démocratisation, technologies d'accès sans casque, secteurs, impacts, discussion de la problématique, scénarios 2030-2035, recommandations |
| [`metavers-crossplateforme/00-synthese.md`](metavers-crossplateforme/00-synthese.md) | Synthèse du dossier cross-plateforme (4 axes + réserves ouvertes) |
| [`metavers-crossplateforme/01-democratisation-accessibilite.md`](metavers-crossplateforme/01-democratisation-accessibilite.md) | Axe 1 — VR vs mobile/PC : équipement, coût, UX, pivot mobile-first de Meta, parts d'usage |
| [`metavers-crossplateforme/02-technologies-sans-casque.md`](metavers-crossplateforme/02-technologies-sans-casque.md) | Axe 2 — Web3D/WebXR, cloud gaming, RA mobile, standards, sobriété technique |
| [`metavers-crossplateforme/03-secteurs-usages-ecrans.md`](metavers-crossplateforme/03-secteurs-usages-ecrans.md) | Axe 3 — Retail, travail/formation, divertissement, éducation + échecs 2025-2026 |
| [`metavers-crossplateforme/04-impacts-economiques-sociaux.md`](metavers-crossplateforme/04-impacts-economiques-sociaux.md) | Axe 4 — Modèles d'affaires, inclusion numérique, temps d'écran, environnement |
| [`metavers-crossplateforme/05-verification-des-sources.md`](metavers-crossplateforme/05-verification-des-sources.md) | Note de vérification : contrôles de cohérence inter-rapports, Tier 1-4, lacunes reconnues |
| [`rapport_metavers_opensource.md`](rapport_metavers_opensource.md) | **Rapport principal, dossier 3** : socle standards ouverts, chaîne de production ouverte, IA générative ouverte, 4 leviers d'adoption, recommandations — échange de vérification n°1 clos (10 accords) |
| [`metavers-opensource/00-synthese.md`](metavers-opensource/00-synthese.md) | Synthèse du dossier open source (4 axes + réserves ouvertes) |
| [`metavers-opensource/01-standards-interopabilite.md`](metavers-opensource/01-standards-interopabilite.md) | Axe 1 — WebGPU/WebXR, OpenXR, glTF, VRM, OpenUSD, fondations (Linux Foundation) |
| [`metavers-opensource/02-moteurs-outils-ouverts.md`](metavers-opensource/02-moteurs-outils-ouverts.md) | Axe 2 — Godot, Blender, Three.js, O3DE, Monado ; financement et bascule Unity |
| [`metavers-opensource/03-ia-generative-ouverte.md`](metavers-opensource/03-ia-generative-ouverte.md) | Axe 3 — Cube 3D, Hunyuan3D, PNJ locaux, frontière OSAID (open source vs open weights) |
| [`metavers-opensource/04-adoption-communautes-economie.md`](metavers-opensource/04-adoption-communautes-economie.md) | Axe 4 — 4 leviers d'adoption, modèles économiques, pérennité (Mozilla Hubs), limites |
| [`metavers-opensource/05-verification-des-sources.md`](metavers-opensource/05-verification-des-sources.md) | Note de vérification : Tier 1-4, 16 contrôles, lacunes reconnues |
| [`metavers-opensource/courant.md`](metavers-opensource/courant.md) | Dialogue inter-agents du dossier 3 : échange n°1 clôturé (5 questions, 10 accords) |

## Chiffres clés (sources dans les rapports)

- **Économie** : métavers jusqu'à 5 000 Md$ de valeur d'ici 2030 (McKinsey 2022) ; IA générative +2 600 à 4 400 Md$/an (McKinsey 2023) ; +7 % de PIB mondial sur 10 ans (Goldman Sachs)
- **Emploi** : −92 M emplois déplacés, +170 M créés d'ici 2030, solde net +78 M (WEF, Future of Jobs 2025)
- **Adoption** : Roblox 144 M d'utilisateurs actifs quotidiens (T4 2025 ; 132 M au T1 2026 après vérifications d'âge) ; ~13 % des ménages américains équipés en VR ; bifurcation matérielle : casques VR/MR −42,8 % en 2025, smart glasses +211 % puis +167 % au T1 2026 (IDC)
- **Énergie** : consommation électrique des centres de données multipliée par 2 → ~945 TWh en 2030 (AIE)
- **Régulation** : AI Act européen applicable depuis août 2026 (étiquetage obligatoire des deepfakes)

### Dossier open source (projets ouverts au service de l'adoption)

- **Socle ouvert** : WebGPU *Baseline* sur iOS/macOS 26 (02/06/2026) ; OpenXR 1.1 (15/04/2024) ; VRM × Khronos (24/10/2024) ; Open Metaverse Foundation (Linux Foundation, 18/01/2023)
- **Chaîne de création** : Three.js ≈ 12,2 M téléchargements npm/semaine (24/09/2026) ; Godot ~2 M de téléchargements par version stable, communauté doublée en 2 ans (06/05/2026) ; Blender 4,2 → 5,7 M€ de revenus (+36 %) en 2025
- **IA ouverte** : Roblox Cube 3D open source (1,8 Md de paramètres, 1,5 M d'assets, 17/03/2025) ; Hunyuan3D = open weights (licence communautaire) ; OSAID 1.0 (28/10/2024) ; 80 % des choix se portent sur des modèles fermés (MIT Sloan, 01/2026)
- **Pérennité** : arrêt de Mozilla Hubs (31/05/2024) → reprise communautaire du code ; à l'inverse Rec Room, Spatial, Mesh, Workrooms fermés avec leurs mondes

### Dossier cross-plateforme (smartphones et ordinateurs)

- **Équipement** : 5,83 Md d'utilisateurs mobiles (70 % de la population, DataReportal 2026) vs 1,49 % des utilisateurs Steam équipés en VR (août 2026) ; casques MR/VR −42,8 % en 2025 (IDC, estimé)
- **Usage** : Roblox 123 M DAU (T2 2026) dont **80 % sur mobile** (10-K) ; session mobile médiane 3-5 min vs session VR 20-40 min (Meta) ; Roblox 2,7 h/DAU/jour
- **Divertissement** : record de concert virtuel — Bruno Mars × Steal a Brainrot (Roblox) 12,8 M de spectateurs simultanés (17/01/2026, homologation Guinness) ; Travis Scott 12,3 M (2020) reste le record des expériences Fortnite dédiées
- **Pivot Meta** : Horizon Worlds « almost exclusively mobile » (02/2026), développement VR arrêté au 15/06/2026 après une croissance ×4 du MAU mobile en 2025
- **Économie** : Roblox 4,89 Md$ de revenus et 6,79 Md$ de bookings en 2025, > 1,5 Md$ versés aux créateurs ; mobile gaming 113,3 Md$ = 9-10× le logiciel AR-VR (~12 Md$, IDC)
- **Sobriété** : reconditionné −87 % GES (ADEME) ; centres de données 415 TWh (2024) → ~945-950 TWh en 2030 (AIE) — l'empreinte se déplace du terminal vers le cloud

## Licence

Ce projet est sous licence [MIT](LICENSE).
