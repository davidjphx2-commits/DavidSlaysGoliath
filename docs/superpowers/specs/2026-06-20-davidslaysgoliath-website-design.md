---
title: davidslaysgoliath.com — Design Spec
date: 2026-06-20
status: approved
---

# davidslaysgoliath.com — Apologetics Website

## Purpose

Theological/apologetics website. Owned domain, DNS already pointed at David's VPS. Goal: clear, doctrinally grounded content on the gospel, finding a sound church, studying the Bible, and living the Christian life — written for a seeker or new believer audience, with an apologetic (faith-defending) tone throughout.

## Stack

Plain HTML/CSS, no framework, no CMS. Same pattern as `stratum137.com`:

- **Source repo:** new GitHub repo `davidjphx2-commits/davidslaysgoliath-website`
- **Local project:** `D:\Theology\Projects\davidslaysgoliath-website\`
- **Deploy:** Coolify static site (nginx:alpine), domain `https://davidslaysgoliath.com` (and `www`), auto-deploy on push to `main`
- **VPS:** same box as stratum137.com (`2.25.204.242`, Coolify v4.1.2, Traefik reverse proxy) — see `D:\Vault\wiki\stratum137\infrastructure\vps-server-reference.md`
- **Gotcha to respect:** Coolify domain field must NOT include a port suffix; click **Save** before **Deploy** or the auto-generated subdomain reappears (see `vps-traefik-routing.md` / `stratum137-website.md`)
- **Update workflow:** David asks for a text/page change → Claude edits the file → `git add -A && git commit && git push` → Coolify auto-redeploys. No self-service CMS editing.

## Visual Design

- **Palette (chosen: Option A)** — sand/tan base `#D9C9A3`, dusk-blue accent `#1F3A52`, warm dark-brown text `#3B2F1E`, secondary bronze `#8C6A3F`
- **Hero image:** public-domain classical art depicting David and Goliath in battle (not the aftermath/decapitation imagery — keep front-page tone confrontational-but-not-gory). Leading candidate: Gustave Doré's 19th-century engraving of David and Goliath. Exact image sourced and licensed-confirmed during implementation (public domain, line-engraving works well against the tan/dusk-blue palette).
- **Typography:** serif for headlines/scripture quotes (gravitas, editorial feel), sans-serif for body copy (readability)
- **Tone:** calm, confident, doctrinally serious — not flashy, not corporate
- **Hero headline:** "A Man After God's Own Heart" with subtitle "Unwavering Faith"

## Site Structure

| Page | File | Content |
|------|------|---------|
| Home | `index.html` | Hero image with headline "A Man After God's Own Heart" / subtitle "Unwavering Faith", short intro, nav links to the 4 content pages |
| The Gospel | `gospel.html` | What the gospel is, sin/separation from God, Christ's atonement, what it means to be saved, having a relationship with God |
| Finding a Good Church | `finding-a-church.html` | Principles for vetting a church: adherence to core biblical doctrines (Scripture authority, Trinity, deity of Christ, salvation by grace through faith, etc.), expository preaching as a primary marker, red flags to avoid |
| How to Study the Bible | `studying-the-bible.html` | New-believer-level guide: where to start, basic hermeneutics (context, audience, genre), recommended reading order, avoiding common pitfalls (proof-texting, isolating verses) |
| Living the Christian Life | `christian-life.html` | Practical discipleship: prayer, fellowship, obedience, sanctification, dealing with struggle/doubt |

Shared layout: header with site name + nav (Home / Gospel / Find a Church / Study the Bible / Christian Life), footer with simple copyright + maybe a contact/about line.

## Content Approach

David has stated the topical scope for each page (above). Actual prose will be drafted collaboratively — Claude drafts each page's content from sound Reformed/evangelical doctrinal grounding (consistent with David's stated theology — Reformed, RC Sproul-aligned, expository-preaching emphasis), David reviews and edits for tone/accuracy before publishing.

## Out of Scope (this phase)

- No CMS / admin panel
- No comments, forums, or user accounts
- No blog/article system (may be a future addition, not in this build)
- No multi-language support
