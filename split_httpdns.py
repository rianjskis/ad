import json
from pathlib import Path
from copy import deepcopy

# 输入文件
infile = Path("httpdns.json")
out_domain = Path("httpdns-domain.json")
out_ip = Path("httpdns-ip.json")

data = json.loads(infile.read_text(encoding='utf-8'))
rules_key = "rules" if "rules" in data else ("rule" if "rule" in data else None)

if rules_key:
    rules = data[rules_key]
    top = {k: v for k, v in data.items() if k != rules_key}
elif isinstance(data, list):
    rules = data
    top = {}
else:
    rules = [data]
    top = {}

domain_fields = {"domain", "domain_suffix", "domain_keyword", "domain_regex", "domain_prefix"}
ip_fields = {"ip_cidr", "ip_is_private", "ip_range"}

domain_rules = []
ip_rules = []

for rule in rules:
    dom_part = {k: deepcopy(v) for k, v in rule.items() if k in domain_fields}
    ip_part = {k: deepcopy(v) for k, v in rule.items() if k in ip_fields}
    other_part = {k: deepcopy(v) for k, v in rule.items() if k not in domain_fields | ip_fields}

    if dom_part:
        dom_rule = deepcopy(other_part)
        dom_rule.update(dom_part)
        domain_rules.append(dom_rule)

    if ip_part:
        ip_rule = deepcopy(other_part)
        ip_rule.update(ip_part)
        ip_rules.append(ip_rule)

def build_out(top, rules_key_name, rules_list):
    if rules_key_name:
        out = dict(top)
        out[rules_key_name] = rules_list
        return out
    else:
        return rules_list

out_domain_data = build_out(top, rules_key, domain_rules)
out_ip_data = build_out(top, rules_key, ip_rules)

out_domain.write_text(json.dumps(out_domain_data, ensure_ascii=False, indent=2), encoding='utf-8')
out_ip.write_text(json.dumps(out_ip_data, ensure_ascii=False, indent=2), encoding='utf-8')

print(f"拆分完成 ✅")
print(f"域名规则数量: {len(domain_rules)}")
print(f"IP 规则数量: {len(ip_rules)}")
