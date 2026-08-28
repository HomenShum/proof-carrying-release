# Git and Graphite closeout

## Stack rules

- Inspect `gt log --stack` and provider PR state; do not trust stale local
  Graphite metadata.
- Every child is based on the exact intended parent commit. Evidence-only work
  may be a child of a test-fixture repair when the combined checkout requires
  that repair to reproduce.
- Before merging the first parent, determine whether each main update triggers
  an automatic deployment. If an intermediate parent is not independently
  releasable, hold/serialize deployment or use the repository's merge queue so
  canonical traffic cannot move to a partial stack. If no safe control exists,
  stop `BLOCKED`; speed is not authority to expose an incomplete stack.
- Submit and merge in dependency order. Wait for checks on each exact head.
- Reverify canonical identity after every merge that can move deployment, and
  again at the final main SHA before cleanup.
- Zero open PRs is a cleanup precondition, not a substitute for branch audit.

## Semantic branch audit

Before deleting a branch, classify commits as reachable, patch-equivalent, or
unique. Review unique diffs for correctness; never merge unsafe work merely to
make the branch list empty. Record the decision and archive all refs.
Evaluation or scoring branches require explicit metric direction (`minimize`
or `maximize`) plus a scenario that fails when the direction is inverted;
names such as `score` or `latency` are not sufficient semantic evidence.

## Recoverable archive

1. Fetch and prune remote heads/tags.
2. Verify every remote head has a matching cached ref.
3. Create a bundle outside the repository and intended cleanup roots:

   ```bash
   git bundle create /safe/archive/all-refs.bundle --all
   git bundle verify /safe/archive/all-refs.bundle
   git bundle list-heads /safe/archive/all-refs.bundle
   ```

4. Compare bundle heads against local and cached remote refs. Archive Graphite
   metadata separately when present. Record byte size and SHA-256.
5. Restore the bundle into a new temporary bare repository and resolve every
   target ref there. `git bundle verify` alone does not prove the operator's
   restore procedure.
6. Run the repository's secret/history scanner before storing the archive
   outside the trusted machine; keep archives access-controlled by default.
7. Do not delete anything until the archive can recreate every target ref.

## Worktree cleanup

Resolve every path to an absolute path and compare it with an explicit
inventory. Reject workspace roots, home directories, unresolved variables,
globs, and unexpected paths. Require clean status unless discarded evidence is
explicitly authorized and archived in a separately hash-manifested package;
Git bundles do not include untracked files. Use `git worktree remove <exact-path>` and
then `git worktree prune`; do not recursively delete worktree directories.

On Windows, keep discovery, validation, and removal in PowerShell and use
`-LiteralPath`. Never enumerate paths in one shell and pass them to another for
deletion.

## Branch cleanup

Delete Graphite-tracked branches through Graphite when possible. Derive the
remote deletion list after merge and archive; validate every branch name before
one atomic push. If atomic deletion fails, stop and inspect rather than falling
back to partial deletion.

Final PASS requires all of the following observations:

```text
current branch = main
working tree = clean
worktree count = 1
local branch list = [main]
remote branch list = [main]
local main SHA = cached remote main SHA = remote main SHA
open stack/PR count = 0
archive verification = PASS
```

The phrase “only main remains” is forbidden until that exact audit passes.
