#!/usr/bin/env python3
"""
AgentSynapse — cross-platform skill installer.
CLI + GUI, bilingual (EN/TR), zero external dependencies (stdlib only).

Usage:
  python skills.py                         Install recommended profile (default)
  python skills.py trusted                 Install trusted categories (K1-K8)
  python skills.py all                     Install all categories (K1-K10)
  python skills.py K1                      Install a single category
  python skills.py --gui                   Launch graphical interface
  python skills.py --lang tr               Force Turkish language
  python skills.py --dry-run               Preview repos without installing
  python skills.py --prefix PATH           Install to custom directory
  python skills.py --uninstall             Remove all installed skills
  python skills.py --check                 Run pre-flight environment check
  python skills.py --list                  List available categories
  python skills.py --help                  Show this help
"""

from __future__ import annotations

import argparse
import datetime
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

# ─────────────────────────────── I18N ───────────────────────────────

S: dict[str, dict[str, str]] = {
    "en": {
        "app_name": "AgentSynapse",
        "desc": "Install curated AI agent skills from GitHub repositories.",
        "recommended": "Recommended",
        "trusted": "Trusted",
        "all": "All",
        "profile_recommended_desc": "Curated subset (~450 skills)",
        "profile_trusted_desc": "K1-K8 -- all trusted categories (~600 skills)",
        "profile_all_desc": "K1-K10 -- everything (~995 skills)",
        "category": "Category",
        "categories": "Categories",
        "profiles": "Profiles",
        "options": "Options",
        "gui": "Launch graphical interface",
        "lang": "Force language (en or tr)",
        "list": "List available categories",
        "show_config": "Dump repo registry as JSON",
        "readme": "Show full README",
        "changelog": "Show changelog",
        "conduct": "Show code of conduct",
        "security": "Show security policy",
        "support": "Show support info",
        "license": "Show license",
        "help": "Show this help message",
        "version": "Show version",
        "usage": "Usage",
        "examples": "Examples",
        "version_str": "AgentSynapse v1.0.0",
        "processing": "Processing",
        "cloning": "cloning...",
        "cloned": "cloned",
        "skills_extracted": "skills extracted",
        "names_fixed": "names fixed",
        "subpath": "subfolder",
        "no_skill_found": "no SKILL.md found",
        "clone_failed": "clone failed",
        "not_found": "not found",
        "timeout": "operation timed out",
        "subpath_not_found": "subpath not found",
        "ok": "OK",
        "warn": "WARN",
        "error": "ERROR",
        "process": "PROCESS",
        "fix": "FIX",
        "invalid_name": "invalid name",
        "missing_name": "missing name, defaulting to",
        "security_path": "Security — invalid target path",
        "final_success": "OPERATION COMPLETED SUCCESSFULLY",
        "final_none": "NO OPERATIONS PERFORMED",
        "final_partial": "OPERATION PARTIALLY COMPLETED (Errors Occurred)",
        "final_fail": "OPERATION FAILED (All Repos Errored)",
        "total": "Total Success",
        "failed": "Failed",
        "fixed": "Fixed",
        "log_saved": "Log saved",
        "tree_saved": "Directory tree saved",
        "git_required": "Git is required. Install git and try again.",
        "available_categories": "Available categories",
        "gui_title": "AgentSynapse — Skill Installer",
        "gui_select": "Select categories to install:",
        "gui_install": "Install",
        "gui_cancel": "Cancel",
        "gui_installing": "Installing...",
        "gui_done": "Done!",
        "gui_success": "Success:",
        "gui_fail": "Failed:",
        "gui_recommended_hint": "Recommended — curated subset",
        "gui_trusted_hint": "Trusted — K1-K8",
        "gui_all_hint": "All — K1-K10",
        "gui_lang_toggle": "Türkçe",
        "dry_run": "Preview repos without installing",
        "prefix": "Custom install directory",
        "uninstall": "Remove all installed skills",
        "uninstall_confirm": "WARNING: This will delete",
        "uninstall_done": "Skills uninstalled successfully",
        "uninstall_cancel": "Uninstall cancelled",
        "python_version": "Python 3.8 or later is required. Found:",
        "installing": "installing...",
        "proceed": "Proceed? (y/N):",
        "check": "Run pre-flight environment check",
        "pre_flight_title": "====== Environment Check ======",
        "check_pass": "PASS",
        "check_warn": "WARN",
        "check_fail": "FAIL",
        "check_git_ok": "Git found",
        "check_git_missing": "Git not found",
        "install_git_hint": "Install Git:",
        "hint_linux": "  sudo apt install git  # Debian/Ubuntu",
        "hint_mac": "  brew install git  # macOS",
        "hint_win": "  winget install Git.Git  # Windows",
        "check_network_ok": "GitHub reachable",
        "check_network_fail": "GitHub unreachable \u2014 check your internet connection",
        "check_network_skip": "Proceeding without network check",
        "check_disk_ok": "Sufficient disk space",
        "check_disk_warn": "Low disk space: {free} MB free, ~500 MB recommended",
        "check_python_ok": "Python {ver}",
        "check_agents_dir_ok": "Skills directory exists",
        "check_agents_dir_created": "Created skills directory at {path}",
        "check_agents_dir_error": "Failed to create skills directory: {error}",
        "retry_clone": "Clone failed, retrying {n}/{max}...",
        "post_verify_title": "====== Post-Install Verification ======",
        "post_verify_count": "Installed skill directories: {count}",
        "post_verify_empty": "No skill directories found in {path}",
    },
    "tr": {
        "app_name": "Agent Beceri Projesi",
        "desc": "GitHub'dan küratörlü AI ajan becerilerini yükleyin.",
        "recommended": "Önerilen",
        "trusted": "Güvenli",
        "all": "Tümü",
        "profile_recommended_desc": "Küratörlü alt küme (~450 beceri)",
        "profile_trusted_desc": "K1-K8 -- tum guvenli kategoriler (~600 beceri)",
        "profile_all_desc": "K1-K10 -- her sey (~995 beceri)",
        "category": "Kategori",
        "categories": "Kategoriler",
        "profiles": "Profiller",
        "options": "Seçenekler",
        "gui": "Grafik arayüzü başlat",
        "lang": "Dili zorla (en veya tr)",
        "list": "Kategorileri listele",
        "show_config": "Repo kaydını JSON olarak göster",
        "readme": "Tam README'yi göster",
        "changelog": "Değişiklik günlüğünü göster",
        "conduct": "Davranış kurallarını göster",
        "security": "Güvenlik politikasını göster",
        "support": "Destek bilgilerini göster",
        "license": "Lisansı göster",
        "help": "Yardım mesajını göster",
        "version": "Sürümü göster",
        "usage": "Kullanım",
        "examples": "Örnekler",
        "version_str": "Agent Beceri Projesi v1.0.0",
        "processing": "İşleniyor",
        "cloning": "klonlanıyor...",
        "cloned": "klonlandı",
        "skills_extracted": "beceri çıkarıldı",
        "names_fixed": "isim düzeltildi",
        "subpath": "alt klasör",
        "no_skill_found": "SKILL.md bulunamadı",
        "clone_failed": "klonlama başarısız",
        "not_found": "bulunamadı",
        "timeout": "işlem zaman aşımına uğradı",
        "subpath_not_found": "alt klasör bulunamadı",
        "ok": "TAMAM",
        "warn": "UYARI",
        "error": "HATA",
        "process": "İŞLEM",
        "fix": "DÜZELTME",
        "invalid_name": "geçersiz isim",
        "missing_name": "isim yok, varsayılan kullanılıyor",
        "security_path": "Güvenlik — geçersiz hedef yolu",
        "final_success": "İŞLEM BAŞARIYLA TAMAMLANDI",
        "final_none": "HİÇBİR İŞLEM YAPILMADI",
        "final_partial": "İŞLEM KISMEN TAMAMLANDI (Hatalar Oluştu)",
        "final_fail": "İŞLEM BAŞARISIZ (Tüm Repolar Hata Verdi)",
        "total": "Başarılı",
        "failed": "Başarısız",
        "fixed": "Düzeltilen",
        "log_saved": "Log kaydedildi",
        "tree_saved": "Klasör yapısı kaydedildi",
        "git_required": "Git gereklidir. Git'i yükleyip tekrar deneyin.",
        "available_categories": "Kullanılabilir kategoriler",
        "gui_title": "Agent Beceri Projesi — Beceri Yükleyici",
        "gui_select": "Yüklenecek kategorileri seçin:",
        "gui_install": "Yükle",
        "gui_cancel": "İptal",
        "gui_installing": "Yükleniyor...",
        "gui_done": "Tamamlandı!",
        "gui_success": "Başarılı:",
        "gui_fail": "Başarısız:",
        "gui_recommended_hint": "Önerilen — küratörlü alt küme",
        "gui_trusted_hint": "Güvenli — K1-K8",
        "gui_all_hint": "Tümü — K1-K10",
        "gui_lang_toggle": "English",
        "dry_run": "Repolari kurmadan onizle",
        "prefix": "Ozel kurulum dizini",
        "uninstall": "Yuklenmis tum becerileri kaldir",
        "uninstall_confirm": "UYARI: Bu islem su klasoru silecek",
        "uninstall_done": "Beceriler basariyla kaldirildi",
        "uninstall_cancel": "Kaldirma iptal edildi",
        "python_version": "Python 3.8 veya ustu gerekli. Bulunan:",
        "installing": "yukleniyor...",
        "proceed": "Devam edilsin mi? (y/N):",
        "check": "Kurulum oncesi ortam kontrolu yap",
        "pre_flight_title": "====== Ortam Kontrolu ======",
        "check_pass": "BASARILI",
        "check_warn": "UYARI",
        "check_fail": "BASARISIZ",
        "check_git_ok": "Git bulundu",
        "check_git_missing": "Git bulunamadi",
        "install_git_hint": "Git'i yukleyin:",
        "hint_linux": "  sudo apt install git  # Debian/Ubuntu",
        "hint_mac": "  brew install git  # macOS",
        "hint_win": "  winget install Git.Git  # Windows",
        "check_network_ok": "GitHub'a erisilebiliyor",
        "check_network_fail": "GitHub'a erisilemiyor \u2014 internet baglantinizi kontrol edin",
        "check_network_skip": "Ag kontrolu olmadan devam ediliyor",
        "check_disk_ok": "Yeterli disk alani var",
        "check_disk_warn": "Az disk alani: {free} MB bos, ~500 MB onerilir",
        "check_python_ok": "Python {ver}",
        "check_agents_dir_ok": "Beceri klasoru mevcut",
        "check_agents_dir_created": "Beceri klasoru olusturuldu: {path}",
        "check_agents_dir_error": "Beceri klasoru olusturulamadi: {error}",
        "retry_clone": "Klonlama basarisiz, yeniden deneniyor {n}/{max}...",
        "post_verify_title": "====== Kurulum Sonrasi Dogrulama ======",
        "post_verify_count": "Yuklenen beceri klasoru sayisi: {count}",
        "post_verify_empty": "{path} klasorunde beceri bulunamadi",
    },
}


