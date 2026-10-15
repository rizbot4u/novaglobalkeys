#!/usr/bin/env python3
"""
Update the footer to include LinkedIn, GitHub, X, and Email.
Keeps the existing Base link.
"""

import re
import shutil
import time
from pathlib import Path

HTML = Path.home() / "novaglobalkeys" / "index.html"
BACKUP = HTML.with_suffix(f".html.bak.footer-{int(time.time())}")

NEW_FOOTER = '''    <!-- FOOTER -->
    <footer class="border-t border-slate-800/80 bg-slate-950 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row items-center justify-between gap-8">

                <div class="text-center md:text-left">
                    <div class="flex items-center justify-center md:justify-start space-x-3 mb-2">
                        <div class="w-6 h-6 rounded-lg bg-gradient-to-tr from-brand-accent to-brand-cyan flex items-center justify-center text-black font-bold text-xs">
                            N
                        </div>
                        <span class="font-bold text-base text-white">NOVA GLOBAL KEYS</span>
                    </div>
                    <p class="text-xs text-slate-500">
                        © 2026 Nova Global Keys. Built for Base Mainnet. Bybit Institutional Broker Kr000820.
                    </p>
                    <p class="text-xs text-slate-500 mt-1">
                        Contact: <a href="mailto:internationaltajars@gmail.com" class="text-brand-accent hover:underline">internationaltajars@gmail.com</a>
                    </p>
                </div>

                <div class="flex items-center space-x-6 text-slate-400 text-sm">
                    <a href="https://github.com/rizbot4u" target="_blank" rel="noopener" class="hover:text-brand-accent transition-colors" title="GitHub">
                        <i class="fa-brands fa-github text-lg"></i>
                    </a>
                    <a href="https://linkedin.com/in/rizwan-ali-974073377" target="_blank" rel="noopener" class="hover:text-brand-accent transition-colors" title="LinkedIn">
                        <i class="fa-brands fa-linkedin text-lg"></i>
                    </a>
                    <a href="https://x.com/novaglobalkeys" target="_blank" rel="noopener" class="hover:text-brand-accent transition-colors" title="X (Twitter)">
                        <i class="fa-brands fa-x-twitter text-lg"></i>
                    </a>
                    <a href="mailto:internationaltajars@gmail.com" class="hover:text-brand-accent transition-colors" title="Email">
                        <i class="fa-solid fa-envelope text-lg"></i>
                    </a>
                    <a href="https://base.org" target="_blank" rel="noopener" class="hover:text-brand-cyan transition-colors" title="Base">
                        <i class="fa-solid fa-cube text-lg"></i>
                    </a>
                </div>

            </div>
        </div>
    </footer>'''


def main():
    if not HTML.exists():
        print(f"❌ Not found: {HTML}")
        return

    src = HTML.read_text(encoding="utf-8")
    shutil.copy2(HTML, BACKUP)
    print(f"✅ Backup: {BACKUP.name}")

    # Find the existing footer and replace it
    pattern = re.compile(r'<!--\s*FOOTER\s*-->.*?</footer>', re.DOTALL)
    match = pattern.search(src)

    if not match:
        print("❌ Could not find footer. Paste this: grep -n 'footer' index.html")
        return

    src = src[:match.start()] + NEW_FOOTER + src[match.end():]
    HTML.write_text(src, encoding="utf-8")
    print("✅ Footer replaced")

    # Verify
    print("")
    print("=== Verification ===")
    for needle, label in [
        ("fa-linkedin", "LinkedIn icon"),
        ("fa-x-twitter", "X icon"),
        ("fa-envelope", "Email icon"),
        ("internationaltajars@gmail.com", "Email address"),
        ("linkedin.com/in/rizwan-ali-974073377", "LinkedIn URL"),
        ("x.com/novaglobalkeys", "X URL"),
    ]:
        count = src.count(needle)
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {label}: {count}")

    print("")
    print("Next:")
    print("  cd ~/novaglobalkeys")
    print("  git add . && git commit -m 'Add full contact footer: LinkedIn, X, email' && git push")


if __name__ == "__main__":
    main()
