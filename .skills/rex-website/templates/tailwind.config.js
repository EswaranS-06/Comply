/** REX Tailwind preset (v3 syntax; for v4 see references/nextjs.md).
 * Colours point at the CSS variables in tokens.css, so dark/light switch at runtime with no rebuild.
 * Usage: module.exports = { presets: [require("./tailwind.config.js")], content: [...] }
 * Dark mode: tokens.css already swaps semantic colours. Use `dark:` only for rare per-theme overrides;
 * the selector strategy below matches the [data-theme] attribute set by the theme toggle. */
module.exports = {
  darkMode: ["selector", '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        rex: {
          obsidian: "#09090B",
          indigo: "#312E81",
          blue: { DEFAULT: "#2563EB", 400: "#89B1FE", 500: "#6D9DFD", 800: "#184EC7" },
          purple: { DEFAULT: "#A855F7", 400: "#C79BFE", 700: "#902DE0" },
          white: "#FFFFFF",
        },
        bg: "var(--bg)",
        "bg-raised": "var(--bg-raised)",
        surface: { DEFAULT: "var(--surface)", 2: "var(--surface-2)" },
        border: { DEFAULT: "var(--border)", strong: "var(--border-strong)" },
        text: { DEFAULT: "var(--text)", muted: "var(--text-muted)" },
        heading: "var(--heading)",
        accent: { DEFAULT: "var(--accent)", hover: "var(--accent-hover)", text: "var(--accent-text)" },
        "accent-2": { DEFAULT: "var(--accent-2)", text: "var(--accent-2-text)" },
        "on-accent": "var(--on-accent)",
        depth: "var(--depth)",
        focus: "var(--focus)",
        code: { bg: "var(--code-bg)", text: "var(--code-text)" },
      },
      fontFamily: {
        display: ['"Space Grotesk"', "system-ui", "sans-serif"],
        sans: ["Arial", "Helvetica", "sans-serif"],
        mono: ['"IBM Plex Mono"', "ui-monospace", "Consolas", "monospace"],
      },
      fontSize: {
        display: ["var(--step-display)", { lineHeight: "1.05", letterSpacing: "0.02em" }],
        h1: ["var(--step-h1)", { lineHeight: "1.05", letterSpacing: "0.02em" }],
        h2: ["var(--step-h2)", { lineHeight: "1.1", letterSpacing: "0.02em" }],
        h3: ["var(--step-h3)", { lineHeight: "1.2" }],
        body: ["1.125rem", { lineHeight: "1.5" }],
        small: ["0.875rem", { lineHeight: "1.45", letterSpacing: "0.01em" }],
        label: ["0.75rem", { lineHeight: "1.3", letterSpacing: "0.04em" }],
      },
      spacing: { section: "var(--section-pad)", cut: "var(--cut)", gutter: "var(--gutter)", page: "var(--page-pad)" },
      maxWidth: { container: "76rem" },
      borderRadius: { DEFAULT: "2px" },
      backgroundImage: {
        "rex-gradient": "linear-gradient(120deg, #2563EB 0%, #5145E8 55%, #A855F7 100%)",
        "rex-dots": "radial-gradient(var(--dot) 1.2px, transparent 1.6px)",
      },
      transitionTimingFunction: { rex: "cubic-bezier(0.2, 0.7, 0.2, 1)" },
    },
  },
  plugins: [
    // Motif utilities: diagonal cut sections and chamfered frames.
    function ({ addUtilities }) {
      addUtilities({
        ".cut-both": { clipPath: "polygon(0 var(--cut), 100% 0, 100% calc(100% - var(--cut)), 0 100%)" },
        ".cut-bottom": { clipPath: "polygon(0 0, 100% 0, 100% calc(100% - var(--cut)), 0 100%)" },
        ".chamfer": { clipPath: "polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 0 100%)" },
        ".chamfer-sm": { clipPath: "polygon(0 0, calc(100% - 10px) 0, 100% 10px, 100% 100%, 0 100%)" },
      });
    },
  ],
};
