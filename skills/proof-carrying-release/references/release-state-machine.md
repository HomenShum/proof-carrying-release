# Release state machine

Use one append-only transition ledger per release. Each transition records the
exact application revision, observed provider target, timestamp, evidence path
and hash, actor class, and prior state. A prose update is not a transition.

```text
FROZEN
  -> PREFLIGHTED
  -> DARK
  -> SEMANTIC_PASS
  -> OBSERVED
  -> BACKEND_PROMOTED
  -> WEB_CANDIDATE_PASS
  -> CANONICAL_PASS
  -> EVIDENCE_FINAL
  -> MERGED
  -> ARCHIVED
  -> CLEAN
```

Any external failure branches to `INCIDENT`, followed by observed `ROLLED_BACK`
or `BLOCKED`. Resume only from the most recent receipt whose provider identity
still matches live state.

## Transition gates

| State | Required observation |
|---|---|
| `FROZEN` | Clean source checkout; exact commit and build inputs recorded |
| `PREFLIGHTED` | Migrations/config predicates, rollback target, quotas, tests, and permissions are ready |
| `DARK` | Immutable candidate exists with zero public traffic |
| `SEMANTIC_PASS` | Candidate health plus a real domain operation succeeds |
| `OBSERVED` | Bounded traffic/watch window completes with declared error and breaker limits |
| `BACKEND_PROMOTED` | Provider reread shows the backend candidate at intended traffic and healthy |
| `WEB_CANDIDATE_PASS` | Unaliased web candidate passes raw, runtime, browser, console/network, and trace gates |
| `CANONICAL_PASS` | Canonical URL resolves to that candidate and the same gates pass again |
| `EVIDENCE_FINAL` | Sanitized manifest and root receipt verify every committed artifact byte |
| `MERGED` | Dependency-ordered stack merged; exact final head checks pass |
| `ARCHIVED` | All refs and stack metadata exist in a verified recoverable archive |
| `CLEAN` | One clean main worktree; one local and remote main; all three main SHAs equal |

## Failure rules

- Invalidate a prior success marker before a new provider mutation.
- If a command fails, reread provider state before selecting rollback.
- A backend promoted before a web failure must be rolled back independently.
- An alias that never moved needs an explicit no-op rollback receipt.
- A configuration repair rebuilds a fresh candidate and restarts every gate
  whose runtime snapshot or downstream behavior may have changed.
- After three repair cycles for the same defect, record `BLOCKED` with raw
  evidence instead of weakening the gate.
