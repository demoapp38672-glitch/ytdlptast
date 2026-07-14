import yt_dlp

ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'extractor_args': {
        'youtubepot-bgutilhttp': {
            'base_url': 'http://bgutil-provider:4416'  # Railway internal service name
        }
    }
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    # ... બાકીનો કોડ ...
from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'YouTube Link Extractor. Use /get-links?url=YOUTUBE_URL'

@app.route('/get-links')
def get_links():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "url parameter required"}), 400
    
    try:
        ydl_opts = {'quiet': True, 'no_warnings': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            mp4_links = []
            m3u8_links = []
            
            for f in info.get('formats', []):
                if f.get('ext') == 'mp4' and f.get('url'):
                    mp4_links.append({
                        'format_id': f.get('format_id'),
                        'resolution': f.get('resolution') or f.get('format_note', 'Unknown'),
                        'url': f.get('url')
                    })
                
                if 'm3u8' in str(f.get('protocol', '')).lower() and f.get('url'):
                    m3u8_links.append({
                        'format_id': f.get('format_id'),
                        'resolution': f.get('resolution') or f.get('format_note', 'Unknown'),
                        'url': f.get('url')
                    })
            
            return jsonify({
                "success": True,
                "mp4": mp4_links,
                "m3u8": m3u8_links
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
