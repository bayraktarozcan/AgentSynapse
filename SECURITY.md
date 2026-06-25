# Security Policy / Güvenlik Politikası

| <kbd>[🇬🇧 **English**](#en)</kbd> | <kbd>[🇹🇷 **Türkçe**](#tr)</kbd> |
|---|---|

---

<a id="en"></a>

<details open>
<summary><b>English</b></summary>

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | Active |

## Reporting a Vulnerability

If you discover a security vulnerability in the Agent Skills Project, please report it privately:

1. **DO NOT** open a public GitHub issue.
2. Open a [GitHub Security Advisory](https://github.com/bayraktarozcan/agent-skills-project/security/advisories/new).

You should receive a response within **48 hours**. If you don't, please follow up.

## What We Consider a Vulnerability

- **Malicious skill injection** — a SKILL.md that instructs an agent to execute harmful commands.
- **Credential exposure** — a repo or skill that leaks API keys, tokens, or secrets.
- **Supply chain risk** — a skill that silently installs dependencies or modifies system files.
- **Social engineering** — a skill that impersonates a trusted project or author.

## Safe Harbor

We consider security research conducted under this policy as authorized conduct.
We will not pursue legal action against researchers who:

- Make a good-faith effort to avoid privacy violations and data destruction.
- Do not exploit a vulnerability beyond what is necessary to confirm it.
- Report vulnerabilities promptly and privately.

## Self-Assessment for Contributors

When adding a new repository to the ecosystem, assess:

1. **Does the repo contain executable code (scripts, binaries)?** — higher risk.
2. **Does the repo use unpinned dependencies?** — supply chain risk.
3. **Are the skill instructions reasonable?** — does any skill instruct the agent to `rm -rf`, `curl | bash`, or modify system configuration without warning?
4. **Is the repo actively maintained?** — stale repos may have unpatched issues.

## Mitigations in This Project

- All repos are cloned to a **temporary directory** that is deleted after installation.
- Skills are **never executed** — they are text files (SKILL.md) installed to `~/.agents/skills/`.
- Risk category (K10) and Community category (K9) are **always opt-in**.
- The recommended profile only includes verified, active repositories.

</details>

<a id="tr"></a>

<details>
<summary><b>Türkçe</b></summary>

## Desteklenen Sürümler

| Sürüm | Destek |
|-------|--------|
| 1.x   | Aktif |

## Güvenlik Açığı Bildirme

Agent Beceri Projesi'nde bir güvenlik açığı keşfederseniz, lütfen özel olarak bildirin:

1. **Herkese açık** bir GitHub sorunu açmayın.
2. [GitHub Güvenlik Danışmanlığı](https://github.com/bayraktarozcan/agent-skills-project/security/advisories/new) açın.

**48 saat** içinde yanıt almalısınız.

## Güvenlik Açığı Olarak Kabul Ettiklerimiz

- **Kötü niyetli beceri enjeksiyonu** — ajana zararlı komutlar çalıştırmasını söyleyen SKILL.md.
- **Kimlik bilgisi sızıntısı** — API anahtarları, tokenler veya sırları sızdıran depo/beceri.
- **Tedarik zinciri riski** — sessizce bağımlılık yükleyen veya sistem dosyalarını değiştiren beceri.
- **Sosyal mühendislik** — güvenilir bir projeyi veya yazarı taklit eden beceri.

## Güvenli Liman

Bu politika kapsamında yürütülen güvenlik araştırmalarını yetkili kabul ediyoruz.

## Katkıda Bulunanlar için Öz Değerlendirme

Ekosisteme yeni bir depo eklerken değerlendirin:

1. Depo çalıştırılabilir kod içeriyor mu? (betikler, ikili dosyalar) — yüksek risk.
2. Depo sabitlenmemiş bağımlılıklar kullanıyor mu? — tedarik zinciri riski.
3. Beceri talimatları makul mü? — ajana rm -rf, curl | bash veya uyarısız sistem yapılandırması değişikliği talimatı var mı?
4. Depo aktif olarak bakımı yapılıyor mu? — güncel olmayan depolarda yamalanmamış sorunlar olabilir.

## Bu Projedeki Önlemler

- Tüm depolar **geçici bir dizine** klonlanır ve kurulumdan sonra silinir.
- Beceriler **asla çalıştırılmaz** — ~/.agents/skills/ konumuna kopyalanan metin dosyalarıdır (SKILL.md).
- Risk (K10) ve Topluluk (K9) kategorileri **her zaman opsiyoneldir**.
- Önerilen profili yalnızca doğrulanmış, aktif depolar içerir.

</details>
