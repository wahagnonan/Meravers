# Métavers et projets open source : comment les exploiter au service du développement et de l'adoption du métavers

**Dossier de recherche — 4 notes thématiques + synthèse + note de vérification**
Sources primaires et études à jour 2024-2026.

**Problématique du jour :**
> « Comment exploiter les projets open source au service du développement et de l'adoption du métavers ? »

## Structure du dossier

| Fichier | Contenu |
|---|---|
| `01-standards-interopabilite.md` | Axe 1 — Standards ouverts (WebXR, OpenXR, glTF, VRM, OpenUSD) et gouvernances |
| `02-moteurs-outils-ouverts.md` | Axe 2 — Chaîne de production ouverte : Godot, Blender, Three.js, O3DE, Monado |
| `03-ia-generative-ouverte.md` | Axe 3 — Modèles ouverts de génération 3D (Cube, Hunyuan3D), PNJ, débat OSAID |
| `04-adoption-communautes-economie.md` | Axe 4 — Leviers d'adoption, modèles économiques, pérennité, limites |
| `05-verification-des-sources.md` | Note de vérification : hiérarchie Tier 1-4, contrôles, lacunes reconnues |
| `courant.md` | Dialogue inter-agents : questions, réponses, accords et décisions |

---

## Synthèse

### Réponse directe à la problématique

**L'open source n'est pas une option philosophique du métavers : c'est son infrastructure déjà construite.** Toute la chaîne — standards (WebGPU/WebXR, OpenXR 1.1, glTF, VRM, OpenUSD), moteurs (Godot, O3DE), outils de création (Blender, Three.js ≈ 12,2 M téléchargements npm/semaine), runtimes (Monado), IA générative 3D (Roblox Cube, Tencent Hunyuan3D) — est couverte par des projets ouverts, gouvernés par le W3C, Khronos et le Linux Foundation.

**Mais l'open source est une condition nécessaire, non suffisante, de l'adoption.** Il abaisse le coût d'entrée à zéro, rend possible le cross-plateforme (donc l'audience mobile : 80 % des DAU Roblox), et garantit la pérennité des mondes au-delà de leur éditeur. Il ne crée ni la distribution, ni la communauté, ni l'interface : les plateformes qui captent réellement l'audience (Roblox, Fortnite, Horizon Worlds mobile) restent propriétaires.

### 1. Standards ouverts : le socle existe déjà

- **WebGPU** est *Baseline* natif sur iOS/macOS/visionOS 26 (statut confirmé au 02/06/2026, MDN/gpuweb) → le rendu 3D performant sans installation est garanti par défaut.
- **WebXR** reste une *Candidate Recommendation* (01/10/2025), **absente de Safari/iOS** : standard ouvert ≠ service ouvert.
- **OpenXR 1.1** (15/04/2024) : Meta, Microsoft, Sony, HTC, PICO, Valve, Google, Collabora (Monado) sont conformes — les silos matériels ont disparu au niveau de l'API, même si les SDK Meta verrouillent encore les casques concurrents sur PC.
- **VRM × Khronos** (24/10/2024) : première candidature sérieuse d'un standard d'avatar portable.
- **Gouvernance** : Open Metaverse Foundation (18/01/2023) et Open 3D Foundation (06/07/2021) sous l'égide du **Linux Foundation** ; Metaverse Standards Forum (2022, 35 membres fondateurs) reste un forum de discussion **sans mesure d'adoption publiée sur son site au 07/10/2026** (lacune documentaire).

### 2. Chaîne de production : couverture complète, financement asymétrique

- **Godot** : ~**2 M de téléchargements par version stable** ; jeux sur Steam en croissance « exponentielle » ; communauté **doublée en deux ans** — mais le Development Fund **ne croît pas** avec les utilisateurs.
- **Blender** : revenus **4,2 → 5,7 M€ (+36 %)** en 2025, après un **exercice 2024 déficitaire** ; soutenu par NVIDIA, AMD, Apple, Intel, et depuis 04/2026 par Anthropic.
- **Bascule possible** : l'annonce du *Runtime Fee* Unity (2023), révoqué le 12/09/2024, est suivie d'une hausse très forte des téléchargements Godot, qualifiée de « doublement de la base » par la presse spécialisée (Tier 2, 27/03/2024 ; métrique exacte non communiquée par Godot) → l'adoption open source est d'abord une réaction au risque perçu.

