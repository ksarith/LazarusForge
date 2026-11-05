#!/usr/bin/env python3
"""Build a duplicate-free Astroid Miner V0.02 archive from V0.01."""
import hashlib, json, zipfile
from pathlib import Path
SOURCE_ZIP="Astroid-miner-AstroidMinerV0.01.zip"
TARGET_ZIP="Astroid-miner-AstroidMinerV0.02.zip"
ROOT="Astroid-miner-AstroidMinerV0.02/"

def build():
    contents={}
    with zipfile.ZipFile(SOURCE_ZIP) as src:
        for info in src.infolist():
            if info.is_dir(): continue
            parts=info.filename.split("/",1)
            rel=parts[1] if len(parts)==2 else parts[0]
            contents[ROOT+rel]=src.read(info.filename)
    with zipfile.ZipFile(TARGET_ZIP,"w",zipfile.ZIP_DEFLATED) as out:
        for name,data in sorted(contents.items()): out.writestr(name,data)
    with zipfile.ZipFile(TARGET_ZIP) as check:
        if check.testzip() is not None: raise RuntimeError("ZIP integrity failure")
        names=check.namelist()
        if len(names)!=len(set(names)): raise RuntimeError("Duplicate ZIP members")
        manifest={n:{"size_bytes":len(check.read(n)),"sha256":hashlib.sha256(check.read(n)).hexdigest()} for n in names}
    Path("build_manifest_v0.02.json").write_text(json.dumps(manifest,indent=2))
if __name__=="__main__": build()
