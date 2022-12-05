import pprint
import re
from pathlib import Path

readmes = filter(lambda x: x.name == "README.md", Path("playbook", "roles").glob("*/*"))

keys = []
for readme in readmes:
    lines = readme.read_text().split("\n")
    for line in lines:
        if re.match(r"\|MASTODON_.*_KEY\|", line):
            if line not in keys:
                keys.append(line)

keys.sort(key=lambda x: x.split("|")[3])

text = """All API keys required for this playbook:

|Secret name|scope|
|---|---|
"""

text += "\n".join(keys)
text += "\n"

Path("playbook", "API-KEYS.md").write_text(text)