### 3. IA générative ouverte : le levier de coût le plus puissant

- **Roblox Cube 3D** : modèle **open source** (GitHub + HuggingFace, 17/03/2025), **1,8 Md de paramètres** entraîné sur **1,5 M d'assets** — publié « pour quiconque, sur ou hors Roblox ».
- **Hunyuan3D 2.0/2.1** (Tencent) : poids et code publiés (21/01/2025, 14/06/2025) sous *community license* → classé **open weights**, pas open source (non conforme OSI).
- **Frontière à assumer** : la *Open Source AI Definition* 1.0 de l'OSI (28/10/2024) n'est pas satisfaite par la simple publication de poids (Llama en est l'exemple) ; et selon le **MIT Sloan (20/01/2026)**, les utilisateurs choisissent **80 % du temps des modèles fermés**.
- **PNJ** : un petit modèle quantifié peut tourner **sur le GPU du joueur** (arXiv 11/2025 ; NVIDIA ACE 02/2025) → PNJ persistants sans coût d'appel — encore au stade technique.

### 4. Adoption : quatre leviers, trois limites

**Leviers** : coût d'entrée nul · interopérabilité multi-écrans · vivier de compétences (game jams, communautés doublées) · réduction du risque perçu.

**Le fait le plus fort du dossier** : quand Mozilla a arrêté Hubs le **31/05/2024**, la communauté a **repris le code** (Hubs Community Edition, toujours disponible en oct. 2026) — alors que Rec Room (01/06/2026), Spatial (27/07/2026), Mesh et Workrooms ont simplement disparu avec leurs mondes. **L'open source garantit que le code survive à son éditeur** ; la continuité de service, elle, dépend de la communauté (distinction posée par l'échange n°1 du `courant.md`).

**Limites** : plateformes d'audience toujours propriétaires · aucun standard de compte/progression · financement concentré sur quelques mécènes industriels · licences « open » trompeuses (Llama, Hunyuan3D).

### Réserves ouvertes

1. Les prix Unity (≈ 2 000-2 400 $/siège/an) viennent de blogs spécialisés — **Tier 3**, à confirmer sur unity.com ; Unreal (**5 % > 1 M$**) est confirmé par la licence officielle (Tier 1).
2. « 2 M de téléchargements » Godot = par version, **pas** des utilisateurs ; chiffre fourni par Godot lui-même avec réserves méthodologiques (févr. 2026).
3. Metaverse Standards Forum : **aucune mesure d'adoption publiée** sur son site au 07/10/2026 (lacune, négative datée).
4. Inconnues : part des expériences créées avec des outils ouverts ; périmètre exact des licences Cube 3D et Hunyuan3D ; audience réelle des PNJ à modèle local.

---

## Sources principales du dossier

- W3C (WebXR CRD 01/10/2025 ; WebGPU), Khronos (OpenXR 1.1, glTF, VRM Consortium 24/10/2024), gpuweb
- Linux Foundation : Open Metaverse Foundation (18/01/2023), Open 3D Foundation (06/07/2021), Alliance for OpenUSD
- Metaverse Standards Forum (2022 →)
- Godot Engine, *Godot usage and engine growth* (06/05/2026) ; Unity, *Canceling the Runtime Fee* (12/09/2024)
- Blender Foundation, *Annual Report 2025* (23/09/2026)
- Roblox, *Introducing Roblox Cube* (17/03/2025), arXiv 2503.15475, GitHub/HuggingFace ; licence d'usage large, fichier LICENSE à confirmer
- Tencent, GitHub `Hunyuan3D-2` / `Hunyuan3D-2.1`
- OSI, *Open Source AI Definition 1.0* (28/10/2024) ; MIT Sloan (20/01/2026)
- Mozilla, *End of support for Mozilla Hubs* (31/05/2024)
- Collabora / Monado ; NVIDIA Omniverse ; NVIDIA ACE (20/02/2025)
- Registre npm (24/09/2026) ; SteamDB ; itch.io

> **Réserve méthodologique** : les valeurs de « marché » de l'open source AI (CAGR 15,1 %, market.us) sont des **projections de cabinet (Tier 3)**, pas des données constatées. Les faits vérifiables de ce dossier — téléchargements, publications, financements, arrêts de service — sont systématiquement distingués des projections. Voir `05-verification-des-sources.md`.
