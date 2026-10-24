# npm-lock-route-map

## Français

Montrer quelle version résolue chaque dépendance npm atteint réellement.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m npm_lock_route_map examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Cartographie les routes physiques d’un package-lock v3 : résolution depuis le paquet demandeur, dépendances imbriquées, hoist, packages scopés et absences optionnelles. Ne confond pas deux versions installées au même nom.

### Limites

Lecture du lock fourni sans npm install ni réseau. Pas de résolution semver/peer, de vérification d’intégrité distante ni de suivi des liens workspace ; un chemin résolu ne prouve pas la satisfiabilité du manifeste.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Show which resolved version each npm dependency actually reaches.

Synthetic data; no network access or secret required.

```sh
python -m npm_lock_route_map examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Maps physical package-lock v3 routes: requester-relative resolution, nested dependencies, hoisting, scoped packages and optional absences. Does not conflate installed versions sharing a name.

### Limits

Reads the supplied lock without npm install or network. No semver/peer solving, remote-integrity verification or workspace-link traversal; a resolved path does not prove manifest satisfiability.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Mostrar qué versión resuelta alcanza realmente cada dependencia npm.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m npm_lock_route_map examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Mapea rutas físicas de package-lock v3: resolución relativa al solicitante, dependencias anidadas, hoist, paquetes con ámbito y ausencias opcionales. No confunde versiones con el mismo nombre.

### Límites

Lee lock suministrado sin npm install ni red. Sin resolución semver/peer, integridad remota o seguimiento de enlaces workspace; ruta resuelta no prueba satisfacibilidad del manifiesto.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json
- https://nodejs.org/api/modules.html#loading-from-node_modules-folders
