# Next.js + Tailwind notes

Notes only; do not scaffold a full app unless asked. Node is available on this machine (v24).

## Files to bring in
- `templates/tokens.css` -> `app/rex-tokens.css` (change `--hero-art` URLs to `/graphics/...`).
- `templates/tailwind.config.js` -> `rex.tailwind.js` (v3 preset), or the v4 `@theme` block below.
- Public assets: `python .claude/skills/rex-website/scripts/copy_assets.py ./public` (icons, manifest, logos, graphics).
- OG: render to `public/og-image.png` with `scripts/render_og.py`, or use `app/opengraph-image.tsx` with the same layout.

## Fonts (next/font, self-hosted, swap)
```tsx
// app/fonts.ts
import { Space_Grotesk, IBM_Plex_Mono } from "next/font/google";
export const display = Space_Grotesk({ subsets: ["latin"], weight: ["500", "700"], display: "swap", variable: "--font-display" });
export const mono = IBM_Plex_Mono({ subsets: ["latin"], weight: ["400", "500"], display: "swap", variable: "--font-mono" });
```
Remove the Google Fonts `<link>` from the head snippet when using next/font.

## Layout with theme handling
```tsx
// app/layout.tsx
import "./rex-tokens.css";
import "./globals.css";
import { display, mono } from "./fonts";
import type { Metadata, Viewport } from "next";

export const metadata: Metadata = {
  metadataBase: new URL("https://rex.example"),
  title: { default: "REX Cybersecurity | Resilience · Engineering · eXclusion", template: "%s | REX Cybersecurity" },
  description: "Defence-led security research, detection engineering, offensive testing and education.",
  icons: { icon: [{ url: "/favicon.ico", sizes: "48x48" }, { url: "/favicon.svg", type: "image/svg+xml" }], apple: "/apple-touch-icon.png" },
  manifest: "/site.webmanifest",
  openGraph: { siteName: "REX Cybersecurity", images: [{ url: "/og-image.png", width: 1200, height: 630, alt: "REX Cybersecurity logo on obsidian with blue and violet diagonal cuts." }] },
  twitter: { card: "summary_large_image" },
};
export const viewport: Viewport = {
  colorScheme: "dark light",
  themeColor: [{ media: "(prefers-color-scheme: dark)", color: "#09090B" }, { media: "(prefers-color-scheme: light)", color: "#FFFFFF" }],
};

const themeScript = `(function(){try{var t=localStorage.getItem("rex-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}catch(e){}})();`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-GB" className={`${display.variable} ${mono.variable}`} suppressHydrationWarning>
      <head><script dangerouslySetInnerHTML={{ __html: themeScript }} /></head>
      <body className="bg-bg text-text font-sans">{children}</body>
    </html>
  );
}
```
`--font-display`/`--font-mono` from next/font override the token fallbacks automatically because the class sits on `<html>`.

## Theme toggle (client component)
```tsx
"use client";
import { useEffect, useState } from "react";
type Theme = "dark" | "light";
const resolve = (): Theme =>
  (document.documentElement.dataset.theme as Theme | undefined) ??
  (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");

export const ThemeToggle = () => {
  const [theme, setTheme] = useState<Theme | null>(null);
  useEffect(() => setTheme(resolve()), []);
  const next: Theme = theme === "light" ? "dark" : "light";
  const toggle = () => {
    document.documentElement.dataset.theme = next;
    localStorage.setItem("rex-theme", next);
    setTheme(next);
  };
  return (
    <button type="button" onClick={toggle} aria-label={`Switch to ${next} theme`}
      className="grid size-11 place-items-center border border-border-strong text-text hover:border-accent focus-visible:outline-2 focus-visible:outline-focus">
      {/* sun / moon SVGs from templates/portfolio/index.html */}
    </button>
  );
};
```

## Tailwind v3
```js
// tailwind.config.js
module.exports = { presets: [require("./rex.tailwind.js")], content: ["./app/**/*.{ts,tsx,mdx}", "./components/**/*.{ts,tsx}"] };
```

## Tailwind v4 (CSS-first)
```css
/* app/globals.css */
@import "tailwindcss";
@import "./rex-tokens.css";
@custom-variant dark (&:where([data-theme="dark"], [data-theme="dark"] *));
@theme inline {
  --color-bg: var(--bg);              --color-bg-raised: var(--bg-raised);
  --color-surface: var(--surface);    --color-surface-2: var(--surface-2);
  --color-border: var(--border);      --color-border-strong: var(--border-strong);
  --color-text: var(--text);          --color-text-muted: var(--text-muted);
  --color-heading: var(--heading);
  --color-accent: var(--accent);      --color-accent-hover: var(--accent-hover);  --color-accent-text: var(--accent-text);
  --color-accent-2: var(--accent-2);  --color-accent-2-text: var(--accent-2-text);
  --color-on-accent: var(--on-accent); --color-focus: var(--focus);
  --color-rex-obsidian: #09090B; --color-rex-indigo: #312E81; --color-rex-blue: #2563EB; --color-rex-purple: #A855F7;
  --font-display: var(--font-display); --font-sans: Arial, Helvetica, sans-serif; --font-mono: var(--font-mono);
  --text-display: var(--step-display); --text-h2: var(--step-h2); --text-label: 0.75rem;
  --radius: 2px;
}
@utility cut-both { clip-path: polygon(0 var(--cut), 100% 0, 100% calc(100% - var(--cut)), 0 100%); }
@utility cut-bottom { clip-path: polygon(0 0, 100% 0, 100% calc(100% - var(--cut)), 0 100%); }
@utility chamfer { clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 0 100%); }
```

## Component mapping
Port `templates/portfolio/index.html` sections 1:1 into `components/` (Header, Hero, About, Services, ResearchCard, Terminal, Timeline, Contact, Footer). Keep the card two-layer border CSS from `styles.css` as a small CSS module or `@layer components` rule; Tailwind borders do not follow clip-path chamfers.
Write-ups: MDX with frontmatter (title, date, tags, attack_ids, summary) rendering into `ResearchCard`; generate `TechArticle` JSON-LD per post.
Verify with `python .claude/skills/rex-website/scripts/shoot.py http://localhost:3000/ samples --prefix next`.
