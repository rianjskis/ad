import sys

inp = sys.argv[1]
out = sys.argv[2]

with open(inp, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(out, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")

    for line in lines:
        line = line.strip()
        if not line or "," not in line:
            continue

        name, url = line.split(",", 1)

        name = name.strip()
        url = url.strip()

        # 简单清洗：避免 ? 或空 URL
        if not url.startswith("http"):
            continue

        f.write(f"#EXTINF:-1,{name}\n")
        f.write(f"{url}\n")
