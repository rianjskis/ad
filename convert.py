import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(output_file, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")

    for line in lines:
        line = line.strip()
        if not line or "," not in line:
            continue

        name, url = line.split(",", 1)

        name = name.strip()
        url = url.strip()

        f.write(f"#EXTINF:-1,{name}\n")
        f.write(f"{url}\n")
