# Specs

One file per workflow: `specs/<workflow-name>.md`, started from the kit's `kit/templates/workflow-spec.md` by the `3b-spec` skill.

A spec lands by pull request and is approved by the workflow's owner before anything is built. CI (`.github/workflows/specs.yml`) checks that every spec has its required sections filled and its base fixtures present.