def _(key: str, lang: str = "en") -> str:
    return S.get(lang, S["en"]).get(key, key)


# ─────────────────────────────── EMBEDDED REPO DATA ───────────────────────────────

REPOS: dict[str, Any] = {
    "version": "1.0.0",
    "description": "Embedded repository registry for AgentSynapse.",
    "categories": [
        {
            "id": "K1",
            "name": "Core",
            "description": "General development, languages, tooling, code quality, and architecture",
            "color": "cyan",
            "repos": [
                {"repo": "addyosmani/agent-skills"},
                {"repo": "mattpocock/skills"},
                {"repo": "mgechev/skills-best-practices"},
                {"repo": "obra/superpowers"},
                {"repo": "multica-ai/andrej-karpathy-skills"},
            ],
        },
        {
            "id": "K2",
            "name": "AI & LLM",
            "description": "AI agents, LLM frameworks, prompt engineering, RAG, browser agents",
            "color": "magenta",
            "recommended": True,
            "repos": [
                {"repo": "anthropics/skills", "recommended": True},
                {"repo": "genkit-ai/skills", "recommended": True},
                {"repo": "browser-act/skills", "recommended": True},
                {"repo": "browser-use/browser-use", "recommended": True},
                {"repo": "NousResearch/hermes-agent"},
                {"repo": "agentspace-so/skills"},
                {"repo": "affaan-m/ECC"},
                {"repo": "openclaw/openclaw"},
                {"repo": "agno-agi/agno"},
            ],
        },
        {
            "id": "K3",
            "name": "Cloud & Backend",
            "description": "Cloud platforms, databases, backend services, and infrastructure",
            "color": "blue",
            "repos": [
                {"repo": "supabase/agent-skills"},
                {"repo": "neondatabase/agent-skills"},
                {"repo": "get-convex/agent-skills"},
                {"repo": "firebase/agent-skills"},
                {"repo": "stripe/ai"},
                {"repo": "getsentry/skills"},
                {"repo": "bytedance/deer-flow", "subpath": "skills/public"},
                {"repo": "metabase/metabase", "subpath": ".claude/skills"},
                {"repo": "inference-sh/skills"},
                {"repo": "firecrawl/cli", "subpath": "skills"},
                {"repo": "scrapegraphai/just-scrape", "subpath": "skills"},
            ],
        },
        {
            "id": "K4",
            "name": "Frontend & UI",
            "description": "User interfaces, design systems, visual tools, and frontend frameworks",
            "color": "yellow",
            "repos": [
                {"repo": "shadcn-ui/ui", "subpath": "skills"},
                {"repo": "emilkowalski/skills"},
                {"repo": "kepano/obsidian-skills"},
                {"repo": "heygen-com/hyperframes"},
                {"repo": "pbakaus/impeccable"},
                {"repo": "google-labs-code/stitch-skills"},
                {"repo": "arvindrk/extract-design-system", "subpath": "skills"},
                {"repo": "sleekdotdesign/agent-skills"},
            ],
        },
        {
            "id": "K5",
            "name": "Mobile",
            "description": "iOS, Android, React Native, Expo, mobile development",
            "color": "green",
            "repos": [
                {"repo": "expo/skills"},
            ],
        },
        {
            "id": "K6",
            "name": "Security",
            "description": "Security reviews, vulnerability scanning, hardening, auth",
            "color": "red",
            "repos": [
                {"repo": "better-auth/skills"},
                {"repo": "squirrelscan/skills"},
            ],
        },
        {
            "id": "K7",
            "name": "Testing",
            "description": "E2E, unit, integration, visual regression testing",
            "color": "darkcyan",
            "repos": [
                {"repo": "currents-dev/playwright-best-practices-skill"},
            ],
        },
        {
            "id": "K8",
            "name": "Content",
            "description": "Writing, documentation, content creation, editing, publishing platforms",
            "color": "darkgreen",
            "repos": [
                {"repo": "WordPress/agent-skills"},
                {"repo": "vercel-labs/agent-skills"},
            ],
        },
        {
            "id": "K9",
            "name": "Community",
            "description": "Third-party contributions, lower star counts, lesser-known authors (opt-in)",
            "color": "darkyellow",
            "recommended": False,
            "repos": [
                {"repo": "higgsfield-ai/skills"},
                {"repo": "intellectronica/agent-skills"},
                {"repo": "doany-ai/skills"},
                {"repo": "runcomfy-com/skills"},
                {"repo": "ruvnet/ruflo"},
            ],
        },
        {
            "id": "K10",
            "name": "Risk",
            "description": "Experimental, unmaintained, or high-risk repos (opt-in)",
            "color": "red",
            "recommended": False,
            "repos": [
                {"repo": "juliusbrussee/caveman"},
                {"repo": "leonxlnx/taste-skill"},
                {"repo": "coreyhaines31/marketingskills"},
                {"repo": "wshobson/agents"},
            ],
        },
    ],
}


# ─────────────────────────────── DOC FILES ON DISK (bilingual) ───────────────────────────────

DOC_FLAGS: dict[str, str] = {
    "readme": "README.md",
    "changelog": "CHANGELOG.md",
    "conduct": "CODE_OF_CONDUCT.md",
    "security": "SECURITY.md",
    "support": "SUPPORT.md",
    "license": "LICENSE",
}


def _console_utf8() -> None:
    if sys.platform == "win32":
        import ctypes
        k32 = ctypes.windll.kernel32
        k32.SetConsoleOutputCP(65001)


