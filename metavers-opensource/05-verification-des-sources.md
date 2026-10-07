# Note de vérification des sources — Dossier « Métavers et projets open source »

*Contrôle qualité effectué le 7 octobre 2026 — traçabilité de la fiabilité du dossier.*

---

## 1. Objet et périmètre

Ce dossier répond à une problématique transverse (« comment exploiter l'open source au service du développement et de l'adoption du métavers ») et s'appuie, pour les faits déjà établis, sur les deux dossiers voisins du dépôt (`metavers-ia/`, `metavers-crossplateforme/`). Aucun chiffre n'est repris de ces dossiers sans y être renvoyé.

**Périmètre de vérification** : les 4 notes (`01` à `04`), la synthèse et le rapport principal. Le dialogue inter-agents (`courant.md`) assure la traçabilité des arbitrages.

---

## 2. Hiérarchie de confiance appliquée

| Tier | Définition | Exemples dans ce dossier |
|---|---|---|
| **T1** | Source primaire : organisation standard, éditeur, publication scientifique, communiqué officiel | W3C, Khronos, gpuweb, Linux Foundation, Godot (article officiel), Unity (blog), Roblox (newsroom/arXiv), Blender (rapport annuel), Mozilla (page support), npm registry |
| **T2** | Presse de référence ou intermédiaire institutionnel relayant des données | Game World Observer, UploadVR, Game Developer, 80.lv, Blendernation, CG Channel, vr.org, Collabora (blog corporate), arXiv (revue par les pairs) |
| **T3** | Projection de cabinet / estimation de marché / blog non primaire | market.us (CAGR 15,1 %), blogs de comparaison de tarifs Unity/Unreal (tech-insider, blog.promise.legal) |
| **T4** | Source secondaire, tracker, agrégateur, non vérifié à la source primaire | UploadVR sur le verrouillage Meta des SDK (réseau), trackers de téléchargements tiers |

**Règle appliquée** : aucune affirmation chiffrée sans source nominative et date ; toute limite de mesure est **explicite** dans la note concernée plutôt que gommée.

---

## 3. Contrôles effectués

