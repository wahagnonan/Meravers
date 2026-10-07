# Axe 3 — IA générative ouverte : les modèles qui fabriquent les mondes

**Dossier « Métavers et projets open source » — note 3/4**
Méthode : chaque affirmation est sourcée (nom, date, URL) et classée **Tier 1-4** (voir `05-verification-des-sources.md`).

---

## 1. Pourquoi l'open source est déterminant ici

Générer un monde 3D coûte très cher en calcul et en données. Un studio indépendant ne répliquera jamais un tel effort — **sauf si les poids du modèle sont publiés**. C'est exactement la stratégie qu'a annoncée Roblox : *« open-sourcing the first release for this model to make it available for use by anyone **on or off the Roblox platform** »* (Roblox Newsroom, 17/03/2025).

L'IA générative 3D est ainsi le **premier domaine où l'open source ne se contente pas d'outiller le métavers : il en abaisse le coût d'entrée de création de plusieurs ordres de grandeur.**

---

## 2. L'état des modèles ouverts de génération 3D

| Projet | Éditeur | Statut & licence | Donnée vérifiée | Tier |
|---|---|---|---|---|
| **Cube 3D** | **Roblox** | Modèle publié (GitHub + HuggingFace), licence d'usage large y compris hors plateforme — *fichier LICENSE à confirmer avant usage commercial* | Fondation **1,8 Md de paramètres** entraînée sur **1,5 M d'assets 3D** ; v0.5 (juil. 2025) : composition 3D plus fidèle + *bounding box conditioning* ; publication initiale **17/03/2025** ; article arXiv **2503.15475** (19/03/2025) | T1 |
| **Hunyuan3D 2.0 / 2.1** | **Tencent** | Dépôt GitHub sous **Tencent Hunyuan Community License** → classé **open weights** (non conforme OSI) + API cloud | Code d'inférence et poids publiés le **21/01/2025** ; v2.1 le **14/06/2025** ; génération d'assets texturés haute résolution | T1 |
| **Modèles de langage pour PNJ** | Meta (Llama), Mistral, Google (Gemma) | Poids ouverts, licences variables | Voir §3 | T1/T2 |
| **Stable Diffusion** (2D, textures) | Stability AI | Poids ouverts (CreativeML OpenRAIL) | Socle de la plupart des pipelines de textures | T2 |

**Roblox Cube** est le cas le mieux documenté du dossier : outil de *text-to-3D mesh* utilisé dans la plateforme **et** disponible hors plateforme (GitHub + HuggingFace), avec publication scientifique associée. C'est un choix stratégique : Roblox veut que les *créateurs* du métavers — pas seulement ses ingénieurs — produisent des assets.

**Réserve de périmètre** : « open source » pour un modèle de génération 3D ne couvre pas toujours les **données d'entraînement** ni le pipeline complet. Hunyuan3D publie poids et code sous *community license* (restriction commerciale possible) — à distinguer d'une licence OSI.

---

## 3. Le débat « open source AI » : une frontière floue qu'il faut assumer

C'est le point de méthode le plus sensible de ce dossier, et il conditionne l'honnêteté de toutes les affirmations qui suivent.

- **Définition officielle** : l'**Open Source Initiative** a publié la *Open Source AI Definition* (**OSAID 1.0**) le **28/10/2024** — un système open source doit être librement utilisable, étudiable, modifiable et partageable.
- **Contestation** : des spécialistes estiment que *publier les poids seuls ne satisfait pas la définition*, car les données d'entraînement et le processus restent indisponibles (Wolters Kluwer Copyright Blog, 04/03/2025 ; débat OSI lui-même, 03/2025).
- **Cas Llama (Meta)** : distribué sous *Llama Community License*, il est communément qualifié d'« open source » dans la presse **sans satisfaire l'OSAID** — c'est le contre-exemple type à ne pas répéter sans précaution.
- **Adoption réelle** : selon une étude du **MIT Sloan** (20/01/2026), les utilisateurs **optent 80 % du temps pour des modèles fermés** malgré un coût et des performances compétitifs des modèles ouverts ; un marché des modèles open source AI affiche un CAGR de 15,1 % (market.us, 2025 — **Tier 3**, projection de cabinet).

**Décision de rédaction pour ce dossier** (échange n°1, décision 1.1) : distinguer systématiquement
- **open source** (OSAID 1.0 respectée : code + poids + données/processus),
- **open weights** (poids publiés, licence parfois restrictive : **Llama, Hunyuan3D**),
- **source-available** (code consultable, usage restreint).

