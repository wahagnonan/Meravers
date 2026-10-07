# Métavers et projets open source : comment les exploiter au service du développement et de l'adoption du métavers

**Rapport principal — Dossier de recherche du 7 octobre 2026**
Méthode et sources : hiérarchie Tier 1-4, distinction stricte données constatées / projections, conforme à la note de vérification `metavers-opensource/05-verification-des-sources.md`.

---

## 1. Cadrage : la question du jour

> **« Comment exploiter les projets open source au service du développement et de l'adoption du métavers ? »**

La question suppose que l'open source est un *levier* à activer. Le travail de vérification montre une réalité antérieure et plus forte : **le socle du métavers est déjà ouvert** — standards, moteurs, outils de création, modèles de génération 3D. La question n'est donc pas « faut-il de l'open source ? » mais **« à quelle fonction l'affecter pour qu'il produise de l'adoption, et où s'arrête son effet ? »**.

Ce rapport répond en quatre temps : le socle (§2), la chaîne de production (§3), l'IA ouverte (§4), les leviers d'adoption et leurs limites (§5-6), puis les recommandations (§7).

**Méthode.** Chaque affirmation chiffrée porte une source nominative, une date et un niveau de confiance : **Tier 1** (source primaire : W3C, Khronos, Linux Foundation, éditeurs, publications), **Tier 2** (presse de référence, intermédiaire institutionnel), **Tier 3** (projections de cabinet, blogs de comparaison), **Tier 4** (tracker, agrégateur). Les lacunes documentaires sont listées, pas comblées par estimation.

---

## 2. Le socle : les standards ouverts ont déjà gagné la couche technique

| Couche | Projet | Statut vérifié | Tier |
|---|---|---|---|
| Immersion navigateur | **WebXR** | *Candidate Recommendation Draft* **01/10/2025** ; **pas** *Baseline* ; absent de Safari/iOS | T1 |
| Rendu Web | **WebGPU** | Activé **par défaut** sur macOS/iOS/iPadOS/visionOS **26** ; statut *Baseline* confirmé au **02/06/2026** (MDN/gpuweb) | T1 |
| Accès matériel XR | **OpenXR 1.1** | **15/04/2024** ; conformes : Meta, Microsoft, Sony, HTC, PICO, Valve, Google, Collabora | T1 |
| Contenus 3D | **glTF 2.0** | Standard de fait du Web 3D et du temps réel | T2 |
| Avatars | **VRM** (extension glTF) | Collaboration **Khronos × VRM Consortium**, **24/10/2024** | T1 |
| Scènes industrielles | **OpenUSD** | Alliance for OpenUSD (Linux Foundation) ; socle natif d'NVIDIA Omniverse | T1 |
| Runtime XR | **Monado** | Runtime OpenXR open source (Collabora) ; sous Android XR, NVIDIA CloudXR, PICO, Snapdragon Spaces (24/06/2026) | T2 |

**Trois enseignements.**

1. **Il n'existe aucun « maillon manquant » propriétaire.** Tous les géants (Meta, Google, Microsoft, Sony) sont conformes à un standard ouvert : l'interopérabilité matérielle est réglée au niveau de l'API.
2. **Standard ouvert ≠ service ouvert.** WebXR existe au W3C depuis 2019 mais reste indisponible sur Safari/iOS (bug WebKit ouvert, 02/06/2026) : l'accès « sans casque » repose en réalité sur **WebGPU et le pixel streaming**, pas sur WebXR immersif. Un standard sans implémentation ne démocratise rien.
3. **Les gouvernances sont collectives.** Les deux fondations « métavers » — **Open Metaverse Foundation** (18/01/2023) et **Open 3D Foundation** (06/07/2021) — sont hébergées par le **Linux Foundation**, modèle qui a fait ses preuves pour le cloud et les conteneurs. Le **Metaverse Standards Forum** (2022, 35 membres fondateurs) travaille sur l'interopérabilité, mais **aucune mesure d'adoption n'y figure sur son site au 07/10/2026** (absence constatée, classée lacune documentaire).

**Réserve de fond** : aucun standard ouvert ne couvre le **compte utilisateur, la progression ou la propriété des objets** — c'est précisément là que se joue le verrouillage des plateformes.

---