| # | Point contrôlé | Résultat |
|---|---|---|
| 1 | Statut WebXR (CRD, pas *Baseline*, absent Safari/iOS) | ✅ Conforme au dossier cross-plateforme (`metavers-crossplateforme/02-technologies-sans-casque.md`) — dates 01/10/2025 et 02/06/2026 alignées |
| 2 | OpenXR 1.1 (15/04/2024) + liste des runtimes conformes | ✅ Conforme à `metavers-crossplateforme/01` et au rapport cross-plateforme |
| 3 | Three.js ≈ 12,2 M et Babylon ≈ 304 k téléchargements npm/semaine | ✅ Même relevé npm (24/09/2026) que le dossier cross-plateforme — aucune divergence |
| 4 | Cube 3D : 1,8 Md de paramètres, 1,5 M d'assets | ✅ Cohérent avec `metavers-ia/01-innovations.md` et `00-synthese.md` (référence dossier voisin) |
| 5 | Roblox Cube « open source » | ✅ Confirmé : newsroom Roblox 17/03/2025 (« open-sourcing… anyone on or off the Roblox platform »), dépôt GitHub `Roblox/cube`, HuggingFace |
| 6 | Arrêt de Mozilla Hubs | ✅ Source primaire : support.mozilla.org, fin de support **31/05/2024** (Hubs Cloud antérieurement au 01/01/2024) ; reprise communautaire documentée par la presse XR (02/2024) |
| 7 | Godot : « ~2 M par version », communauté « doublée », jeux Steam « exponentiels » | ✅ Toutes trois issues de l'article officiel du 06/05/2026 ; les **réserves méthodologiques de l'auteur lui-même** sont reprises telles quelles (données hétérogènes, jusqu'à févr. 2026, pas de suivi utilisateur) |
| 8 | « Godot a doublé sa base dans le mois » après Unity | ⚠️ **Tier 2** (Game World Observer, 27/03/2024) — pas de source Godot primaire ; conservé avec attribution |
| 9 | Unity Runtime Fee : annonce → révocation 12/09/2024 | ✅ Source primaire unity.com |
| 10 | Blender : revenus 4,2 → 5,7 M€ (+36 %) ; exercice 2024 déficitaire | ✅ Rapport annuel 2025 (23/09/2026, primaire) + 80.lv (16/09/2025, T2) — les deux faits sont complémentaires et **non contradictoires** (déficit 2024, croissance 2025) |
| 11 | OSAID 1.0 publiée le 28/10/2024 ; contestation « poids seuls ≠ open source » | ✅ OSI (primaire) + Wolters Kluwer Copyright Blog (04/03/2025, T2) |
| 12 | MIT Sloan « 80 % de choix pour des modèles fermés » | ✅ Article universitaire du 20/01/2026 ; **périmètre du panel non précisé dans le titre** → réserves n°4 |
| 13 | Prix Unity et Unreal | ⚠️ **Unreal : 5 % de royalty au-delà de 1 M$ → confirmé sur la licence Epic (Tier 1)** ; **Unity : abonnement par siège (grille officielle)**, la valeur « ≈ 2 310 $/siège/an » reste **Tier 3** (blogs 2026) — à confirmer sur unity.com avant reprise chiffrée |
| 14 | « Aucune mesure d'adoption du Metaverse Standards Forum » | ✅ Absence vérifiée sur metaverse-standards.org : communiqués d'initiatives, pas de métriques publiées → classé **lacune documentaire** |
| 15 | Licence Hunyuan3D | ⚠️ *Community license* (GitHub) : **pas** une licence OSI → classé « open weights » dans `03` et `00` |
| 16 | Cross-cohérence avec les autres dossiers | ✅ Aucun chiffre de ce dossier ne contredit `metavers-ia/` ou `metavers-crossplateforme/` (contrôle sur : Roblox DAU, arrêts de services, standards) |

---

## 4. Décisions de classement prises

1. **« Open source » réservé** aux projets satisfaisant l'OSAID 1.0 ou une licence OSI (Godot/MIT, Blender/GPL, Three.js/MIT, O3DE/Apache 2.0, Monado/MIT, glTF, WebXR).
2. **« Open weights »** pour Llama (Meta) et Hunyuan3D (Tencent) — licences communautaires.
3. **« Source-available »** non utilisé dans ce dossier : aucune cible concernée vérifiée à ce stade.
4. Les chiffres Godot sont **toujours** accompagnés de la réserve « téléchargements par version, pas utilisateurs ».

---

## 5. Lacunes reconnues (chiffres recherchés et non trouvés)

- **Part des contenus métavers créés avec des outils open source** (aucune donnée).
- **Nombre d'expériences/exposants utilisant WebXR** en production (aucune mesure publique).
- **Budget exact de l'Open Metaverse Foundation** et nombre de projets actifs (non publié).
- **Audience réelle des PNJ à modèle local** (aucun déploiement chiffré).
- **Périmètre exact des licences** `Roblox/cube` et `Tencent-Hunyuan/Hunyuan3D-2` pour usage commercial (à lire au niveau du fichier LICENSE).
- **Coût comparatif réel d'un projet** développé avec/outils ouverts vs propriétaires (aucune étude).

---

## 6. Règles de reprise pour les autres fichiers du dépôt

1. Toute reprise d'un chiffre de ce dossier doit conserver son **Tier** et sa **date**.
2. Ne jamais écrire « Llama est open source » sans la mention **open weights** et le renvoi à l'OSAID.
3. Les tarifs Unity (Tier 3) ne doivent pas quitter le dossier sans confirmation primaire ; Unreal (5 % > 1 M$) est confirmé en licence officielle.
4. Le statut de WebXR (non *Baseline*, absent d'iOS) doit accompagner toute mention « le métavers est accessible depuis le navigateur ».
