#!/usr/bin/env python3
"""
Agent Skills Project — cross-platform skill installer.
CLI + GUI, bilingual (EN/TR), zero external dependencies (stdlib only).

Usage:
  python skills.py                         Install recommended profile (default)
  python skills.py trusted                 Install trusted categories (K1-K8)
  python skills.py all                     Install all categories (K1-K10)
  python skills.py K1                      Install a single category
  python skills.py --gui                   Launch graphical interface
  python skills.py --lang tr               Force Turkish language
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
from pathlib import Path
from typing import Any

# ─────────────────────────────── I18N ───────────────────────────────

S: dict[str, dict[str, str]] = {
    "en": {
        "app_name": "Agent Skills Project",
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
        "version_str": "Agent Skills Project v1.0.0",
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
        "gui_title": "Agent Skills Project — Skill Installer",
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
    },
}


def _(key: str, lang: str = "en") -> str:
    return S.get(lang, S["en"]).get(key, key)


# ─────────────────────────────── EMBEDDED REPO DATA ───────────────────────────────

REPOS: dict[str, Any] = {
    "version": "1.0.0",
    "description": "Embedded repository registry for Agent Skills Project.",
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
    Returns (skill_count, fix_count).
    """
    safe_name = repo.replace("/", "-")
    tmpdir = Path(tempfile.mkdtemp(prefix=f"asp-{safe_name}-"))

    logging.info(f"[PROCESS] {repo} {_('cloning', lang)}")
    print(c(f"  [{_('process', lang)}] {repo} {_('cloning', lang)}", "blue"))

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
        cleanup(tmpdir)
        return 0, 0
    except subprocess.TimeoutExpired:
        logging.error(f"[ERROR] {repo} — {_('timeout', lang)}")
        print(c(f"  [{_('error', lang)}] {repo} — {_('timeout', lang)}", "red"))
        cleanup(tmpdir)
        return 0, 0

    if result.returncode != 0:
        logging.error(f"[ERROR] {repo} — {_('clone_failed', lang)}: {result.stderr.strip()}")
        print(c(f"  [{_('error', lang)}] {repo} — {_('clone_failed', lang)}", "red"))
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


# ─────────────────────────────── INSTALL FROM LIST ───────────────────────────────

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

    prev_id = ""
    prev_name = ""
    prev_color = ""
    cat_ok = 0
    cat_fail = 0
    total_ok = 0
    total_fail = 0
    total_fixes = 0

    for cat_id, cat_name, cat_color, repo, subpath in rows:
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
                f"  [{_('process', lang)}] {repo}"
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

    save_tree(lang)
    if LOG_PATH:
        print(c(f"  {_('log_saved', lang)}: {LOG_PATH}", "white"))


