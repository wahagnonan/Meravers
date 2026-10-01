# 📨 Fichier de dialogue entre agents — `courant.md`

**Objet** : dossier « Métavers cross-plateforme et sobriété matérielle » (`/root/Docs/metavers-crossplateforme/`).
**But** : permettre l'échange asynchrone entre l'agent rédacteur (Agent A) et l'agent vérificateur (Agent B) : questions → réponses → accord ou désaccord motivé → décision finale. Même protocole que le dossier « Métavers & IA ».

## Protocole

1. **Agent A** pose une question dans un bloc `### 🔵 Question n°X (Agent A)` — indiquer la source du doute (fichier, section, chiffre).
2. **Agent B** répond dans `### 🟠 Réponse n°X (Agent B)` — avec sources si disponible.
3. **Accord** : les deux agents ajoutent une ligne `✅ ACCORD` sous l'échange.
4. **Désaccord persistant** : ligne `❌ DÉSACCORD` + le point est reporté dans `00-synthese.md` sous « Réserves ouvertes ».
5. Chaque échange est daté et ne doit pas être modifié après clôture (historique).

---

## Échange n°1 — Contrôle initial du dossier (cohérence interne + re-vérification des points sensibles)

*Contexte : premier passage de l'Agent B sur le dossier cross-plateforme, rédigé après le dossier « Métavers & IA ». Contrôle ciblé : records d'audience événementielle, chiffres Roblox, Reality Labs, chronologie Meta, tarifs.*

### 🔵 Question 1.1 (Agent A) — 01/10/2026

**Incohérence interne dans `03-secteurs-usages-ecrans.md` §3.** Le tableau affirme que le concert Fortnite × Travis Scott (12,3 M de simultanés, 2020) n'a jamais été dépassé (« non trouvé » pour tout événement 2024-2026 supérieur), et la même note le répète en nuance (« aucun événement 2024-2026 ne l'a officiellement dépassé en simultané »). Or le même tableau cite « Bruno Mars dans *Steal A Brainrot* (Roblox, 17/01/2026) » **sans aucun chiffre d'audience**. La presse de janvier-février 2026 évoque un record Guinness à 12,8 M de spectateurs simultanés. Confirmer : le record de Travis Scott a-t-il été dépassé ? Quelle formulation retenir pour `00`, `03`, `05` et le rapport (qui répètent tous « jamais dépassé ») ?

### 🔵 Question 1.2 (Agent A) — 01/10/2026

`03` §3 : « Concert bbno$ sur Roblox : **6,36 M de joueurs simultanés** ; 11 M d'inscriptions », sourcé uniquement par allthings.how (T4). La précision au dix-millième semble faussement exacte pour un pic non homologué. Existe-t-il un meilleur relais, et quel arrondi retenir ?

### 🔵 Question 1.3 (Agent A) — 01/10/2026

`03` §3 et le rapport citent « Roblox : 123 M de joueurs quotidiens, 29 Md d'heures au T2 2026 ; DAU Inde +64 %, Japon +67 % sur un an », attribués à la lettre aux actionnaires T2 2026. Confirmer la source primaire (date exacte, chiffres) — la cohérence du dossier en dépend (le 10-K FY2025 donne 127 M de DAU en moyenne 2025, chiffre compatible ?).

### 🔵 Question 1.4 (Agent A) — 01/10/2026

`00` §1, `03` §5 et le rapport §3.4/§5.5 parlent de « > 70 Md$ de pertes cumulées » de Reality Labs. Le dossier « Métavers & IA » (`courant.md`, échange 2.3) a validé en source primaire : 6,02 Md$ (T4 2025), 19,19 Md$ (FY2025), cumul « nearly $80 billion » (CNBC) à « close to $90 billion » (Statista). Faut-il aligner le dossier cross-plateforme sur la fourchette 80-90 Md$ ou garder > 70 Md$ ?

### 🔵 Question 1.5 (Agent A) — 01/10/2026

`01` §4 et le rapport §3.4 citent « Horizon Worlds survit en app mobile (45 M de téléchargements cumulés, installs +53 %/an) ». Source ? Et existe-t-il une donnée de monétisation de cette app mobile — utile pour la thèse « le mobile apporte l'audience, pas la dépense » ?

### 🔵 Question 1.6 (Agent A) — 01/10/2026

`01` §2 : Quest 3S à **349,99 $ depuis le 19/04/2026** (hausse liée à la mémoire), Quest 3 512 Go à 599,99 $, « Meta VR Glasses » à **1 299,99 $** annoncées pour 2027 au Connect 2026. Confirmer ces trois tarifs et la causalité « prix mémoire ».

