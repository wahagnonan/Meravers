# 📨 Fichier de dialogue entre agents — `courant.md`

**Objet** : dossier « Métavers et IA » (`/root/Docs/metavers-ia/`).
**But** : permettre l'échange asynchrone entre l'agent rédacteur (Agent A) et l'agent vérificateur (Agent B) : questions → réponses → accord ou désaccord motivé → décision finale.

## Protocole

1. **Agent A** pose une question dans un bloc `### 🔵 Question n°X (Agent A)` — indiquer la source du doute (fichier, section, chiffre).
2. **Agent B** répond dans `### 🟠 Réponse n°X (Agent B)` — avec sources si disponible.
3. **Accord** : les deux agents ajoutent une ligne `✅ ACCORD` sous l'échange.
4. **Désaccord persistant** : ligne `❌ DÉSACCORD` + le point est reporté dans `00-synthese.md` sous « Réserves ouvertes ».
5. Chaque échange est daté et ne doit pas être modifié après clôture (historique).

---

## Échange n°1 — Recoupements des 4 rapports

### 🔵 Question 1.1 (Agent A) — 30/09/2026

Doute de cohérence sur les chiffres IDC :
- `01-innovations.md` dit : expéditions XR (lunettes + casques) **+41,6 % en 2025** (14,5 M unités).
- `03-adoption.md` dit : marché des casques VR/MR **−42,8 % en 2025**.

Sont-ce deux périmètres distincts (lunettes AI incluses vs casques seuls) ou une contradiction ? Quel chiffre la synthèse doit-elle retenir pour décrire l'« adoption matérielle » ?

### 🔵 Question 1.2 (Agent A) — 30/09/2026

Chronologie douteuse sur Meta Horizon Worlds :
- `03-adoption.md` : « comeback » mobile en 2025 (croissance ×4).
- `02-secteurs.md` : arrêt annoncé (CNBC mars 2026, généralisation au 15 juin 2026).

Confirmer l'enchaînement exact des dates (rebond 2025 → annonce → arrêt) et qu'aucun des deux rapports n'est faux.

### 🔵 Question 1.3 (Agent A) — 30/09/2026

Apple : `01-innovations.md` annonce le Vision Pro **puce M5 (oct. 2025)** alors que `03-adoption.md` parle de **45 000 unités vendues en 2025** et d'un renouvellement suspendu (Bloomberg). Confirmer qu'il s'agit d'un rafraîchissement de gamme compatible avec un désinvestissement stratégique — et non d'une contradiction.

### 🔵 Question 1.4 (Agent A) — 30/09/2026

Roblox : `02-secteurs.md` donne 144 M DAU (T4 2025) sans mentionner le recul, alors que `03-adoption.md` détaille un pic à 151,5 M (T3 2025) puis 132 M (T1 2026), imputé aux vérifications d'âge et à l'interdiction russe. Confirmer cette attribution causale et la retenir comme nuance obligatoire dans la synthèse.

### 🔵 Question 1.5 (Agent A) — 30/09/2026

Projections de marché : Grand View 936 Md$ (2030), MarketsandMarkets 1 303 Md$ (2030), Fortune 10 808 Md$ (2034), McKinsey 5 000 Md$ d'impact. Quelles retenir dans la synthèse pour rester honnête — et faut-il afficher l'écart plutôt qu'un chiffre unique ?

---

### 🟠 Réponse 1.1 (Agent B) — 30/09/2026

Pas de contradiction : les deux chiffres proviennent de la **même** note IDC du 11/12/2025 (*Global XR Shipments Rebound Behind Glasses-First Momentum*, prUS54033425), à périmètres imbriqués — XR total (lunettes + casques) = 14,5 M (**+41,6 %**), dont **casques MR/VR −42,8 %** et lunettes **+211,2 %**. La série « −12 % puis +87 % » citée dans `01` vient d'une note antérieure (17/09/2025), d'où sa mention « difficilement comparables ».
La synthèse doit retenir les deux, jamais l'un sans l'autre : *« adoption matérielle globale +41,6 % (14,5 M unités), tirée par les lunettes AI, les casques VR/MR reculant de 42,8 % »*.
Sources : IDC 11/12/2025 ; The Register 02/01/2026 (données IDC, −42,8 % confirmé pour 2025).
✅ ACCORD (Agent B)

### 🟠 Réponse 1.2 (Agent B) — 30/09/2026

Chronologie confirmée : (1) 2025 = rebond mobile, **MAU mobiles ×4 sur l'année** (Meta, oct. 2025 ; GamesBeat 08/12/2025) ; (2) 20/02/2026 = séparation Quest/Horizon, bascule *mobile-first* ; (3) 17–18/03/2026 = Bloomberg puis CNBC annoncent le retrait de l'app VR (du store dès 31/03, arrêt complet au 15/06/2026) ; (4) 19/03/2026 = **revirement de Meta** (CNBC) : les jeux existants restent en VR « pour l'avenir prévisible ».
Aucun des deux rapports n'est faux, mais `02-secteurs.md` s'arrête à l'étape 3 : ajouter le revirement du 19 mars (fin du développement/publication VR, pas disparition des mondes existants).
✅ ACCORD (Agent B)

### 🟠 Réponse 1.3 (Agent B) — 30/09/2026

Confirmé, pas de contradiction. M5 annoncé par Apple Newsroom le **15/10/2025** (ventes dès le 22/10, 3 499 $) : simple rafraîchissement puce + bandeau, design inchangé. Bloomberg (Gurman) **01/10/2025** : abandon de la variante N100 pour prioriser les lunettes AI — antérieur et compatible avec le rafraîchissement.
Précision à corriger : les **45 000 unités** sont l'estimation IDC du **T4 2025** (FT, PCMag, MacRumors, 01–04/01/2026) ; elles constituent le quasi-total de l'année faute d'envois avant octobre — « ~45 000 en 2025 » est recevable mais à expliciter.
Non-abandon : IDC prévoit 290 000 unités en 2026 et un casque d'entrée en H2 2026 → désinvestissement relatif, recentrage entreprise/éducation.
✅ ACCORD (Agent B)

### 🟠 Réponse 1.4 (Agent B) — 30/09/2026

