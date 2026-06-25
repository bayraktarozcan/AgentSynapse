# Installation Guide — Kurulum Kılavuzu

| <kbd>[🇬🇧 **English**](#en)</kbd> | <kbd>[🇹🇷 **Türkçe**](#tr)</kbd> |

<a id="en"></a>
<details open>
<summary>English</summary>

## Prerequisites

| Requirement | Check command | Notes |
|-------------|---------------|-------|
| Python 3.9+ | `python --version` | If not installed, download from [python.org](https://python.org) |
| Git | `git --version` | If not installed, download from [git-scm.com](https://git-scm.com) |
| tkinter (optional) | — | Needed only for `--gui` mode. Included with Python on Windows & macOS. Linux: `sudo apt install python3-tk` |

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/anomalyco/agent-skills-project.git
cd agent-skills-project
```

### 2. Run the installer

```bash
python skills.py
```

This installs the **recommended** profile (34 repos, ~450 skills). Output goes to `~/.agents/skills/`.

### Profiles

| Command | What it installs | Repos | Skills |
|---------|-----------------|-------|--------|
| `python skills.py` | Recommended — curated subset | 34 | ~450 |
| `python skills.py trusted` | All trusted (K1–K8) | 39 | ~600 |
| `python skills.py all` | Everything (K1–K10) | 48 | ~995 |
| `python skills.py K2` | Single category (AI & LLM) | 9 | varies |
| `python skills.py K1 K3 K5` | Multiple categories | varies | varies |

### Turkish Aliases

| Turkish command | Equivalent |
|----------------|------------|
| `python skills.py onerilen` | `python skills.py` (recommended) |
| `python skills.py guvenli` | `python skills.py trusted` |
| `python skills.py tumu` | `python skills.py all` |
| `python skills.py tum` | `python skills.py all` |

### GUI Mode

```bash
python skills.py --gui
```

Launches a tkinter interface with:
- Category checkboxes (toggle each K1–K10)
- Profile quick-select buttons (Recommended / Trusted / All)
- Progress bar showing installation progress
- Live scrolled log output
- Language toggle button (English / Türkçe)

### Language Selection

- **Auto-detect**: The installer reads the `LANG` or `LC_ALL` environment variable. If it starts with `tr`, Turkish is used.
- **Force a language**: `python skills.py --lang tr` or `python skills.py --lang en`
- **GUI toggle**: Click the language button in the bottom-right corner of the GUI window.

### Documentation Flags

All documentation is available at runtime without opening separate files:

| Flag | Shows |
|------|-------|
| `--help` | Help message with all options |
| `--version` | Version string |
| `--list` | List all available categories with descriptions |
| `--show-config` | Dump the embedded repo registry as JSON |
| `--readme` | Display README.md (bilingual) |
| `--changelog` | Display CHANGELOG.md (bilingual) |
| `--conduct` | Display CODE_OF_CONDUCT.md (bilingual) |
| `--security` | Display SECURITY.md (bilingual) |
| `--support` | Display SUPPORT.md (bilingual) |
| `--license` | Display LICENSE |

### Output Files

All generated files are created in your **current working directory** (where you run `skills.py`), not in the project directory. This ensures global compatibility regardless of where you cloned the repo.

| File | Description |
|------|-------------|
| `Logs/skills-install_YYYY-MM-DD_HH-MM-SS.log` | Full installation log with timestamps, errors, and warnings |
| `skills-tree_YYYY-MM-DD_HH-MM-SS.txt` | Directory tree of `~/.agents/` showing installed skills structure |

### Verification

After installation, verify the skills are in place:

```bash
ls ~/.agents/skills/          # macOS / Linux
dir %USERPROFILE%\.agents\skills  # Windows
```

Each subdirectory should contain at least one `SKILL.md` file.

</details>

<a id="tr"></a>
<details>
<summary>Türkçe</summary>

## Gereksinimler

| Gereksinim | Kontrol komutu | Notlar |
|------------|----------------|--------|
| Python 3.9+ | `python --version` | Yüklü değilse [python.org](https://python.org) adresinden indirin |
| Git | `git --version` | Yüklü değilse [git-scm.com](https://git-scm.com) adresinden indirin |
| tkinter (isteğe bağlı) | — | Yalnızca `--gui` modu için gerekli. Windows ve macOS'ta Python ile gelir. Linux: `sudo apt install python3-tk` |

## Kurulum Adımları

### 1. Depoyu klonlayın

```bash
git clone https://github.com/anomalyco/agent-skills-project.git
cd agent-skills-project
```

### 2. Yükleyiciyi çalıştırın

```bash
python skills.py
```

Bu, **önerilen** profili (34 depo, ~450 beceri) yükler. Çıktı `~/.agents/skills/` klasörüne gider.

### Profiller

| Komut | Ne yükler | Depo | Beceri |
|-------|-----------|------|--------|
| `python skills.py` | Önerilen — küratörlü alt küme | 34 | ~450 |
| `python skills.py guvenli` | Tüm güvenli (K1–K8) | 39 | ~600 |
| `python skills.py tumu` | Her şey (K1–K10) | 48 | ~995 |
| `python skills.py K2` | Tek kategori (AI & DBM) | 9 | değişir |
| `python skills.py K1 K3 K5` | Birden çok kategori | değişir | değişir |

### Türkçe Alias'lar

| Türkçe komut | Eşdeğeri |
|--------------|----------|
| `python skills.py onerilen` | `python skills.py` (önerilen) |
| `python skills.py guvenli` | `python skills.py trusted` |
| `python skills.py tumu` | `python skills.py all` |
| `python skills.py tum` | `python skills.py all` |

### GUI Modu

```bash
python skills.py --gui
```

tkinter arayüzünü başlatır:
- Kategori onay kutuları (her K1–K10'u açıp kapatma)
- Profil hızlı seçim düğmeleri (Önerilen / Güvenli / Tümü)
- İlerleme çubuğu
- Canlı kaydırılabilir günlük çıktısı
- Dil değiştirme düğmesi (English / Türkçe)

### Dil Seçimi

- **Otomatik algılama**: Yükleyici, `LANG` veya `LC_ALL` ortam değişkenini okur. `tr` ile başlıyorsa Türkçe kullanılır.
- **Dili zorlama**: `python skills.py --lang tr` veya `python skills.py --lang en`
- **GUI değiştirme**: Pencere sağ alt köşesindeki dil düğmesine tıklayın.

### Dokümantasyon Flag'leri

Tüm dokümantasyon çalışma zamanında ayrı dosya açmadan kullanılabilir:

| Flag | Gösterir |
|------|----------|
| `--help` | Tüm seçeneklerle yardım mesajı |
| `--version` | Sürüm numarası |
| `--list` | Tüm kategorileri açıklamalarıyla listeler |
| `--show-config` | Repo kaydını JSON olarak döker |
| `--readme` | README.md'yi gösterir (çift dilli) |
| `--changelog` | CHANGELOG.md'yi gösterir (çift dilli) |
| `--conduct` | CODE_OF_CONDUCT.md'yi gösterir (çift dilli) |
| `--security` | SECURITY.md'yi gösterir (çift dilli) |
| `--support` | SUPPORT.md'yi gösterir (çift dilli) |
| `--license` | LICENSE'ı gösterir |

### Çıktı Dosyaları

Tüm oluşturulan dosyalar **geçerli çalışma dizininizde** (`skills.py`'yi çalıştırdığınız yerde) oluşturulur, proje dizininde değil. Bu, repoyu nereye klonlarsanız klonlayın global uyumluluk sağlar.

| Dosya | Açıklama |
|-------|----------|
| `Logs/skills-install_YYYY-AA-GG_SS-DD-SN.log` | Zaman damgalı tam kurulum günlüğü, hatalar ve uyarılar |
| `skills-tree_YYYY-AA-GG_SS-DD-SN.txt` | `~/.agents/` klasör yapısını gösteren ağaç görünümü |

### Doğrulama

Kurulumdan sonra becerilerin yerinde olduğunu doğrulayın:

```bash
ls ~/.agents/skills/          # macOS / Linux
dir %USERPROFILE%\.agents\skills  # Windows
```

Her alt klasör en az bir `SKILL.md` dosyası içermelidir.

</details>