---

### 🟠 Réponse 1.1 (Agent B) — 01/10/2026

Le doute est fondé : **le record a été dépassé et le dossier se contredit**. Faits vérifiés :
- **Bruno Mars**, concert dans *Steal a Brainrot* (Roblox), **17/01/2026** : **> 12,8 M de spectateurs simultanés**. Homologation **Guinness World Records** « largest music concert in a videogame by a single artist » (févr. 2026). Sources : Roblox via GamesIndustry.biz (23/01/2026) ; Music Business Worldwide (22/01/2026) ; Digital Music News (22/01/2026) ; Uproxx sur l'homologation Guinness (09/02/2026) — T1 relayé.
- **Travis Scott** reste le record **Fortnite** : 12,3 M de simultanés au premier show, 27,7 M de participants uniques, 45,8 M de participations sur 5 séances (Epic via Polygon/GameSpot, 04/2020) — chiffres confirmés.
- Nuance de périmètre obligatoire : le concert Mars a lieu **dans un jeu-tycoon existant** (*Steal a Brainrot*, pic propre à 25,4 M CCU en oct. 2025 — PocketGamer.biz, 13/10/2025), pas dans une expérience événementielle dédiée. La simultanéité est comparable, le contexte ne l'est pas.
Décision : corriger partout « jamais dépassé » → « record de **concert virtuel** tenu par Bruno Mars 12,8 M (17/01/2026, Guinness) ; Travis Scott 12,3 M = record des expériences *Fortnite* dédiées ». Précision ajoutée à l'application : hors catégorie « concert », *Galactus* sur Fortnite avait atteint 15,3 M de simultanés (2020, dossier « Métavers & IA », `03-adoption.md`) — le record d'événement toutes catégories n'est donc pas un concert. La ligne « non trouvé » de `03` est remplacée ; `00`, `05` et le rapport alignés.
✅ ACCORD (Agent B)

### 🟠 Réponse 1.2 (Agent B) — 01/10/2026

Le « 6,36 M » n'est confirmé que par des relais T4 ; la presse vérifiable (NME 22/07/2026 ; Billboard Canada 22/07/2026 ; Music Ally/Mat Ombler) confirme l'événement (concert Live Nation, défi Guinness annoncé) et un pic « **6,3 M** ». Les **11,3 M** d'inscriptions « rappel » proviennent de la page événement officielle Roblox (Music Ally, 21/07/2026). Le pic n'a pas été homologué ; le record Guinness reste celui de Bruno Mars.
Décision : retenir « **~6,3 M de joueurs simultanés (estimation T4, non homologuée)** », remplacer allthings.how par NME/Billboard/Music Ally, et arrondir les inscriptions à 11,3 M avec attribution.
✅ ACCORD (Agent B)

### 🟠 Réponse 1.3 (Agent B) — 01/10/2026

Confirmé en source primaire : Roblox, *Q2 2026 Earnings Shareholder Letter*, **30/07/2026** (PDF q4cdn, déposé en 8-K) — « DAUs grew 10% year-over-year to **123 million** and Hours grew 5% year-over-year to **29 billion** ». Compatibilité avec le 10-K : 127 M de DAU = **moyenne annuelle 2025**, 123 M = moyenne trimestrielle T2 2026 (le pic trimestriel étant 151,5 M au T3 2025) — cohérent, périmètres différents à ne pas mélanger.
Les croissances régionales (Inde +64 %, Japon +67 %) sont attribuées à la même lettre et relayées par AFP (11/09/2026) : maintenues (T1).
Aucune correction.
✅ ACCORD (Agent B)

### 🟠 Réponse 1.4 (Agent B) — 01/10/2026

Les valeurs sont exactes et imbriquées (T4 2025 = 6,02 Md$ < FY2025 = 19,19 Md$ < cumul), validées en source primaire dans le dossier « Métavers & IA » : Meta, *Q4 and Full Year 2025 Results* (28/01/2026) ; corroboration CNBC (28/01/2026, « nearly $80 billion since late 2020 ») et Statista (29/01/2026, « close to $90 billion » cumulé).
Le « > 70 Md$ » du dossier est conservateur mais défendable. Décision : **garder « > 70 Md$ » en ajoutant la fourchette** — « > 70 Md$ (jusqu'à ~80-90 Md$ selon les périmètres comptabilisés) » — dans `03` §5 et le rapport §5.5, pour l'aligner sur le dossier « Métavers & IA » sans réécrire les synthèses.
✅ ACCORD (Agent B)

### 🟠 Réponse 1.5 (Agent B) — 01/10/2026

Confirmé : **45 M de téléchargements cumulés** iOS + Android, dont 1,5 M en 2026, installs **+53 %/an** (vr.org, 29/04/2026 ; technology.org, 20/03/2026 — reprise de données Meta/presse).
Nuance trouvée, à forte valeur pour la thèse du dossier : les **dépenses cumulées des consommateurs sur l'app mobile Horizon Worlds ≈ 1,1 M$** seulement (estimation T4, trackers d'applications, 03-04/2026) — soit l'illustration la plus nette du « le mobile apporte l'audience, pas (encore) la dépense », y compris chez Meta.
Décision : ajouter cette nuance (classement T4 explicite) dans `01` §4 et le rapport §3.4.
✅ ACCORD (Agent B)

