import json

def json_to_m3u(json_path, m3u_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        channels = json.load(f)

    with open(m3u_path, 'w', encoding='utf-8') as m3u:
        m3u.write("#EXTM3U\n")
        for channel in channels:
            name = channel.get("channel", "Unknown")
            url = channel.get("link")
            tvg_id = channel.get("id", "")
            country = channel.get("country", "")
            if url:
                m3u.write(
                    f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{name}" tvg-country="{country}" tvg-logo="" group-title="{country}",{name}\n{url}\n'
                )

def main():
    json_file = "algeria.json"  # At the root of the project
    m3u_file = "algeria.m3u"
    json_to_m3u(json_file, m3u_file)
    print(f"Converted {json_file} to {m3u_file}")

if __name__ == "__main__":
    main()