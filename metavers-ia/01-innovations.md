# Métavers et Intelligence Artificielle — Les innovations technologiques (2024‑2026)

*Rapport annexe 1/4 — recherche documentaire, sources à l'appui*

## 1. Cadrage

Les estimations de marché divergent fortement : McKinsey annonçait jusqu'à 5 000 milliards $ d'impact d'ici 2030 [24], tandis que Grand View Research chiffre le marché mondial du métavers à 105,4 Md$ en 2024, projeté à 936,6 Md$ en 2030 (TCAC 46,4 %) [25]. Ces chiffres sont à prendre comme des ordres de grandeur, pas des prévisions vérifiées. Gartner, lui, a placé en 2025 les modèles multimodaux et les agents IA au « sommet des attentes exagérées » [23], et son Hype Cycle Emerging Technologies 2025 tourne autour de l'« IA agentic », de l'« hypermachinité » et de l'humanité augmentée — le métavers y est devenu un cas d'usage transversal plutôt qu'un thème autonome [22].

## 2. Technologies clés du métavers

**Casques et calcul spatial.** IDC estime les expéditions mondiales XR (lunettes + casques) à 14,5 millions d'unités en 2025, soit +41,6 %, tirées par les lunettes AI (+211 %) alors que les casques MR/VR reculent de 42,8 % [1]. Les lunettes XR devraient croître de 29,3 % par an jusqu'en 2029 [1]. Sur le segment XR strict, IDC prévoyait initialement un repli de 12 % en 2025 puis une reprise de +87 % en 2026 dépassant le pic de 11,2 M d'unités de 2021 (TCAC 38,6 % 2025‑2029) [2] — **les deux séries sont difficilement comparables** (périmètres différents). Meta détenait 50,8 % du marché AR/VR au T1 2025 [3].

**Lancements majeurs.** Apple a équipé le Vision Pro d'une puce M5 (latence capteur‑écran de 12 ms, rafraîchissement 120 Hz, accélération matérielle du ray tracing, IA jusqu'à 50 % plus rapide) en octobre 2025 [4] ; visionOS 26 utilise un algorithme génératif pour transformer des photos 2D en scènes spatiales en profondeur [5]. Samsung a lancé Galaxy XR (1 799 $) en octobre 2025, premier produit d'Android XR avec Gemini intégré au niveau système et standards ouverts OpenXR/WebXR [6][7]. Meta a lancé en septembre 2025 les lunettes Meta Ray‑Ban Display et le bandeau Neural Band (EMG de surface, 18 h d'autonomie) [8], puis a annoncé l'écriture neurale manuscrite et la navigation piétonne dans 32 villes au CES 2026 [10].

**Standards et rendu temps réel.** OpenUSD (Pixar/NVIDIA) est standardisé par l'Alliance for OpenUSD, créée en 2023 sous l'égide du Linux Foundation [18]. NVIDIA fait d'Omniverse une plateforme « native OpenUSD » connectée à OpenXR, permettant le streaming de scènes USD vers Vision Pro, Quest ou Pico [18][19]. Ces briques servent de socle aux jumeaux numériques industriels (blueprint « Mega » pour simuler des flottes de robots en entrepôt, 2025) [16].

**Blockchain / NFT.** Le marché du foncier virtuel resterait autour de 4,12 Md$ en 2025, avec un prix moyen de parcelle retombé à ~3 000 $ (pic : ~15 000 $ en 2021) et ~80 % des terrains non développés [32] — **chiffres issus d'une source secondaire (échangeur crypto), donc incertains**.

## 3. L'apport de l'IA

**Text‑to‑3D et génération procédurale.** Meta a présenté WorldGen (nov. 2025), système de bout en bout générant des mondes 3D navigables à partir d'un prompt texte : scènes texturées de 50 × 50 m, compatible Unity/Unreal, en ~5 minutes [11][12]. Roblox a open‑sourcé Cube 3D (mars 2025), modèle fondation de 1,8 Md de paramètres entraîné sur 1,5 M d'assets 3D, puis réduit la latence de génération de 31 s à 4 s (juin 2025) [13][14].

**NPC, agents et copilotes.** Meta Horizon Studio génère par prompt des meshes, textures, skyboxes, audio, scripts TypeScript et des NPCs dotés d'histoire, voix et style de conversation ; le Meta Horizon Engine récemment refondu charge les mondes 4× plus vite et accueille 100+ joueurs simultanés (5× plus) [9]. Roblox ajoute un Assistant intégré à Studio, une API de génération textuelle et une API de traduction temps réel in‑game (2025) [13].

**Multimodalité, voix, navigation.** Gartner place le multimodal parmi les innovations IA appelées à s'imposer sous 5 ans [23]. Les lunettes AI délivrent traduction, sous‑titres et navigation temps réel (Meta Ray‑Ban Display) [10], tandis que Gemini Live sur Galaxy XR voit et entend l'environnement pour répondre conversationnellement [7].

