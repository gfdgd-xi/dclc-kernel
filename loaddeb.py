#!/usr/bin/env python3
import os
import sys
programPath = os.path.split(os.path.realpath(__file__))[0] 
os.system(f"bash '{programPath}/incremental-updating-packages.sh' '{programPath}'")
os.system("apt-ftparchive release . > Release")
os.system("rm Release.gpg")
os.system("rm InRelease")
os.system("rm gpg.asc")
os.system("gpg --armor --detach-sign -o Release.gpg Release")
os.system("gpg --clearsign -o InRelease Release")
os.system("gpg --armor --output gpg.asc --export 3025613752@qq.com")