# AGENTS.md / Ajan Çalışma Sözleşmesi

| <kbd>[🇬🇧 **English**](#en)</kbd> | <kbd>[🇹🇷 **Türkçe**](#tr)</kbd> |
|---|---|

---

<a id="en"></a>

<details open>
<summary><b>English</b></summary>

Agent working contract for this repository. Truth over completeness: content here
only states what is verified by the live project. Nothing is fabricated.

## Project
- Host: GitLab. Project: bayraktarozcan/AgentSynapse. Default branch: `main`.
- This is a personal, single-owner, direct-push repository. No MR/PR gate is in
  use (branch protection = Maintainers push, force-push disabled).

## CI status (active: default-branch pipeline only)
- `.gitlab-ci.yml` is ACTIVE but limited to the default branch:
  `workflow: rules: [{ if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH }]`.
  - Jobs: `skills-syntax` (py_compile + `--version`/`--list`), `skills-profile-coverage`
    (`--check --profile temel` and `--profile tam`), and `pages` (docs -> GitLab Pages).
  - CI runs on pushes to `main`. It is NOT a quality gate for MRs/PRs (none are used).
  - No test-suite exists, so there is still no real coverage badge source. Do NOT
    register or keep badges that fake a pipeline/coverage source; they would lie.
  - Only badges with a live-verified real SVG (HTTP 200, `image/svg+xml`) are kept.
- Current verified badges: `Latest Release` (https://gitlab.com/bayraktarozcan/AgentSynapse/-/badges/release.svg) and `MIT License`
  (https://img.shields.io/gitlab/license/bayraktarozcan%2FAgentSynapse.svg), both probed HTTP 200 real SVG.
  Note: the native license path https://gitlab.com/bayraktarozcan/AgentSynapse/-/badges/license.svg is NOT registered
  and currently returns 403; the registered license badge is the shields.io URL above.
- The README's static shields.io badges (skills/repos/categories/license) are static
  text badges over verified facts (566+ skills, 34 repos, 10 categories, MIT).

## Badge policy (apply when touching badges)
1. Register a badge only after probing its image URL returns HTTP 200 with
   content-type `image/svg+xml` (real SVG, not an error page).
2. Remove badges whose data source is gone (old/broken). Do not replace them
   with a static badge that lies (e.g., a fake pipeline/coverage/unknown license).
3. Verify the final badge list by live-probing every image URL before closing.

## Conventions
- Keep all added files and scripts ASCII-safe; avoid inline PowerShell fragments
  that mix quote terminators (write scripts to temp and run with
  `powershell.exe -File`); repository tooling is Windows PowerShell + GitLab `glab`.
- Commit message style: conventional commits (e.g., `docs:`), single clean commit
  per logical change, direct push to `main` on both remotes (origin + gitlab).

## License
- Repo ships `LICENSE` = MIT (https://gitlab.com/bayraktarozcan/AgentSynapse/-/blob/main/LICENSE). The license badge reflects real
  GitLab license data served by shields.io (verified HTTP 200 SVG).

</details>

<a id="tr"></a>

Bu depo için ajan çalışma sözleşmesi. Eksiksizlikten çok doğruluk: buradaki içerik
yalnızca canlı proje tarafından doğrulanmış olanı belirtir. Hiçbir şey uydurulmaz.

## Proje
- Host: GitLab. Proje: bayraktarozcan/AgentSynapse. Varsayılan dal: `main`.
- Bu kişisel, tek sahipli, doğrudan push yapılan bir depodur. MR/PR kapısı
  kullanılmaz (dal koruması = Maintainers push, force-push devre dışı).

## CI durumu (aktif: yalnızca varsayılan dal pipeline'ı)
- `.gitlab-ci.yml` AKTİF'tir ancak varsayılan dal ile sınırlıdır:
  `workflow: rules: [{ if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH }]`.
  - Görevler: `skills-syntax` (py_compile + `--version`/`--list`), `skills-profile-coverage`
    (`--check --profile temel` ve `--profile tam`) ve `pages` (docs -> GitLab Pages).
  - CI, `main` dalına yapılan push'larda çalışır. MR/PR'lar için kalite kapısı
    DEĞİLDİR (bunlar kullanılmaz).
  - Test paketi yoktur, bu yüzden hâlâ gerçek bir kapsam (coverage) rozeti kaynağı
    yoktur. Pipeline/kapsam kaynağını taklit eden rozetleri eklemeyin veya
    tutmayın; yalan söylerler.
  - Yalnızca canlı doğrulanmış gerçek SVG'ler (HTTP 200, `image/svg+xml`) tutulur.
- Mevcut doğrulanmış rozetler: `Latest Release` (https://gitlab.com/bayraktarozcan/AgentSynapse/-/badges/release.svg) ve `MIT License`
  (https://img.shields.io/gitlab/license/bayraktarozcan%2FAgentSynapse.svg) — ikisi de HTTP 200 gerçek SVG olarak test edildi.
  Not: yerel lisans yolu https://gitlab.com/bayraktarozcan/AgentSynapse/-/badges/license.svg KAYITLI DEĞİLDİR ve
  şu anda 403 döndürür; kayıtlı lisans rozeti yukarıdaki shields.io URL'sidir.
- README'deki statik shields.io rozetleri (skills/repos/categories/license), doğrulanmış
  gerçeklerin üzerindeki statik metin rozetleridir (566+ beceri, 34 depo, 10 kategori, MIT).

## Rozet politikası (rozetlere dokunurken uygula)
1. Bir rozeti yalnızca görsel URL'si HTTP 200 ve `image/svg+xml` içerik türü
   döndürdüğünde kaydet (gerçek SVG, hata sayfası değil).
2. Veri kaynağı kaybolmuş rozetleri kaldır (eski/bozuk). Onları yalan söyleyen
   statik bir rozetle değiştirmeyin (ör. sahte pipeline/coverage/bilinmeyen lisans).
3. Kapanmadan önce tüm rozet listesini her görsel URL'yi canlı test ederek doğrulayın.

## Sözleşmeler
- Eklenen tüm dosyaları ve betikleri ASCII-güvenli tutun; tırnak sonlandırıcıları
  karıştıran satır içi PowerShell parçalarından kaçının (betikleri temp'e yazıp
  `powershell.exe -File` ile çalıştırın); depo araçları Windows PowerShell +
  GitLab `glab`'dir.
- Commit mesajı stili: geleneksel commit'ler (örn. `docs:`), mantıksal değişiklik
  başına tek temiz commit, her iki remote'a (origin + gitlab) `main` dalına doğrudan push.

## Lisans
- Depo `LICENSE` = MIT içerir (https://gitlab.com/bayraktarozcan/AgentSynapse/-/blob/main/LICENSE). Lisans rozeti,
  shields.io tarafından sunulan gerçek GitLab lisans verisini yansıtır (HTTP 200 SVG doğrulandı).