## 3. La chaîne de production ouverte — complète, mais finançée par un cercle étroit

### 3.1 Cartographie

| Étage | Projet | Licence | Repère vérifié |
|---|---|---|---|
| Moteur d'univers | **Godot** | MIT | ~**2 M de téléchargements par version stable** ; jeux sur Steam en croissance « exponentielle » ; communauté **doublée en deux ans** (article officiel, 06/05/2026) |
| Moteur industriel | **O3DE** | Apache 2.0 | Open 3D Foundation (Linux Foundation), 06/07/2021 |
| Modélisation 3D | **Blender** | GPL | Revenus **4,2 → 5,7 M€ (+36 %)** en 2025 (rapport annuel, 23/09/2026) ; **exercice 2024 déficitaire** |
| Web 3D | **Three.js** | MIT | ≈ **12,2 M téléchargements npm/semaine** (24/09/2026), ≈ **40×** Babylon.js |
| Création d'assets | **glTF / VRM** | Khronos / VRM Consortium | Portabilité des assets et des avatars |
| IA 3D | **Cube 3D** (Roblox), **Hunyuan3D** (Tencent) | Publiés | Voir §4 |

### 3.2 Deux enseignements stratégiques

**a) L'adoption open source est d'abord une réaction au risque perçu.** L'annonce du *Runtime Fee* par Unity (sept. 2023) et sa révocation le **12/09/2024** (source primaire Unity) sont suivies d'une hausse très forte des téléchargements Godot, qualifiée de « **doublement de la base d'utilisateurs en un mois** » par la presse spécialisée (Tier 2, 27/03/2024 — métrique exacte non communiquée comme telle par Godot, et non reprise par son article officiel du 06/05/2026). Le déclencheur n'était pas la philosophie du libre, mais la découverte qu'un éditeur peut changer unilatéralement les conditions d'un investissement pluriannuel. Pour le métavers — où l'on stocke des années de contenu — c'est l'argument d'adoption n°1.

**b) L'adoption ne finance pas l'open source.** L'article officiel Godot l'écrit sans détour : le *Development Fund* (sept. 2023) est **resté stable** alors que la base d'utilisateurs a doublé, et l'auteur liste lui-même trois hypothèses (perception « projet déjà installé », message de valeur mal perçu, lecture « simple alternative gratuite »). Blender, lui, a connu un **déficit en 2024** avant de retrouver +36 % de revenus en 2025, avec des mécènes corporatifs qui évoluent (Chaos, 07/2025 ; **Anthropic**, 29/04/2026).

> **Risque structurel** : l'écosystème ouvert du métavers repose sur un cercle restreint de financeurs industriels (NVIDIA, AMD, Apple, Intel, Google, Meta…). Une déprise de l'un d'eux ralentit le socle dont dépendent *toutes* les plateformes, y compris propriétaires.

---

## 4. L'IA générative ouverte : le levier de coût le plus puissant

Générer un monde 3D coûte cher en calcul et en données ; publier les poids du modèle est le seul moyen de rendre cette capacité accessible aux petits studios. C'est explicitement la stratégie de Roblox :

- **Cube 3D** : *« open-sourcing the first release … to make it available for use by anyone **on or off the Roblox platform** »* (newsroom Roblox, **17/03/2025**). Modèle de **1,8 Md de paramètres** entraîné sur **1,5 M d'assets 3D**, publié sur GitHub **et** HuggingFace, avec publication scientifique (arXiv 2503.15475, 19/03/2025) et version v0.5 (juil. 2025).
- **Hunyuan3D 2.0 / 2.1** (Tencent) : poids et code d'inférence publiés le **21/01/2025**, puis le **14/06/2025**, sous **Tencent Hunyuan Community License** → **open weights** (non conforme OSI).
- **PNJ à modèle local** : un petit modèle quantifié tourne **sur le GPU du joueur** (llama.cpp, 8B/4 bits) — démontré en recherche (arXiv, 11/11/2025) et intégré aux SDK NVIDIA ACE (20/02/2025). Conséquence : des PNJ persistants **sans coût d'appel API**, condition de faisabilité pour les expériences communautaires.

### La frontière qu'il faut assumer : « open source » ≠ « poids publiés »