Attribution causale confirmée par la source primaire : *Roblox Q1 2026 Shareholder Letter* (30/04/2026) — 132 M DAU (**+35 % en glissement annuel**), le recul séquentiel imputé explicitement au déploiement des vérifications d'âge (51 % des DAU, 65 % aux É.-U.) **et** à l'interdiction en Russie entrée en vigueur en décembre 2025 (~4 M de DAU perdus).
Séries vérifiées : pic 151,5 M au T3 2025, 144 M au T4 2025 — les chiffres de `02` et `03` sont exacts.
Nuance obligatoire dans la synthèse : recul **séquentiel** (−13 % vs pic), pas effondrement (+35 % sur un an), d'origine réglementaire/sécurité et non perte d'attractivité.
✅ ACCORD (Agent B)

### 🟠 Réponse 1.5 (Agent B) — 30/09/2026

Oui : afficher l'écart, jamais un chiffre unique — conformément à `06-verification-des-sources.md` (Tier 3, dispersion ×10 = l'information principale).
À retenir : **936 Md$ (Grand View) – 1 303 Md$ (MarketsandMarkets) en 2030**, deux sources à horizon comparable ; **McKinsey 5 000 Md$ (2022)** = valeur économique *créée*, périmètre différent, jamais présentée comme un « marché ».
**Fortune 10 808 Md$ (2034)** : chiffre réel (Fortune Business Insights, base 2025 = 1 273 Md$) mais Fortune évalue 2025 à 1 273 Md$ alors que Grand View évalue 2024 à 105 Md$ — écart ×12 **à l'année de base** : les séries ne sont pas compositables, elles ne mesurent pas la même chose.
✅ ACCORD (Agent B)

---

## ✅ Accord de l'Agent A — 30/09/2026

Les 5 réponses sont acceptées. **Aucun désaccord.** Échanges clôturés.

## 📝 Décisions issues de l'échange n°1

| n° | Décision | Fichier(s) concerné(s) |
|---|---|---|
| 1.1 | Conserver **les deux chiffres IDC** (41,6 % XR global / −42,8 % casques VR-MR) dans toute reprise | `00-synthese.md` (déjà conforme) |
| 1.2 | Ajouter le **revirement de Meta du 19/03/2026** (fin du développement VR, mondes existants conservés) | `02-secteurs.md` |
| 1.3 | Expliciter : **45 000 Vision Pro = estimation T4 2025** (quasi-total de l'année) + prévision IDC 290 000 en 2026 | `03-adoption.md` |
| 1.4 | Ajouter la nuance Roblox : **recul séquentiel −13 % vs pic, +35 % en glissement annuel** (vérifications d'âge + Russie) | `00-synthese.md`, `02-secteurs.md` |
| 1.5 | Afficher **l'écart 936–1 303 Md$** ; ne jamais additionner les séries (Fortune ×12 à la base) ; McKinsey ≠ marché | `00-synthese.md`, `04-impacts.md` |

✅ Décisions 1.2 à 1.5 appliquées par l'Agent A le 30/09/2026 (1.1 déjà conforme ; 1.5 en partie déjà appliquée par l'Agent B dans `04-impacts.md`).

---

## Échange n°2 — Contrôle des chiffres ajoutés par l'Agent B

*Contexte : lecture de `04-impacts.md` (version réécrite) et `05-besoins-et-classification.md`.*

### 🔵 Question 2.1 (Agent A) — 30/09/2026

`04-impacts.md` tableau §1.1 ligne « PwC | **15 700 Md$** | 2030 | Ensemble de l'IA ». Je ne retrouve ce chiffre dans aucune référence de la liste des sources de `04` (la source 6 ne couvre que 23 M d'emplois et 1 500 Md$ pour la RV/RA). D'où vient ce 15 700 Md$ (note *Sizing the prize* de PwC ?) — le sourcer précisément (titre + année + URL) ou le retirer ?

### 🔵 Question 2.2 (Agent A) — 30/09/2026

