# Axe 2 — Enjeux et innovations technologiques de l'accès sans casque

**Dossier « Métavers cross-plateforme et sobriété matérielle » — recherche documentaire, octobre 2026.**

**Légende :** ✅ = donnée constatée/divulguée ; 🔮 = projection/estimation de cabinet. T1 = source officielle/standard ; T2 = étude ; T3 = projection de cabinet ; T4 = presse secondaire.

---

## 1. Web3D et WebXR : l'univers 3D dans le navigateur

| Affirmation / chiffre | Source | Date | Confiance |
|---|---|---|---|
| ✅ WebXR Device API = W3C *Candidate Recommendation Draft* (statut « work in progress », pas encore Recommandation) | W3C / Immersive Web WG | 01/10/2025 | T1 |
| ✅ WebXR = « Limited availability », **pas *Baseline*** : non disponible dans plusieurs navigateurs majeurs ; Safari/iOS toujours en bug ouvert | MDN Web Docs / WebKit Bugzilla | 02/06/2026 | T1 |
| ✅ WebGPU activé **par défaut** sur macOS 26, iOS 26, iPadOS 26, visionOS 26 | gpuweb, *Implementation Status* | 2025-2026 | T1 |
| ✅ Three.js ≈ **12,2 M téléchargements npm/semaine** ; @babylonjs/core ≈ 304 k/semaine (ratio ≈ 40×) | registre npm | 24/09/2026 | T1 |
| ✅ Roblox : **123 M de joueurs quotidiens** au T2 2026 (+10 %/an), pic de 151 M à l'été 2025 ; 29 Md d'heures sur le trimestre | Roblox, lettre aux actionnaires (SEC), relayé AFP | 11-12/09/2026 | T1 |
| ✅ « Roblox Everywhere » : lancement **dans Chrome, sans installation, via un lien**, d'ici fin 2026 ; mode hors ligne mi-2027 | Roblox Developers Conference | 11/09/2026 | T1 |
| ✅ Fortnite jouable dans le navigateur via Xbox Cloud Gaming **sans abonnement ni installation** (depuis 05/2022) ; min. 10 Mbps (20 Mbps recommandés) | Xbox / Epic | 2022-2026 | T1 |
| ✅ Sessions gratuites Fortnite cloud limitées à **60 min** | Xbox (via Pure Xbox) | 05/2025 | T4 |
| ✅ Mozilla Hubs **arrêté** (serveur demo et abonnements) le 31/05/2024, code transféré à la communauté | Mozilla | 02-05/2024 | T1 |
| ✅ Spatial : **coucher des paliers Free/Pro et de l'hébergement 3D au 27/07/2026** | Spatial, *A Note to Our Creator Community* | 28/05/2026 | T1 |
| 🔮 Chiffre d'affaires mondial du cloud gaming 2026 : **entre 4,81 et 28,29 Md$** selon les cabinets (écart ×6 lié aux définitions) | Precedence / The Business Research Company (compilation) | 2026 | T3 |
| 🔮 Utilisateurs cloud gaming mondiaux : 395,9 M (2024) → **~482 M en 2026** | Statista Market Insights | 2024-2026 | T3 |
| ✅ Xbox Cloud Gaming : **> 500 millions d'heures streamées** sur l'exercice clos le 30/06/2025 | Microsoft (earnings call, Satya Nadella) | juillet 2025 | T1 |
| ✅ Derniers compteurs officiels publiés : Game Pass **34 M abonnés** (02/2024) ; GeForce NOW **25 M inscrits** (02/2023) — plus de mise à jour depuis | Microsoft / NVIDIA | 2023-2024 | T1 (daté) |
| 🔮 « 45 M GeForce NOW / 38 M xCloud / 22 M Luna » | GlanceDigest | 07/2026 | **T4 — à ne pas citer comme établi** |
| ✅ Latence interactive mesurée sur plateformes de cloud gaming mobile : **112 à 403 ms** (moyenne 163 ms) ; seuil de jouabilité < 100 ms | Étude NSDI'25 (USENIX), 100 appareils, USA/Chine | 04/2025 | T2 |
| ✅ Exigences NVIDIA Omniverse / CloudXR : 100-200 Mbps, latence pose→image 30 ms idéale, **100 ms maximum** | NVIDIA Docs | 2025-2026 | T1 |
| ✅ NVIDIA Omniverse **Kit App Streaming** : applications 3D OpenUSD streamées dans un navigateur Chromium, serveurs RTX | NVIDIA Technical Blog | 20/08/2025 | T1 |
| 🔮 Taille du marché RA mobile : 12,8 → 49,6 → 65,2 Md$ selon les cabinets (2024-2026) ; **aucun consensus** | Emergen / MarketsandMarkets / Precedence | 2025-2026 | T3 |

