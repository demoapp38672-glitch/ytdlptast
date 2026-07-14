<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protected Player</title>

    <style>
        /* Reset */
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
            background: black;
            overflow: hidden;
        }

        /* Player Container */
        .video-container {
            position: relative;
            width: 100%;
            height: 100%;
        }

        /* ========== 🔥 TOP LEFT BLOCK (Title & Logo) ========== */
        .block-top-left {
            position: absolute;
            top: 0;
            left: 0;
            width: calc(100% - 130px);
            height: 85px;
            z-index: 20;
            background: black;
            pointer-events: none;
        }

        /* ========== 🔥 BOTTOM BLOCK (YouTube Logo) ========== */
        .block-bottom {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50px;
            z-index: 20;
            background: black;
            pointer-events: none;
        }

        /* ========== 🔥 CENTER BOTTOM BLOCK (More options) ========== */
        .block-center {
            position: absolute;
            bottom: 80px;
            left: 50%;
            transform: translateX(-50%);
            width: 220px;
            height: 80px;
            z-index: 50;
            background: transparent;
            pointer-events: none;
        }

        /* Iframe */
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        /* ========== EXTRA: Loading Text ========== */
        .loading {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #666;
            font-family: Arial, sans-serif;
            font-size: 18px;
            z-index: 1;
        }
    </style>
</head>

<body>

    <!-- Loading -->
    <div class="loading">⏳ Loading video...</div>

    <div class="video-container">

        <!-- ========== 🔥 OVERLAY BLOCKS ========== -->
        <div class="block-top-left"></div>
        <div class="block-bottom"></div>
        <div class="block-center"></div>

        <!-- ========== 🔥 YOUTUBE PLAYER ========== -->
        <iframe id="player"
            src=""
            allow="autoplay; encrypted-media; picture-in-picture"
            allowfullscreen>
        </iframe>

    </div>

    <script>
        // ========== GET VIDEO ID FROM URL ==========
        // URL: ?id=VIDEO_ID (જેમ PHP માં હતું)
        const urlParams = new URLSearchParams(window.location.search);
        const videoId = urlParams.get('id') || 'qAzl41z3zgY'; // Default video

        // ========== BUILD EMBED URL ==========
        // તમારા PHP કોડની બધી સુવિધાઓ જાળવી રાખી છે
        const embedUrl =
            `https://www.youtube.com/embed/${videoId}?` +
            `autoplay=1` +
            `&playsinline=1` +
            `&fs=0` + // Fullscreen disabled (તમે ઇચ્છો તો 1 કરો)
            `&rel=0` +
            `&modestbranding=1` +
            `&controls=1` +
            `&disablekb=1` + // Keyboard shortcuts disabled
            `&showinfo=0` + // Title hidden
            `&iv_load_policy=3`; // No annotations

        // ========== LOAD IFRAME ==========
        const iframe = document.getElementById('player');
        iframe.src = embedUrl;

        // ========== HIDE LOADING TEXT ==========
        iframe.addEventListener('load', function() {
            document.querySelector('.loading').style.display = 'none';
        });

        // Fallback: 5 સેકન્ડ પછી loading hide કરો
        setTimeout(function() {
            document.querySelector('.loading').style.display = 'none';
        }, 5000);

        // ========== EXTRA SECURITY ==========
        // 1. Right Click Block
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
            return false;
        });

        // 2. Keyboard Shortcuts Block
        document.addEventListener('keydown', function(e) {
            // F12 (Dev Tools)
            if (e.key === 'F12') {
                e.preventDefault();
                return false;
            }
            // Ctrl+U (View Source)
            if (e.ctrlKey && (e.key === 'u' || e.key === 'U')) {
                e.preventDefault();
                return false;
            }
            // Ctrl+S (Save)
            if (e.ctrlKey && (e.key === 's' || e.key === 'S')) {
                e.preventDefault();
                return false;
            }
            // Ctrl+C (Copy) - વૈકલ્પિક
            if (e.ctrlKey && (e.key === 'c' || e.key === 'C')) {
                e.preventDefault();
                return false;
            }
        });

        console.log('🔒 Protected Player Loaded');
        console.log('📹 Video ID:', videoId);
    </script>
</body>
</html>