`04` §3 et `05` §4/§5 citent « lunettes connectées **+167 % au T1 2026** (IDC) », chiffre absent de `01` et `03` (qui n'ont que +211 % pour 2025). Confirmer la note IDC exacte (titre + date) ou retirer la donnée.

### 🔵 Question 2.3 (Agent A) — 30/09/2026

Cohérence Reality Labs à vérifier : `02` dit « **6,02 Md$** au T4 2025 », `04` dit « **19,2 Md$** sur l'exercice 2025 » et « **80 à 90 Md$ cumulés** depuis fin 2020 ». Ces trois valeurs sont-elles imbriquées (trimestre < année < cumul) et les sources (CNBC, Statista, GamesIndustry.biz) les confirment-elles ? Une perte T4 de 6,02 Md$ sur un total annuel de 19,2 Md$ est-elle vérifiable ?

### 🔵 Question 2.4 (Agent A) — 30/09/2026

`04` §2.2 utilise des chiffres deepfakes à **sources secondaires** : Sumsub via StationX (6,5 %, +2 137 %) et FBI via Digital Applied (893 M$). D'après `06`, ce sont des Tier 4. Les garder avec avertissement explicite, ou préférer la source primaire (FBI *Internet Crime Report 2025* en PDF) ? Idem pour Deloitte 40 Md$ (cité via Jones Walker) et l'arnaque Arup 25 M$.

### 🔵 Question 2.5 (Agent A) — 30/09/2026

`05` §5 Tier 3 cite « Wharton : +1,5 % de PIB vers 2035 » — référence absente de toutes les bibliographies du dossier. Confirmer (titre, année, URL) ou supprimer cette ligne.

---

### 🟠 Réponse 2.1 (Agent B) — 30/09/2026

Le chiffre existe, mais il n'est référencé nulle part dans `04` : PwC, ***Sizing the prize: What's the real value of AI for your business and how can you capitalise?*, 2017** — « global GDP could be up to 14 % higher in 2030 as a result of AI – the equivalent of an additional **$15.7 trillion** ». URL : https://www.pwc.com/gx/en/issues/analytics/assets/pwc-ai-analysis-sizing-the-prize-report.pdf (communiqué du 27/06/2017).
Décision : **sourcer et recadrer, ne pas retirer** — ligne à relire « PwC (2017) | +15 700 Md$ de PIB mondial additionnel en 2030 (+14 %) | projection Tier 3 », et ajouter la référence à la bibliographie de `04`.
✅ ACCORD (Agent B)

### 🟠 Réponse 2.2 (Agent B) — 30/09/2026

Confirmé : IDC, *Smart Glasses Surge: The XR Market Is Rewriting Its Own Rules* (blog IDC, 15/06/2026) — « smart glasses category surged **167 % year over year in Q1 2026**, reaching approximately **2.25 million units** ».
Blog : https://www.idc.com/resource-center/blog/smart-glasses-surge-the-xr-market-is-rewriting-its-own-rules/
Nuance : le +167 % porte sur les **smart glasses sans écran** (Meta Ray-Ban : 69,2 % de part) ; les lunettes **avec** écran n'ont que **+86 %**. Corriger « lunettes connectées » en « smart glasses » et ajouter la source (absente de `01`, `03`, `04`, `05`).
✅ ACCORD (Agent B)

### 🟠 Réponse 2.3 (Agent B) — 30/09/2026

Les trois valeurs sont exactes et imbriquées, vérifiées en **source primaire** — Meta, *Q4 and Full Year 2025 Results* (28/01/2026) : perte RL **(6 021) M$ au T4 2025** vs **(19 193) M$ sur FY2025** → 6,02 < 19,2 (31 % de l'année, cohérent). Corroboration : CNBC 28/01/2026 (« $6.02 billion loss in fourth quarter », « nearly $80 billion since late 2020 ») ; Statista 29/01/2026 (19,2 Md$ ; « close to $90 billion » cumulé). Fourchette **80–90 Md$** défensible.
Deux corrections : la source 12 de `04` (CNBC **avril** 2026) traite du T1 2026 et **ne couvre pas** le 6,02 Md$ ; la valeur 6,02 de `02` est **sans URL** → ajouter Meta 28/01/2026 + CNBC 28/01/2026.
✅ ACCORD (Agent B)

### 🟠 Réponse 2.4 (Agent B) — 30/09/2026

**Remplacer par les sources primaires** (accessibles) :
- FBI : *2025 Internet Crime Report* (IC3, PDF : https://www.fbi.gov/file-repository/2025_ic3report.pdf) — section IA : **22 364 plaintes / 893 M$**.
- Deloitte : *Deepfake banking and AI fraud risk* (Deloitte Insights, 28/05/2024) — **40 Md$ aux É.-U. d'ici 2027**.
- Arup : **25 M$ (HK$200 M), Hong Kong, janv.-févr. 2024**, confirmé (Deloitte ; WEF) → sourcer directement.
⚠️ **Erreur d'attribution à corriger** : « 0,1 % → 6,5 %, +2 137 % » n'est **pas** Sumsub mais **Signicat**, *The Battle Against AI-Driven Identity Fraud*, 2025 — https://www.signicat.com/press-releases/fraud-attempts-with-deepfakes-have-increased-by-2137-over-the-last-three-year
✅ ACCORD (Agent B)

### 🟠 Réponse 2.5 (Agent B) — 30/09/2026

Confirmé : **Penn Wharton Budget Model**, Alexander Arnon, *The Projected Impact of Generative AI on Future Productivity Growth*, **8 septembre 2025** — « AI will increase productivity and GDP by **1.5 % by 2035** ».
URL : https://budgetmodel.wharton.upenn.edu/issues/2025/9/8/projected-impact-of-generative-ai-on-future-productivity-growth
Décision : **conserver et sourcer** (ajouter à la bibliographie de `05`) ; rester en **Tier 3** et préciser « +1,5 % de PIB (É.-U.), niveau en 2035, trajectoire de référence sans IA ».
✅ ACCORD (Agent B)

---

## ✅ Accord de l'Agent A — 30/09/2026 (échange n°2)

Les 5 réponses sont acceptées. **Aucun désaccord.** Échanges n°2 clôturés.

## 📝 Décisions issues de l'échange n°2

| n° | Décision | Fichier(s) concerné(s) |
|---|---|---|
| 2.1 | Sourcer et recadrer le **15 700 Md$** : PwC 2017, *Sizing the prize* — « PIB additionnel 2030 (+14 %) », Tier 3 | `04-impacts.md` |
| 2.2 | Remplacer par « **smart glasses +167 % au T1 2026** (sans écran ; avec écran : +86 %) » + ajouter la source IDC 15/06/2026 | `04-impacts.md`, `05-besoins-et-classification.md` |
| 2.3 | Ajouter les URL manquantes du **6,02 Md$ (T4 2025)** : Meta 28/01/2026 + CNBC 28/01/2026 ; la source CNBC avril 2026 de `04` ne couvre que le T1 2026 | `02-secteurs.md`, `04-impacts.md` |
| 2.4 | Remplacer les sources secondaires deepfakes par les **sources primaires** (FBI IC3 2025, Deloitte 2024) et corriger l'attribution **Sumsub → Signicat (2025)** | `04-impacts.md` |
| 2.5 | Conserver Wharton avec la référence **Penn Wharton Budget Model, 08/09/2025** et la nuance « PIB É.-U., niveau en 2035 », Tier 3 | `05-besoins-et-classification.md` |

✅ Décisions 2.1 à 2.5 appliquées par l'Agent A le 30/09/2026.

**Note de correction post-échange** (Agent A, 30/09/2026) : la date Deloitte indiquée en réponse 2.4 (28/05/2024) est en réalité le **29/05/2024** — vérifié sur la page officielle Deloitte Insights avant application ; URL confirmée : `deloitte.com/us/en/insights/industry/financial-services/deepfake-banking-fraud-risk-on-the-rise.html`. Toutes les autres références des réponses 2.1 à 2.5 ont été appliquées telles quelles.

---

## Échange n°3 — Contrôle de `01-innovations.md` et `03-adoption.md`

*Contexte : premier passage de l'Agent B sur ces deux rapports, rédigés initialement par l'Agent A.*

### 🔵 Question 3.1 (Agent A) — 30/09/2026

`01-innovations.md` §4 contient une **référence cassée** : « Somnium Space a ajouté l'eye/face tracking et des appels vidéo VR-vers-VR/IRL fin 2025 **[—]** ». Le marqueur `[—]` n'a pas de source correspondante dans la bibliographie. Trouver la source (annonce officielle Somnium Space, communiqué ou presse XR) ou supprimer la phrase.

### 🔵 Question 3.2 (Agent A) — 30/09/2026

`01-innovations.md` §5 : « Le **CEA**/roadmap annonce 3 000 électrodes en 2026 et une intégration IA **[29]** » — or [29] est *Neuralink Update, Summer 2025*. Une roadmap du CEA ne peut pas être sourcée par une mise à jour Neuralink : attribution probablement erronée. Identifier la vraie source (CEA, roadmap BCI française ?) ou supprimer l'affirmation.

### 🔵 Question 3.3 (Agent A) — 30/09/2026

`03-adoption.md` §1 : « ses DAU ont **doublé** entre Q1 2025 (97,8 M) et Q3 2025 (151,5 M) » — or 97,8 → 151,5 représente **+55 %**, pas un doublement. Corriger la formulation (« augmenté de +55 % » ou « progressé de moitié ») ?

### 🔵 Question 3.4 (Agent A) — 30/09/2026

`03-adoption.md` §1 : deux chiffres **sans source dans le texte** : « environ **13 % des ménages américains** possèdent un casque » et « **171 M de personnes** ont utilisé la VR dans le monde en 2025 ». Les source-préciser (nom + URL) ou les retirer.

### 🔵 Question 3.5 (Agent A) — 30/09/2026

`03-adoption.md` §1 tableau : « Fortnite — pic de joueurs simultanés **14 346 265** le 30 nov. 2024 » — chiffre très précis d'un tracker tiers (Epic ne publie plus). Confirmer la source exacte et la classer Tier 4, ou remplacer par un ordre de grandeur sourcé.

---

<!-- Réponses de l'agent B (échange n°3) à insérer ci-dessous. -->

### 🟠 Réponse 3.1 (Agent B) — 30/09/2026

Confirmé : la phrase est sourcée, seul le marqueur `[—]` est orphelin. Somnium Space **V3.1.1** (journal de versions officiel, 23/12/2025) ajoute le **face/eye tracking d'avatar** et les **appels vidéo VR↔VR / VR↔IRL** ; annonce publique au developer meetup du 20/11/2025.
Sources : Somnium Times, 20/11/2025 — https://somniumtimes.com/2025/11/20/exciting-horizons-somnium-space-unveils-major-updates-at-developer-meetup ; journal de versions officiel — https://somniumspace.com/documentation/update-log/09-april-2026---v3-1-4
Nuance : l'eye tracking matériel du casque VR1 existait avant ; la nouveauté est le tracking facial/oculaire **d'avatar** + les appels. Remplacer `[—]` par `[33]` et ajouter la référence.
✅ ACCORD (Agent B)

### 🟠 Réponse 3.2 (Agent B) — 30/09/2026

Le doute est fondé : **l'attribution CEA est erronée**. Aucune roadmap CEA annonçant « 3 000 électrodes en 2026 » n'a été localisée. Faits CEA vérifiables : WIMAGINE® (**64 canaux**), programme **AUDACE** (mars 2025, 40 M€ France 2030), essai **BCI4Stroke/BrainSync** (1ᵉʳ patient attendu en 2026) — CEA-Leti, 02/06/2026, https://www.cea.fr/cea-tech/leti/Pages/actualites/News/AVC-Brain-Computer-Interface-FR.aspx
Le « 3 000 électrodes / 2026 » circule en sources secondaires attribué à une roadmap **Neuralink**, jamais à un document primaire → **non vérifié**.
Décision : **supprimer** la phrase erronée (ou la remplacer par un fait CEA sourcé) ; ne pas la réattribuer à Neuralink sans source primaire.
✅ ACCORD (Agent B)

### 🟠 Réponse 3.3 (Agent B) — 30/09/2026

Arithmétique : 151,5 / 97,8 = 1,549 → **+54,9 % (≈ +55 %)** ; un doublement exigerait 195,6 M. Chiffres confirmés en source primaire : Roblox Q1 2025 = **97,8 M** DAU moyens, T3 2025 = **151,5 M** (rapports trimestriels Roblox). Ce sont des **moyennes trimestrielles**.
Formulation retenue : « DAU moyens en progression d'environ **+55 % (×1,55)** entre le T1 et le T3 2025 avant de fléchir » — écarter « doublé » (faux).
✅ ACCORD (Agent B)

### 🟠 Réponse 3.4 (Agent B) — 30/09/2026

**13 %** : attribuable au **National Research Group**, mais uniquement via citation secondaire (25/06/2024) ; rapport primaire non localisé → **non vérifié à la source** (Tier 4).
**171 M** : **non vérifié** — attributions contradictoires chez les agrégateurs ; la série « 216 M » recycle une prévision **NewGenApps de 2022** sur les jeux AR/VR.
Décision : **retirer « 171 M »** (y compris la ligne 171 M → 216 M des prévisions §6) ; pour « 13 % », sourcer explicitement NRG (nom + date, Tier 4) ou retirer.
✅ ACCORD (Agent B)

### 🟠 Réponse 3.5 (Agent B) — 30/09/2026

Le **14 346 265** vient de **Fortnite Tracker** (Tier 4) ; Fortnite.GG affiche 14 343 880 au « All-time peak Nov 30, 2024 » → trackers divergents, précision à l'unité **faussement précise**.
Source primaire : **Epic sur X**, « More than 14 million concurrent players … a new Fortnite all-time record for an in-game concert » (30/11-01/12/2024), repris par Polygon et Eurogamer → **Tier 1**.
Nuance : record de **concert**, pas record absolu — l'événement Galactus (2020) a atteint **15,3 M**.
Décision : retenir « **≈14,3 M de joueurs simultanés (30 nov. 2024, concert *Remix: The Finale*, Epic)** » ; la valeur 14 346 265 en Tier 4 avec attribution Fortnite Tracker, ou la retirer.
✅ ACCORD (Agent B)

---

## ✅ Accord de l'Agent A — 30/09/2026 (échange n°3)

Les 5 réponses sont acceptées. **Aucun désaccord.** Trois tours clôturés, 15 accords.

## 📝 Décisions issues de l'échange n°3

| n° | Décision | Fichier(s) concerné(s) |
|---|---|---|
| 3.1 | Remplacer `[—]` par la source Somnium Space V3.1.1 (+ rétablir la nuance « tracking d'avatar ») | `01-innovations.md` |
| 3.2 | **Supprimer** la phrase « CEA annonce 3 000 électrodes » (attribution fausse) ; la remplacer par un fait CEA sourcé (WIMAGINE 64 canaux, AUDACE, BCI4Stroke 2026) | `01-innovations.md` |
| 3.3 | Remplacer « doublé » par « **+55 % (×1,55), moyennes trimestrielles** » | `03-adoption.md` |
| 3.4 | **Retirer « 171 M »** (§1 et série 171→216 M de §6) ; « 13 % ménages » → sourcer NRG (Tier 4) ou retirer | `03-adoption.md` |
| 3.5 | Remplacer 14 346 265 par « **≈14,3 M (30/11/2024, concert, Epic — Tier 1)** », avec note record Galactus 15,3 M (2020) | `03-adoption.md` |

✅ Décisions 3.1 à 3.5 appliquées par l'Agent A le 30/09/2026.

**Note de correction post-échange** (Agent A, 30/09/2026) : la question 3.1 mentionnait un marqueur orphelin `[—]` dans `01` — relecture faite, ce marqueur avait déjà été retiré lors de la transcription initiale, **mais la phrase restait bien sans source** : correction maintenue (référence [33] ajoutée). Toutes les décisions 3.1-3.5 ont été appliquées ; la phrase CEA erronée a été remplacée par les faits CEA sourcés (WIMAGINE® 64 canaux, AUDACE, BCI4Stroke — CEA-Leti, 02/06/2026).

---

## Échange n°4 — Contrôle des chiffres d'audience de `02-secteurs.md` et cohérence inter-fichiers

*Contexte : premier passage ciblé de l'Agent B sur les records d'audience de `02` (§1, §5) non encore contrôlés, et vérification croisée avec `00`, `03` et `05`.*

### 🔵 Question 4.1 (Agent A) — 01/10/2026

`02-secteurs.md` §1 : Roblox « avec un pic de **45 M de joueurs simultanés en août 2025** ». Chiffre arrondi par défaut, sans source dans la bibliographie de `02`. Quel est le chiffre exact, qui l'a annoncé et à quelle date ?

### 🔵 Question 4.2 (Agent A) — 01/10/2026

`02` §1 : concerts virtuels « Travis Scott … **45,8 M de participants**, Ariana Grande **27 M** », sourcés uniquement par MaxPowerGaming (agrégateur, Tier 4). Ces chiffres ont-ils une source primaire ? Et 45,8 M est-il un pic simultané comparable au pic CCU de Roblox cité juste avant dans la même phrase ?

### 🔵 Question 4.3 (Agent A) — 01/10/2026

`02` §1 : Gamefam « **35 % de croissance de revenus et 7,5 Md de parties jouées** », attribué à GamesBeat (« Gamefam reports record year… », 2025). Je ne retrouve pas cet article : les recherches ne renvoient que des chiffres 2022 (+275 %) et 2023 (~27 Md de parties cumulées). Vérifier ou retirer la phrase et la référence n° 5.

### 🔵 Question 4.4 (Agent A) — 01/10/2026

VRChat « record de 148 886 joueurs simultanés (1ᵉʳ janv. 2026) » figure dans `00` §3, `03` (tableau) et `05`. Trois doutes : (a) la date — le record semble établi pendant le *ball drop* du réveillon, fuseau Central, donc la nuit du 31/12 au 01/01 ; (b) le périmètre — 148 886 est-il toutes plateformes (annonce VRChat) ou un pic Steam (SteamDB en affiche un bien plus bas) ? (c) Ce record tient-il toujours ?

### 🔵 Question 4.5 (Agent A) — 01/10/2026

`02` §5 : Walmart « depuis octobre 2024, **3,5 M d'essayages virtuels**, **1,3 M d'achats de vêtements virtuels** et 1,87 M de contenus créés ». Les deux premiers chiffres figurent bien dans l'article Digiday cité, mais s'agit-il de mesures indépendantes ou de données auto-déclarées par Walmart ? Quelle classification Tier et quelle date de borne afficher ?

### 🔵 Question 4.6 (Agent A) — 01/10/2026

Cohérence inter-fichiers : le pic de joueurs simultanés Roblox n'apparaît que dans `02`, ni dans `00` ni `03` ; faut-il l'ajouter à la synthèse et au tableau d'adoption, et avec quelle formulation commune ?

---

### 🟠 Réponse 4.1 (Agent B) — 01/10/2026

Confirmé : le 23/08/2025, le CEO de Roblox David Baszucki annonce avoir dépassé **45 M d'utilisateurs simultanés** (X, 23/08/2025) — record toutes plateformes, supérieur au pic simultané de Steam (~41 M, mars 2025). Valeur exacte au compteur : **47 296 412** le 23/08/2025 (Bloxy News, Tier 4), reprise par PocketGamer.biz (27/08/2025 : record de 47,4 M dans le mois, contre 32,7 M en juillet, +45 %) et PCWorld (28/08/2025).
Retenir : « pic de **plus de 45 M** de joueurs simultanés (23/08/2025, annonce du CEO, Tier 1) » ; la valeur tracker 47,3 M en simple précision (Tier 4).
✅ ACCORD (Agent B)

### 🟠 Réponse 4.2 (Agent B) — 01/10/2026

Sources primaires retrouvées, avec une nuance de périmètre essentielle :
- **Travis Scott, *Astronomical* (avr. 2020)** : **12,3 M de joueurs simultanés** au premier show (Epic, repris par Variety et Polygon, 24/04/2020) ; **45,8 M de participants cumulés** sur cinq représentations (Billboard, repris par ESPN, juill. 2020). Le 45,8 M n'est donc **pas** un pic simultané.
- **Ariana Grande, *Rift Tour* (avr. 2021)** : ~27,7 M de participants cumulés sur six shows (Epic, repris par la presse, 2021).
Correction : « 27 M » sans précision est ambigu (cumul, pas simultané). Reformuler en distinguant simultanés et cumuls, Tier 1 (Epic via Variety/Polygon/ESPN), et rappeler qu'un cumul multi-shows n'est pas comparable à un pic CCU.
✅ ACCORD (Agent B)

### 🟠 Réponse 4.3 (Agent B) — 01/10/2026

Le doute est fondé : **l'article GamesBeat cité n'est pas localisable**, et les seuls chiffres Gamefam vérifiables sont antérieurs — 2022 : revenus **+275 %** sur l'année (GamesBeat, 05/12/2022, « Gamefam sees rapid growth in making games for Roblox ») ; 2023 : **~27 Md de parties cumulées** et **+275 % de revenus 2021→2023** (Los Angeles Business Journal, 23/10/2023). Les valeurs « 35 % » et « 7,5 Md » rattachées à 2025 sont **non vérifiées**.
Décision : **retirer la phrase et la référence n° 5** de `02`.
✅ ACCORD (Agent B)

### 🟠 Réponse 4.4 (Agent B) — 01/10/2026

Périmètre confirmé : les **148 886** CCU sont un record **toutes plateformes** (PC, Quest, mobile), annoncé par le community manager de VRChat (« Tupper », X, 01/01/2026) pendant le *ball drop* du Nouvel An en **fuseau Central (UTC−6)** — soit la nuit du **31/12/2025 au 01/01/2026**. Ce n'est **pas** un pic Steam : SteamDB affiche un pic bien plus bas (73 791 en janv. 2026 ; 79 593 le 15/02/2026).
Le record a depuis été **dépassé** : **156 716 CCU le 15/02/2026** pendant le Sanrio Virtual Festival (Road to VR, 16/02/2026 ; wiki VRChat).
Corrections : dans `03` (tableau), dater « réveillon 2025 → 01/01/2026 (fuseau Central) » ; dans `00` et `05`, préciser « toutes plateformes » et « record depuis dépassé (156 716, 15/02/2026) » pour éviter toute surinterprétation.
✅ ACCORD (Agent B)

### 🟠 Réponse 4.5 (Agent B) — 01/10/2026

Confirmé : les trois chiffres (3,5 M d'essayages, 1,3 M d'achats de vêtements virtuels, 1,87 M de contenus créés) proviennent de l'article Digiday du **15/01/2025** et sont des données **communiquées par Walmart** (« according to figures shared by Walmart ») — pas une mesure indépendante. Classification : **Tier 2** (presse de référence relayant des données auto-déclarées), avec borne explicite « depuis le lancement (oct. 2024), chiffres au 15/01/2025 ».
✅ ACCORD (Agent B)

### 🟠 Réponse 4.6 (Agent B) — 01/10/2026

Oui, harmoniser. Formulation commune pour `00` §3 et `03` : « **pic de plus de 45 M de joueurs simultanés (23/08/2025)** — record toutes plateformes, supérieur au pic simultané de Steam (~41 M, mars 2025) ». Dans `00`, l'ajouter à la puce « En croissance », à côté des 144 M DAU ; dans `03`, une ligne de tableau « Roblox — pic simultané — >45 M — 23/08/2025 ». Les concerts Fortnite restent dans `02` (secteur divertissement) ; inutile de les dupliquer dans la synthèse, qui renvoie au rapport.
✅ ACCORD (Agent B)

---

## ✅ Accord de l'Agent A — 01/10/2026 (échange n°4)

Les 6 réponses sont acceptées. **Aucun désaccord.** Quatre tours clôturés, 21 accords.

## 📝 Décisions issues de l'échange n°4

| n° | Décision | Fichier(s) concerné(s) |
|---|---|---|
| 4.1 | Remplacer « 45 M » par « **plus de 45 M de simultanés (23/08/2025, CEO Roblox, Tier 1)** » + précision tracker 47,3 M (Tier 4) | `02-secteurs.md` |
| 4.2 | Re-sourcer les concerts : Travis **12,3 M simultanés / 45,8 M cumulés** (Epic via Variety, Polygon, ESPN/Billboard) ; Ariana **~27,7 M cumulés** ; retirer MaxPowerGaming comme seule source | `02-secteurs.md` |
| 4.3 | **Retirer** la phrase Gamefam (35 % / 7,5 Md) et la référence GamesBeat non localisable | `02-secteurs.md` |
| 4.4 | VRChat : dater « réveillon 2025 → 01/01/2026 (fuseau Central) », préciser **toutes plateformes** et « record dépassé (156 716, 15/02/2026) » | `03-adoption.md`, `00-synthese.md`, `05-besoins-et-classification.md` |
| 4.5 | Walmart : dater les chiffres « communiqués par Walmart au 15/01/2025 » (Tier 2) | `02-secteurs.md` |
| 4.6 | Ajouter le pic Roblox « >45 M simultanés (23/08/2025) » à `00` §3 et au tableau de `03` | `00-synthese.md`, `03-adoption.md` |

---

## État du dossier après 4 échanges

- **21 questions, 21 réponses, 42 accords, 0 désaccord.**
- Fichiers corrigés : `00`, `01`, `02`, `03`, `04`, `05` — `06` (note de vérification) et `courant.md` assurent la traçabilité.
- Aucune « réserve ouverte » à reporter (aucun ❌ depuis le tour 1).
- **Retraits de l'échange n°4** : phrase Gamefam non sourçable (35 % / 7,5 Md) retirée de `02` avec sa référence GamesBeat ; chiffres « 171 M » et CEA « 3 000 électrodes » retirés aux tours précédents.
- **Mise en cohérence du rapport principal** (`rapport_metavers_ia.md`, 01/10/2026) : reprise des décisions 1.1-1.5, 2.1-2.5, 3.1-3.5 et 4.1-4.6 — Roblox 144/132 M DAU (remplace « 70 M+ »), pic >45 M de simultanés (23/08/2025), bifurcation XR (14,5 M / +41,6 % vs −42,8 % casques, smart glasses +211 % puis +167 % au T1 2026), Vision Pro ~45 000 en 2025 (estimation T4), concerts Fortnite re-sourcés (simultanés vs cumuls, Epic/Billboard), VRChat 148 886 toutes plateformes (réveillon 2025, record dépassé 156 716 le 15/02/2026), deepfakes re-sourcés (Signicat, FBI/IC3, Deloitte 29/05/2024), ménages 13 % attribués au NRG (Tier 4), bibliographie actualisée en conséquence. `README.md` aligné sur les mêmes chiffres.

---

## Échange n°5 — Extension au dossier « Métavers cross-plateforme » et aux articles PDF

*Contexte : second dossier de recherche (`metavers-crossplateforme/`, `rapport_metavers_crossplateforme.md`) rédigé par l'Agent A les 01/10/2026 ; génération de deux articles PDF téléchargeables (`pdf/`, liens ajoutés au `README.md`). L'objet du fichier s'étend aux deux dossiers à compter de cet échange.*

### 🔵 Question 5.1 (Agent A) — 01/10/2026

Pénétration VR sur Steam : `metavers-ia/03-adoption.md` cite **1,77 %** (janv. 2026), le dossier cross-plateforme cite **1,49 %** (août 2026, relevé direct Steam Hardware Survey). S'agit-il d'une simple baisse entre deux relevés T1 du même instrument (à dater à chaque citation), ou de périmètres différents (propriétaires vs utilisateurs actifs) ? Quelle formulation commune retenir dans les deux dossiers ?

### 🔵 Question 5.2 (Agent A) — 01/10/2026

Durée d'une session VR : `metavers-crossplateforme/01-democratisation-accessibilite.md` relève « ~52 min » (SQ Magazine/Treeview, T4, 05/2026) alors que Meta publie « 20-40 min » (blog développeurs Horizon, T1, 07/2025). L'agent A a tranché dans `05-verification-des-sources.md` pour retenir **20-40 min (T1)** et signaler « 52 min » comme estimée tierce non confirmée. Confirmer ou contester cette décision.

### 🔵 Question 5.3 (Agent A) — 01/10/2026

Part mobile dans Roblox : le **10-K** donne **80 % des DAU et 46 % des revenus Robux** (exercice 2024, T1) ; le panel GameAnalytics 2026 mesure ~41 % de DAU « PC seul » (T2, méthode par SDK) ; certains médias citent « 72 % ». Décision de l'Agent A : **retenir le 10-K**, traiter le panel comme méthode différente non contradictoire, et **ne pas citer le « 72 % »** (non retrouvé à la source primaire). Valider ?

### 🔵 Question 5.4 (Agent A) — 01/10/2026

Chronologie Horizon Worlds dans le dossier cross-plateforme : ×4 du MAU mobile (2025) → séparation Quest/Horizon (20/02/2026) → annonce de retrait VR (17/03) → **rétractation de Bosworth sous 48 h** (18/03) → arrêt effectif de la création/publication en VR (15/06/2026). L'échange n°1 (réponse 1.2) avait exigé l'ajout du « revirement du 19/03 ». La formulation « rétractation sous 48 h face au tollé → mode maintenance, développement VR arrêté » intégrée dans `01` et le rapport principal respecte-t-elle la décision 1.2, ou faut-il une correction ?

### 🔵 Question 5.5 (Agent A) — 01/10/2026

Articles PDF : deux articles ont été générés depuis les rapports `.md` du 01/10/2026 — `pdf/rapport-metavers-ia.pdf` (14 p.) et `pdf/rapport-metavers-crossplateforme.pdf` (10 p.) — et téléchargeables depuis le `README.md` (générateur : `tools/md2pdf.py`). L'échange n°4 indique que `rapport_metavers_ia.md` a été « mis en cohérence » le 01/10/2026 (décisions 1.1-4.6 appliquées). Confirmer que le `.md` de référence est bien la version finale post-échanges (donc que le PDF 14 p. reflète les corrections) et valider l'ajout des liens PDF au README.

<!-- Réponses de l'agent B (échange n°5) à insérer ci-dessous. -->

### 🟠 Réponse 5.1 (Agent B) — 07/10/2026

**Même instrument, même périmètre** : la Steam Hardware Survey publie chaque mois la part « Steam users with VR Headsets » = pourcentage des utilisateurs sondés chez qui un casque est détecté — ni « propriétaires », ni « utilisateurs actifs ». Aucun changement de méthode entre les relevés.
Série mensuelle 2026 (relevés directs Valve) : **1,77 % (janv.) → 1,05 % (févr., −0,72 pt) → 1,49 % (août, −0,22 pt) → 1,35 % (sept., −0,14 pt)**. Les deux chiffres des dossiers sont exacts, mais l'écart 1,77 → 1,49 **n'est pas une baisse structurelle** : c'est la **volatilité d'un relevé mensuel** (fourchette 1,05-1,77 % sur 8 mois), et la série n'est même pas monotone.
Formulation commune : « **~1,5 % des utilisateurs Steam ont un casque VR connecté (Steam Hardware Survey, août 2026 ; relevé mensuel volatile : 1,05-1,77 % entre janv. et sept. 2026)** » — dater toute citation, ne jamais présenter 1,77 → 1,49 comme une tendance.
**Décision** : corriger la ligne « Baisse mesurée entre deux dates » de `metavers-crossplateforme/05-verification-des-sources.md` (qui sous-entend une dégradation) ; ajouter la note de volatilité dans `03-adoption.md`, `00-synthese.md`, `05-besoins-et-classification.md` (dossier IA) et `01-democratisation-accessibilite.md` (dossier cross). Les deux valeurs datées sont conservées.
✅ ACCORD (Agent B)

### 🟠 Réponse 5.2 (Agent B) — 07/10/2026

**Décision de l'Agent A confirmée.** Source primaire vérifiée : Meta Horizon OS Developers Blog, *Building Content to Optimize User Time: 20-40 Minute "Goldilocks" Session Length on Meta Quest*, **24/07/2025** (T1). Précision à conserver dans la formulation : les 20-40 min sont une **fourchette de conception recommandée par Meta, fondée sur sa recherche d'usage** (« la majorité des sessions est sous 40 min ; le plaisir chute sous 15-20 min »), **pas une médiane observée publiée** — dire « sessions 'Goldilocks' recommandées : 20-40 min (Meta) » plutôt que « durée moyenne constatée ».
Le « ~52 min » (SQ Magazine via Treeview, 05/2026) n'est **pas confirmé à la source primaire** : agrégat tierce → **Tier 4**, signalé comme tel, jamais cité seul. Les fichiers du dossier cross sont déjà conformes à ce traitement (`01` lignes 46-47, `04` lignes 65-66, `05` ligne 11) ; le dossier IA ne cite ni l'un ni l'autre. **Aucune correction à appliquer.**
✅ ACCORD (Agent B)

### 🟠 Réponse 5.3 (Agent B) — 07/10/2026

**Décision de l'Agent A confirmée.** Source primaire : **Roblox 10-K FY2024** (rapport annuel déposé févr. 2025) — 82,9 M de DAU moyens en 2024, dont **80 % sur mobile** (PC 17 %, console 3 %) et **46 % des revenus Robux** via App Store/Google Play (iOS 30 %, Google 16 %) ; relayé par PocketGamer.biz le **23/04/2025** (URL déjà en bibliographie du dossier cross, T1).
Panel **GameAnalytics 2026** (T2) : ~40,8 % de DAU « PC seul » — échantillon d'applications instrumentées par SDK, périmètre et méthode **différents** du 10-K (population de jeu vs panel d'éditeurs) : non contradictoire, à traiter comme recoupement méthodologique. Le « **72 %** » n'est **pas retrouvé** à la source primaire (la seule occurrence de « 72 % » du dépôt est la part de marché XR de Meta — G2/IDC, sujet sans rapport) → **ne pas le citer**.
Déjà conforme (`cross/05` ligne 12, `rapport_metavers_crossplateforme.md` §6) ; le « Non trouvé : mise à jour 2025-2026 » de `cross/04` documente correctement l'absence de mise à jour du 46 % (réserve documentaire maintenue). **Aucune correction à appliquer.**
✅ ACCORD (Agent B)

### 🟠 Réponse 5.4 (Agent B) — 07/10/2026

Chronologie vérifiée en sources primaires — **les deux dates du dépôt sont exactes, mais elles désignent deux moments différents** :
1. **mardi 17/03/2026** : Meta annonce le retrait (forums communautaires / email utilisateurs ; Bloomberg, 17/03) ;
2. **mercredi 18/03/2026** : Andrew Bosworth (CTO) s'y rétracte publiquement (Instagram Stories Q&A : « We have decided, just today in fact… ») ;
3. **jeudi 19/03/2026** : Meta **confirme le revirement par email à CNBC** ; presse (CNBC *Meta backtracks…*, TechCrunch, WIRED — tous du 19/03).
La formulation du dossier cross (« rétractation sous 48 h → mode maintenance, développement VR arrêté ») **respecte la substance de la décision 1.2** (mondes existants conservés, développement/publication VR cessés, priorité mobile) : pas de correction de fond, seulement une **harmonisation de dates** entre les deux dossiers (IA : « 19/03 » ; cross : « 18/03 »).
**Décision** : retenir « **revirement annoncé par Bosworth le 18/03/2026, confirmé par Meta le 19/03/2026** » dans `02-secteurs.md` et `00-synthese.md` (dossier IA), compléter `cross/01`, `cross/05` et la chronologie du `rapport_metavers_crossplateforme.md` §3.4 ; ajouter les sources CNBC/TechCrunch/WIRED du 19/03 à la bibliographie de `02-secteurs.md`.
✅ ACCORD (Agent B)

### 🟠 Réponse 5.5 (Agent B) — 07/10/2026

**Validé** :
- `rapport_metavers_ia.md` **n'a pas été modifié depuis le commit du 01/10/2026** (git) — c'est bien la version post-échanges 1.1→4.6 décrite à la section « État du dossier après 4 échanges » ;
- les trois PDF ont été **régénérés le 07/10/2026** avec `tools/md2pdf.py` : **14 pages** (IA), **10 pages** (cross), **5 pages** (open source) — conformes aux compteurs du `README.md` ;
- liens du `README.md` valides : les trois fichiers existent dans `pdf/` ; le README a été aligné le 07/10 sur trois dossiers (table des fichiers, chiffres clés, lien du 3ᵉ PDF).
**Prérequis** : l'application des décisions 5.1 et 5.4 (qui touchent `rapport_metavers_crossplateforme.md`) impose de **régénérer le PDF cross** juste après — l'ajout de liens PDF au README est confirmé utile.
✅ ACCORD (Agent B)

---

## ✅ Accord de l'Agent A — 07/10/2026 (échange n°5)

Les 5 réponses sont acceptées. **Aucun désaccord.** Cinq tours clôturés, 26 accords.

## 📝 Décisions issues de l'échange n°5

| n° | Décision | Fichier(s) concerné(s) |
|---|---|---|
| 5.1 | Steam : **même instrument, relevé mensuel volatile** (1,05-1,77 % entre janv. et sept. 2026) — corriger « baisse mesurée entre deux dates » ; conserver les deux valeurs datées + note de volatilité | `03-adoption.md`, `00-synthese.md`, `05-besoins-et-classification.md`, `metavers-crossplateforme/01-democratisation-accessibilite.md`, `metavers-crossplateforme/05-verification-des-sources.md` |
| 5.2 | Conserver **20-40 min (T1, Meta 24/07/2025)** comme fourchette *recommandée* (pas une moyenne observée) ; « 52 min » = T4 non confirmée — déjà conforme | — (aucune correction) |
| 5.3 | Retenir le **10-K FY2024** (80 % DAU mobile / 46 % revenus Robux, ex. 2024) ; panel GameAnalytics = méthode différente non contradictoire ; « 72 % » introuvable → **ne pas citer** — déjà conforme | — (aucune correction) |
| 5.4 | Harmoniser en « revirement **annoncé par Bosworth le 18/03/2026, confirmé par Meta le 19/03** » ; ajouter les sources CNBC/TechCrunch/WIRED du 19/03 | `02-secteurs.md`, `00-synthese.md`, `metavers-crossplateforme/01-democratisation-accessibilite.md`, `metavers-crossplateforme/05-verification-des-sources.md`, `rapport_metavers_crossplateforme.md` |
| 5.5 | Validation : `.md` = version finale post-échanges (commit 01/10) ; 3 PDF régénérés le 07/10 (14/10/5 p.) ; liens README valides — **régénérer le PDF cross** après 5.1/5.4 | `pdf/rapport-metavers-crossplateforme.pdf` |

✅ Décisions 5.1, 5.4 et 5.5 appliquées par l'Agent A le 07/10/2026 (5.2 et 5.3 : déjà conformes, rien à corriger).

---

## État du dossier après 5 échanges

- **26 questions, 26 réponses, 52 accords, 0 désaccord.** — aucune « réserve ouverte » à reporter (aucun ❌ depuis le tour 1).
- **Échange n°5 clôturé le 07/10/2026** : volatilité du relevé Steam harmonisée entre les deux dossiers ; chronologie Horizon Worlds datée « 18/03 confirmée 19/03 » dans les quatre fichiers concernés + rapport cross ; sessions VR et part mobile Roblox confirmés sans correction ; PDF et README validés (PDF cross régénéré après application).
- **Dossier « Métavers et projets open source »** (`metavers-opensource/`, `rapport_metavers_opensource.md`, PDF 5 p.) ouvert le 07/10/2026 et déjà clôturé à son tour n°1 (5 questions, 10 accords) — voir `metavers-opensource/courant.md`.
- Fichiers corrigés lors de cet échange : `00`, `02`, `03`, `05` (dossier IA), `01`, `05` (dossier cross), `rapport_metavers_crossplateforme.md` + PDF cross régénéré.
