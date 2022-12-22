import re
from pathlib import Path

readmes = filter(lambda x: x.name == "README.md", Path("playbook", "roles").glob("*/*"))

tokens = []
for readme in readmes:
    lines = readme.read_text().split("\n")
    for line in lines:
        if re.match(r"\|MASTODON_.*_TOKEN\|", line):
            if line not in tokens:
                tokens.append(line)

tokens.sort(key=lambda x: x.split("|")[3])

text = """All API tokens required for this playbook:

|Secret name|scope|
|---|---|
"""

text += "\n".join(tokens)
text += "\n"

Path("playbook", "API-TOKENS.md").write_text(text)
