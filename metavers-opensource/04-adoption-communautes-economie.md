# Axe 4 — Adoption, communautés et modèles économiques : ce que l'open source change

**Dossier « Métavers et projets open source » — note 4/4**
Méthode : chaque affirmation est sourcée (nom, date, URL) et classée **Tier 1-4** (voir `05-verification-des-sources.md`).

---

## 1. Comment l'open source sert l'adoption : les quatre leviers constatés

### Levier 1 — Baisser le coût d'entrée à zéro
Un créateur peut modéliser (Blender), développer (Godot, Three.js), standardiser ses assets (glTF/VRM) et publier (navigateur) **sans dépenser un centime de licence**. Comparaison : Godot = 0 $ sans royalty (MIT) ; **Unreal = gratuit + 5 % de royalty au-delà de 1 M$ de revenus par produit (licence officielle Epic, Tier 1)** ; **Unity = abonnement par siège** (grille officielle ; l'ordre de grandeur ~2 000-2 400 $/siège/an vient de la presse spécialisée 2026, **Tier 3**).

### Levier 2 — Rendre l'interopérabilité possible (et donc l'échelle)
WebXR/OpenXR/glTF/VRM permettent à une expérience d'exister sur PC, mobile et casque sans réécriture. C'est la condition technique du « cross-plateforme par défaut » — or on sait, du dossier cross-plateforme, que **80 % des DAU Roblox sont sur mobile** et que l'audience vient du mobile : l'open source est ce qui permet de *porter* l'expérience sur tous les écrans.

### Levier 3 — Créer un vivier de compétences
- Communauté Godot **doublée en deux ans** (article officiel, 06/05/2026) ;
- croissance **« exponentielle »** des jeux Godot publiés sur Steam (SteamDB) ;
- présence en hausse au **Global Game Jam** et au **GMTK Game Jam**.
→ Les jeunes développeurs apprennent sur des outils ouverts : l'adoption professionnelle de demain se prépare dans les game jams d'aujourd'hui.

### Levier 4 — Réduire le risque perçu (le vrai moteur psychologique)
L'épisode Unity *Runtime Fee* (annonce sept. 2023, révocation 12/09/2024) a montré que la menace n'était pas le prix, mais **la capacité unilatérale à le changer**. La presse spécialisée qualifie cette hausse de « doublement de la base d'utilisateurs dans le mois » (Tier 2, 27/03/2024 ; métrique exacte non communiquée par Godot). Pour le métavers — où l'on investit des années de contenu dans une plateforme — cette réduction de risque est un argument d'adoption majeur.

---

## 2. Les modèles économiques ouverts : ce qui finance réellement l'écosystème

| Mécanisme | Exemple vérifié | Donnée | Tier |
|---|---|---|---|
| **Fonds de développement par donations** | Godot Development Fund (lancé 09/2023) | Revenus **stables sans croissance** malgré la hausse des utilisateurs | T1 |
| **Dons corporatifs + fonds dédié** | Blender Development Fund | Revenus **4,2 → 5,7 M€ (+36 %)** en 2025 ; exercice 2024 déficitaire ; Chaos (07/2025) et **Anthropic (29/04/2026)** rejoignent le fonds | T1/T2 |
| **Mécénat industriel des géants** | NVIDIA, AMD, Apple, Intel, Meta, Google… | Membres et financeurs des fondations (ASWF, Linux Foundation, Khronos) | T1 |
| **Open core / services** | Collabora (Monado), NVIDIA (Omniverse sur OpenUSD) | Le logiciel est ouvert, le service/cloud est monétisé | T2 |
| **Open source comme vitrine d'écosystème** | Roblox (Cube 3D), Meta (Llama) | Modèle ouvert pour attirer créateurs/chercheurs, monétisation en aval sur la plateforme | T1 |
| **Gouvernance DAO (Web3)** | Decentraland | 526 dépôts publics sur GitHub ; proposition DAO (30/01/2024) : *tout code financé par la DAO doit être publié en public* | T2 |

**Leçon** : **l'adoption n'a jamais financé l'open source automatiquement.** Godot le dit lui-même dans son article officiel : les utilisateurs ne donnent pas parce qu'ils considèrent le projet comme déjà installé. Le financement repose sur une poignée de mécènes industriels — ce qui concentre un risque stratégique (si un ménage se retire, le projet ralentit).

---

## 3. Le contre-modèle : quand l'open source *sauve* un projet abandonné

**Mozilla Hubs** est le cas d'école : Mozilla a arrêté le support de Hubs le **31/05/2024** (support.mozilla.org) et décommissionné Hubs Cloud au 01/01/2024 — mais **le code étant open source, la communauté a constitué la « Hubs Community Edition » qui continue** (ryanschultz.com, 26/02/2024 ; UploadVR, 16/02/2024).

**Précision de pérennité** (échange n°1, décision 1.5) : distinguer **« le code survit »** (garanti : dépôt public forkable, toujours disponible en octobre 2026) de **« le service survit »** (conditionné aux contributeurs : serveurs, maintenance, communauté). L'argument solide est la *possibilité de reprise*, pas une promesse de continuité automatique.

C'est exactement l'inverse de ce qui arrive aux services propriétaires équivalents : Rec Room fermé le 01/06/2026, Spatial créateur arrêté le 27/07/2026, Mesh retiré (12/2025), Workrooms fermé (02/2026) — **les utilisateurs n'ont rien pu récupérer** (dossier cross-plateforme).

> **Résultat pour le métavers** : dans le modèle propriétaire, la fermeture d'un service efface des mondes et des communautés. Dans le modèle ouvert, elle transfère la responsabilité aux utilisateurs. **L'open source est la seule garantie d'existence continue d'un monde virtuel au-delà de son éditeur.**

---

## 4. Ce que l'open source ne résout pas (limites et risques)

1. **L'adoption finale reste captive des plateformes fermées.** Roblox (123 M DAU T2 2026), Fortnite et Horizon Worlds mobile sont propriétaires : leurs mondes, comptes et économies ne sont pas ouverts. Les standards ouverts équipent les *alternatives*, pas les géants du trafic.
2. **Interopérabilité sociale jamais atteinte** : aucun avatar, aucun compte, aucun objet Roblox/Fortnite n'est portable — voir réserve n°4 de la note 1.
3. **Financement fragile** : Godot stagnant, Blender dépendant de sa croissance des revenus, projets de niche (Monado, runtimes) maintenus par peu de personnes.
4. **Qualité et sécurité** : absence de SLA, dépendance à la contribution bénévole ; la chaîne d'outils ouverte n'a pas de support entreprise systématique.
5. **Licences « open » trompeuses** : Llama (Meta) et Hunyuan3D (Tencent) sont publiés sous licences communautaires, pas sous une définition OSI — classer en **open weights**, pas en open source.

---

## 5. Réponse opérationnelle à la problématique du jour

**« Comment exploiter les projets open source au service du développement et de l'adoption du métavers ? »** — en les affectant à quatre fonctions distinctes :

| Fonction | Ce qu'on utilise | Effet attendu sur l'adoption |
|---|---|---|
| **Socle technique** | WebGPU/WebXR, OpenXR, glTF, VRM, OpenUSD | Portabilité multi-écrans → audience mobile |
| **Chaîne de création** | Blender, Godot, Three.js, Monado | Coût d'entrée 0 → explosion du nombre de créateurs |
| **Génération de contenus** | Cube 3D (Roblox), Hunyuan3D, SLM pour PNJ | Passage de l'heure-modélisation à la minute-génération |
| **Garantie de pérennité** | Open Metaverse Foundation, code source récupérable | Confiance → l'investissement de temps n'est pas perdu |

**Et ce qu'il ne faut pas promettre** : l'open source ne crée pas, à lui seul, l'adoption grand public — il en est la **condition nécessaire** (interopérabilité, coût, pérennité) sans en être la **condition suffisante** (l'interface, la communauté et la distribution restent déterminantes).

