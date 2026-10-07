# Axe 1 — Standards ouverts et interopérabilité : le socle sans lequel pas de métavers

**Dossier « Métavers et projets open source » — note 1/4**
Méthode : chaque affirmation est sourcée (nom, date, URL) et classée **Tier 1-4** (voir `05-verification-des-sources.md`). Données constatées et projections sont distinguées.

---

## 1. Le constat de départ : le métavers ne peut pas être propriétaire

Un « métavers » au sens interopérable — un compte, un avatar, une expérience qui traversent les plateformes — exige des **formats et des protocoles communs**. Or un standard propriétaire est, par définition, une dépendance : c'est la leçon qu'a formalisée l'industrie après l'époque des silos ( chaque casque avec son SDK, chaque moteur avec son format d'export).

Toutes les couches critiques du métavers sont aujourd'hui portées par des projets **ouverts, gouvernés collectivement** :

| Couche | Standard / projet | Gouvernance | Statut vérifié | Tier |
|---|---|---|---|---|
| Rendu 3D temps réel sur le Web | **WebGPU**, **WebGL** | W3C / gpuweb | WebGPU **activé par défaut** sur macOS 26, iOS 26, iPadOS 26, visionOS 26 — statut *Baseline* confirmé au 02/06/2026 | T1 |
| Immersion dans le navigateur | **WebXR Device API** | W3C, Immersive Web WG | *Candidate Recommendation Draft* du **01/10/2025** — **pas** une fonctionnalité *Baseline* ; absent de Safari/iOS (bug WebKit ouvert) | T1 |
| Accès matériel VR/AR | **OpenXR 1.1** | Khronos Group | Publié le **15/04/2024** ; runtimes conformes : Meta, Microsoft, Sony, HTC, PICO, Valve, Google (Android XR), Collabora (Monado) | T1 |
| Échange de contenus 3D | **glTF 2.0** | Khronos Group | Standard de fait du Web 3D et des temps réel | T2 |
| Avatars portables | **VRM** (extension glTF) | VRM Consortium | Collaboration **Khronos × VRM Consortium** annoncée le **24/10/2024** pour standardisation internationale | T1 |
| Scènes industrielles / jumeaux numériques | **OpenUSD** | Alliance for OpenUSD (Linux Foundation, depuis 2023) | Adopté nativement par NVIDIA Omniverse | T1 |
| Runtime XR open source | **Monado** | Collabora / freedesktop.org | Runtime OpenXR complet ; utilisé sous Android XR, NVIDIA CloudXR, PICO, Snapdragon Spaces (24/06/2026) | T2 |

**Lecture** : il n'y a pas de « couche propriétaire manquante ». Le socle technique du métavers existe, il est ouvert, et il est déjà implémenté — y compris par les géants propriétaires (Meta, Google, Microsoft, Sony sont tous conformes OpenXR).

---

## 2. Ce que les standards ouverts ont déjà permis concrètement

### 2.1 L'accès « sans casque » : victoire nette de l'open source Web

- **WebGPU** est devenu une fonctionnalité *Baseline* sur iOS/macOS 26 (statut confirmé au 02/06/2026, MDN/gpuweb) : le rendu 3D performant dans le navigateur est désormais **garanti par défaut**, sans installation. C'est la condition technique de la thèse « le métavers accessible, c'est le téléphone déjà possédé » du dossier cross-plateforme.
- **Three.js** (licence MIT) est téléchargé ≈ **12,2 millions de fois par semaine** sur npm contre ≈ **304 k/semaine** pour @babylonjs/core — soit un ratio d'environ **40×** en faveur du moteur 100 % communautaire (registre npm, relevé du **24/09/2026**, T1).
- **Roblox « dans Chrome, sans installation, via un lien »** (annonce RDC, septembre 2026) repose intégralement sur cette pile Web ouverte.

### 2.2 L'interopérabilité matérielle : OpenXR a cassé les silos

Avant OpenXR (1.0 en 2019, 1.1 en 2024), un développeur XR devait écrire un intégration par casque. Aujourd'hui, **un même code cible Meta, Microsoft, Sony, HTC, PICO, Valve et Google**. Le contre-exemple documenté : les intégrations « OpenXR » Unity/Unreal de Meta bloquent sur PC les casques non-Quest (UploadVR, 05/2025, **Tier 4**) — c'est la preuve que *le standard ouvert ne suffit pas si un acteur verrouille son implémentation*.

### 2.3 Les avatars : le premier vrai chantier d'interopérabilité transverse

Le format **VRM** (basé sur glTF 2.0) porte l'avatar humain d'une plateforme à l'autre : expressions faciales standardisées (joie, colère, tristesse…), portabilité du modèle. La collaboration **Khronos × VRM Consortium** (24/10/2024) signe le passage d'un format de communauté (pixiv/VRoid, forte dans l'ouest asiatique) à une candidature de standard international. C'est le maillon exact que réclamait la recommandation du dossier « Métavers & IA » : *« exiger l'interopérabilité des comptes et des standards »*.

---

## 3. Les gouvernances collectives : qui écrit les règles du métavers ?

| Organisme | Création | Rôle | Vérifié | Tier |
|---|---|---|---|---|
| **Khronos Group** | — | OpenXR 1.1, glTF, Vulkan ; collaboration VRM | 15/04/2024 ; 24/10/2024 | T1 |
| **W3C / Immersive Web WG** | — | WebXR, WebGPU | CRD 01/10/2025 | T1 |
| **Metaverse Standards Forum** | juin 2022 (35 membres fondateurs : Meta, Microsoft, NVIDIA, Sony…) | Groupes de travail, prototypages, *plugfests*, outillage open source ; initiative « Forum Labs » ; initiative « Open Metaverse Browser » présentée à SIGGRAPH 2026 | metaverse-standards.org | T2 |
| **Open Metaverse Foundation** (Linux Foundation) | **18/01/2023** | Fondation dédiée aux logiciels et standards ouverts du métavers, neutre vis-à-vis des fournisseurs | linuxfoundation.org ; openmv.org | T1 |
| **Open 3D Foundation** (Linux Foundation) | **06/07/2021** | Abrite **O3DE** (Apache 2.0), moteur 3D ouvert issu d'Amazon Lumberyard | linuxfoundation.org ; o3de.org | T1 |
| **Alliance for OpenUSD** | 2023 (Linux Foundation) | Standardisation d'USD pour les scènes 3D | docs NVIDIA | T1 |
| **VRM Consortium** | — | Format d'avatar VRM | vrm-consortium.org | T1 |

**Point saillant** : les deux fondations « métavers » sont hébergées par le **Linux Foundation** — c'est-à-dire que la gouvernance du socle du métavers a été confiée au même modèle qui a réussi pour le cloud, les conteneurs et l'IA embarquée. C'est l'organisation, pas l'enthousiasme médiatique, qui fait durer un standard.

---

## 4. Limites et réserves — ce que les standards ouverts ne résolvent pas

1. **Standard ouvert ≠ service ouvert.** WebXR est un standard du W3C depuis 2019, mais il **n'est pas disponible sur Safari/iOS** (bug WebKit ouvert, relevé 02/06/2026) : un standard sans implémentation ne démocratise rien. L'accès « sans casque » repose donc sur WebGPU et le streaming, **pas** sur WebXR immersif.
2. **Le verrou reste dans la couche applicative.** Les SDK Meta verrouillent les casques concurrents sur PC (UploadVR, 05/2025) : le standard est ouvert, l'écosystème ne l'est pas entièrement.
3. **Les forums de standardisation ne produisent pas d'adoption.** Le Metaverse Standards Forum publie des *présentations* et des *initiatives* ; **aucune mesure d'adoption n'y figure sur son site au 07/10/2026** (absence constatée, classée lacune documentaire dans `05`).
4. **L'absence de standard d'identité/compte.** Personne n'a standardisé le compte utilisateur, la progression ou la propriété des objets : c'est précisément là que se joue le lock-in, et aucun standard ouvert ne le couvre encore.

---

## Sources de la note

1. W3C, *WebXR Device API* (Candidate Recommendation Draft), 01/10/2025 — https://www.w3.org/TR/2025/CRD-webxr-20251001/ (T1)
2. MDN Web Docs / WebKit Bugzilla, statut *Baseline* de WebXR, 02/06/2026 (T1)
3. gpuweb, *Implementation Status* (WebGPU iOS/macOS 26) — https://github.com/gpuweb/gpuweb/wiki/Implementation-Status (T1)
4. Khronos Group, *Khronos releases OpenXR 1.1*, 15/04/2024 — https://www.khronos.org/news/press/khronos-releases-openxr-1.1-to-further-streamline-cross-platform-xr-development (T1)
5. Khronos Group & VRM Consortium, communiqué de collaboration, 24/10/2024 — https://www.khronos.org/news/press/the-khronos-group-and-vrm-consortium-collaborate-to-advance-international-standardization-of-the-vrm-3d-avatar-file-format (T1)
6. Registre npm : trois.js (~12,2 M/tel. sem.) et @babylonjs/core (~304 k/sem.), relevé 24/09/2026 (T1)
7. Linux Foundation, *Linux Foundation Announces Launch of the Open Metaverse Foundation*, 18/01/2023 — https://www.linuxfoundation.org/press/open-metaverse-foundation ; Open Metaverse Foundation — https://www.openmv.org/ (T1)
8. Linux Foundation, *Linux Foundation to Form New Open 3D Foundation*, 06/07/2021 ; O3DE (Apache 2.0) — https://o3de.org/ (T1)
9. Metaverse Standards Forum — https://metaverse-standards.org/ ; initiative « Open Metaverse Browser », SIGGRAPH 2026 (T2)
10. Collabora / vr.org, *Monado open source OpenXR runtime*, 24/06/2026 ; Collabora, *Google Cardboard comes to Monado*, 31/10/2025 — https://www.collabora.com/news-and-blog/blog/2025/10/31/expanding-access-to-xr-bringing-google-cardboard-support-to-monado/ (T2)
11. UploadVR, intégrations OpenXR Meta bloquant les casques non-Quest, 05/2025 (T4)
12. NVIDIA, *OpenUSD FAQ / Omniverse*, consulté 2026 (T1)
