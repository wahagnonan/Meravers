# Axe 2 — Moteurs, outils et briques logicielles ouverts : la chaîne de production du métavers

**Dossier « Métavers et projets open source » — note 2/4**
Méthode : chaque affirmation est sourcée (nom, date, URL) et classée **Tier 1-4** (voir `05-verification-des-sources.md`).

---

## 1. Cartographie de la chaîne de production

| Étage | Projet ouvert | Licence / statut | Donnée vérifiée | Tier |
|---|---|---|---|---|
| **Moteur de jeu / univers** | **Godot Engine** | MIT, sans royalties ni quota d'installation | ~**2 M de téléchargements par version stable** (site/GitHub) ; **jeux Godot sur Steam en croissance « exponentielle »** (SteamDB) — relevé février 2026 | T1 |
| **Moteur industriel / simulation** | **O3DE** (Open 3D Engine) | Apache 2.0, Open 3D Foundation (Linux Foundation) | Projet créé le 06/07/2021 à partir de Lumberyard (AWS) | T1 |
| **Modélisation 3D / assets** | **Blender** | GPL | Revenus Blender Foundation **+36 % : 4,2 → 5,7 M€** (rapport annuel 2025, publié 23/09/2026) ; exercice 2024 déficitaire | T1 |
| **Web 3D** | **Three.js** | MIT | ≈ **12,2 M téléchargements npm/semaine** (24/09/2026), ≈ 40× Babylon.js | T1 |
| **Web 3D (alternatif)** | **Babylon.js** | Apache 2.0 | ≈ 304 k téléchargements npm/semaine (24/09/2026) | T1 |
| **Runtime XR** | **Monado** | MIT, Collabora/freedesktop.org | Runtime OpenXR complet, sous Android XR / NVIDIA CloudXR / PICO / Snapdragon Spaces (24/06/2026) ; Google Cardboard supporté depuis 31/10/2025 | T2 |
| **Streaming de scènes** | **NVIDIA Omniverse Kit App Streaming** | Outil NVIDIA sur socle OpenUSD ouvert | Scènes streamées dans Chromium, serveurs RTX (20/08/2025) | T1 |
| **Format d'assets** | **glTF 2.0 / VRM** | Khronos / VRM Consortium | Standard de fait du Web 3D ; standardisation VRM engagée depuis 24/10/2024 | T1 |

**Lecture** : la chaîne complète — de la création d'assets jusqu'au rendu dans un navigateur — est couverte par des projets ouverts. Il n'y a aucun « maillon manquant » qui forcerait à passer par un outil propriétaire.

---

## 2. Le cas Godot : la preuve que l'open source capte l'adoption

L'article officiel *« Godot usage and engine growth »* (Clay John, **06/05/2026**, godotengine.org) donne les repères les plus fiables du dossier :

- **Téléchargements** : « à peu près **2 millions** par version stable » (site + GitHub). Réserve explicite de l'auteur : données hétérogènes (site/GitHub/Steam/Google Play comptent différemment), données au **février 2026**, et *« ce n'est pas un tableau exact »*.
- **Jeux publiés** : le nombre de jeux Godot sur **Steam** présente des *« signes forts de croissance exponentielle »* (source : SteamDB) ; volume bien plus élevé sur **itch.io** (barrière d'entrée plus faible).
- **Communauté** : *« notre communauté a **doublé** en taille au cours des deux dernières années »* — avec le biais reconnu de la mesure (réseaux occidentaux/anglais, Discord non compté, croissance Chine non mesurée).
- **Game jams** : croissance nette au **Global Game Jam** et au **GMTK Game Jam** (saut 2023 → 2024), donc présence dans la *génération montante* des développeurs et dans l'enseignement.
- **Financement** : le *Development Fund* (lancé sept. 2023) est **stable sans croître** malgré la hausse des utilisateurs — l'auteur liste lui-même trois hypothèses (perception « projet déjà installé », message de valeur mal communiqué, perception « simple alternative gratuite »). Les sponsors corporatifs (donations ponctuelles) ne sont pas tracés.

**Événement déclencheur historique** : l'annonce du *Runtime Fee* par Unity (sept. 2023), son backlash, puis sa **révocation le 12/09/2024** (unity.com) — la presse spécialisée qualifie cette hausse de *« doublement de la base d'utilisateurs dans le mois »* après l'annonce Unity (Game World Observer, 27/03/2024, **Tier 2** — métrique exacte : téléchargements/inscriptions, **non communiquée comme telle par Godot**, et non reprise par l'article officiel du 06/05/2026). Les fondateurs de Godot redoutaient d'ailleurs cet afflux (*Game Developer*, 05/09/2024).

> **Enseignement pour le métavers** : la porte d'entrée de l'adoption open source n'est pas la philosophie, c'est **la suppression d'un risque perçu** (coût, dépendance, changement de conditions unilatéral). Un studio choisi Godot le jour où Unity a menacé sa rémunération.

---

## 3. Le cas Blender : la norme 3D ouverte devenue incontournable

