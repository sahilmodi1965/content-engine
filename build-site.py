#!/usr/bin/env python3
"""Build a single self-contained index.html dashboard from the engine's source files.
Run this anytime: `python3 build-site.py`. It reads scripts/, narrative-bank.md,
runs.jsonl and higgsfield/ and regenerates index.html. The HTML is the readable
source of truth — open it in a browser to understand everything at a glance.
"""
import os, re, json, html, glob

BASE = os.path.dirname(os.path.abspath(__file__))
ANGLES = [
    ("1-pdf", "$100 PDF", "stepaheadco.com/ship · global scale", "#2563eb"),
    ("2-webinar", "Webinar", "100 AED bi-weekly · recurring income", "#7c3aed"),
    ("3-automation", "Automation", "build-in-public · business owners", "#0891b2"),
    ("4-bigticket", "Big-Ticket", "company-transformation consulting", "#b45309"),
]
LEV_BADGE = {"high": ("🟢 high", "#16a34a"), "medium": ("🟡 medium", "#ca8a04"), "low": ("⚪ low", "#6b7280")}

def esc(s): return html.escape(s or "")

def md_inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s

def md_to_html(md):
    out, in_ul = [], False
    for line in md.splitlines():
        if re.match(r"^\s*[-*] ", line):
            if not in_ul: out.append("<ul>"); in_ul = True
            out.append("<li>" + md_inline(line.split(" ", 1)[1] if " " in line.strip() else "") + "</li>")
            continue
        if in_ul: out.append("</ul>"); in_ul = False
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1)); out.append(f"<h{lvl+1}>{md_inline(m.group(2))}</h{lvl+1}>"); continue
        if line.strip() == "": out.append(""); continue
        if line.strip().startswith(">"): out.append("<blockquote>" + md_inline(line.strip()[1:].strip()) + "</blockquote>"); continue
        out.append("<p>" + md_inline(line) + "</p>")
    if in_ul: out.append("</ul>")
    return "\n".join(out)

def parse_script(path):
    txt = open(path, encoding="utf-8").read()
    title = re.search(r"^#\s+(.*)$", txt, re.M)
    angle = re.search(r"\*\*Angle:\*\*\s*([a-z]+)", txt)
    lev = re.search(r"\*\*Leverage:\*\*\s*([a-z]+)", txt)
    hook = re.search(r"\*\*Hook[^:]*:\*\*\s*(.*)", txt)
    cta = re.search(r"\*\*CTA[^:]*:\*\*\s*(.*)", txt)
    return {
        "title": title.group(1).strip() if title else os.path.basename(path),
        "angle": angle.group(1) if angle else "",
        "lev": (lev.group(1) if lev else "low").strip(),
        "hook": hook.group(1).strip() if hook else "",
        "cta": (cta.group(1).strip() if cta else ""),
        "body": txt, "rel": os.path.relpath(path, BASE),
    }

# ---- gather ----
runs = [json.loads(l) for l in open(os.path.join(BASE, "council/runs.jsonl")) if l.strip()]
last = runs[-1] if runs else {}
scripts_by_angle = {}
total = 0
for slug, *_ in ANGLES:
    files = sorted(glob.glob(os.path.join(BASE, "scripts", slug, "*.md")))
    scripts_by_angle[slug] = [parse_script(f) for f in files]
    total += len(files)

bank = ""
bp = os.path.join(BASE, "narrative-bank.md")
if os.path.exists(bp): bank = open(bp, encoding="utf-8").read()
# strip the TOC-heavy top, keep from first angle heading
voice = ""
vp = os.path.join(BASE, "voice-profile.md")
if os.path.exists(vp): voice = open(vp, encoding="utf-8").read()

hig = ""
hp = os.path.join(BASE, "higgsfield/test-reel/TEST-REEL.md")
if os.path.exists(hp): hig = open(hp, encoding="utf-8").read()

productions = []
pp = os.path.join(BASE, "higgsfield/productions.jsonl")
if os.path.exists(pp):
    productions = [json.loads(l) for l in open(pp, encoding="utf-8") if l.strip()]

