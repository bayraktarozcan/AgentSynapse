# AgentSynapse

| <kbd>[ÄŸÅ¸â€¡Â¬ÄŸÅ¸â€¡Â§ **English**](#en)</kbd> | <kbd>[ÄŸÅ¸â€¡Â¹ÄŸÅ¸â€¡Â· **TÃƒÂ¼rkÃƒÂ§e**](#tr)</kbd> |
|---|---|

---

<a id="en"></a>

<details open>
<summary><b>English</b></summary>

**566+ curated AI agent skills** from 34 top-tier repositories, organized into 10 functional categories, installable in one command. Built for [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [OpenCode](https://opencode.ai), and any agent framework that reads SKILL.md.

[![Skills](https://img.shields.io/badge/skills-566%2B-blue?style=flat-square&color=58a6ff)](https://github.com/bayraktarozcan/AgentSynapse)
[![Repos](https://img.shields.io/badge/repos-34-success?style=flat-square&color=3fb950)](https://github.com/bayraktarozcan/AgentSynapse)
[![Categories](https://img.shields.io/badge/categories-10-purple?style=flat-square&color=bc8cff)](#category-reference)
[![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](LICENSE)

---

## Quickstart

```bash
git clone https://github.com/bayraktarozcan/AgentSynapse.git
cd AgentSynapse

# Recommended -- 566+ curated skills (default)
python skills.py

# Or if Python 3 is installed as python3:
python3 skills.py

# Full trusted suite (K1-K8)
python skills.py trusted

# Everything (including opt-in categories)
python skills.py all

# Just AI skills
python skills.py K2

# Launch graphical interface
python skills.py --gui
```

Skills land in `~/.agents/skills/<name>/SKILL.md` -- auto-discovered by Claude Code and OpenCode.

---

## Requirements

- **Python 3.8+** (stdlib only -- no pip install needed)
- **Git** (for cloning repositories)
- **tkinter** (optional, for `--gui` mode)

---

## Features

- **One-command install** -- clone 34 repos, extract skills, deduplicate, done.
- **10 functional categories** -- Core, AI & LLM, Cloud & Backend, Frontend & UI, Mobile, Security, Testing, Content, Community, Risk.
- **Bilingual** -- English and Turkish interfaces. Auto-detects or `--lang tr`.
- **Cross-platform** -- Windows, macOS, Linux. Single Python file, no dependencies.
- **Trust by default** -- Recommended profile ships verified repos; Community & Risk are opt-in.
- **Automatic dedup** -- when two repos ship the same skill, the higher-category copy wins.
- **Agent-native format** -- all skills are standard SKILL.md. No conversion needed.
- **Full audit trail** -- timestamped logs, tree output per run.
- **Graphical interface** -- `--gui` launches a tkinter installer with profile quick-select.

---

## Usage

### Profiles

| Command | Scope | Repos | Skills (approx) |
|---------|-------|-------|-----------------|
| `python skills.py` | Recommended | 34 | ~566 |
| `python skills.py trusted` | Trusted (K1-K8) | 39 | ~640 |
| `python skills.py all` | All (K1-K10) | 48 | ~995 |

### Specialization

`skill-specialization.json` maps every skill to a specialization class (C1Ã¢â‚¬â€œC5). The `--profile` flag scopes what stays installed:

| Profile | Classes | Skills |
|---------|---------|--------|
| `temel` | C1, C2 | 222 |
| `dengeli` | C1, C2, C3, first 76 of C4 | 355 |
| `tam` (default) | All C1Ã¢â‚¬â€œC5 | 566 |

After an install with `--profile temel` or `--profile dengeli`, out-of-profile skills are moved to `~/.agents/_quarantine_<profile>_<date>/` (a `_moved-list.txt` is written). Preview with `--dry-run`, inspect via `--list` / `--check`:

```bash
python skills.py --dry-run --profile temel    # preview what would move
python skills.py --check --profile dengeli    # coverage report
python skills.py --list --profile temel       # profile map
```

### Categories

```bash
python skills.py K1          # Core -- languages, tooling
python skills.py K2          # AI & LLM -- agents, RAG, prompting
python skills.py K3          # Cloud & Backend
python skills.py K4          # Frontend & UI
python skills.py K5          # Mobile
python skills.py K6          # Security
python skills.py K7          # Testing
python skills.py K8          # Content
python skills.py K9          # Community (opt-in)
python skills.py K10         # Risk (opt-in)
```

Multiple categories at once:

```bash
python skills.py K2 K4 K6    # AI + Frontend + Security
```

### Options

| Flag | Description |
|------|-------------|
| `--gui` | Launch graphical interface |
| `--lang tr` | Force Turkish language |
| `--lang en` | Force English |
| `--dry-run` | Preview repos without installing |
| `--prefix PATH` | Custom install directory |
| `--profile P` | Enforce specialization profile (temel, dengeli, tam; default tam) |
| `--uninstall` | Remove all installed skills |
| `--check` | Pre-flight environment check (Python, Git, network, disk) |
| `--list` | List available categories |
| `--show-config` | Dump repo registry as JSON |
| `--version` | Show version |
| `--readme` | Show full README |
| `--changelog` | Show changelog |
| `--conduct` | Show code of conduct |
| `--security` | Show security policy |
| `--support` | Show support info |
| `--license` | Show license |
| `--help` | Show help |

### Turkish CLI

```bash
python skills.py --lang tr onerilen      # Onerilen profili yukle
python skills.py --lang tr guvenli       # Guvenli kategorileri yukle
python skills.py --lang tr tumu          # Tumunu yukle
python skills.py --lang tr K2            # Sadece AI kategorisi
python skills.py --lang tr --list        # Kategorileri listele
python skills.py --lang tr --gui         # Grafik arayuzu baslat
```

---

## Category Reference

| Code | Category | Repos | Status |
|------|----------|-------|--------|
| **K1** | Core (languages, tooling, code quality) | 5 | Default |
| **K2** | AI & LLM (agents, RAG, prompting, browser agents) | 9 | Default |
| **K3** | Cloud & Backend (AWS, Vercel, Stripe, Neon, Supabase) | 11 | Default |
| **K4** | Frontend & UI (React, Next.js, Expo, shadcn, WordPress) | 8 | Default |
| **K5** | Mobile (iOS, Android, React Native, Expo) | 1 | Default |
| **K6** | Security (review, scanning, hardening) | 2 | Default |
| **K7** | Testing (E2E, unit, visual regression) | 1 | Default |
| **K8** | Content (writing, docs, editing, publishing) | 2 | Default |
| **K9** | Community (third-party, lower star counts) | 5 | Opt-in |
| **K10** | Risk (experimental, unmaintained) | 4 | Opt-in |

---

## How It Works

```
git clone --depth 1 --single-branch <repo> -> parse SKILL.md frontmatter -> deduplicate -> copy to ~/.agents/skills/<name>/
```

1. **Clone** -- each repo is shallow-cloned (single branch only) to a temp directory.
2. **Parse** -- every `SKILL.md` is read for its `name:` field and subdirectory path.
3. **Deduplicate** -- if two repos share a skill name, the higher-category (higher K number) copy wins.
4. **Install** -- skills land in `~/.agents/skills/<name>/SKILL.md`.

---

## Project Structure

```
AgentSynapse/
+-- skills.py            # The entire project -- CLI + GUI, bilingual, self-contained
+-- README.md            # This file (bilingual EN/TR)
+-- CHANGELOG.md         # Bilingual changelog
+-- CODE_OF_CONDUCT.md   # Bilingual code of conduct
+-- SECURITY.md          # Bilingual security policy
+-- SUPPORT.md           # Bilingual support info
+-- CONTRIBUTING.md      # Bilingual contributing guide
+-- LICENSE              # MIT License
+-- Legacy/              # Archived files from earlier project versions (skills.ps1, karar.md)
+-- Logs/                # Timestamped install logs (auto-generated)
+-- skills-tree_*.txt    # Timestamped directory tree per run (auto-generated)
+-- skill-specialization.json # Specialization manifest (566 skills, C1-C5)
+-- .github/             # Issue templates, funding, dependabot
```

---

## Development

```bash
# Clone repo
git clone https://github.com/bayraktarozcan/AgentSynapse.git
cd AgentSynapse

# Run regression
python skills.py recommended           # 34 repos, ~566 skills
python skills.py trusted               # 39 repos, ~640 skills
python skills.py all                   # 48 repos, ~995 skills
```

### Adding a Repository

1. Edit the `REPOS` dict in `skills.py` -- add repo entry under the appropriate category.
2. Run `python skills.py K<category>` to verify it installs.

### Adding a Language

Edit the `S` dict in `skills.py` -- add a new language key and translate all strings.

---

## Agent Compatibility

| Agent | Global Path | Native Support |
|-------|-------------|----------------|
| **Claude Code** | `~/.agents/skills/` | Full |
| **OpenCode** | `~/.agents/skills/` | Full |
| **Gemini CLI** | `~/.config/gemini/` | Researching |
| **Cursor** | `.cursor/rules/` (`.mdc`) | Different format |

---

## License

MIT -- see [LICENSE](LICENSE).

---

## Community

- [Issues](https://github.com/bayraktarozcan/AgentSynapse/issues) -- bugs, feature requests, questions.
- [Discussions](https://github.com/bayraktarozcan/AgentSynapse/discussions) -- ideas, showcase, help.

Built for the AI agent community.

</details>

<a id="tr"></a>

**566'dan fazla kÃƒÂ¼ratÃƒÂ¶rlÃƒÂ¼ AI ajan becerisi**, 34 ÃƒÂ¼st dÃƒÂ¼zey depodan alÃ„Â±nmÃ„Â±Ã…Å¸, 10 iÃ…Å¸levsel kategoriye ayrÃ„Â±lmÃ„Â±Ã…Å¸, tek komutla yÃƒÂ¼klenebilir. Claude Code, OpenCode ve SKILL.md okuyan her ajan ÃƒÂ§erÃƒÂ§evesi iÃƒÂ§in ÃƒÂ¼retilmiÃ…Å¸tir.

[![Skills](https://img.shields.io/badge/skills-566%2B-blue?style=flat-square&color=58a6ff)](https://github.com/bayraktarozcan/AgentSynapse)
[![Repos](https://img.shields.io/badge/repos-34-success?style=flat-square&color=3fb950)](https://github.com/bayraktarozcan/AgentSynapse)
[![Categories](https://img.shields.io/badge/categories-10-purple?style=flat-square&color=bc8cff)](#category-reference)
[![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](LICENSE)

---

## HÃ„Â±zlÃ„Â± BaÃ…Å¸langÃ„Â±ÃƒÂ§

```bash
git clone https://github.com/bayraktarozcan/AgentSynapse.git
cd AgentSynapse

# Ãƒâ€“nerilen -- 566+ kÃƒÂ¼ratÃƒÂ¶rlÃƒÂ¼ beceri (varsayÃ„Â±lan)
python skills.py

# Veya Python 3, python3 olarak yÃƒÂ¼klendiyse:
python3 skills.py

# Tam gÃƒÂ¼venli suite (K1-K8)
python skills.py trusted

# Her Ã…Å¸ey (opsiyonel kategoriler dahil)
python skills.py all

# Sadece AI becerileri
python skills.py K2

# Grafik arayÃƒÂ¼zÃƒÂ¼ baÃ…Å¸lat
python skills.py --gui
```

Beceriler `~/.agents/skills/<name>/SKILL.md` konumuna kurulur -- Claude Code ve OpenCode tarafÃ„Â±ndan otomatik keÃ…Å¸fedilir.

---

## Gereksinimler

- **Python 3.8+** (sadece standart kÃƒÂ¼tÃƒÂ¼phane -- pip gerekmez)
- **Git** (depolarÃ„Â± klonlamak iÃƒÂ§in)
- **tkinter** (opsiyonel, `--gui` modu iÃƒÂ§in)

---

## Ãƒâ€“zellikler

- **Tek komutla kurulum** -- 34 depoyu klonla, becerileri ÃƒÂ§Ã„Â±kar, tekrarlarÃ„Â± temizle, bitti.
- **10 iÃ…Å¸levsel kategori** -- Ãƒâ€¡ekirdek, AI & LLM, Bulut & Backend, Ãƒâ€“n yÃƒÂ¼z & UI, Mobil, GÃƒÂ¼venlik, Test, Ã„Â°ÃƒÂ§erik, Topluluk, Risk.
- **Ã„Â°ki dilli** -- Ã„Â°ngilizce ve TÃƒÂ¼rkÃƒÂ§e. Otomatik algÃ„Â±lama veya `--lang tr`.
- **Ãƒâ€¡apraz platform** -- Windows, macOS, Linux. Tek Python dosyasÃ„Â±, baÃ„Å¸Ã„Â±mlÃ„Â±lÃ„Â±k yok.
- **VarsayÃ„Â±lan olarak gÃƒÂ¼venilir** -- Ãƒâ€“nerilen profili yalnÃ„Â±zca doÃ„Å¸rulanmÃ„Â±Ã…Å¸ depolar iÃƒÂ§erir; Topluluk ve Risk opsiyoneldir.
- **Otomatik tekrar temizleme** -- iki depo aynÃ„Â± beceriye sahipse, ÃƒÂ¼st kategorideki (yÃƒÂ¼ksek K numarasÃ„Â±) kazanÃ„Â±r.
- **Ajan-yerel formatÃ„Â±** -- tÃƒÂ¼m beceriler standart SKILL.md formatÃ„Â±ndadÃ„Â±r. DÃƒÂ¶nÃƒÂ¼Ã…Å¸ÃƒÂ¼m gerekmez.
- **Tam denetim izi** -- zaman damgalÃ„Â± gÃƒÂ¼nlÃƒÂ¼kler, ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±rma baÃ…Å¸Ã„Â±na klasÃƒÂ¶r aÃ„Å¸acÃ„Â±.
- **Grafik arayÃƒÂ¼z** -- `--gui` ile tkinter yÃƒÂ¼kleyici, profil hÃ„Â±zlÃ„Â± seÃƒÂ§imi.

---

## KullanÃ„Â±m

### Profiller

| Komut | Kapsam | Depo | Beceri (yaklaÃ…Å¸Ã„Â±k) |
|-------|--------|------|--------------------|
| `python skills.py` | Ãƒâ€“nerilen | 34 | ~566 |
| `python skills.py trusted` | GÃƒÂ¼venli (K1-K8) | 39 | ~640 |
| `python skills.py all` | TÃƒÂ¼mÃƒÂ¼ (K1-K10) | 48 | ~995 |

### UzmanlaÃ…Å¸ma

`skill-specialization.json`, her beceriyi bir uzmanlaÃ…Å¸ma sÃ„Â±nÃ„Â±fÃ„Â±na (C1Ã¢â‚¬â€œC5) eÃ…Å¸ler. `--profile` bayraÃ„Å¸Ã„Â± neyin kurulu kalacaÃ„Å¸Ã„Â±nÃ„Â± kapsamlar:

| Profil | SÃ„Â±nÃ„Â±flar | Beceri |
|--------|----------|--------|
| `temel` | C1, C2 | 222 |
| `dengeli` | C1, C2, C3, C4'ÃƒÂ¼n ilk 76'sÃ„Â± | 355 |
| `tam` (varsayÃ„Â±lan) | TÃƒÂ¼m C1Ã¢â‚¬â€œC5 | 566 |

`--profile temel` veya `--profile dengeli` ile yapÃ„Â±lan bir kurulumun ardÃ„Â±ndan profil dÃ„Â±Ã…Å¸Ã„Â± beceriler `~/.agents/_quarantine_<profil>_<tarih>/` klasÃƒÂ¶rÃƒÂ¼ne taÃ…Å¸Ã„Â±nÃ„Â±r (`_moved-list.txt` yazÃ„Â±lÃ„Â±r). `--dry-run` ile ÃƒÂ¶nizleyin, `--list` / `--check` ile inceleyin:

```bash
python skills.py --dry-run --profile temel    # neyin taÃ…Å¸Ã„Â±nacaÃ„Å¸Ã„Â±nÃ„Â± ÃƒÂ¶nizle
python skills.py --check --profile dengeli    # kapsam raporu
python skills.py --list --profile temel       # profil haritasÃ„Â±
```

### Kategoriler

```bash
python skills.py K1          # Ãƒâ€¡ekirdek -- diller, araÃƒÂ§lar
python skills.py K2          # AI & LLM -- ajanlar, RAG, yÃƒÂ¶nlendirme
python skills.py K3          # Bulut & Backend
python skills.py K4          # Ãƒâ€“n yÃƒÂ¼z & UI
python skills.py K5          # Mobil
python skills.py K6          # GÃƒÂ¼venlik
python skills.py K7          # Test
python skills.py K8          # Ã„Â°ÃƒÂ§erik
python skills.py K9          # Topluluk (opsiyonel)
python skills.py K10         # Risk (opsiyonel)
```

### SeÃƒÂ§enekler

| Bayrak | AÃƒÂ§Ã„Â±klama |
|--------|----------|
| `--gui` | Grafik arayÃƒÂ¼zÃƒÂ¼ baÃ…Å¸lat |
| `--lang tr` | TÃƒÂ¼rkÃƒÂ§e'yi zorla |
| `--lang en` | Ã„Â°ngilizce'yi zorla |
| `--dry-run` | RepolarÃ„Â± kurmadan ÃƒÂ¶nizle |
| `--prefix PATH` | Ãƒâ€“zel kurulum dizini |
| `--profile P` | UzmanlaÃ…Å¸ma profilini uygula (temel, dengeli, tam; varsayÃ„Â±lan tam) |
| `--uninstall` | TÃƒÂ¼m becerileri kaldÃ„Â±r |
| `--check` | Ãƒâ€“n uÃƒÂ§uÃ…Å¸ ortam kontrolÃƒÂ¼ (Python, Git, aÃ„Å¸, disk) |
| `--list` | Kategorileri listele |
| `--show-config` | Repo kaydÃ„Â±nÃ„Â± JSON olarak gÃƒÂ¶ster |
| `--version` | SÃƒÂ¼rÃƒÂ¼mÃƒÂ¼ gÃƒÂ¶ster |
| `--readme` | Tam README'yi gÃƒÂ¶ster |
| `--changelog` | DeÃ„Å¸iÃ…Å¸iklik gÃƒÂ¼nlÃƒÂ¼Ã„Å¸ÃƒÂ¼nÃƒÂ¼ gÃƒÂ¶ster |
| `--conduct` | DavranÃ„Â±Ã…Å¸ kurallarÃ„Â±nÃ„Â± gÃƒÂ¶ster |
| `--security` | GÃƒÂ¼venlik politikasÃ„Â±nÃ„Â± gÃƒÂ¶ster |
| `--support` | Destek bilgilerini gÃƒÂ¶ster |
| `--license` | LisansÃ„Â± gÃƒÂ¶ster |
| `--help` | YardÃ„Â±m mesajÃ„Â±nÃ„Â± gÃƒÂ¶ster |

### TÃƒÂ¼rkÃƒÂ§e CLI

```bash
python skills.py --lang tr onerilen      # Ãƒâ€“nerilen profili yÃƒÂ¼kle
python skills.py --lang tr guvenli       # GÃƒÂ¼venli kategorileri yÃƒÂ¼kle
python skills.py --lang tr tumu          # TÃƒÂ¼mÃƒÂ¼nÃƒÂ¼ yÃƒÂ¼kle
python skills.py --lang tr K2            # Sadece AI kategorisi
python skills.py --lang tr --list        # Kategorileri listele
python skills.py --lang tr --gui         # Grafik arayÃƒÂ¼zÃƒÂ¼ baÃ…Å¸lat
```

---

## Kategori ReferansÃ„Â±

| Kod | Kategori | Depo | Durum |
|-----|----------|------|-------|
| **K1** | Ãƒâ€¡ekirdek (diller, araÃƒÂ§lar, kod kalitesi) | 5 | VarsayÃ„Â±lan |
| **K2** | AI & LLM (ajanlar, RAG, yÃƒÂ¶nlendirme, tarayÃ„Â±cÃ„Â± ajanlarÃ„Â±) | 9 | VarsayÃ„Â±lan |
| **K3** | Bulut & Backend (AWS, Vercel, Stripe, Neon, Supabase) | 11 | VarsayÃ„Â±lan |
| **K4** | Ãƒâ€“n yÃƒÂ¼z & UI (React, Next.js, Expo, shadcn, WordPress) | 8 | VarsayÃ„Â±lan |
| **K5** | Mobil (iOS, Android, React Native, Expo) | 1 | VarsayÃ„Â±lan |
| **K6** | GÃƒÂ¼venlik (inceleme, tarama, saÃ„Å¸lamlaÃ…Å¸tÃ„Â±rma) | 2 | VarsayÃ„Â±lan |
| **K7** | Test (E2E, birim, gÃƒÂ¶rsel regresyon) | 1 | VarsayÃ„Â±lan |
| **K8** | Ã„Â°ÃƒÂ§erik (yazma, dokÃƒÂ¼mantasyon, dÃƒÂ¼zenleme, yayÃ„Â±ncÃ„Â±lÃ„Â±k) | 2 | VarsayÃ„Â±lan |
| **K9** | Topluluk (ÃƒÂ¼ÃƒÂ§ÃƒÂ¼ncÃƒÂ¼ taraf, dÃƒÂ¼Ã…Å¸ÃƒÂ¼k yÃ„Â±ldÃ„Â±z sayÃ„Â±sÃ„Â±) | 5 | Opsiyonel |
| **K10** | Risk (deneysel, bakÃ„Â±mÃ„Â± yapÃ„Â±lmayan) | 4 | Opsiyonel |

---

## NasÃ„Â±l Ãƒâ€¡alÃ„Â±Ã…Å¸Ã„Â±r

```
git clone --depth 1 --single-branch <repo> -> SKILL.md ÃƒÂ¶n yÃƒÂ¼zÃƒÂ¼nÃƒÂ¼ ayrÃ„Â±Ã…Å¸tÃ„Â±r -> tekrarlarÃ„Â± temizle -> ~/.agents/skills/<name>/ konumuna kopyala
```

1. **Klonla** -- her depo geÃƒÂ§ici dizine --depth 1 --single-branch ile klonlanÃ„Â±r (yalnÃ„Â±zca tek dal).
2. **AyrÃ„Â±Ã…Å¸tÃ„Â±r** -- her SKILL.md dosyasÃ„Â±nÃ„Â±n `name:` alanÃ„Â± ve alt dizin yolu okunur.
3. **TekrarlarÃ„Â± temizle** -- iki depo aynÃ„Â± beceri adÃ„Â±na sahipse, ÃƒÂ¼st kategorideki (yÃƒÂ¼ksek K) kazanÃ„Â±r.
4. **Kur** -- beceriler `~/.agents/skills/<name>/SKILL.md` konumuna kopyalanÃ„Â±r.

---

## Proje YapÃ„Â±sÃ„Â±

```
AgentSynapse/
+-- skills.py            # TÃƒÂ¼m proje -- CLI + GUI, iki dilli, kendi kendine yeter
+-- README.md            # Bu dosya (ÃƒÂ§ift dilli EN/TR)
+-- CHANGELOG.md         # Ãƒâ€¡ift dilli deÃ„Å¸iÃ…Å¸iklik gÃƒÂ¼nlÃƒÂ¼Ã„Å¸ÃƒÂ¼
+-- CODE_OF_CONDUCT.md   # Ãƒâ€¡ift dilli davranÃ„Â±Ã…Å¸ kurallarÃ„Â±
+-- SECURITY.md          # Ãƒâ€¡ift dilli gÃƒÂ¼venlik politikasÃ„Â±
+-- SUPPORT.md           # Ãƒâ€¡ift dilli destek bilgileri
+-- CONTRIBUTING.md      # Ãƒâ€¡ift dilli katkÃ„Â± rehberi
+-- LICENSE              # MIT LisansÃ„Â±
+-- Legacy/              # Ãƒâ€“nceki proje sÃƒÂ¼rÃƒÂ¼mlerinden arÃ…Å¸iv dosyalarÃ„Â± (skills.ps1, karar.md)
+-- Logs/                # Zaman damgalÃ„Â± kurulum gÃƒÂ¼nlÃƒÂ¼kleri (otomatik)
+-- skills-tree_*.txt    # Ãƒâ€¡alÃ„Â±Ã…Å¸tÃ„Â±rma baÃ…Å¸Ã„Â±na zaman damgalÃ„Â± klasÃƒÂ¶r aÃ„Å¸acÃ„Â± (otomatik)
+-- skill-specialization.json # UzmanlaÃ…Å¸ma manifesti (566 beceri, C1-C5)
+-- .github/             # Issue Ã…Å¸ablonlarÃ„Â±, finansman, dependabot
```

---

## GeliÃ…Å¸tirme

```bash
# Depoyu klonla
git clone https://github.com/bayraktarozcan/AgentSynapse.git
cd AgentSynapse

# Regresyon testi
python skills.py recommended           # 34 depo, ~566 beceri
python skills.py trusted               # 39 depo, ~640 beceri
python skills.py all                   # 48 depo, ~995 beceri
```

### Depo Ekleme

1. `skills.py` iÃƒÂ§indeki `REPOS` sÃƒÂ¶zlÃƒÂ¼Ã„Å¸ÃƒÂ¼nÃƒÂ¼ dÃƒÂ¼zenleyin -- uygun kategori altÃ„Â±na depo giriÃ…Å¸i ekleyin.
2. `python skills.py K<kategori>` ile kurulumu doÃ„Å¸rulayÃ„Â±n.

### Dil Ekleme

`skills.py` iÃƒÂ§indeki `S` sÃƒÂ¶zlÃƒÂ¼Ã„Å¸ÃƒÂ¼nÃƒÂ¼ dÃƒÂ¼zenleyin -- yeni bir dil anahtarÃ„Â± ekleyin ve tÃƒÂ¼m dizeleri ÃƒÂ§evirin.

---

## Ajan UyumluluÃ„Å¸u

| Ajan | Genel Yol | Yerel Destek |
|------|-----------|--------------|
| **Claude Code** | `~/.agents/skills/` | Tam |
| **OpenCode** | `~/.agents/skills/` | Tam |
| **Gemini CLI** | `~/.config/gemini/` | AraÃ…Å¸tÃ„Â±rÃ„Â±lÃ„Â±yor |
| **Cursor** | `.cursor/rules/` (`.mdc`) | FarklÃ„Â± format |

---

## Lisans

MIT -- detaylar iÃƒÂ§in [LICENSE](LICENSE) dosyasÃ„Â±na bakÃ„Â±n.

---

## Topluluk

- [Sorunlar](https://github.com/bayraktarozcan/AgentSynapse/issues) -- hatalar, ÃƒÂ¶zellik talepleri, sorular.
- [TartÃ„Â±Ã…Å¸malar](https://github.com/bayraktarozcan/AgentSynapse/discussions) -- fikirler, vitrin, yardÃ„Â±m.

AI ajan topluluÃ„Å¸u iÃƒÂ§in ÃƒÂ¼retilmiÃ…Å¸tir.