def show_doc(name: str, lang: str) -> None:
    path = SCRIPT_DIR / DOC_FLAGS[name]
    if not path.exists():
        print(f"Error: {path.name} not found")
        return
    text = path.read_text(encoding="utf-8").strip()
    _console_utf8()
    try:
        sys.stdout.buffer.write(text.encode("utf-8"))
        sys.stdout.buffer.write(b"\n")
    except (UnicodeEncodeError, AttributeError):
        print(text.encode("utf-8", errors="replace").decode("utf-8", errors="replace"))


# ─────────────────────────────── PATHS ───────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
SKILLS_DIR = Path.home() / ".agents" / "skills"
AGENTS_DIR = Path.home() / ".agents"
LOGS_DIR = Path.cwd() / "Logs"
TREE_DIR = Path.cwd()

# ─────────────────────────────── LOGGING ───────────────────────────────

LOG_PATH: Path | None = None
LOG_FILE_HANDLER: logging.Handler | None = None


def setup_logging(lang: str) -> None:
    global LOG_PATH, LOG_FILE_HANDLER
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    LOG_PATH = LOGS_DIR / f"skills-install_{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.log"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if LOG_FILE_HANDLER:
        logger.removeHandler(LOG_FILE_HANDLER)

    LOG_FILE_HANDLER = logging.FileHandler(str(LOG_PATH), encoding="utf-8")
    LOG_FILE_HANDLER.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")
    LOG_FILE_HANDLER.setFormatter(fmt)
    logger.addHandler(LOG_FILE_HANDLER)

    logging.info("=" * 60)
    logging.info(f"{_('app_name', lang)} — {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
    logging.info("=" * 60)


# ─────────────────────────────── COLOR ───────────────────────────────

_COLORS: dict[str, str] = {
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[0;34m",
    "magenta": "\033[0;35m",
    "cyan": "\033[0;36m",
    "white": "\033[1;37m",
    "reset": "\033[0m",
}


def c(text: str, color: str = "") -> str:
    if not color or not sys.stdout.isatty():
        return text
    return f"{_COLORS.get(color, '')}{text}{_COLORS['reset']}"


def color_for_cat(cat_id: str) -> str:
    idx = abs(hash(cat_id)) % 6
    return ["cyan", "magenta", "blue", "green", "yellow", "white"][idx]


# ─────────────────────────────── REPO DATA ───────────────────────────────

def load_config(lang: str = "en") -> dict[str, Any]:
    return REPOS


def list_categories(lang: str) -> list[dict[str, Any]]:
    data = load_config(lang)
    return data.get("categories", [])


def list_repos(target: str, lang: str) -> list[tuple[str, str, str, str, str]]:
    """
    Returns list of (cat_id, cat_name, cat_color, repo, subpath).
    target: profile name ("recommended", "trusted", "all") or a category id.
    """
    trusted_ids = {"K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"}
    results: list[tuple[str, str, str, str, str]] = []

    for cat in list_categories(lang):
        cat_id: str = cat["id"]
        cat_name: str = cat["name"]
        cat_color: str = cat.get("color", "white")
        repos_list: list[dict[str, Any]] = cat.get("repos", [])

        if target == "recommended":
            if cat.get("recommended") is False:
                continue
            has_per_repo = any(
                r.get("recommended") is not None for r in repos_list
            )
            if has_per_repo:
                repos_list = [r for r in repos_list if r.get("recommended")]
        elif target == "trusted":
            if cat_id not in trusted_ids:
                continue
        elif target != "all":
            # Single category match
            target_u = target.upper()
            if (
                cat_id != target_u
                and cat_id.lower() != target.lower()
                and cat_name.lower() != target.lower()
            ):
                continue

        for r in repos_list:
            results.append(
                (cat_id, cat_name, cat_color, r["repo"], r.get("subpath", ""))
            )

    return results


# ─────────────────────────────── CLEANUP HELPERS ───────────────────────────────

def valid_name(name: str) -> str:
    n = name.lower().replace(" ", "-").replace("_", "-")
    n = re.sub(r"[^a-z0-9-]", "", n)
    n = re.sub(r"-+", "-", n)
    n = n.strip("-")
    return (n or "skill")[:64].rstrip("-")


def cleanup(tmpdir: str | Path) -> None:
    try:
        d = Path(tmpdir)
        if d.exists():
            shutil.rmtree(d)
    except OSError:
        pass


# ─────────────────────────────── PROCESS A SINGLE REPO ───────────────────────────────

def process_repo(
    repo: str, subpath: str, lang: str
) -> tuple[int, int]:
    """
    Clone repo, find SKILL.md files, copy to SKILLS_DIR.
    Retries up to 2 times on clone failure.
    Returns (skill_count, fix_count).
    """
    safe_name = repo.replace("/", "-")
    tmpdir = Path(tempfile.mkdtemp(prefix=f"asp-{safe_name}-"))

    logging.info(f"[PROCESS] {repo} {_('cloning', lang)}")
    print(c(f"  [{_('process', lang)}] {repo} {_('cloning', lang)}", "blue"))

    max_retries = 3
    last_error = ""

    for attempt in range(1, max_retries + 1):
        try:
            result = subprocess.run(
                ["git", "clone", "--depth", "1", f"https://github.com/{repo}.git", str(tmpdir)],
                capture_output=True,
                text=True,
                timeout=300,
            )
        except FileNotFoundError:
            logging.error(f"[ERROR] git {_('not_found', lang)}")
            print(c(f"  [{_('error', lang)}] git {_('not_found', lang)}", "red"))
            _install_git_hint(lang)
            cleanup(tmpdir)
            return 0, 0
        except subprocess.TimeoutExpired as exc:
            last_error = str(exc)
            logging.error(f"[ERROR] {repo} — {_('timeout', lang)} (attempt {attempt}/{max_retries})")
            print(c(f"  [{_('error', lang)}] {repo} — {_('timeout', lang)}", "red"))
            cleanup(tmpdir)
            if attempt < max_retries:
                tmpdir = Path(tempfile.mkdtemp(prefix=f"asp-{safe_name}-"))
                print(c(f"    {_('retry_clone', lang).format(n=attempt + 1, max=max_retries)}", "yellow"))
                time.sleep(2)
                continue
            return 0, 0

        if result.returncode == 0:
            break  # success

        last_error = result.stderr.strip()
        logging.error(f"[ERROR] {repo} — {_('clone_failed', lang)} (attempt {attempt}/{max_retries}): {last_error}")
        print(c(f"  [{_('error', lang)}] {repo} — {_('clone_failed', lang)}", "red"))
        if attempt < max_retries:
            cleanup(tmpdir)
            tmpdir = Path(tempfile.mkdtemp(prefix=f"asp-{safe_name}-"))
            print(c(f"    {_('retry_clone', lang).format(n=attempt + 1, max=max_retries)}", "yellow"))
            time.sleep(2)
        else:
            cleanup(tmpdir)
            return 0, 0

    src = tmpdir
    if subpath:
        src = tmpdir / subpath
        if not src.is_dir():
            logging.error(f"[ERROR] {repo} — {_('subpath_not_found', lang)}: {subpath}")
            print(
                c(
                    f"  [{_('error', lang)}] {repo} — {_('subpath_not_found', lang)}: {subpath}",
                    "red",
                )
            )
            cleanup(tmpdir)
            return 0, 0

    # Remove junk dirs
    for junk in (
        "node_modules", ".git", ".changeset", "dist", "build",
        ".next", ".turbo", "__pycache__", ".venv", "venv", "env",
        ".ruff_cache", ".mypy_cache", ".pytest_cache",
    ):
        junk_path = src / junk
        if junk_path.is_dir():
            shutil.rmtree(junk_path, ignore_errors=True)

    count = 0
    fixes = 0
    processed_names: set[str] = set()

    for mdfile in src.rglob("SKILL.md"):
        skill_dir = mdfile.parent
        dir_name = skill_dir.name

        # If dir is 'skills'/'skill'/'plugin', go up one
        if dir_name in ("skills", "skill", "plugin"):
            dir_name = skill_dir.parent.name

        # Try to extract 'name:' from frontmatter
        parsed_name = ""
        try:
            with open(mdfile, encoding="utf-8", errors="replace") as f:
                head = f.read(2000)
            in_front = 0
            for line in head.splitlines():
                if line.startswith("---"):
                    in_front += 1
                    if in_front >= 2:
                        break
                    continue
                if in_front == 1 and line.lower().startswith("name:"):
                    parsed_name = line.split(":", 1)[1].strip().strip("\"'")
                    break
        except OSError:
            pass

        name = parsed_name or dir_name
        fixed_name = valid_name(name)

        if name != fixed_name:
            if parsed_name:
                msg = f"[FIX] {_('invalid_name', lang)} '{parsed_name}' -> '{fixed_name}'"
            else:
                msg = f"[FIX] {_('missing_name', lang)} '{dir_name}' -> '{fixed_name}'"
            logging.warning(msg)
            print(c(f"    [{_('fix', lang)}] {msg}", "yellow"))

            # Fix in file
            try:
                with open(mdfile, encoding="utf-8") as f:
                    content = f.read()
                content = re.sub(
                    r"^name:\s*.*",
                    f"name: {fixed_name}",
                    content,
                    count=1,
                    flags=re.MULTILINE,
                )
                with open(mdfile, "w", encoding="utf-8") as f:
                    f.write(content)
            except OSError:
                pass
            name = fixed_name
            fixes += 1

        if not name or name in processed_names:
            continue
        processed_names.add(name)

        dest = SKILLS_DIR / name
        if not str(dest).startswith(str(SKILLS_DIR)):
            logging.error(f"[SECURITY] {_('security_path', lang)}: {dest}")
            print(c(f"  [{_('error', lang)}] {_('security_path', lang)}: {dest}", "red"))
            continue

        dest.mkdir(parents=True, exist_ok=True)
        _copy_recursive(skill_dir, dest)
        count += 1

    cleanup(tmpdir)

    if count == 0:
        logging.warning(f"[WARN] {repo} — {_('no_skill_found', lang)}")
        print(c(f"  [{_('warn', lang)}] {repo} — {_('no_skill_found', lang)}", "yellow"))
        return 0, fixes

    msg = f"[{_('ok', lang)}] {repo} -> {count} {_('skills_extracted', lang)}"
    if fixes > 0:
        msg += f", {fixes} {_('names_fixed', lang)}"
    logging.info(msg)
    print(c(f"  [{_('ok', lang)}] {repo} -> {count} {_('skills_extracted', lang)}", "green"))
    if fixes > 0:
        print(c(f"       {fixes} {_('names_fixed', lang)}", "yellow"))
    return count, fixes


def _copy_recursive(src: Path, dst: Path) -> None:
    """Copy all files from src to dst, merging directories."""
    for item in src.iterdir():
        s = src / item.name
        d = dst / item.name
        if s.is_dir():
            _copy_recursive(s, d)
        else:
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(s, d)


# ─────────────────────────────── PROACTIVE ERROR HANDLING ───────────────────────────────


def _print_check(label: str, status: str, detail: str = "", lang: str = "en") -> None:
    status_map = {
        _("check_pass", lang): "green",
        _("check_warn", lang): "yellow",
        _("check_fail", lang): "red",
    }
    sc = status_map.get(status, "white")
    label_pad = label.ljust(28)
    print(c(f"  [{status}] {label_pad} {detail}", sc))


def _get_free_space(path: Path) -> int:
    """Return free space in MB at the given path."""
    try:
        usage = shutil.disk_usage(path)
        return usage.free // (1024 * 1024)
    except OSError:
        return 0


def _check_network(lang: str) -> bool:
    """Check if GitHub is reachable via HEAD request."""
    import urllib.request
    import urllib.error
    try:
        req = urllib.request.Request(
            "https://github.com",
            method="HEAD",
            headers={"User-Agent": "Mozilla/5.0"},
        )
        urllib.request.urlopen(req, timeout=10)
        return True
    except (urllib.error.URLError, OSError):
        return False


def _install_git_hint(lang: str) -> None:
    """Print OS-specific git install instruction."""
    print(c(f"    {_('install_git_hint', lang)}", "yellow"))
    if sys.platform == "linux":
        print(c(f"    {_('hint_linux', lang)}", "white"))
    elif sys.platform == "darwin":
        print(c(f"    {_('hint_mac', lang)}", "white"))
    elif sys.platform == "win32":
        print(c(f"    {_('hint_win', lang)}", "white"))
    else:
        print(c(f"    https://git-scm.com/downloads", "white"))
    print()


def pre_flight_check(lang: str) -> bool:
    """Run all environment checks. Returns True if all critical checks pass."""
    env_pass = True

    print()
    print(c(f"  {_('pre_flight_title', lang)}", "white"))
    print(c("=" * 55, "white"))

    # 1. Python version
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    if sys.version_info >= (3, 8):
        _print_check(_("check_python_ok", lang).format(ver=py_ver), _("check_pass", lang), lang=lang)
    else:
        _print_check(_("check_python_ok", lang).format(ver=py_ver), _("check_fail", lang), lang=lang)
        env_pass = False

    # 2. Git
    if _check_git(lang):
        _print_check(_("check_git_ok", lang), _("check_pass", lang), lang=lang)
    else:
        _print_check(_("check_git_missing", lang), _("check_fail", lang), lang=lang)
        _install_git_hint(lang)
        env_pass = False

    # 3. Network
    if _check_network(lang):
        _print_check(_("check_network_ok", lang), _("check_pass", lang), lang=lang)
    else:
        _print_check(_("check_network_fail", lang), _("check_fail", lang), lang=lang)
        _print_check(_("check_network_skip", lang), _("check_warn", lang), lang=lang)

    # 4. Disk space
    parent = SKILLS_DIR.parent if SKILLS_DIR.parent.exists() else Path.home()
    free_mb = _get_free_space(parent)
    if free_mb >= 500:
        _print_check(_("check_disk_ok", lang), _("check_pass", lang), detail=f"{free_mb} MB", lang=lang)
    elif free_mb > 0:
        _print_check(_("check_disk_warn", lang).format(free=free_mb), _("check_warn", lang), lang=lang)
    else:
        _print_check(_("check_disk_ok", lang), _("check_pass", lang), detail="N/A", lang=lang)

    # 5. Skills directory
    try:
        SKILLS_DIR.mkdir(parents=True, exist_ok=True)
        if SKILLS_DIR.is_dir():
            _print_check(_("check_agents_dir_ok", lang), _("check_pass", lang), detail=str(SKILLS_DIR), lang=lang)
        else:
            _print_check(_("check_agents_dir_created", lang).format(path=str(SKILLS_DIR)), _("check_pass", lang), lang=lang)
    except OSError as e:
        _print_check(_("check_agents_dir_error", lang).format(error=str(e)), _("check_fail", lang), lang=lang)
        env_pass = False

    print(c("=" * 55, "white"))
    print()
    return env_pass


def _post_install_verify(lang: str) -> None:
    """Count installed skill directories and print summary."""
    print()
    print(c(f"  {_('post_verify_title', lang)}", "white"))
    print(c("=" * 55, "white"))
    if SKILLS_DIR.is_dir():
        skill_dirs = [d for d in SKILLS_DIR.iterdir() if d.is_dir()]
        count = len(skill_dirs)
        if count > 0:
            _print_check(_("post_verify_count", lang).format(count=count), _("check_pass", lang), lang=lang)
        else:
            _print_check(_("post_verify_empty", lang).format(path=str(SKILLS_DIR)), _("check_warn", lang), lang=lang)
    else:
        _print_check(_("post_verify_empty", lang).format(path=str(SKILLS_DIR)), _("check_warn", lang), lang=lang)
    print(c("=" * 55, "white"))
    print()


# ─────────────────────────────── INSTALL FROM LIST ───────────────────────────────

def _check_git(lang: str) -> bool:
    """Check if git is available. Returns True if found."""
    try:
        result = subprocess.run(
            ["git", "--version"], capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: search common git locations
    common_paths = [
        r"C:\Program Files\Git\cmd\git.exe",
        r"C:\Program Files (x86)\Git\cmd\git.exe",
        "/usr/bin/git",
        "/usr/local/bin/git",
        "/opt/homebrew/bin/git",
    ]
    for gp in common_paths:
        if Path(gp).exists():
            return True

    return False


def _dry_run_list(target: str, lang: str) -> None:
    rows = list_repos(target, lang)
    if not rows:
        print(c(f"  [{_('warn', lang)}] No repos found for '{target}'.", "yellow"))
        return
    cat_map: dict[str, list[str]] = {}
    skill_est = 0
    for cat_id, cat_name, cat_color, repo, subpath in rows:
        cat_map.setdefault(f"{cat_id} — {cat_name}", []).append(repo + (f" ({_('subpath', lang)}: {subpath})" if subpath else ""))
        skill_est += 10
    print(c(f"\n  [{_('dry_run', lang).upper()}]", "white"))
    print(c("=" * 55, "white"))
    for cat_header, repos_list in cat_map.items():
        print(c(f"  {cat_header}", "cyan"))
        for r in repos_list:
            print(f"    {r}")
        print()
    print(c(f"  {_('total', lang)}: {len(rows)} {_('dry_run', lang)}", "white"))
    print(c(f"  ~{skill_est} {_('skills_extracted', lang)}", "white"))
    print()


def install(
    target: str, lang: str
) -> tuple[int, int, int]:
    """
    Install skills for the given target.
    Returns (ok_count, fail_count, fix_count).
    """
    rows = list_repos(target, lang)

    if not rows:
        print(c(f"  [{_('warn', lang)}] No repos found for '{target}'.", "yellow"))
        return 0, 0, 0

    # Auto-create skills directory
    try:
        SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(c(f"  [{_('error', lang)}] {_('check_agents_dir_error', lang).format(error=str(e))}", "red"))
        return 0, 0, 0

    if not _check_git(lang):
        print(c(f"  [{_('error', lang)}] git {_('not_found', lang)}", "red"))
        _install_git_hint(lang)
        return 0, 0, 0

    total_rows = len(rows)

    prev_id = ""
    prev_name = ""
    prev_color = ""
    cat_ok = 0
    cat_fail = 0
    total_ok = 0
    total_fail = 0
    total_fixes = 0

    for idx, (cat_id, cat_name, cat_color, repo, subpath) in enumerate(rows, 1):
        if cat_id != prev_id:
            if prev_id:
                col = color_for_cat(prev_id)
                print(c("─" * 55, "white"))
                print(
                    c(
                        f"[SUMMARY] {prev_id} — {prev_name}: "
                        f"{_('ok', lang).upper()}: {cat_ok} | "
                        f"{_('failed', lang)}: {cat_fail}",
                        col,
                    )
                )
            prev_id = cat_id
            prev_name = cat_name
            prev_color = cat_color
            cat_ok = 0
            cat_fail = 0
            col = color_for_cat(cat_id)
            print()
            print(c("=" * 55, col))
            print(c(f"     {cat_id} — {cat_name}", col))
            print(c("=" * 55, col))

        print(
            c(
                f"  [{idx}/{total_rows}] {repo}"
                + (f" -> {_('subpath', lang)} '{subpath}'" if subpath else ""),
                "blue",
            )
        )

        sk_count, fx_count = process_repo(repo, subpath, lang)
        total_fixes += fx_count

        if sk_count > 0:
            cat_ok += 1
            total_ok += 1
        else:
            cat_fail += 1
            total_fail += 1

    if prev_id:
        col = color_for_cat(prev_id)
        print(c("─" * 55, "white"))
        print(
            c(
                f"[SUMMARY] {prev_id} — {prev_name}: "
                f"{_('ok', lang).upper()}: {cat_ok} | "
                f"{_('failed', lang)}: {cat_fail}",
                col,
            )
        )

    return total_ok, total_fail, total_fixes


# ─────────────────────────────── TREE ───────────────────────────────

def save_tree(lang: str) -> str | None:
    if not AGENTS_DIR.is_dir():
        return None
    tree_file = TREE_DIR / f"skills-tree_{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.txt"
    tree_lines: list[str] = []

    def _walk(dirpath: Path, prefix: str = "") -> None:
        entries = sorted(dirpath.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            suffix = "/" if entry.is_dir() else ""
            tree_lines.append(f"{prefix}{connector}{entry.name}{suffix}")
            if entry.is_dir():
                extension = "    " if is_last else "│   "
                _walk(entry, prefix + extension)

    try:
        _walk(AGENTS_DIR)
    except OSError:
        tree_lines.append("(error reading directory tree)")

    tree_file.write_text("\n".join(tree_lines), encoding="utf-8")
    logging.info(f"[INFO] {_('tree_saved', lang)}: {tree_file}")
    print(c(f"  [{_('ok', lang)}] {_('tree_saved', lang)}: {tree_file}", "white"))
    return str(tree_file)


# ─────────────────────────────── HELPERS ───────────────────────────────

def _detect_lang() -> str:
    """Detect language from environment. Turkish if LANG starts with tr, else English."""
    lang_env = os.environ.get("LANG", "") or os.environ.get("LC_ALL", "") or ""
    return "tr" if lang_env.lower().startswith("tr") else "en"


def print_header(title: str, lang: str) -> None:
    print()
    print(c("=" * 55, "green"))
    print(c(f"  {title}", "green"))
    print(c("=" * 55, "green"))
    print()


def final_report(ok: int, fail: int, fixes: int, lang: str) -> None:
    if fail == 0 and ok > 0:
        status = _("final_success", lang)
        sc = "green"
    elif ok == 0 and fail == 0:
        status = _("final_none", lang)
        sc = "yellow"
    elif ok > 0 and fail > 0:
        status = _("final_partial", lang)
        sc = "yellow"
    else:
        status = _("final_fail", lang)
        sc = "red"

    print()
    print(c("=" * 55, sc))
    print(c(f"         {status}", sc))
    print(c(f"  {_('total', lang)}: {ok} | {_('failed', lang)}: {fail} | {_('fixed', lang)}: {fixes}", sc))
    print(c("=" * 55, sc))

    if ok > 0:
        _post_install_verify(lang)

    save_tree(lang)
    if LOG_PATH:
        print(c(f"  {_('log_saved', lang)}: {LOG_PATH}", "white"))


# ─────────────────────────────── GUI ───────────────────────────────

# ── OLED Dark Theme ──

OLED_BG = "#000000"
OLED_BG_SEC = "#0d1117"
OLED_BG_CARD = "#161b22"
OLED_BG_HOVER = "#1c2128"
OLED_BORDER = "#30363d"
OLED_BORDER_FOCUS = "#484f58"
OLED_TEXT = "#e6edf3"
OLED_TEXT_SEC = "#8b949e"
OLED_TEXT_MUTED = "#6e7681"
OLED_ACCENT = "#d29922"
OLED_ACCENT_DIM = "#bb8009"
OLED_SUCCESS = "#3fb950"
OLED_SUCCESS_DIM = "#2ea043"
OLED_WARN = "#d29922"
OLED_ERROR = "#f85149"
OLED_SELECT = "#264f78"
OLED_FONT = ("Segoe UI", 10)
OLED_FONT_MONO = ("Consolas", 10)
OLED_FONT_SMALL = ("Segoe UI", 9)
OLED_FONT_HEADER = ("Segoe UI", 11, "bold")


def _apply_oled_theme(root: tk.Tk) -> None:
    """Apply OLED dark theme to all tkinter/ttk widgets in-place."""
    import tkinter as tk
    from tkinter import ttk

    root.configure(bg=OLED_BG)
    root.option_add("*Font", OLED_FONT)

    style = ttk.Style(root)

    # Determine platform theme name
    theme = style.theme_use()
    available = style.theme_names()
    # Prefer "clam" as base for custom themes
    if "clam" in available:
        style.theme_use("clam")

    # ── Root / Frame ──
    style.configure(".", background=OLED_BG, foreground=OLED_TEXT,
                     fieldbackground=OLED_BG, troughcolor=OLED_BG,
                     selectbackground=OLED_SELECT, selectforeground=OLED_TEXT,
                     borderwidth=0, focuscolor=OLED_BORDER_FOCUS)

    # ── Frame ──
    style.configure("TFrame", background=OLED_BG)
    style.configure("Card.TFrame", background=OLED_BG_CARD,
                    relief="solid", borderwidth=1)
    style.configure("Section.TFrame", background=OLED_BG_SEC,
                    relief="flat", borderwidth=0)

    # ── Label ──
    style.configure("TLabel", background=OLED_BG, foreground=OLED_TEXT,
                    font=OLED_FONT, padding=2)
    style.configure("Header.TLabel", background=OLED_BG, foreground=OLED_TEXT,
                    font=OLED_FONT_HEADER)
    style.configure("Muted.TLabel", background=OLED_BG, foreground=OLED_TEXT_SEC,
                    font=OLED_FONT_SMALL)
    style.configure("Accent.TLabel", background=OLED_BG, foreground=OLED_ACCENT,
                    font=OLED_FONT)

    # ── Button ──
    style.configure("TButton", background=OLED_BG_CARD, foreground=OLED_TEXT,
                    font=OLED_FONT, borderwidth=1, focuscolor="none",
                    relief="solid", padding=(14, 6))
    style.map("TButton",
              background=[("active", OLED_BG_HOVER), ("pressed", OLED_BORDER)],
              foreground=[("active", OLED_TEXT), ("pressed", OLED_ACCENT)],
              bordercolor=[("active", OLED_ACCENT_DIM), ("focus", OLED_BORDER_FOCUS)])

    # ── Accent Button (Install) ──
    style.configure("Accent.TButton", background=OLED_ACCENT_DIM, foreground=OLED_BG,
                    font=OLED_FONT_HEADER, borderwidth=0, relief="flat",
                    padding=(20, 8))
    style.map("Accent.TButton",
              background=[("active", OLED_ACCENT), ("disabled", OLED_BORDER)],
              foreground=[("active", OLED_BG), ("disabled", OLED_TEXT_MUTED)])

    # ── Danger Button (Cancel) ──
    style.configure("Danger.TButton", background="#21262d", foreground=OLED_TEXT,
                    font=OLED_FONT, borderwidth=1, relief="solid",
                    padding=(14, 6))
    style.map("Danger.TButton",
              background=[("active", OLED_ERROR), ("pressed", "#da3633")],
              foreground=[("active", "#ffffff")])

    # ── Checkbutton ──
    style.configure("TCheckbutton", background=OLED_BG, foreground=OLED_TEXT,
                    font=OLED_FONT, focuscolor="none", indicatormargin=4)
    style.map("TCheckbutton",
              background=[("active", OLED_BG_SEC)],
              foreground=[("active", OLED_TEXT)])

    # ── Radiobutton ──
    style.configure("TRadiobutton", background=OLED_BG, foreground=OLED_TEXT,
                    font=OLED_FONT, focuscolor="none")
    style.map("TRadiobutton",
              background=[("active", OLED_BG_SEC)])

    # ── Progressbar ──
    style.configure("Horizontal.TProgressbar",
                    background=OLED_ACCENT, troughcolor=OLED_BG_SEC,
                    bordercolor=OLED_BORDER, lightcolor=OLED_ACCENT_DIM,
                    darkcolor=OLED_ACCENT, thickness=8)

    # ── Scrollbar ──
    style.configure("Vertical.TScrollbar",
                    background=OLED_BG_CARD, troughcolor=OLED_BG,
                    bordercolor=OLED_BORDER, arrowcolor=OLED_TEXT,
                    relief="flat", borderwidth=0)
    style.map("Vertical.TScrollbar",
              background=[("active", OLED_BORDER)],
              arrowcolor=[("active", OLED_ACCENT)])

    # ── Entry ──
    style.configure("TEntry", fieldbackground=OLED_BG_SEC, foreground=OLED_TEXT,
                    font=OLED_FONT, borderwidth=1, relief="solid",
                    insertcolor=OLED_TEXT)
    style.map("TEntry",
              fieldbackground=[("focus", OLED_BG_CARD)],
              bordercolor=[("focus", OLED_ACCENT_DIM)])

    # ── Labelframe ──
    style.configure("TLabelframe", background=OLED_BG, foreground=OLED_TEXT,
                    bordercolor=OLED_BORDER, relief="solid", borderwidth=1)
    style.configure("TLabelframe.Label", background=OLED_BG, foreground=OLED_TEXT,
                    font=OLED_FONT)

    # ── Treeview ──
    style.configure("Treeview", background=OLED_BG_SEC, foreground=OLED_TEXT,
                    fieldbackground=OLED_BG_SEC, font=OLED_FONT_SMALL,
                    borderwidth=0)
    style.map("Treeview",
              background=[("selected", OLED_SELECT)],
              foreground=[("selected", OLED_TEXT)])
    style.configure("Treeview.Heading", background=OLED_BG_CARD,
                    foreground=OLED_TEXT, font=OLED_FONT,
                    borderwidth=1, relief="solid")
    style.map("Treeview.Heading",
              background=[("active", OLED_BG_HOVER)])


def _dark_text_widget(widget: tk.Text) -> None:
    """Apply dark theme to a plain tk.Text widget."""
    widget.configure(
        bg=OLED_BG_SEC,
        fg=OLED_TEXT,
        insertbackground=OLED_TEXT,
        selectbackground=OLED_SELECT,
        selectforeground=OLED_TEXT,
        borderwidth=1,
        relief="solid",
        highlightbackground=OLED_BORDER,
        highlightcolor=OLED_BORDER_FOCUS,
        highlightthickness=1,
        padx=8,
        pady=6,
    )
    # Configure tags for colored log output
    widget.tag_configure("green", foreground=OLED_SUCCESS)
    widget.tag_configure("blue", foreground="#58a6ff")
    widget.tag_configure("red", foreground=OLED_ERROR)
    widget.tag_configure("yellow", foreground=OLED_WARN)
    widget.tag_configure("white", foreground=OLED_TEXT)
    widget.tag_configure("bold", font=OLED_FONT_HEADER)
    widget.tag_configure("dim", foreground=OLED_TEXT_MUTED)


def gui_main(args: argparse.Namespace) -> None:
    lang = args.lang or _detect_lang()

    try:
        import tkinter as tk
        from tkinter import ttk, scrolledtext
    except ImportError:
        print(c("[ERROR] tkinter is not available on this system.", "red"))
        print("Install python3-tk (Linux) or use the CLI mode instead.")
        sys.exit(1)

    # ── setup ──
    root = tk.Tk()
    root.title(_("gui_title", lang))
    root.minsize(720, 560)
    root.geometry("860x640")
    _apply_oled_theme(root)

    # Variables
    current_lang = lang
    category_vars: dict[str, tk.BooleanVar] = {}
    categories = list_categories(current_lang)

    # ── Functions ──
    def toggle_lang() -> None:
        nonlocal current_lang
        current_lang = "tr" if current_lang == "en" else "en"
        _refresh_gui_text()

    def _refresh_gui_text() -> None:
        root.title(_("gui_title", current_lang))
        select_label.config(text=_("gui_select", current_lang))
        install_btn.config(text=_("gui_install", current_lang))
        cancel_btn.config(text=_("gui_cancel", current_lang))
        toggle_btn.config(text=_("gui_lang_toggle", current_lang))
        recommended_btn.config(
            text=f"{_('recommended', current_lang)} ({_('gui_recommended_hint', current_lang)})"
        )
        trusted_btn.config(
            text=f"{_('trusted', current_lang)} ({_('gui_trusted_hint', current_lang)})"
        )
        all_btn.config(text=f"{_('all', current_lang)} ({_('gui_all_hint', current_lang)})")

    def set_profile(profile: str) -> None:
        trusted_ids = {"K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"}
        data = load_config(current_lang)
        for cat in data.get("categories", []):
            cid = cat["id"]
            if profile == "all":
                checked = True
            elif profile == "trusted":
                checked = cid in trusted_ids
            elif profile == "recommended":
                has_per_repo = any(
                    r.get("recommended") is not None for r in cat.get("repos", [])
                )
                if cat.get("recommended") is False:
                    checked = False
                elif has_per_repo:
                    checked = any(
                        r.get("recommended") for r in cat.get("repos", [])
                    )
                else:
                    checked = True
            else:
                checked = False
            if cid in category_vars:
                category_vars[cid].set(checked)

    def run_install() -> None:
        selected = [cid for cid, var in category_vars.items() if var.get()]
        if not selected:
            return

        setup_logging(current_lang)
        install_btn.config(state="disabled", text=_("gui_installing", current_lang))
        cancel_btn.config(state="disabled")
        log_text.delete("1.0", tk.END)
        progress_bar["value"] = 0
        progress_bar["maximum"] = len(selected)

        data = load_config(current_lang)
        rows: list[tuple[str, str, str, str, str]] = []
        cat_map = {c["id"]: c for c in data.get("categories", [])}
        for cid in selected:
            cat = cat_map.get(cid)
            if not cat:
                continue
            for r in cat.get("repos", []):
                rows.append((cid, cat["name"], cat.get("color", "white"), r["repo"], r.get("subpath", "")))

        progress_bar["maximum"] = len(rows)
        ok_count = 0
        fail_count = 0
        fix_count = 0

        prev_id = ""
        for idx, (cat_id, cat_name, _, repo, subpath) in enumerate(rows):
            if cat_id != prev_id:
                prev_id = cat_id
                _gui_log(log_text, f"\n{'='*50}\n   {cat_id} — {cat_name}\n{'='*50}\n", "bold")
            _gui_log(log_text, f"  [{_('process', current_lang)}] {repo}" +
                     (f" -> {_('subpath', current_lang)} '{subpath}'" if subpath else "") +
                     " " + _('cloning', current_lang) + "\n", "blue")
            root.update_idletasks()

            sk_count, fx_count = process_repo(repo, subpath, current_lang)
            fix_count += fx_count
            if sk_count > 0:
                ok_count += 1
                _gui_log(log_text,
                         f"  [{_('ok', current_lang)}] {repo} -> {sk_count} {_('skills_extracted', current_lang)}\n",
                         "green")
            else:
                fail_count += 1

            progress_bar["value"] = idx + 1
            root.update_idletasks()

        progress_bar["value"] = progress_bar["maximum"]
        _gui_log(
            log_text,
            f"\n{'='*55}\n"
            f"  {_('gui_done', current_lang)}\n"
            f"  {_('gui_success', current_lang)} {ok_count}  "
            f"{_('gui_fail', current_lang)} {fail_count}  "
            f"{_('fixed', current_lang)}: {fix_count}\n"
            f"{'='*55}\n",
            "green",
        )

        save_tree(current_lang)
        if LOG_PATH:
            _gui_log(log_text, f"\n{_('log_saved', current_lang)}: {LOG_PATH}\n", "dim")

        install_btn.config(state="normal", text=_("gui_install", current_lang))
        cancel_btn.config(state="normal")

    def _gui_log(widget: tk.Text, msg: str, tag: str = "") -> None:
        if tag:
            widget.insert(tk.END, msg, tag)
        else:
            widget.insert(tk.END, msg)
        widget.see(tk.END)
        root.update_idletasks()

    # ── Top bar ──
    top_bar = tk.Frame(root, bg=OLED_BG_SEC, height=40)
    top_bar.pack(fill=tk.X)
    top_bar.pack_propagate(False)

    title_lbl = tk.Label(top_bar, text=_("gui_title", current_lang),
                         bg=OLED_BG_SEC, fg=OLED_ACCENT,
                         font=OLED_FONT_HEADER, anchor=tk.W)
    title_lbl.pack(side=tk.LEFT, padx=(16, 0), pady=8)

    toggle_btn = tk.Button(top_bar, text=_("gui_lang_toggle", current_lang),
                           command=toggle_lang,
                           bg=OLED_BG_CARD, fg=OLED_TEXT,
                           font=OLED_FONT_SMALL, relief="flat",
                           bd=0, padx=12, pady=4,
                           activebackground=OLED_BG_HOVER,
                           activeforeground=OLED_ACCENT,
                           cursor="hand2")
    toggle_btn.pack(side=tk.RIGHT, padx=12, pady=6)

    # ── Main content ──
    content = tk.Frame(root, bg=OLED_BG)
    content.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

    # ── Profile quick-select ──
    profile_frame = tk.Frame(content, bg=OLED_BG)
    profile_frame.pack(fill=tk.X, pady=(12, 0))

    select_label = tk.Label(profile_frame, text=_("gui_select", current_lang),
                            bg=OLED_BG, fg=OLED_TEXT,
                            font=OLED_FONT_HEADER, anchor=tk.W)
    select_label.pack(fill=tk.X, pady=(0, 8))

    profile_btn_frame = tk.Frame(profile_frame, bg=OLED_BG)
    profile_btn_frame.pack(fill=tk.X)

    btn_style = {"font": OLED_FONT_SMALL, "relief": "flat", "bd": 0,
                 "cursor": "hand2", "padx": 14, "pady": 6}

    recommended_btn = tk.Button(profile_btn_frame,
        text=f"{_('recommended', current_lang)} ({_('gui_recommended_hint', current_lang)})",
        command=lambda: set_profile("recommended"),
        bg=OLED_BG_CARD, fg=OLED_TEXT,
        activebackground=OLED_BG_HOVER, activeforeground=OLED_ACCENT,
        **btn_style)
    recommended_btn.pack(side=tk.LEFT, padx=(0, 6))

    trusted_btn = tk.Button(profile_btn_frame,
        text=f"{_('trusted', current_lang)} ({_('gui_trusted_hint', current_lang)})",
        command=lambda: set_profile("trusted"),
        bg=OLED_BG_CARD, fg=OLED_TEXT,
        activebackground=OLED_BG_HOVER, activeforeground=OLED_ACCENT,
        **btn_style)
    trusted_btn.pack(side=tk.LEFT, padx=(0, 6))

    all_btn = tk.Button(profile_btn_frame,
        text=f"{_('all', current_lang)} ({_('gui_all_hint', current_lang)})",
        command=lambda: set_profile("all"),
        bg=OLED_BG_CARD, fg=OLED_TEXT,
        activebackground=OLED_BG_HOVER, activeforeground=OLED_ACCENT,
        **btn_style)
    all_btn.pack(side=tk.LEFT)

    # ── Separator ──
    sep = tk.Frame(content, bg=OLED_BORDER, height=1)
    sep.pack(fill=tk.X, pady=(12, 8))

    # ── Category checkboxes (scrollable) ──
    canvas_frame = tk.Frame(content, bg=OLED_BG)
    canvas_frame.pack(fill=tk.BOTH, expand=True, pady=(4, 8))

    canvas = tk.Canvas(canvas_frame, bg=OLED_BG, highlightthickness=0,
                       bd=0, relief="flat")
    scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL,
                             bg=OLED_BG_CARD, troughcolor=OLED_BG,
                             activebackground=OLED_BORDER,
                             bd=0, relief="flat")
    scrollable = tk.Frame(canvas, bg=OLED_BG)

    scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable, anchor=tk.NW)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar.config(command=canvas.yview)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    for cat in categories:
        cid = cat["id"]
        desc = cat.get("description", "")
        var = tk.BooleanVar(value=False)
        category_vars[cid] = var

        row = tk.Frame(scrollable, bg=OLED_BG_SEC, bd=0,
                       highlightbackground=OLED_BORDER,
                       highlightthickness=1, highlightcolor=OLED_BORDER)
        row.pack(fill=tk.X, padx=0, pady=2)

        cb = tk.Checkbutton(row, text=f"  {cid} — {cat['name']}",
                            variable=var,
                            bg=OLED_BG_SEC, fg=OLED_TEXT,
                            selectcolor=OLED_BG,
                            activebackground=OLED_BG_HOVER,
                            activeforeground=OLED_TEXT,
                            font=OLED_FONT, relief="flat", bd=0,
                            cursor="hand2")
        cb.pack(side=tk.LEFT, padx=4, pady=4)
        if desc:
            desc_lbl = tk.Label(row, text=f"  {desc}",
                                bg=OLED_BG_SEC, fg=OLED_TEXT_SEC,
                                font=OLED_FONT_SMALL, anchor=tk.W)
            desc_lbl.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))

    # ── Progress bar ──
    progress_canvas = tk.Canvas(content, height=8, bg=OLED_BG,
                                highlightthickness=0, bd=0)
    progress_canvas.pack(fill=tk.X, pady=(0, 4))

    def _draw_progress(val: float = 0, maximum: float = 100) -> None:
        progress_canvas.delete("all")
        w = progress_canvas.winfo_width() - 2
        y = 1
        h = 6
        if w < 2:
            w = 200
        progress_canvas.create_rectangle(1, y, w + 1, y + h,
                                          outline=OLED_BORDER, fill=OLED_BG_SEC,
                                          width=0)
        if maximum > 0:
            fill_w = max(0, int(w * val / maximum))
            progress_canvas.create_rectangle(1, y, fill_w + 1, y + h,
                                              outline="", fill=OLED_ACCENT,
                                              width=0)

    progress_bar: dict[str, Any] = {"value": 0, "maximum": 100}
    progress_bar["_draw"] = _draw_progress

    # ── Log output (ScrolledText replacement with dark theme) ──
    log_frame = tk.Frame(content, bg=OLED_BG)
    log_frame.pack(fill=tk.BOTH, expand=True)

    log_text = tk.Text(log_frame, height=10, wrap=tk.WORD,
                       font=OLED_FONT_MONO, spacing1=1, spacing3=1)
    _dark_text_widget(log_text)
    log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    log_scroll = tk.Scrollbar(log_frame, orient=tk.VERTICAL,
                              command=log_text.yview,
                              bg=OLED_BG_CARD, troughcolor=OLED_BG,
                              activebackground=OLED_BORDER,
                              bd=0, relief="flat")
    log_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    log_text.config(yscrollcommand=log_scroll.set)

    # ── Bottom buttons ──
    btn_frame = tk.Frame(content, bg=OLED_BG)
    btn_frame.pack(fill=tk.X, pady=(8, 0))

    cancel_btn = tk.Button(btn_frame, text=_("gui_cancel", current_lang),
                           command=root.destroy,
                           bg="#21262d", fg=OLED_TEXT,
                           font=OLED_FONT, relief="flat", bd=0,
                           padx=20, pady=8, cursor="hand2",
                           activebackground=OLED_ERROR,
                           activeforeground="#ffffff")
    cancel_btn.pack(side=tk.RIGHT)

    install_btn = tk.Button(btn_frame, text=_("gui_install", current_lang),
                            command=run_install,
                            bg=OLED_ACCENT_DIM, fg=OLED_BG,
                            font=OLED_FONT_HEADER, relief="flat", bd=0,
                            padx=28, pady=8, cursor="hand2",
                            activebackground=OLED_ACCENT,
                            activeforeground=OLED_BG)
    install_btn.pack(side=tk.RIGHT, padx=(0, 10))

    # Override progress drawing on resize
    def _on_resize(_event=None):
        _draw_progress(progress_bar["value"], progress_bar["maximum"])
    root.bind("<Configure>", _on_resize)

    root.mainloop()


