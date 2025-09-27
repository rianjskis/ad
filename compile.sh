#!/usr/bin/env bash
set -e

# 源 JSON 路径
SRC_JSON="Filters/AWAvenue-Ads-Rule-Singbox.json"
# 输出 .srs 路径
OUT_SRS="Filters/AWAvenue-Ads-Rule-Singbox.srs"

# 指定 sing-box 版本（可按需改）
SBOX_VER="1.13.0"
# 根据 Linux x86_64 可执行文件名（根据你需要的架构改）
BIN_NAME="sing-box-linux-amd64"
DOWNLOAD_URL="https://github.com/SagerNet/sing-box/releases/download/v${SBOX_VER}/${BIN_NAME}"

# 如果没有 sing-box 可执行文件，就下载
if [ ! -f "./sing-box" ]; then
  echo "Downloading sing-box version ${SBOX_VER} ..."
  curl -L -o sing-box "$DOWNLOAD_URL"
  chmod +x sing-box
fi

# 编译命令： JSON → .srs
./sing-box rule-set compile --output "$OUT_SRS" "$SRC_JSON"

echo "Compiled: $SRC_JSON → $OUT_SRS"
