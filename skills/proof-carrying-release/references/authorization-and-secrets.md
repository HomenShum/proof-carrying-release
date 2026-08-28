# Authorization and secrets

## Existing authority

Read-only repository/provider inspection, local tests, anonymous health checks,
predicate-only configuration diagnosis, and receipt preparation are reversible
and normally remain within a release request.

An explicit request to deploy or ship the named application normally covers:

- building immutable candidates;
- applying already-approved compatible migrations;
- bounded canary traffic and declared observation windows;
- canonical promotion after gates pass;
- automatic rollback to the recorded stable target.

It does not silently cover a materially different durable mutation:

- creating, rotating, or revoking credentials;
- creating identity-provider applications, callbacks, domains, organizations,
  users, roles, or permissions;
- enabling billing or paid services;
- destructive or incompatible schema/data changes;
- deleting refs or worktrees that are not in a verified archive;
- changing account, project, tenant, or repository scope.

If one is discovered, continue every safe prerequisite, then ask once
immediately before the action. State the exact object, scope, persistence, and
whether an old credential/object remains active. A generic “go” resumes actions
already named; it does not expand authority.

## Secret handling

- Prefer provider-native secret stores and stdin/clipboard-safe commands.
- Never place a secret in a command argument, repository file, screenshot,
  receipt, chat message, or shell output.
- Do not retain unsalted secret hashes or identifiers derived from secret
  values. Record boolean predicates such as present, correct shape, equal, and
  configured.
- When a UI reveals a one-time secret, copy it directly into the destination
  secret store, verify only predicates, clear clipboard/process state, and do
  not capture the revealing screen.
- Leave an old credential active unless revocation was separately authorized.
- Sanitize account-derived deployment hosts and local user paths before
  manifest generation. Keep deployment IDs and canonical public URLs when they
  prove the same fact without identity leakage.

If secret material reaches a log or artifact, stop publication, rotate it with
authorization, remove it from every reachable history, and regenerate all
affected receipts. Redaction alone does not repair an exposed credential.