---

## Sources de la note

1. Godot Engine, *Godot usage and engine growth*, 06/05/2026 (T1)
2. Unity, *Unity is Canceling the Runtime Fee*, 12/09/2024 (T1) ; Game World Observer, 27/03/2024 (T2)
3. Blender Foundation, *Annual Report 2025*, 23/09/2026 (T1) ; 80.lv, 16/09/2025 (T2) ; CG Channel, 11/07/2025 (Chaos) ; Blendernation, 29/04/2026 (Anthropic) (T2)
4. Mozilla, *End of support for Mozilla Hubs*, 31/05/2024 — https://support.mozilla.org/en-US/kb/end-support-mozilla-hubs (T1) ; UploadVR, 16/02/2024 ; ryanschultz.com, 26/02/2024 (T2)
5. Decentraland, dépôts GitHub (526) ; proposition DAO *Open Source all code generated using DAO funds*, 30/01/2024 (T2)
6. Roblox, *Q2 2026 Earnings Shareholder Letter*, 30/07/2026 (123 M DAU) — cf. dossier cross-plateforme (T1)
7. Dossier « Métavers cross-plateforme » : fermetures Rec Room (01/06/2026), Spatial (27/07/2026), Mesh (12/2025), Workrooms (02/2026) (T1/T2)
8. Epic Games, licence Unreal Engine (5 % > 1 M$) — licence officielle (T1) ; presse spécialisée 2026 pour le niveau de prix Unity (tech-insider, blog.promise.legal) — **Tier 3**