**Lecture :** trois voies rendent le métavers accessible sans installation lourde — (1) le **navigateur** (WebGL/WebGPU, bientôt Roblox dans Chrome), (2) le **pixel streaming** (Fortnite via Xbox Cloud, Omniverse Kit), (3) l'**application légère universelle** (Roblox, Fortnite installables partout). Le WebXR immersif (casque dans le navigateur) reste lui bloqué sur Safari/iOS ; c'est le WebGPU et le streaming qui portent réellement l'accès « sans casque ».

## 2. Réalité augmentée mobile : la caméra comme passerelle

| Affirmation / chiffre | Source | Date | Confiance |
|---|---|---|---|
| ✅ Pokémon GO : **> 800 M de joueurs cumulés**, **> 1 Md$ de revenus en 2025** | Scopely (communiqué 10 ans) | 10/07/2026 | T1 |
| ✅ Pokémon GO : **20 M+ de joueurs actifs hebdomadaires** ; 100 M+ de joueurs uniques en 2024 | Scopely (annonce de rachat) | 12/03/2025 | T1 |
| ✅ Pokémon GO : cumul ≈ **9,1 Md$** de dépenses joueurs (iOS + Android) ; DAU ≈ 12 M, MAU ≈ 40 M (avril 2026) | AppMagic / Udonis | 2026 | T2 |
| ✅ Snapchat : **350 M+ d'utilisateurs AR/jour**, **8 Md d'utilisations de Lenses/jour**, 400 000 développeurs, 4 M de Lenses | Snap Inc. (résultats 2025) | 05-11/2025 | T1 |
| ✅ Google « Try it on » : essayage virtuel sur **milliards d'articles** à partir d'une photo ; vêtements US (07/2025), chaussures + Australie/Canada/Japon (10/2025) | Google (blog officiel) | 2025 | T1 |
| ✅ Apple : AR Quick Look (essayage produit 3D/USDZ sans app depuis iOS 12) ; **chiffres d'adoption : non trouvés** | Apple Developer | 2018-2026 | T1 (aucun volume publié) |
| 🔮 Marché « essayage virtuel » : 12,09 Md$ (2025) → **15,29 Md$ (2026)** → 38,92 Md$ (2030) | The Business Research Company | 07/2026 | T3 |
| ✅ WebAR : **> 50 000 applications web** créées sur 8th Wall ; portée estimée à 3,5 Md de smartphones | 8th Wall / Niantic | 2018-2023 | T1 |
| ✅ Arrêt de l'offre hébergée 8th Wall annoncé (11/2025), abandon progressif en 2026, moteur open-source | 8th Wall / Niantic Spatial | 2025-2026 | T4 |

**Lecture :** la RA mobile est la forme la plus massive d'« immersion sans casque » : elle utilise la caméra déjà dans la main de l'utilisateur. Pokémon GO démontre que des centaines de millions de personnes acceptent de superposer du virtuel sur le réel sans aucun équipement additionnel.

## 3. Interopérabilité et standards cross-plateforme

