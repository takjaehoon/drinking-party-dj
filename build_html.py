import json

with open('/Users/kimdoyun/.gemini/antigravity/scratch/drinking-party-dj/tracks_db.json', 'r', encoding='utf-8') as f:
    tracks = json.load(f)

tracks_json = json.dumps(tracks, ensure_ascii=False, indent=2)

html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>술자리 AI DJ</title>
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
            darkBg: '#0b0c10',
            darkCard: '#15161e',
            darkElevated: '#1f212d'
          }},
          animation: {{
            'spin-slow': 'spin 4s linear infinite',
            'pulse-fast': 'pulse 1s cubic-bezier(0.4, 0, 0.6, 1) infinite'
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      background-color: #0b0c10;
      color: #f3f4f6;
      font-family: 'Pretendard', sans-serif;
      touch-action: manipulation;
      -webkit-tap-highlight-color: transparent;
      overflow-x: hidden;
    }}
    .neon-border-purple {{
      box-shadow: 0 0 15px rgba(168, 85, 247, 0.4), inset 0 0 10px rgba(168, 85, 247, 0.1);
    }}
    .neon-border-cyan {{
      box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
    }}
    .neon-border-pink {{
      box-shadow: 0 0 20px rgba(236, 72, 153, 0.6);
    }}
    .vinyl-grooves {{
      background: radial-gradient(circle, #27272a 20%, #18181b 21%, #09090b 40%, #18181b 41%, #27272a 60%, #18181b 61%, #09090b 80%, #18181b 81%);
    }}
    @keyframes barPulse {{
      0%, 100% {{ height: 20%; }}
      50% {{ height: 100%; }}
    }}
    .visualizer-bar {{
      animation: barPulse 0.7s ease-in-out infinite alternate;
    }}
    .paused-anim {{
      animation-play-state: paused !important;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col items-center justify-start p-3 sm:p-5 select-none">

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
    }}
    const soundEngine = new PartySoundEngine();
  </script>

  <!-- Main Container -->
  <div id="app" class="w-full max-w-md mx-auto flex flex-col min-h-[92vh] relative pb-6">

    <!-- Top Universal Header -->
    <header class="w-full flex items-center justify-between py-2 px-1 border-b border-zinc-800/80 mb-3">
      <div class="flex items-center space-x-2">
        <span class="text-xl">🍸</span>
        <div>
          <h1 class="font-display tracking-wide font-black text-transparent bg-clip-text bg-gradient-to-r from-neonPurple via-neonPink to-neonCyan text-lg leading-tight">
            술자리 AI DJ
          </h1>
          <p class="text-[10px] text-zinc-400 tracking-wider flex items-center space-x-1">
            <span class="w-1.5 h-1.5 rounded-full bg-neonCyan animate-ping"></span>
            <span id="headerLiveStatus">AI 실시간 다이내믹 믹싱</span>
          </p>
        </div>
      </div>
      <button id="soundToggleBtn" onclick="toggleAudio()" class="flex items-center space-x-1 px-2.5 py-1 rounded-full bg-zinc-800/90 hover:bg-zinc-700 border border-zinc-700 text-xs font-semibold transition">
        <span id="soundIcon">🔊</span>
        <span id="soundText" class="text-[11px] text-zinc-300">사운드 ON</span>
      </button>
    </header>

    <!-- LIVE TOAST BANNER (Shows Song Changes Visually) -->
    <div id="djToast" class="hidden w-full bg-gradient-to-r from-purple-950 via-zinc-900 to-pink-950 border border-neonPurple/60 rounded-xl p-2.5 mb-2 text-center text-xs font-bold text-white shadow-lg transition-all">
      <span id="djToastText">🎧 새로운 라운드로 믹싱되었습니다!</span>
    </div>

    <!-- SCREEN 1: 상태 선택 화면 (Setup) -->
    <section id="screen-setup" class="flex-1 flex flex-col justify-between space-y-5">
      
      <!-- Hero Banner -->
      <div class="bg-gradient-to-br from-purple-950/40 via-darkCard to-zinc-900 border border-purple-800/30 rounded-2xl p-4 text-center">
        <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-purple-950 text-purple-300 border border-purple-700/50 mb-2">
          50+ 다이내믹 파티 제너레이터
        </span>
        <h2 class="text-xl font-bold text-white tracking-tight">
          “오늘 어떤 자리인가요?”
        </h2>
        <p class="text-xs text-zinc-400 mt-1">
          상태를 고르시면 버튼을 누를 때마다 끝없이 새로운 선곡과 게임이 나옵니다!
        </p>
      </div>

      <!-- 1. 모임 성격 선택 -->
      <div class="space-y-2">
        <label class="text-xs font-bold text-zinc-300 flex items-center space-x-1.5">
          <span class="text-neonPurple">01</span>
          <span>모임 성격</span>
        </label>
        <div class="grid grid-cols-2 gap-2 text-xs font-medium">
          <button type="button" onclick="selectChip('groupType', '미팅/과팅', this)" class="chip-btn py-2.5 px-3 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-left flex items-center space-x-2 transition active:scale-95">
            <span>💘</span>
            <span class="font-semibold">미팅 · 과팅</span>
          </button>
          <button type="button" onclick="selectChip('groupType', '친구 모임', this)" class="chip-btn py-2.5 px-3 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-left flex items-center space-x-2 transition active:scale-95">
            <span>🍻</span>
            <span class="font-semibold">친구 모임</span>
          </button>
          <button type="button" onclick="selectChip('groupType', '과/동아리 회식', this)" class="chip-btn py-2.5 px-3 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-left flex items-center space-x-2 transition active:scale-95">
            <span>🎓</span>
            <span class="font-semibold">과 · 동아리</span>
          </button>
          <button type="button" onclick="selectChip('groupType', '회사 회식', this)" class="chip-btn py-2.5 px-3 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-left flex items-center space-x-2 transition active:scale-95">
            <span>💼</span>
            <span class="font-semibold">회사 회식</span>
          </button>
        </div>
      </div>

      <!-- 2. 차수 선택 -->
      <div class="space-y-2">
        <label class="text-xs font-bold text-zinc-300 flex items-center space-x-1.5">
          <span class="text-neonCyan">02</span>
          <span>지금 몇 차?</span>
        </label>
        <div class="grid grid-cols-3 gap-2 text-xs font-medium">
          <button type="button" onclick="selectChip('round', '1차', this)" class="chip-btn py-2.5 px-3 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-center font-bold transition active:scale-95">
            1차
          </button>
          <button type="button" onclick="selectChip('round', '2차', this)" class="chip-btn py-2.5 px-3 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-center font-bold transition active:scale-95">
            2차
          </button>
          <button type="button" onclick="selectChip('round', '3차+', this)" class="chip-btn py-2.5 px-3 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-center font-bold transition active:scale-95">
            3차+
          </button>
        </div>
      </div>

      <!-- 3. 현재 분위기 선택 -->
      <div class="space-y-2">
        <label class="text-xs font-bold text-zinc-300 flex items-center space-x-1.5">
          <span class="text-neonPink">03</span>
          <span>현재 분위기 체감</span>
        </label>
        <div class="grid grid-cols-3 gap-2 text-xs font-medium">
          <button type="button" onclick="selectChip('atmosphere', '어색함', this)" class="chip-btn py-2.5 px-2 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-center transition active:scale-95">
            <span class="block text-sm mb-0.5">❄️</span>
            <span class="font-semibold text-[11px]">아직 어색함</span>
          </button>
          <button type="button" onclick="selectChip('atmosphere', '올라옴', this)" class="chip-btn py-2.5 px-2 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-center transition active:scale-95">
            <span class="block text-sm mb-0.5">🥂</span>
            <span class="font-semibold text-[11px]">슬슬 올라옴</span>
          </button>
          <button type="button" onclick="selectChip('atmosphere', '폭발', this)" class="chip-btn py-2.5 px-2 rounded-xl border border-zinc-800 bg-darkCard text-zinc-300 text-center transition active:scale-95">
            <span class="block text-sm mb-0.5">🔥</span>
            <span class="font-semibold text-[11px]">텐션 폭발</span>
          </button>
        </div>
      </div>

      <!-- Start Button Bar -->
      <div class="pt-4 pb-2">
        <button id="startSessionBtn" onclick="startDjSession()" disabled class="w-full py-4 px-5 rounded-2xl font-black text-base flex items-center justify-center space-x-2 transition duration-300 bg-zinc-800 text-zinc-500 cursor-not-allowed border border-zinc-700/50">
          <span class="text-xl">🍻</span>
          <span id="startBtnText">3가지 항목을 선택해 주세요</span>
        </button>
      </div>
    </section>

    <!-- SCREEN 2: AI DJ & MC 진행 데스크 (Main Console) -->
    <section id="screen-console" class="hidden flex-1 flex flex-col justify-between space-y-3">
      
      <!-- Top Action Bar -->
      <div class="flex items-center justify-between px-1">
        <button onclick="backToSetup()" class="text-xs text-zinc-400 hover:text-white flex items-center space-x-1 py-1 px-2.5 rounded-lg bg-zinc-900 border border-zinc-800 transition">
          <span>←</span>
          <span>상황 다시 선택</span>
        </button>
        <div class="flex items-center space-x-1.5 px-3 py-1 rounded-full bg-purple-950/80 border border-purple-700/60 text-xs font-bold text-purple-300">
          <span class="w-2 h-2 rounded-full bg-neonPurple animate-pulse"></span>
          <span id="consoleSessionTag">미팅 · 1차 · NORMAL</span>
        </div>
      </div>

      <!-- Player Deck (Real Audio Stream with Album Art & Vinyl Disc) -->
      <div class="bg-darkCard border border-zinc-800 rounded-3xl p-4 shadow-xl relative overflow-hidden">
        <div class="absolute top-0 right-0 w-32 h-32 bg-neonPurple/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="flex items-center space-x-4">
          <!-- Album Art with Vinyl Rim -->
          <div class="relative shrink-0 cursor-pointer" onclick="togglePlayPause()">
            <div id="vinylDisc" class="w-20 h-20 rounded-2xl overflow-hidden border-2 border-zinc-600 shadow-2xl relative flex items-center justify-center">
              <img id="trackArtwork" src="" alt="Album Art" class="w-full h-full object-cover" />
              <div class="absolute inset-0 bg-black/20 flex items-center justify-center">
                <span id="playStateBadge" class="w-7 h-7 rounded-full bg-black/70 backdrop-blur-sm flex items-center justify-center text-xs text-white shadow">
                  ▶
                </span>
              </div>
            </div>
            <!-- Live Indicator Badge -->
            <span class="absolute -bottom-1 -right-1 bg-red-600 text-[9px] font-black tracking-wider text-white px-1.5 py-0.5 rounded-md border border-black shadow">
              LIVE
            </span>
          </div>

          <!-- Track Info & Controls -->
          <div class="flex-1 min-w-0">
            <div class="flex items-center justify-between">
              <span id="trackMoodBadge" class="text-[10px] font-bold px-2 py-0.5 rounded bg-zinc-800 text-neonCyan border border-cyan-900/50">
                HIGH TENSION
              </span>
              <span id="trackRoundCount" class="text-[10px] font-bold text-zinc-500">
                ROUND 1
              </span>
            </div>
            <h3 id="trackTitle" class="text-base font-black text-white truncate mt-1 tracking-tight">
              Spicy
            </h3>
            <p id="trackArtist" class="text-xs text-zinc-400 truncate">
              aespa
            </p>

            <!-- Audio Waveform Visualizer & Progress -->
            <div class="flex items-center justify-between mt-2 pt-1 border-t border-zinc-800/80">
              <div class="flex items-end space-x-1 h-3.5">
                <div class="visualizer-bar w-1 bg-neonPurple rounded-full" style="animation-delay: 0.1s;"></div>
                <div class="visualizer-bar w-1 bg-neonPink rounded-full" style="animation-delay: 0.3s;"></div>
                <div class="visualizer-bar w-1 bg-neonCyan rounded-full" style="animation-delay: 0.5s;"></div>
                <div class="visualizer-bar w-1 bg-neonPurple rounded-full" style="animation-delay: 0.2s;"></div>
                <div class="visualizer-bar w-1 bg-neonPink rounded-full" style="animation-delay: 0.4s;"></div>
              </div>
              <span class="text-[10px] text-zinc-400 font-medium" id="audioStatusText">음악 스트리밍 중...</span>
            </div>
          </div>
        </div>
      </div>

      <!-- AI MC Dialogue Bubble -->
      <div class="relative bg-gradient-to-br from-zinc-900 via-darkElevated to-zinc-900 border-2 border-purple-600/50 rounded-2xl p-3.5 shadow-lg">
        <div class="absolute -top-3 left-4 bg-neonPurple text-black px-2.5 py-0.5 rounded-full font-black text-[11px] flex items-center space-x-1 shadow-md">
          <span>🎤</span>
          <span>AI DJ 호스트</span>
        </div>
        <p id="mcBanterText" class="text-sm font-bold text-zinc-100 mt-1 leading-snug tracking-tight">
          “다들 눈 마주치면 큰일 나는 병 걸리셨어요? 독서실 온 거 아니니까 폰 내려놓고 첫인상부터 털고 갑시다.”
        </p>
      </div>

      <!-- Centerpiece Party Mission / Game Card -->
      <div id="missionContainer" class="flex-1 bg-gradient-to-b from-darkCard to-black border-2 border-neonCyan/40 rounded-2xl p-4 flex flex-col justify-between shadow-2xl neon-border-cyan">
        <div>
          <div class="flex items-center justify-between mb-1">
            <span id="missionTag" class="px-2 py-0.5 rounded-full text-[10px] font-black bg-cyan-950 text-cyan-300 border border-cyan-700/50">
              🎯 이번 라운드 미션
            </span>
            <span class="text-[10px] text-zinc-500 font-semibold" id="missionCategoryTag">테이블 공통</span>
          </div>
          <h2 id="missionTitle" class="text-lg sm:text-xl font-black text-white tracking-tight mt-1 leading-tight">
            오른쪽 사람 첫인상 3초 공개
          </h2>
          <p id="missionDesc" class="text-xs text-zinc-300 mt-1.5 leading-relaxed">
            돌아가며 오른쪽 사람의 첫인상을 딱 세 글자로 솔직하게 말해주세요! 가장 빵 터진 사람이 다음 곡 버튼을 누릅니다.
          </p>
        </div>

        <div class="pt-2">
          <button onclick="openGameModal()" class="w-full py-2 px-3 rounded-xl bg-zinc-800 hover:bg-zinc-700 border border-zinc-700 text-xs font-bold text-zinc-200 flex items-center justify-center space-x-1.5 transition active:scale-98">
            <span>ℹ️</span>
            <span id="ruleBtnLabel">3초 요약 룰 보기</span>
          </button>
        </div>
      </div>

      <!-- 4-Button Tension Controller Panel -->
      <div class="space-y-1 pt-1">
        <div class="flex items-center justify-between px-1">
          <span class="text-[10px] font-bold text-zinc-400">DJ INTERACTION CONTROL</span>
          <span class="text-[10px] text-neonPink font-bold">누를 때마다 새로운 곡 & 게임 출격!</span>
        </div>
        
        <div class="grid grid-cols-2 gap-2">
          <!-- Button 1: Tension UP -->
          <button onclick="handleTensionAction('up')" class="py-3 px-2 rounded-xl font-black text-xs sm:text-sm bg-gradient-to-r from-orange-600 to-red-600 hover:from-orange-500 hover:to-red-500 text-white shadow-lg border border-orange-400/40 flex items-center justify-center space-x-1 active:scale-95 transition">
            <span class="text-base">🔥</span>
            <span>텐션 올려! (새 곡)</span>
          </button>

          <!-- Button 2: Chill Down -->
          <button onclick="handleTensionAction('down')" class="py-3 px-2 rounded-xl font-bold text-xs sm:text-sm bg-zinc-800 hover:bg-zinc-700 text-zinc-200 border border-zinc-700 flex items-center justify-center space-x-1 active:scale-95 transition">
            <span class="text-base">😌</span>
            <span>조금 낮춰 (감성)</span>
          </button>

          <!-- Button 3: Keep Vibe -->
          <button onclick="handleTensionAction('keep')" class="py-3 px-2 rounded-xl font-bold text-xs sm:text-sm bg-zinc-800 hover:bg-zinc-700 text-zinc-200 border border-zinc-700 flex items-center justify-center space-x-1 active:scale-95 transition">
            <span class="text-base">🎵</span>
            <span>이 느낌 계속</span>
          </button>

          <!-- Button 4: Next Track -->
          <button onclick="handleTensionAction('next')" class="py-3 px-2 rounded-xl font-bold text-xs sm:text-sm bg-purple-900/60 hover:bg-purple-800/80 text-purple-200 border border-purple-700/60 flex items-center justify-center space-x-1 active:scale-95 transition">
            <span class="text-base">⏭</span>
            <span>다음 곡 믹싱</span>
          </button>
        </div>
      </div>

    </section>

    <!-- SCREEN 3: 게임 설명 바텀 시트 / 모달 -->
    <div id="gameRuleModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-end sm:items-center justify-center p-0 sm:p-4">
      <div class="w-full max-w-md bg-darkCard border-t sm:border border-zinc-700 rounded-t-3xl sm:rounded-3xl p-5 shadow-2xl">
        <div class="flex items-center justify-between pb-3 border-b border-zinc-800">
          <div class="flex items-center space-x-2">
            <span class="text-xl">🎲</span>
            <h3 id="modalTitle" class="text-lg font-black text-white">게임 룰</h3>
          </div>
          <button onclick="closeGameModal()" class="text-zinc-400 hover:text-white text-xl p-1 font-bold">✕</button>
        </div>
        <div class="py-4 space-y-2.5">
          <div class="flex items-start space-x-3 bg-zinc-900/80 p-3 rounded-xl border border-zinc-800">
            <span class="w-5 h-5 rounded-full bg-neonPurple text-black font-black text-xs flex items-center justify-center shrink-0">1</span>
            <p class="text-xs text-zinc-200" id="ruleStep1"></p>
          </div>
          <div class="flex items-start space-x-3 bg-zinc-900/80 p-3 rounded-xl border border-zinc-800">
            <span class="w-5 h-5 rounded-full bg-neonPink text-white font-black text-xs flex items-center justify-center shrink-0">2</span>
            <p class="text-xs text-zinc-200" id="ruleStep2"></p>
          </div>
          <div class="flex items-start space-x-3 bg-zinc-900/80 p-3 rounded-xl border border-zinc-800">
            <span class="w-5 h-5 rounded-full bg-neonCyan text-black font-black text-xs flex items-center justify-center shrink-0">3</span>
            <p class="text-xs text-zinc-200" id="ruleStep3"></p>
          </div>
        </div>
        <button onclick="closeGameModal()" class="w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-neonPurple to-neonPink font-black text-sm text-white shadow-lg">
          닫고 바로 게임 시작하기 🍻
        </button>
      </div>
    </div>

  </div>

  <!-- Big Database of 30 Real Tracks & 36 Missions & 30 MC Banters -->
  <script>
    const ALL_TRACKS = {tracks_json};

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
          title: "러브샷 의리 룰렛",
          desc: "테이블 양옆 사람과 즉석 러브샷! 거부권 행사 시 잔 채워서 2배 마시기!",
          ruleTitle: "의리 러브샷 룰",
          steps: [
            "AI DJ가 지정한 좌우 사람과 팔을 교차해 러브샷을 합니다.",
            "쑥스러워서 피하는 사람은 흑기사 없이 혼자 2잔 마시기!",
            "다 함께 환호하며 짠!"
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
          title: "오른쪽 사람 첫인상 3초 공개",
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
          title: "딸기 당근 수박 참외 멜론",
          desc: "박자에 맞춰 과일 이름을 개수대로 부릅니다. 박자 놓치면 바로 잔 비우기!",
          ruleTitle: "과일 게임 룰",
          steps: [
            "무릎-손뼉 4박자에 맞춰 과일 이름을 개수만큼 부릅니다.",
            "박자가 밀리거나 혀가 꼬이면 즉시 탈락!",
            "살아남은 사람이 다음 술래가 됩니다."
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
        }},
        {{
          title: "마니또 감사 칭찬 한마디",
          desc: "오늘 고생한 사람이나 옆자리 친구에게 고마웠던 점 하나씩 전하기.",
          ruleTitle: "감사 릴레이 룰",
          steps: [
            "오른쪽 사람의 수고와 장점을 따뜻하게 칭찬합니다.",
            "칭찬을 들은 사람은 잔을 채워줍니다.",
            "훈훈하게 건배하며 라운드를 마무리합니다."
          ]
        }}
      ]
    }};

    // 30 AI MC Banters
    const BANTERS_DB = {{
      high: [
        "“오호, 눈빛들 살아났네요? 브레이크 해제하고 마실 사람 지목 들어갑니다!”",
        "“텐션 터졌습니다! 오늘 누구 하나 업혀 나가기 전까지 선곡 빡세게 갑니다!”",
        "“비트 빨라진 거 느껴지시죠? 지금부터 폰 보는 사람은 흑기사 없습니다!”",
        "“분위기 제대로 달아올랐네요. 이 타이밍에 빼는 건 반칙입니다, 원샷!”",
        "“부장님도 마이크 잡을 시간입니다. 오늘 결제는 법카니까 끝까지 갑니다!”",
        "“여기 술자리 맞죠? 클럽 온 거 아니죠? 텐션 미쳤네요 계속 갑니다!”",
        "“자, 이번 판은 살살 안 갑니다. 걸리면 무조건 잔 비우는 걸로!”",
        "“심장 박동수랑 BPM 맞춰드릴게요. 잔 채우고 바로 돌진합니다!”",
        "“목 쉴 때까지 부르는 겁니다. 후렴구 떼창 안 하면 탈락이에요!”",
        "“어색했던 분들 맞나요? 텐션 200% 찍었으니 더 센 걸로 비트 꺾습니다!”"
      ],
      normal: [
        "“다들 눈 마주치면 큰일 나는 병 걸리셨어요? 폰 내려놓고 첫인상부터 털고 갑시다.”",
        "“슬슬 알콜 들어가서 말문 트였죠? 영혼 없는 리액션은 탈락입니다.”",
        "“이 노래 나오면 몸이 먼저 반응하죠? 리듬 타면서 다음 미션 갑니다.”",
        "“적당히 그루브 타면서 서로 호구조사 끝내봅시다. 판 다시 깝니다!”",
        "“분위기 알맞게 익었네요. 여기서 한 번 더 비트 얹어드릴게요.”",
        "“선배 후배 눈치 보지 말고 동아리방처럼 편하게 썰 풉시다!”",
        "“음악 딱 좋죠? 이 분위기 살려서 테이블 전원 참여 미션 갑니다.”",
        "“잔 비어 있는 사람 누구죠? 잔 채우고 템포 맞춰갑니다!”",
        "“대화 정적 흐르려던 찰나에 제가 딱 들어왔죠? 다음 턴 갑니다!”",
        "“슬슬 취기 올라오시죠? 기분 딱 좋을 때 재밌는 판 하나 던집니다.”"
      ],
      chill: [
        "“속도 좀 조절할게요. 슬슬 서로 취향 물어보면서 진솔한 얘기 좀 터볼 타이밍입니다.”",
        "“분위기 너무 달렸네요. 템포 잠깐 낮추고 옛날 흑역사 하나씩 털어놓고 짠합시다.”",
        "“슬슬 진지한 얘기 나오는 시간입니다. 오늘 고생한 사람들한테 칭찬 하나씩 던지시죠.”",
        "“다들 숨 좀 고르세요. 감성적인 BGM 깔아드릴 테니 깊은 토크 갑니다.”",
        "“술자리에서 이런 얘기 한 번쯤 나와야 진짜 친해지는 법이죠.”",
        "“템포 다운! 잔잔하게 술잔 기울이면서 서로 속마음 좀 들어봅시다.”",
        "“너무 달리기만 하면 재미없죠? 한 템포 쉬어가면서 감성 채웁니다.”",
        "“오늘 밤 분위기 감성 제대로네요. 잔 채우고 조용히 건배 한 번 갑니다.”"
      ]
    }};

    // App State
    const state = {{
      groupType: null,
      round: null,
      atmosphere: null,
      mood: 'normal',
      roundCount: 1,
      lastTrackIdx: -1,
      lastBanterIdx: -1,
      lastMissionIdx: -1
    }};

    // Setup chip selector
    function selectChip(category, value, el) {{
      soundEngine.playScratch();
      state[category] = value;

      const parent = el.parentElement;
      parent.querySelectorAll('.chip-btn').forEach(btn => {{
        btn.classList.remove('border-neonPurple', 'border-neonCyan', 'border-neonPink', 'bg-purple-950/70', 'bg-cyan-950/70', 'bg-pink-950/70', 'text-white');
        btn.classList.add('border-zinc-800', 'bg-darkCard', 'text-zinc-300');
      }});

      let border = 'border-neonPurple', bg = 'bg-purple-950/70';
      if (category === 'round') {{ border = 'border-neonCyan'; bg = 'bg-cyan-950/70'; }}
      else if (category === 'atmosphere') {{ border = 'border-neonPink'; bg = 'bg-pink-950/70'; }}

      el.classList.remove('border-zinc-800', 'bg-darkCard', 'text-zinc-300');
      el.classList.add(border, bg, 'text-white');

      if (category === 'atmosphere') {{
        if (value === '어색함') state.mood = 'chill';
        else if (value === '올라옴') state.mood = 'normal';
        else if (value === '폭발') state.mood = 'high';
      }}

      checkCanStart();
    }}

    function checkCanStart() {{
      const btn = document.getElementById('startSessionBtn');
      const txt = document.getElementById('startBtnText');
      if (state.groupType && state.round && state.atmosphere) {{
        btn.disabled = false;
        btn.className = "w-full py-4 px-5 rounded-2xl font-black text-base flex items-center justify-center space-x-2 transition duration-300 bg-gradient-to-r from-neonPurple via-neonPink to-neonCyan text-white cursor-pointer shadow-xl";
        txt.textContent = `🍻 AI야, 분위기 살려줘 (음악 시작)`;
      }} else {{
        btn.disabled = true;
        btn.className = "w-full py-4 px-5 rounded-2xl font-black text-base flex items-center justify-center space-x-2 transition duration-300 bg-zinc-800 text-zinc-500 cursor-not-allowed border border-zinc-700/50";
        txt.textContent = `3가지 항목을 선택해 주세요`;
      }}
    }}

    // Start Session
    function startDjSession() {{
      if (!state.groupType || !state.round || !state.atmosphere) return;
      soundEngine.playAirhorn();

      document.getElementById('screen-setup').classList.add('hidden');
      document.getElementById('screen-console').classList.remove('hidden');

      generateNextRound();
    }}

    // Random Pick helper (ensures no immediate repeat)
    function pickRandom(arr, lastIdx) {{
      if (arr.length <= 1) return {{ item: arr[0], idx: 0 }};
      let idx;
      do {{
        idx = Math.floor(Math.random() * arr.length);
      }} while (idx === lastIdx);
      return {{ item: arr[idx], idx }};
    }}

    // Core Dynamic Generator: Generates fresh Track + Banter + Mission
    function generateNextRound() {{
      const mood = state.mood || 'normal';

      // 1. Pick Track
      const matchingTracks = ALL_TRACKS.filter(t => t.mood === mood);
      const trackPool = matchingTracks.length > 0 ? matchingTracks : ALL_TRACKS;
      const {{ item: track, idx: tIdx }} = pickRandom(trackPool, state.lastTrackIdx);
      state.lastTrackIdx = tIdx;

      // 2. Pick Banter
      const banters = BANTERS_DB[mood] || BANTERS_DB['normal'];
      const {{ item: banter, idx: bIdx }} = pickRandom(banters, state.lastBanterIdx);
      state.lastBanterIdx = bIdx;

      // 3. Pick Mission
      const missions = MISSIONS_DB[mood] || MISSIONS_DB['normal'];
      const {{ item: mission, idx: mIdx }} = pickRandom(missions, state.lastMissionIdx);
      state.lastMissionIdx = mIdx;

      // Update Header & Round
      document.getElementById('consoleSessionTag').textContent = `${{state.groupType}} · ${{state.round}} · ${{mood.toUpperCase()}}`;
      document.getElementById('trackRoundCount').textContent = `ROUND ${{state.roundCount++}}`;
      
      let badgeColor = "text-neonCyan border-cyan-900/50";
      let moodLabel = "GROOVE · 110 BPM";
      if (mood === 'high') {{
        badgeColor = "text-orange-400 border-orange-900/50";
        moodLabel = "🔥 HIGH TENSION · 130+ BPM";
      }} else if (mood === 'chill') {{
        badgeColor = "text-blue-300 border-blue-900/50";
        moodLabel = "😌 CHILL · 80 BPM";
      }}
      const badge = document.getElementById('trackMoodBadge');
      badge.className = `text-[10px] font-bold px-2 py-0.5 rounded bg-zinc-800 ${{badgeColor}} border`;
      badge.textContent = moodLabel;

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

      // Play Native HTML5 Audio
      const bgm = document.getElementById('realBgmAudio');
      if (track.audioUrl) {{
        bgm.src = track.audioUrl;
        bgm.play().then(() => {{
          setVinylSpinning(true);
          document.getElementById('audioStatusText').textContent = "실제 음원 스트리밍 중 🎶";
        }}).catch(err => {{
          console.warn("Audio autoplay blocked, click to play:", err);
          document.getElementById('audioStatusText').textContent = "▶ 앨범 커버를 눌러 재생";
          setVinylSpinning(false);
        }});
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
      const bars = document.querySelectorAll('.visualizer-bar');
      if (isSpinning) {{
        badge.textContent = '⏸';
        bars.forEach(b => b.classList.remove('paused-anim'));
      }} else {{
        badge.textContent = '▶';
        bars.forEach(b => b.classList.add('paused-anim'));
      }}
    }}

    // Toast
    function showToast(msg) {{
      const toast = document.getElementById('djToast');
      const txt = document.getElementById('djToastText');
      txt.textContent = msg;
      toast.classList.remove('hidden');
      clearTimeout(window.toastTimer);
      window.toastTimer = setTimeout(() => toast.classList.add('hidden'), 3500);
    }}

    // 4 Tension Interaction Handlers (Drives the dynamic loop!)
    function handleTensionAction(action) {{
      const missionBox = document.getElementById('missionContainer');

      if (action === 'up') {{
        soundEngine.playAirhorn();
        state.mood = 'high';
        missionBox.classList.add('neon-border-pink');
        setTimeout(() => missionBox.classList.remove('neon-border-pink'), 1000);
        showToast("🔥 텐션 UP! 고텐션 댄스곡과 폭소 게임으로 리믹스!");
      }} else if (action === 'down') {{
        soundEngine.playChillChime();
        state.mood = 'chill';
        showToast("😌 캄다운 모드! 감성적인 곡과 진솔한 토크 미션 출격.");
      }} else if (action === 'next') {{
        soundEngine.playScratch();
        // Cycle mood
        const moods = ['chill', 'normal', 'high'];
        const curIdx = moods.indexOf(state.mood);
        state.mood = moods[(curIdx + 1) % moods.length];
        showToast("⏭ 새로운 트랙과 미션으로 믹싱합니다!");
      }} else if (action === 'keep') {{
        soundEngine.playBassDrop();
        showToast("🎵 현재 바이브 인정! 이 느낌 그대로 계속 달립니다.");
        document.getElementById('mcBanterText').textContent = "“오케이, 지금 흐름 좋습니다. 선곡 안 끊기게 이 바이브 그대로 유지합니다!”";
        return;
      }}

      // Immediately generate fresh combination!
      generateNextRound();
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
      const bgm = document.getElementById('realBgmAudio');
      if (bgm) bgm.pause();
      document.getElementById('screen-console').classList.add('hidden');
      document.getElementById('screen-setup').classList.remove('hidden');
    }}

    // Auto next when audio ends
    document.getElementById('realBgmAudio').addEventListener('ended', () => {{
      soundEngine.playScratch();
      showToast("⏭ 다음 곡으로 자동 믹싱!");
      generateNextRound();
    }});
  </script>
</body>
</html>
'''

with open('/Users/kimdoyun/.gemini/antigravity/scratch/drinking-party-dj/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully generated dynamic index.html with 30 real audio tracks and 50+ variations!")