- **Finances** : rapport annuel Blender Foundation **2025** publié le **23/09/2026** : revenus **+36 %, de 4,2 à 5,7 M€** ; part des donateurs corporatifs stable ; croissance des membres individuels du Development Fund. En sens inverse, **l'exercice 2024 s'est soldé par un déficit** (80.lv, 16/09/2025, Tier 2) — la croissance des revenus ne garantit pas l'équilibre.
- **Gouvernance** : Blender est membre de l'**ASWF** (Academy Software Foundation), de **Khronos**, de la **Linux Foundation** et de l'**OIN**, et soutenu par AMD, Apple, Intel et NVIDIA (blender.org) — c'est-à-dire que l'outil de création 3D du métavers est financé par l'industrie qu'il sert, sans en être contrôlé.
- **Signal récent** : **Anthropic** a rejoint le Development Fund comme donateur corporatif (blendernation, 29/04/2026, Tier 2) — les acteurs de l'IA générative financent désormais l'outil de création 3D open source dont ils ont besoin pour entraîner/valider leurs pipelines.

---

## 4. La rupture de confiance comme moteur d'adoption — et ses limites

**Ce qui accélère l'open source :**
1. **Unilatéralisme tarifaire** : Unity Runtime Fee (2023) → exode vers Godot.
2. **Coût d'entrée nul** : pas de licence par siège, pas de royalty (Godot MIT). **Unreal = gratuit + 5 % de royalty au-delà de 1 M$ de revenus par produit (licence officielle Epic, Tier 1)** ; **Unity = abonnement par siège** (grille officielle ; l'ordre de grandeur ~2 000-2 400 $/siège/an vient de la presse spécialisée 2026, **Tier 3**).
3. **Portabilité des compétences** : un asset glTF/USD, un avatar VRM et un code OpenXR se déplacent d'un outil à l'autre — l'open source rend le *changement d'outil possible*, donc le lock-in n'est plus une fatalité.

**Ce qui freine :**
1. **Financement asymétrique** : Godot ~2 M de téléchargements/stable mais Development Fund stable ; Blender rentable seulement par croissance des revenus. *Adoption ≠ rémunération des mainteneurs* — c'est la faille structurelle de l'open source dans le métavers, qui demande des investissements lourds (rendu temps réel, moteurs physiques).
2. **Écarts fonctionnels réels** : O3DE (Apache 2.0) n'a pas atteint l'audience de Unity/Unreal ; être « ouvert » ne suffit pas à convaincre les studios AAA.
3. **Dette de maintenance** : projets maintenus par peu de contributeurs (Monado, runtimes) — un standard ouvert sans mainteneur est un risque, pas une garantie.

---

## 5. Réserves ouvertes (à vérifier en échange n°1 du `courant.md`)

- **Godot : « ~2 M par version »** est un chiffre de téléchargements *cumulés par version*, pas une base d'utilisateurs — ne pas le présenter comme des « 2 M d'utilisateurs ».
- **« Croissance exponentielle »** : formule de l'article officiel Godot, fondée sur SteamDB (Tier 2 pour l'interprétation, Tier 1 pour le fait que Godot le publie).
- **Unity/Unreal : prix** — voir décision 1.3 du `courant.md` : Unreal confirmé en licence officielle (Tier 1), Unity en ordre de grandeur Tier 3.
- **Aucune donnée** sur la part des expériences Roblox/Fortnite *créées* avec des outils open source (lacune documentaire).

---

## Sources de la note

1. Godot Engine, *Godot usage and engine growth*, Clay John, 06/05/2026 — https://godotengine.org/article/godot-growth-stats-2026/ (T1)
2. Unity, *Unity is Canceling the Runtime Fee*, 12/09/2024 — https://unity.com/blog/unity-is-canceling-the-runtime-fee (T1)
3. Game World Observer, *Godot doubled user base after Unity controversy*, 27/03/2024 — https://gameworldobserver.com/2024/03/27/godot-doubled-user-base-after-unity-controversy (T2)
4. Game Developer, *Godot founders had desperately hoped Unity wouldn't 'blow up'*, 05/09/2024 (T2)
5. Blender Foundation, *Annual Report 2025*, 23/09/2026 — https://www.blender.org/news/blender-foundation-annual-report-2025/ (T1) ; relayé : blendernation / gamedev.net (T2)
6. 80.lv, *Blender Reports Operating at a Loss in 2024*, 16/09/2025 (T2)
7. Blendernation, *Anthropic joins the Blender Development Fund*, 29/04/2026 (T2)
8. blender.org, page *Foundation* (membres ASWF/Khronos/Linux Foundation/OIN) (T1)
9. Registre npm, relevé 24/09/2026 : three.js, @babylonjs/core (T1)
10. Open 3D Foundation / O3DE, *Announcing Open 3D Engine*, 06/07/2021 — https://o3de.org/ (T1)
11. Collabora, *Google Cardboard comes to Monado*, 31/10/2025 ; vr.org, *Monado Is the Open Source Runtime…*, 24/06/2026 (T2)
12. NVIDIA Technical Blog, *Omniverse Kit App Streaming*, 20/08/2025 (T1)
13. Epic Games, licence Unreal Engine (royalty 5 % au-delà de 1 M$) — licence officielle (T1) ; presse spécialisée 2026 (tech-insider, blog.promise.legal) pour le niveau de prix Unity — **Tier 3**