Et ne jamais écrire « Llama est open source » sans cette précision. **Formulation commune** : « Cube 3D (Roblox) — modèle publié (GitHub + HuggingFace), licence d'usage large, fichier LICENSE à confirmer » / « Hunyuan3D (Tencent) — poids publiés sous licence communautaire (open weights) ».

---

## 4. PNJ et monde génératif : ce que l'apport open source change concrètement

- **PNJ locaux** : des travaux de recherche 2025 montrent qu'un **petit modèle de langage (SLM) quantifié peut tourner sur le GPU du joueur** (llama.cpp, modèle 8B en 4 bits) pour des dialogues de PNJ — schéma décrit dans *Fixed-Persona SLMs with Modular Memory* (arXiv, 11/11/2025) et dans les SDK NVIDIA ACE (blog développeur NVIDIA, 20/02/2025, modèle *Mistral-Nemo-Minitron*).
- **Intérêt pour le métavers** : ça signifie des PNJ persistants **sans appel API payant par requête**, y compris sur plateformes où la latence ou la facture cloud est prohibitive — condition directe d'adoption pour les petits studios et les expériences communautaires.
- **Limite** : aucun déploiement grand public n'est encore documenté à grande échelle dans le dossier (lacune documentaire — voir `05`).

---

## 5. Réserves ouvertes (à vérifier en échange n°1 du `courant.md`)

1. **Cube 3D « 1,8 Md de paramètres »** : chiffre de la note initiale (devforum Roblox, 20/03/2025) et repris par le dossier « Métavers & IA » — confirmer que la v0.5 (juil. 2025) n'a pas modifié ce paramétrage.
2. **« Disponible hors Roblox »** : vérifier que la licence du dépôt `Roblox/cube` autorise bien l'usage commercial hors plateforme (GitHub LICENSE).
3. **Hunyuan3D « community license »** : vérifier les restrictions exactes (usage commercial, licences > X utilisateurs) avant de le classer « open source ».
4. **80 % de choix pour des modèles fermés** : étude MIT Sloan du 20/01/2026 — vérifier le périmètre (quel panel, quelle définition de « modèle fermé »).
5. **PNJ SLM** : aucune mesure d'audience (nombre de joueurs touchés) — ne pas présenter la démonstration technique comme un déploiement.

---

## Sources de la note

1. Roblox Newsroom, *Introducing Roblox Cube*, 17/03/2025 — https://about.roblox.com/newsroom/2025/03/introducing-roblox-cube (T1)
2. Roblox DevForum, *[Beta] Cube 3D Generation Tools and APIs for Creators*, 20/03/2025 — https://devforum.roblox.com/t/beta-cube-3d-generation-tools-and-apis-for-creators/3558947 (T1)
3. arXiv, *Cube: A Roblox View of 3D Intelligence*, 19/03/2025 — https://arxiv.org/abs/2503.15475 (T1)
4. GitHub `Roblox/cube` (v0.5, juil. 2025) ; HuggingFace `Roblox/cube3d-v0.5` (T1)
5. GitHub `Tencent-Hunyuan/Hunyuan3D-2` (21/01/2025) et `Hunyuan3D-2.1` (14/06/2025) ; HuggingFace `tencent/Hunyuan3D-2` (T1)
6. OSI, *Open Source AI Definition 1.0*, 28/10/2024 (T1) ; Wolters Kluwer Copyright Blog, 04/03/2025 (T2) ; OSI Discuss, 03/2025 (T2)
7. MIT Sloan, *AI open models have benefits. So why aren't they more widely used?*, 20/01/2026 — https://mitsloan.mit.edu/ideas-made-to-matter/ai-open-models-have-benefits-so-why-arent-they-more-widely-used (T2)
8. market.us, *Open-Source AI Model Market* (CAGR 15,1 %), 2025 (T3 — projection)
9. arXiv, *Fixed-Persona SLMs with Modular Memory: Scalable NPC Dialogue on Consumer Hardware*, 11/11/2025 — https://arxiv.org/html/2511.10277v1 (T2)
10. NVIDIA Developer Blog, *Bring NVIDIA ACE AI Characters to Games*, 20/02/2025 (T1)
11. Red Hat Developers, *The state of open source AI models in 2025*, 07/01/2026 (T2)