# headline proof from sprint
proof = []
sp = os.path.join(BASE, "CONTENT-SPRINT.md")
if os.path.exists(sp):
    s = open(sp, encoding="utf-8").read()
    m = re.search(r"Headline proof.*?\n(.*?)\n##", s, re.S)
    if m: proof = [md_inline(x[2:]) for x in m.group(1).splitlines() if x.strip().startswith("- ")]

# ---- render ----
def script_card(sc):
    badge, col = LEV_BADGE.get(sc["lev"], LEV_BADGE["low"])
    return f"""
    <details class="card">
      <summary>
        <span class="lev" style="background:{col}1a;color:{col}">{badge}</span>
        <span class="ctitle">{esc(sc['title'])}</span>
      </summary>
      <div class="hook">🎯 {esc(sc['hook'])}</div>
      <div class="cta">📣 {esc(sc['cta'])}</div>
      <div class="body">{md_to_html(sc['body'])}</div>
      <a class="filelink" href="{esc(sc['rel'])}">{esc(sc['rel'])}</a>
    </details>"""

angle_sections = []
nav = []
for slug, name, sub, col in ANGLES:
    cards = "".join(script_card(s) for s in scripts_by_angle[slug])
    n = len(scripts_by_angle[slug])
    nav.append(f'<a href="#{slug}" style="border-color:{col}"><b>{name}</b><span>{n}</span></a>')
    angle_sections.append(f"""
    <section id="{slug}" class="angle">
      <h2 style="border-color:{col}"><span style="color:{col}">●</span> {esc(name)} <small>{esc(sub)} · {n} scripts</small></h2>
      {cards}
    </section>""")

proof_html = "".join(f"<li>{p}</li>" for p in proof)
ang = last.get("angles", {})
updated = last.get("ts", "")

