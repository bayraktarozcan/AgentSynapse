# FAQ — SSS (Sık Sorulan Sorular)

| <kbd>[🇬🇧 **English**](#en)</kbd> | <kbd>[🇹🇷 **Türkçe**](#tr)</kbd> |

<a id="en"></a>
<details open>
<summary>English</summary>

## General Questions

### How long does installation take?

The first run clones 34–48 repositories (depends on profile). This typically takes **2–5 minutes** on a broadband connection. Each repo is cloned sequentially; the bottleneck is network speed and the number of repos in the chosen profile.

### Where are skills installed?

All skills are installed to `~/.agents/skills/`. Each source repository gets its own subdirectory named after the repo (e.g., `~/.agents/skills/anthropics-skills/`). This location is auto-discovered by:

- **Claude Code** — reads `~/.agents/skills/` by default
- **OpenCode** — reads the same directory
- **Cursor** — supports the same convention
- Any agent that uses the standard `SKILL.md` discovery path

### How do I uninstall skills?

Simply delete the directory:

```bash
# macOS / Linux
rm -rf ~/.agents/skills

# Windows
rmdir /s %USERPROFILE%\.agents\skills
```

Or remove individual subdirectories for repos you no longer need.

### Can I install to a different location?

Not currently. The installer always writes to `~/.agents/skills/`. This is by design — all major agent tools expect skills in this location.

## Troubleshooting

### The installer says "git not found"

Git is required to clone repositories. Install it from [git-scm.com](https://git-scm.com/), restart your terminal, and try again.

To verify Git is installed:

```bash
git --version
```

### tkinter not found / --gui doesn't work

The `--gui` flag requires tkinter, which is Python's standard GUI toolkit.

| Platform | Solution |
|----------|----------|
| Windows | tkinter is bundled with the official Python installer. Reinstall Python from [python.org](https://python.org) and ensure "tcl/tk and IDLE" is checked. |
| macOS | tkinter is bundled with the official Python installer from python.org. If using Homebrew's Python, install with: `brew install python-tk` |
| Linux (Debian/Ubuntu) | `sudo apt install python3-tk` |
| Linux (Fedora) | `sudo dnf install python3-tkinter` |
| Linux (Arch) | `sudo pacman -S tk` |

### My agent isn't picking up the installed skills

1. Verify the skills are installed: `ls ~/.agents/skills/` (should show subdirectories)
2. Check that each subdirectory contains a `SKILL.md` file
3. Restart your editor / agent after installation
4. Make sure your agent is configured to look in `~/.agents/skills/` (this is the default for Claude Code, OpenCode, and Cursor)

### Installation is slow

The first run clones every repository from scratch. This is network-bound. Possible improvements:
- Use a faster internet connection
- Install fewer categories (e.g., `python skills.py K2` instead of the full profile)
- After the first install, subsequent runs are faster (repos are cached)

### I see "Operation timed out" errors

Some repositories may be large or slow to clone. The installer has a 120-second timeout per repo. If a repo consistently times out:
- Check your internet connection
- The repo may be temporarily unavailable (try again later)
- Skip that repo by choosing a more specific category

### What does "subpath not found" mean?

Some repos store their skills in a subdirectory rather than the root. The installer looks for the specified subpath. If the upstream repo changes its structure, this error may appear. Please [open an issue](https://github.com/bayraktarozcan/agent-skills-project/issues) if you encounter this.

## Category Questions

### Why are Community (K9) and Risk (K10) excluded by default?

These categories contain:
- **K9 (Community)**: Repositories with lower GitHub star counts, lesser-known authors, or unverified quality
- **K10 (Risk)**: Experimental, potentially unmaintained, or high-risk repositories

They are excluded from all profiles except `all` to maintain a high quality bar for the default experience. You can include them with:

```bash
python skills.py all
# or individually:
python skills.py K9 K10
```

### How are categories decided?

Each repository is placed into a category based on its primary function. Criteria include:
- The repository's description and README
- The content of its SKILL.md files
- The domain of the parent project (e.g., Supabase → Cloud, Expo → Mobile)

## Technical Questions

### What Python version is required?

Python 3.9 or later. The installer uses `from __future__ import annotations` and `pathlib.Path`, which are stable in 3.9+.

### Does it work on Windows / macOS / Linux?

Yes. The installer is tested on:
- **Windows** 10/11 (PowerShell 5.1+)
- **macOS** 12+ (Intel and Apple Silicon)
- **Linux** (Ubuntu 22.04+, Debian, Fedora, Arch)

### What does the installer actually do?

1. Reads the embedded `REPOS` registry (48 repos across 10 categories)
2. Filters repos based on the requested profile or category
3. For each repo: clones it to a temp directory, finds `SKILL.md` files, copies them to `~/.agents/skills/<repo-name>/`, cleans up temp files
4. Fixes invalid directory names (spaces → hyphens, dots → underscores)
5. Deduplicates — if two repos ship the same skill filename, the higher-category version wins
6. Saves a timestamped log and directory tree snapshot

### How are duplicates handled?

When two repos contain a `SKILL.md` file with the same name, the one from the **higher category number** wins. For example, if both K2 (AI & LLM) and K4 (Frontend) have `react-skills.md`, the K4 version is kept because 4 > 2.

### Where are logs and tree files saved?

In your **current working directory** (where you run `python skills.py`):
- `Logs/skills-install_YYYY-MM-DD_HH-MM-SS.log` — detailed installation log
- `skills-tree_YYYY-MM-DD_HH-MM-SS.txt` — directory tree of `~/.agents/`

These are timestamped to the second, so every run produces unique files.

</details>

<a id="tr"></a>
<details>
<summary>Türkçe</summary>

## Genel Sorular

### Kurulum ne kadar sürer?

İlk çalıştırma 34–48 depoyu klonlar (profile bağlı). Geniş bant bağlantıda tipik olarak **2–5 dakika** sürer. Her depo sırayla klonlanır; darboğaz ağ hızı ve seçilen profildeki depo sayısıdır.

### Beceriler nereye yüklenir?

Tüm beceriler `~/.agents/skills/` klasörüne yüklenir. Her kaynak depo, repo adıyla kendi alt klasörünü alır (örn. `~/.agents/skills/anthropics-skills/`). Bu konum aşağıdakiler tarafından otomatik olarak keşfedilir:

- **Claude Code** — varsayılan olarak `~/.agents/skills/` okur
- **OpenCode** — aynı dizini okur
- **Cursor** — aynı kuralı destekler
- Standart `SKILL.md` keşif yolunu kullanan her ajan

### Becerileri nasıl kaldırırım?

Dizini silmeniz yeterlidir:

```bash
# macOS / Linux
rm -rf ~/.agents/skills

# Windows
rmdir /s %USERPROFILE%\.agents\skills
```

Veya artık ihtiyacınız olmayan bireysel alt klasörleri kaldırın.

### Farklı bir konuma yükleyebilir miyim?

Şu anda hayır. Yükleyici her zaman `~/.agents/skills/` konumuna yazar. Bu bilinçli bir tasarım kararıdır — tüm büyük ajan araçları becerileri bu konumda bekler.

## Sorun Giderme

### Yükleyici "git bulunamadı" diyor

Depoları klonlamak için Git gereklidir. [git-scm.com](https://git-scm.com/) adresinden yükleyin, terminalinizi yeniden başlatın ve tekrar deneyin.

Git'in yüklü olduğunu doğrulamak için:

```bash
git --version
```

### tkinter bulunamadı / --gui çalışmıyor

`--gui` flag'i, Python'un standart GUI araç seti olan tkinter'ı gerektirir.

| Platform | Çözüm |
|----------|-------|
| Windows | tkinter, resmi Python yükleyicisiyle birlikte gelir. Python'u [python.org](https://python.org) adresinden yeniden yükleyin ve "tcl/tk and IDLE" seçeneğinin işaretli olduğundan emin olun. |
| macOS | tkinter, python.org adresindeki resmi Python yükleyicisiyle birlikte gelir. Homebrew Python kullanıyorsanız: `brew install python-tk` |
| Linux (Debian/Ubuntu) | `sudo apt install python3-tk` |
| Linux (Fedora) | `sudo dnf install python3-tkinter` |
| Linux (Arch) | `sudo pacman -S tk` |

### Ajan yüklenen becerileri görmüyor

1. Becerilerin yüklü olduğunu doğrulayın: `ls ~/.agents/skills/` (alt klasörleri göstermeli)
2. Her alt klasörün bir `SKILL.md` dosyası içerdiğini kontrol edin
3. Kurulumdan sonra düzenleyicinizi / ajanınızı yeniden başlatın
4. Ajanınızın `~/.agents/skills/` konumuna bakacak şekilde yapılandırıldığından emin olun (Claude Code, OpenCode ve Cursor için varsayılan budur)

### Kurulum yavaş

İlk çalıştırma her depoyu sıfırdan klonlar. Bu ağ bağımlıdır. Olası iyileştirmeler:
- Daha hızlı bir internet bağlantısı kullanın
- Daha az kategori yükleyin (tam profil yerine `python skills.py K2`)
- İlk kurulumdan sonraki çalıştırmalar daha hızlıdır (depolar önbelleğe alınır)

### "İşlem zaman aşımına uğradı" hatası görüyorum

Bazı depolar büyük veya klonlaması yavaş olabilir. Yükleyicinin depo başına 120 saniyelik bir zaman aşımı vardır. Bir depo sürekli zaman aşımına uğrarsa:
- İnternet bağlantınızı kontrol edin
- Depo geçici olarak kullanılamıyor olabilir (daha sonra tekrar deneyin)
- Daha spesifik bir kategori seçerek bu depoyu atlayın

### "Alt klasör bulunamadı" ne anlama geliyor?

Bazı depolar becerilerini kök dizin yerine bir alt dizinde saklar. Yükleyici belirtilen alt yolu arar. Yukarı akış deposu yapısını değiştirirse bu hata görünebilir. Bununla karşılaşırsanız lütfen [bir issue açın](https://github.com/bayraktarozcan/agent-skills-project/issues).

## Kategori Soruları

### Topluluk (K9) ve Risk (K10) neden varsayılan olarak hariç tutuluyor?

Bu kategoriler şunları içerir:
- **K9 (Topluluk)**: Düşük GitHub yıldız sayılarına sahip, az bilinen yazarlar veya doğrulanmamış kalite
- **K10 (Risk)**: Deneysel, potansiyel olarak bakımı yapılmayan veya yüksek riskli depolar

Varsayılan deneyimde yüksek kalite çıtasını korumak için `tumu` dışındaki tüm profillerden hariç tutulurlar. Bunları şu şekilde dahil edebilirsiniz:

```bash
python skills.py tumu
# veya tek tek:
python skills.py K9 K10
```

### Kategoriler nasıl belirleniyor?

Her depo, birincil işlevine göre bir kategoriye yerleştirilir. Kriterler şunları içerir:
- Deponun açıklaması ve README'si
- SKILL.md dosyalarının içeriği
- Üst projenin alanı (örn. Supabase → Bulut, Expo → Mobil)

## Teknik Sorular

### Hangi Python sürümü gerekli?

Python 3.9 veya üstü. Yükleyici `from __future__ import annotations` ve `pathlib.Path` kullanır; bunlar 3.9+'da kararlıdır.

### Windows / macOS / Linux'ta çalışır mı?

Evet. Yükleyici aşağıdakilerde test edilmiştir:
- **Windows** 10/11 (PowerShell 5.1+)
- **macOS** 12+ (Intel ve Apple Silicon)
- **Linux** (Ubuntu 22.04+, Debian, Fedora, Arch)

### Yükleyici aslında ne yapıyor?

1. Gömülü `REPOS` kaydını okur (10 kategoride 48 depo)
2. İstenen profile veya kategoriye göre depoları filtreler
3. Her depo için: geçici bir dizine klonlar, `SKILL.md` dosyalarını bulur, `~/.agents/skills/<depo-adi>/` konumuna kopyalar, geçici dosyaları temizler
4. Geçersiz dizin adlarını düzeltir (boşluklar → tireler, noktalar → alt çizgiler)
5. Tekilleştirir — iki depo aynı beceri dosya adını gönderirse, yüksek kategori numarasına sahip olan kazanır
6. Zaman damgalı bir günlük ve dizin ağacı görüntüsü kaydeder

### Yinelenenler nasıl ele alınıyor?

İki depo aynı ada sahip bir `SKILL.md` dosyası içerdiğinde, **daha yüksek kategori numarasına** sahip olan kazanır. Örneğin, hem K2 (AI & DBM) hem de K4 (Ön Yüz) `react-skills.md` içeriyorsa, 4 > 2 olduğu için K4 sürümü korunur.

### Günlükler ve ağaç dosyaları nereye kaydediliyor?

**Geçerli çalışma dizininizde** (`python skills.py` çalıştırdığınız yerde):
- `Logs/skills-install_YYYY-AA-GG_SS-DD-SN.log` — ayrıntılı kurulum günlüğü
- `skills-tree_YYYY-AA-GG_SS-DD-SN.txt` — `~/.agents/` dizin ağacı

Bunlar saniyeye kadar zaman damgalıdır, böylece her çalıştırma benzersiz dosyalar üretir.

</details>