## 4. Convergence IA‑métavers : les plateformes

- **Meta** : stratégie de convergence explicite — « là où AR/VR et IA se rencontrent, c'est le métavers » ; outils génératifs Horizon Studio, Hyperscape (capture photoréaliste de pièces), préparation d'un assistant IA agentic [8][9].
- **Microsoft** : a retiré Microsoft Mesh le 1ᵉʳ décembre 2025 au profit des « immersive events » natifs dans Teams (avatars, espaces 3D, PC/Mac/Quest), signe d'une priorité donnée à l'intégration logicielle plutôt qu'au métavers autonome [20][21].
- **NVIDIA** : Cosmos (world foundation models, 20 M d'heures de vidéo d'entraînement) couple à Omniverse pour générer des données synthétiques physiquement réalistes [15] ; Cosmos 3 (mai 2026) est présenté comme le premier « omnimodel » ouvert combinant vision, monde et action [17].
- **Google/Samsung/Qualcomm** : Android XR conçu « pour l'ère Gemini », qui doit passer des casques aux lunettes AI [6][7].
- **Roblox, Decentraland, Somnium Space** : génération 3D embarquée côté joueurs chez Roblox [13] ; Somnium Space a ajouté (version V3.1.1, 23/12/2025) le face/eye tracking **d'avatar** et les appels vidéo VR‑vers‑VR/IRL — l'eye tracking matériel du casque VR1 existant antérieurement [33].
- **Apple** : a suspendu en octobre 2025 le renouvellement du Vision Pro (variante N100) pour réallouer les équipes aux lunettes AI [27], cibles initialement annoncées fin 2026 [28] mais repoussées selon des informations ultérieures (fin 2027) — **calendrier incertain**.

## 5. Interfaces cerveau‑machine

Neuralink est passé de 7 participants (été 2025) à 12 patients en septembre 2025, cumulant ~15 000 heures d'usage et 7,5 h/jour en moyenne [29][30]. Côté français, le CEA développe l'implant **WIMAGINE® (64 canaux)**, le programme **AUDACE** (40 M€, France 2030, mars 2025) et l'essai **BCI4Stroke/BrainSync** (1ᵉʳ patient attendu en 2026) [34]. MIT Technology Review recense ~25 essais cliniques de BCI en cours en 2025 et estime que la rupture commerciale surviendra sous 5 à 10 ans [31]. Ces technologies restent **expérimentales et non approuvées à la vente**.

## 6. Jalons 2024‑2026

