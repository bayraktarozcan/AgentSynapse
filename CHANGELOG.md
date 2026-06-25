# Changelog / Değişiklik Günlüğü

| <kbd>[🇬🇧 **English**](#en)</kbd> | <kbd>[🇹🇷 **Türkçe**](#tr)</kbd> |
|---|---|

---

<a id="en"></a>

<details open>
<summary><b>English</b></summary>

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-25

### Added

- **Functional categories (K1–K10)**: replaced the old trust-based Kademe system with 10 functional categories (Core, AI, Cloud, Frontend, Mobile, Security, Testing, Content, Community, Risk).
- **Onerilen (Recommended) profile**: new default install profile — 34 repos, ~450 skills, curated for quality and relevance.
- **Cross-platform Python script**: single `skills.py` replaces old skills.ps1/skills.sh.
- **GUI mode**: `--gui` launches tkinter installer with profile quick-select.
- **Bilingual support**: English + Turkish, auto-detected or `--lang tr`.
- **Embedded repo data**: all repo config in skills.py, no external files needed.
- **Embedded docs**: accessible via `--readme`, `--changelog`, `--conduct`, `--security`, `--support`, `--license` flags.
- `--show-config` flag to dump embedded repo registry as JSON.

### Changed

- Default profile changed from `guvenli` (trusted) to `onerilen` (recommended).
- `sickn33/antigravity-awesome-skills` removed due to quality/trust concerns.
- CLI parameter names updated to English/category-based names (Turkish aliases retained).

### Fixed

- Missing target-path safety check (skill name could escape `$SKILLS_DIR`).
- `git clone` timeout and FileNotFoundError handling.
- GUI set_profile() wrong default for categories without explicit `recommended` field.
- list_repos() excluding categories with absent `recommended` key.

### Removed

- skills.ps1, skills.sh, docs/, CONTRIBUTING.md, karar.md, CATEGORIES.md — replaced by skills.py.
- repos.json, repos.example.json — data embedded in skills.py.
- External .md files — content embedded as bilingual constants in skills.py.

## [0.1.0] - 2026-06-24

### Added

- Initial project scaffolding.
- `skills.ps1` — PowerShell installer with Kademe-based trust classification (K1–K6).
- `karar.md` — classification document.
- `guvenli` (trusted), `tum` (all), and individual category installs.
- Git repository initialization.

</details>

<a id="tr"></a>

Projedeki tüm kayda değer değişiklikler bu dosyada belgelenmiştir.

## [1.0.0] - 2026-06-25

### Eklenenler

- **İşlevsel kategoriler (K1–K10)**: eski Kademe sistemi yerine 10 işlevsel kategori.
- **Önerilen profili**: varsayılan kurulum profili — 34 depo, ~450 beceri.
- **Çapraz platform Python betiği**: tek `skills.py`, eski skills.ps1/skills.sh yerine.
- **GUI modu**: `--gui` ile tkinter yükleyici, profil hızlı seçimi.
- **İki dilli destek**: İngilizce + Türkçe, otomatik algılama veya `--lang tr`.
- **Gömülü depo verisi**: tüm depo yapılandırması skills.py içinde, harici dosya gerekmez.
- **Gömülü dokümanlar**: `--readme`, `--changelog`, `--conduct`, `--security`, `--support`, `--license` ile erişilebilir.
- `--show-config` bayrağı ile gömülü depo kaydını JSON olarak dökme.

### Değişenler

- Varsayılan profil `güvenli`'den `önerilen`'e değiştirildi.
- `sickn33/antigravity-awesome-skills` kalite endişeleri nedeniyle kaldırıldı.
- CLI parametre adları İngilizce/kategori tabanlı olarak güncellendi (Türkçe takma adlar korundu).

### Düzenlenenler

- Eksik hedef yol güvenlik kontrolü (beceri adı SKILLS_DIR dışına çıkabiliyordu).
- `git clone` zaman aşımı ve FileNotFoundError yönetimi.
- GUI set_profile()'da açık recommended alanı olmayan kategoriler için yanlış varsayılan.
- list_repos()'un recommended anahtarı olmayan kategorileri dışlaması.

### Kaldırılanlar

- skills.ps1, skills.sh, docs/, CONTRIBUTING.md, karar.md, CATEGORIES.md — skills.py ile değiştirildi.
- repos.json, repos.example.json — veriler skills.py içine gömüldü.
- Tüm harici .md dosyaları — içerik skills.py içinde iki dilli sabitler olarak gömüldü.

## [0.1.0] - 2026-06-24

### Eklenenler

- İlk proje iskeleti.
- skills.ps1 — PowerShell yükleyici, Kademe tabanlı sınıflandırma (K1–K6).
- karar.md — sınıflandırma belgesi.
- Git deposu başlatma.
