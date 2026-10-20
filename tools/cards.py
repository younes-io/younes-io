"""Writes the profile cards in cards/, one light and one dark SVG each."""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "cards"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

THEMES = {
    "light": dict(bg="#ffffff", border="#d1d9e0", text="#1f2328", muted="#59636e", link="#0969da"),
    "dark": dict(bg="#0d1117", border="#3d444d", text="#f0f6fc", muted="#9198a1", link="#4493f8"),
}

CARDS = [
    ("mdust", "Markdown → HTML", ["Byte-identical to markdown-it,", "about 10× faster."], "Rust · Wasm", "#dea584"),
    ("agent-skills", "intent → TLA⁺ → ⊢", ["Skills for TLA⁺ specs and", "TLAPS proofs, machine-checked."], "TLA⁺", "#8f6bd8"),
    ("devnull", "tty → /dev/null", ["Claude Code plugins.", "/screensaver until Esc."], "Claude Code", "#d97757"),
    ("vscode-tlaplus", "TLA⁺ → VS Code", ["Coverage heat maps and", "go-to-definition."], "TypeScript", "#3178c6"),
    ("CommunityModules", "TLA⁺ ⇄ CBOR", ["Reads and writes TLA⁺", "values as CBOR."], "TLA⁺", "#8f6bd8"),
    ("cargo-wizard", "rustc → sccache rustc", ["sccache as a compiler", "wrapper option."], "Rust", "#dea584"),
]


def card(name, sig, lines, lang, dot, t):
    body = "".join(
        f'<text x="20" y="{80 + i * 19}" font-family="{SANS}" font-size="13" fill="{t["text"]}">{escape(l)}</text>'
        for i, l in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="270" height="150" viewBox="0 0 270 150">
<rect x="0.5" y="0.5" width="269" height="149" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>
<text x="20" y="34" font-family="{MONO}" font-size="15" font-weight="600" fill="{t["link"]}">{escape(name)}</text>
<text x="20" y="55" font-family="{MONO}" font-size="12" fill="{t["muted"]}">: {escape(sig)}</text>
{body}
<circle cx="25" cy="126" r="4.5" fill="{dot}"/>
<text x="36" y="130" font-family="{SANS}" font-size="12" fill="{t["muted"]}">{escape(lang)}</text>
</svg>
'''


def header(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="820" height="96" viewBox="0 0 820 96">
<text x="410" y="58" text-anchor="middle" font-family="{MONO}" font-size="30" fill="{t["text"]}">⟦ software ⟧ <tspan fill="{t["muted"]}">≜</tspan> semantics</text>
</svg>
'''


for theme, t in THEMES.items():
    (OUT / f"header-{theme}.svg").write_text(header(t))
    for name, *rest in CARDS:
        (OUT / f"{name}-{theme}.svg").write_text(card(name, *rest, t))
