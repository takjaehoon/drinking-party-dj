import json

with open('/Users/kimdoyun/.gemini/antigravity/scratch/drinking-party-dj/massive_tracks.json', 'r', encoding='utf-8') as f:
    tracks = json.load(f)

tracks_json = json.dumps(tracks, ensure_ascii=False, indent=2)

html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <meta name="referrer" content="strict-origin-when-cross-origin" />
  <title>술자리 AI DJ · 프로 에디션</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;900&family=Righteous&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Pretendard', '-apple-system', 'sans-serif'],
            display: ['Righteous', 'sans-serif']
          }},
          colors: {{
            neonPurple: '#a855f7',
            neonPink: '#ec4899',
            neonCyan: '#06b6d4',
            neonGreen: '#22c55e',
            neonOrange: '#f97316',
            spotifyGreen: '#1db954',
            darkBg: '#0b0c10',
            darkCard: '#15161e',
            darkElevated: '#1f212d'
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      background-color: #07080c;
      color: #f3f4f6;
      font-family: 'Pretendard', sans-serif;
      touch-action: manipulation;
      -webkit-tap-highlight-color: transparent;
      overflow-x: hidden;
      transition: background-color 0.4s ease;
    }}
    .club-mesh-bg {{
      background-color: #07080c;
      background-image: 
        radial-gradient(circle at 10% 10%, rgba(168, 85, 247, 0.22) 0%, transparent 40%),
        radial-gradient(circle at 90% 10%, rgba(6, 182, 212, 0.22) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.12) 0%, transparent 60%),
        radial-gradient(circle at 85% 85%, rgba(249, 115, 22, 0.18) 0%, transparent 45%),
        radial-gradient(circle at 15% 90%, rgba(34, 197, 94, 0.14) 0%, transparent 45%);
      background-attachment: fixed;
    }}
    /* Tactile 3D Arcade Push Button */
    .arcade-btn {{
      position: relative;
      transition: all 0.12s cubic-bezier(0.4, 0, 0.2, 1);
      border-bottom-width: 3px !important;
    }}
    .arcade-btn:active {{
      transform: translateY(2px);
      border-bottom-width: 1px !important;
    }}
    /* Flowing Rainbow Gradient for Start button */
    @keyframes flowGradient {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}
    .animate-flow-gradient {{
      background-size: 250% 250% !important;
      animation: flowGradient 4s ease infinite !important;
    }}
    /* Host Voice Waveform animation */
    @keyframes voicePulse {{
      0%, 100% {{ height: 4px; }}
      50% {{ height: 16px; }}
    }}
    .voice-bar-1 {{ animation: voicePulse 0.45s ease-in-out infinite alternate; }}
    .voice-bar-2 {{ animation: voicePulse 0.6s ease-in-out 0.12s infinite alternate; }}
    .voice-bar-3 {{ animation: voicePulse 0.35s ease-in-out 0.22s infinite alternate; }}
    .voice-bar-4 {{ animation: voicePulse 0.5s ease-in-out 0.08s infinite alternate; }}

    /* Strobe pattern around turntable platter rim */
    .turntable-rim {{
      background: repeating-conic-gradient(
        from 0deg,
        #1a1b22 0deg 6deg,
        #2d2f3c 6deg 12deg
      );
      box-shadow: 0 0 25px rgba(0, 0, 0, 0.95), inset 0 0 10px rgba(0,0,0,0.8);
    }}
    .neon-border-purple {{
      box-shadow: 0 0 20px rgba(168, 85, 247, 0.45), inset 0 0 12px rgba(168, 85, 247, 0.15);
    }}
    .neon-border-cyan {{
      box-shadow: 0 0 20px rgba(6, 182, 212, 0.45), inset 0 0 12px rgba(6, 182, 212, 0.15);
    }}
    .neon-border-pink {{
      box-shadow: 0 0 25px rgba(236, 72, 153, 0.65), inset 0 0 15px rgba(236, 72, 153, 0.2);
    }}
    @keyframes barPulse {{
      0%, 100% {{ height: 15%; }}
      50% {{ height: 100%; }}
    }}
    .visualizer-bar {{
      animation: barPulse 0.55s ease-in-out infinite alternate;
    }}
    .paused-anim {{
      animation-play-state: paused !important;
    }}
    @keyframes spinVinyl {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    .spin-vinyl {{
      animation: spinVinyl 3.2s linear infinite;
    }}
    .spin-paused {{
      animation-play-state: paused !important;
    }}
    .turntable-grooves {{
      background: radial-gradient(circle at center, #252528 0%, #17181c 25%, #0e0e12 45%, #1c1d22 65%, #0a0b0d 85%, #020204 100%);
      box-shadow: inset 0 0 10px rgba(255, 255, 255, 0.18), 0 4px 15px rgba(0,0,0,0.85);
    }}
    @keyframes strobePulse {{
      0% {{ background-color: #07080c; box-shadow: inset 0 0 60px rgba(168, 85, 247, 0.35); }}
      25% {{ background-color: #220330; box-shadow: inset 0 0 95px rgba(236, 72, 153, 0.6); }}
      50% {{ background-color: #02202e; box-shadow: inset 0 0 95px rgba(6, 182, 212, 0.6); }}
      75% {{ background-color: #2b1301; box-shadow: inset 0 0 95px rgba(249, 115, 22, 0.6); }}
      100% {{ background-color: #07080c; box-shadow: inset 0 0 60px rgba(168, 85, 247, 0.35); }}
    }}
    .strobe-active {{
      animation: strobePulse 1.4s ease-in-out infinite alternate !important;
    }}
    .strobe-active-glow {{
      box-shadow: 0 0 60px rgba(236, 72, 153, 0.8), inset 0 0 35px rgba(168, 85, 247, 0.6) !important;
    }}

    /* Real High-End Club Crowd & Laser Stage Backdrop */
    .club-stage-backdrop {{
      position: fixed;
      inset: 0;
      z-index: 0;
      background-image: 
        radial-gradient(ellipse at 50% 25%, rgba(7, 8, 12, 0.4) 0%, rgba(7, 8, 12, 0.72) 60%, #07080c 100%),
        linear-gradient(to bottom, rgba(7, 8, 12, 0.35) 0%, rgba(7, 8, 12, 0.25) 35%, rgba(7, 8, 12, 0.88) 85%, #07080c 100%),
        url('./assets/club_crowd_bg.jpg');
      background-size: cover;
      background-position: center top;
      background-repeat: no-repeat;
      pointer-events-none;
      animation: clubLaserPulse 3.5s ease-in-out infinite alternate;
    }}
    @keyframes clubLaserPulse {{
      0%, 100% {{ filter: brightness(0.95) contrast(1.05); }}
      50% {{ filter: brightness(1.22) contrast(1.15); }}
    }}

  </style>
</head>
<body class="club-mesh-bg min-h-screen flex flex-col items-center justify-start p-2.5 sm:p-5 select-none transition-all duration-300 relative">

  <!-- 🌟 High-Definition Cinematic Club Crowd & Laser Stage Backdrop -->
  <div class="club-stage-backdrop"></div>

  <!-- Native Background Audio Player -->
  <audio id="realBgmAudio" preload="auto"></audio>

  <!-- Party Sound FX Synthesizer -->
  <script>
    class PartySoundEngine {{
      constructor() {{
        this.ctx = null;
        this.isMuted = false;
      }}
      init() {{
        if (!this.ctx) {{
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
        }}
        if (this.ctx.state === 'suspended') {{
          this.ctx.resume();
        }}
      }}
      toggleMute() {{
        this.isMuted = !this.isMuted;
        const bgm = document.getElementById('realBgmAudio');
        if (bgm) bgm.muted = this.isMuted;
        return this.isMuted;
      }}
      playScratch() {{
        if (this.isMuted) return;
        this.init();
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(480, now);
        osc.frequency.exponentialRampToValueAtTime(140, now + 0.1);
        osc.frequency.exponentialRampToValueAtTime(600, now + 0.2);
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.22);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.22);
      }}
      playAirhorn() {{
        if (this.isMuted) return;
        this.init();
        const now = this.ctx.currentTime;
        [466.16, 554.37, 622.25].forEach(freq => {{
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(freq, now);
          osc.frequency.exponentialRampToValueAtTime(freq * 1.04, now + 0.22);
          gain.gain.setValueAtTime(0.22, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.25);
        }});
      }}
      playChillChime() {{
        if (this.isMuted) return;
        this.init();
        const now = this.ctx.currentTime;
        [523.25, 659.25, 783.99].forEach((freq, i) => {{
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.08);
          gain.gain.setValueAtTime(0.2, now + i * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.4);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.08);
          osc.stop(now + i * 0.08 + 0.45);
        }});
      }}
      playBassDrop() {{
        if (this.isMuted) return;
        this.init();
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(140, now);
        osc.frequency.exponentialRampToValueAtTime(35, now + 0.5);
        gain.gain.setValueAtTime(0.8, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.55);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.55);
      }}
      playSiren() {{
        if (this.isMuted) return;
        this.init();
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(650, now);
        osc.frequency.linearRampToValueAtTime(1250, now + 0.18);
        osc.frequency.linearRampToValueAtTime(650, now + 0.36);
        osc.frequency.linearRampToValueAtTime(1250, now + 0.54);
        osc.frequency.linearRampToValueAtTime(650, now + 0.72);
        gain.gain.setValueAtTime(0.35, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.78);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.78);
      }}
      playOneShot() {{
        if (this.isMuted) return;
        this.init();
        const now = this.ctx.currentTime;
        [0, 0.16, 0.32].forEach((t) => {{
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(880, now + t);
          gain.gain.setValueAtTime(0.3, now + t);
          gain.gain.exponentialRampToValueAtTime(0.01, now + t + 0.1);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + t);
          osc.stop(now + t + 0.1);
        }});
        const oscEnd = this.ctx.createOscillator();
        const gainEnd = this.ctx.createGain();
        oscEnd.type = 'sawtooth';
        oscEnd.frequency.setValueAtTime(1760, now + 0.48);
        oscEnd.frequency.exponentialRampToValueAtTime(440, now + 0.95);
        gainEnd.gain.setValueAtTime(0.45, now + 0.48);
        gainEnd.gain.exponentialRampToValueAtTime(0.01, now + 1.0);
        oscEnd.connect(gainEnd);
        gainEnd.connect(this.ctx.destination);
        oscEnd.start(now + 0.48);
        oscEnd.stop(now + 1.0);
      }}
    }}
    const soundEngine = new PartySoundEngine();
  </script>

  <!-- Main Container (Cyber-Rave DJ Console Flight Case) -->
  
  <!-- Main Container (Cyber-Rave DJ Console Flight Case) -->
  <div id="app" class="w-full max-w-md mx-auto flex flex-col min-h-[94vh] relative z-10 pb-6 bg-zinc-950/85 backdrop-blur-2xl border border-zinc-700/60 rounded-3xl p-3 sm:p-5 shadow-[0_0_60px_rgba(0,0,0,0.95)] my-1 sm:my-3">

    <!-- Top Universal Header (Pro Mixer Rack Bar) -->
    <header class="w-full flex items-center justify-between py-2 px-1 border-b border-zinc-800/80 mb-3 bg-zinc-900/50 rounded-2xl p-2.5">
      <div class="flex items-center space-x-2.5">
        <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-purple-600 to-pink-600 flex items-center justify-center text-base shadow-[0_0_12px_rgba(168,85,247,0.5)]">
          🍸
        </div>
        <div>
          <div class="flex items-center space-x-1.5">
            <h1 class="font-display tracking-wider font-black text-transparent bg-clip-text bg-gradient-to-r from-neonPurple via-neonPink to-neonCyan text-lg leading-tight">
              술자리 AI DJ
            </h1>
            <span class="px-1.5 py-0.2 rounded text-[9px] font-black bg-purple-950 text-purple-300 border border-purple-600/50">PRO 2.0</span>
          </div>
          <p class="text-[10px] text-zinc-400 tracking-wider flex items-center space-x-1 mt-0.5">
            <span class="w-1.5 h-1.5 rounded-full bg-neonGreen animate-ping"></span>
            <span class="font-mono text-zinc-300 font-semibold">LIVE MIX & MC STATION</span>
          </p>
        </div>
      </div>
      <button id="soundToggleBtn" onclick="toggleAudio()" class="arcade-btn flex items-center space-x-1 px-3 py-1.5 rounded-full bg-zinc-800/90 hover:bg-zinc-700 border border-zinc-600 border-b-zinc-950 text-xs font-bold transition">
        <span id="soundIcon">🔊</span>
        <span id="soundText" class="text-[11px] text-zinc-200">사운드 ON</span>
      </button>
    </header>

    <!-- LIVE TOAST BANNER -->
    <div id="djToast" class="hidden w-full bg-gradient-to-r from-purple-950 via-zinc-900 to-pink-950 border border-neonPurple/60 rounded-xl p-2.5 mb-2 text-center text-xs font-bold text-white shadow-lg transition-all">
      <span id="djToastText">🎧 새로운 라운드로 믹싱되었습니다!</span>
    </div>

    <!-- SCREEN 1: 상태 선택 화면 (Setup) -->
    <section id="screen-setup" class="flex-1 flex flex-col justify-between space-y-4">
      
      <!-- Hero Banner -->
      <div class="relative bg-gradient-to-br from-purple-950/60 via-zinc-900/90 to-pink-950/50 border border-purple-500/40 rounded-2xl p-4 text-center shadow-xl overflow-hidden">
        <div class="absolute -right-8 -top-8 w-28 h-28 bg-neonPurple/20 rounded-full blur-2xl pointer-events-none"></div>
        <div class="absolute -left-8 -bottom-8 w-28 h-28 bg-neonCyan/20 rounded-full blur-2xl pointer-events-none"></div>
        <span class="inline-flex items-center space-x-1 px-3 py-0.5 rounded-full text-[11px] font-black bg-purple-900/80 text-purple-200 border border-purple-500/60 mb-2 shadow">
          <span>🎧</span>
          <span>AI 실시간 맞춤 믹싱 & MC 가동</span>
        </span>
        <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight leading-snug">
          “오늘 테이블 분위기 세팅”
        </h2>
        <p class="text-xs text-zinc-300 mt-1.5 leading-relaxed">
          상황과 장르를 고르면 실시간 비트 드롭 & 맞춤 게임이 시작됩니다!
        </p>
      </div>

      <!-- 1. 모임 성격 선택 -->
      <div class="space-y-1.5">
        <label class="text-xs font-black text-zinc-200 flex items-center space-x-2">
          <span class="px-1.5 py-0.5 rounded bg-purple-950 text-neonPurple border border-purple-600/50 font-mono text-[10px]">01</span>
          <span>모임 성격</span>
        </label>
        <div class="grid grid-cols-2 gap-2 text-xs font-medium">
          <button type="button" onclick="selectChip('groupType', '미팅/과팅', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-base">💘</span>
            <span class="font-bold">미팅 · 과팅</span>
          </button>
          <button type="button" onclick="selectChip('groupType', '친구 모임', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-base">🍻</span>
            <span class="font-bold">친구 모임</span>
          </button>
          <button type="button" onclick="selectChip('groupType', '과/동아리 회식', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-base">🎓</span>
            <span class="font-bold">과 · 동아리</span>
          </button>
          <button type="button" onclick="selectChip('groupType', '회사 회식', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-base">💼</span>
            <span class="font-bold">회사 회식</span>
          </button>
        </div>
      </div>

      <!-- 2. 차수 선택 -->
      <div class="space-y-1.5">
        <label class="text-xs font-black text-zinc-200 flex items-center space-x-2">
          <span class="px-1.5 py-0.5 rounded bg-cyan-950 text-neonCyan border border-cyan-600/50 font-mono text-[10px]">02</span>
          <span>지금 몇 차?</span>
        </label>
        <div class="grid grid-cols-3 gap-2 text-xs font-medium">
          <button type="button" onclick="selectChip('round', '1차', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-center font-black">
            1차
          </button>
          <button type="button" onclick="selectChip('round', '2차', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-center font-black">
            2차
          </button>
          <button type="button" onclick="selectChip('round', '3차+', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-center font-black">
            3차+
          </button>
        </div>
      </div>

      <!-- 3. 현재 분위기 선택 -->
      <div class="space-y-1.5">
        <label class="text-xs font-black text-zinc-200 flex items-center space-x-2">
          <span class="px-1.5 py-0.5 rounded bg-pink-950 text-neonPink border border-pink-600/50 font-mono text-[10px]">03</span>
          <span>현재 분위기 체감</span>
        </label>
        <div class="grid grid-cols-3 gap-2 text-xs font-medium">
          <button type="button" onclick="selectChip('atmosphere', '어색함', this)" class="chip-btn arcade-btn py-2.5 px-2 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-center">
            <span class="block text-base mb-0.5">❄️</span>
            <span class="font-bold text-[11px]">아직 어색함</span>
          </button>
          <button type="button" onclick="selectChip('atmosphere', '올라옴', this)" class="chip-btn arcade-btn py-2.5 px-2 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-center">
            <span class="block text-base mb-0.5">🥂</span>
            <span class="font-bold text-[11px]">슬슬 올라옴</span>
          </button>
          <button type="button" onclick="selectChip('atmosphere', '폭발', this)" class="chip-btn arcade-btn py-2.5 px-2 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-center">
            <span class="block text-base mb-0.5">🔥</span>
            <span class="font-bold text-[11px]">텐션 폭발</span>
          </button>
        </div>
      </div>

      <!-- 4. 선호 음악 장르 선택 -->
      <div class="space-y-1.5">
        <label class="text-xs font-black text-zinc-200 flex items-center space-x-2">
          <span class="px-1.5 py-0.5 rounded bg-emerald-950 text-neonGreen border border-emerald-600/50 font-mono text-[10px]">04</span>
          <span>선호 음악 장르</span>
        </label>
        <div class="grid grid-cols-2 gap-2 text-xs font-medium">
          <button type="button" onclick="selectChip('genre', 'ALL', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-lg">🔀</span>
            <div>
              <div class="font-black text-white text-xs">전체 올장르</div>
              <div class="text-[10px] text-zinc-400">힙합·K-POP·밴드 올믹스</div>
            </div>
          </button>
          <button type="button" onclick="selectChip('genre', 'HIPHOP', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-lg">🧢</span>
            <div>
              <div class="font-black text-white text-xs">힙합 · 랩</div>
              <div class="text-[10px] text-zinc-400">국힙 & 트렌디 외힙</div>
            </div>
          </button>
          <button type="button" onclick="selectChip('genre', 'KPOP', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-lg">✨</span>
            <div>
              <div class="font-black text-white text-xs">K-POP 댄스</div>
              <div class="text-[10px] text-zinc-400">아이돌 & 흥폭발 댄스</div>
            </div>
          </button>
          <button type="button" onclick="selectChip('genre', 'BAND', this)" class="chip-btn arcade-btn py-2.5 px-3 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-left flex items-center space-x-2.5">
            <span class="text-lg">🎸</span>
            <div>
              <div class="font-black text-white text-xs">밴드 · 인디 · 팝</div>
              <div class="text-[10px] text-zinc-400">떼창 락 & 감성 팝송</div>
            </div>
          </button>
        </div>
      </div>

      <!-- 5. 재생 모드 선택 -->
      <div class="space-y-1.5">
        <label class="text-xs font-black text-zinc-200 flex items-center justify-between">
          <span class="flex items-center space-x-2">
            <span class="px-1.5 py-0.5 rounded bg-cyan-950 text-neonCyan border border-cyan-600/50 font-mono text-[10px]">05</span>
            <span>술자리 진행 모드</span>
          </span>
          <span class="text-[10px] text-zinc-400 font-normal">진행 중 언제든 변경 가능</span>
        </label>
        <div class="grid grid-cols-2 gap-2 text-xs font-medium">
          <button type="button" onclick="selectPlayMode('automix', this)" class="mode-chip arcade-btn py-2.5 px-2 rounded-xl border border-neonCyan border-b-cyan-400 bg-cyan-950/80 text-white text-center shadow-[0_0_15px_rgba(6,182,212,0.4)]">
            <span class="block font-black text-xs">⚡️ 30초 자동믹싱 (추천)</span>
            <span class="text-[9px] text-cyan-200/90 block mt-0.5">30초 재생 후 다음 라운드로 빠른 전환</span>
          </button>
          <button type="button" onclick="selectPlayMode('manual', this)" class="mode-chip arcade-btn py-2.5 px-2 rounded-xl border border-zinc-700/80 border-b-zinc-950 bg-zinc-900/90 text-zinc-300 text-center">
            <span class="block font-bold text-xs">⏸ 수동 믹싱</span>
            <span class="text-[9px] text-zinc-400 block mt-0.5">현재 분위기 유지 & 직접 다음 곡 넘기기</span>
          </button>
        </div>
        <div class="text-[9.5px] text-zinc-400 text-center mt-1.5 font-medium">
          💡 완곡을 듣고 싶을 땐 상단의 <span class="text-spotifyGreen font-bold">🟢 Spotify 완곡</span> 버튼을 누르면 즉시 연결됩니다!
        </div>
      </div>

      <!-- Start Button Bar -->
      <div class="pt-2 pb-2">
        <button id="startSessionBtn" onclick="startDjSession()" disabled class="arcade-btn w-full py-4 px-5 rounded-2xl font-black text-base flex flex-col items-center justify-center space-y-0.5 transition duration-300 bg-zinc-900 text-zinc-600 cursor-not-allowed border border-zinc-800 border-b-zinc-950">
          <div class="flex items-center space-x-2">
            <span class="text-xl">🍻</span>
            <span id="startBtnText">4가지 항목을 선택해 주세요</span>
          </div>
          <span id="startBtnSub" class="text-[11px] font-normal text-zinc-500">모임 성격 · 차수 · 분위기 · 장르 선택 대기 중</span>
        </button>
      </div>
    </section>

    <!-- SCREEN 2: AI DJ & MC 진행 데스크 (Main Console) -->
    <section id="screen-console" class="hidden flex-1 flex flex-col justify-between space-y-3">
      
      <!-- Top Action Bar with Strobe & Session Tag -->
      <div class="flex items-center justify-between px-1">
        <button onclick="backToSetup()" class="arcade-btn text-xs font-bold text-zinc-300 hover:text-white flex items-center space-x-1 py-1.5 px-3 rounded-xl bg-zinc-900/90 border border-zinc-700 border-b-zinc-950 transition">
          <span>⚙️</span>
          <span>상황 재설정</span>
        </button>
        
        <div class="flex items-center space-x-1.5 px-3 py-1 rounded-full bg-purple-950/90 border border-purple-500/70 text-xs font-black text-purple-200 shadow-[0_0_12px_rgba(168,85,247,0.4)]">
          <span class="w-2 h-2 rounded-full bg-neonPurple animate-ping"></span>
          <span id="consoleSessionTag">미팅 · 1차 · 올장르 · NORMAL</span>
        </div>

        <button id="strobeToggleBtn" onclick="toggleStrobe()" class="arcade-btn px-3 py-1.5 rounded-full bg-zinc-900 hover:bg-pink-950/90 border border-zinc-700 border-b-zinc-950 hover:border-pink-500 text-[11px] font-black text-zinc-300 hover:text-pink-300 flex items-center space-x-1 transition shadow" title="클럽 사이키 조명 효과">
          <span>🚨</span>
          <span id="strobeText">사이키 OFF</span>
        </button>
      </div>

      <!-- Player Deck (Real Audio Stream with 3D Turntable, Visualizer & Controls) -->
      <div class="bg-gradient-to-b from-zinc-900 via-zinc-950 to-zinc-900 border-2 border-purple-500/50 rounded-3xl p-3.5 sm:p-4 shadow-2xl relative overflow-hidden neon-border-purple">
        <!-- Rack screws visual detail -->
        <div class="absolute top-2 left-2 w-2 h-2 rounded-full bg-zinc-600 border border-zinc-800 opacity-60"></div>
        <div class="absolute top-2 right-2 w-2 h-2 rounded-full bg-zinc-600 border border-zinc-800 opacity-60"></div>
        <div class="absolute -top-10 -right-10 w-40 h-40 bg-neonPurple/20 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -bottom-10 -left-10 w-40 h-40 bg-neonCyan/20 rounded-full blur-3xl pointer-events-none"></div>

        <div class="flex items-center space-x-3 sm:space-x-4">
          <!-- 3D Turntable Platter with Grooves & Spinning Vinyl -->
          <div class="relative shrink-0">
            <div class="w-24 h-24 sm:w-28 sm:h-28 rounded-full turntable-rim p-1.5 border-2 border-zinc-600/80 shadow-2xl relative flex items-center justify-center">
              <!-- Spinning Vinyl Disc -->
              <div id="vinylDisc" onclick="handleVinylScratch()" class="w-full h-full rounded-full turntable-grooves spin-vinyl relative flex items-center justify-center cursor-pointer shadow-inner active:scale-95 transition-transform" title="터치하면 DJ 스크래치 발동!">
                <!-- Center Label Artwork -->
                <div class="w-11 h-11 sm:w-13 sm:h-13 rounded-full overflow-hidden border-2 border-neonCyan shadow-lg relative flex items-center justify-center pointer-events-none">
                  <img id="trackArtwork" src="" alt="Album Art" class="w-full h-full object-cover" />
                  <!-- Vinyl Spindle Hole -->
                  <div class="w-2.5 h-2.5 rounded-full bg-black border border-zinc-300 absolute"></div>
                </div>
              </div>
              <!-- Play / Pause Overlay Button on center -->
              <button onclick="togglePlayPause()" class="absolute inset-0 m-auto w-8 h-8 rounded-full bg-black/70 hover:bg-black/90 backdrop-blur-sm flex items-center justify-center text-xs text-white border border-white/40 shadow-xl active:scale-90 transition z-10" title="재생/일시정지">
                <span id="playStateBadge">▶</span>
              </button>
              <!-- Tonearm visual graphic -->
              <div class="absolute -top-1 -right-1 w-3 h-8 border-r-2 border-t-2 border-zinc-400 rounded-tr-lg pointer-events-none opacity-80"></div>
            </div>
            <!-- LIVE Strobe Badge -->
            <span class="absolute -bottom-1 left-1/2 -translate-x-1/2 bg-red-600 text-[9px] font-black tracking-wider text-white px-2 py-0.2 rounded-full border border-black shadow-md flex items-center space-x-1">
              <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
              <span>LIVE</span>
            </span>
          </div>

          <!-- Track Info & 16-Band Equalizer Spectrum -->
          <div class="flex-1 min-w-0">
            <div class="flex items-center justify-between">
              <span id="trackGenreBadge" class="text-[10px] font-black px-2 py-0.5 rounded-md bg-zinc-900 text-neonCyan border border-cyan-700/60 shadow-sm">
                HIP-HOP · 120 BPM
              </span>
              <span id="trackRoundCount" class="text-[10px] font-mono font-bold text-neonPurple">
                ROUND 1
              </span>
            </div>
            <h3 id="trackTitle" class="text-base sm:text-lg font-black text-white truncate mt-1 tracking-tight">
              METEOR
            </h3>
            <p id="trackArtist" class="text-xs text-zinc-300 truncate font-semibold">
              CHANGMO
            </p>

            <!-- 16-Band Animated LED Spectrum Analyzer -->
            <div id="spectrumVisualizer" class="flex items-end space-x-0.5 sm:space-x-1 h-5 mt-1.5 pt-1 overflow-hidden" title="실시간 오디오 이퀄라이저">
              <!-- Generated by initSpectrum() -->
            </div>

            <!-- Audio Progress Bar & Time -->
            <div class="mt-1.5 pt-1 border-t border-zinc-800/80">
              <div class="w-full bg-zinc-800 rounded-full h-1.5 overflow-hidden relative cursor-pointer" onclick="seekAudio(event)" title="클릭하여 구간 이동">
                <div id="audioProgressBar" class="bg-gradient-to-r from-neonPurple via-neonPink to-neonCyan h-full w-0 transition-all duration-150"></div>
              </div>
              <div class="flex items-center justify-between text-[10px] text-zinc-400 mt-1">
                <span id="audioCurrentTime" class="font-mono text-zinc-300">0:00</span>
                <span id="audioStatusText" class="text-neonCyan font-bold">비트 스트리밍</span>
                <span id="audioDuration" class="font-mono text-zinc-300">0:30</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Mode Switcher & Transport Controls -->
        <div class="flex items-center justify-between mt-3 pt-3 border-t border-zinc-800/80">
          
          <!-- Mode Toggle Pills: ⚡️ 30초 믹싱 vs ⏸ 수동 믹싱 vs 🟢 Spotify 완곡 -->
          <div class="flex items-center space-x-1.5 bg-zinc-950/90 p-1 rounded-xl border border-zinc-800 text-[11px]">
            <button onclick="setPlayMode('automix')" id="modeBtnMix" class="arcade-btn px-2.5 py-1 rounded-lg font-black bg-neonCyan text-black shadow-[0_0_12px_rgba(6,182,212,0.5)] border-b-cyan-700 transition" title="30초 후 다음 라운드로 자동 믹싱">
              ⚡️ 30초 믹싱
            </button>
            <button onclick="setPlayMode('manual')" id="modeBtnManual" class="arcade-btn px-2.5 py-1 rounded-lg font-bold text-zinc-400 hover:text-white border-b-transparent transition" title="수동으로 다음 곡 넘기기">
              ⏸ 수동 믹싱
            </button>
            <button onclick="openSpotifyDirect()" id="modeBtnSpotify" class="arcade-btn px-2.5 py-1 rounded-lg font-black bg-emerald-950 text-spotifyGreen border border-emerald-700 border-b-emerald-950 hover:bg-emerald-900 shadow-[0_0_10px_rgba(29,185,84,0.3)] flex items-center space-x-1 transition" title="스포티파이 앱에서 3~4분 완곡 재생">
              <span>🟢 Spotify 완곡</span>
              <span>↗</span>
            </button>
          </div>

          <!-- Transport: Prev & Play & Next -->
          <div class="flex items-center space-x-1.5">
            <!-- Prev Track Button -->
            <button onclick="handleHistoryNav('prev')" class="arcade-btn p-2 rounded-xl bg-zinc-800 hover:bg-zinc-700 text-zinc-200 hover:text-white border border-zinc-600 border-b-zinc-950 shadow" title="이전 곡">
              <span class="text-xs">⏮</span>
            </button>

            <!-- Play / Pause Button -->
            <button onclick="togglePlayPause()" class="arcade-btn p-2 rounded-xl bg-neonPurple text-black font-black border border-purple-400 border-b-purple-900 shadow-[0_0_12px_rgba(168,85,247,0.5)]" title="재생/일시정지">
              <span id="deskPlayIcon" class="text-xs">⏸</span>
            </button>

            <!-- Next Track Button -->
            <button onclick="handleHistoryNav('next')" class="arcade-btn p-2 rounded-xl bg-zinc-800 hover:bg-zinc-700 text-zinc-200 hover:text-white border border-zinc-600 border-b-zinc-950 shadow" title="다음 곡">
              <span class="text-xs">⏭</span>
            </button>
          </div>
        </div>
      </div>

                  <!-- 🎧 DJ TRACK NOTE (곡 한줄 설명 / 술자리 가이드 카드) -->
      <div id="djTrackNoteCard" class="bg-gradient-to-r from-purple-950/90 via-zinc-900/90 to-zinc-950 border-2 border-neonPurple/70 rounded-2xl p-3 shadow-[0_0_20px_rgba(168,85,247,0.35)] space-y-1.5 transition duration-300">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-1.5">
            <span class="text-sm animate-pulse">🎧</span>
            <span class="text-xs font-black tracking-wider text-purple-300">DJ TRACK NOTE (한줄 설명)</span>
            <span class="text-[9px] px-1.5 py-0.5 rounded-full bg-purple-900/60 text-purple-200 border border-purple-500/40 font-bold">DJ PICK</span>
          </div>
          <button onclick="openSpotifyDirect()" class="text-[10px] font-black text-spotifyGreen hover:text-emerald-300 flex items-center space-x-1 bg-emerald-950/80 px-2 py-0.5 rounded-lg border border-emerald-700/60 transition" title="스포티파이에서 완곡 듣기">
            <span>🟢 Spotify 완곡</span>
            <span>↗</span>
          </button>
        </div>
        <div id="djTrackNoteText" class="text-xs sm:text-sm font-bold text-zinc-100 text-center leading-relaxed tracking-wide py-2.5 px-3 bg-black/60 rounded-xl border border-purple-500/30 shadow-inner">
          "DJ 추천 코멘트 불러오는 중..."
        </div>
        <div class="flex items-center justify-between text-[9.5px] text-zinc-400 px-1 pt-0.5">
          <span>🍻 이 곡에 어울리는 술자리 바이브를 즐겨보세요!</span>
          <span class="text-purple-300/90 font-semibold">술자리 맞춤 BGM 🎶</span>
        </div>
      </div>

      <!-- DJ LIVE FX LAUNCHPAD (4-PAD INTERACTIVE SOUNDBOARD) -->
      <div class="bg-gradient-to-r from-zinc-900 via-zinc-950 to-zinc-900 border-2 border-zinc-700/70 rounded-2xl p-2.5 shadow-xl">
        <div class="flex items-center justify-between px-1 mb-1.5">
          <div class="flex items-center space-x-1.5">
            <span class="text-xs">🎛</span>
            <span class="text-[11px] font-black tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-neonPurple via-neonPink to-neonCyan">DJ LIVE SOUNDPAD</span>
          </div>
          <span class="text-[9px] font-bold text-zinc-400">누르면 즉시 터지는 사운드 FX</span>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
          <button onclick="triggerSoundpad('horn', this)" class="arcade-btn py-2.5 px-1 rounded-xl bg-gradient-to-b from-purple-900 to-purple-950 hover:from-purple-800 hover:to-purple-900 border border-purple-500/70 border-b-purple-950 text-purple-200 flex flex-col items-center justify-center shadow-[0_0_12px_rgba(168,85,247,0.3)]">
            <span class="text-base">📢</span>
            <span class="text-[10px] font-black mt-0.5 tracking-tight">에어혼</span>
          </button>
          <button onclick="triggerSoundpad('drop', this)" class="arcade-btn py-2.5 px-1 rounded-xl bg-gradient-to-b from-pink-900 to-pink-950 hover:from-pink-800 hover:to-pink-900 border border-pink-500/70 border-b-pink-950 text-pink-200 flex flex-col items-center justify-center shadow-[0_0_12px_rgba(236,72,153,0.3)]">
            <span class="text-base">💥</span>
            <span class="text-[10px] font-black mt-0.5 tracking-tight">베이스드롭</span>
          </button>
          <button onclick="triggerSoundpad('siren', this)" class="arcade-btn py-2.5 px-1 rounded-xl bg-gradient-to-b from-amber-800 to-amber-950 hover:from-amber-700 hover:to-amber-900 border border-amber-500/70 border-b-amber-950 text-amber-200 flex flex-col items-center justify-center shadow-[0_0_12px_rgba(245,158,11,0.3)]">
            <span class="text-base">🚨</span>
            <span class="text-[10px] font-black mt-0.5 tracking-tight">싸이렌</span>
          </button>
          <button onclick="triggerSoundpad('oneshot', this)" class="arcade-btn py-2.5 px-1 rounded-xl bg-gradient-to-b from-cyan-900 to-cyan-950 hover:from-cyan-800 hover:to-cyan-900 border border-cyan-500/70 border-b-cyan-950 text-cyan-200 flex flex-col items-center justify-center shadow-[0_0_12px_rgba(6,182,212,0.3)]">
            <span class="text-base">🥂</span>
            <span class="text-[10px] font-black mt-0.5 tracking-tight">원샷 카운트</span>
          </button>
        </div>
      </div>

      <!-- AI MC Dialogue Bubble (Live On-Air Studio with bouncing voice waveform) -->
      <div class="relative bg-gradient-to-br from-zinc-900 via-zinc-950 to-zinc-900 border-2 border-purple-500/60 rounded-2xl p-3.5 shadow-xl">
        <div class="absolute -top-3 left-4 bg-gradient-to-r from-purple-600 to-pink-600 text-white px-2.5 py-0.5 rounded-full font-black text-[11px] flex items-center space-x-1.5 shadow-lg border border-purple-300/40">
          <span>🎙️</span>
          <span>AI DJ 호스트 ON AIR</span>
          <!-- Animated Voice Waveform Bars -->
          <div class="flex items-end space-x-0.5 h-3 px-0.5">
            <span class="w-0.5 bg-neonGreen rounded-full voice-bar-1 inline-block"></span>
            <span class="w-0.5 bg-neonCyan rounded-full voice-bar-2 inline-block"></span>
            <span class="w-0.5 bg-neonPink rounded-full voice-bar-3 inline-block"></span>
            <span class="w-0.5 bg-neonGreen rounded-full voice-bar-4 inline-block"></span>
          </div>
        </div>
        <p id="mcBanterText" class="text-sm font-bold text-zinc-100 mt-1 leading-snug tracking-tight">
          “오늘 모임 성격과 차수에 맞춘 실시간 AI 맞춤 믹싱 & 토크를 가동합니다! 🍻”
        </p>
      </div>

      <!-- Centerpiece Party Mission / Game Card -->
      <div id="missionContainer" class="flex-1 bg-gradient-to-b from-zinc-900 via-black to-zinc-950 border-2 border-neonCyan/50 rounded-2xl p-4 flex flex-col justify-between shadow-2xl neon-border-cyan transition-all">
        <div>
          <div class="flex items-center justify-between mb-1">
            <span id="missionTag" class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-cyan-950 text-cyan-200 border border-cyan-500/60 shadow">
              🎯 이번 라운드 미션
            </span>
            <span class="text-[10px] text-zinc-400 font-bold" id="missionCategoryTag">테이블 공통</span>
          </div>
          <h2 id="missionTitle" class="text-lg sm:text-xl font-black text-white tracking-tight mt-1 leading-tight">
            상황 맞춤 술자리 미션
          </h2>
          <p id="missionDesc" class="text-xs text-zinc-300 mt-1.5 leading-relaxed">
            모임 성격과 차수에 맞춰 자연스러운 아이스브레이킹 및 술자리 게임이 펼쳐집니다!
          </p>
        </div>

        <div class="pt-2">
          <button onclick="openGameModal()" class="arcade-btn w-full py-2.5 px-3 rounded-xl bg-zinc-800/90 hover:bg-zinc-700 border border-zinc-600 border-b-zinc-950 text-xs font-black text-zinc-100 flex items-center justify-center space-x-1.5 shadow">
            <span>🎲</span>
            <span id="ruleBtnLabel">3초 요약 룰 보기</span>
          </button>
        </div>
      </div>

      <!-- 4-Button Tension Controller Panel -->
      <div class="space-y-1.5 pt-1">
        <div class="flex items-center justify-between px-1">
          <span class="text-[10px] font-black text-zinc-400 tracking-wider">DJ INTERACTION CONTROL</span>
          <span class="text-[10px] text-neonPink font-black">⚡️ 터치 시 즉시 새로운 비트 & 게임 출격!</span>
        </div>
        
        <div class="grid grid-cols-2 gap-2">
          <!-- Button 1: Tension UP -->
          <button onclick="handleTensionAction('up')" class="arcade-btn py-3.5 px-2 rounded-xl font-black text-xs sm:text-sm bg-gradient-to-r from-amber-500 via-orange-600 to-red-600 hover:from-amber-400 hover:to-red-500 text-white shadow-[0_0_20px_rgba(249,115,22,0.45)] border-t border-amber-300/40 border-b-4 border-b-red-950 flex items-center justify-center space-x-1">
            <span class="text-base">🔥</span>
            <span>텐션 올려! (새 곡)</span>
          </button>

          <!-- Button 2: Chill Down -->
          <button onclick="handleTensionAction('down')" class="arcade-btn py-3.5 px-2 rounded-xl font-black text-xs sm:text-sm bg-gradient-to-r from-cyan-900 via-teal-900 to-slate-900 hover:from-cyan-800 hover:to-slate-800 text-cyan-200 border-t border-cyan-400/30 border-b-4 border-b-cyan-950 shadow-[0_0_15px_rgba(6,182,212,0.3)] flex items-center justify-center space-x-1">
            <span class="text-base">😌</span>
            <span>조금 낮춰 (감성)</span>
          </button>

          <!-- Button 3: Keep Vibe -->
          <button onclick="handleTensionAction('keep')" class="arcade-btn py-3.5 px-2 rounded-xl font-black text-xs sm:text-sm bg-gradient-to-r from-purple-900 via-fuchsia-950 to-indigo-950 hover:from-purple-800 hover:to-indigo-900 text-purple-200 border-t border-purple-400/30 border-b-4 border-b-purple-950 shadow-[0_0_15px_rgba(168,85,247,0.3)] flex items-center justify-center space-x-1">
            <span class="text-base">🎵</span>
            <span>이 느낌 계속</span>
          </button>

          <!-- Button 4: Next Track -->
          <button onclick="handleTensionAction('next')" class="arcade-btn py-3.5 px-2 rounded-xl font-black text-xs sm:text-sm bg-gradient-to-r from-emerald-900 via-teal-950 to-slate-900 hover:from-emerald-800 hover:to-slate-800 text-emerald-200 border-t border-emerald-400/30 border-b-4 border-b-emerald-950 shadow-[0_0_15px_rgba(34,197,94,0.3)] flex items-center justify-center space-x-1">
            <span class="text-base">⏭</span>
            <span>다음 곡 믹싱</span>
          </button>
        </div>
      </div>

    </section>

    <!-- SCREEN 3: 게임 설명 바텀 시트 / 모달 -->
    <div id="gameRuleModal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-end sm:items-center justify-center p-0 sm:p-4">
      <div class="w-full max-w-md bg-zinc-950/95 border-t sm:border-2 border-purple-500/60 rounded-t-3xl sm:rounded-3xl p-5 shadow-2xl neon-border-purple">
        <div class="flex items-center justify-between pb-3 border-b border-zinc-800">
          <div class="flex items-center space-x-2">
            <span class="text-xl">🎲</span>
            <h3 id="modalTitle" class="text-lg font-black text-white">게임 룰</h3>
          </div>
          <button onclick="closeGameModal()" class="text-zinc-400 hover:text-white text-xl p-1 font-bold">✕</button>
        </div>
        <div class="py-4 space-y-2.5">
          <div class="flex items-start space-x-3 bg-zinc-900/90 p-3 rounded-xl border border-zinc-800">
            <span class="w-5 h-5 rounded-full bg-neonPurple text-black font-black text-xs flex items-center justify-center shrink-0">1</span>
            <p class="text-xs text-zinc-200" id="ruleStep1"></p>
          </div>
          <div class="flex items-start space-x-3 bg-zinc-900/90 p-3 rounded-xl border border-zinc-800">
            <span class="w-5 h-5 rounded-full bg-neonPink text-white font-black text-xs flex items-center justify-center shrink-0">2</span>
            <p class="text-xs text-zinc-200" id="ruleStep2"></p>
          </div>
          <div class="flex items-start space-x-3 bg-zinc-900/90 p-3 rounded-xl border border-zinc-800">
            <span class="w-5 h-5 rounded-full bg-neonCyan text-black font-black text-xs flex items-center justify-center shrink-0">3</span>
            <p class="text-xs text-zinc-200" id="ruleStep3"></p>
          </div>
        </div>
        <button onclick="closeGameModal()" class="arcade-btn w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-neonPurple to-neonPink font-black text-sm text-white shadow-lg border-b-4 border-b-purple-950">
          닫고 바로 게임 시작하기 🍻
        </button>
      </div>
    </div>

    <!-- SCREEN 4: (Cleaned up - Full songs open directly via Spotify) -->
  </div>

  <!-- Database of 77 Real Tracks & 36 Missions & 36 MC Banters -->
  <script>
    const ALL_TRACKS = {tracks_json};


    // Situation-Aware Missions Database by (groupType -> round)
    const SITUATION_MISSIONS = {{
  "미팅/과팅": {{
    "1차": [
      {{
        "title": "깻잎논쟁 & 애인 밸런스 토크",
        "desc": "내 애인이 내 친구 깻잎 떼어주기 vs 패딩 지퍼 올려주기! 각자 선택하고 솔직한 이유 털기!",
        "ruleTitle": "미팅 밸런스 룰",
        "steps": [
          "하나, 둘, 셋에 손가락으로 둘 중 하나를 동시에 가리킵니다.",
          "의견이 갈린 사람들끼리 불꽃 튀는 유쾌한 토론 진행!",
          "취향 통하는 사람끼리 눈맞춤하며 가볍게 첫 잔 짠!"
        ]
      }},
      {{
        "title": "MBTI & 첫 느낌 추측 배틀",
        "desc": "맞은편 사람이 E일까 I일까? T일까 F일까? 서로의 MBTI를 조심스럽게 추측해 맞히기!",
        "ruleTitle": "MBTI 맞히기 룰",
        "steps": [
          "맞은편 사람의 MBTI 4자리를 추측해서 말합니다.",
          "실제 MBTI를 공개하고 3개 이상 맞히면 맞힌 사람에게 박수!",
          "틀린 사람은 가볍게 한 모금 마시며 자연스럽게 스몰토크 시작."
        ]
      }},
      {{
        "title": "호구조사 금지! 3문 3답 스피드 토크",
        "desc": "나이/학번 묻기 금지! '주말에 뭐 해?', '최근 빠진 음식은?' 등 센스 있는 취향 질문 던지기.",
        "ruleTitle": "3문 3답 룰",
        "steps": [
          "지목된 사람이 5초 안에 질문에 빠르게 답합니다.",
          "대답을 듣고 바로 다른 사람에게 다른 취향 질문 토스!",
          "취향 겹치는 사람 발견하면 하이파이브하고 건배!"
        ]
      }},
      {{
        "title": "손병호 게임 (미팅 순한맛)",
        "desc": "‘오늘 향수 뿌리고 온 사람’, ‘흰색 옷 입은 사람’ 등 가벼운 조건으로 손가락 접기!",
        "ruleTitle": "손병호 룰",
        "steps": [
          "다섯 손가락을 펴고 돌아가며 센스 있는 조건을 하나씩 외칩니다.",
          "해당되는 사람은 손가락을 접습니다.",
          "가장 먼저 다 접은 사람이 맞은편 사람과 함께 건배!"
        ]
      }},
      {{
        "title": "연애 취향 밸런스 게임",
        "desc": "‘매일 칼답 연락 vs 하루 한두 번 통화’, ‘연상 vs 연하’ 솔직하게 가리키기!",
        "ruleTitle": "연애관 토크 룰",
        "steps": [
          "셋 셀 때 동시에 손가락으로 한쪽을 가리킵니다.",
          "취향이 찰떡같이 통하는 남녀 발견 시 환호!",
          "서로 잔을 채워주며 분위기를 한층 훈훈하게 만듭니다."
        ]
      }},
      {{
        "title": "음악 1초 킬링파트 퀴즈",
        "desc": "지금 배경에 나오는 노래 제목 3초 안에 맞히기! 가장 먼저 맞힌 사람이 승리!",
        "ruleTitle": "음악 퀴즈 룰",
        "steps": [
          "BGM 전주나 보컬을 듣고 제목을 가장 먼저 외칩니다.",
          "정답 맞힌 사람이 원하는 파트너와 함께 기분 좋게 짠!",
          "모두 함께 노래 따라 부르며 어색함 날리기."
        ]
      }},
      {{
        "title": "첫 잔 원샷 텔레파시 게임",
        "desc": "‘하나, 둘, 셋’에 동시에 원샷할지 반 꺾을지 선택! 마음이 통한 사람끼리 하이파이브!",
        "ruleTitle": "텔레파시 룰",
        "steps": [
          "다 같이 술잔을 들고 신호에 맞춰 마십니다.",
          "원샷파와 반샷파로 나뉘어 서로 웃으며 인사!",
          "자연스럽게 술잔 다시 채워주며 말문 트기."
        ]
      }},
      {{
        "title": "플레이리스트 최애곡 1곡 공유",
        "desc": "노래방 가면 무조건 부르는 애창곡이나 요즘 무한반복 중인 노래 하나씩 소개하기.",
        "ruleTitle": "음악 취향 룰",
        "steps": [
          "각자 최애 아티스트나 노래 제목을 말합니다.",
          "취향이 겹치는 사람끼리 폭풍 공감 대화!",
          "DJ가 해당 장르로 선곡 이어갑니다."
        ]
      }},
      {{
        "title": "휴양지 여행 스타일 토크",
        "desc": "‘에메랄드빛 휴양지에서 누워있기 vs 핫플 도심 하루 3만 보 관광’ 밸런스 선택!",
        "ruleTitle": "여행 밸런스 룰",
        "steps": [
          "손가락으로 본인 여행 스타일을 가리킵니다.",
          "함께 여행 가면 꿀잼일 것 같은 조합 찾기!",
          "잘 맞는 사람들끼리 잔 부딪히기."
        ]
      }},
      {{
        "title": "카톡 프로필 & 배경화면 TMI",
        "desc": "내 폰 배경화면이나 최근 카톡 프사 고른 비하인드 스토리 10초 공유!",
        "ruleTitle": "프사 TMI 룰",
        "steps": [
          "각자 폰 배경화면이나 프사를 살짝 보여줍니다.",
          "반려동물, 여행지 사진 등 자연스러운 대화 소재 발굴!",
          "따뜻한 칭찬과 함께 기분 좋게 짠!"
        ]
      }}
    ],
    "2차": [
      {{
        "title": "자리 바꾸기 & 남녀 짝 체인지",
        "desc": "분위기 리프레시! 제비뽑기나 가위바위보로 자리를 섞어 새로운 짝꿍과 대화하기!",
        "ruleTitle": "자리 바꾸기 룰",
        "steps": [
          "술래가 정한 규칙대로 자리를 한 칸씩 이동하거나 섞습니다.",
          "새로 옆자리가 된 짝꿍에게 서로 술을 따라줍니다.",
          "새로운 케미를 기대하며 다 같이 잔 부딪히기!"
        ]
      }},
      {{
        "title": "귓속말 게임 (스릴만점 심쿵)",
        "desc": "귓속말로 비밀 질문을 속삭이고, 지목당한 사람이 질문을 알고 싶으면 한 잔 마시기!",
        "ruleTitle": "귓속말 룰",
        "steps": [
          "옆사람 귓가에 '이 테이블에서 가장 매력적인 사람은?' 등 질문 속삭이기.",
          "질문을 들은 사람이 대상자를 손가락으로 콕 가리킵니다.",
          "지목된 사람이 질문이 뭔지 알고 싶다면 술 한 잔 마시고 공개!"
        ]
      }},
      {{
        "title": "시크릿 호감 투표 (시그널 보내기)",
        "desc": "‘나랑 데이트 코스 제일 잘 맞을 것 같은 사람’ 셋 세고 동시에 가리키기!",
        "ruleTitle": "시그널 매칭 룰",
        "steps": [
          "하나, 둘, 셋에 서로 동시에 마음속 원픽을 가리킵니다.",
          "서로를 동시에 지목한 '쌍방 매칭' 탄생 시 환호와 축하주!",
          "엇갈린 사람들은 쿨하게 웃으며 다 함께 원샷!"
        ]
      }},
      {{
        "title": "아파트 게임 (텐션 급상승)",
        "desc": "손을 무작위로 층층이 쌓고, 술래가 부른 층수에 손이 걸린 사람이 마시기!",
        "ruleTitle": "아파트 룰",
        "steps": [
          "아-파트 아파트 구호에 맞춰 손을 층층이 포갭니다.",
          "술래가 원하는 층수(예: 12층)를 외치면 맨 밑 손부터 숫자를 셉니다.",
          "해당 층수에 걸린 사람이 시원하게 한 잔!"
        ]
      }},
      {{
        "title": "눈빛 3초 교환 챌린지",
        "desc": "맞은편 파트너와 지그시 눈을 마주치고 먼저 웃거나 시선 피한 사람이 패배!",
        "ruleTitle": "눈빛 배틀 룰",
        "steps": [
          "3초 동안 서로의 눈을 조용히 응시합니다.",
          "부끄러워서 빵 터지거나 먼저 고개 돌린 사람이 마시기!",
          "심쿵 모먼트 즐기며 다 함께 짠!"
        ]
      }},
      {{
        "title": "더 게임 오브 데스 (미팅 에디션)",
        "desc": "신나는 인트로 구호와 함께 손가락으로 누군가를 가리키고 숫자를 셉니다!",
        "ruleTitle": "데스 게임 룰",
        "steps": [
          "아싸 너 너 너! 구호와 함께 술래가 숫자를 부릅니다.",
          "손가락을 타고 지목된 순서대로 숫자를 셉니다.",
          "마지막 숫자에 당첨된 사람이 벌칙주!"
        ]
      }},
      {{
        "title": "러브샷 룰렛 지목권",
        "desc": "소주병을 돌려 병목이 가리킨 사람이 원하는 파트너와 함께 가벼운 러브샷!",
        "ruleTitle": "러브샷 룰",
        "steps": [
          "소주병을 테이블 중앙에서 돌립니다.",
          "당첨된 사람이 원하는 사람에게 잔을 건네고 러브샷 제의!",
          "주변 사람들은 환호하며 박수 쳐주기."
        ]
      }},
      {{
        "title": "베스킨라빈스 31 (귀여운 눈치싸움)",
        "desc": "돌아가며 숫자를 1개에서 3개까지 부르고, 마지막 31을 부른 사람이 벌주!",
        "ruleTitle": "베스킨 룰",
        "steps": [
          "귀여운 율동과 함께 숫자를 순서대로 부릅니다.",
          "상대방을 보내버리기 위한 치열한 두뇌 싸움!",
          "31에 걸린 사람이 시원하게 마십니다."
        ]
      }},
      {{
        "title": "지목 토크 (이미지 게임)",
        "desc": "‘여기서 제일 츤데레 같아 보이는 사람’, ‘연애할 때 올인할 것 같은 사람’ 지목!",
        "ruleTitle": "이미지 게임 룰",
        "steps": [
          "술래가 매력적인 조건을 외치면 셋 셀 때 동시에 손가락으로 지목합니다.",
          "가장 많은 표를 받은 사람이 기분 좋게 건배사!",
          "칭찬과 호감이 오가는 훈훈한 술자리."
        ]
      }},
      {{
        "title": "동전 뒤집기 심쿵 챌린지",
        "desc": "동전을 던져 앞면이면 맞은편 사람 칭찬하기, 뒷면이면 가볍게 원샷!",
        "ruleTitle": "동전 룰",
        "steps": [
          "테이블 위에서 동전을 튕겨 결과를 확인합니다.",
          "앞면이 나오면 눈을 보고 진심 담긴 칭찬 1가지 건네기.",
          "뒷면이 나오면 호탕하게 건배!"
        ]
      }}
    ],
    "3차+": [
      {{
        "title": "오늘의 원픽 & 애프터 지목 건배",
        "desc": "오늘 모임에서 가장 즐겁게 해준 사람이나 더 알아보고 싶은 사람에게 잔 건네기.",
        "ruleTitle": "애프터 지목 룰",
        "steps": [
          "각자 오늘 가장 고마웠거나 매력적이었던 사람에게 따뜻한 한마디.",
          "자연스럽게 단톡방이나 연락처를 공유합니다.",
          "오늘의 소중한 인연을 축하하며 마지막 잔 건배!"
        ]
      }},
      {{
        "title": "진실게임 (미팅 심야 에디션)",
        "desc": "소주병을 돌려 병목이 가리킨 사람이 테이블의 질문에 솔직하게 답하기!",
        "ruleTitle": "진실게임 룰",
        "steps": [
          "소주병을 테이블 중앙에서 빙글빙글 돌립니다.",
          "병목이 멈춘 사람이 질문을 받고 솔직하게 대답합니다.",
          "도저히 말 못 하겠으면 벌칙주 마시고 비밀 지키기 가능!"
        ]
      }},
      {{
        "title": "연락처 교환 & 단톡방 결의",
        "desc": "오늘 헤어지기 아쉬운 사람들끼리 단톡방 만들고 막잔 원샷!",
        "ruleTitle": "단톡방 룰",
        "steps": [
          "테이블 대표가 단톡방을 개설하고 전원 초대합니다.",
          "방제는 오늘 있었던 가장 웃긴 키워드로 설정!",
          "다 함께 잔을 높이 들고 원샷!"
        ]
      }},
      {{
        "title": "오늘 있었던 심쿵 모먼트 고백",
        "desc": "‘오늘 몇 차 때 사실 좀 설렜다’ 솔직 담백하게 털어놓는 시간.",
        "ruleTitle": "심쿵 고백 룰",
        "steps": [
          "과장 없이 진솔하게 느꼈던 매력 포인트를 말합니다.",
          "칭찬받은 사람은 뿌듯한 미소와 함께 건배!",
          "새벽 감성 속에 훈훈하게 마무리."
        ]
      }},
      {{
        "title": "해장 메뉴 투표 & 4차 국밥파 모집",
        "desc": "집에 갈 사람과 해장 국밥 먹으러 갈 사람 솔직하게 손들기!",
        "ruleTitle": "해장 투표 룰",
        "steps": [
          "국밥 vs 라면 vs 편의점 아이스크림으로 갈립니다.",
          "안전 귀가할 사람들은 택시 태워 보내주기.",
          "남은 파티원들끼리 파이팅 건배!"
        ]
      }},
      {{
        "title": "속마음 익명 투표 (카톡 투표)",
        "desc": "‘오늘 최고의 무드메이커는?’ 단톡방 익명 투표로 1등 뽑고 축하주!",
        "ruleTitle": "익명 투표 룰",
        "steps": [
          "단톡방 투표 기능을 켜고 1분간 투표를 진행합니다.",
          "1등으로 뽑힌 사람에게 모두가 아낌없는 박수와 환호!",
          "즐거웠던 추억을 기리며 다 같이 짠!"
        ]
      }},
      {{
        "title": "헤어지기 10분 전 솔직 한마디",
        "desc": "‘오늘 나와줘서 고마워, 조심히 들어가’ 서로에게 건네는 따뜻한 배웅 인사.",
        "ruleTitle": "배웅 인사 룰",
        "steps": [
          "돌아가며 오늘 자리에 대한 솔직하고 다정한 소감을 전합니다.",
          "마지막 잔을 정성껏 채우고 부딪힙니다.",
          "다음 만남을 기약하며 기분 좋게 마무리."
        ]
      }},
      {{
        "title": "새벽 2시 인생 감성 토크",
        "desc": "요즘 가장 큰 고민이나 가치관, 새벽 감성에 어울리는 진솔한 대화 나누기.",
        "ruleTitle": "감성 토크 룰",
        "steps": [
          "조용한 BGM 속에서 서로의 이야기에 귀 기울입니다.",
          "깊어진 공감대와 함께 천천히 술잔을 비웁니다.",
          "특별한 인연에 감사하며 건배!"
        ]
      }}
    ]
  }},
  "친구 모임": {{
    "1차": [
      {{
        "title": "최근 도파민 터진 썰 방출",
        "desc": "최근 있었던 가장 어이없고 웃긴 일, 쇼핑 대참사, 꿀잼 썰 하나씩 풀기!",
        "ruleTitle": "도파민 토크 룰",
        "steps": [
          "각자 최근에 가장 도파민 터졌던 에피소드를 풉니다.",
          "듣고 제일 크게 빵 터진 사람이 승리!",
          "제일 노잼 썰을 푼 사람이 조용히 잔 비우기."
        ]
      }},
      {{
        "title": "훈민정음 게임 (영단어 금지 5분)",
        "desc": "앞으로 5분간 영단어(OK, 짠, 마셔, 텐션, 폰 등) 쓰면 걸릴 때마다 벌주!",
        "ruleTitle": "훈민정음 룰",
        "steps": [
          "외래어와 영어를 절대 쓰지 않고 순우리말로만 대화합니다.",
          "‘오케이’, ‘원샷’, ‘나이스’ 등 영어를 쓰면 즉시 지적당해 마십니다.",
          "교묘한 유도신문으로 친구를 낚는 것이 꿀잼 포인트!"
        ]
      }},
      {{
        "title": "안주 쟁탈 가위바위보",
        "desc": "테이블에서 가장 맛있는 안주 부위를 걸고 벌이는 진검승부!",
        "ruleTitle": "안주 배틀 룰",
        "steps": [
          "다 같이 안내면 진 거 가위바위보를 합니다.",
          "최후의 승자가 원하는 최고급 안주 한입 독점!",
          "패배자들은 부러워하며 술잔 부딪히기."
        ]
      }},
      {{
        "title": "손병호 게임 (찐친 매운맛)",
        "desc": "‘최근 일주일간 이성한테 까인 사람 접어’ 등 거침없는 친구 저격 손병호!",
        "ruleTitle": "손병호 룰",
        "steps": [
          "다섯 손가락을 펴고 강력한 조건을 하나씩 외칩니다.",
          "친구들의 뼈를 때리는 질문으로 폭소 유발!",
          "가장 먼저 다 접은 친구가 시원하게 원샷!"
        ]
      }},
      {{
        "title": "초성 퀴즈 배틀",
        "desc": "영화 제목, 예능, 연예인 이름 초성을 3초 안에 맞히는 뇌지컬 싸움!",
        "ruleTitle": "초성 퀴즈 룰",
        "steps": [
          "출제자가 자음 2~3글자(예: ㅂㅈㄷ)를 외칩니다.",
          "가장 늦게 정답을 외치거나 헛소리한 친구가 마십니다.",
          "정답 맞힌 친구가 다음 퀴즈 출제!"
        ]
      }},
      {{
        "title": "눈치게임 1부터 순서대로",
        "desc": "눈치 싸움의 정석! 동시에 숫자를 외치거나 마지막에 남은 사람이 패배!",
        "ruleTitle": "눈치게임 룰",
        "steps": [
          "1부터 참가자 수까지 무작위로 숫자를 외치며 일어섭니다.",
          "동시에 외치면 둘 다 벌칙주!",
          "마지막까지 눈치 보며 못 일어난 친구가 독박 원샷."
        ]
      }},
      {{
        "title": "스마트폰 뒤집기 챌린지",
        "desc": "모두 폰을 뒤집어놓고, 가장 먼저 폰 만진 사람이 술값 만원 보태기!",
        "ruleTitle": "폰 압수 룰",
        "steps": [
          "술자리 동안 폰을 테이블 중앙에 포개어 둡니다.",
          "친구와의 대화에 100% 집중!",
          "급한 연락 와서 폰 만지면 벌칙주 한 잔 마시고 확인."
        ]
      }},
      {{
        "title": "안 온 친구에게 전화 걸어 1분 버티기",
        "desc": "오늘 못 온 친구에게 스피커폰 걸어서 '너 왜 안 왔냐' 낚시 토크!",
        "ruleTitle": "전화 낚시 룰",
        "steps": [
          "다 같이 지켜보는 가운데 스피커폰 통화를 연결합니다.",
          "1분 동안 웃지 않고 진지한 척 연기 성공 시 전원 건배!",
          "웃음 터지면 통화 건 친구가 원샷."
        ]
      }},
      {{
        "title": "소주병 라벨 스크래치 배틀",
        "desc": "소주병 라벨을 찢어지지 않고 한 번에 가장 길게 떼어낸 사람이 승리!",
        "ruleTitle": "라벨 떼기 룰",
        "steps": [
          "각자 테이블 위 소주병 라벨을 조심스럽게 뗍니다.",
          "가장 깔끔하고 길게 뗀 친구에게 안주 선택권!",
          "찢어먹은 친구들은 벌칙주 건배."
        ]
      }},
      {{
        "title": "배달앱 최근 주문내역 1위 공개",
        "desc": "내 배민/요기요 최근 주문 음식 1위를 까고 야식 취향 검증하기!",
        "ruleTitle": "배달앱 공개 룰",
        "steps": [
          "각자 최근 주문 내역을 테이블에 당당히 오픈합니다.",
          "가장 의외이거나 웃긴 메뉴를 시킨 친구가 폭소 유발!",
          "공감하며 다 함께 잔을 비웁니다."
        ]
      }}
    ],
    "2차": [
      {{
        "title": "학창 시절 추억 & 이불킥 흑역사 방출",
        "desc": "찐친들 모였으니 드디어 봉인 해제! 옛날 학창 시절 그 사건 다시 꺼내기!",
        "ruleTitle": "흑역사 소환 룰",
        "steps": [
          "‘야 너 옛날에 그거 기억나냐?’로 시작하는 추억 소환.",
          "가장 치명적인 흑역사를 폭로당한 친구가 자폭 원샷!",
          "오랜 친구들만의 끈끈함으로 다 함께 짠!"
        ]
      }},
      {{
        "title": "서로의 첫인상 vs 찐친 현인상 비교",
        "desc": "처음 알았을 땐 안 친해질 줄 알았는데, 지금은 둘도 없는 찐친이 된 사연 털기!",
        "ruleTitle": "찐친 인상 토크 룰",
        "steps": [
          "처음 만났을 때 가졌던 오해나 편견을 웃으며 털어놓습니다.",
          "지금은 서로의 어떤 점이 제일 좋은지 솔직하게 칭찬!",
          "우정을 기리며 다 같이 잔을 비웁니다."
        ]
      }},
      {{
        "title": "소주 뚜껑 꼬리 날리기 & 업다운",
        "desc": "병뚜껑 꼬리를 손가락으로 튕겨서 떨어뜨린 사람이 양옆 친구에게 벌주!",
        "ruleTitle": "병뚜껑 룰",
        "steps": [
          "돌아가며 손가락으로 꼬리를 한 번씩 튕깁니다.",
          "꼬리를 떨어뜨린 사람이 승리자!",
          "병뚜껑 안쪽 숫자로 업다운 게임까지 연계 진행!"
        ]
      }},
      {{
        "title": "타이타닉 침몰 게임",
        "desc": "맥주잔 위에 빈 소주잔 띄우고, 소주를 조금씩 붓다가 가라앉힌 사람이 원샷!",
        "ruleTitle": "타이타닉 룰",
        "steps": [
          "맥주가 든 글라스에 빈 소주잔을 살포시 띄웁니다.",
          "돌아가며 소주를 원하는 만큼 방울방울 따릅니다.",
          "소주잔을 물속으로 가라앉힌 사람이 타이타닉주 원샷!"
        ]
      }},
      {{
        "title": "바니바니 당근당근 게임",
        "desc": "‘바니바니 바니바니 당근당근’ 리듬 타며 손짓 토스하는 광란의 게임!",
        "ruleTitle": "바니바니 룰",
        "steps": [
          "바니바니 모션을 취하며 다음 타자에게 지목을 넘깁니다.",
          "양옆 사람은 쉼 없이 ‘당근당근’을 외칩니다.",
          "박자 놓치거나 모션 틀린 친구가 벌칙주!"
        ]
      }},
      {{
        "title": "폰 갤러리 가장 웃긴 짤 배틀",
        "desc": "내 폰 사진첩에 있는 가장 킹받고 웃긴 짤 하나씩 보여주며 빵 터지기!",
        "ruleTitle": "짤 배틀 룰",
        "steps": [
          "각자 폰에서 가장 웃긴 사진 1장을 테이블에 공개합니다.",
          "투표를 통해 가장 덜 웃긴 사진을 낸 친구가 마십니다.",
          "다 같이 껄껄 웃으며 짠!"
        ]
      }},
      {{
        "title": "노래방 애창곡 킬링파트 떼창",
        "desc": "BGM 후렴구 나올 때 가장 열정적으로 목청껏 부른 친구에게 안주 몰아주기!",
        "ruleTitle": "떼창 배틀 룰",
        "steps": [
          "스피커에서 나오는 음악 후렴구를 다 같이 떼창합니다.",
          "가장 흥이 폭발한 사람을 전원 투표로 선정!",
          "가장 얌전하게 있던 친구가 시원하게 건배!"
        ]
      }},
      {{
        "title": "침묵의 공공칠빵 & 인디언밥",
        "desc": "소리 내면 즉시 탈락! 손가락과 눈빛으로만 007빵 진행하기!",
        "ruleTitle": "무소음 007빵 룰",
        "steps": [
          "소리를 전혀 내지 않고 손짓으로만 과녁을 지정합니다.",
          "실수로 소리 내거나 박자 틀린 사람이 시원하게 마시기.",
          "친구들의 우스꽝스러운 표정에 웃음 참기 챌린지!"
        ]
      }},
      {{
        "title": "단톡방 박제 굴욕 사진 털기",
        "desc": "우리 단톡방 사진첩 깊숙이 숨겨진 전설의 엽사 1장 소환!",
        "ruleTitle": "엽사 배틀 룰",
        "steps": [
          "가장 충격적인 과거 사진을 찾아낸 사람이 환호!",
          "사진 속 주인공 친구가 호탕하게 원샷!",
          "오랜 우정의 역사를 되새기며 짠."
        ]
      }},
      {{
        "title": "노래 1초 전주 맞히기 내기",
        "desc": "폰 음악 1초만 재생하고 제목 맞히기! 맞힌 사람이 안주 한 점 독점!",
        "ruleTitle": "전주 퀴즈 룰",
        "steps": [
          "출제자가 플레이리스트 곡을 1초만 틀었다가 끕니다.",
          "가장 먼저 손들고 가수와 제목을 외친 사람이 승리.",
          "가장 늦게 감 잡은 친구가 건배 제의!"
        ]
      }}
    ],
    "3차+": [
      {{
        "title": "새벽 감성 인생곡 떼창 & 고마움 고백",
        "desc": "평소 낯간지러워서 못 했던 고마운 마음 털어놓고 감성 명곡에 건배!",
        "ruleTitle": "감성 토크 룰",
        "steps": [
          "힘들 때 곁에 있어줘서 고마웠던 순간을 담백하게 말합니다.",
          "새벽 감성에 젖어 다 같이 어깨동무하고 건배!",
          "다음 정모/여행 날짜 잡으며 훈훈하게 마무리."
        ]
      }},
      {{
        "title": "막차 포기 선언 & 첫차 건배사",
        "desc": "‘오늘 끝까지 달린다!’ 막차 시간 넘기고 찐하게 첫차까지 버티기 결의!",
        "ruleTitle": "첫차 룰",
        "steps": [
          "남은 친구들끼리 잔을 가득 채웁니다.",
          "멋진 건배사 하나 외치고 다 함께 원샷!",
          "살아남은 자들의 전우애 다지기."
        ]
      }},
      {{
        "title": "다음 우정 여행지 투표",
        "desc": "‘올해 안에 무조건 넷이서 여행 간다’ 제주도 vs 해외 vs 글램핑 투표!",
        "ruleTitle": "여행 계획 룰",
        "steps": [
          "원하는 여행지를 하나씩 제안합니다.",
          "총무 맡을 사람 가위바위보로 선정!",
          "기분 좋은 약속과 함께 다 같이 짠!"
        ]
      }},
      {{
        "title": "해장 메뉴 쏘기 가위바위보",
        "desc": "내일 아침 순대국밥/뼈해장국 값 쏘기 걸고 벌이는 단판 승부!",
        "ruleTitle": "국밥 내기 룰",
        "steps": [
          "단판 가위바위보로 패자를 정합니다.",
          "패배자는 내일 아침 든든한 국밥 결제 확정!",
          "승자들은 환호하며 마지막 잔을 비웁니다."
        ]
      }},
      {{
        "title": "10년 뒤 우리 모습 예언하기",
        "desc": "10년 뒤에 누가 제일 먼저 결혼하고 누가 건물주 될지 솔직한 뇌피셜!",
        "ruleTitle": "미래 예언 룰",
        "steps": [
          "각자 친구들의 10년 뒤 미래 모습을 진지하고 웃기게 묘사합니다.",
          "가장 설득력 있는 예언을 들은 친구가 기분 좋게 짠!",
          "우정 변치 말자고 맹세하기."
        ]
      }},
      {{
        "title": "편의점 아이스크림 쏘기 배틀",
        "desc": "새벽 술자리 필수 코스! 편의점 털러 갈 사람 가위바위보로 선정!",
        "ruleTitle": "아이스크림 룰",
        "steps": [
          "단판 승부로 진 사람이 편의점 결제!",
          "시원한 아이스크림으로 숙취 날려버리기.",
          "달콤한 휴식과 함께 잔 비우기."
        ]
      }},
      {{
        "title": "우정 서약 건배사",
        "desc": "잔 가득 채우고 서로 손목 걸고 끝까지 의리 지키기 건배!",
        "ruleTitle": "의리 서약 룰",
        "steps": [
          "친구들끼리 잔을 한가운데로 모읍니다.",
          "평생 갈 찐친임을 다짐하며 힘차게 구호 외치기.",
          "다 같이 막잔 원샷!"
        ]
      }},
      {{
        "title": "마지막 생존자 단체 셀카",
        "desc": "오늘 모임의 대미를 장식하는 흔들린 찐친 단체 사진 남기기!",
        "ruleTitle": "생존 셀카 룰",
        "steps": [
          "가장 멀쩡한 사람이 폰을 들고 단체 사진을 찍습니다.",
          "단톡방 공지에 올리고 오늘 하루 완벽 마무리!",
          "서로 조심히 들어가라고 인사하며 해산."
        ]
      }}
    ]
  }},
  "과/동아리 회식": {{
    "1차": [
      {{
        "title": "학번 & 나이 리셋! 3분 야자타임",
        "desc": "딱 3분간 선후배 계급장 떼기! 편하게 반말하며 그동안 못 했던 질문 던지기!",
        "ruleTitle": "야자타임 룰",
        "steps": [
          "타이머 시작과 동시에 모든 존댓말이 전면 금지됩니다.",
          "선배에게 '밥 사줘', '요즘 어때?' 편하게 말 걸기.",
          "존댓말 실수하거나 쫄아서 말 못 한 사람이 벌칙주!"
        ]
      }},
      {{
        "title": "교수님 / 동아리 밈 퀴즈 배틀",
        "desc": "우리 과, 우리 동아리 사람이라면 무조건 아는 전설의 일화 맞히기!",
        "ruleTitle": "과 퀴즈 룰",
        "steps": [
          "과/동아리 내 유명한 사건이나 교수님 명언 퀴즈를 냅니다.",
          "가장 먼저 정답을 외친 사람에게 환호와 안주 배분!",
          "동질감 100% 충전하며 다 같이 잔 채우기."
        ]
      }},
      {{
        "title": "출석부 게임 & 신입생 환영 짠",
        "desc": "테이블 돌아가며 이름과 별명을 리듬에 맞춰 외치며 얼굴 익히기!",
        "ruleTitle": "출석부 룰",
        "steps": [
          "박자에 맞춰 특정 사람의 이름을 부르고 숫자를 외칩니다.",
          "박자 놓치거나 이름 버벅거린 사람이 벌칙주!",
          "모두의 이름을 다 외우는 순간 다 같이 원샷!"
        ]
      }},
      {{
        "title": "전공 공감 밸런스 토크",
        "desc": "‘팀플 무임승차 조원 vs 아침 9시 전공 필수 강의’ 무엇이 더 고통스러운가?",
        "ruleTitle": "대학 밸런스 룰",
        "steps": [
          "손가락으로 더 끔찍한 쪽을 동시에 가리킵니다.",
          "격한 공감 토크와 함께 대학 생활 스트레스 날리기!",
          "동기들과 위로의 짠!"
        ]
      }},
      {{
        "title": "선배 찬스 안주 추가 주문권",
        "desc": "선배들에게 특급 애교나 멋진 칭찬을 건네고 먹고 싶은 사이드 안주 얻어내기!",
        "ruleTitle": "선배 찬스 룰",
        "steps": [
          "가장 센스 있는 멘트를 날린 후배가 안주 메뉴 선택!",
          "선배는 쿨하게 주문 벨 누르고 결제!",
          "후배들은 선배님을 찬양하며 감사의 건배!"
        ]
      }},
      {{
        "title": "딸기 게임 (아이 엠 그라운드)",
        "desc": "박자에 맞춰 딸기를 1개부터 8개까지 늘려가며 외치는 순발력 게임!",
        "ruleTitle": "딸기 룰",
        "steps": [
          "무릎 치고 손뼉 치고 오른손 왼손 흔들며 박자를 탑니다.",
          "해당 숫자에 맞게 딸기 비트를 외칩니다.",
          "박자 절거나 숫자 틀린 사람이 벌주!"
        ]
      }},
      {{
        "title": "수강신청 광탈 & 학점 흑역사 배틀",
        "desc": "수강신청 서버 터져서 망했던 썰, 재수강 과목 자랑하며 폭소하기!",
        "ruleTitle": "학점 배틀 룰",
        "steps": [
          "가장 처참한 수강신청 실패 썰을 푼 사람이 승리.",
          "다 같이 위로하며 다 함께 건배!",
          "학점 걱정은 오늘 밤만큼은 잊어버리기."
        ]
      }},
      {{
        "title": "시간표 꿀강 & 헬강 공유 토크",
        "desc": "다음 학기 절대 놓치면 안 되는 꿀교양과 절대 피해야 할 헬교양 공유!",
        "ruleTitle": "꿀강 공유 룰",
        "steps": [
          "선배들이 후배들에게 특급 강의 꿀팁을 전수합니다.",
          "유익한 정보에 감동하며 후배들이 선배에게 잔 올리기!",
          "화기애애하게 짠!"
        ]
      }},
      {{
        "title": "동아리 TMI 퀴즈 배틀",
        "desc": "동아리방 비밀번호, 회비 잔액, 역대 회장 이름 등 소소한 상식 퀴즈!",
        "ruleTitle": "동아리 퀴즈 룰",
        "steps": [
          "가장 먼저 정답을 외친 사람에게 박수와 안주 증정.",
          "틀린 사람은 가볍게 한 모금 축이며 동아리 애착 다지기.",
          "다 함께 동아리 구호 외치며 건배!"
        ]
      }},
      {{
        "title": "새내기 환영 사랑의 러브샷",
        "desc": "새로 들어온 신입 동아리원과 짝선배의 훈훈한 맞잔 교환!",
        "ruleTitle": "신입 환영 룰",
        "steps": [
          "선배와 후배가 짝을 이뤄 가볍게 잔을 부딪힙니다.",
          "따뜻한 격려 한마디와 함께 시원하게 마시기.",
          "동아리 구성원 전원이 힘찬 박수로 환영!"
        ]
      }}
    ],
    "2차": [
      {{
        "title": "선배 지갑 털기 가위바위보",
        "desc": "다음 차수 안주나 노래방 비용 걸고 선배들과 후배들의 한판 승부!",
        "ruleTitle": "지갑 배틀 룰",
        "steps": [
          "선배 대표 vs 후배 대표 단판 가위바위보!",
          "후배가 이기면 선배가 쿨하게 다음 차수 결제 공약!",
          "존경과 사랑을 담아 선배님께 힘찬 건배사!"
        ]
      }},
      {{
        "title": "동아리 장기자랑 & 10초 개인기 배틀",
        "desc": "가장 뻔뻔하고 당당하게 개인기나 랩 한 소절 뽑은 사람에게 박수!",
        "ruleTitle": "개인기 룰",
        "steps": [
          "부담 갖지 말고 웃긴 성대모사나 댄스 10초 시전.",
          "가장 큰 웃음을 준 사람을 전원 투표로 선정!",
          "동아리 텐션을 우주 끝까지 끌어올립니다."
        ]
      }},
      {{
        "title": "침묵의 007빵 게임",
        "desc": "소리를 내지 않고 오직 손짓과 입모양으로만 진행하는 스릴만점 게임!",
        "ruleTitle": "007빵 룰",
        "steps": [
          "공공칠빵을 무소음으로 진행합니다.",
          "으악 소리를 내거나 손을 잘못 든 사람이 마십니다.",
          "조용한 긴장감 속에 터지는 웃음 폭탄!"
        ]
      }},
      {{
        "title": "동아리 임원진 사랑의 건배사",
        "desc": "한 학기 동안 고생한 회장, 부회장, 총무에게 따뜻한 감사와 응원의 멘트!",
        "ruleTitle": "임원진 감사 룰",
        "steps": [
          "후배들이 임원진에게 릴레이 칭찬을 건넵니다.",
          "감동한 임원진이 대표 건배사를 외칩니다.",
          "동아리 일체감을 느끼며 다 함께 원샷!"
        ]
      }},
      {{
        "title": "테이블 대항 가위바위보 릴레이",
        "desc": "옆 테이블과 술잔 걸고 벌이는 1대1 릴레이 가위바위보 대항전!",
        "ruleTitle": "테이블 대항 룰",
        "steps": [
          "각 테이블 대표가 나와 연달아 가위바위보를 합니다.",
          "패배한 테이블 전원이 유쾌하게 단체 건배!",
          "회식 전체 분위기를 하나로 묶습니다."
        ]
      }},
      {{
        "title": "홍삼 게임 (아싸 너 너 너!)",
        "desc": "두 명씩 지목을 주고받다가 같은 사람을 지목하면 아싸 홍삼 에브리바디 홍삼!",
        "ruleTitle": "홍삼 게임 룰",
        "steps": [
          "양손으로 두 사람을 각각 지목합니다.",
          "서로가 서로를 지목하면 다 같이 춤추며 구호 외치기!",
          "박자 놓치거나 동작 멈칫한 사람이 벌칙주."
        ]
      }},
      {{
        "title": "선배님 이름 삼행시 짓기 배틀",
        "desc": "오늘 술 사주는 선배 이름으로 감동 또는 폭소 삼행시 도전!",
        "ruleTitle": "삼행시 룰",
        "steps": [
          "가장 센스 있는 삼행시를 지은 후배에게 안주 몰아주기.",
          "감동한 선배님이 흐뭇하게 술잔을 듭니다.",
          "모두 함께 환호하며 원샷!"
        ]
      }},
      {{
        "title": "주량 허세 폭로전",
        "desc": "‘나 원래 소주 3병 마신다’ 해놓고 1병에 뻗었던 과거 사건 폭로!",
        "ruleTitle": "주량 폭로 룰",
        "steps": [
          "테이블에서 가장 주량 허세 심했던 멤버를 지목합니다.",
          "지목된 멤버가 억울함을 호소하며 벌칙주 마시기!",
          "다 같이 껄껄 웃으며 짠."
        ]
      }},
      {{
        "title": "더 게임 오브 데스 (선후배 저격)",
        "desc": "손가락으로 타깃을 찍고 부른 숫자만큼 순서대로 넘어가는 진검승부!",
        "ruleTitle": "데스 게임 룰",
        "steps": [
          "신나는 인트로 구호와 함께 숫자를 외칩니다.",
          "손가락을 타고 지목이 이동합니다.",
          "마지막 숫자에 걸린 사람이 시원하게 한 잔!"
        ]
      }},
      {{
        "title": "과/동아리 떼창 응원가 열창",
        "desc": "축제 때 부르던 동아리 대표곡이나 과 응원가를 목청껏 떼창하기!",
        "ruleTitle": "응원가 룰",
        "steps": [
          "BGM에 맞춰 다 같이 어깨동무하고 후렴구를 부릅니다.",
          "가장 목청 큰 사람에게 박수 갈채!",
          "하나 된 마음으로 다 같이 잔을 비웁니다."
        ]
      }}
    ],
    "3차+": [
      {{
        "title": "동아리 번창 기원 어깨동무 떼창 건배",
        "desc": "남은 사람들끼리 끈끈하게 어깨동무하고 축제 엔딩곡 부르며 잔 비우기!",
        "ruleTitle": "떼창 건배 룰",
        "steps": [
          "흘러나오는 BGM에 맞춰 다 같이 목청껏 떼창!",
          "다음 학기에도 다 같이 함께하자는 굳은 약속.",
          "잔을 높이 치켜들고 원샷!"
        ]
      }},
      {{
        "title": "비밀 롤링페이퍼 / 한 줄 응원 토크",
        "desc": "오늘 자리 함께해 준 동료들에게 따뜻한 한마디씩 남겨주기.",
        "ruleTitle": "응원 토크 룰",
        "steps": [
          "옆사람에게 진심 어린 응원과 격려를 해줍니다.",
          "끈끈해진 마음으로 술잔을 채웁니다.",
          "동아리 뽕 차오르는 감동의 순간!"
        ]
      }},
      {{
        "title": "동방(동아리방) 뒤풀이 파티원 결의",
        "desc": "술집 끝나고 동아리방 가서 컵라면 먹을 정예 멤버 모집!",
        "ruleTitle": "동방 룰",
        "steps": [
          "남은 파티원들끼리 출석 체크!",
          "편의점 들러서 아이스크림과 라면 챙기기.",
          "마지막 잔을 시원하게 비우고 이동!"
        ]
      }},
      {{
        "title": "차기 회장/임원 강제 지목 가위바위보",
        "desc": "다음 학기 동아리를 이끌 차기 회장 후보를 유쾌하게 지목하기!",
        "ruleTitle": "차기 회장 룰",
        "steps": [
          "가장 리더십 넘치는 사람에게 전원 손가락 지목!",
          "지목된 후보가 당선(?) 소감과 함께 건배사 제의.",
          "모두 환호하며 응원의 원샷!"
        ]
      }},
      {{
        "title": "동방 청소 당번 내기",
        "desc": "내일 낮에 동아리방 분리수거 및 청소하러 올 사람 정하는 가위바위보!",
        "ruleTitle": "청소 내기 룰",
        "steps": [
          "단판 가위바위보로 패자를 선발합니다.",
          "당첨자는 내일 동방 청소 확정!",
          "승자들은 고마운 마음을 담아 건배."
        ]
      }},
      {{
        "title": "선배님의 진솔한 진로 & 인생 조언",
        "desc": "새벽 감성에 터놓는 취업, 학점, 미래에 대한 선배들의 따뜻한 꿀팁.",
        "ruleTitle": "진로 조언 룰",
        "steps": [
          "선배들의 현실적인 경험담을 조용히 경청합니다.",
          "후배들의 든든한 앞날을 응원하며 술잔을 부딪힙니다.",
          "서로에게 큰 힘이 되는 따뜻한 시간."
        ]
      }},
      {{
        "title": "과잠 입고 첫차 귀가 서약",
        "desc": "살아남은 정예 멤버들끼리 첫차 올 때까지 의리 지키기 결의!",
        "ruleTitle": "첫차 서약 룰",
        "steps": [
          "모두 잔을 높이 들고 마지막 건배 구호를 외칩니다.",
          "다 같이 막잔을 털어 넣고 완벽한 피날레.",
          "안전 귀가를 약속하며 해산!"
        ]
      }},
      {{
        "title": "학술제/축제 무대 회고 토크",
        "desc": "지난 축제나 공연 준비하면서 가장 힘들었지만 뿌듯했던 순간 회상!",
        "ruleTitle": "축제 회고 룰",
        "steps": [
          "함께 땀 흘렸던 추억을 돌아보며 감동 나누기.",
          "수고했던 서로의 등을 두드려주며 짠!",
          "잊지 못할 청춘의 한 페이지 완성."
        ]
      }}
    ]
  }},
  "회사 회식": {{
    "1차": [
      {{
        "title": "칼퇴 축하 & 동료 칭찬 릴레이",
        "desc": "오늘 야근 안 하고 무사히 퇴근한 기념! 오늘 일하면서 고마웠던 팀원에게 한마디.",
        "ruleTitle": "칭찬 릴레이 룰",
        "steps": [
          "오른쪽 팀원이 이번 주에 잘했던 일이나 고마웠던 점을 칭찬합니다.",
          "칭찬받은 사람이 감사의 뜻으로 건배사를 제의합니다.",
          "업무 스트레스를 털어내며 시원하게 첫 잔 짠!"
        ]
      }},
      {{
        "title": "직장인 공감 밸런스 토크",
        "desc": "‘월요일 아침 9시 전체 회의 vs 금요일 저녁 6시 전체 회식’ 각자 선택!",
        "ruleTitle": "직장 밸런스 룰",
        "steps": [
          "하나, 둘, 셋에 손가락으로 둘 중 하나를 지목합니다.",
          "모두가 폭풍 공감하며 직장 생활 애환 나누기!",
          "서로 고생 많았다는 의미로 다 함께 건배."
        ]
      }},
      {{
        "title": "로또 1등 되면 내일 사직서 양식 고백",
        "desc": "이번 주 로또 50억 당첨되면 당장 내일 출근할 것인지 솔직하게 털기!",
        "ruleTitle": "로또 공약 룰",
        "steps": [
          "‘조용히 다닌다’ vs ‘팀원 전원에게 1억씩 쏘고 칼퇴한다’ 공약 발표.",
          "가장 파격적인 공약을 한 사람에게 건배사 권한 부여!",
          "행복한 상상과 함께 다 같이 잔을 비웁니다."
        ]
      }},
      {{
        "title": "부장님/팀장님 3초 센스 건배사",
        "desc": "지루한 훈화 말씀 대신 3초 안에 끝나는 초스피드 센스 건배사 릴레이!",
        "ruleTitle": "센스 건배사 룰",
        "steps": [
          "세 글자나 네 글자로 짧고 강렬한 건배사를 외칩니다.",
          "모두가 힘차게 후창하며 원샷!",
          "가장 반응 좋았던 사람에게 박수 갈채."
        ]
      }},
      {{
        "title": "점심 메뉴 선택권 쟁탈 가위바위보",
        "desc": "내일 점심 회식 메뉴를 내 마음대로 고를 수 있는 절대 권한 배틀!",
        "ruleTitle": "점메추 배틀 룰",
        "steps": [
          "팀원 전원이 단판 가위바위보를 진행합니다.",
          "최종 우승자가 내일 점심 메뉴 확정!",
          "모두 승자의 취향을 존중하며 짠!"
        ]
      }},
      {{
        "title": "팀 분기 목표 달성 기원 건배",
        "desc": "이번 분기 인센티브와 프로젝트 대박을 기원하며 힘찬 결의 다지기!",
        "ruleTitle": "인센티브 기원 룰",
        "steps": [
          "팀의 대박과 성과급을 위해 잔을 높이 듭니다.",
          "화이팅을 외치며 첫 잔을 비웁니다.",
          "맛있는 안주와 함께 본격적인 회식 시작."
        ]
      }},
      {{
        "title": "월요병 극복 나만의 힐링법 공유",
        "desc": "주말 지나고 월요일 출근할 때 멘탈 잡는 나만의 소소한 비법 공유!",
        "ruleTitle": "월요병 극복 룰",
        "steps": [
          "각자 좋아하는 영양제, 모닝커피, 운동 등 꿀팁을 전수합니다.",
          "서로의 꿀팁에 고개를 끄덕이며 술잔을 채웁니다.",
          "건강한 직장 생활을 기원하며 건배!"
        ]
      }},
      {{
        "title": "사내 메신저 이모티콘 퀴즈",
        "desc": "우리 팀에서 가장 자주 쓰이는 메신저 짤이나 이모티콘 흉내 내기!",
        "ruleTitle": "이모티콘 룰",
        "steps": [
          "몸짓이나 표정으로 특정 이모티콘을 표현합니다.",
          "가장 먼저 맞힌 사람에게 맛있는 안주 양보!",
          "동료들과 웃음을 나누며 기분 좋게 짠!"
        ]
      }},
      {{
        "title": "슬기로운 연차 사용 계획 자랑",
        "desc": "다가오는 연휴에 연차 붙여서 어디 갈지 설레는 계획 30초 공유!",
        "ruleTitle": "연차 자랑 룰",
        "steps": [
          "휴가 일정과 가고 싶은 여행지를 신나게 이야기합니다.",
          "동료들은 서로 업무 백업을 약속하며 축하!",
          "워라밸 만세를 외치며 시원하게 건배."
        ]
      }},
      {{
        "title": "익명 칭찬 롤링페이퍼 (스마트폰 메모)",
        "desc": "폰을 옆사람에게 돌려가며 각자 고마웠던 점 한 줄씩 적어주기!",
        "ruleTitle": "롤링페이퍼 룰",
        "steps": [
          "스마트폰 메모장에 칭찬을 한 줄씩 작성하고 넘깁니다.",
          "본인 폰을 돌려받고 감동의 미소 짓기!",
          "따뜻해진 분위기 속에서 다 함께 원샷!"
        ]
      }}
    ],
    "2차": [
      {{
        "title": "법카 찬스 프리미엄 안주 털기",
        "desc": "회식의 꽃 법인카드! 평소 내 돈 주고 못 먹던 최고급 메뉴 주문하고 짠!",
        "ruleTitle": "법카 찬스 룰",
        "steps": [
          "테이블에서 가장 먹고 싶었던 특선 메뉴를 결의합니다.",
          "회사 매출 대박과 팀의 번창을 기원하며 건배!",
          "맛있는 안주와 함께 한결 편안해진 토크 타임."
        ]
      }},
      {{
        "title": "노래방 치트키 애창곡 추천 배틀",
        "desc": "내가 회식 2차 노래방에서 부르면 무조건 분위기 뒤집어놓는 곡 자랑하기!",
        "ruleTitle": "치트키 송 룰",
        "steps": [
          "각자 회식 자리 텐션을 찢어놓는 비장의 노래 1곡 소개.",
          "BGM으로 틀고 다 같이 후렴구 흥얼거리며 리듬 타기!",
          "팀 내 최고 보컬리스트에게 박수갈채와 함께 짠!"
        ]
      }},
      {{
        "title": "세대 화합 퀴즈 배틀 (신조어 vs 레트로)",
        "desc": "MZ 신조어 맞히기 vs 부장님 시절 레트로 퀴즈로 세대 차이 좁히기!",
        "ruleTitle": "세대 공감 룰",
        "steps": [
          "서로 세대별 유행어 퀴즈를 하나씩 냅니다.",
          "틀릴 때마다 서로 알려주며 빵 터지기!",
          "세대 격차 허물며 기분 좋게 건배."
        ]
      }},
      {{
        "title": "내 인생 최고의 휴가지 공유",
        "desc": "이번 여름휴가나 연차 때 꼭 가봐야 할 인생 여행지 서로 추천하기.",
        "ruleTitle": "휴가 꿀팁 룰",
        "steps": [
          "가장 힐링 되었던 여행지와 맛집을 공유합니다.",
          "서로 휴가 일정 겹치지 않게 조율하며(?) 폭소!",
          "워라밸을 응원하며 다 함께 짠!"
        ]
      }},
      {{
        "title": "영단어 금지 비즈니스 모드 (3분)",
        "desc": "‘컨펌’, ‘어레인지’, ‘미팅’, ‘이슈’ 등 회사 영어 쓰면 걸릴 때마다 벌주!",
        "ruleTitle": "비즈니스 금지 룰",
        "steps": [
          "3분 동안 회사 업무 이야기를 순우리말로만 합니다.",
          "무의식중에 회사 영어를 내뱉은 동료 적발!",
          "스트레스 풀며 시원하게 한 모금."
        ]
      }},
      {{
        "title": "팀장님의 20대 시절 애창곡 감상",
        "desc": "선배 동료의 청춘 시절을 가슴 뛰게 했던 전설의 명곡 BGM으로 소환!",
        "ruleTitle": "청춘 소환 룰",
        "steps": [
          "선배 동료의 최애곡을 추천받아 함께 듣습니다.",
          "그 시절 추억 이야기를 들으며 세대 공감대 형성!",
          "존경의 의미를 담아 다 함께 잔을 올립니다."
        ]
      }},
      {{
        "title": "센스 만점 4글자 건배사 배틀",
        "desc": "‘청바지’, ‘사이다’, ‘오징어’ 등 위트 넘치는 줄임말 건배사 릴레이!",
        "ruleTitle": "건배사 배틀 룰",
        "steps": [
          "돌아가며 기발한 4글자 건배사를 제의합니다.",
          "팀원들이 우렁찬 목소리로 구호를 따라 외칩니다.",
          "가장 빵 터진 사람에게 박수와 환호!"
        ]
      }},
      {{
        "title": "퇴근 후 딴짓! 취미 생활 자랑",
        "desc": "골프, 캠핑, 베이킹, 헬스 등 회사 밖 진짜 내 모습 공유하기!",
        "ruleTitle": "취미 공유 룰",
        "steps": [
          "각자 요즘 푹 빠져 있는 취미나 관심사를 털어놓습니다.",
          "동료의 새로운 매력을 발견하며 눈빛 교환!",
          "즐거운 취미 생활을 응원하며 건배."
        ]
      }},
      {{
        "title": "다음 회식 메뉴 결정 가위바위보",
        "desc": "다음 분기 회식 메뉴 소고기 vs 삼겹살 vs 해산물 결정권 쟁탈전!",
        "ruleTitle": "회식 메뉴 룰",
        "steps": [
          "전원 단판 가위바위보를 통해 우승자를 가립니다.",
          "우승자가 다음 회식 희망 메뉴를 당당히 선포!",
          "팀장님/부장님의 쿨한 승낙과 함께 원샷!"
        ]
      }},
      {{
        "title": "팀장님 찬스 편의점 하겐다즈 내기",
        "desc": "회식 2차 후 디저트 아이스크림 쏘기 걸고 벌이는 미니게임!",
        "ruleTitle": "디저트 내기 룰",
        "steps": [
          "팀장님과 팀원들의 스릴 넘치는 가위바위보 한판.",
          "달콤한 디저트 획득을 기대하며 환호!",
          "유쾌한 웃음과 함께 잔을 비웁니다."
        ]
      }}
    ],
    "3차+": [
      {{
        "title": "내일 숙취 제로 & 안전 귀가 택시비 빵",
        "desc": "내일 업무에 지장 없도록 물 많이 마시기 & 무사 귀가 약속 건배!",
        "ruleTitle": "안전 귀가 룰",
        "steps": [
          "끝까지 살아남은 팀원들끼리 가위바위보로 택시비 보태주기!",
          "내일 오전 커피 내기 약속 걸기.",
          "서로 수고했다고 악수하며 깔끔하게 마무리 건배!"
        ]
      }},
      {{
        "title": "내일 아침 아이스 아메리카노 쏘기 내기",
        "desc": "출근길 팀원 전원에게 모닝커피 쏠 사람 단판 가위바위보!",
        "ruleTitle": "커피 내기 룰",
        "steps": [
          "남은 사람들끼리 가위바위보를 진행합니다.",
          "내일 아침 모닝커피 당번 선정!",
          "산뜻한 내일을 기약하며 막잔 원샷."
        ]
      }},
      {{
        "title": "팀워크 다지기 훈훈한 악수 건배",
        "desc": "오늘 회식을 계기로 한층 더 돈독해진 팀원들과 맞잡은 두 손!",
        "ruleTitle": "팀워크 건배 룰",
        "steps": [
          "양옆 동료와 따뜻하게 악수를 나눕니다.",
          "다음 프로젝트 대박을 다짐하며 건배!",
          "안전 귀가를 약속하며 해산."
        ]
      }},
      {{
        "title": "비밀 보장! 오늘 회식 감동 모먼트",
        "desc": "오늘 자리에서 오해를 풀었거나 진심으로 고마웠던 순간 솔직 고백!",
        "ruleTitle": "감동 고백 룰",
        "steps": [
          "서로에게 전하는 진솔한 격려와 감사의 한마디.",
          "끈끈해진 동료애를 느끼며 잔을 천천히 비웁니다.",
          "서로를 존중하는 마음으로 훈훈하게 마무리."
        ]
      }},
      {{
        "title": "막차 팀원 카카오택시 배웅하기",
        "desc": "막차 끊긴 팀원들 안전하게 택시 태워 보내주고 무사 귀가 확인!",
        "ruleTitle": "택시 배웅 룰",
        "steps": [
          "서로 택시 번호를 챙겨주고 출발을 배웅합니다.",
          "단톡방에 '무사 귀가 완료' 톡 남기기 약속!",
          "끝까지 서로를 챙기는 따뜻한 회식 문화 완성."
        ]
      }},
      {{
        "title": "내일 정시 출근 서약 막잔",
        "desc": "내일 지각 없이 당당하게 9시 출근할 것을 전원 서약하며 원샷!",
        "ruleTitle": "정시 출근 룰",
        "steps": [
          "남은 팀원 전원이 잔을 가득 채우고 일어섭니다.",
          "프로페셔널한 직장인의 자존심을 걸고 막잔 비우기!",
          "내일 회사에서 밝은 얼굴로 만나요!"
        ]
      }},
      {{
        "title": "올해 프로젝트 성공 기원 어깨동무",
        "desc": "우리 팀 올해 역대 최고 실적 달성을 기원하며 전우애 충전!",
        "ruleTitle": "실적 대박 룰",
        "steps": [
          "동료들과 어깨를 나란히 하고 파이팅을 외칩니다.",
          "서로가 있어서 든든하다는 덕담 나누기.",
          "힘차게 잔을 부딪히며 피날레!"
        ]
      }},
      {{
        "title": "마지막 남은 안주 싹쓸이 가위바위보",
        "desc": "마지막 남은 최고의 안주 한 입을 걸고 벌이는 직급 파괴 승부!",
        "ruleTitle": "안주 싹쓸이 룰",
        "steps": [
          "계급장 떼고 단판 가위바위보 승부!",
          "승자가 맛있게 안주를 비우고 박수갈채.",
          "기분 좋게 자리 정리하고 귀가."
        ]
      }}
    ]
  }}
}};

    // Situation-Aware AI DJ Host Banters by (groupType -> round)
    const CONTEXT_BANTERS = {{
  "미팅/과팅": {{
    "1차": [
      "“처음 봬서 살짝 낯가리시죠? 어색한 정적 제가 비트로 싹 날려드릴게요. 잔 들고 아이스브레이킹 갑니다!”",
      "“눈치 보지 마세요! 미팅은 원래 30분 지나면 다 친해지는 법입니다. 취향 밸런스 토크 바로 갑니다!”",
      "“맞은편 사람 얼굴 힐끔힐끔 보지 말고, 당당하게 눈 마주치며 시원하게 짠 합시다!”",
      "“어색할 땐 건배가 보약입니다. 다 같이 잔 들고 아이스브레이킹 비트 들어갑니다!”",
      "“첫 잔 비우고 나면 말문 트입니다! 편하게 취향 나누면서 텐션 올려보시죠!”",
      "“독서실 분위기 금지! 가벼운 게임 하나 던져드릴 테니 긴장 풀고 즐기세요!”",
      "“오늘의 인연은 지금 이 순간부터 시작됩니다. 잔 부딪히고 출발합니다!”"
    ],
    "2차": [
      "“오호, 1차 때 어색했던 분들 맞나요? 분위기 핑크빛으로 달아올랐네요. 설렘 텐션 더 올립니다!”",
      "“눈빛 교환 슬슬 시작됐죠? 이 타이밍 놓치면 후회합니다. 마음에 드는 사람한테 잔 건네세요!”",
      "“비트 빨라진 거 느껴지시죠? 지금부터 폰 보는 사람은 흑기사 없습니다, 원샷!”",
      "“2차 오니까 케미가 제대로 사네요! 다음 게임으로 서로 더 깊숙이 알아가 봅시다!”",
      "“자리도 섞였겠다, 이제 진짜 솔직해질 시간입니다! 다음 미션 주목하세요!”",
      "“심장 박동수랑 BPM 맞춰드릴 테니, 망설이지 말고 직진하세요!”",
      "“둘만의 귓속말 오가는 거 다 지켜보고 있습니다! 핑크빛 텐션 폭발!”"
    ],
    "3차+": [
      "“오늘 미팅의 전설이 탄생하는 순간입니다! 이 분위기 그대로 애프터까지 직진합시다!”",
      "“새벽 감성 터졌네요. 오늘 놓치면 영영 후회할 사람 누구죠? 잔 채우고 고백 각 갑니다!”",
      "“헤어지기 아쉬운 사람 손! 단톡방 파고 마지막 건배 시원하게 갑니다!”",
      "“오늘 밤 잊지 못할 추억 하나 만들고 갑니다. 다 같이 막잔 원샷!”",
      "“해장 국밥 멤버 결성 완료! 끝까지 함께한 여러분이 오늘 미팅의 챔피언입니다!”",
      "“새벽 2시, 진짜 마음이 통하는 시간입니다. 마지막 잔 채우고 축배를 듭시다!”",
      "“내일 아침 카톡 선톡 먼저 보내는 사람이 위너입니다. 아름다운 밤 되세요!”"
    ]
  }},
  "친구 모임": {{
    "1차": [
      "“친구들 모였으면 가식 떨 거 없죠? 오늘 누구 하나 기어 나갈 때까지 비트 빡세게 갑니다!”",
      "“누가 폰 보냐? 폰 집어넣고 술잔 채워라! 영혼 없는 리액션은 벌주다!”",
      "“적당히 비트 타면서 서로 도파민 썰 끝내봅시다. 판 다시 깝니다!”",
      "“친구끼리 빼는 거 없다! 시원하게 잔 채우고 워밍업 시작합니다!”",
      "“오랜만에 모였으니 목 쉴 때까지 떠들어봅시다! 첫 미션 갑니다!”",
      "“안주 눈독 들이지 말고 가위바위보 준비해라! 진검승부 시작!”",
      "“어차피 내일 후회할 거 오늘 신나게 달립시다! 첫 잔 짠!”"
    ],
    "2차": [
      "“학창 시절 흑역사 드디어 봉인 해제할 시간입니다! 이불킥 썰 풀면서 원샷 갑니다!”",
      "“분위기 제대로 달아올랐네요. 이 타이밍에 빼는 친구는 절교입니다, 마셔!”",
      "“심장 박동수랑 BPM 맞춰드릴게요. 잔 채우고 바로 돌진합니다!”",
      "“이 그루브 나오면 절로 고개 흔들리죠? 옛날 추억 썰 풀면서 건배!”",
      "“타이타닉 침몰할 준비하시고, 술잔 꽉 잡으세요!”",
      "“바니바니 비트 들어갑니다! 틀린 놈이 오늘 2차 쏘는 거다!”",
      "“친구야 사랑한다 외치면서 시원하게 잔 비웁시다!”"
    ],
    "3차+": [
      "“새벽 감성 젖어드네요. 평소 낯간지러워서 못 했던 고마운 마음 잔에 담아 짠!”",
      "“첫차 뜰 때까지 브레이크 없습니다. 인생 명곡 틀어드릴 테니 끝까지 갑니다!”",
      "“이 멤버 리멤버! 오늘 밤 우리 우정 영원하길 바라며 원샷!”",
      "“해장 국밥 먹으러 갈 최후의 용사들만 잔을 듭니다!”",
      "“10년 뒤에도 우리 이렇게 모여서 술 마시자. 멋진 친구들아 건배!”",
      "“편의점 아이스크림 쏘기 가위바위보 장전하시고! 막판 스퍼트!”",
      "“마지막 생존자 단체 사진 박고 명예롭게 퇴근합시다!”"
    ]
  }},
  "과/동아리 회식": {{
    "1차": [
      "“선배 후배 눈치 보지 말고 동아리방처럼 편하게 갑시다! 잔 비어 있는 사람 채우세요!”",
      "“신입생 환영합니다! 오늘 어색함 싹 털어버릴 수 있게 신나는 비트 깔아드릴게요!”",
      "“학번 계급장 떼고 다 같이 잔 부딪힙니다! 야자타임 들어갈 준비하세요!”",
      "“동아리 출석 체크 완료! 오늘 밤 가장 크게 소리 지른 사람에게 안주 우선권!”",
      "“대학 생활의 낭만은 지금부터입니다. 잔 채우고 건배!”",
      "“교수님 뒷담화도 오늘은 무죄! 동아리 텐션 시원하게 올려봅니다!”",
      "“선배님 지갑 털릴 준비 되셨습니까? 후배님들 잔 높이 드세요!”"
    ],
    "2차": [
      "“개강/종강의 한을 술잔에 담아! 오늘 밤 동아리 회식 텐션 천장 뚫어버립니다!”",
      "“선배님들 지갑 열릴 시간입니다! 후배들은 잔 높이 들고 힘차게 응원하세요!”",
      "“동아리 장기자랑 들어갑니다! 끼와 흥을 아낌없이 방출하세요!”",
      "“2차 오니까 단합력 미쳤네요! 007빵 장전하시고 슛 들어갑니다!”",
      "“홍삼 게임 에브리바디 홍삼! 리듬 놓치면 바로 흑기사 갑니다!”",
      "“선배님 사랑합니다 삼행시 발사! 감동의 눈물과 함께 원샷!”",
      "“우리 과, 우리 동아리가 우주 최강입니다! 다 함께 떼창 짠!”"
    ],
    "3차+": [
      "“동아리 번창을 위하여! 남은 용사들끼리 어깨동무하고 마지막 원샷 갑니다!”",
      "“축제 엔딩곡 깔아드립니다! 다 같이 목청껏 떼창하며 잔을 비웁니다!”",
      "“동방에서 컵라면 끓일 파티원 모집 완료! 막잔 시원하게 털어 넣읍시다!”",
      "“차기 회장 당선 축하드립니다! 다음 학기도 우리 동아리 대박 기원!”",
      "“동방 청소 당번 정하기 가위바위보 준비하시고, 살아남으세요!”",
      "“선배님들의 주옥같은 인생 명언 가슴에 새기며 다 같이 건배!”",
      "“과잠 깃 세우고 첫차 타러 갑시다! 오늘 회식 완벽 대성공!”"
    ]
  }},
  "회사 회식": {{
    "1차": [
      "“오늘 하루도 고생 많으셨습니다! 업무 스트레스는 제가 다 믹싱해서 갈아버립니다, 건배!”",
      "“칼퇴의 기쁨을 술잔에 담아! 오늘 야근 막아준 동료에게 박수 보내며 짠 합시다!”",
      "“월요병 퇴치 비트 들어갑니다! 편안한 마음으로 술자리 즐기시죠!”",
      "“팀장님도 부장님도 오늘만큼은 음악과 안주에 집중! 즐겁게 달려봅시다!”",
      "“회사 밖에서는 모두가 평등합니다. 시원하게 첫 잔 짠!”",
      "“이번 분기 목표 달성과 인센티브 대박을 기원하며 잔을 높이 듭니다!”",
      "“센스 터지는 3초 건배사 릴레이 들어갑니다! 잔 가득 채우세요!”"
    ],
    "2차": [
      "“부장님도 래퍼 빙의할 시간입니다. 오늘 결제는 법카니까 브레이크 없이 질주합니다!”",
      "“노래방 치트키 장전하시고! 오늘 팀워크 게이지 200% 충전하고 갑니다!”",
      "“법카 한도 뚫릴 때까지 안주 털러 갑니다! 모두 잔을 높이 드세요!”",
      "“세대 격차는 이 비트로 종결합니다! 전 세대 대통합 건배!”",
      "“회사 영어 금지! 컨펌, 어레인지 말하는 순간 즉시 벌주 들어갑니다!”",
      "“팀장님의 20대 청춘 명곡 틀어드립니다! 모두 다 같이 리듬 타시죠!”",
      "“디저트 하겐다즈 걸고 팀장님과 가위바위보 한판 승부 갑니다!”"
    ],
    "3차+": [
      "“내일 출근 걱정은 잠시 접어두고! 안전 귀가와 팀의 무궁한 발전을 위해 막잔 원샷!”",
      "“살아남은 팀원들에게 경의를 표합니다. 택시비 내기 가위바위보 준비하세요!”",
      "“오늘 회식 대성공! 서로 수고했다고 악수하며 훈훈하게 마무리합시다!”",
      "“내일 아침 모닝커피 쏠 사람 정하는 공정한 승부! 가위바위보 갑니다!”",
      "“막차 놓친 팀원들 카카오택시 탑승 완료! 서로 챙겨주는 우리 팀 최고!”",
      "“내일 9시 정시 출근 서약과 함께 프로페셔널하게 막잔 비웁니다!”",
      "“올해 프로젝트 대박과 성과급 파티를 기원하며, 파이팅 건배!”"
    ]
  }}
}};

    // 36 Diverse Party Games & Missions
    const MISSIONS_DB = {{
      high: [
        {{
          title: "후렴 나오기 전 3초 눈치게임",
          desc: "노래 비트 드롭 직전까지 1부터 순서대로 외치기! 동시에 외치거나 마지막에 남은 사람 원샷!",
          ruleTitle: "3초 눈치게임 룰",
          steps: [
            "누구든 먼저 1을 외치며 게임을 시작합니다.",
            "동시에 같은 숫자를 외치면 두 사람 모두 즉시 패배!",
            "마지막 숫자까지 눈치 보며 못 외친 최후의 1인이 벌칙주를 마십니다."
          ]
        }},
        {{
          title: "노필터 손병호 게임",
          desc: "돌아가며 억울한 사실 하나씩 털기! 손가락 5개 먼저 다 접은 사람이 벌칙주 흑기사 없음!",
          ruleTitle: "손병호 게임 룰",
          steps: [
            "돌아가며 순서대로 “~해본 사람 접어”를 외칩니다.",
            "해당되는 사람은 변명 없이 손가락 하나를 접습니다.",
            "손가락 5개를 가장 먼저 다 접은 사람이 벌칙주 당첨!"
          ]
        }},
        {{
          title: "3초 아이컨택 지목게임",
          desc: "하나 둘 셋과 동시에 마음에 드는 사람을 가리킵니다! 서로 통한 쌍은 건배, 혼자 남은 사람은 원샷!",
          ruleTitle: "아이컨택 지목 룰",
          steps: [
            "구호에 맞춰 동시에 한 사람을 손가락으로 지목합니다.",
            "서로 통한 쌍은 사이좋게 짠을 합니다.",
            "지목받지 못했거나 엇갈린 사람은 벌칙주를 마십니다!"
          ]
        }},
        {{
          title: "안녕 클레오파트라 고음 배틀",
          desc: "돌아가며 한 키씩 높여 외치기! 삑사리 나거나 음 못 올리면 즉시 탈락!",
          ruleTitle: "클레오파트라 룰",
          steps: [
            "“안녕 클레오파트라 세상에서 제일가는 포테이토칩”을 부릅니다.",
            "다음 사람은 앞사람보다 무조건 높은 음으로 불러야 합니다.",
            "목소리가 갈라지거나 포기하면 벌칙주!"
          ]
        }},
        {{
          title: "쇼미더머니 4마디 싸이퍼",
          desc: "비트에 맞춰 아무말 랩 4마디씩 뱉기! 비트 놓치거나 절면 즉시 원샷!",
          ruleTitle: "싸이퍼 배틀 룰",
          steps: [
            "흘러나오는 힙합 비트에 맞춰 라임을 얹습니다.",
            "가사가 안 떠오르면 옹알이라도 플로우 타기!",
            "가장 빵 터지거나 절어버린 사람이 벌칙주 당첨!"
          ]
        }},
        {{
          title: "귓속말 게임",
          desc: "오른쪽 사람 귀에 질문을 속삭입니다. 지목당한 사람은 무슨 질문인지 알고 싶으면 술을 마셔야 합니다!",
          ruleTitle: "귓속말 게임 룰",
          steps: [
            "옆 사람에게만 들리게 “여기서 제일 ~한 사람”을 속삭입니다.",
            "지목당한 사람은 무슨 질문인지 알기 위해 술 한 잔을 원샷해야 질문이 공개됩니다!",
            "비밀 유지가 깨지는 순간 폭소 보장!"
          ]
        }},
        {{
          title: "침묵의 007빵",
          desc: "목소리 내면 탈락! 오직 손동작과 눈빛으로만 007빵을 돌립니다.",
          ruleTitle: "침묵의 007빵 룰",
          steps: [
            "소리를 절대 내지 않고 손가락으로 영-영-칠-빵을 가리킵니다.",
            "‘빵’을 맞은 양옆 사람은 소리 없이 손을 들어야 합니다.",
            "소리를 내거나 엉뚱한 행동을 한 사람이 벌칙주!"
          ]
        }},
        {{
          title: "훈민정음 (초성 스피드 퀴즈)",
          desc: "술래가 초성을 부르면 3초 안에 단어를 외치고 엄지를 들어야 합니다. 꼴찌는 벌칙!",
          ruleTitle: "훈민정음 룰",
          steps: [
            "술래가 자음 두 개(예: ㄱㄱ)를 외칩니다.",
            "단어(고기, 감기 등)를 외친 사람은 중앙에 엄지를 올립니다.",
            "가장 늦게 엄지를 올린 최후의 1인이 마십니다."
          ]
        }},
        {{
          title: "하이라이트 떼창 배틀",
          desc: "노래 후렴구 나올 때 가장 열정적으로 목청껏 부른 사람에게 안주 우선권 지급!",
          ruleTitle: "떼창 배틀 룰",
          steps: [
            "BGM 후렴구에 맞춰 다 같이 떼창을 부릅니다.",
            "가장 흥이 폭발한 사람을 전원 투표로 선정!",
            "가장 얌전하게 있던 사람이 벌칙주를 마십니다."
          ]
        }},
        {{
          title: "3초 병뚜껑 날리기",
          desc: "소주 뚜껑 꼬리를 튕겨서 날린 사람이 양옆 사람에게 벌칙주 하사!",
          ruleTitle: "병뚜껑 룰",
          steps: [
            "돌아가며 손가락으로 꼬리를 한 번씩 튕깁니다.",
            "꼬리를 떨어뜨린 사람이 승리자!",
            "승리자가 지목한 사람이 원샷을 합니다."
          ]
        }}
      ],
      normal: [
        {{
          title: "상황 맞춤 술자리 미션",
          desc: "돌아가며 오른쪽 사람의 첫인상을 딱 세 글자로 솔직하게 말해주세요! 가장 빵 터진 사람이 다음 곡 버튼 누르기!",
          ruleTitle: "첫인상 토크 룰",
          steps: [
            "눈 피하지 말고 오른쪽 사람 얼굴을 3초간 응시합니다.",
            "생각나는 첫인상 키워드를 딱 세 글자로 외칩니다.",
            "가장 빵 터진 대답을 들은 사람이 다음 곡을 선곡합니다!"
          ]
        }},
        {{
          title: "이상형 밸런스 토크",
          desc: "‘유머 코드 맞는 사람’ vs ‘얼굴 내 취향인 사람’ 중 각자 솔직하게 선택하고 이유 말하기!",
          ruleTitle: "밸런스 토크 룰",
          steps: [
            "3초 안에 둘 중 하나를 동시에 손가락으로 가리킵니다.",
            "소수 의견을 낸 사람이 솔직하게 이유를 털어놓습니다.",
            "공감한 사람끼리 다 같이 잔을 부딪칩니다!"
          ]
        }},
        {{
          title: "옆 사람 칭찬 릴레이",
          desc: "오른쪽 사람의 장점 3가지를 10초 안에 숨도 안 쉬고 말하기! 버벅거리면 마시기!",
          ruleTitle: "칭찬 릴레이 룰",
          steps: [
            "옆 사람의 칭찬거리 3개를 빠르게 외칩니다.",
            "오글거려도 진심을 담아 칭찬합니다.",
            "칭찬을 들은 사람이 감사의 뜻으로 건배사를 제의합니다."
          ]
        }},
        {{
          title: "선후배 리셋 3분 야자타임",
          desc: "앞으로 딱 3분간 나이/학번 리셋! 반말로 건배사 한 사람에게 가산점!",
          ruleTitle: "야자타임 룰",
          steps: [
            "타이머 시작과 동시에 모든 존댓말이 금지됩니다.",
            "편하게 말을 놓으며 그동안 못 했던 질문을 던집니다.",
            "존댓말 실수한 사람이 벌칙주를 마십니다!"
          ]
        }},
        {{
          title: "폰 갤러리 최근 사진 썰",
          desc: "내 폰 사진첩의 가장 최근 사진을 공개하고 사연을 풉니다. 비밀 사진이면 술로 때우기 가능!",
          ruleTitle: "갤러리 털기 룰",
          steps: [
            "사진첩을 열어 가장 최근 사진을 테이블에 보여줍니다.",
            "도저히 보여줄 수 없는 사진이면 자진해서 벌칙주 한 잔!",
            "재밌는 사연이면 모두 함께 건배!"
          ]
        }},
        {{
          title: "아파트 게임",
          desc: "손을 무작위로 쌓아 술래가 부른 층수에 손이 걸린 사람이 패배!",
          ruleTitle: "아파트 게임 룰",
          steps: [
            "아-파트 아파트 구호와 함께 손을 무작위로 포갭니다.",
            "술래가 원하는 층수(예: 15층)를 외칩니다.",
            "맨 밑 손부터 빼서 올리며 해당 층수에 걸린 사람이 마십니다."
          ]
        }},
        {{
          title: "영단어 금지 훈민정음 모드 (5분)",
          desc: "앞으로 5분간 영단어(OK, 짠, 마셔, 텐션 등) 쓰면 걸릴 때마다 한 잔씩!",
          ruleTitle: "영단어 금지 룰",
          steps: [
            "외래어와 영어를 절대 쓰지 않고 순우리말로 대화합니다.",
            "‘오케이’, ‘원샷’ 등 영어를 쓴 사람은 즉시 적발되어 마십니다.",
            "유도신문으로 상대를 낚는 것이 꿀잼 포인트!"
          ]
        }}
      ],
      chill: [
        {{
          title: "서로의 흑역사 폭로 토크",
          desc: "가장 어처구니없었던 흑역사를 푼 사람에게 술 마실 권한을 드립니다.",
          ruleTitle: "흑역사 토크 룰",
          steps: [
            "학창 시절이나 최근에 겪은 역대급 흑역사를 고백합니다.",
            "듣는 사람들이 점수를 매겨 가장 치명적인 사람을 뽑습니다.",
            "위로의 의미로 다 함께 잔을 부딪칩니다!"
          ]
        }},
        {{
          title: "인생 영화 & 인생곡 추천",
          desc: "내가 가장 힘들 때 위로받았던 인생 명곡이나 영화 하나씩 공유하기.",
          ruleTitle: "인생 취향 토크 룰",
          steps: [
            "각자 마음에 남는 인생 콘텐츠를 소개합니다.",
            "취향이 겹치는 사람끼리 깊은 대화를 나눕니다.",
            "낭만적인 분위기 속에 잔을 채웁니다."
          ]
        }},
        {{
          title: "로또 1등 되면 할 일 3가지",
          desc: "로또 50억 당첨되면 당장 내일 아침에 뭐 할지 솔직하게 털어놓기!",
          ruleTitle: "로또 토크 룰",
          steps: [
            "현실적인 계획부터 황당한 망상까지 자유롭게 고백합니다.",
            "테이블 사람들에게 얼마씩 쏠지 공약하기!",
            "미래의 대박을 기원하며 건배!"
          ]
        }},
        {{
          title: "최근 가장 설렜던 순간 고백",
          desc: "연애든 취미든 최근 내 심장을 뛰게 만들었던 순간 하나씩 털기!",
          ruleTitle: "설렘 토크 룰",
          steps: [
            "사소하지만 설렜던 순간을 담백하게 말합니다.",
            "거짓말하거나 억지로 꾸며내면 의심주 마시기!",
            "따뜻한 분위기로 짠을 합니다."
          ]
        }},
        {{
          title: "첫인상 vs 현인상 솔직 비교",
          desc: "처음 봤을 때랑 지금 몇 시간 마셔보고 나서 바뀐 인상 솔직하게 털기!",
          ruleTitle: "인상 비교 룰",
          steps: [
            "처음엔 차가워 보였는데 사실은 허당이라든지 솔직하게 말합니다.",
            "반전 매력을 인정받은 사람에게 박수!",
            "더 친해진 기념으로 다 같이 잔을 부딪칩니다."
          ]
        }}
      ]
    }};

    // 30+ AI MC Banters
    const BANTERS_DB = {{
      high: [
        "“오호, 비트 묵직한 거 들어갑니다! 헤드뱅잉 장전하시고 원샷 갑니다!”",
        "“쇼미더머니 각 나왔네요! 텐션 터졌으니 브레이크 없이 질주합니다!”",
        "“드랍 더 비트! 오늘 누구 하나 업혀 나가기 전까지 선곡 빡세게 갑니다!”",
        "“비트 빨라진 거 느껴지시죠? 지금부터 폰 보는 사람은 흑기사 없습니다!”",
        "“분위기 제대로 달아올랐네요. 이 타이밍에 빼는 건 반칙입니다, 원샷!”",
        "“부장님도 래퍼 빙의할 시간입니다. 오늘 결제는 법카니까 끝까지 갑니다!”",
        "“여기 술자리 맞죠? 클럽 온 거 아니죠? 텐션 미쳤네요 계속 갑니다!”",
        "“자, 이번 판은 살살 안 갑니다. 걸리면 무조건 잔 비우는 걸로!”",
        "“심장 박동수랑 BPM 맞춰드릴게요. 잔 채우고 바로 돌진합니다!”",
        "“목 쉴 때까지 떼창 부르는 겁니다. 후렴구 안 부르면 탈락이에요!”",
        "“어색했던 분들 맞나요? 텐션 200% 찍었으니 더 센 트랩으로 꺾습니다!”"
      ],
      normal: [
        "“다들 눈 마주치면 큰일 나는 병 걸리셨어요? 폰 내려놓고 첫인상부터 털고 갑시다.”",
        "“슬슬 알콜 들어가서 말문 트였죠? 영혼 없는 리액션은 탈락입니다.”",
        "“이 그루브 나오면 고개 절로 흔들리죠? 리듬 타면서 다음 미션 갑니다.”",
        "“적당히 비트 타면서 서로 호구조사 끝내봅시다. 판 다시 깝니다!”",
        "“분위기 알맞게 익었네요. 여기서 힙한 비트 한 번 더 얹어드릴게요.”",
        "“선배 후배 눈치 보지 말고 동아리방처럼 편하게 썰 풉시다!”",
        "“음악 딱 좋죠? 이 분위기 살려서 테이블 전원 참여 미션 갑니다.”",
        "“잔 비어 있는 사람 누구죠? 잔 채우고 템포 맞춰갑니다!”",
        "“대화 정적 흐르려던 찰나에 제가 딱 들어왔죠? 다음 턴 갑니다!”"
      ],
      chill: [
        "“속도 좀 조절할게요. 감성 힙합 깔아드릴 테니 진솔한 얘기 좀 터봅시다.”",
        "“분위기 너무 달렸네요. 템포 잠깐 낮추고 옛날 흑역사 하나씩 털어놓고 짠합시다.”",
        "“슬슬 진지한 얘기 나오는 시간입니다. 오늘 고생한 사람들한테 칭찬 하나씩 던지시죠.”",
        "“다들 숨 좀 고르세요. 칠(Chill)한 BGM 깔아드릴 테니 깊은 토크 갑니다.”",
        "“술자리에서 이런 얘기 한 번쯤 나와야 진짜 친해지는 법이죠.”",
        "“템포 다운! 잔잔하게 술잔 기울이면서 서로 속마음 좀 들어봅시다.”",
        "“오늘 밤 분위기 감성 제대로네요. 잔 채우고 조용히 건배 한 번 갑니다.”"
      ]
    }};

    // App State
    const state = {{
      groupType: null,
      round: null,
      atmosphere: null,
      genre: null,
      mood: 'normal',
      playMode: 'automix', // 'automix', 'manual'
      playedKeys: new Set(),
      playedMissions: new Set(),
      playedBanters: new Set(),
      loopCount: 0,
      strobeOn: false,
      history: [],
      historyIdx: -1
    }};

    // Setup chip selector
    function selectChip(category, value, el) {{
      soundEngine.playScratch();
      state[category] = value;

      const parent = el.parentElement;
      parent.querySelectorAll('.chip-btn').forEach(btn => {{
        btn.classList.remove(
          'border-neonPurple', 'border-neonCyan', 'border-neonPink', 'border-neonGreen',
          'bg-purple-950/80', 'bg-cyan-950/80', 'bg-pink-950/80', 'bg-emerald-950/80',
          'text-white', 'border-b-purple-400', 'border-b-cyan-400', 'border-b-pink-400', 'border-b-emerald-400',
          'shadow-[0_0_15px_rgba(168,85,247,0.4)]', 'shadow-[0_0_15px_rgba(6,182,212,0.4)]',
          'shadow-[0_0_15px_rgba(236,72,153,0.4)]', 'shadow-[0_0_15px_rgba(34,197,94,0.4)]'
        );
        btn.classList.add('border-zinc-700/80', 'border-b-zinc-950', 'bg-zinc-900/90', 'text-zinc-300');
      }});

      let border = 'border-neonPurple', bg = 'bg-purple-950/80', shadow = 'shadow-[0_0_15px_rgba(168,85,247,0.4)]', bBorder = 'border-b-purple-400';
      if (category === 'round') {{
        border = 'border-neonCyan';
        bg = 'bg-cyan-950/80';
        shadow = 'shadow-[0_0_15px_rgba(6,182,212,0.4)]';
        bBorder = 'border-b-cyan-400';
      }} else if (category === 'atmosphere') {{
        border = 'border-neonPink';
        bg = 'bg-pink-950/80';
        shadow = 'shadow-[0_0_15px_rgba(236,72,153,0.4)]';
        bBorder = 'border-b-pink-400';
      }} else if (category === 'genre') {{
        border = 'border-neonGreen';
        bg = 'bg-emerald-950/80';
        shadow = 'shadow-[0_0_15px_rgba(34,197,94,0.4)]';
        bBorder = 'border-b-emerald-400';
      }}

      el.classList.remove('border-zinc-700/80', 'border-b-zinc-950', 'bg-zinc-900/90', 'text-zinc-300');
      el.classList.add(border, bg, shadow, bBorder, 'text-white');

      if (category === 'atmosphere') {{
        if (value === '어색함') state.mood = 'chill';
        else if (value === '올라옴') state.mood = 'normal';
        else if (value === '폭발') state.mood = 'high';
      }}

      checkCanStart();
    }}

    function selectPlayMode(mode, el) {{
      soundEngine.playScratch();
      state.playMode = mode;

      document.querySelectorAll('.mode-chip').forEach(btn => {{
        btn.classList.remove(
          'border-neonCyan', 'border-neonPurple',
          'bg-cyan-950/80', 'bg-purple-950/80',
          'text-white', 'border-b-cyan-400', 'border-b-purple-400',
          'shadow-[0_0_15px_rgba(6,182,212,0.4)]', 'shadow-[0_0_15px_rgba(168,85,247,0.4)]'
        );
        btn.classList.add('border-zinc-700/80', 'border-b-zinc-950', 'bg-zinc-900/90', 'text-zinc-300');
      }});

      el.classList.remove('border-zinc-700/80', 'border-b-zinc-950', 'bg-zinc-900/90', 'text-zinc-300');
      if (mode === 'automix') {{
        el.classList.add('border-neonCyan', 'border-b-cyan-400', 'bg-cyan-950/80', 'text-white', 'shadow-[0_0_15px_rgba(6,182,212,0.4)]');
      }} else {{
        el.classList.add('border-neonPurple', 'border-b-purple-400', 'bg-purple-950/80', 'text-white', 'shadow-[0_0_15px_rgba(168,85,247,0.4)]');
      }}
    }}

    // Play Mode switcher on desk (Supports 30s auto-mix and manual mix)
    function setPlayMode(mode) {{
      soundEngine.playScratch();
      state.playMode = mode;
      state.loopCount = 0;
      
      const btnMix = document.getElementById('modeBtnMix');
      const btnManual = document.getElementById('modeBtnManual');
      const bgm = document.getElementById('realBgmAudio');

      [btnMix, btnManual].forEach(b => {{
        if (b) b.className = 'arcade-btn px-2.5 py-1 rounded-lg font-bold text-zinc-400 hover:text-white border-b-transparent transition';
      }});

      if (mode === 'automix') {{
        if (btnMix) btnMix.className = 'arcade-btn px-2.5 py-1 rounded-lg font-black bg-neonCyan text-black shadow-md border-b-cyan-700 transition';
        showToast("⚡️ 30초 자동믹싱 ON! (끝나면 다음 라운드로 즉시 자동 전환)");
        if (bgm && bgm.paused) bgm.play();
      }} else if (mode === 'manual') {{
        if (btnManual) btnManual.className = 'arcade-btn px-2.5 py-1 rounded-lg font-black bg-neonPurple text-white shadow-[0_0_12px_rgba(168,85,247,0.5)] border-b-purple-900 transition';
        showToast("⏸ 수동 믹싱 ON! (곡이 끝나면 대기하며 직접 다음 곡을 넘깁니다)");
      }}
    }}

    // Vinyl Scratch handler
    function handleVinylScratch() {{
      soundEngine.playScratch();
      const disc = document.getElementById('vinylDisc');
      if (disc) {{
        disc.classList.add('scale-95');
        setTimeout(() => disc.classList.remove('scale-95'), 150);
      }}
      showToast("💿 DJ SCRATCH! *끼긱-끼긱*");
    }}

    // DJ Soundpad Live Trigger
    function triggerSoundpad(type, el) {{
      if (type === 'horn') soundEngine.playAirhorn();
      else if (type === 'drop') soundEngine.playBassDrop();
      else if (type === 'siren') soundEngine.playSiren();
      else if (type === 'oneshot') soundEngine.playOneShot();

      if (el) {{
        el.classList.add('ring-2', 'ring-white', 'scale-95');
        setTimeout(() => el.classList.remove('ring-2', 'ring-white', 'scale-95'), 180);
      }}

      if (state.strobeOn) {{
        document.body.classList.add('strobe-active-glow');
        setTimeout(() => document.body.classList.remove('strobe-active-glow'), 250);
      }}
    }}

    // Club Strobe Lighting Toggle
    function toggleStrobe() {{
      state.strobeOn = !state.strobeOn;
      const btn = document.getElementById('strobeToggleBtn');
      const txt = document.getElementById('strobeText');
      const body = document.body;
      soundEngine.playScratch();

      if (state.strobeOn) {{
        body.classList.add('strobe-active');
        if (btn) btn.className = "px-2.5 py-1 rounded-full bg-gradient-to-r from-pink-600 to-purple-600 border border-pink-400 text-[11px] font-black text-white flex items-center space-x-1 transition shadow-lg animate-pulse";
        if (txt) txt.textContent = "🚨 사이키 ON!";
        showToast("🚨 클럽 사이키 모드 ON! 테이블 조명을 켜세요!");
      }} else {{
        body.classList.remove('strobe-active');
        if (btn) btn.className = "px-2.5 py-1 rounded-full bg-zinc-900 hover:bg-pink-950/80 border border-zinc-700 hover:border-pink-500/80 text-[11px] font-black text-zinc-300 hover:text-pink-300 flex items-center space-x-1 transition shadow";
        if (txt) txt.textContent = "사이키 OFF";
        showToast("사이키 조명을 껐습니다.");
      }}
    }}

    // Initialize 16-Band Equalizer Spectrum
    function initSpectrum() {{
      const container = document.getElementById('spectrumVisualizer');
      if (!container) return;
      container.innerHTML = '';
      const colors = ['bg-neonGreen', 'bg-neonGreen', 'bg-neonCyan', 'bg-neonCyan', 'bg-neonPurple', 'bg-neonPurple', 'bg-neonPink', 'bg-neonOrange', 'bg-red-500'];
      for (let i = 0; i < 16; i++) {{
        const bar = document.createElement('div');
        const color = colors[Math.min(Math.floor(i / 2), colors.length - 1)];
        const dur = (0.35 + Math.random() * 0.35).toFixed(2);
        const delay = (Math.random() * 0.3).toFixed(2);
        bar.className = `flex-1 rounded-t-sm ${{color}} visualizer-bar`;
        bar.style.animation = `barPulse ${{dur}}s ease-in-out ${{delay}}s infinite alternate`;
        container.appendChild(bar);
      }}
    }}


    // Direct Spotify 1-Tap Launcher
    function openSpotifyDirect() {{
      if (state.historyIdx >= 0 && state.history[state.historyIdx]) {{
        const cur = state.history[state.historyIdx].track;
        const bgm = document.getElementById('realBgmAudio');
        if (bgm && !bgm.paused) {{
          bgm.pause();
          setVinylSpinning(false);
          const icon = document.getElementById('deskPlayIcon');
          if (icon) icon.textContent = '▶';
          const stat = document.getElementById('audioStatusText');
          if (stat) stat.textContent = '일시 정지됨';
        }}
        soundEngine.playAirhorn();

        const q = encodeURIComponent(`${{cur.artist}} ${{cur.title}}`);
        showToast(`🟢 Spotify로 이동: [${{cur.title}}] 완곡 스트리밍!`);
        
        const spotifyAppUri = `spotify:search:${{q}}`;
        const spotifyWebUrl = `https://open.spotify.com/search/${{q}}`;
        
        const start = Date.now();
        window.location.href = spotifyAppUri;
        setTimeout(() => {{
          if (Date.now() - start < 1500) {{
            window.open(spotifyWebUrl, '_blank');
          }}
        }}, 600);
      }}
    }}

    function checkCanStart() {{
      const btn = document.getElementById('startSessionBtn');
      const txt = document.getElementById('startBtnText');
      const sub = document.getElementById('startBtnSub');
      if (state.groupType && state.round && state.atmosphere && state.genre) {{
        btn.disabled = false;
        btn.className = "arcade-btn animate-flow-gradient w-full py-4 px-5 rounded-2xl font-black text-base flex flex-col items-center justify-center space-y-0.5 transition duration-300 bg-gradient-to-r from-neonPurple via-neonPink to-neonCyan text-white cursor-pointer shadow-[0_0_25px_rgba(236,72,153,0.6)] border-b-4 border-b-purple-950 active:translate-y-1";
        txt.textContent = `🔥 AI DJ ON AIR (파티 & 음악 시작)`;
        if (sub) sub.textContent = `선택한 장르와 분위기에 맞는 비트가 즉시 재생됩니다!`;
      }} else {{
        btn.disabled = true;
        btn.className = "arcade-btn w-full py-4 px-5 rounded-2xl font-black text-base flex flex-col items-center justify-center space-y-0.5 transition duration-300 bg-zinc-900 text-zinc-600 cursor-not-allowed border border-zinc-800 border-b-zinc-950";
        txt.textContent = `4가지 항목을 선택해 주세요`;
        if (sub) sub.textContent = `모임 성격 · 차수 · 분위기 · 장르 선택 대기 중`;
      }}
    }}

    // Start Session
    function startDjSession() {{
      if (!state.groupType || !state.round || !state.atmosphere || !state.genre) return;
      soundEngine.playAirhorn();

      document.getElementById('screen-setup').classList.add('hidden');
      document.getElementById('screen-console').classList.remove('hidden');

      initSpectrum();
      setPlayMode(state.playMode || 'sing');
      generateNewRound();
    }}

    // Random Pick helper
    function pickRandom(arr) {{
      return arr[Math.floor(Math.random() * arr.length)];
    }}

    // Generate a fresh new round and push to history
    function generateNewRound() {{
      const mood = state.mood || 'normal';
      state.loopCount = 0;

      // 1. Filter by Genre
      let pool = ALL_TRACKS;
      if (state.genre && state.genre !== 'ALL') {{
        if (state.genre === 'HIPHOP') {{
          pool = ALL_TRACKS.filter(t => t.genre === 'HIPHOP' || t.genre === 'GLOBAL HIPHOP');
        }} else if (state.genre === 'KPOP') {{
          pool = ALL_TRACKS.filter(t => t.genre === 'K-POP');
        }} else if (state.genre === 'BAND') {{
          pool = ALL_TRACKS.filter(t => ['BAND', 'POP', 'INDIE'].includes(t.genre));
        }}
      }}

      // 2. Filter by Mood
      let moodPool = pool.filter(t => t.mood === mood);
      if (moodPool.length > 0) {{
        pool = moodPool;
      }} else if (pool.length === 0) {{
        pool = ALL_TRACKS.filter(t => t.mood === mood);
        if (pool.length === 0) pool = ALL_TRACKS;
      }}

      // 3. Duplicate Prevention (No repeats until all songs in the pool are played)
      if (!state.playedKeys) state.playedKeys = new Set();
      
      let unplayed = pool.filter(t => !state.playedKeys.has((t.title + '---' + t.artist).toLowerCase()));
      if (unplayed.length === 0) {{
        // Entire pool played! Reset played keys for this pool to start fresh cycle
        pool.forEach(t => state.playedKeys.delete((t.title + '---' + t.artist).toLowerCase()));
        unplayed = pool;
      }}

      const track = pickRandom(unplayed.length > 0 ? unplayed : pool);
      state.playedKeys.add((track.title + '---' + track.artist).toLowerCase());

      // 3. Situation-Aware Contextual Missions (No-repeat shuffle)
      const grp = state.groupType || '미팅/과팅';
      const rnd = state.round || '1차';
      let missionList = [];

      if (SITUATION_MISSIONS[grp] && SITUATION_MISSIONS[grp][rnd]) {{
        missionList = SITUATION_MISSIONS[grp][rnd];
      }} else if (SITUATION_MISSIONS[grp]) {{
        Object.values(SITUATION_MISSIONS[grp]).forEach(arr => missionList.push(...arr));
      }}

      if (!missionList || missionList.length === 0) {{
        missionList = MISSIONS_DB[mood] || MISSIONS_DB['normal'];
      }}

      let unplayedMissions = missionList.filter(m => !state.playedMissions.has(m.title));
      if (unplayedMissions.length === 0) {{
        state.playedMissions.clear();
        unplayedMissions = missionList;
      }}
      const mission = pickRandom(unplayedMissions);
      state.playedMissions.add(mission.title);

      // 4. Situation-Aware AI DJ Host Banters (No-repeat shuffle)
      let banterList = [];
      if (CONTEXT_BANTERS[grp] && CONTEXT_BANTERS[grp][rnd]) {{
        banterList = CONTEXT_BANTERS[grp][rnd];
      }} else if (CONTEXT_BANTERS[grp]) {{
        Object.values(CONTEXT_BANTERS[grp]).forEach(arr => banterList.push(...arr));
      }}

      if (!banterList || banterList.length === 0) {{
        banterList = BANTERS_DB[mood] || BANTERS_DB['normal'];
      }}

      let unplayedBanters = banterList.filter(b => !state.playedBanters.has(b));
      if (unplayedBanters.length === 0) {{
        state.playedBanters.clear();
        unplayedBanters = banterList;
      }}
      const banter = pickRandom(unplayedBanters);
      state.playedBanters.add(banter);

      const roundData = {{
        track,
        banter,
        mission,
        mood,
        roundNumber: state.history.length + 1
      }};

      state.history.push(roundData);
      state.historyIdx = state.history.length - 1;

      renderRound(roundData);
    }}

    // Render a round from history or new
    function renderRound(data) {{
      const {{ track, banter, mission, mood, roundNumber }} = data;

      // Update Header & Round
      const genreNames = {{ 'ALL': '올장르', 'HIPHOP': '힙합', 'KPOP': 'K-POP', 'BAND': '밴드/인디' }};
      const genreLabel = genreNames[state.genre] || '올장르';
      document.getElementById('consoleSessionTag').textContent = `${{state.groupType}} · ${{state.round}} · ${{genreLabel}} · ${{mood.toUpperCase()}}`;
      document.getElementById('trackRoundCount').textContent = `ROUND ${{roundNumber}} (${{state.historyIdx + 1}}/${{state.history.length}})`;
      
      const badge = document.getElementById('trackGenreBadge');
      badge.textContent = `${{track.genre || 'PARTY'}} · ${{mood === 'high' ? '🔥 135 BPM' : mood === 'chill' ? '😌 80 BPM' : '🥂 110 BPM'}}`;
      badge.className = `text-[10px] font-bold px-2 py-0.5 rounded bg-zinc-800 ${{mood === 'high' ? 'text-orange-400 border-orange-800/60' : mood === 'chill' ? 'text-blue-300 border-blue-800/60' : 'text-neonCyan border-cyan-800/60'}} border`;

      // Update Track Info
      document.getElementById('trackTitle').textContent = track.title;
      document.getElementById('trackArtist').textContent = track.artist;
      document.getElementById('trackArtwork').src = track.artwork;

      // Update AI Banter
      document.getElementById('mcBanterText').textContent = banter;

      // Update Mission
      document.getElementById('missionTitle').textContent = mission.title;
      document.getElementById('missionDesc').textContent = mission.desc;
      document.getElementById('ruleBtnLabel').textContent = `${{mission.ruleTitle}} 보기`;

      // Update Modal
      document.getElementById('modalTitle').textContent = mission.ruleTitle;
      document.getElementById('ruleStep1').textContent = mission.steps[0];
      document.getElementById('ruleStep2').textContent = mission.steps[1];
      document.getElementById('ruleStep3').textContent = mission.steps[2];

      // Update DJ Track Note (곡 한줄 설명)
      const noteEl = document.getElementById('djTrackNoteText');
      if (noteEl) {{
        noteEl.textContent = track.description || `"${{track.artist}} - ${{track.title}}: 분위기를 띄우는 신나는 비트! 🍻"`;
      }}

      // Synchronize 30s background audio
      const bgm = document.getElementById('realBgmAudio');
      if (bgm && track.audioUrl) {{
        if (bgm.src !== track.audioUrl) {{
          bgm.src = track.audioUrl;
        }}
        bgm.currentTime = 0;
        bgm.loop = false; // Clean 30-second round
        bgm.play().then(() => {{
          setVinylSpinning(true);
          const icon = document.getElementById('deskPlayIcon');
          if (icon) icon.textContent = '⏸';
          const modeLabels = {{ 'automix': '⚡️ 30초 믹싱', 'manual': '⏸ 수동 모드' }};
          document.getElementById('audioStatusText').textContent = modeLabels[state.playMode] || '비트 스트리밍';
        }}).catch(err => {{
          console.warn("Audio play blocked:", err);
          document.getElementById('audioStatusText').textContent = "▶ 터치하여 재생";
          setVinylSpinning(false);
          const icon = document.getElementById('deskPlayIcon');
          if (icon) icon.textContent = '▶';
        }});
      }}
    }}

    // Previous & Next Track Navigation
    function handleHistoryNav(dir) {{
      if (dir === 'prev') {{
        if (state.historyIdx > 0) {{
          soundEngine.playScratch();
          state.historyIdx--;
          renderRound(state.history[state.historyIdx]);
          showToast(`⏮ 이전 곡: [${{state.history[state.historyIdx].track.title}}]`);
        }} else {{
          showToast("첫 번째 곡입니다!");
        }}
      }} else if (dir === 'next') {{
        soundEngine.playScratch();
        if (state.historyIdx < state.history.length - 1) {{
          state.historyIdx++;
          renderRound(state.history[state.historyIdx]);
          showToast(`⏭ 다음 곡: [${{state.history[state.historyIdx].track.title}}]`);
        }} else {{
          generateNewRound();
          showToast(`⏭ 새로운 라운드 출격!`);
        }}
      }}
    }}

    // Play/Pause Toggle
    function togglePlayPause() {{
      const bgm = document.getElementById('realBgmAudio');
      if (bgm.paused) {{
        bgm.play();
        setVinylSpinning(true);
      }} else {{
        bgm.pause();
        setVinylSpinning(false);
        soundEngine.playScratch();
      }}
    }}

    function setVinylSpinning(isSpinning) {{
      const badge = document.getElementById('playStateBadge');
      const deskIcon = document.getElementById('deskPlayIcon');
      const disc = document.getElementById('vinylDisc');
      const spectrum = document.getElementById('spectrumVisualizer');
      if (isSpinning) {{
        if (badge) badge.textContent = '⏸';
        if (deskIcon) deskIcon.textContent = '⏸';
        if (disc) disc.classList.remove('spin-paused');
        if (spectrum) spectrum.classList.remove('paused-anim');
      }} else {{
        if (badge) badge.textContent = '▶';
        if (deskIcon) deskIcon.textContent = '▶';
        if (disc) disc.classList.add('spin-paused');
        if (spectrum) spectrum.classList.add('paused-anim');
      }}
    }}

    // Progress Bar Updater & Seeker
    const bgm = document.getElementById('realBgmAudio');
    bgm.addEventListener('timeupdate', () => {{
      if (bgm.duration) {{
        const pct = (bgm.currentTime / bgm.duration) * 100;
        document.getElementById('audioProgressBar').style.width = `${{pct}}%`;
        
        const curM = Math.floor(bgm.currentTime / 60);
        const curS = Math.floor(bgm.currentTime % 60);
        document.getElementById('audioCurrentTime').textContent = `${{curM}}:${{curS < 10 ? '0' : ''}}${{curS}}`;
        
        const durM = Math.floor(bgm.duration / 60);
        const durS = Math.floor(bgm.duration % 60);
        document.getElementById('audioDuration').textContent = `${{durM}}:${{durS < 10 ? '0' : ''}}${{durS}}`;
      }}
    }});

    function seekAudio(e) {{
      const bar = e.currentTarget;
      const rect = bar.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const pct = clickX / rect.width;
      if (bgm.duration) {{
        bgm.currentTime = pct * bgm.duration;
      }}
    }}

    // Auto next when audio ends (handles 30s automix or manual mode)
    bgm.addEventListener('ended', () => {{
      if (state.playMode === 'automix') {{
        soundEngine.playScratch();
        showToast("⚡️ 30초 믹싱: 다음 라운드로 자동 전환!");
        generateNewRound();
      }} else {{
        setVinylSpinning(false);
        const icon = document.getElementById('deskPlayIcon');
        if (icon) icon.textContent = '▶';
        document.getElementById('audioStatusText').textContent = '재생 완료 (대기 중)';
      }}
    }});

    // Toast
    function showToast(msg) {{
      const toast = document.getElementById('djToast');
      const txt = document.getElementById('djToastText');
      txt.textContent = msg;
      toast.classList.remove('hidden');
      clearTimeout(window.toastTimer);
      window.toastTimer = setTimeout(() => toast.classList.add('hidden'), 3000);
    }}

    // 4 Tension Interaction Handlers
    function handleTensionAction(action) {{
      const missionBox = document.getElementById('missionContainer');

      if (action === 'up') {{
        soundEngine.playAirhorn();
        state.mood = 'high';
        missionBox.classList.add('neon-border-pink');
        setTimeout(() => missionBox.classList.remove('neon-border-pink'), 1000);
        showToast("🔥 텐션 UP! 고텐션 비트와 폭소 게임으로 리믹스!");
      }} else if (action === 'down') {{
        soundEngine.playChillChime();
        state.mood = 'chill';
        showToast("😌 캄다운 모드! 감성적인 곡과 진솔한 토크 미션 출격.");
      }} else if (action === 'next') {{
        soundEngine.playScratch();
        handleHistoryNav('next');
        return;
      }} else if (action === 'keep') {{
        soundEngine.playBassDrop();
        showToast("🎵 현재 바이브 인정! 이 느낌 그대로 계속 달립니다.");
        document.getElementById('mcBanterText').textContent = "“오케이, 지금 흐름 좋습니다. 선곡 안 끊기게 이 바이브 그대로 유지합니다!”";
        return;
      }}

      generateNewRound();
    }}

    // Modal
    function openGameModal() {{
      soundEngine.playScratch();
      document.getElementById('gameRuleModal').classList.remove('hidden');
    }}
    function closeGameModal() {{
      soundEngine.playScratch();
      document.getElementById('gameRuleModal').classList.add('hidden');
    }}

    // Audio Mute
    function toggleAudio() {{
      const isMuted = soundEngine.toggleMute();
      document.getElementById('soundIcon').textContent = isMuted ? '🔇' : '🔊';
      document.getElementById('soundText').textContent = isMuted ? '사운드 OFF' : '사운드 ON';
    }}

    // Back to Setup
    function backToSetup() {{
      bgm.pause();
      document.getElementById('screen-console').classList.add('hidden');
      document.getElementById('screen-setup').classList.remove('hidden');
    }}
  </script>
</body>
</html>
'''

with open('/Users/kimdoyun/.gemini/antigravity/scratch/drinking-party-dj/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully updated index.html with 100% reliable full track launchers!")
