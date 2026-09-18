# AGENTS.md

Agent working contract for this repository. Truth over completeness: content here
only states what is verified by the live project. Nothing is fabricated.

## Project
- Host: GitLab. Project: bayraktarozcan/AgentSynapse. Default branch: `main`.
- This is a personal, single-owner, direct-push repository. No MR/PR gate is in
  use (branch protection = Maintainers push, force-push disabled).

## CI status (important ??? do not expect pipelines)
- `.gitlab-ci.yml` is intentionally inert: top-level `workflow: rules: [{ when: never }]`.
  CI never runs, therefore:
  - There is NO live pipeline or coverage data. Do NOT register or keep badges
    whose image source depends on pipelines/coverage; they would render broken.
  - Only badges with a live-verified real SVG (HTTP 200, `image/svg+xml`) are kept.
- Current verified badges: `Latest Release` (https://gitlab.com/bayraktarozcan/AgentSynapse/-/badges/release.svg) and `MIT License`
  (https://gitlab.com/bayraktarozcan/AgentSynapse/-/badges/license.svg), both probed HTTP 200 real SVG.

## Badge policy (apply when touching badges)
1. Register a badge only after probing its image URL returns HTTP 200 with
   content-type `image/svg+xml` (real SVG, not an error page).
2. Remove badges whose data source is gone (old/broken). Do not replace them
   with a static badge that lies (e.g., a fake pipeline/coverage/unknown license).
3. Verify the final badge list by live-probing every image URL before closing.

## Conventions
- Keep all added files and scripts ASCII-safe; avoid inline PowerShell fragments
  that mix quote terminators (write scripts to temp and run with
  `powershell.exe -File`) ??? this repository's tooling is Windows PowerShell +
  GitLab `glab`.
- Commit message style: conventional commits (e.g., `docs:`), single clean commit
  per logical change, direct push to `main` on both remotes (origin + gitlab).

## License
- Repo ships `LICENSE` = MIT (https://gitlab.com/bayraktarozcan/AgentSynapse/-/blob/main/LICENSE). The license badge reflects real
  GitLab license data served by shields.io (verified HTTP 200 SVG).
