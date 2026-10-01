# Métavers cross-plateforme et sobriété matérielle : le rôle des smartphones et ordinateurs dans la démocratisation, l'adoption massive et les modèles économiques des univers virtuels de demain

**Dossier de recherche — 4 rapports thématiques + synthèse + note de vérification**
Sources primaires et études à jour 2024-2026.

**Problématique centrale :**
> « Dans quelle mesure l'accès au métavers via les écrans du quotidien (téléphones mobiles et ordinateurs) affranchit-il les univers virtuels de la contrainte des casques VR, et comment ce métavers « accessible » redéfinit-il les usages, la technologie et l'économie numérique mondiale ? »

## Structure du dossier

| Fichier | Contenu |
|---|---|
| `01-democratisation-accessibilite.md` | Axe 1 — Taux d'équipement, coût d'entrée, UX, pivot mobile-first de Meta, parts d'usage par écran |
| `02-technologies-sans-casque.md` | Axe 2 — Web3D/WebXR, cloud gaming et pixel streaming, RA mobile, standards, sobriété technique |
| `03-secteurs-usages-ecrans.md` | Axe 3 — Retail, travail/formation, divertissement/culture, éducation + échecs 2025-2026 |
| `04-impacts-economiques-sociaux.md` | Axe 4 — Modèles d'affaires mobiles, échelle des marchés, inclusion, temps d'écran, environnement |
| `05-verification-des-sources.md` | Note de vérification : contrôles de cohérence, hiérarchie Tier 1-4, lacunes reconnues |

---

## Synthèse

### Réponse directe à la problématique

**L'accès par les écrans du quotidien a déjà affranchi le métavers de la contrainte du casque — en volume.** La preuve par les ordres de grandeur : ~5,83 Md d'utilisateurs mobiles (70 % de l'humanité, DataReportal 2026) et 1,26 Md de smartphones livrés en 2025 contre quelques dizaines de millions de casques au mieux (casques MR/VR −42,8 % en 2025 selon IDC), et **1,49 % des utilisateurs Steam** seulement équipés en VR (août 2026). Sur Roblox, **80 % des utilisateurs actifs quotidiens sont sur mobile** (10-K) ; au T3 2025, ~11,5 des ~14 Md d'heures d'engagement mensuelles provenaient du mobile. Le métavers n'a jamais été un marché du casque : il est un marché de l'écran, et l'écran est d'abord le téléphone.

**Mais l'affranchissement est matériel, pas total.** Trois déplacements de contrainte se substituent à celle du casque : la **latence et le débit** (cloud gaming : 112-403 ms mesurées, seuil de jouabilité < 100 ms — NSDI'25), le **coût de l'infrastructure** (sessions cloud limitées, abonnements), et l'**attention** (~2,7 h/jour par utilisateur quotidien de Roblox s'ajoutant à ~6 h 51 de temps d'écran général).

### 1. Démocratisation et accessibilité

- **Équipement** : 5,83 Md de smartphones (70,4 % de la population) vs parc VR de l'ordre de ~27 M de Quest (reconstitution T4) ; VR sur Steam : 1,49 %. VR US : ~13 % des ménages (T4, 2024).
- **Coût** : Quest 3S à 349,99 $ (depuis 04/2026), Vision Pro à 3 499 $, « Meta VR Glasses » annoncé à 1 299,99 $ (2027) — le smartphone, lui, est un achat déjà payé et polyvalent. ASP mondial smartphone : > 400 $ (T4 2025), mais l'entrée de gamme existe dès 39 $ (Afrique, GSMA).
- **UX** : mobile = sessions de 3-5 min, 3,8 fois/jour ; VR = sessions « Goldilocks » de 20-40 min (Meta). Complémentarité de régimes d'usage, non substitution.
- **Pivot historique** : Meta déclare Horizon Worlds « almost exclusively mobile » (02/2026), sépare Quest et Horizon, arrête le développement VR (annoncé 17/03/2026, effectif au 15/06/2026) — après une croissance **×4 du MAU mobile** en 2025. Rec Room fermé (01/06/2026), Spatial créateur arrêté (27/07/2026) : la VR sociale et les mondes 3D gratuits payés par le casque s'effondrent ; le mobile reste.

### 2. Enjeux et innovations technologiques