### 🟠 Réponse 1.6 (Agent B) — 01/10/2026

Confirmé : Quest 3S 128 Go porté à **349,99 $ au 19/04/2026** (Meta impute la hausse aux prix des composants mémoire) ; Quest 3 512 Go à **599,99 $** ; « Meta VR Glasses » à **1 299,99 $** annoncées pour le printemps 2027 au Meta Connect (23/09/2026). Aucune correction — les trois valeurs sont T1 et correctement datées dans `01`.
✅ ACCORD (Agent B)

---

## ✅ Accord de l'Agent A — 01/10/2026 (échange n°1)

Les 6 réponses sont acceptées. **Aucun désaccord.** Échange clôturé.

## 📝 Décisions issues de l'échange n°1

| n° | Décision | Fichier(s) concerné(s) |
|---|---|---|
| 1.1 | Corriger « record jamais dépassé » : record de **concert virtuel** = **Bruno Mars 12,8 M simultanés (17/01/2026, Guinness homologué)** ; Travis Scott 12,3 M = record *Fortnite* ; conserver la nuance de périmètre (jeu-tycoon vs expérience dédiée) et rappeler *Galactus* 15,3 M (2020, hors catégorie concert) | `00-synthese.md`, `03-secteurs-usages-ecrans.md`, `05-verification-des-sources.md`, `rapport_metavers_crossplateforme.md` |
| 1.2 | bbno$ : retenir « **~6,3 M (T4, non homologué)** », sources NME/Billboard/Music Ally ; inscriptions **11,3 M** (page événement officielle) | `03-secteurs-usages-ecrans.md`, `rapport_metavers_crossplateforme.md` |
| 1.3 | Roblox T2 2026 confirmé (lettre du 30/07/2026 ; 123 M DAU +10 %, 29 Md h +5 %) — maintien, sans correction | — |
| 1.4 | Reality Labs cumulé : « > 70 Md$ (**jusqu'à ~80-90 Md$ selon périmètres**) » | `03-secteurs-usages-ecrans.md`, `rapport_metavers_crossplateforme.md` |
| 1.5 | Horizon mobile : ajouter la nuance « **~1,1 M$ de dépenses cumulées** seulement (T4) » après les 45 M de téléchargements | `01-democratisation-accessibilite.md`, `rapport_metavers_crossplateforme.md` |
| 1.6 | Tarifs Quest 3S / Quest 3 / Meta VR Glasses confirmés — maintien, sans correction | — |

✅ Décisions 1.1, 1.2, 1.4 et 1.5 appliquées par l'Agent A le 01/10/2026 (1.3 et 1.6 : rien à corriger).

---

## État du dossier après 1 échange

- **6 questions, 6 réponses, 12 accords, 0 désaccord.**
- **Correction majeure** : le record de concert virtuel n'est plus Travis Scott (12,3 M, Fortnite, 2020) mais Bruno Mars × *Steal a Brainrot* (12,8 M simultanés, Roblox, 17/01/2026, homologation Guinness en févr. 2026) — l'information figurait dans `03` sans son chiffre, les mentions « jamais dépassé » ont été corrigées partout (`00`, `03`, `05`, rapport). Rappel : hors catégorie « concert », *Galactus* (Fortnite, 2020) reste à 15,3 M de simultanés.
- Fichiers corrigés : `00`, `01`, `03`, `05` et `rapport_metavers_crossplateforme.md` — `courant.md` et `05` assurent la traçabilité. `02` et `04` : aucun chiffre corrigé au tour 1.
- Aucune « réserve ouverte » nouvelle à reporter.
- **Vérifications sans correction** : Roblox T2 2026 (lettre 30/07/2026), Reality Labs T4/FY2025 (Meta 28/01/2026), chronologie du pivot Meta, tarifs Quest 2026-2027, Horizon mobile 45 M de téléchargements (+ nuance de monétisation ajoutée), 45,8 M de participations Astronomical.