# ─────────────────────────────── ENTRY ───────────────────────────────

def _show_general_help(lang: str) -> None:
    lang = lang or "en"
    print()
    print(c(f"  {_('app_name', lang)}", "green"))
    print(f"  {_('desc', lang)}")
    print()
    print(f"  {_('usage', lang)}: python skills.py [target] [options]")
    print()
    print(f"  {_('profiles', lang).upper()}:")
    print(f"    recommended   {_('profile_recommended_desc', lang)}")
    print(f"    trusted       {_('profile_trusted_desc', lang)}")
    print(f"    all           {_('profile_all_desc', lang)}")
    print()
    print(f"  {_('categories', lang).upper()}:")
    for cat in list_categories(lang):
        print(f"    {cat['id']:<10} {cat['name']}")
    print()
    print(f"  {_('options', lang).upper()}:")
    print(f"    --gui       {_('gui', lang)}")
    print(f"    --lang tr   {_('lang', lang)}")
    print(f"    --dry-run   {_('dry_run', lang)}")
    print(f"    --prefix PATH {_('prefix', lang)}")
    print(f"    --uninstall {_('uninstall', lang)}")
    print(f"    --check     {_('check', lang)}")
    print(f"    --list      {_('list', lang)}")
    print(f"    --show-config {_('show_config', lang)}")
    print(f"    --readme    {_('readme', lang)}")
    print(f"    --changelog {_('changelog', lang)}")
    print(f"    --conduct   {_('conduct', lang)}")
    print(f"    --security  {_('security', lang)}")
    print(f"    --support   {_('support', lang)}")
    print(f"    --license   {_('license', lang)}")
    print(f"    --version   {_('version', lang)}")
    print(f"    --help      {_('help', lang)}")
    print()
    print(f"  {_('examples', lang)}:")
    print("    python skills.py                    # Install recommended (default)")
    print("    python skills.py trusted            # Install trusted")
    print("    python skills.py --gui              # Launch GUI")
    print("    python skills.py --lang tr          # Turkish CLI")
    print("    python skills.py K1 K5 K10          # Specific categories")
    print()


