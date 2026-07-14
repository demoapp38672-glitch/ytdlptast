from flask import Flask, request, jsonify
import yt_dlp
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return '''
    <h2>YouTube Link Extractor API</h2>
    <p>Use: /get-links?url=YOUTUBE_URL</p>
    <p>Example: /get-links?url=https://www.youtube.com/watch?v=VIDEO_ID</p>
    '''

@app.route('/get-links')
def get_links():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "url parameter required"}), 400
    
    try:
        # 🔥 યોગ્ય ઓપ્શન્સ - cookies + ફોર્મેટ ફિક્સ
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'cookiefile': 'cookies.txt',  # cookies ફાઇલ
            'extract_flat': False,        # બધી ડિટેલ મેળવો
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # MP4 પ્રાધાન્ય
            'merge_output_format': 'mp4',  # મર્જ કરીને MP4 બનાવો
        }
        
        # જો cookies.txt ન હોય તો એરર ન આવે તે માટે
        if not os.path.exists('cookies.txt'):
            app.logger.warning("cookies.txt not found, trying without cookies")
            del ydl_opts['cookiefile']
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # 🔍 બધા ફોર્મેટ્સની લિસ્ટ
            all_formats = []
            for f in info.get('formats', []):
                format_data = {
                    'format_id': f.get('format_id'),
                    'ext': f.get('ext'),
                    'resolution': f.get('resolution') or f.get('format_note', 'Unknown'),
                    'vcodec': f.get('vcodec'),
                    'acodec': f.get('acodec'),
                    'url': f.get('url'),
                    'protocol': f.get('protocol'),
                    'filesize': f.get('filesize'),
                }
                all_formats.append(format_data)
            
            # 🎯 MP4 અને m3u8 ફિલ્ટર કરો
            mp4_links = [f for f in all_formats if f['ext'] == 'mp4' and f.get('url')]
            m3u8_links = [f for f in all_formats if 'm3u8' in str(f.get('protocol', '')).lower() and f.get('url')]
            
            # 🏆 શ્રેષ્ઠ MP4 શોધો
            best_mp4 = None
            if mp4_links:
                # resolution અને filesize બંને જુઓ
                best_mp4 = max(mp4_links, key=lambda x: (
                    int(x.get('resolution', '0x0').split('x')[0]) if 'x' in x.get('resolution', '0x0') else 0,
                    x.get('filesize', 0) or 0
                ))
            
            return jsonify({
                "success": True,
                "video_title": info.get('title'),
                "total_formats": len(all_formats),
                "best_mp4": best_mp4,
                "mp4_links": mp4_links[:5],  # ફક્ત ટોચના 5
                "m3u8_links": m3u8_links[:5], # ફક્ત ટોચના 5
                "all_formats_count": len(all_formats)
            })
            
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
