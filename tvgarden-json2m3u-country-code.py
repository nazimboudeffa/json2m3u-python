import os
import json
from collections import defaultdict

def collect_channels_by_country(channel_lists_dir):
    country_channels = defaultdict(list)
    for filename in os.listdir(channel_lists_dir):
        if filename.endswith('.json'):
            json_path = os.path.join(channel_lists_dir, filename)
            with open(json_path, 'r', encoding='utf-8') as f:
                channels = json.load(f)
                for channel in channels:
                    country = channel.get("country", "XX").upper()
                    country_channels[country].append(channel)
    return country_channels

def generate_m3u_for_country(country, channels, output_dir):
    m3u_lines = ["#EXTM3U"]
    for channel in channels:
        name = channel.get("name", "Unknown")
        group = channel.get("group", "")
        logo = channel.get("logo", "")
        for url in channel.get("stream_urls", []):
            extinf = f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}'
            m3u_lines.append(extinf)
            m3u_lines.append(url)
    output_path = os.path.join(output_dir, f"{country}.m3u")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(m3u_lines))
    print(f"M3U file generated: {output_path}")

def main():
    base_dir = os.path.dirname(__file__)
    channel_lists_dir = os.path.join(base_dir, 'channel-lists')
    output_dir = os.path.join(base_dir, 'output-country-code')
    os.makedirs(output_dir, exist_ok=True)
    country_channels = collect_channels_by_country(channel_lists_dir)
    for country, channels in country_channels.items():
        generate_m3u_for_country(country, channels, output_dir)

if __name__ == "__main__":
    main()