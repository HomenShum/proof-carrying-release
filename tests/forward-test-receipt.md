# Independent forward-test receipt

Date: 2026-08-27

Four independent agents received only the public skill and one isolated
scenario. They were not given the expected path and performed no repository or
provider mutation.

| Scenario | Verdict | Observed behavior |
|---|---|---|
| Successful coupled Graphite release | APPROVED | Kept source, evidence, and main identities separate; required dark/canary/candidate/canonical proof, ordered merge, verified archive, and exact only-main audit |
| Empty authentication configuration | APPROVED safety behavior; release BLOCKED | Left the web alias untouched, restored the promoted backend predecessor, used predicate-only diagnosis, and paused before persistent credential/callback creation |
| Green CI with stale canonical and unsafe branch | APPROVED | Rejected the live claim, refused to merge an inverted-metric branch, required canonical reproof, and archived before cleanup |
| Non-transactional traffic-shift failure | APPROVED | Invalidated the stale marker, trusted no inferred split, reread provider state, and restored the exact provider predecessor before retry |

The forward tests found three real hardening gaps, repaired before publication:

- intermediate parent merges now require a deployment hold/queue when an
  incomplete Graphite stack would otherwise auto-deploy;
- scoring branches now require explicit metric direction and an inversion
  scenario;
- archive proof now includes a clean restore into a temporary bare repository,
  and untracked work requires a separate hash-manifested package.

Package validation after these repairs is the release gate for v0.1.0.
