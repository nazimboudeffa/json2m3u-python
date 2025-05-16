import os
import json

def generate_m3u_from_json(json_path, output_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        channels = json.load(f)
    m3u_lines = ["#EXTM3U"]
    for channel in channels:
        name = channel.get("name", "Unknown")
        group = channel.get("group", "")
        logo = channel.get("logo", "")
        # Use all stream URLs for each channel
        for url in channel.get("stream_urls", []):
            extinf = f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}'
            m3u_lines.append(extinf)
            m3u_lines.append(url)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(m3u_lines))
    print(f"M3U file generated: {output_path}")

def main():
    base_dir = os.path.dirname(__file__)
    channel_lists_dir = os.path.join(base_dir, 'channel-lists')
    output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(channel_lists_dir):
        if filename.endswith('.json'):
            country_code = os.path.splitext(filename)[0]
            json_path = os.path.join(channel_lists_dir, filename)
            output_path = os.path.join(output_dir, f"{country_code}.m3u")
            generate_m3u_from_json(json_path, output_path)

if __name__ == "__main__":
    main()