L'**Open Source Initiative** a publié sa *Open Source AI Definition* (**OSAID 1.0**) le **28/10/2024** : un système open source doit être librement utilisable, étudiable, modifiable **et partageable**. La publication des poids seuls ne satisfait pas cette définition si les données et le processus restent indisponibles (débat documenté, 03-04/2025). D'où la règle de rédaction de ce dossier :

- **open source** → Godot, Blender, Three.js, O3DE, Monado, glTF, WebXR ; **Cube 3D (Roblox)** — modèle publié, licence d'usage large (fichier LICENSE à confirmer) ;
- **open weights** → **Llama (Meta)**, **Hunyuan3D (Tencent)** ;
- et le constat du **MIT Sloan (20/01/2026)** : les utilisateurs **choisissent 80 % du temps des modèles fermés**, malgré des coûts et performances compétitifs.

L'openness n'est donc pas encore un critère de choix majoritaire — c'est un *potentiel* inexploité.

---

## 5. Les quatre leviers d'adoption par l'open source

| # | Levier | Mécanisme | Effet mesurable |
|---|---|---|---|
| 1 | **Coût d'entrée nul** | Pas de licence par siège, pas de royalty (Godot MIT) ; **Unreal = gratuit + 5 % au-delà de 1 M$ (licence Epic, Tier 1)** ; Unity = abonnement par siège (ordre de grandeur ~2 000-2 400 $/siège/an, **Tier 3**) | Barrière à l'entrée = 0 pour créateurs et studios indépendants |
| 2 | **Interopérabilité multi-écrans** | WebGPU/OpenXR/glTF/VRM permettent de porter une expérience sur PC, mobile et casque | Condition technique de l'audience mobile (80 % des DAU Roblox, 10-K) |
| 3 | **Vivier de compétences** | Communauté Godot **doublée en 2 ans** ; jeux sur Steam en croissance « exponentielle » ; game jams en hausse (Global Game Jam, GMTK) | Formation de la génération montante sur des outils ouverts |
| 4 | **Réduction du risque perçu** | Code récupérable, standards portables, absence de conditions unilatérales | Épisode Unity (2023-2024) et hausse des téléchargements Godot qui suit (Tier 2) |

### Le fait le plus décisif du dossier : la pérennité

**Mozilla** a mis fin au support de **Hubs** le **31/05/2024** (source primaire Mozilla) — mais Hubs étant open source, **la communauté a repris le code (« Hubs Community Edition »), toujours disponible en octobre 2026**.

**Distinction de pérennité** (échange n°1, décision 1.5) : **le code survit** (garanti : dépôt public forkable) ; **le service survit** (conditionné aux contributeurs). C'est la *possibilité de reprise* qui est l'argument, pas une promesse de continuité automatique.

À l'inverse, dans le modèle propriétaire, les fermetures **effacent les mondes** : Rec Room (01/06/2026), Spatial créateur (27/07/2026), Microsoft Mesh (12/2025), Meta Workrooms (02/2026), arrêt du développement VR d'Horizon Worlds (15/06/2026) — les utilisateurs n'ont rien pu récupérer.

> **Conclusion opérationnelle** : l'open source est la **seule garantie qu'un univers virtuel survive à son éditeur**. C'est l'argument le plus fort à faire valoir auprès de toute institution (éducation, musées, collectivités) qui investit du temps de création dans une plateforme.

---

## 6. Ce que l'open source ne fait pas — les limites honnêtes

1. **Il ne crée pas l'audience.** Les plateformes qui captent réellement les utilisateurs — Roblox (123 M DAU au T2 2026), Fortnite, Horizon Worlds mobile — sont **propriétaires** ; leurs comptes, avatars et économies ne sont pas ouverts. L'open source équipe les alternatives, pas le trafic.
2. **Il ne règle pas l'interopérabilité sociale.** Aucun avatar, aucune progression, aucun objet n'est portable entre plateformes ; le chantier VRM × Khronos (24/10/2024) en est au stade de la standardisation, pas du déploiement.
3. **Son financement est fragile et concentré** (§3.2b) — adoption en hausse, fonds stables.
4. **Il n'a pas de support par défaut** : pas de SLA, dépendance à la contribution bénévole sur des briques critiques (runtimes, moteurs).
5. **Le vocabulaire est piégé** : des projets largement présentés comme « open source » (Llama, Hunyuan3D) sont sous licences communautaires ; les présenter comme tels décrédibilise l'argumentaire.