| Affirmation / chiffre | Source | Date | Confiance |
|---|---|---|---|
| ✅ **OpenXR 1.1** publié ; runtimes conformes : Meta, Microsoft, Sony, HTC, PICO, Valve, Google (Android XR), Collabora (Monado) | Khronos Group | 15/04/2024 | T1 |
| ✅ WebXR utilise OpenXR comme backend par défaut dans Chrome, Edge, Firefox ; Unity (2020 LTS), Unreal (4.24), Godot (4.0), NVIDIA Omniverse conformes | Khronos (SIGGRAPH) | 2025 | T1 |
| ✅ Contre-exemple de fragmentation : les intégrations « OpenXR » Unity/Unreal de Meta bloquent sur PC les casques non-Quest | UploadVR | 05/2025 | T4 |
| ✅ Epic : **972 M de comptes cross-platform**, 317 M d'utilisateurs PC | Epic Games, *2025 Year in Review* | 02/2026 | T2 |
| 🔮 Fortnite : ~110 M MAU mondiaux (2025), 650 M comptes enregistrés | compilations tierces | 2025-2026 | T3/T4 |
| ✅ Roblox : un seul compte et une seule progression sur PC, mobile, Xbox, casques VR | Roblox (politique de confidentialité) | constant | T1 |

## 4. Sobriété matérielle (volet technique et environnemental)

| Affirmation / chiffre | Source | Date | Confiance |
|---|---|---|---|
| ✅ Smartphone reconditionné vs neuf : **−77 % à −91 % d'impact annuel**, **−87 % GES**, 82 kg de matières premières évitées | ADEME, *Évaluation de l'impact environnemental des produits reconditionnés* | 2022 / rééd. 2024-2025 | T1 |
| ✅ **63 % des smartphones utilisés ont moins de 2 ans** ; passer un PC/tablette de 2 à 4 ans d'usage améliore son bilan environnemental de **50 %** | ADEME, guide sobriété numérique | 2021-2026 | T1 |
| ✅ **1,2 milliard de smartphones vendus dans le monde en 2024** | ADEME (infographie) | 01/2025 | T1 |
| ✅ France : **6,9 M de téléphones reconditionnés vendus en 2023 = 37 % du marché** | ADEME | 2023 | T1 |
| ✅ La phase de production ≈ **45 % de l'empreinte énergétique du numérique** ; **> 90 %** du cycle de vie d'un smartphone est consommé avant l'achat (si gardé 2 ans) ; > 80 % pour un ordinateur portable | The Shift Project, *Lean ICT* | 10/2018 | T1 |
| ✅ Trajectoire « Sobriété » : croissance de la consommation énergétique ramenée de **+9 %/an à +1,5 %/an** | The Shift Project, *Lean ICT* | 10/2018 | T1 (scénario) |
| ✅ Rapport dédié *Mondes virtuels & réseaux face à la double contrainte carbone* | The Shift Project | 15/03/2024 | T1 |
| ✅ Chiffrage **spécifique** « accès métavers sans casque → matériel évité » : **non trouvé** (ADEME/Shift) | — | — | — |

## Limites et nuances techniques

