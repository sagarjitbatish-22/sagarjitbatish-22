import re
from datetime import datetime, timezone

now = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")

with open("README.md", "r", encoding="utf-8") as f:
    text = f.read()

new_text = re.sub(
    r"<!-- UPDATED-START -->.*?<!-- UPDATED-END -->",
    f"<!-- UPDATED-START -->\n{now}\n<!-- UPDATED-END -->",
    text,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_text)