- **Navigateur** : WebGPU natif sur iOS/macOS 26 ; Roblox annoncé « dans Chrome, sans installation » fin 2026 ; Fortnite déjà jouable via Xbox Cloud sans abonnement (> 500 M d'heures streamées en FY2025). WebXR immersif toujours bloqué sur Safari/iOS.
- **Cloud/pixel streaming** : Xbox Cloud > 500 M d'heures ; GeForce NOW 25 M inscrits (dernier chiffre officiel 2023) ; marché du cloud gaming estimé entre 4,8 et 28,3 Md$ en 2026 (écart ×6 : aucune donnée fiable unique — Tier 3).
- **RA mobile** : Pokémon GO > 800 M de cumul et > 1 Md$ de revenus en 2025 (Scopely) ; Snapchat 350 M d'utilisateurs AR/jour ; Google essayage virtuel sur milliards d'articles.
- **Standards** : OpenXR 1.1 (Khronos), Epic 972 M de comptes cross-platform, un compte Roblox unique sur tous les écrans.
- **Sobriété technique** : ADEME — reconditionné −87 % GES, +50 % de bilan à 4 ans vs 2 ans d'usage ; The Shift Project — > 90 % de l'empreinte d'un smartphone avant l'achat. Le « sans casque » évite un matériel, à condition de prolonger celui qu'on a.

### 3. Transformation des secteurs (usages sur écrans)

| Secteur | Cas concret | Chiffre clé |
|---|---|---|
| Retail | Google Try On, Amazon VTO, IKEA Place, Walmart × Zepeto | +60 % de vues (Google) ; 3,5 M d'essayages + 1,3 M d'achats virtuels (Walmart/Zepeto) |
| Travail/formation | Gather.town, Teams immersif ; *vs* Mesh retiré (12/2025), Workrooms fermé (02/2026) | PwC : formation VR 4× plus rapide — **valable en VR, non transférable au 2D** |
| Divertissement | Record de concert virtuel : Bruno Mars × Steal a Brainrot (Roblox, **12,8 M simultanés**, 01/2026, homologation Guinness) ; Travis Scott 12,3 M = record *Fortnite* (2020) ; Roblox 123 M DAU (T2 2026) | Événements à millions de participants **déjà sur mobile/console** |
| Éducation | VictoryXR (100+ établissements, accès navigateur), m-learning UNESCO | Campus jumeau à 50 000 $ : incompatible avec le Sud global — le navigateur et le SMS restent la porte d'entrée |
| Échecs | Rec Room, Mesh, Workrooms, Spatial, Horizon VR | Fin d'un modèle : mondes 3D gratuits trop coûteux à héberger — **recentrage sur l'écran, pas abandon** |

### 4. Impacts économiques, sociaux et sociétaux

- **Modèles d'affaires** : Roblox 4,89 Md$ de revenus et 6,79 Md$ de bookings en 2025 (T1) ; **> 1,5 Md$ versés aux créateurs** (42 000+ créateurs, médiane ~1 500 $) ; mobile = 80 % des DAU mais 46 % des revenus Robux — le PC/console sure-monetise. Achats intégrés (skins, avatars) = cœur du modèle.
- **Échelle** : mobile gaming 113,3 Md$ (56 % du jeu mondial, Newzoo) **≈ 9-10×** le logiciel AR-VR (~12 Md$, IDC).
- **Inclusion** : le mobile élargit la porte, mais 2,2 Md de personnes restent hors ligne (UIT) et un smartphone d'entrée coûte jusqu'à ~45 % du revenu mensuel en Afrique subsaharienne (Findex 2025). La fracture n'est pas seulement « casque ou pas casque ».
- **Temps d'écran** : 6 h 51/jour (hors travail) ; Roblox 2,7 h/DAU/jour ; régulation en cours — vérifications d'âge Roblox (01/2026), Online Safety Act UK (6 amendes Ofcom), PPL Sénat français (âge 13 ans).
- **Environnement** : sobriété terminale réelle (pas de casque à produire, durée de vie à allonger) **contre** 945-950 TWh de centres de données projetés en 2030 (AIE) — l'empreinte se déplace, elle ne disparaît pas.

### Réserves ouvertes

1. Session VR « ~52 min » (T4) non confirmée : retenir les 20-40 min de Meta (T1) — *voir note 05*.
2. −42,8 % casques VR 2025 = estimation provisoire IDC (« once final numbers are in »).
3. Marché cloud gaming : écart ×6 entre cabinets — aucune valeur unique défendable (Tier 3).
4. Lacunes documentaires : coût du casque en mois de revenu, part mobile actualisée des bookings Roblox, install base officielle Quest.

---

## Sources principales du dossier

- Roblox Corporation, *10-K FY2024/FY2025*, *Q4 & FY2025 Shareholder Letter*, *Q2 2026 Shareholder Letter* (SEC)
- Meta, *Connect 2025/2026*, *An Update on Meta Quest Pricing*, blog développeurs Horizon, CNBC/WIRED (arrêt VR 2026)
- IDC, *Global XR Shipments* (prUS54033425), *Quarterly Mobile Phone Tracker*
- Steam Hardware Survey (août 2026) ; Counterpoint, *Smartphone Installed Base / ASP*
- DataReportal, *Digital 2026* (Global Overview + Mid-Year) ; GSMA Intelligence
- Newzoo, *Global Games Market 2025* ; Sensor Tower ; GameAnalytics 2026
- W3C (WebXR CRD), Khronos (OpenXR 1.1), gpuweb (WebGPU), npm registry
- Microsoft (Xbox Cloud, Mesh), Epic Games (Fortnite, UEFN), NVIDIA (Omniverse Kit Streaming)
- USENIX NSDI'25 (latence cloud gaming mobile) ; NVIDIA Docs (exigences réseau)
- Scopely (Pokémon GO), Snap Inc. (Lens Fest 2025), Google (Virtual Try-On), Shopify, Amazon, IKEA
- PwC, *Virtual Reality Study* ; VictoryXR ; UNESCO ; AFD
- UIT, *Facts and Figures 2025* ; Banque mondiale, *Global Findex 2025* ; GDIP
- ADEME (reconditionnement, face cachée du numérique) ; The Shift Project (*Lean ICT*, *Mondes virtuels & réseaux*) ; AIE (*Energy and AI*)
- Ofcom (Online Safety Act) ; OMS (CIM-11) ; Sénat français (PPL écrans)

> **Réserve méthodologique** : les projections de cabinets (essayage virtuel, cloud gaming, RA mobile) sont des estimations commerciales, pas des données constatées — leur dispersion (×6 pour le cloud gaming) est l'information principale. Les faits vérifiables (Roblox, Meta, IDC, Steam Survey, ADEME, UIT) sont systématiquement distingués des projections. Voir `05-verification-des-sources.md`.