2024 : Mesh GA dans Teams [21], Vision Pro mondial. 2025 : Vision Pro M5, Galaxy XR, Meta Ray‑Ban Display, WorldGen, Cube 3D, Cosmos/Mega, retrait de Mesh. 2026 : CES tourné vers les lunettes AI (XREAL/Google, guides d'onde Lumus >70° de champ de vision), Cosmos 3, reports Apple [26][17][27].

---

## Sources

[1] IDC, *Global XR Shipments Rebound Behind Glasses‑First Momentum*, 2025, https://my.idc.com/getdoc.jsp?containerId=prUS54033425
[2] IDC, *Growth Expected to Pause for AR/VR Headsets*, 2025, https://my.idc.com/getdoc.jsp?containerId=prUS53278025
[3] IDC, *AR/VR Market Rebounds with 18.1% Growth*, 2025, https://my.idc.com/getdoc.jsp?containerId=prAP53608225
[4] Apple, *Apple Vision Pro upgraded with the M5 chip and Dual Knit Band*, 2025, https://www.apple.com/newsroom/2025/10/apple-vision-pro-upgraded-with-the-m5-chip-and-dual-knit-band/
[5] Apple, *visionOS 26 introduces powerful new spatial experiences*, 2025, https://www.apple.com/newsroom/2025/06/visionos-26-introduces-powerful-new-spatial-experiences-for-apple-vision-pro/
[6] Samsung, *Introducing Galaxy XR: Opening New Worlds*, 2025, https://news.samsung.com/global/introducing-galaxy-xr-opening-new-worlds
[7] Google, *Introducing Galaxy XR, the first Android XR headset*, 2025, https://blog.google/products-and-platforms/platforms/android/samsung-galaxy-xr/
[8] Meta, *Meta Connect 2025 Day One Keynote*, 2025, https://www.meta.com/blog/connect-2025-day-one-keynote-ai-glasses-ray-ban-display-neural-band-metaverse-news/
[9] Meta, *Meta Connect 2025 Day 2 Keynote Recap*, 2025, https://www.meta.com/blog/connect-2025-day-2-keynote-recap-vr-development-use-cases-wearable-device-access-toolkit/
[10] Meta, *CES 2026: Meta Ray‑Ban Display Teleprompter, Neural Handwriting…*, 2026, https://www.meta.com/blog/ces-2026-meta-ray-ban-display-teleprompter-emg-handwriting-garmin-unified-cabin-university-of-utah-tetraski/
[11] Meta Reality Labs, *WorldGen — Text to Immersive 3D Worlds*, 2025, https://www.meta.com/blog/worldgen-3d-world-generation-reality-labs-generative-ai-research/
[12] D. Wang et al., *WorldGen: From Text to Traversable and Interactive 3D Worlds*, 2025, https://arxiv.org/html/2511.16825
[13] Roblox, *Introducing Roblox Cube*, 2025, https://about.roblox.com/newsroom/2025/03/introducing-roblox-cube
[14] Roblox, *Accelerating AI Inference for 3D Creation on Roblox*, 2025, https://about.roblox.com/newsroom/2025/06/accelerating-ai-inference-roblox-3d-creation
[15] NVIDIA, *NVIDIA Launches Cosmos World Foundation Model Platform*, 2025, https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development
[16] NVIDIA, *NVIDIA Unveils 'Mega' Omniverse Blueprint*, 2025, https://blogs.nvidia.com/blog/mega-omniverse-blueprint/
[17] NVIDIA, *NVIDIA Launches Cosmos 3*, 2026, https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai
[18] NVIDIA, *OpenUSD Frequently Asked Questions — Omniverse*, consulté 2026, https://docs-prod.omniverse.nvidia.com/usd/latest/learn-openusd/faq.html
[19] NVIDIA, *Omniverse Spatial Documentation (OpenXR/CloudXR)*, consulté 2026, https://docs.omniverse.nvidia.com/xr/omniverse-spatial-docs/latest/
[20] Microsoft, *Immersive events in Microsoft Teams: Now generally available*, 2025, https://techcommunity.microsoft.com/blog/microsoftteamsblog/immersive-events-in-microsoft-teams-now-generally-available/4468628
[21] M. Finnegan, Computerworld, *Microsoft retires Mesh app, launches 'immersive spaces' for Teams*, 2025, https://www.computerworld.com/article/4100319/microsoft-retires-mesh-app-launches-immersive-spaces-for-teams.html
[22] Gartner, *2025 Hype Cycle for Emerging Technologies*, 2025, https://www.gartner.com/en/articles/hype-cycle-for-emerging-technologies
[23] Gartner, *Gartner Hype Cycle Identifies Top AI Innovations in 2025*, 2025, https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025
[24] McKinsey & Company, *Value creation in the metaverse*, 2022, https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/value-creation-in-the-metaverse
[25] Grand View Research, *Metaverse Market Size, Share & Trends Report, 2026‑2033*, 2025, https://www.grandviewresearch.com/industry-analysis/metaverse-market-report
[26] J. Ubrani, IDC, *The future of smart glasses was on full display at CES 2026*, 2026, https://www.idc.com/resource-center/blog/the-future-of-smart-glasses-was-on-full-display-at-ces-2026/
[27] M. Gurman, Bloomberg, *Apple Shelves Vision Headset Revamp to Prioritize Meta‑Like AI Smart Glasses*, 2025, https://www.bloomberg.com/news/articles/2025-10-01/apple-shelves-vision-headset-revamp-to-prioritize-meta-like-ai-smart-glasses
[28] M. Gurman, Bloomberg, *Apple Plans Glasses for 2026 as Part of AI Push*, 2025, https://www.bloomberg.com/news/articles/2025-05-22/apple-plans-glasses-for-2026-as-part-of-ai-push-nixes-watch-with-camera
[29] Neuralink, *Neuralink Update, Summer 2025*, 2025, https://neuralink.com/updates/
[30] TechSpot, *Neuralink: 12 patients have used its brain interface chips*, 2025, https://www.techspot.com/news/109403-elon-musk-neuralink-12-patients-have-used-brain.html
[31] MIT Technology Review, *Brain‑computer interfaces face a critical test*, 2025, https://www.technologyreview.com/2025/04/01/1114009/brain-computer-interfaces-10-breakthrough-technologies-2025/
[32] Bitrue, *Metaverse Land Sales: Decentraland vs Sandbox Q4 Update*, 2025, https://www.bitrue.com/blog/metaverse-land-sales-decentraland-vs-sandbox-q4
[33] Somnium Times, *Exciting Horizons: Somnium Space Unveils Major Updates at Developer Meetup*, 20/11/2025, et journal de versions officiel Somnium Space (V3.1.1, 23/12/2025), https://somniumtimes.com/2025/11/20/exciting-horizons-somnium-space-unveils-major-updates-at-developer-meetup
[34] CEA-Leti, *AVC : Brain-Computer Interface* (WIMAGINE®, AUDACE, BCI4Stroke/BrainSync), 02/06/2026, https://www.cea.fr/cea-tech/leti/Pages/actualites/News/AVC-Brain-Computer-Interface-FR.aspx

**Réserves** : chiffres McKinsey (2022) anciens ; estimations de marché très divergentes selon cabinets ; données foncières cryptos non vérifiées par une source primaire ; calendrier Apple non confirmé officiellement ; aucune donnée fiable localisée sur les brevets spécifiques déposés 2024‑2026.
