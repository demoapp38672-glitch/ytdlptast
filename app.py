from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''
    <h2>YouTube Link Extractor API</h2>
    <p>Use: /get-links?url=YOUTUBE_URL</p>
    <p>Example: /get-links?url=https://www.youtube.com/watch?v=VIDEO_ID</p>
    '''

@app.route('/get-links', methods=['GET'])
def get_links():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Please provide ?url=YOUR_YOUTUBE_URL"}), 400
    
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # ફક્ત MP4 અને m3u8 લિંક્સ ફિલ્ટર કરો
            mp4_links = []
            m3u8_links = []
            
            for f in info.get('formats', []):
                ext = f.get('ext')
                protocol = str(f.get('protocol', ''))
                
                # MP4 ફોર્મેટ
                if ext == 'mp4' and f.get('url'):
                    mp4_links.append({
                        'format_id': f.get('format_id'),
                        'resolution': f.get('resolution') or f.get('format_note') or 'Unknown',
                        'url': f.get('url'),
                        'filesize': f.get('filesize')
                    })
                
                # m3u8 ફોર્મેટ
                if 'm3u8' in protocol.lower() and f.get('url'):
                    m3u8_links.append({
                        'format_id': f.get('format_id'),
                        'resolution': f.get('resolution') or f.get('format_note') or 'Unknown',
                        'url': f.get('url'),
                        'protocol': protocol
                    })
            
            # શ્રેષ્ઠ MP4 લિંક (સૌથી વધુ રિઝોલ્યુશન)
            best_mp4 = None
            if mp4_links:
                # resolution મુજબ સૉર્ટ કરો
                best_mp4 = max(mp4_links, key=lambda x: x.get('resolution', '0x0'))
            
            # શ્રેષ્ઠ m3u8 લિંક
            best_m3u8 = None
            if m3u8_links:
                best_m3u8 = m3u8_links[0]  # પહેલી લિંક
            
            return jsonify({
                "success": True,
                "best_mp4": best_mp4,      # સૌથી સારી MP4 લિંક
                "best_m3u8": best_m3u8,    # m3u8 લિંક
                "all_mp4": mp4_links,      # બધી MP4 લિંક્સ
                "all_m3u8": m3u8_links    # બધી m3u8 લિંક્સ
            })
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
