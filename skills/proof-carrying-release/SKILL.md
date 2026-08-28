---
name: proof-carrying-release
description: Audit, execute, resume, or close a production software release whose exact source revision must pass Graphite-stack CI, isolated candidate or canary, semantic, trace, and canonical user-surface gates before promotion, with rollback receipts and recoverable only-main cleanup. Use for ship/deploy/release requests, failed-rollout recovery, exact live proof, or "merge the stack and leave only main." Do not use for feature implementation, local-only QA, or ordinary CI.
license: MIT
---

# Proof-carrying release

A release owner is trying to move one exact change into production. The common
failure is not a broken build; it is a green lower-layer signal being mistaken
for proof that users received the intended behavior. This skill owns the chain
from frozen source to canonical observation and recoverable repository closure.

## Boundary

Feature implementation and feature proof happen before this skill. Consume the
project's existing tests, feature packet, traces, evals, clips, and browser
journeys. Do not replace them with a second harness. If `feature-proof`,
`before-after-proof`, `agentic-ui-qa`, NodeProof, or an equivalent maintained
gate is installed, consume its receipts. Otherwise use the project's own
authoritative commands and journeys.

This skill owns:

- exact release identity and provider target identity;
- Graphite stack order and exact-head CI;
- dark candidates, bounded traffic, watch, promotion, and rollback;
- candidate and canonical semantic proof;
- evidence finalization, independent challenge, ref archival, and cleanup.

It does not grant new authority. A request to ship covers ordinary candidate
creation, bounded traffic movement, promotion, and automatic rollback for the
named application. It does not silently authorize credentials, billing,
identity-provider objects, permissions, domains, destructive migrations, or
unarchived deletion.

## Read only what the release needs

- Always read [release-state-machine.md](references/release-state-machine.md).
- Before any external mutation, read
  [authorization-and-secrets.md](references/authorization-and-secrets.md).
- For proof capture or evidence finalization, read
  [proof-and-receipt-contract.md](references/proof-and-receipt-contract.md).
- For provider rollout, read [provider-profiles.md](references/provider-profiles.md).
- For stacked merge, archive, or cleanup, read
  [git-graphite-closeout.md](references/git-graphite-closeout.md).
- When creating or changing this skill, run the scenarios in
  [forward-tests.md](references/forward-tests.md).

## Modes

Choose from observed state; do not restart a valid release from memory.

### Audit

Read-only. Identify the exact application commit, stack topology, required
checks, deployable surfaces, canonical URLs, provider targets, previous stable
identities, rollback commands, proof journeys, evidence location, and current
authorization. Return `READY` only when every prerequisite is observed.

### Execute

Start from a clean detached checkout of the exact application commit. Run the
project's gates, deploy an immutable dark candidate, run semantic smoke, move a
bounded share of traffic, watch the declared window, promote the backend, then
prove an unaliased frontend candidate. Move the canonical alias only after the
candidate passes. Re-run raw, API, browser, console/network, and trace gates on
canonical.

### Resume

Read provider state and receipts first. Confirm which target is serving now,
which candidate failed, and whether rollback completed. Diagnose the earliest
failed layer. A configuration change requires a fresh deployment; never reuse
a build whose environment was snapshotted earlier. Invalidate old success
markers and rerun the affected chain.

### Closeout

Finalize evidence only after canonical proof. Submit and merge Graphite stacks
in dependency order, wait for exact-head CI, and reverify canonical state if a
merge can trigger deployment. Create and verify a bundle of all refs before any
deletion. Remove worktrees and branches only after semantic branch audit, zero
open stack items, clean `main`, and local/cached/remote SHA equality.

## Core invariants

1. Track `application_sha`, `evidence_sha`, and `main_sha` separately. A later
   documentation commit did not change deployed runtime bytes.
2. Record the exact previously serving provider identity before mutation.
3. Provider commands are not transactions. After any exit, reread provider
   state; never infer success or rollback from the command status alone.
4. Couple surfaces sequentially with separate rollback boundaries. A healthy
   API cannot certify the web, and an unaliased web candidate cannot certify
   the canonical URL.
5. Every candidate proof is fresh for that candidate. Never reuse a smoke,
   watch, trace, or screenshot marker across revisions or rebuilds.
6. Promotion requires both candidate proof and fresh canonical proof. Provider
   `Ready`, green CI, DOM, pixels, and trace readback each prove different
   layers.
7. Unknown cost remains unknown. A dashboard row must point to the trace from
   the exact journey whose latency, tokens, or cost it reports.
8. Keep failed candidate, incident, and rollback receipts. Failure evidence is
   diagnostic state, not clutter.
9. Generate the artifact manifest after sanitization and last. Do not commit
   credentials, personal paths, account-derived hosts, secret values, or
   unsalted secret hashes.
10. Archive before delete. Patch-equivalent work may be dropped after audit;
    unique unsafe work is archived, not merged merely to satisfy cleanup.

## Execution loop

1. Classify the request and name one literal release PASS statement.
2. Build a requirement-to-proof matrix, including failure and rollback paths.
3. Freeze source identity and capture provider/rollback baselines.
4. Confirm authorization at the next actual mutation boundary.
5. Advance one state at a time; write a receipt after observing each state.
6. On failure, stop forward motion, reread providers, and rollback the affected
   surface. Preserve the failed evidence.
7. After canonical PASS, finalize and verify evidence bytes.
8. Ask an independent judge to refute the release from raw state and artifacts.
9. Merge, reprove if deployment can move, archive, then clean refs/worktrees.
10. Report what is live, what is merely local, and every remaining limitation.

## Stop conditions

- `BLOCKED`: required authorization is absent, the prior stable target cannot
  be identified, rollback is not possible, or the same bounded repair fails
  three times.
- `ROLLED_BACK`: the candidate failed and observed provider state confirms the
  prior stable target serves 100% again.
- `PASS`: canonical raw/API/browser/trace gates name the exact application
  revision, evidence verifies, independent judgment passes, and requested
  repository closure is observed.

Never use "live," "deployed," "shipped," or "only main remains" before the
corresponding observed PASS gate.
