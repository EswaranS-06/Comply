#!/usr/bin/env bash
# Publish the current forge tree to main as a tagged release.
#
#   scripts/release.sh v0.2.1 "Sign-in and sessions"
#
# main receives everything on forge EXCEPT the paths in EXCLUDE.
# Run only after the checks in docs/12-testing.md pass.
set -euo pipefail

VERSION="${1:?usage: release.sh vX.Y.Z \"summary\"}"
SUMMARY="${2:?usage: release.sh vX.Y.Z \"summary\"}"
EXCLUDE=(docs .skills CLAUDE.md)

[[ "$VERSION" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "version must look like v0.2.1"; exit 1; }
[[ "$(git rev-parse --abbrev-ref HEAD)" == "forge" ]] || { echo "run from the forge branch"; exit 1; }
[[ -z "$(git status --porcelain)" ]] || { echo "working tree is not clean; commit first"; exit 1; }
git rev-parse -q --verify "refs/tags/$VERSION" >/dev/null && { echo "tag $VERSION already exists"; exit 1; }

SOURCE="$(git rev-parse --short HEAD)"
PATHSPEC=(.)
for p in "${EXCLUDE[@]}"; do PATHSPEC+=(":(exclude)$p"); done

git checkout -q main
git rm -rq --ignore-unmatch .
git checkout forge -- "${PATHSPEC[@]}"
git add -A
git commit -q -m "$VERSION: $SUMMARY" -m "Built from forge $SOURCE."
git tag -a "$VERSION" -m "$VERSION: $SUMMARY"
git checkout -q forge
git tag -a "forge-$VERSION" "$SOURCE" -m "forge source of $VERSION"

echo "released $VERSION on main from forge $SOURCE"
