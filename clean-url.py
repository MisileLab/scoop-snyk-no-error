from json import loads, dumps
from pathlib import Path

data: dict[str, str] = loads(Path("snyk.json").read_text())
data["url"] = data["url"].removesuffix("?utm_source=SCOOP#/snyk-win.exe")
_ = Path("snyk.json").write_text(dumps(data, indent=4))

