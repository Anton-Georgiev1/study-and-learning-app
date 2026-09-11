"""
Dribbble-inspired UI Template Generator.
Provides a strict 3-color minimalist theme (Canvas, Ink, Accent)
with Lucide icons in a single unified color, consistent style, and zero icon backgrounds.
"""

def render_app() -> str:
    return """<!DOCTYPE html>
<html lang="en" class="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>StudyHub &mdash; Smart Learning App</title>
  <meta name="description" content="A minimalist, Dribbble-crafted study and learning application built purely in Python with dual themes, 3D flashcards, revision notes, Pomodoro timer, and Gemini AI tutor." />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <!-- Lucide Icons Library -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    /* ============================================================
       STRICT 3-COLOR SYSTEM TOKENS (Canvas, Ink, Single Accent)
       ============================================================ */
    :root {
      --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      /* Color 1: Base / Canvas (White) */
      --bg-canvas: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #ffffff;
      --bg-muted: #f1f5f9;
      --bg-active: #eef2ff;

      /* Color 2: Ink / Slate Neutral */
      --text-main: #0f172a;
      --text-secondary: #475569;
      --text-tertiary: #94a3b8;
      --border-subtle: #e2e8f0;
      --border-strong: #cbd5e1;

      /* Color 3: Single Accent Color (Indigo) */
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-soft: #eef2ff;
      --primary-text: #4f46e5;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.03);
      --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.04), 0 8px 10px -6px rgba(0, 0, 0, 0.02);
      --shadow-glow: 0 0 20px rgba(79, 70, 229, 0.12);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
    }

    html.dark {
      /* Color 1: Base / Canvas (Deep Obsidian) */
      --bg-canvas: #090d16;
      --bg-surface: #111827;
      --bg-surface-elevated: #1a2236;
      --bg-muted: #1e293b;
      --bg-active: #1e1b4b;

      /* Color 2: Ink / Slate Neutral */
      --text-main: #f8fafc;
      --text-secondary: #94a3b8;
      --text-tertiary: #64748b;
      --border-subtle: #1f293d;
      --border-strong: #334155;

      /* Color 3: Single Accent Color (Indigo) */
      --primary: #6366f1;
      --primary-hover: #818cf8;
      --primary-soft: #1e1b4b;
      --primary-text: #a5b4fc;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
      --shadow-card: 0 10px 30px rgba(0, 0, 0, 0.5);
      --shadow-glow: 0 0 25px rgba(99, 102, 241, 0.2);
    }

    /* Reset & Base */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
                  border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
                  color 0.15s ease,
                  box-shadow 0.2s ease;
    }

    body {
      font-family: var(--font-main);
      background-color: var(--bg-canvas);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }

    /* Unified Icon Styling: Single color, consistent style, ZERO background */
    .lucide {
      width: 1.15rem;
      height: 1.15rem;
      stroke-width: 1.8;
      stroke: var(--primary) !important;
      color: var(--primary) !important;
      background: none !important;
      background-color: transparent !important;
      border: none !important;
      box-shadow: none !important;
      border-radius: 0 !important;
      display: inline-block;
      vertical-align: middle;
      flex-shrink: 0;
    }

    .icon-sm {
      width: 1rem !important;
      height: 1rem !important;
      stroke-width: 1.8 !important;
    }

    .icon-md {
      width: 1.25rem !important;
      height: 1.25rem !important;
      stroke-width: 1.8 !important;
    }

    .icon-lg {
      width: 1.6rem !important;
      height: 1.6rem !important;
      stroke-width: 1.8 !important;
    }

    /* Contrast icon color inside filled primary button */
    .btn-primary .lucide {
      stroke: #ffffff !important;
      color: #ffffff !important;
    }

    /* Top Navigation Header */
    header {
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
    }

    .header-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0.85rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--text-main);
    }

    .brand-title {
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }

    .brand-badge {
      font-size: 0.7rem;
      font-weight: 700;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      background: var(--bg-muted);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
      margin-left: 0.4rem;
    }

    /* Dribbble Pill Navigation Tabs */
    .nav-pill-group {
      display: flex;
      align-items: center;
      background: var(--bg-muted);
      padding: 0.3rem;
      border-radius: 9999px;
      gap: 0.25rem;
      border: 1px solid var(--border-subtle);
    }

    .nav-pill {
      background: transparent;
      border: none;
      padding: 0.5rem 1rem;
      font-size: 0.875rem;
      font-weight: 600;
      border-radius: 9999px;
      cursor: pointer;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 0.45rem;
      white-space: nowrap;
    }

    .nav-pill:hover {
      color: var(--text-main);
    }

    .nav-pill.active {
      background: var(--bg-surface);
      color: var(--primary);
      box-shadow: var(--shadow-sm);
    }

    /* Action buttons in header */
    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }

    .theme-toggle {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--bg-muted);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.5rem 0.95rem;
      border-radius: 9999px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
    }

    .theme-toggle:hover {
      background: var(--bg-active);
      border-color: var(--primary);
      color: var(--primary);
    }

    /* Banner / Key ribbon */
    .top-ribbon {
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      padding: 0.45rem 1.5rem;
      font-size: 0.825rem;
    }

    .top-ribbon-content {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .pill-status {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.2rem 0.65rem;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.75rem;
    }

    .pill-status.connected {
      background: var(--bg-active);
      color: var(--primary);
      border: 1px solid var(--primary);
    }

    .pill-status.disconnected {
      background: var(--bg-muted);
      color: var(--text-tertiary);
      border: 1px solid var(--border-subtle);
    }

    .pulse-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: currentColor;
    }

    /* Main layout container */
    main {
      max-width: 1200px;
      width: 100%;
      margin: 0 auto;
      padding: 2rem 1.5rem 4rem;
      flex: 1;
    }

    /* Bento metrics bar */
    .bento-metrics {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem;
      margin-bottom: 2rem;
    }

    @media (max-width: 900px) {
      .bento-metrics {
        grid-template-columns: repeat(2, 1fr);
      }
      .nav-pill-group {
        overflow-x: auto;
        max-width: 100%;
      }
    }

    @media (max-width: 600px) {
      .bento-metrics {
        grid-template-columns: 1fr;
      }
      .header-container {
        flex-direction: column;
        align-items: flex-start;
      }
    }

    .bento-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.5rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .bento-card:hover {
      box-shadow: var(--shadow-md);
      border-color: var(--border-strong);
    }

    .bento-info-title {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-tertiary);
      margin-bottom: 0.25rem;
    }

    .bento-info-val {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.2;
    }

    /* Views */
    .tab-view {
      display: none;
    }

    .tab-view.active {
      display: block;
      animation: viewFade 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes viewFade {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Surface Card container */
    .card-panel {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 1.75rem;
      box-shadow: var(--shadow-card);
    }

    /* Dribbble 3D Flashcard Component */
    .flashcard-deck-shelf {
      display: flex;
      gap: 1rem;
      overflow-x: auto;
      padding-bottom: 0.75rem;
      margin-bottom: 1.5rem;
      scroll-snap-type: x mandatory;
    }

    .deck-pill-card {
      flex: 0 0 240px;
      scroll-snap-align: start;
      background: var(--bg-surface);
      border: 2px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.15rem;
      cursor: pointer;
      text-align: left;
    }

    .deck-pill-card:hover {
      border-color: var(--border-strong);
      transform: translateY(-2px);
    }

    .deck-pill-card.selected {
      border-color: var(--primary);
      background: var(--bg-active);
      box-shadow: var(--shadow-glow);
    }

    .deck-tag {
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      background: var(--bg-muted);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
      margin-bottom: 0.5rem;
    }

    .deck-card-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.25rem;
    }

    .deck-card-count {
      font-size: 0.8rem;
      color: var(--text-secondary);
    }

    /* 3D Flip Flashcard Stage */
    .flashcard-stage {
      perspective: 1200px;
      width: 100%;
      min-height: 320px;
      margin: 1.5rem 0;
      cursor: pointer;
    }

    .flashcard-flipper {
      position: relative;
      width: 100%;
      height: 100%;
      min-height: 320px;
      transform-style: preserve-3d;
      transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
      border-radius: var(--radius-xl);
    }

    .flashcard-flipper.flipped {
      transform: rotateY(180deg);
    }

    .flashcard-side {
      position: absolute;
      width: 100%;
      height: 100%;
      min-height: 320px;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border-radius: var(--radius-xl);
      padding: 3rem 2.5rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      box-shadow: var(--shadow-card);
      border: 1px solid var(--border-subtle);
    }

    .flashcard-side.front {
      background: var(--bg-surface);
      color: var(--text-main);
    }

    .flashcard-side.back {
      background: var(--bg-surface);
      color: var(--text-main);
      transform: rotateY(180deg);
      border: 2px solid var(--primary);
    }

    .card-meta-pill {
      position: absolute;
      top: 1.25rem;
      left: 1.5rem;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-tertiary);
    }

    .card-flip-prompt {
      position: absolute;
      bottom: 1.25rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-tertiary);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .card-question {
      font-size: 1.35rem;
      font-weight: 700;
      line-height: 1.5;
      max-width: 650px;
    }

    .card-answer {
      font-size: 1.15rem;
      font-weight: 500;
      line-height: 1.6;
      max-width: 650px;
      white-space: pre-wrap;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.65rem 1.25rem;
      font-size: 0.9rem;
      font-weight: 700;
      border-radius: 9999px;
      cursor: pointer;
      border: 1px solid transparent;
      white-space: nowrap;
    }

    .btn-primary {
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      transform: translateY(-1px);
    }

    .btn-secondary {
      background: var(--bg-muted);
      color: var(--text-main);
      border-color: var(--border-subtle);
    }

    .btn-secondary:hover {
      background: var(--bg-surface-elevated);
      border-color: var(--border-strong);
    }

    .btn-sm {
      padding: 0.4rem 0.85rem;
      font-size: 0.8rem;
    }

    /* Pomodoro Circular Widget */
    .pomodoro-box {
      max-width: 520px;
      margin: 0 auto;
      text-align: center;
      padding: 2.5rem 2rem;
    }

    .timer-svg-wrapper {
      position: relative;
      width: 260px;
      height: 260px;
      margin: 1.5rem auto;
    }

    .timer-ring-bg {
      stroke: var(--bg-muted);
      stroke-width: 12;
      fill: none;
    }

    .timer-ring-progress {
      stroke: var(--primary);
      stroke-width: 12;
      stroke-linecap: round;
      fill: none;
      transform: rotate(-90deg);
      transform-origin: 50% 50%;
      transition: stroke-dashoffset 0.5s ease;
    }

    .timer-center-info {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .timer-countdown {
      font-family: var(--font-mono);
      font-size: 3.5rem;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.04em;
      line-height: 1;
    }

    .timer-mode-tag {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      margin-top: 0.5rem;
    }

    /* Inputs */
    input[type="text"], textarea, select {
      width: 100%;
      padding: 0.75rem 1rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
      background: var(--bg-surface);
      color: var(--text-main);
      font-family: inherit;
      font-size: 0.9rem;
    }

    input[type="text"]:focus, textarea:focus, select:focus {
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px var(--primary-soft);
    }

    /* Notes card grid */
    .notes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.25rem;
    }

    .note-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      cursor: pointer;
    }

    .note-card:hover {
      border-color: var(--border-strong);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }

    /* Gemini Guide Stepper */
    .guide-container {
      max-width: 820px;
      margin: 0 auto;
    }

    .step-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.5rem 1.75rem;
      margin-bottom: 1.25rem;
      display: flex;
      gap: 1.25rem;
      align-items: flex-start;
    }

    .step-number {
      font-family: var(--font-mono);
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--primary);
      width: 2rem;
      flex-shrink: 0;
      line-height: 1.2;
    }

    /* AI Studio Chips */
    .prompt-chip {
      background: var(--bg-muted);
      border: 1px solid var(--border-subtle);
      padding: 0.35rem 0.8rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
    }

    .prompt-chip:hover {
      border-color: var(--primary);
      color: var(--primary);
      background: var(--bg-active);
    }

    /* Modal */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 100;
      padding: 1rem;
      backdrop-filter: blur(4px);
    }

    .modal-backdrop.open {
      display: flex;
    }

    .modal-sheet {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      width: 100%;
      max-width: 520px;
      padding: 2rem;
      box-shadow: var(--shadow-card);
    }

    /* Toast */
    #toast-banner {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--text-main);
      color: var(--bg-surface);
      padding: 0.75rem 1.4rem;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.85rem;
      box-shadow: var(--shadow-card);
      display: none;
      z-index: 200;
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-container">
      <a href="#" class="brand" onclick="navigate('flashcards')">
        <i data-lucide="graduation-cap" class="icon-lg"></i>
        <div>
          <div style="display:flex; align-items:center;">
            <span class="brand-title">StudyHub</span>
            <span class="brand-badge">Python Core</span>
          </div>
        </div>
      </a>

      <!-- Dribbble Pill Navigation -->
      <nav class="nav-pill-group">
        <button class="nav-pill active" id="pill-flashcards" onclick="navigate('flashcards')">
          <i data-lucide="layers" class="icon-sm"></i> <span>Flashcards</span>
        </button>
        <button class="nav-pill" id="pill-notes" onclick="navigate('notes')">
          <i data-lucide="file-text" class="icon-sm"></i> <span>Notes</span>
        </button>
        <button class="nav-pill" id="pill-timer" onclick="navigate('timer')">
          <i data-lucide="timer" class="icon-sm"></i> <span>Pomodoro</span>
        </button>
        <button class="nav-pill" id="pill-ai" onclick="navigate('ai')">
          <i data-lucide="sparkles" class="icon-sm"></i> <span>AI Tutor</span>
        </button>
        <button class="nav-pill" id="pill-guide" onclick="navigate('guide')">
          <i data-lucide="key-round" class="icon-sm"></i> <span>Key Guide</span>
        </button>
      </nav>

      <!-- Theme Switcher (White & Dark) -->
      <div class="header-actions">
        <button class="theme-toggle" id="theme-btn" onclick="toggleTheme()" title="Switch Light / Dark Theme">
          <span id="theme-icon-wrap"><i data-lucide="moon" class="icon-sm"></i></span>
          <span id="theme-text">Dark</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Live Key Ribbon -->
  <div class="top-ribbon">
    <div class="top-ribbon-content">
      <div style="display:flex; align-items:center; gap:0.6rem;">
        <span style="color:var(--text-tertiary); font-weight:600;">Gemini AI Engine:</span>
        <span id="ribbon-key-status" class="pill-status disconnected">
          <span class="pulse-dot"></span>
          <span id="ribbon-status-text">Checking...</span>
        </span>
      </div>
      <a href="#guide" onclick="navigate('guide')" style="color:var(--primary); font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.35rem;">
        <span>Configure Gemini Key</span>
        <i data-lucide="arrow-right" class="icon-sm"></i>
      </a>
    </div>
  </div>

  <!-- Main Content Body -->
  <main>

    <!-- Bento Overview Bar (No background on icons, single color) -->
    <section class="bento-metrics">
      <div class="bento-card">
        <div>
          <div class="bento-info-title">Daily Streak</div>
          <div class="bento-info-val" id="stat-streak">1 Day</div>
        </div>
        <i data-lucide="flame" class="icon-lg"></i>
      </div>
      <div class="bento-card">
        <div>
          <div class="bento-info-title">Focus Time</div>
          <div class="bento-info-val" id="stat-minutes">0 min</div>
        </div>
        <i data-lucide="clock" class="icon-lg"></i>
      </div>
      <div class="bento-card">
        <div>
          <div class="bento-info-title">Cards Studied</div>
          <div class="bento-info-val" id="stat-cards">0 cards</div>
        </div>
        <i data-lucide="check-circle-2" class="icon-lg"></i>
      </div>
      <div class="bento-card">
        <div>
          <div class="bento-info-title">Sessions Done</div>
          <div class="bento-info-val" id="stat-sessions">0 pomos</div>
        </div>
        <i data-lucide="target" class="icon-lg"></i>
      </div>
    </section>

    <!-- 1. FLASHCARDS TAB -->
    <section id="view-flashcards" class="tab-view active">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
        <div>
          <h1 style="font-size:1.75rem; font-weight:800; letter-spacing:-0.03em;">Active Recall Decks</h1>
          <p style="color:var(--text-secondary); font-size:0.95rem;">Strengthen neural pathways through timed retrieval.</p>
        </div>
        <div style="display:flex; gap:0.5rem;">
          <button class="btn btn-secondary" onclick="openAddCardModal()">
            <i data-lucide="plus" class="icon-sm"></i>
            <span>Add Card</span>
          </button>
          <button class="btn btn-primary" onclick="openAddDeckModal()">
            <i data-lucide="folder-plus" class="icon-sm"></i>
            <span>New Deck</span>
          </button>
        </div>
      </div>

      <!-- Deck Carousel / Horizontal Shelf -->
      <div class="flashcard-deck-shelf" id="deck-shelf">
        <!-- Rendered by JS -->
      </div>

      <!-- 3D Flipping Card Arena -->
      <div class="card-panel" style="padding:2.5rem 2rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
          <span style="font-weight:700; font-size:0.9rem; color:var(--text-secondary);" id="active-deck-title-badge">Python Core Concepts</span>
          <div style="display:flex; align-items:center; gap:0.5rem;">
            <span id="card-counter" style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:var(--text-tertiary);">1 / 4</span>
            <button class="btn btn-secondary btn-sm" onclick="shuffleDeck()" title="Shuffle cards">
              <i data-lucide="shuffle" class="icon-sm"></i>
            </button>
          </div>
        </div>

        <div class="flashcard-stage" onclick="flipActiveCard()">
          <div class="flashcard-flipper" id="card-flipper">
            <!-- Front -->
            <div class="flashcard-side front">
              <span class="card-meta-pill">Prompt</span>
              <div class="card-question" id="card-front-content">Loading flashcard prompt...</div>
              <div class="card-flip-prompt">
                <i data-lucide="mouse-pointer-click" class="icon-sm"></i>
                <span>Click card or press <kbd style="background:var(--bg-muted); border:1px solid var(--border-subtle); padding:0.1rem 0.4rem; border-radius:4px; font-family:var(--font-mono); font-size:0.75rem;">Space</kbd> to reveal answer</span>
              </div>
            </div>
            <!-- Back -->
            <div class="flashcard-side back">
              <span class="card-meta-pill" style="color:var(--primary);">Answer</span>
              <div class="card-answer" id="card-back-content">Answer will display here.</div>
              <div class="card-flip-prompt">
                <i data-lucide="rotate-cw" class="icon-sm"></i>
                <span>Click to flip back</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Rating controls (Strict 3-color palette: neutral and primary accent) -->
        <div style="display:flex; justify-content:center; align-items:center; gap:0.75rem; margin-top:1.5rem; flex-wrap:wrap;">
          <button class="btn btn-secondary" onclick="prevCard()">
            <i data-lucide="arrow-left" class="icon-sm"></i>
            <span>Prev</span>
          </button>
          <button class="btn btn-secondary" onclick="rateMastery('again')">
            <i data-lucide="rotate-ccw" class="icon-sm"></i>
            <span>Need Review</span>
          </button>
          <button class="btn btn-primary" onclick="rateMastery('got-it')">
            <i data-lucide="check" class="icon-sm"></i>
            <span>Mastered</span>
          </button>
          <button class="btn btn-secondary" onclick="nextCard()">
            <span>Next</span>
            <i data-lucide="arrow-right" class="icon-sm"></i>
          </button>
        </div>
      </div>
    </section>

    <!-- 2. NOTES TAB -->
    <section id="view-notes" class="tab-view">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
        <div>
          <h1 style="font-size:1.75rem; font-weight:800; letter-spacing:-0.03em;">Revision Notes</h1>
          <p style="color:var(--text-secondary); font-size:0.95rem;">High-yield study summaries, mental models, and cheat sheets.</p>
        </div>
        <button class="btn btn-primary" onclick="openNoteModal()">
          <i data-lucide="plus" class="icon-sm"></i>
          <span>New Note</span>
        </button>
      </div>

      <div style="margin-bottom:1.5rem; position:relative;">
        <i data-lucide="search" class="icon-sm" style="position:absolute; left:1rem; top:50%; transform:translateY(-50%);"></i>
        <input type="text" id="note-search-input" style="padding-left:2.5rem;" placeholder="Search notes by title, subject, or content..." oninput="searchNotes()" />
      </div>

      <div class="notes-grid" id="notes-list-container">
        <!-- Rendered by JS -->
      </div>
    </section>

    <!-- 3. POMODORO TAB -->
    <section id="view-timer" class="tab-view">
      <div class="card-panel pomodoro-box">
        <h1 style="font-size:1.75rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:0.25rem;">Focus Interval</h1>
        <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:1.5rem;">Train your deep attention and prevent cognitive fatigue.</p>

        <!-- Mode pills -->
        <div style="display:flex; justify-content:center; gap:0.5rem; margin-bottom:1rem;">
          <button class="btn btn-secondary btn-sm" id="pomo-mode-focus" onclick="setTimerMode('focus')">Focus (25m)</button>
          <button class="btn btn-secondary btn-sm" id="pomo-mode-short" onclick="setTimerMode('short')">Short Rest (5m)</button>
          <button class="btn btn-secondary btn-sm" id="pomo-mode-long" onclick="setTimerMode('long')">Deep Rest (15m)</button>
        </div>

        <!-- SVG Ring -->
        <div class="timer-svg-wrapper">
          <svg width="260" height="260" viewBox="0 0 260 260">
            <circle class="timer-ring-bg" cx="130" cy="130" r="110"></circle>
            <circle class="timer-ring-progress" id="timer-ring" cx="130" cy="130" r="110" stroke-dasharray="691.15" stroke-dashoffset="0"></circle>
          </svg>
          <div class="timer-center-info">
            <div class="timer-countdown" id="timer-digits">25:00</div>
            <div class="timer-mode-tag" id="timer-tag">STUDY SESSION</div>
          </div>
        </div>

        <!-- Timer Controls -->
        <div style="display:flex; justify-content:center; gap:1rem; margin-top:1rem;">
          <button class="btn btn-primary" id="timer-play-btn" style="padding:0.75rem 2rem; font-size:1rem;" onclick="toggleTimer()">
            <i data-lucide="play" class="icon-sm"></i>
            <span>Start Focus</span>
          </button>
          <button class="btn btn-secondary" style="padding:0.75rem 1.5rem;" onclick="resetTimer()">
            <i data-lucide="rotate-ccw" class="icon-sm"></i>
            <span>Reset</span>
          </button>
        </div>
      </div>
    </section>

    <!-- 4. AI TUTOR TAB -->
    <section id="view-ai" class="tab-view">
      <div style="margin-bottom:1.5rem;">
        <h1 style="font-size:1.75rem; font-weight:800; letter-spacing:-0.03em;">AI Study Companion</h1>
        <p style="color:var(--text-secondary); font-size:0.95rem;">Ask questions, generate flashcards, or take a quick practice quiz.</p>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem;" id="ai-grid">
        <!-- Explainer -->
        <div class="card-panel">
          <h2 style="font-size:1.15rem; font-weight:800; margin-bottom:0.4rem; display:flex; align-items:center; gap:0.5rem;">
            <i data-lucide="lightbulb" class="icon-md"></i>
            <span>Concept Explainer</span>
          </h2>
          <p style="color:var(--text-secondary); font-size:0.85rem; margin-bottom:1rem;">Break down challenging topics with everyday analogies.</p>

          <div style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:1rem;">
            <button class="prompt-chip" onclick="fillPrompt('Explain how Python decorators work with an analogy')">Decorators</button>
            <button class="prompt-chip" onclick="fillPrompt('How does the Feynman technique work?')">Feynman Method</button>
            <button class="prompt-chip" onclick="fillPrompt('Difference between asynchronous and multi-threaded programming')">Async vs Threading</button>
          </div>

          <div style="margin-bottom:0.75rem;">
            <label style="font-size:0.8rem; font-weight:700; color:var(--text-tertiary);">Mode:</label>
            <select id="ai-mode-select">
              <option value="simplify">Feynman Technique (Explain like I'm 12)</option>
              <option value="academic">Deep Academic Tutor</option>
              <option value="summarize">High-Yield Exam Summary</option>
            </select>
          </div>

          <div style="margin-bottom:1rem;">
            <textarea id="ai-prompt-box" rows="3" placeholder="What concept do you want to master today?"></textarea>
          </div>

          <button class="btn btn-primary" style="width:100%;" onclick="runAiExplainer()">
            <i data-lucide="sparkles" class="icon-sm"></i>
            <span>Ask AI Tutor</span>
          </button>

          <div id="ai-explain-box" style="display:none; margin-top:1.25rem; padding:1.25rem; background:var(--bg-muted); border-radius:var(--radius-md); font-size:0.9rem; line-height:1.6; border:1px solid var(--border-subtle); white-space:pre-wrap;">
          </div>
        </div>

        <!-- Flashcard & Quiz Maker -->
        <div class="card-panel">
          <h2 style="font-size:1.15rem; font-weight:800; margin-bottom:0.4rem; display:flex; align-items:center; gap:0.5rem;">
            <i data-lucide="zap" class="icon-md"></i>
            <span>Instant Flashcards & Quiz</span>
          </h2>
          <p style="color:var(--text-secondary); font-size:0.85rem; margin-bottom:1rem;">Paste notes or a topic and let Gemini construct learning materials.</p>

          <div style="margin-bottom:1rem;">
            <textarea id="ai-material-box" rows="4" placeholder="Enter topic or paste notes: e.g. Mitochondria, Krebs cycle, and cellular respiration..."></textarea>
          </div>

          <div style="display:flex; gap:0.5rem; margin-bottom:1.5rem;">
            <button class="btn btn-secondary" style="flex:1;" onclick="runAiCardGen()">
              <i data-lucide="layers" class="icon-sm"></i>
              <span>Make 4 Flashcards</span>
            </button>
            <button class="btn btn-primary" style="flex:1;" onclick="runAiQuizGen()">
              <i data-lucide="help-circle" class="icon-sm"></i>
              <span>Generate Quiz</span>
            </button>
          </div>

          <div id="ai-cards-target" style="display:none;"></div>
          <div id="ai-quiz-target" style="display:none;"></div>
        </div>
      </div>
    </section>

    <!-- 5. GEMINI KEY GUIDE TAB -->
    <section id="view-guide" class="tab-view">
      <div class="guide-container">
        <div style="margin-bottom:2rem; text-align:center;">
          <h1 style="font-size:2rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:0.5rem;">Google Gemini API Key Guide</h1>
          <p style="color:var(--text-secondary); font-size:1rem; max-width:620px; margin:0 auto;">
            Connect your free Google Gemini API key to activate the intelligent study assistant, automatic flashcard generator, and practice quizzes.
          </p>
        </div>

        <!-- Interactive Key Storage & Management Panel (Store, Change, Delete, Test) -->
        <div class="card-panel" style="margin-bottom:2rem; border-color:var(--primary);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1.25rem; flex-wrap:wrap; gap:0.75rem;">
            <div>
              <div style="font-size:0.75rem; font-weight:800; text-transform:uppercase; color:var(--primary); letter-spacing:0.05em;">API Key Settings & Storage</div>
              <div id="guide-status-title" style="font-size:1.35rem; font-weight:800; color:var(--text-main); margin-top:0.25rem;">
                Gemini API Key
              </div>
              <div id="guide-status-sub" style="font-size:0.875rem; color:var(--text-secondary); margin-top:0.25rem;">
                Enter your key once to store and activate it. You can change, test, or delete it anytime.
              </div>
            </div>
            <div id="key-badge-container">
              <span class="pill-status disconnected" id="key-active-badge">
                <span class="pulse-dot"></span>
                <span id="key-active-badge-text">Checking...</span>
              </span>
            </div>
          </div>

          <!-- Input Row -->
          <div style="display:flex; flex-direction:column; gap:0.75rem;">
            <div style="position:relative; display:flex; align-items:center;">
              <input type="password" id="gemini-key-input" placeholder="Paste your Google Gemini API key (starts with AIzaSy...)" style="padding-right:2.8rem; font-family:var(--font-mono); font-size:0.875rem;" />
              <button type="button" onclick="toggleKeyVisibility()" style="position:absolute; right:0.75rem; background:none; border:none; color:var(--primary); cursor:pointer; padding:0.25rem; display:flex; align-items:center;" title="Toggle show/hide key">
                <i data-lucide="eye" id="key-eye-icon" class="icon-sm"></i>
              </button>
            </div>

            <!-- Action Buttons: Save/Update, Test Connection, Delete Key -->
            <div style="display:flex; gap:0.6rem; flex-wrap:wrap; align-items:center;">
              <button class="btn btn-primary" id="btn-save-key" onclick="saveGeminiKey()">
                <i data-lucide="check" class="icon-sm"></i>
                <span id="btn-save-key-text">Save & Store Key</span>
              </button>
              <button class="btn btn-secondary" id="btn-test-key" onclick="testConnection()">
                <i data-lucide="refresh-cw" class="icon-sm"></i>
                <span>Test Live Connection</span>
              </button>
              <button class="btn btn-secondary" id="btn-delete-key" style="display:none;" onclick="deleteGeminiKey()">
                <i data-lucide="trash-2" class="icon-sm"></i>
                <span>Delete Key</span>
              </button>
            </div>
          </div>

          <!-- Live feedback box -->
          <div id="key-feedback-box" style="display:none; margin-top:1rem; padding:0.75rem 1rem; border-radius:var(--radius-md); font-size:0.85rem; border:1px solid var(--border-subtle); background:var(--bg-muted);">
          </div>
        </div>

        <!-- 4 Step Guide (Clean typographic step numbers, no background shapes) -->
        <div class="step-card">
          <div class="step-number">01</div>
          <div>
            <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:0.35rem;">Visit Google AI Studio</h3>
            <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:0.75rem;">
              Navigate to the official Google AI Studio key manager:
            </p>
            <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="display:inline-flex; align-items:center; gap:0.4rem;">
              <span>aistudio.google.com/app/apikey</span>
              <i data-lucide="external-link" class="icon-sm"></i>
            </a>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">02</div>
          <div>
            <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:0.35rem;">Sign In with your Google Account</h3>
            <p style="color:var(--text-secondary); font-size:0.9rem;">
              Sign in with your Google account. Developers and learners receive generous free tier requests every day.
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">03</div>
          <div>
            <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:0.35rem;">Click "Create API Key"</h3>
            <p style="color:var(--text-secondary); font-size:0.9rem;">
              Click the <strong>"Create API Key"</strong> button and select or create a project. Copy your newly generated key starting with <code>AIzaSy...</code>.
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">04</div>
          <div>
            <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:0.35rem;">Attach to your Application</h3>
            <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:0.5rem;">
              In AI Studio, open the <strong>Settings / Secrets</strong> menu and set <code>GEMINI_API_KEY</code>, or save it in your <code>.env</code> file:
            </p>
            <pre style="background:var(--bg-muted); padding:0.75rem 1rem; border-radius:var(--radius-md); font-family:var(--font-mono); font-size:0.85rem; border:1px solid var(--border-subtle);">GEMINI_API_KEY="AIzaSyYourSecretKeyHere"</pre>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Modals -->
  <!-- New Deck Modal -->
  <div class="modal-backdrop" id="modal-deck">
    <div class="modal-sheet">
      <h2 style="font-size:1.25rem; font-weight:800; margin-bottom:1rem;">Create Study Deck</h2>
      <div style="display:flex; flex-direction:column; gap:0.85rem;">
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Deck Title</label>
          <input type="text" id="new-deck-title" placeholder="e.g. Cognitive Biases" />
        </div>
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Category</label>
          <input type="text" id="new-deck-category" placeholder="e.g. Psychology, Science, Code" />
        </div>
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Description</label>
          <textarea id="new-deck-desc" rows="2" placeholder="What will this deck cover?"></textarea>
        </div>
        <div style="display:flex; justify-content:flex-end; gap:0.5rem; margin-top:0.5rem;">
          <button class="btn btn-secondary" onclick="closeModals()">Cancel</button>
          <button class="btn btn-primary" onclick="submitNewDeck()">Create Deck</button>
        </div>
      </div>
    </div>
  </div>

  <!-- New Card Modal -->
  <div class="modal-backdrop" id="modal-card">
    <div class="modal-sheet">
      <h2 style="font-size:1.25rem; font-weight:800; margin-bottom:1rem;">Add Flashcard</h2>
      <div style="display:flex; flex-direction:column; gap:0.85rem;">
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Prompt / Question (Front)</label>
          <textarea id="new-card-front" rows="2" placeholder="e.g. What is the Pareto Principle?"></textarea>
        </div>
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Answer (Back)</label>
          <textarea id="new-card-back" rows="3" placeholder="e.g. 80% of consequences come from 20% of causes."></textarea>
        </div>
        <div style="display:flex; justify-content:flex-end; gap:0.5rem; margin-top:0.5rem;">
          <button class="btn btn-secondary" onclick="closeModals()">Cancel</button>
          <button class="btn btn-primary" onclick="submitNewCard()">Save Card</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Note Modal -->
  <div class="modal-backdrop" id="modal-note">
    <div class="modal-sheet" style="max-width:600px;">
      <h2 style="font-size:1.25rem; font-weight:800; margin-bottom:1rem;" id="note-modal-title">Create Revision Note</h2>
      <div style="display:flex; flex-direction:column; gap:0.85rem;">
        <input type="hidden" id="edit-note-id" />
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Title</label>
          <input type="text" id="note-title-input" placeholder="e.g. Spaced Repetition Intervals" />
        </div>
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Topic / Subject</label>
          <input type="text" id="note-topic-input" placeholder="e.g. Neuroscience, Physics, Code" />
        </div>
        <div>
          <label style="font-size:0.8rem; font-weight:700;">Content</label>
          <textarea id="note-content-input" rows="6" placeholder="Write your key takeaways, formulas, and explanations..."></textarea>
        </div>
        <div style="display:flex; justify-content:flex-end; gap:0.5rem; margin-top:0.5rem;">
          <button class="btn btn-secondary" onclick="closeModals()">Cancel</button>
          <button class="btn btn-primary" onclick="submitNote()">Save Note</button>
        </div>
      </div>
    </div>
  </div>

  <div id="toast-banner">Notification</div>

  <!-- Client-Side App Controller -->
  <script>
    // State
    let appState = {
      decks: [],
      notes: [],
      stats: { pomodoros_completed: 0, study_minutes: 0, cards_reviewed: 0, streak_days: 1 },
      currentDeckId: null,
      currentCardIndex: 0,
      isFlipped: false,
      timer: {
        totalSeconds: 25 * 60,
        remainingSeconds: 25 * 60,
        mode: 'focus',
        intervalId: null
      }
    };

    // Helper to refresh Lucide icons (Single style, single color, no background)
    function refreshIcons() {
      if (window.lucide && typeof window.lucide.createIcons === 'function') {
        try {
          window.lucide.createIcons();
        } catch (e) {
          console.warn('Lucide icon render notice:', e);
        }
      }
    }

    // Theme Management (White / Dark)
    function initTheme() {
      const saved = localStorage.getItem('study_theme') || 'light';
      setTheme(saved);
    }

    function setTheme(theme) {
      const html = document.documentElement;
      const wrap = document.getElementById('theme-icon-wrap');
      const text = document.getElementById('theme-text');
      if (theme === 'dark') {
        html.classList.remove('light');
        html.classList.add('dark');
        if (wrap) wrap.innerHTML = '<i data-lucide="sun" class="icon-sm"></i>';
        if (text) text.textContent = 'Light';
        localStorage.setItem('study_theme', 'dark');
      } else {
        html.classList.remove('dark');
        html.classList.add('light');
        if (wrap) wrap.innerHTML = '<i data-lucide="moon" class="icon-sm"></i>';
        if (text) text.textContent = 'Dark';
        localStorage.setItem('study_theme', 'light');
      }
      refreshIcons();
    }

    function toggleTheme() {
      const isDark = document.documentElement.classList.contains('dark');
      setTheme(isDark ? 'light' : 'dark');
    }

    // Navigation
    function navigate(tabName) {
      document.querySelectorAll('.nav-pill').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-view').forEach(view => view.classList.remove('active'));

      const pill = document.getElementById('pill-' + tabName);
      const view = document.getElementById('view-' + tabName);
      if (pill) pill.classList.add('active');
      if (view) view.classList.add('active');
      refreshIcons();
    }

    function showToast(msg) {
      const t = document.getElementById('toast-banner');
      t.textContent = msg;
      t.style.display = 'block';
      setTimeout(() => { t.style.display = 'none'; }, 2600);
    }

    // Audio cue
    function playChime() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.3); // A5
        gain.gain.setValueAtTime(0.15, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.6);
        osc.start();
        osc.stop(ctx.currentTime + 0.6);
      } catch (e) {}
    }

    // Load Data
    async function loadInitialData() {
      try {
        const [statusRes, decksRes, notesRes] = await Promise.all([
          fetch('/api/status').then(r => r.json()),
          fetch('/api/decks').then(r => r.json()),
          fetch('/api/notes').then(r => r.json())
        ]);

        updateGeminiStatus(statusRes);
        appState.decks = decksRes.decks || [];
        appState.notes = notesRes.notes || [];
        appState.stats = statusRes.stats || appState.stats;

        renderStats();
        renderDecksShelf();
        renderNotes();

        if (appState.decks.length > 0) {
          selectDeck(appState.decks[0].id);
        }
        refreshIcons();
      } catch (err) {
        console.error('Error loading data:', err);
      }
    }

    function updateGeminiStatus(status) {
      const ribbonBadge = document.getElementById('ribbon-key-status');
      const ribbonText = document.getElementById('ribbon-status-text');
      const guideTitle = document.getElementById('guide-status-title');
      const guideSub = document.getElementById('guide-status-sub');
      const keyBadge = document.getElementById('key-active-badge');
      const keyBadgeText = document.getElementById('key-active-badge-text');
      const btnSaveText = document.getElementById('btn-save-key-text');
      const btnDelete = document.getElementById('btn-delete-key');
      const keyInput = document.getElementById('gemini-key-input');

      appState.gemini_configured = !!status.gemini_configured;

      if (status.gemini_configured) {
        if (ribbonBadge) ribbonBadge.className = 'pill-status connected';
        if (ribbonText) ribbonText.textContent = 'Active (' + status.gemini_preview + ')';

        if (guideTitle) guideTitle.textContent = 'Gemini API Connected';
        if (guideSub) guideSub.textContent = 'Key ' + status.gemini_preview + ' is stored and ready for flashcards, quizzes, and tutoring.';

        if (keyBadge) keyBadge.className = 'pill-status connected';
        if (keyBadgeText) keyBadgeText.textContent = 'Active (' + status.gemini_preview + ')';

        if (btnSaveText) btnSaveText.textContent = 'Change / Update Key';
        if (btnDelete) btnDelete.style.display = 'inline-flex';
        if (keyInput) keyInput.placeholder = 'Enter new key to replace (' + status.gemini_preview + ')';
      } else {
        if (ribbonBadge) ribbonBadge.className = 'pill-status disconnected';
        if (ribbonText) ribbonText.textContent = 'Key Not Set';

        if (guideTitle) guideTitle.textContent = 'No Key Configured';
        if (guideSub) guideSub.textContent = 'Enter your Gemini API key below to store it and unlock AI study features.';

        if (keyBadge) keyBadge.className = 'pill-status disconnected';
        if (keyBadgeText) keyBadgeText.textContent = 'Key Not Stored';

        if (btnSaveText) btnSaveText.textContent = 'Save & Store Key';
        if (btnDelete) btnDelete.style.display = 'none';
        if (keyInput) keyInput.placeholder = 'Paste your Google Gemini API key (starts with AIzaSy...)';
      }
      refreshIcons();
    }

    function toggleKeyVisibility() {
      const input = document.getElementById('gemini-key-input');
      const icon = document.getElementById('key-eye-icon');
      if (!input || !icon) return;
      if (input.type === 'password') {
        input.type = 'text';
        icon.setAttribute('data-lucide', 'eye-off');
      } else {
        input.type = 'password';
        icon.setAttribute('data-lucide', 'eye');
      }
      refreshIcons();
    }

    async function saveGeminiKey() {
      const input = document.getElementById('gemini-key-input');
      const key = input ? input.value.trim() : '';
      if (!key) {
        showToast('Please enter an API key');
        if (input) input.focus();
        return;
      }
      showToast('Saving Gemini API key...');
      try {
        const res = await fetch('/api/gemini/key', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ api_key: key })
        });
        const data = await res.json();
        if (res.ok && data.status === 'saved') {
          showToast('Gemini API key stored successfully');
          if (input) input.value = '';
          const st = await fetch('/api/status').then(r => r.json());
          updateGeminiStatus(st);
          testConnection();
        } else {
          showToast(data.error || 'Failed to save key');
        }
      } catch (err) {
        showToast('Error saving key: ' + err.message);
      }
    }

    async function deleteGeminiKey() {
      if (!confirm('Are you sure you want to remove the stored Gemini API key?')) {
        return;
      }
      showToast('Deleting stored key...');
      try {
        const res = await fetch('/api/gemini/key/delete', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();
        if (res.ok && data.status === 'deleted') {
          showToast('Gemini API key deleted');
          const input = document.getElementById('gemini-key-input');
          if (input) input.value = '';
          const feedback = document.getElementById('key-feedback-box');
          if (feedback) feedback.style.display = 'none';
          const st = await fetch('/api/status').then(r => r.json());
          updateGeminiStatus(st);
        } else {
          showToast('Failed to delete key');
        }
      } catch (err) {
        showToast('Error deleting key: ' + err.message);
      }
    }

    function renderStats() {
      document.getElementById('stat-streak').textContent = (appState.stats.streak_days || 1) + ' Days';
      document.getElementById('stat-minutes').textContent = (appState.stats.study_minutes || 0) + ' min';
      document.getElementById('stat-cards').textContent = (appState.stats.cards_reviewed || 0) + ' cards';
      document.getElementById('stat-sessions').textContent = (appState.stats.pomodoros_completed || 0) + ' pomos';
      refreshIcons();
    }

    // Flashcards Shelf & Arena
    function renderDecksShelf() {
      const shelf = document.getElementById('deck-shelf');
      shelf.innerHTML = '';
      appState.decks.forEach(deck => {
        const isSel = deck.id === appState.currentDeckId;
        const card = document.createElement('div');
        card.className = 'deck-pill-card' + (isSel ? ' selected' : '');
        card.onclick = () => selectDeck(deck.id);

        card.innerHTML = `
          <span class="deck-tag">${deck.category || 'General'}</span>
          <div class="deck-card-title">${deck.title}</div>
          <div class="deck-card-count">${(deck.cards || []).length} cards</div>
        `;
        shelf.appendChild(card);
      });
      refreshIcons();
    }

    function selectDeck(deckId) {
      appState.currentDeckId = deckId;
      appState.currentCardIndex = 0;
      appState.isFlipped = false;
      renderDecksShelf();
      renderActiveCard();
    }

    function getCurrentDeck() {
      return appState.decks.find(d => d.id === appState.currentDeckId);
    }

    function renderActiveCard() {
      const deck = getCurrentDeck();
      const flipper = document.getElementById('card-flipper');
      flipper.classList.remove('flipped');
      appState.isFlipped = false;

      if (!deck || !deck.cards || deck.cards.length === 0) {
        document.getElementById('active-deck-title-badge').textContent = deck ? deck.title : 'No Deck';
        document.getElementById('card-counter').textContent = '0 / 0';
        document.getElementById('card-front-content').textContent = 'This deck is currently empty. Click "+ Add Card" above to add study material.';
        document.getElementById('card-back-content').textContent = 'No answer yet.';
        refreshIcons();
        return;
      }

      document.getElementById('active-deck-title-badge').textContent = deck.title;
      const total = deck.cards.length;
      if (appState.currentCardIndex >= total) appState.currentCardIndex = 0;
      const card = deck.cards[appState.currentCardIndex];

      document.getElementById('card-counter').textContent = (appState.currentCardIndex + 1) + ' / ' + total;
      document.getElementById('card-front-content').textContent = card.front;
      document.getElementById('card-back-content').textContent = card.back;
      refreshIcons();
    }

    function flipActiveCard() {
      const flipper = document.getElementById('card-flipper');
      appState.isFlipped = !appState.isFlipped;
      if (appState.isFlipped) {
        flipper.classList.add('flipped');
      } else {
        flipper.classList.remove('flipped');
      }
      refreshIcons();
    }

    function nextCard() {
      const deck = getCurrentDeck();
      if (!deck || !deck.cards || deck.cards.length === 0) return;
      appState.currentCardIndex = (appState.currentCardIndex + 1) % deck.cards.length;
      renderActiveCard();
    }

    function prevCard() {
      const deck = getCurrentDeck();
      if (!deck || !deck.cards || deck.cards.length === 0) return;
      appState.currentCardIndex = (appState.currentCardIndex - 1 + deck.cards.length) % deck.cards.length;
      renderActiveCard();
    }

    function shuffleDeck() {
      const deck = getCurrentDeck();
      if (!deck || !deck.cards || deck.cards.length < 2) return;
      for (let i = deck.cards.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [deck.cards[i], deck.cards[j]] = [deck.cards[j], deck.cards[i]];
      }
      appState.currentCardIndex = 0;
      renderActiveCard();
      showToast('Deck order randomized');
    }

    async function rateMastery(rating) {
      await fetch('/api/stats/increment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: 'cards_reviewed', value: 1 })
      });
      appState.stats.cards_reviewed = (appState.stats.cards_reviewed || 0) + 1;
      renderStats();
      if (rating === 'got-it') {
        showToast('Marked as mastered');
      } else {
        showToast('Scheduled for review');
      }
      nextCard();
    }

    // Revision Notes
    function renderNotes(filterText = '') {
      const container = document.getElementById('notes-list-container');
      container.innerHTML = '';
      const filtered = appState.notes.filter(n => {
        const q = filterText.toLowerCase();
        return n.title.toLowerCase().includes(q) ||
               (n.topic || '').toLowerCase().includes(q) ||
               n.content.toLowerCase().includes(q);
      });

      if (filtered.length === 0) {
        container.innerHTML = '<div style="color:var(--text-tertiary); padding:2rem; text-align:center;">No revision notes match your query.</div>';
        return;
      }

      filtered.forEach(note => {
        const el = document.createElement('div');
        el.className = 'note-card';
        el.innerHTML = `
          <div>
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.5rem;">
              <span class="deck-tag">${note.topic || 'General'}</span>
              <button onclick="event.stopPropagation(); deleteNote('${note.id}')" style="background:none; border:none; color:var(--text-tertiary); cursor:pointer; display:inline-flex; align-items:center; padding:0.25rem;" title="Delete Note">
                <i data-lucide="trash-2" class="icon-sm"></i>
              </button>
            </div>
            <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:0.5rem;">${note.title}</h3>
            <p style="font-size:0.875rem; color:var(--text-secondary); white-space:pre-wrap; line-height:1.5;">${note.content}</p>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:1rem; border-top:1px solid var(--border-subtle); padding-top:0.75rem;">
            <span style="font-size:0.75rem; color:var(--text-tertiary);">${note.updated_at || ''}</span>
            <button class="btn btn-secondary btn-sm" onclick="event.stopPropagation(); askAiAboutNote('${note.title}')">
              <i data-lucide="sparkles" class="icon-sm"></i>
              <span>Ask AI</span>
            </button>
          </div>
        `;
        el.onclick = () => editNote(note);
        container.appendChild(el);
      });
      refreshIcons();
    }

    function searchNotes() {
      const q = document.getElementById('note-search-input').value;
      renderNotes(q);
    }

    function askAiAboutNote(title) {
      navigate('ai');
      document.getElementById('ai-prompt-box').value = 'Explain the key concepts and study tips for: ' + title;
      runAiExplainer();
    }

    // Pomodoro Timer
    function setTimerMode(mode) {
      clearInterval(appState.timer.intervalId);
      appState.timer.intervalId = null;
      document.getElementById('timer-play-btn').innerHTML = '<i data-lucide="play" class="icon-sm"></i> <span>Start Focus</span>';

      appState.timer.mode = mode;
      let mins = 25;
      let tag = 'STUDY SESSION';
      if (mode === 'short') { mins = 5; tag = 'SHORT BREAK'; }
      if (mode === 'long') { mins = 15; tag = 'DEEP RECOVERY'; }

      appState.timer.totalSeconds = mins * 60;
      appState.timer.remainingSeconds = mins * 60;
      document.getElementById('timer-tag').textContent = tag;
      updateTimerUI();
      refreshIcons();
    }

    function toggleTimer() {
      const btn = document.getElementById('timer-play-btn');
      if (appState.timer.intervalId) {
        clearInterval(appState.timer.intervalId);
        appState.timer.intervalId = null;
        btn.innerHTML = '<i data-lucide="play" class="icon-sm"></i> <span>Resume</span>';
      } else {
        btn.innerHTML = '<i data-lucide="pause" class="icon-sm"></i> <span>Pause</span>';
        appState.timer.intervalId = setInterval(tickTimer, 1000);
      }
      refreshIcons();
    }

    function resetTimer() {
      clearInterval(appState.timer.intervalId);
      appState.timer.intervalId = null;
      document.getElementById('timer-play-btn').innerHTML = '<i data-lucide="play" class="icon-sm"></i> <span>Start Focus</span>';
      appState.timer.remainingSeconds = appState.timer.totalSeconds;
      updateTimerUI();
      refreshIcons();
    }

    async function tickTimer() {
      if (appState.timer.remainingSeconds > 0) {
        appState.timer.remainingSeconds--;
        updateTimerUI();
      } else {
        clearInterval(appState.timer.intervalId);
        appState.timer.intervalId = null;
        document.getElementById('timer-play-btn').innerHTML = '<i data-lucide="play" class="icon-sm"></i> <span>Start Focus</span>';
        refreshIcons();
        playChime();
        showToast('Focus session complete! Great work.');

        if (appState.timer.mode === 'focus') {
          await fetch('/api/stats/increment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: 'pomodoros_completed', value: 1 })
          });
          await fetch('/api/stats/increment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: 'study_minutes', value: 25 })
          });
          appState.stats.pomodoros_completed = (appState.stats.pomodoros_completed || 0) + 1;
          appState.stats.study_minutes = (appState.stats.study_minutes || 0) + 25;
          renderStats();
        }
      }
    }

    function updateTimerUI() {
      const s = appState.timer.remainingSeconds;
      const m = Math.floor(s / 60);
      const sec = s % 60;
      const str = String(m).padStart(2, '0') + ':' + String(sec).padStart(2, '0');
      document.getElementById('timer-digits').textContent = str;

      const ring = document.getElementById('timer-ring');
      const circumference = 691.15;
      const fraction = 1 - (s / appState.timer.totalSeconds);
      ring.style.strokeDashoffset = (circumference * fraction);
    }

    // AI Studio Integrations
    function fillPrompt(text) {
      document.getElementById('ai-prompt-box').value = text;
    }

    async function runAiExplainer() {
      const prompt = document.getElementById('ai-prompt-box').value.trim();
      const mode = document.getElementById('ai-mode-select').value;
      const resultBox = document.getElementById('ai-explain-box');

      if (!prompt) {
        showToast('Please type a question or concept first');
        return;
      }

      resultBox.style.display = 'block';
      resultBox.textContent = 'Thinking with Gemini...';

      try {
        const res = await fetch('/api/gemini/explain', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt, mode })
        });
        const data = await res.json();
        if (data.text) {
          resultBox.textContent = data.text;
        } else {
          resultBox.textContent = 'Notice: ' + (data.error || 'Failed to explain concept.');
        }
      } catch (err) {
        resultBox.textContent = 'Request error: ' + err.message;
      }
    }

    async function runAiCardGen() {
      const text = document.getElementById('ai-material-box').value.trim();
      const target = document.getElementById('ai-cards-target');
      if (!text) {
        showToast('Please enter some study material or topic');
        return;
      }

      target.style.display = 'block';
      target.innerHTML = '<div style="padding:1rem; color:var(--text-tertiary);">Creating 4 flashcards with Gemini...</div>';

      try {
        const res = await fetch('/api/gemini/generate-cards', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text })
        });
        const data = await res.json();

        if (data.cards && data.cards.length > 0) {
          let html = `<div style="margin-top:1rem; border-top:1px solid var(--border-subtle); padding-top:1rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
              <span style="font-weight:800; font-size:0.95rem;">Generated Flashcards</span>
              <button class="btn btn-primary btn-sm" onclick="saveGeneratedCards(${JSON.stringify(data.cards).replace(/"/g, '&quot;')})">
                <i data-lucide="plus" class="icon-sm"></i>
                <span>Add to Current Deck</span>
              </button>
            </div>`;

          data.cards.forEach((c, idx) => {
            html += `<div style="background:var(--bg-muted); padding:0.75rem 1rem; border-radius:var(--radius-md); margin-bottom:0.5rem; font-size:0.85rem;">
              <strong style="color:var(--text-main);">Q: ${c.front}</strong><br/>
              <span style="color:var(--text-secondary);">A: ${c.back}</span>
            </div>`;
          });
          html += '</div>';
          target.innerHTML = html;
          refreshIcons();
        } else {
          target.innerHTML = `<div style="padding:1rem; color:var(--text-secondary);">Notice: ${data.error || 'Could not parse cards.'}</div>`;
        }
      } catch (err) {
        target.innerHTML = `<div style="padding:1rem; color:var(--text-secondary);">Error: ${err.message}</div>`;
      }
    }

    async function saveGeneratedCards(cards) {
      if (!appState.currentDeckId) {
        showToast('Please select a deck first');
        return;
      }
      for (const c of cards) {
        await fetch('/api/decks/card', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ deck_id: appState.currentDeckId, front: c.front, back: c.back })
        });
      }
      showToast('Added ' + cards.length + ' cards to current deck');
      const decksRes = await fetch('/api/decks').then(r => r.json());
      appState.decks = decksRes.decks || [];
      renderDecksShelf();
      renderActiveCard();
      navigate('flashcards');
    }

    async function runAiQuizGen() {
      const topic = document.getElementById('ai-material-box').value.trim();
      const target = document.getElementById('ai-quiz-target');
      if (!topic) {
        showToast('Please provide a topic for the quiz');
        return;
      }

      target.style.display = 'block';
      target.innerHTML = '<div style="padding:1rem; color:var(--text-tertiary);">Formulating quiz questions...</div>';

      try {
        const res = await fetch('/api/gemini/quiz', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ topic })
        });
        const data = await res.json();

        if (data.quiz && data.quiz.length > 0) {
          let html = `<div style="margin-top:1rem; border-top:1px solid var(--border-subtle); padding-top:1rem;">
            <h3 style="font-size:1.05rem; font-weight:800; margin-bottom:1rem;">Practice Quiz</h3>`;

          data.quiz.forEach((q, qIdx) => {
            html += `<div style="background:var(--bg-muted); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
              <div style="font-weight:700; margin-bottom:0.75rem; font-size:0.9rem;">${qIdx + 1}. ${q.question}</div>
              <div style="display:flex; flex-direction:column; gap:0.4rem;">`;

            q.options.forEach((opt, optIdx) => {
              html += `<button class="btn btn-secondary btn-sm" style="justify-content:flex-start; text-align:left;" onclick="checkQuizAnswer(this, ${optIdx === q.correct_index}, '${q.explanation.replace(/'/g, "\\'")}')">
                ${String.fromCharCode(65 + optIdx)}. ${opt}
              </button>`;
            });

            html += `</div><div class="quiz-feedback" style="margin-top:0.5rem; font-size:0.85rem; display:none;"></div></div>`;
          });
          html += '</div>';
          target.innerHTML = html;
          refreshIcons();
        } else {
          target.innerHTML = `<div style="padding:1rem; color:var(--text-secondary);">Notice: ${data.error || 'Could not formulate quiz.'}</div>`;
        }
      } catch (err) {
        target.innerHTML = `<div style="padding:1rem; color:var(--text-secondary);">Error: ${err.message}</div>`;
      }
    }

    function checkQuizAnswer(btn, isCorrect, explanation) {
      const parent = btn.closest('div');
      parent.querySelectorAll('button').forEach(b => b.disabled = true);
      const feedback = parent.parentElement.querySelector('.quiz-feedback');
      feedback.style.display = 'block';

      if (isCorrect) {
        btn.style.background = 'var(--primary)';
        btn.style.color = '#fff';
        btn.style.borderColor = 'var(--primary)';
        feedback.style.color = 'var(--primary)';
        feedback.innerHTML = '<div style="display:flex; align-items:center; gap:0.4rem; font-weight:700;"><i data-lucide="check-circle-2" class="icon-sm"></i> <span>Correct</span></div><div style="margin-top:0.25rem;">' + explanation + '</div>';
        playChime();
      } else {
        btn.style.background = 'var(--bg-muted)';
        btn.style.color = 'var(--text-main)';
        btn.style.borderColor = 'var(--border-strong)';
        feedback.style.color = 'var(--text-secondary)';
        feedback.innerHTML = '<div style="display:flex; align-items:center; gap:0.4rem; font-weight:700;"><i data-lucide="x-circle" class="icon-sm"></i> <span>Incorrect</span></div><div style="margin-top:0.25rem;">' + explanation + '</div>';
      }
      refreshIcons();
    }

    // Connection test
    async function testConnection() {
      const feedback = document.getElementById('key-feedback-box');
      if (feedback) {
        feedback.style.display = 'block';
        feedback.innerHTML = '<div style="display:flex; align-items:center; gap:0.4rem; color:var(--text-secondary);"><i data-lucide="refresh-cw" class="icon-sm"></i> <span>Testing connection with Google Gemini...</span></div>';
        refreshIcons();
      }
      showToast('Testing Gemini Connection...');
      try {
        const res = await fetch('/api/gemini/explain', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: 'Say hi in 3 words', mode: 'simplify' })
        });
        const data = await res.json();
        if (data.text) {
          showToast('Gemini Verified: ' + data.model);
          if (feedback) {
            feedback.style.display = 'block';
            feedback.style.borderColor = 'var(--primary)';
            feedback.innerHTML = '<div style="display:flex; align-items:center; gap:0.4rem; font-weight:700; color:var(--primary);"><i data-lucide="check-circle-2" class="icon-sm"></i> <span>Live Connection Verified (' + data.model + ')</span></div><div style="margin-top:0.35rem; color:var(--text-secondary); font-size:0.85rem;">Gemini replied: "' + data.text + '"</div>';
          }
          const st = await fetch('/api/status').then(r => r.json());
          updateGeminiStatus(st);
        } else {
          showToast('Key issue: ' + (data.error || 'Check key'));
          if (feedback) {
            feedback.style.display = 'block';
            feedback.style.borderColor = 'var(--border-strong)';
            feedback.innerHTML = '<div style="display:flex; align-items:center; gap:0.4rem; font-weight:700; color:var(--text-main);"><i data-lucide="alert-circle" class="icon-sm"></i> <span>Connection Error</span></div><div style="margin-top:0.35rem; color:var(--text-secondary); font-size:0.85rem;">' + (data.error || 'Please check if the API key is valid.') + '</div>';
          }
        }
      } catch (e) {
        showToast('Connection failed: ' + e.message);
        if (feedback) {
          feedback.style.display = 'block';
          feedback.style.borderColor = 'var(--border-strong)';
          feedback.innerHTML = '<div style="display:flex; align-items:center; gap:0.4rem; font-weight:700; color:var(--text-main);"><i data-lucide="alert-circle" class="icon-sm"></i> <span>Request Failed</span></div><div style="margin-top:0.35rem; color:var(--text-secondary); font-size:0.85rem;">' + e.message + '</div>';
        }
      }
      refreshIcons();
    }

    // Modals
    function openAddDeckModal() {
      document.getElementById('modal-deck').classList.add('open');
    }
    function openAddCardModal() {
      if (!appState.currentDeckId) {
        showToast('Please select or create a deck first');
        return;
      }
      document.getElementById('modal-card').classList.add('open');
    }
    function openNoteModal() {
      document.getElementById('edit-note-id').value = '';
      document.getElementById('note-title-input').value = '';
      document.getElementById('note-topic-input').value = '';
      document.getElementById('note-content-input').value = '';
      document.getElementById('note-modal-title').textContent = 'Create Revision Note';
      document.getElementById('modal-note').classList.add('open');
    }
    function editNote(note) {
      document.getElementById('edit-note-id').value = note.id;
      document.getElementById('note-title-input').value = note.title;
      document.getElementById('note-topic-input').value = note.topic;
      document.getElementById('note-content-input').value = note.content;
      document.getElementById('note-modal-title').textContent = 'Edit Revision Note';
      document.getElementById('modal-note').classList.add('open');
    }
    function closeModals() {
      document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('open'));
    }

    async function submitNewDeck() {
      const title = document.getElementById('new-deck-title').value.trim();
      const category = document.getElementById('new-deck-category').value.trim();
      const desc = document.getElementById('new-deck-desc').value.trim();
      if (!title) { showToast('Please enter a title'); return; }

      const res = await fetch('/api/decks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, category, description: desc })
      });
      const data = await res.json();
      closeModals();
      document.getElementById('new-deck-title').value = '';
      document.getElementById('new-deck-category').value = '';
      document.getElementById('new-deck-desc').value = '';

      const decksRes = await fetch('/api/decks').then(r => r.json());
      appState.decks = decksRes.decks || [];
      selectDeck(data.deck.id);
      showToast('Deck created');
    }

    async function submitNewCard() {
      const front = document.getElementById('new-card-front').value.trim();
      const back = document.getElementById('new-card-back').value.trim();
      if (!front || !back) { showToast('Both front and back are required'); return; }

      await fetch('/api/decks/card', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ deck_id: appState.currentDeckId, front, back })
      });
      closeModals();
      document.getElementById('new-card-front').value = '';
      document.getElementById('new-card-back').value = '';

      const decksRes = await fetch('/api/decks').then(r => r.json());
      appState.decks = decksRes.decks || [];
      renderDecksShelf();
      renderActiveCard();
      showToast('Card added');
    }

    async function submitNote() {
      const id = document.getElementById('edit-note-id').value;
      const title = document.getElementById('note-title-input').value.trim();
      const topic = document.getElementById('note-topic-input').value.trim();
      const content = document.getElementById('note-content-input').value.trim();
      if (!title || !content) { showToast('Title and content are required'); return; }

      const res = await fetch('/api/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id, title, topic, content })
      });
      const data = await res.json();
      appState.notes = data.notes || [];
      closeModals();
      renderNotes();
      showToast('Note saved');
    }

    async function deleteNote(noteId) {
      if (!confirm('Are you sure you want to delete this note?')) return;
      const res = await fetch('/api/notes/delete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ note_id: noteId })
      });
      const data = await res.json();
      appState.notes = data.notes || [];
      renderNotes();
      showToast('Note deleted');
    }

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;

      if (e.code === 'Space') {
        e.preventDefault();
        flipActiveCard();
      } else if (e.code === 'ArrowRight') {
        nextCard();
      } else if (e.code === 'ArrowLeft') {
        prevCard();
      }
    });

    // Boot
    window.addEventListener('DOMContentLoaded', () => {
      initTheme();
      loadInitialData();
      refreshIcons();
    });
  </script>
</body>
</html>
"""