---

## 7. Recommandations : une affectation par fonction

Pour répondre directement à la question du jour, l'exploitation de l'open source doit être **affectée à quatre fonctions distinctes**, avec un indicateur d'adoption pour chacune :

| Fonction | Projets à exploiter | Indicateur d'adoption à suivre |
|---|---|---|
| **1. Socle technique (portabilité)** | WebGPU/WebXR, OpenXR 1.1, glTF, VRM, OpenUSD | Évolution du statut *Baseline* de WebXR (intégration Safari/iOS) ; nombre de plateformes conformes |
| **2. Chaîne de création (coût)** | Blender, Godot, Three.js, Monado, O3DE | Téléchargements Godot **par version** (pas convertis en « utilisateurs ») ; revenus du Blender Development Fund |
| **3. Génération de contenus (échelle)** | Roblox Cube 3D, Hunyuan3D, SLM locaux pour PNJ | Licences réellement appliquées (GitHub LICENSE) ; premier déploiement grand public de PNJ locaux |
| **4. Pérennité (confiance)** | Open Metaverse Foundation, code source récupérable, auto-hébergement | Nombre de reprises communautaires après arrêt d'un service (type Hubs) |

**Recommandations opérationnelles :**

1. **Exiger l'ouverture comme critère d'investissement** : tout projet éducatif, culturel ou institutionnel doit choisir un socle dont le code est récupérable (règle « que se passe-t-il le jour où l'éditeur ferme ? »).
2. **Standardiser avant de construire** : glTF/VRM pour les assets et avatars, OpenXR/WebXR pour l'accès — c'est ce qui rend le cross-plateforme (donc l'audience mobile) possible.
3. **Financer plutôt que consommer** : l'écart adoption/financement (Godot) est le principal risque systémique ; un pourcentage du budget d'un projet ouvert doit retourner aux fonds de développement (Godot Development Fund, Blender Development Fund).
4. **Ne jamais promettre ce que l'open source ne fait pas** : il ne remplace ni la distribution, ni la communauté, ni l'interface. C'est une **condition nécessaire, non suffisante**, de l'adoption.
5. **Être rigoureux sur le vocabulaire** : distinguer *open source*, *open weights* et *source available* dans toute communication — sinon l'argument se retourne.

---

## 8. Réserves ouvertes

1. **Prix Unity** (ordre de grandeur ≈ 2 000-2 400 $/siège/an) : **Tier 3**, blogs spécialisés 2026 — confirmation sur unity.com requise avant reprise externe. **Unreal (5 % > 1 M$)** : confirmé en licence officielle (Tier 1).
2. **Godot « ~2 M »** : téléchargements **par version stable**, pas utilisateurs (réserve méthodologique de Godot lui-même, données jusqu'à févr. 2026).
3. **« Godot a doublé sa base en un mois »** : Tier 2, pas de source Godot primaire.
4. **Le Metaverse Standards Forum** (2022, 35 membres fondateurs) : activités et initiatives publiées, **aucune mesure d'adoption au 07/10/2026** (lacune).
5. **Licences** : périmètre exact de `Roblox/cube` et `Hunyuan3D-2` (usage commercial) à confirmer au niveau des fichiers LICENSE.
6. **Lacunes** : part des contenus créés avec des outils ouverts ; nombre d'expériences WebXR en production ; budget de l'Open Metaverse Foundation ; audience réelle des PNJ locaux.

---

## Fiches thématiques du dossier

- `metavers-opensource/00-synthese.md` — synthèse et réponse à la problématique
- `metavers-opensource/01-standards-interopabilite.md` — Axe 1 : standards et gouvernances
- `metavers-opensource/02-moteurs-outils-ouverts.md` — Axe 2 : moteurs et outils
- `metavers-opensource/03-ia-generative-ouverte.md` — Axe 3 : IA générative ouverte
- `metavers-opensource/04-adoption-communautes-economie.md` — Axe 4 : adoption, économie, pérennité
- `metavers-opensource/05-verification-des-sources.md` — contrôle qualité, Tier 1-4, lacunes
- `metavers-opensource/courant.md` — dialogue inter-agents (questions/réponses/décisions)
