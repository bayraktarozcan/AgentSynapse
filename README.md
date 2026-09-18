# AgentSynapse

| <kbd>[ğŸ‡¬ğŸ‡§ **English**](#en)</kbd> | <kbd>[ğŸ‡¹ğŸ‡· **TÃ¼rkÃ§e**](#tr)</kbd> |
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

`skill-specialization.json` maps every skill to a specialization class (C1â€“C5). The `--profile` flag scopes what stays installed:

| Profile | Classes | Skills |
|---------|---------|--------|
| `temel` | C1, C2 | 222 |
| `dengeli` | C1, C2, C3, first 76 of C4 | 355 |
| `tam` (default) | All C1â€“C5 | 566 |

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

**566'dan fazla kÃ¼ratÃ¶rlÃ¼ AI ajan becerisi**, 34 Ã¼st dÃ¼zey depodan alÄ±nmÄ±ÅŸ, 10 iÅŸlevsel kategoriye ayrÄ±lmÄ±ÅŸ, tek komutla yÃ¼klenebilir. Claude Code, OpenCode ve SKILL.md okuyan her ajan Ã§erÃ§evesi iÃ§in Ã¼retilmiÅŸtir.

[![Skills](https://img.shields.io/badge/skills-566%2B-blue?style=flat-square&color=58a6ff)](https://github.com/bayraktarozcan/AgentSynapse)
[![Repos](https://img.shields.io/badge/repos-34-success?style=flat-square&color=3fb950)](https://github.com/bayraktarozcan/AgentSynapse)
[![Categories](https://img.shields.io/badge/categories-10-purple?style=flat-square&color=bc8cff)](#category-reference)
[![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](LICENSE)

---

## HÄ±zlÄ± BaÅŸlangÄ±Ã§

```bash
git clone https://github.com/bayraktarozcan/AgentSynapse.git
cd AgentSynapse

# Ã–nerilen -- 566+ kÃ¼ratÃ¶rlÃ¼ beceri (varsayÄ±lan)
python skills.py

# Veya Python 3, python3 olarak yÃ¼klendiyse:
python3 skills.py

# Tam gÃ¼venli suite (K1-K8)
python skills.py trusted

# Her ÅŸey (opsiyonel kategoriler dahil)
python skills.py all

# Sadece AI becerileri
python skills.py K2

# Grafik arayÃ¼zÃ¼ baÅŸlat
python skills.py --gui
```

Beceriler `~/.agents/skills/<name>/SKILL.md` konumuna kurulur -- Claude Code ve OpenCode tarafÄ±ndan otomatik keÅŸfedilir.

---

## Gereksinimler

- **Python 3.8+** (sadece standart kÃ¼tÃ¼phane -- pip gerekmez)
- **Git** (depolarÄ± klonlamak iÃ§in)
- **tkinter** (opsiyonel, `--gui` modu iÃ§in)

---

## Ã–zellikler

- **Tek komutla kurulum** -- 34 depoyu klonla, becerileri Ã§Ä±kar, tekrarlarÄ± temizle, bitti.
- **10 iÅŸlevsel kategori** -- Ã‡ekirdek, AI & LLM, Bulut & Backend, Ã–n yÃ¼z & UI, Mobil, GÃ¼venlik, Test, Ä°Ã§erik, Topluluk, Risk.
- **Ä°ki dilli** -- Ä°ngilizce ve TÃ¼rkÃ§e. Otomatik algÄ±lama veya `--lang tr`.
- **Ã‡apraz platform** -- Windows, macOS, Linux. Tek Python dosyasÄ±, baÄŸÄ±mlÄ±lÄ±k yok.
- **VarsayÄ±lan olarak gÃ¼venilir** -- Ã–nerilen profili yalnÄ±zca doÄŸrulanmÄ±ÅŸ depolar iÃ§erir; Topluluk ve Risk opsiyoneldir.
- **Otomatik tekrar temizleme** -- iki depo aynÄ± beceriye sahipse, Ã¼st kategorideki (yÃ¼ksek K numarasÄ±) kazanÄ±r.
- **Ajan-yerel formatÄ±** -- tÃ¼m beceriler standart SKILL.md formatÄ±ndadÄ±r. DÃ¶nÃ¼ÅŸÃ¼m gerekmez.
- **Tam denetim izi** -- zaman damgalÄ± gÃ¼nlÃ¼kler, Ã§alÄ±ÅŸtÄ±rma baÅŸÄ±na klasÃ¶r aÄŸacÄ±.
- **Grafik arayÃ¼z** -- `--gui` ile tkinter yÃ¼kleyici, profil hÄ±zlÄ± seÃ§imi.

---

## KullanÄ±m

### Profiller

| Komut | Kapsam | Depo | Beceri (yaklaÅŸÄ±k) |
|-------|--------|------|--------------------|
| `python skills.py` | Ã–nerilen | 34 | ~566 |
| `python skills.py trusted` | GÃ¼venli (K1-K8) | 39 | ~640 |
| `python skills.py all` | TÃ¼mÃ¼ (K1-K10) | 48 | ~995 |

### UzmanlaÅŸma

`skill-specialization.json`, her beceriyi bir uzmanlaÅŸma sÄ±nÄ±fÄ±na (C1â€“C5) eÅŸler. `--profile` bayraÄŸÄ± neyin kurulu kalacaÄŸÄ±nÄ± kapsamlar:

| Profil | SÄ±nÄ±flar | Beceri |
|--------|----------|--------|
| `temel` | C1, C2 | 222 |
| `dengeli` | C1, C2, C3, C4'Ã¼n ilk 76'sÄ± | 355 |
| `tam` (varsayÄ±lan) | TÃ¼m C1â€“C5 | 566 |

`--profile temel` veya `--profile dengeli` ile yapÄ±lan bir kurulumun ardÄ±ndan profil dÄ±ÅŸÄ± beceriler `~/.agents/_quarantine_<profil>_<tarih>/` klasÃ¶rÃ¼ne taÅŸÄ±nÄ±r (`_moved-list.txt` yazÄ±lÄ±r). `--dry-run` ile Ã¶nizleyin, `--list` / `--check` ile inceleyin:

```bash
python skills.py --dry-run --profile temel    # neyin taÅŸÄ±nacaÄŸÄ±nÄ± Ã¶nizle
python skills.py --check --profile dengeli    # kapsam raporu
python skills.py --list --profile temel       # profil haritasÄ±
```

### Kategoriler

```bash
python skills.py K1          # Ã‡ekirdek -- diller, araÃ§lar
python skills.py K2          # AI & LLM -- ajanlar, RAG, yÃ¶nlendirme
python skills.py K3          # Bulut & Backend
python skills.py K4          # Ã–n yÃ¼z & UI
python skills.py K5          # Mobil
python skills.py K6          # GÃ¼venlik
python skills.py K7          # Test
python skills.py K8          # Ä°Ã§erik
python skills.py K9          # Topluluk (opsiyonel)
python skills.py K10         # Risk (opsiyonel)
```

### SeÃ§enekler

| Bayrak | AÃ§Ä±klama |
|--------|----------|
| `--gui` | Grafik arayÃ¼zÃ¼ baÅŸlat |
| `--lang tr` | TÃ¼rkÃ§e'yi zorla |
| `--lang en` | Ä°ngilizce'yi zorla |
| `--dry-run` | RepolarÄ± kurmadan Ã¶nizle |
| `--prefix PATH` | Ã–zel kurulum dizini |
| `--profile P` | UzmanlaÅŸma profilini uygula (temel, dengeli, tam; varsayÄ±lan tam) |
| `--uninstall` | TÃ¼m becerileri kaldÄ±r |
| `--check` | Ã–n uÃ§uÅŸ ortam kontrolÃ¼ (Python, Git, aÄŸ, disk) |
| `--list` | Kategorileri listele |
| `--show-config` | Repo kaydÄ±nÄ± JSON olarak gÃ¶ster |
| `--version` | SÃ¼rÃ¼mÃ¼ gÃ¶ster |
| `--readme` | Tam README'yi gÃ¶ster |
| `--changelog` | DeÄŸiÅŸiklik gÃ¼nlÃ¼ÄŸÃ¼nÃ¼ gÃ¶ster |
| `--conduct` | DavranÄ±ÅŸ kurallarÄ±nÄ± gÃ¶ster |
| `--security` | GÃ¼venlik politikasÄ±nÄ± gÃ¶ster |
| `--support` | Destek bilgilerini gÃ¶ster |
| `--license` | LisansÄ± gÃ¶ster |
| `--help` | YardÄ±m mesajÄ±nÄ± gÃ¶ster |

### TÃ¼rkÃ§e CLI

```bash
python skills.py --lang tr onerilen      # Ã–nerilen profili yÃ¼kle
python skills.py --lang tr guvenli       # GÃ¼venli kategorileri yÃ¼kle
python skills.py --lang tr tumu          # TÃ¼mÃ¼nÃ¼ yÃ¼kle
python skills.py --lang tr K2            # Sadece AI kategorisi
python skills.py --lang tr --list        # Kategorileri listele
python skills.py --lang tr --gui         # Grafik arayÃ¼zÃ¼ baÅŸlat
```

---

## Kategori ReferansÄ±

| Kod | Kategori | Depo | Durum |
|-----|----------|------|-------|
| **K1** | Ã‡ekirdek (diller, araÃ§lar, kod kalitesi) | 5 | VarsayÄ±lan |
| **K2** | AI & LLM (ajanlar, RAG, yÃ¶nlendirme, tarayÄ±cÄ± ajanlarÄ±) | 9 | VarsayÄ±lan |
| **K3** | Bulut & Backend (AWS, Vercel, Stripe, Neon, Supabase) | 11 | VarsayÄ±lan |
| **K4** | Ã–n yÃ¼z & UI (React, Next.js, Expo, shadcn, WordPress) | 8 | VarsayÄ±lan |
| **K5** | Mobil (iOS, Android, React Native, Expo) | 1 | VarsayÄ±lan |
| **K6** | GÃ¼venlik (inceleme, tarama, saÄŸlamlaÅŸtÄ±rma) | 2 | VarsayÄ±lan |
| **K7** | Test (E2E, birim, gÃ¶rsel regresyon) | 1 | VarsayÄ±lan |
| **K8** | Ä°Ã§erik (yazma, dokÃ¼mantasyon, dÃ¼zenleme, yayÄ±ncÄ±lÄ±k) | 2 | VarsayÄ±lan |
| **K9** | Topluluk (Ã¼Ã§Ã¼ncÃ¼ taraf, dÃ¼ÅŸÃ¼k yÄ±ldÄ±z sayÄ±sÄ±) | 5 | Opsiyonel |
| **K10** | Risk (deneysel, bakÄ±mÄ± yapÄ±lmayan) | 4 | Opsiyonel |

---

## NasÄ±l Ã‡alÄ±ÅŸÄ±r

```
git clone --depth 1 --single-branch <repo> -> SKILL.md Ã¶n yÃ¼zÃ¼nÃ¼ ayrÄ±ÅŸtÄ±r -> tekrarlarÄ± temizle -> ~/.agents/skills/<name>/ konumuna kopyala
```

1. **Klonla** -- her depo geÃ§ici dizine --depth 1 --single-branch ile klonlanÄ±r (yalnÄ±zca tek dal).
2. **AyrÄ±ÅŸtÄ±r** -- her SKILL.md dosyasÄ±nÄ±n `name:` alanÄ± ve alt dizin yolu okunur.
3. **TekrarlarÄ± temizle** -- iki depo aynÄ± beceri adÄ±na sahipse, Ã¼st kategorideki (yÃ¼ksek K) kazanÄ±r.
4. **Kur** -- beceriler `~/.agents/skills/<name>/SKILL.md` konumuna kopyalanÄ±r.

---

## Proje YapÄ±sÄ±

```
AgentSynapse/
+-- skills.py            # TÃ¼m proje -- CLI + GUI, iki dilli, kendi kendine yeter
+-- README.md            # Bu dosya (Ã§ift dilli EN/TR)
+-- CHANGELOG.md         # Ã‡ift dilli deÄŸiÅŸiklik gÃ¼nlÃ¼ÄŸÃ¼
+-- CODE_OF_CONDUCT.md   # Ã‡ift dilli davranÄ±ÅŸ kurallarÄ±
+-- SECURITY.md          # Ã‡ift dilli gÃ¼venlik politikasÄ±
+-- SUPPORT.md           # Ã‡ift dilli destek bilgileri
+-- CONTRIBUTING.md      # Ã‡ift dilli katkÄ± rehberi
+-- LICENSE              # MIT LisansÄ±
+-- Legacy/              # Ã–nceki proje sÃ¼rÃ¼mlerinden arÅŸiv dosyalarÄ± (skills.ps1, karar.md)
+-- Logs/                # Zaman damgalÄ± kurulum gÃ¼nlÃ¼kleri (otomatik)
+-- skills-tree_*.txt    # Ã‡alÄ±ÅŸtÄ±rma baÅŸÄ±na zaman damgalÄ± klasÃ¶r aÄŸacÄ± (otomatik)
+-- skill-specialization.json # UzmanlaÅŸma manifesti (566 beceri, C1-C5)
+-- .github/             # Issue ÅŸablonlarÄ±, finansman, dependabot
```

---

## GeliÅŸtirme

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

1. `skills.py` iÃ§indeki `REPOS` sÃ¶zlÃ¼ÄŸÃ¼nÃ¼ dÃ¼zenleyin -- uygun kategori altÄ±na depo giriÅŸi ekleyin.
2. `python skills.py K<kategori>` ile kurulumu doÄŸrulayÄ±n.

### Dil Ekleme

`skills.py` iÃ§indeki `S` sÃ¶zlÃ¼ÄŸÃ¼nÃ¼ dÃ¼zenleyin -- yeni bir dil anahtarÄ± ekleyin ve tÃ¼m dizeleri Ã§evirin.

---

## Ajan UyumluluÄŸu

| Ajan | Genel Yol | Yerel Destek |
|------|-----------|--------------|
| **Claude Code** | `~/.agents/skills/` | Tam |
| **OpenCode** | `~/.agents/skills/` | Tam |
| **Gemini CLI** | `~/.config/gemini/` | AraÅŸtÄ±rÄ±lÄ±yor |
| **Cursor** | `.cursor/rules/` (`.mdc`) | FarklÄ± format |

---

## Lisans

MIT -- detaylar iÃ§in [LICENSE](LICENSE) dosyasÄ±na bakÄ±n.

---

## Topluluk

- [Sorunlar](https://github.com/bayraktarozcan/AgentSynapse/issues) -- hatalar, Ã¶zellik talepleri, sorular.
- [TartÄ±ÅŸmalar](https://github.com/bayraktarozcan/AgentSynapse/discussions) -- fikirler, vitrin, yardÄ±m.

AI ajan topluluÄŸu iÃ§in Ã¼retilmiÅŸtir.