def _parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse args supporting multiple positional targets."""
    parser = argparse.ArgumentParser(
        prog="skills.py",
        add_help=False,
    )
    parser.add_argument("targets", nargs="*", default=[])
    parser.add_argument("--gui", action="store_true")
    parser.add_argument("--lang", choices=["en", "tr"], default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--prefix", type=str, default=None)
    parser.add_argument("--uninstall", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--show-config", action="store_true")
    parser.add_argument("--readme", action="store_true")
    parser.add_argument("--changelog", action="store_true")
    parser.add_argument("--conduct", action="store_true")
    parser.add_argument("--security", action="store_true")
    parser.add_argument("--support", action="store_true")
    parser.add_argument("--license", action="store_true")
    parser.add_argument("--version", action="store_true")
    parser.add_argument("--help", action="store_true")
    return parser.parse_args(argv)


def main() -> None:
    global SKILLS_DIR, AGENTS_DIR

    if sys.version_info < (3, 8):
        print(f"Error: {_('python_version', 'en')} {sys.version}")
        sys.exit(1)

    args = _parse_args(sys.argv[1:])
    lang = args.lang or _detect_lang()

    if args.help:
        _show_general_help(lang)
        return

    if args.gui:
        gui_main(args)
    elif args.list:
        setup_logging(lang)
        print(f"\n{_('available_categories', lang)}:")
        for cat in list_categories(lang):
            desc = cat.get("description", "")
            print(f"  {cat['id']:<6} {cat['name']:<20} {desc}")
        print()
    elif getattr(args, "show_config", False):
        print(json.dumps(REPOS, indent=2, ensure_ascii=False))
    elif args.check:
        pre_flight_check(lang)
    elif args.version:
        print(_("version_str", lang))
    elif args.uninstall:
        print()
        print(c(f"  {_('uninstall_confirm', lang)}: {SKILLS_DIR}", "red"))
        answer = input(c(f"  {_('proceed', lang)} ", "yellow")).strip().lower()
        if answer in ("y", "yes"):
            if SKILLS_DIR.is_dir():
                shutil.rmtree(SKILLS_DIR)
                print(c(f"  [{_('ok', lang)}] {_('uninstall_done', lang)}", "green"))
            else:
                print(c(f"  [{_('warn', lang)}] {SKILLS_DIR} {_('not_found', lang)}", "yellow"))
        else:
            print(c(f"  {_('uninstall_cancel', lang)}", "white"))
    else:
        doc_done = False
        for flag_name in ("readme", "changelog", "conduct", "security", "support", "license"):
            if getattr(args, flag_name, False):
                show_doc(flag_name, lang)
                doc_done = True
                break
        if doc_done:
            return

        alias_map = {
            "onerilen": "recommended",
            "guvenli": "trusted",
            "tumu": "all",
            "tum": "all",
        }
        targets = [alias_map.get(t.lower(), t) for t in args.targets] or ["recommended"]

        if args.dry_run:
            for target in targets:
                _dry_run_list(target, lang)
            return

        if args.prefix:
            SKILLS_DIR = Path(args.prefix).resolve()
            AGENTS_DIR = SKILLS_DIR.parent

        setup_logging(lang)
        total_ok = 0
        total_fail = 0
        total_fixes = 0

        for target in targets:
            titles = {
                "recommended": (f"  {_('recommended', lang).upper()} {_('categories', lang).upper()}", "green"),
                "trusted": (f"  {_('trusted', lang).upper()} {_('categories', lang).upper()} (K1-K8)", "cyan"),
                "all": (f"  {_('all', lang).upper()} {_('categories', lang).upper()} (K1-K10)", "magenta"),
            }
            if target in titles:
                print_header(titles[target][0], lang)
            else:
                print_header(f"  {target.upper()}", lang)

            ok, fail, fixes = install(target, lang)
            total_ok += ok
            total_fail += fail
            total_fixes += fixes

        final_report(total_ok, total_fail, total_fixes, lang)


if __name__ == "__main__":
    main()
