# AgentSynapse

| <kbd>[Ã„Å¸Ã…Â¸Ã¢â‚¬Â¡Ã‚Â¬Ã„Å¸Ã…Â¸Ã¢â‚¬Â¡Ã‚Â§ **English**](#en)</kbd> | <kbd>[Ã„Å¸Ã…Â¸Ã¢â‚¬Â¡Ã‚Â¹Ã„Å¸Ã…Â¸Ã¢â‚¬Â¡Ã‚Â· **TÃƒÆ’Ã‚Â¼rkÃƒÆ’Ã‚Â§e**](#tr)</kbd> |
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

`skill-specialization.json` maps every skill to a specialization class (C1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“C5). The `--profile` flag scopes what stays installed:

| Profile | Classes | Skills |
|---------|---------|--------|
| `temel` | C1, C2 | 222 |
| `dengeli` | C1, C2, C3, first 76 of C4 | 355 |
| `tam` (default) | All C1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“C5 | 566 |

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

**566'dan fazla kÃƒÆ’Ã‚Â¼ratÃƒÆ’Ã‚Â¶rlÃƒÆ’Ã‚Â¼ AI ajan becerisi**, 34 ÃƒÆ’Ã‚Â¼st dÃƒÆ’Ã‚Â¼zey depodan alÃƒâ€Ã‚Â±nmÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸, 10 iÃƒâ€¦Ã…Â¸levsel kategoriye ayrÃƒâ€Ã‚Â±lmÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸, tek komutla yÃƒÆ’Ã‚Â¼klenebilir. Claude Code, OpenCode ve SKILL.md okuyan her ajan ÃƒÆ’Ã‚Â§erÃƒÆ’Ã‚Â§evesi iÃƒÆ’Ã‚Â§in ÃƒÆ’Ã‚Â¼retilmiÃƒâ€¦Ã…Â¸tir.

[![Skills](https://img.shields.io/badge/skills-566%2B-blue?style=flat-square&color=58a6ff)](https://github.com/bayraktarozcan/AgentSynapse)
[![Repos](https://img.shields.io/badge/repos-34-success?style=flat-square&color=3fb950)](https://github.com/bayraktarozcan/AgentSynapse)
[![Categories](https://img.shields.io/badge/categories-10-purple?style=flat-square&color=bc8cff)](#category-reference)
[![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](LICENSE)

---

## HÃƒâ€Ã‚Â±zlÃƒâ€Ã‚Â± BaÃƒâ€¦Ã…Â¸langÃƒâ€Ã‚Â±ÃƒÆ’Ã‚Â§

```bash
git clone https://github.com/bayraktarozcan/AgentSynapse.git
cd AgentSynapse

# ÃƒÆ’Ã¢â‚¬â€œnerilen -- 566+ kÃƒÆ’Ã‚Â¼ratÃƒÆ’Ã‚Â¶rlÃƒÆ’Ã‚Â¼ beceri (varsayÃƒâ€Ã‚Â±lan)
python skills.py

# Veya Python 3, python3 olarak yÃƒÆ’Ã‚Â¼klendiyse:
python3 skills.py

# Tam gÃƒÆ’Ã‚Â¼venli suite (K1-K8)
python skills.py trusted

# Her Ãƒâ€¦Ã…Â¸ey (opsiyonel kategoriler dahil)
python skills.py all

# Sadece AI becerileri
python skills.py K2

# Grafik arayÃƒÆ’Ã‚Â¼zÃƒÆ’Ã‚Â¼ baÃƒâ€¦Ã…Â¸lat
python skills.py --gui
```

Beceriler `~/.agents/skills/<name>/SKILL.md` konumuna kurulur -- Claude Code ve OpenCode tarafÃƒâ€Ã‚Â±ndan otomatik keÃƒâ€¦Ã…Â¸fedilir.

---

## Gereksinimler

- **Python 3.8+** (sadece standart kÃƒÆ’Ã‚Â¼tÃƒÆ’Ã‚Â¼phane -- pip gerekmez)
- **Git** (depolarÃƒâ€Ã‚Â± klonlamak iÃƒÆ’Ã‚Â§in)
- **tkinter** (opsiyonel, `--gui` modu iÃƒÆ’Ã‚Â§in)

---

## ÃƒÆ’Ã¢â‚¬â€œzellikler

- **Tek komutla kurulum** -- 34 depoyu klonla, becerileri ÃƒÆ’Ã‚Â§Ãƒâ€Ã‚Â±kar, tekrarlarÃƒâ€Ã‚Â± temizle, bitti.
- **10 iÃƒâ€¦Ã…Â¸levsel kategori** -- ÃƒÆ’Ã¢â‚¬Â¡ekirdek, AI & LLM, Bulut & Backend, ÃƒÆ’Ã¢â‚¬â€œn yÃƒÆ’Ã‚Â¼z & UI, Mobil, GÃƒÆ’Ã‚Â¼venlik, Test, Ãƒâ€Ã‚Â°ÃƒÆ’Ã‚Â§erik, Topluluk, Risk.
- **Ãƒâ€Ã‚Â°ki dilli** -- Ãƒâ€Ã‚Â°ngilizce ve TÃƒÆ’Ã‚Â¼rkÃƒÆ’Ã‚Â§e. Otomatik algÃƒâ€Ã‚Â±lama veya `--lang tr`.
- **ÃƒÆ’Ã¢â‚¬Â¡apraz platform** -- Windows, macOS, Linux. Tek Python dosyasÃƒâ€Ã‚Â±, baÃƒâ€Ã…Â¸Ãƒâ€Ã‚Â±mlÃƒâ€Ã‚Â±lÃƒâ€Ã‚Â±k yok.
- **VarsayÃƒâ€Ã‚Â±lan olarak gÃƒÆ’Ã‚Â¼venilir** -- ÃƒÆ’Ã¢â‚¬â€œnerilen profili yalnÃƒâ€Ã‚Â±zca doÃƒâ€Ã…Â¸rulanmÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸ depolar iÃƒÆ’Ã‚Â§erir; Topluluk ve Risk opsiyoneldir.
- **Otomatik tekrar temizleme** -- iki depo aynÃƒâ€Ã‚Â± beceriye sahipse, ÃƒÆ’Ã‚Â¼st kategorideki (yÃƒÆ’Ã‚Â¼ksek K numarasÃƒâ€Ã‚Â±) kazanÃƒâ€Ã‚Â±r.
- **Ajan-yerel formatÃƒâ€Ã‚Â±** -- tÃƒÆ’Ã‚Â¼m beceriler standart SKILL.md formatÃƒâ€Ã‚Â±ndadÃƒâ€Ã‚Â±r. DÃƒÆ’Ã‚Â¶nÃƒÆ’Ã‚Â¼Ãƒâ€¦Ã…Â¸ÃƒÆ’Ã‚Â¼m gerekmez.
- **Tam denetim izi** -- zaman damgalÃƒâ€Ã‚Â± gÃƒÆ’Ã‚Â¼nlÃƒÆ’Ã‚Â¼kler, ÃƒÆ’Ã‚Â§alÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸tÃƒâ€Ã‚Â±rma baÃƒâ€¦Ã…Â¸Ãƒâ€Ã‚Â±na klasÃƒÆ’Ã‚Â¶r aÃƒâ€Ã…Â¸acÃƒâ€Ã‚Â±.
- **Grafik arayÃƒÆ’Ã‚Â¼z** -- `--gui` ile tkinter yÃƒÆ’Ã‚Â¼kleyici, profil hÃƒâ€Ã‚Â±zlÃƒâ€Ã‚Â± seÃƒÆ’Ã‚Â§imi.

---

## KullanÃƒâ€Ã‚Â±m

### Profiller

| Komut | Kapsam | Depo | Beceri (yaklaÃƒâ€¦Ã…Â¸Ãƒâ€Ã‚Â±k) |
|-------|--------|------|--------------------|
| `python skills.py` | ÃƒÆ’Ã¢â‚¬â€œnerilen | 34 | ~566 |
| `python skills.py trusted` | GÃƒÆ’Ã‚Â¼venli (K1-K8) | 39 | ~640 |
| `python skills.py all` | TÃƒÆ’Ã‚Â¼mÃƒÆ’Ã‚Â¼ (K1-K10) | 48 | ~995 |

### UzmanlaÃƒâ€¦Ã…Â¸ma

`skill-specialization.json`, her beceriyi bir uzmanlaÃƒâ€¦Ã…Â¸ma sÃƒâ€Ã‚Â±nÃƒâ€Ã‚Â±fÃƒâ€Ã‚Â±na (C1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“C5) eÃƒâ€¦Ã…Â¸ler. `--profile` bayraÃƒâ€Ã…Â¸Ãƒâ€Ã‚Â± neyin kurulu kalacaÃƒâ€Ã…Â¸Ãƒâ€Ã‚Â±nÃƒâ€Ã‚Â± kapsamlar:

| Profil | SÃƒâ€Ã‚Â±nÃƒâ€Ã‚Â±flar | Beceri |
|--------|----------|--------|
| `temel` | C1, C2 | 222 |
| `dengeli` | C1, C2, C3, C4'ÃƒÆ’Ã‚Â¼n ilk 76'sÃƒâ€Ã‚Â± | 355 |
| `tam` (varsayÃƒâ€Ã‚Â±lan) | TÃƒÆ’Ã‚Â¼m C1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“C5 | 566 |

`--profile temel` veya `--profile dengeli` ile yapÃƒâ€Ã‚Â±lan bir kurulumun ardÃƒâ€Ã‚Â±ndan profil dÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸Ãƒâ€Ã‚Â± beceriler `~/.agents/_quarantine_<profil>_<tarih>/` klasÃƒÆ’Ã‚Â¶rÃƒÆ’Ã‚Â¼ne taÃƒâ€¦Ã…Â¸Ãƒâ€Ã‚Â±nÃƒâ€Ã‚Â±r (`_moved-list.txt` yazÃƒâ€Ã‚Â±lÃƒâ€Ã‚Â±r). `--dry-run` ile ÃƒÆ’Ã‚Â¶nizleyin, `--list` / `--check` ile inceleyin:

```bash
python skills.py --dry-run --profile temel    # neyin taÃƒâ€¦Ã…Â¸Ãƒâ€Ã‚Â±nacaÃƒâ€Ã…Â¸Ãƒâ€Ã‚Â±nÃƒâ€Ã‚Â± ÃƒÆ’Ã‚Â¶nizle
python skills.py --check --profile dengeli    # kapsam raporu
python skills.py --list --profile temel       # profil haritasÃƒâ€Ã‚Â±
```

### Kategoriler

```bash
python skills.py K1          # ÃƒÆ’Ã¢â‚¬Â¡ekirdek -- diller, araÃƒÆ’Ã‚Â§lar
python skills.py K2          # AI & LLM -- ajanlar, RAG, yÃƒÆ’Ã‚Â¶nlendirme
python skills.py K3          # Bulut & Backend
python skills.py K4          # ÃƒÆ’Ã¢â‚¬â€œn yÃƒÆ’Ã‚Â¼z & UI
python skills.py K5          # Mobil
python skills.py K6          # GÃƒÆ’Ã‚Â¼venlik
python skills.py K7          # Test
python skills.py K8          # Ãƒâ€Ã‚Â°ÃƒÆ’Ã‚Â§erik
python skills.py K9          # Topluluk (opsiyonel)
python skills.py K10         # Risk (opsiyonel)
```

### SeÃƒÆ’Ã‚Â§enekler

| Bayrak | AÃƒÆ’Ã‚Â§Ãƒâ€Ã‚Â±klama |
|--------|----------|
| `--gui` | Grafik arayÃƒÆ’Ã‚Â¼zÃƒÆ’Ã‚Â¼ baÃƒâ€¦Ã…Â¸lat |
| `--lang tr` | TÃƒÆ’Ã‚Â¼rkÃƒÆ’Ã‚Â§e'yi zorla |
| `--lang en` | Ãƒâ€Ã‚Â°ngilizce'yi zorla |
| `--dry-run` | RepolarÃƒâ€Ã‚Â± kurmadan ÃƒÆ’Ã‚Â¶nizle |
| `--prefix PATH` | ÃƒÆ’Ã¢â‚¬â€œzel kurulum dizini |
| `--profile P` | UzmanlaÃƒâ€¦Ã…Â¸ma profilini uygula (temel, dengeli, tam; varsayÃƒâ€Ã‚Â±lan tam) |
| `--uninstall` | TÃƒÆ’Ã‚Â¼m becerileri kaldÃƒâ€Ã‚Â±r |
| `--check` | ÃƒÆ’Ã¢â‚¬â€œn uÃƒÆ’Ã‚Â§uÃƒâ€¦Ã…Â¸ ortam kontrolÃƒÆ’Ã‚Â¼ (Python, Git, aÃƒâ€Ã…Â¸, disk) |
| `--list` | Kategorileri listele |
| `--show-config` | Repo kaydÃƒâ€Ã‚Â±nÃƒâ€Ã‚Â± JSON olarak gÃƒÆ’Ã‚Â¶ster |
| `--version` | SÃƒÆ’Ã‚Â¼rÃƒÆ’Ã‚Â¼mÃƒÆ’Ã‚Â¼ gÃƒÆ’Ã‚Â¶ster |
| `--readme` | Tam README'yi gÃƒÆ’Ã‚Â¶ster |
| `--changelog` | DeÃƒâ€Ã…Â¸iÃƒâ€¦Ã…Â¸iklik gÃƒÆ’Ã‚Â¼nlÃƒÆ’Ã‚Â¼Ãƒâ€Ã…Â¸ÃƒÆ’Ã‚Â¼nÃƒÆ’Ã‚Â¼ gÃƒÆ’Ã‚Â¶ster |
| `--conduct` | DavranÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸ kurallarÃƒâ€Ã‚Â±nÃƒâ€Ã‚Â± gÃƒÆ’Ã‚Â¶ster |
| `--security` | GÃƒÆ’Ã‚Â¼venlik politikasÃƒâ€Ã‚Â±nÃƒâ€Ã‚Â± gÃƒÆ’Ã‚Â¶ster |
| `--support` | Destek bilgilerini gÃƒÆ’Ã‚Â¶ster |
| `--license` | LisansÃƒâ€Ã‚Â± gÃƒÆ’Ã‚Â¶ster |
| `--help` | YardÃƒâ€Ã‚Â±m mesajÃƒâ€Ã‚Â±nÃƒâ€Ã‚Â± gÃƒÆ’Ã‚Â¶ster |

### TÃƒÆ’Ã‚Â¼rkÃƒÆ’Ã‚Â§e CLI

```bash
python skills.py --lang tr onerilen      # ÃƒÆ’Ã¢â‚¬â€œnerilen profili yÃƒÆ’Ã‚Â¼kle
python skills.py --lang tr guvenli       # GÃƒÆ’Ã‚Â¼venli kategorileri yÃƒÆ’Ã‚Â¼kle
python skills.py --lang tr tumu          # TÃƒÆ’Ã‚Â¼mÃƒÆ’Ã‚Â¼nÃƒÆ’Ã‚Â¼ yÃƒÆ’Ã‚Â¼kle
python skills.py --lang tr K2            # Sadece AI kategorisi
python skills.py --lang tr --list        # Kategorileri listele
python skills.py --lang tr --gui         # Grafik arayÃƒÆ’Ã‚Â¼zÃƒÆ’Ã‚Â¼ baÃƒâ€¦Ã…Â¸lat
```

---

## Kategori ReferansÃƒâ€Ã‚Â±

| Kod | Kategori | Depo | Durum |
|-----|----------|------|-------|
| **K1** | ÃƒÆ’Ã¢â‚¬Â¡ekirdek (diller, araÃƒÆ’Ã‚Â§lar, kod kalitesi) | 5 | VarsayÃƒâ€Ã‚Â±lan |
| **K2** | AI & LLM (ajanlar, RAG, yÃƒÆ’Ã‚Â¶nlendirme, tarayÃƒâ€Ã‚Â±cÃƒâ€Ã‚Â± ajanlarÃƒâ€Ã‚Â±) | 9 | VarsayÃƒâ€Ã‚Â±lan |
| **K3** | Bulut & Backend (AWS, Vercel, Stripe, Neon, Supabase) | 11 | VarsayÃƒâ€Ã‚Â±lan |
| **K4** | ÃƒÆ’Ã¢â‚¬â€œn yÃƒÆ’Ã‚Â¼z & UI (React, Next.js, Expo, shadcn, WordPress) | 8 | VarsayÃƒâ€Ã‚Â±lan |
| **K5** | Mobil (iOS, Android, React Native, Expo) | 1 | VarsayÃƒâ€Ã‚Â±lan |
| **K6** | GÃƒÆ’Ã‚Â¼venlik (inceleme, tarama, saÃƒâ€Ã…Â¸lamlaÃƒâ€¦Ã…Â¸tÃƒâ€Ã‚Â±rma) | 2 | VarsayÃƒâ€Ã‚Â±lan |
| **K7** | Test (E2E, birim, gÃƒÆ’Ã‚Â¶rsel regresyon) | 1 | VarsayÃƒâ€Ã‚Â±lan |
| **K8** | Ãƒâ€Ã‚Â°ÃƒÆ’Ã‚Â§erik (yazma, dokÃƒÆ’Ã‚Â¼mantasyon, dÃƒÆ’Ã‚Â¼zenleme, yayÃƒâ€Ã‚Â±ncÃƒâ€Ã‚Â±lÃƒâ€Ã‚Â±k) | 2 | VarsayÃƒâ€Ã‚Â±lan |
| **K9** | Topluluk (ÃƒÆ’Ã‚Â¼ÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â¼ncÃƒÆ’Ã‚Â¼ taraf, dÃƒÆ’Ã‚Â¼Ãƒâ€¦Ã…Â¸ÃƒÆ’Ã‚Â¼k yÃƒâ€Ã‚Â±ldÃƒâ€Ã‚Â±z sayÃƒâ€Ã‚Â±sÃƒâ€Ã‚Â±) | 5 | Opsiyonel |
| **K10** | Risk (deneysel, bakÃƒâ€Ã‚Â±mÃƒâ€Ã‚Â± yapÃƒâ€Ã‚Â±lmayan) | 4 | Opsiyonel |

---

## NasÃƒâ€Ã‚Â±l ÃƒÆ’Ã¢â‚¬Â¡alÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸Ãƒâ€Ã‚Â±r

```
git clone --depth 1 --single-branch <repo> -> SKILL.md ÃƒÆ’Ã‚Â¶n yÃƒÆ’Ã‚Â¼zÃƒÆ’Ã‚Â¼nÃƒÆ’Ã‚Â¼ ayrÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸tÃƒâ€Ã‚Â±r -> tekrarlarÃƒâ€Ã‚Â± temizle -> ~/.agents/skills/<name>/ konumuna kopyala
```

1. **Klonla** -- her depo geÃƒÆ’Ã‚Â§ici dizine --depth 1 --single-branch ile klonlanÃƒâ€Ã‚Â±r (yalnÃƒâ€Ã‚Â±zca tek dal).
2. **AyrÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸tÃƒâ€Ã‚Â±r** -- her SKILL.md dosyasÃƒâ€Ã‚Â±nÃƒâ€Ã‚Â±n `name:` alanÃƒâ€Ã‚Â± ve alt dizin yolu okunur.
3. **TekrarlarÃƒâ€Ã‚Â± temizle** -- iki depo aynÃƒâ€Ã‚Â± beceri adÃƒâ€Ã‚Â±na sahipse, ÃƒÆ’Ã‚Â¼st kategorideki (yÃƒÆ’Ã‚Â¼ksek K) kazanÃƒâ€Ã‚Â±r.
4. **Kur** -- beceriler `~/.agents/skills/<name>/SKILL.md` konumuna kopyalanÃƒâ€Ã‚Â±r.

---

## Proje YapÃƒâ€Ã‚Â±sÃƒâ€Ã‚Â±

```
AgentSynapse/
+-- skills.py            # TÃƒÆ’Ã‚Â¼m proje -- CLI + GUI, iki dilli, kendi kendine yeter
+-- README.md            # Bu dosya (ÃƒÆ’Ã‚Â§ift dilli EN/TR)
+-- CHANGELOG.md         # ÃƒÆ’Ã¢â‚¬Â¡ift dilli deÃƒâ€Ã…Â¸iÃƒâ€¦Ã…Â¸iklik gÃƒÆ’Ã‚Â¼nlÃƒÆ’Ã‚Â¼Ãƒâ€Ã…Â¸ÃƒÆ’Ã‚Â¼
+-- CODE_OF_CONDUCT.md   # ÃƒÆ’Ã¢â‚¬Â¡ift dilli davranÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸ kurallarÃƒâ€Ã‚Â±
+-- SECURITY.md          # ÃƒÆ’Ã¢â‚¬Â¡ift dilli gÃƒÆ’Ã‚Â¼venlik politikasÃƒâ€Ã‚Â±
+-- SUPPORT.md           # ÃƒÆ’Ã¢â‚¬Â¡ift dilli destek bilgileri
+-- CONTRIBUTING.md      # ÃƒÆ’Ã¢â‚¬Â¡ift dilli katkÃƒâ€Ã‚Â± rehberi
+-- LICENSE              # MIT LisansÃƒâ€Ã‚Â±
+-- Legacy/              # ÃƒÆ’Ã¢â‚¬â€œnceki proje sÃƒÆ’Ã‚Â¼rÃƒÆ’Ã‚Â¼mlerinden arÃƒâ€¦Ã…Â¸iv dosyalarÃƒâ€Ã‚Â± (skills.ps1, karar.md)
+-- Logs/                # Zaman damgalÃƒâ€Ã‚Â± kurulum gÃƒÆ’Ã‚Â¼nlÃƒÆ’Ã‚Â¼kleri (otomatik)
+-- skills-tree_*.txt    # ÃƒÆ’Ã¢â‚¬Â¡alÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸tÃƒâ€Ã‚Â±rma baÃƒâ€¦Ã…Â¸Ãƒâ€Ã‚Â±na zaman damgalÃƒâ€Ã‚Â± klasÃƒÆ’Ã‚Â¶r aÃƒâ€Ã…Â¸acÃƒâ€Ã‚Â± (otomatik)
+-- skill-specialization.json # UzmanlaÃƒâ€¦Ã…Â¸ma manifesti (566 beceri, C1-C5)
+-- .github/             # Issue Ãƒâ€¦Ã…Â¸ablonlarÃƒâ€Ã‚Â±, finansman, dependabot
```

---

## GeliÃƒâ€¦Ã…Â¸tirme

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

1. `skills.py` iÃƒÆ’Ã‚Â§indeki `REPOS` sÃƒÆ’Ã‚Â¶zlÃƒÆ’Ã‚Â¼Ãƒâ€Ã…Â¸ÃƒÆ’Ã‚Â¼nÃƒÆ’Ã‚Â¼ dÃƒÆ’Ã‚Â¼zenleyin -- uygun kategori altÃƒâ€Ã‚Â±na depo giriÃƒâ€¦Ã…Â¸i ekleyin.
2. `python skills.py K<kategori>` ile kurulumu doÃƒâ€Ã…Â¸rulayÃƒâ€Ã‚Â±n.

### Dil Ekleme

`skills.py` iÃƒÆ’Ã‚Â§indeki `S` sÃƒÆ’Ã‚Â¶zlÃƒÆ’Ã‚Â¼Ãƒâ€Ã…Â¸ÃƒÆ’Ã‚Â¼nÃƒÆ’Ã‚Â¼ dÃƒÆ’Ã‚Â¼zenleyin -- yeni bir dil anahtarÃƒâ€Ã‚Â± ekleyin ve tÃƒÆ’Ã‚Â¼m dizeleri ÃƒÆ’Ã‚Â§evirin.

---

## Ajan UyumluluÃƒâ€Ã…Â¸u

| Ajan | Genel Yol | Yerel Destek |
|------|-----------|--------------|
| **Claude Code** | `~/.agents/skills/` | Tam |
| **OpenCode** | `~/.agents/skills/` | Tam |
| **Gemini CLI** | `~/.config/gemini/` | AraÃƒâ€¦Ã…Â¸tÃƒâ€Ã‚Â±rÃƒâ€Ã‚Â±lÃƒâ€Ã‚Â±yor |
| **Cursor** | `.cursor/rules/` (`.mdc`) | FarklÃƒâ€Ã‚Â± format |

---

## Lisans

MIT -- detaylar iÃƒÆ’Ã‚Â§in [LICENSE](LICENSE) dosyasÃƒâ€Ã‚Â±na bakÃƒâ€Ã‚Â±n.

---

## Topluluk

- [Sorunlar](https://github.com/bayraktarozcan/AgentSynapse/issues) -- hatalar, ÃƒÆ’Ã‚Â¶zellik talepleri, sorular.
- [TartÃƒâ€Ã‚Â±Ãƒâ€¦Ã…Â¸malar](https://github.com/bayraktarozcan/AgentSynapse/discussions) -- fikirler, vitrin, yardÃƒâ€Ã‚Â±m.

AI ajan topluluÃƒâ€Ã…Â¸u iÃƒÆ’Ã‚Â§in ÃƒÆ’Ã‚Â¼retilmiÃƒâ€¦Ã…Â¸tir.
