# Proof and receipt contract

## Proof layers

Use the lowest-cost evidence that actually reaches the claim, but never let a
lower layer certify a higher one.

| Claim | Minimum proof |
|---|---|
| Source is releasable | Clean exact checkout, dependency lock, scenario gates, stack-aware CI |
| Backend candidate works | Provider identity, health, real domain operation, trace or receipt |
| Bounded rollout is safe | Declared traffic share/window, error totals, breakers, severity logs |
| Web candidate works | Unaliased raw release identity plus rendered user journey and browser health |
| Canonical is live | Canonical raw identity, API health, rendered journey, trace, provider alias/traffic reread |
| Evaluation is inspectable | Trace-local dataset/case/score, latency, token, cost status, and dashboard/readback link |
| Repository is closed | Exact-head CI, verified archive, zero open stack items, only-main audit |

Capture before/after when behavior changed. A backend-only change still needs a
before/after request, trace, metric, or durable-state receipt. For UI work,
capture pixels plus DOM/console/network evidence at declared viewports.

## Receipt fields

Every release receipt should make these questions answerable without reading a
terminal transcript:

```json
{
  "schema_version": "proof-carrying-release/v1",
  "release_id": "bounded-public-id",
  "application_sha": "40-lowercase-hex",
  "evidence_sha": null,
  "state": "WEB_CANDIDATE_PASS",
  "provider": {
    "surface": "web",
    "candidate_id": "provider-stable-id",
    "previous_stable_id": "provider-stable-id",
    "canonical_matches_candidate": false
  },
  "observation": {
    "started_at": "ISO-8601",
    "completed_at": "ISO-8601",
    "traffic_percent": 0,
    "errors": 0,
    "breakers_open": 0
  },
  "proof": {
    "raw_identity": "relative/path.json",
    "api": "relative/path.json",
    "browser": "relative/path.json",
    "trace": "relative/path.json"
  },
  "verdict": "PASS"
}
```

Use bounded public IDs; omit tenant, account, email, local home, secret hashes,
cookies, bearer values, and provider hosts that encode an identity.

## Evidence closure

1. Preserve failed attempts separately and link them from the final receipt.
2. Sanitize before hashing. Record a redaction ledger with original/sanitized
   byte hashes and field classes, never original values.
3. Normalize reviewable text; keep provider-native raw logs and media binary.
4. Generate the artifact manifest last and atomically. Cover every committed
   artifact except the manifest and root receipt.
5. Recompute byte length and SHA-256 from a clean checkout.
6. Bind the root receipt to the manifest hash, application SHA, evidence SHA,
   provider identities, canonical proof, rejected attempts, and known limits.
7. Run a privacy scan over text and OCR the published screenshots/video frames.

Cost categories are `provider_measured`, `estimated_from_measured_tokens`,
`proven_zero_no_model`, and `unmeasured`. Never turn missing cost into zero.