HTML = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sahil's Content Engine</title>
<style>
:root{{--bg:#0b0e14;--card:#141925;--ink:#e6e9ef;--mut:#8b93a7;--line:#222a3a;--accent:#3b82f6}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif}}
.wrap{{max-width:920px;margin:0 auto;padding:28px 20px 80px}}
header h1{{font-size:30px;margin:0 0 4px}}
.sub{{color:var(--mut);margin:0 0 18px}}
.stats{{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}}
.stat{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px;min-width:96px}}
.stat b{{font-size:22px;display:block}}
.stat span{{color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.04em}}
nav{{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0 26px;position:sticky;top:0;background:var(--bg);padding:10px 0;z-index:5}}
nav a{{flex:1;min-width:120px;text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--line);border-left:3px solid;border-radius:10px;padding:8px 12px;display:flex;justify-content:space-between;align-items:center}}
nav a span{{color:var(--mut);font-variant-numeric:tabular-nums}}
.panel{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:16px 0}}
.panel h3{{margin:0 0 10px}}
.proof li{{margin:8px 0;color:#cfd5e2}}
.angle h2{{border-left:3px solid;padding-left:12px;font-size:21px;margin:34px 0 14px}}
.angle h2 small{{color:var(--mut);font-weight:400;font-size:13px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:10px 0;padding:0 16px}}
.card summary{{cursor:pointer;padding:14px 0;display:flex;gap:10px;align-items:center;list-style:none}}
.card summary::-webkit-details-marker{{display:none}}
.card summary::before{{content:"▸";color:var(--mut);transition:.15s}}
.card[open] summary::before{{transform:rotate(90deg)}}
.ctitle{{font-weight:600}}
.lev{{font-size:11px;padding:3px 8px;border-radius:20px;white-space:nowrap;font-weight:600}}
.hook{{color:#dbeafe;background:#1d283a;border-radius:8px;padding:8px 12px;margin:4px 0 8px;font-size:14px}}
.cta{{color:#bbf7d0;background:#11261b;border-radius:8px;padding:8px 12px;margin:0 0 12px;font-size:14px}}
.body{{border-top:1px solid var(--line);padding-top:10px;font-size:14.5px}}
.body h2,.body h3{{font-size:15px;color:#aeb6c9;margin:14px 0 4px}}
.body code{{background:#0b0e14;padding:1px 5px;border-radius:4px;font-size:13px;color:#9ece6a}}
.filelink{{display:inline-block;margin:10px 0 16px;color:var(--mut);font-size:12px;text-decoration:none}}
blockquote{{border-left:3px solid var(--line);margin:8px 0;padding-left:12px;color:var(--mut)}}
details.big>summary{{font-weight:600;cursor:pointer;padding:6px 0}}
a{{color:var(--accent)}}
.prod{{display:flex;gap:14px;align-items:flex-start;margin:12px 0;flex-wrap:wrap}}
.prod video{{width:200px;max-width:48vw;border-radius:10px;background:#000;border:1px solid var(--line)}}
.prodmeta{{flex:1;min-width:200px}}
.prodmeta b{{display:block;margin-bottom:6px}}
.pnote{{color:var(--mut);font-size:13px;margin-top:6px}}
footer{{color:var(--mut);font-size:13px;margin-top:40px;border-top:1px solid var(--line);padding-top:16px}}
</style></head><body><div class="wrap">
<header>
  <h1>Sahil's Content Engine</h1>
  <p class="sub">My standing PR team as code — every story, script and CTA in one page. Updated {esc(updated)}.</p>
</header>
<div class="stats">
  <div class="stat"><b>{total}</b><span>scripts</span></div>
  <div class="stat"><b>{ang.get('pdf','-')}</b><span>PDF</span></div>
  <div class="stat"><b>{ang.get('webinar','-')}</b><span>Webinar</span></div>
  <div class="stat"><b>{ang.get('automation','-')}</b><span>Automation</span></div>
  <div class="stat"><b>{ang.get('bigticket','-')}</b><span>Big-ticket</span></div>
  <div class="stat"><b>{len(runs)}</b><span>runs</span></div>
</div>
<nav>{''.join(nav)}</nav>
<div class="panel proof"><h3>🔥 Headline proof — your strongest receipts</h3><ul>{proof_html}</ul></div>
{('<div class="panel"><h3>🎞️ Productions — rendered Higgsfield reels</h3>' + ''.join('<div class="prod"><video controls preload="metadata" poster="' + esc(p.get('still_url','')) + '" src="' + esc(p.get('clip_url','')) + '"></video><div class="prodmeta"><b>' + esc(p.get('title','')) + '</b><span class="lev" style="background:#2563eb1a;color:#2563eb">' + esc(p.get('angle','')) + '</span><div class="pnote">' + esc(p.get('status','')) + ' · ' + str(p.get('credits','')) + ' cr · ' + esc(p.get('date','')) + '</div><div class="pnote">' + esc(p.get('note','')) + '</div></div></div>' for p in productions) + '</div>') if productions else ''}
<div class="panel"><h3>🎬 Higgsfield channel — staged test</h3>
  <p style="color:var(--mut);margin:.2em 0">Soul-ID AI reels with your real VO. Spend-gated: cheap stills → review → hardest motion shot → review + cost → render. One test reel staged, awaiting your review &amp; <code>SOUL_UUID</code>.</p>
  <details class="big"><summary>Open test-reel spec</summary><div class="body">{md_to_html(hig)}</div></details>
</div>
{''.join(angle_sections)}
<div class="panel"><h3>📚 Narrative bank <small style="color:var(--mut);font-weight:400">— append-only, compounds each run</small></h3>
  <details class="big"><summary>Open the full bank</summary><div class="body">{md_to_html(bank)}</div></details>
</div>
<div class="panel"><h3>🗣️ Voice profile</h3>
  <details class="big"><summary>How the engine writes as you</summary><div class="body">{md_to_html(voice)}</div></details>
</div>
<footer>Generated by <code>build-site.py</code> from the repo's source files. Run it after every engine run to refresh. Priority order: PDF → Webinar → Automation → Big-ticket.</footer>
</div></body></html>"""

open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(HTML)
print(f"Wrote index.html — {total} scripts, {len(runs)} runs, {len(proof)} proof points.")