1. **Latence non résolue sur mobile.** Mesures académiques NSDI'25 : **112-403 ms** de latence interactive sur cloud gaming mobile (moyenne 163 ms), alors que le seuil de jouabilité est < 100 ms ; le VSync Android pèse 35,7 ms de la latence réseau exclue. Un essai RootMetrics (Los Angeles) avait montré qu'aucun opérateur 5G n'atteignait l'exigence de 10-30 ms annoncée. La 5G est une condition nécessaire, non suffisante.
2. **Qualité graphique contre coût réseau.** Le streaming haute fidélité exige 100-200 Mbps (NVIDIA Omniverse) ; Xbox n'exige que 10-20 Mbps mais avec compression visible. Le compromis qualité/débit est le point d'entrée obligé du raisonnement « sobriété ».
3. **Fragmentation des navigateurs.** WebXR n'est pas *Baseline* et reste absent de Safari/iOS (bug WebKit ouvert) alors que WebGPU l'est depuis iOS 26 : l'accès « sans casque » dépend de deux stacks différentes selon la plateforme. Chrome d'abord pour Roblox (« d'autres navigateurs suivront, sans calendrier »).
4. **Coût et usages contraints du cloud.** Files d'attente, sessions limitées à 60 min (Fortnite gratuit), abonnements jusqu'à ~20 $/mois (GeForce NOW Ultimate) : le « pas de matériel » se paie en abonnement et en infrastructure. Les centres de données concentrent par ailleurs l'essentiel de la trajectoire énergétique du numérique (Shift Project, AIE).
5. **Fragilité des plateformes et opacité des chiffres.** Fermetures Mozilla Hubs (2024), Spatial (juillet 2026), vague Horizon/Rec Room (2026) ; les opérateurs ne publient plus d'utilisateurs (derniers comptes officiels : 2023-2024). Toute projection d'audience cloud en 2026 est modélisée, non comptée.

## Sources principales

- W3C, *WebXR Device API* (CRD) — https://www.w3.org/TR/2025/CRD-webxr-20251001/
- MDN, *WebXR Device API* — https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API
- gpuweb, *Implementation Status* (WebGPU iOS 26) — https://github.com/gpuweb/gpuweb/wiki/Implementation-Status
- npm registry, `three` — https://www.npmjs.com/package/three
- AFP/France 24, Roblox (RDC 2026) — https://www.france24.com/fr/info-en-continu/20260911-jeux-video-roblox-va-permettre-de-jouer-hors-de-l-application-et-mieux-payer-les-createurs
- Xbox/Epic, *Play Fortnite on Xbox Cloud Gaming* — https://www.fortnite.com/mobile/xbox-cloud-gaming
- Mozilla, *End of support for Mozilla Hubs* — https://support.mozilla.org/en-us/kb/end-support-mozilla-hubs
- MSH-LSE, fermeture de Spatial — https://web.msh-lse.fr/metaversic/2026/05/29/la-nuit-tombe-aussi-sur-spatial/
- Compilation 2026 (écart des estimations cloud gaming) — https://coopboardgames.com/statistics/cloud-gaming-market-size/
- USENIX NSDI'25, *Dissecting and Streamlining the Interactive Loop of Mobile Cloud Gaming* — https://www.usenix.org/system/files/nsdi25-li-yang.pdf
- NVIDIA, *Spatial Streaming Network Setup* — https://docs.omniverse.nvidia.com/avp/latest/setup-network.html
- NVIDIA, *Omniverse Kit App Streaming* — https://developer.nvidia.com/blog/deploying-your-omniverse-kit-apps-at-scale/
- Scopely/Axis Intelligence, statistiques Pokémon GO 2026 — https://axis-intelligence.com/pokemon-go-statistics/
- Snap Inc., *Lens Fest 2025* — https://newsroom.snap.com/lens-fest-2025?lang=en-US
- Google, *Try On expansions* — https://blog.google/products-and-platforms/products/shopping/virtual-try-on-shoes/
- Khronos, *OpenXR 1.1* — https://www.khronos.org/news/press/khronos-releases-openxr-1.1-to-further-streamline-cross-platform-xr-development
- ADEME, reconditionnement vs neuf — https://librairie.ademe.fr/economie-circulaire-et-dechets/5241-evaluation-de-l-impact-environnemental-d-un-ensemble-de-produits-reconditionnes.html
- The Shift Project, *Lean ICT* — https://theshiftproject.org/publications/pour-une-sobriete-numerique/
- The Shift Project, *Mondes virtuels & réseaux* — https://dev.theshiftproject.org/publications/mondes-virtuels-reseaux-double-contrainte-carbone/
