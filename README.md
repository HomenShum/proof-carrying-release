# proof-carrying-release

A public [Claude Code](https://claude.com/claude-code) skill for releases where
“CI passed” is not enough. It carries one exact application revision through a
Graphite stack, candidate/canary gates, canonical API and browser proof,
rollback, evidence closure, and recoverable only-`main` cleanup.

The skill is intentionally not another test runner. It consumes the tests,
feature packets, traces, dashboards, and browser journeys a project already
owns, then proves that the same bytes reached the surface users receive.

## Install

Preferred, through Homen Shum's public marketplace:

```text
/plugin marketplace add HomenShum/claude-marketplace
/plugin install proof-carrying-release@homenshum
/reload-plugins
```

Invoke it directly with:

```text
/proof-carrying-release:proof-carrying-release
```

For local development:

```bash
git clone https://github.com/HomenShum/proof-carrying-release.git
claude plugin validate ./proof-carrying-release --strict
claude --plugin-dir ./proof-carrying-release
```

## What it owns

```text
exact source -> stack-aware CI -> dark candidate -> bounded canary
             -> unaliased web candidate -> canonical reproof
             -> ordered merge -> verified ref archive -> only main
```

- Keeps `application_sha`, later evidence commits, and final `main` distinct.
- Treats API, raw response, rendered UI, traces, and dashboards as different
  proof layers.
- Records the previously serving target before every provider mutation.
- Rolls back coupled surfaces independently and preserves failed receipts.
- Pauses immediately before newly discovered credentials, identity-provider
  configuration, billing, permissions, or destructive data changes.
- Archives and verifies refs before deleting branches or worktrees.

See [the skill](skills/proof-carrying-release/SKILL.md) for the complete
protocol.

## License

MIT © Homen Shum
