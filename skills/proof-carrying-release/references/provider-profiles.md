# Provider profiles

Adapt provider commands to the project's maintained runbook. The gates are
portable; product names are examples, not defaults.

## Backend service

1. Record service, region/project, exact serving revision, traffic split, image
   digest, release identity, and rollback command.
2. Apply compatible migrations before traffic when the application contract
   requires them; capture schema/version predicates without data values.
3. Deploy a new immutable revision at zero traffic.
4. Run liveness and one real semantic operation against the candidate target.
5. Move the declared bounded share, watch the full window, and record request
   volume, errors, open breakers, severity logs, latency budget, and trace IDs.
6. Promote only when thresholds pass, then reread service state and canonical
   health. Otherwise restore the exact recorded predecessor and prove 100%.

For Cloud Run, use a tagged or revision-specific URL for candidate smoke and
`gcloud run services describe` plus logging queries for state. Do not infer the
traffic split from deploy output.

## Web application

1. Ensure build-time and runtime release identity variables exist before the
   build. A configuration edit requires a new deployment.
2. Create an unaliased immutable candidate. Keep deployment protection intact;
   use the provider's supported authenticated test path.
3. Verify the raw response contains the exact release signal and crawlable
   product signal. A hydrated screenshot cannot substitute for raw content.
4. Run the declared rendered journey against the candidate: desktop/mobile as
   relevant, console/network health, accessibility, reload/restore, and exact
   trace-linked selection.
5. Move the alias only after candidate PASS. Use a provider precondition or
   compare-and-swap when available. Otherwise reread the alias immediately
   before the move and abort if it drifted from the recorded predecessor.
   Confirm the alias resolves to that deployment, then rerun raw and rendered
   gates on canonical.

For Vercel, `READY` means the deployment built; it does not prove environment
predicates, auth routes, canonical alias state, or product behavior.

## Coupled release

Release backend and web sequentially. If backend promotion precedes a web
failure, keep the web alias on stable and roll the backend back to its recorded
predecessor. Preserve both the web no-op rollback and backend rollback receipts.
Retry from a fresh backend candidate when the repaired web configuration may
change tokens, audiences, URLs, or cross-surface behavior.