# ─────────────────────────────── GUI ───────────────────────────────

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
    root.minsize(700, 500)
    root.geometry("800x600")

    # Try to set icon
    try:
        root.iconbitmap(default="")
    except Exception:
        pass

    # ── Variables ──
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

        # Collect repos for selected categories
        data = load_config(current_lang)
        rows: list[tuple[str, str, str, str, str]] = []
        cat_map = {c["id"]: c for c in data.get("categories", [])}
        for cid in selected:
            cat = cat_map.get(cid)
            if not cat:
                continue
            cat_color = cat.get("color", "white")
            for r in cat.get("repos", []):
                rows.append((cid, cat["name"], cat_color, r["repo"], r.get("subpath", "")))

        progress_bar["maximum"] = len(rows)
        ok_count = 0
        fail_count = 0
        fix_count = 0

        prev_id = ""
        for idx, (cat_id, cat_name, _, repo, subpath) in enumerate(rows):
            if cat_id != prev_id:
                prev_id = cat_id
                _gui_log(
                    log_text,
                    f"\n{'='*50}\n     {cat_id} — {cat_name}\n{'='*50}\n",
                    "blue",
                )
            _gui_log(log_text, f"  [{_('process', current_lang)}] {repo}" +
                     (f" -> {_('subpath', current_lang)} '{subpath}'" if subpath else "") +
                     " " + _('cloning', current_lang) + "\n", "blue")
            root.update_idletasks()

            sk_count, fx_count = process_repo(repo, subpath, current_lang)
            fix_count += fx_count
            if sk_count > 0:
                ok_count += 1
                _gui_log(log_text, f"  [{_('ok', current_lang)}] {repo} -> {sk_count} {_('skills_extracted', current_lang)}\n", "green")
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
            _gui_log(log_text, f"\n{_('log_saved', current_lang)}: {LOG_PATH}\n", "white")

        install_btn.config(state="normal", text=_("gui_install", current_lang))
        cancel_btn.config(state="normal")

    def _gui_log(widget: tk.Text, msg: str, color: str = "") -> None:
        widget.insert(tk.END, msg)
        widget.see(tk.END)
        root.update_idletasks()

    # ── Layout ──
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Top bar: lang toggle
    top_frame = ttk.Frame(main_frame)
    top_frame.pack(fill=tk.X, pady=(0, 5))
    toggle_btn = ttk.Button(top_frame, text=_("gui_lang_toggle", current_lang), command=toggle_lang)
    toggle_btn.pack(side=tk.RIGHT)

    # Select label
    select_label = ttk.Label(main_frame, text=_("gui_select", current_lang), font=("", 10, "bold"))
    select_label.pack(anchor=tk.W, pady=(0, 5))

    # Profile quick-select buttons
    profile_frame = ttk.Frame(main_frame)
    profile_frame.pack(fill=tk.X, pady=(0, 5))
    recommended_btn = ttk.Button(
        profile_frame,
        text=f"{_('recommended', current_lang)} ({_('gui_recommended_hint', current_lang)})",
        command=lambda: set_profile("recommended"),
    )
    recommended_btn.pack(side=tk.LEFT, padx=(0, 5))
    trusted_btn = ttk.Button(
        profile_frame,
        text=f"{_('trusted', current_lang)} ({_('gui_trusted_hint', current_lang)})",
        command=lambda: set_profile("trusted"),
    )
    trusted_btn.pack(side=tk.LEFT, padx=(0, 5))
    all_btn = ttk.Button(
        profile_frame,
        text=f"{_('all', current_lang)} ({_('gui_all_hint', current_lang)})",
        command=lambda: set_profile("all"),
    )
    all_btn.pack(side=tk.LEFT)

    # Category checkboxes in a scrollable frame
    canvas_frame = ttk.Frame(main_frame)
    canvas_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 5))

    canvas = tk.Canvas(canvas_frame, highlightthickness=0)
    scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable = ttk.Frame(canvas)

    scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable, anchor=tk.NW)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Enable mousewheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    for cat in categories:
        cid = cat["id"]
        desc = cat.get("description", "")
        var = tk.BooleanVar(value=False)
        category_vars[cid] = var
        cb = ttk.Checkbutton(
            scrollable,
            text=f"{cid} — {cat['name']}" + (f"  ({desc})" if desc else ""),
            variable=var,
        )
        cb.pack(anchor=tk.W, padx=5, pady=1)

    # Progress bar
    progress_bar = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, mode="determinate")
    progress_bar.pack(fill=tk.X, pady=(5, 5))

    # Log output
    log_text = scrolledtext.ScrolledText(main_frame, height=12, font=("Consolas", 9), wrap=tk.WORD)
    log_text.pack(fill=tk.BOTH, expand=True)

    # Bottom buttons
    btn_frame = ttk.Frame(main_frame)
    btn_frame.pack(fill=tk.X, pady=(5, 0))
    cancel_btn = ttk.Button(btn_frame, text=_("gui_cancel", current_lang), command=root.destroy)
    cancel_btn.pack(side=tk.RIGHT)
    install_btn = ttk.Button(btn_frame, text=_("gui_install", current_lang), command=run_install)
    install_btn.pack(side=tk.RIGHT, padx=(0, 5))

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
    args = _parse_args(sys.argv[1:])
    lang = args.lang or _detect_lang()

    if args.help or (len(sys.argv) == 1 and not args.targets and not args.gui and not args.list and not args.version
                     and not getattr(args, "show_config", False) and not args.readme and not args.changelog
                     and not args.conduct and not args.security and not args.support and not args.license):
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
    elif args.version:
        print(_("version_str", lang))
    else:
        doc_done = False
        for flag_name in ("readme", "changelog", "conduct", "security", "support", "license"):
            if getattr(args, flag_name, False):
                show_doc(flag_name, lang)
                doc_done = True
                break
        if doc_done:
            return
        setup_logging(lang)
        alias_map = {
            "onerilen": "recommended",
            "guvenli": "trusted",
            "tumu": "all",
            "tum": "all",
        }
        targets = [alias_map.get(t.lower(), t) for t in args.targets] or ["recommended"]
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
