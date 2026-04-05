#!/usr/bin/env bash
set -e

mkdir -p data

echo "== 下载规则 =="
curl -L -o data/adg1.txt https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt
curl -L -o data/adg2.txt https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_15_DnsFilter/filter.txt

echo "== 提取域名规则 =="

cat data/adg*.txt \
| sed 's/\r//' \
| grep -v '^!' \
| grep -v '^@@' \
| grep -v '/' \
| grep -v '\$' \
| sed 's/||//' \
| sed 's/\^.*//' \
| sed 's/^\.//' \
| sed 's/^|http[s]*:\/\///' \
| sed '/^$/d' \
| sort -u > data/domains.txt

echo "域名数量："
wc -l data/domains.txt

echo "== 生成 sing-box JSON =="

echo '{ "version": 1, "rules": [ { "domain_suffix": [' > data/rule.json

awk '{print "\"" $0 "\","}' data/domains.txt >> data/rule.json

sed -i '$ s/,$//' data/rule.json

echo '] } ] }' >> data/rule.json

echo "== 完成 JSON 生成 =="