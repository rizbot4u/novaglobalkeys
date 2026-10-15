#!/usr/bin/env python3
"""
Insert the live settlement proof card into the BaseScan Receipts section.
Uses a more robust marker that matches your exact HTML structure.
"""

import re
import shutil
import time
from pathlib import Path

HTML = Path.home() / "novaglobalkeys" / "index.html"
BACKUP = HTML.with_suffix(f".html.bak.tx-{int(time.time())}")

LIVE_TX_CARD = '''
                <!-- Live Atomic Settlement Proof -->
                <div class="glass-panel p-6 rounded-2xl border border-slate-800 hover:border-slate-700 transition-all">
                    <div class="flex items-center justify-between mb-4">
                        <span class="px-3 py-1 rounded-md text-xs font-mono bg-purple-500/10 text-purple-400 border border-purple-500/20">Live Settlement</span>
                        <span class="text-xs font-mono text-slate-500">Block 52635071</span>
                    </div>
                    <h4 class="text-lg font-bold text-white mb-1">First Atomic DvP Settlement</h4>
                    <p class="text-xs text-slate-400 mb-4">500 DKHYR + 5 NVP-1 exchanged in a single transaction. Confirmed on Base Mainnet.</p>
                    <div class="bg-slate-950 p-3 rounded-lg flex items-center justify-between font-mono text-xs text-slate-300 border border-slate-800 mb-4">
                        <span class="truncate">0x1a04cf220d364b7a05a7492e32fe093831975f5636e49e4b17de9245cadc6101</span>
                    </div>
                    <a href="https://basescan.org/tx/0x1a04cf220d364b7a05a7492e32fe093831975f5636e49e4b17de9245cadc6101" target="_blank" rel="noopener" class="inline-flex items-center text-xs font-semibold text-purple-400 hover:underline">
                        Verify Settlement on BaseScan <i class="fa-solid fa-arrow-up-right-from-square ml-1 text-[10px]"></i>
                    </a>
                </div>
'''

def main():
    src = HTML.read_text(encoding="utf-8")

    if "First Atomic DvP Settlement" in src:
        print("ℹ️  Live settlement card already present. Nothing to do.")
        return

    shutil.copy2(HTML, BACKUP)
    print(f"✅ Backup: {BACKUP.name}")

    # Find the EIP-7702 card (last card in the receipts grid) and insert after it
    # The EIP-7702 card ends with the BaseScan verify link. We look for that anchor.
    pattern = re.compile(
        r'(<a href="https://basescan\.org/tx/0x53bd4a8c3f5ef4f6852efd0e17f8d742d80f274e779b4459266d47c3523481c7"[^>]*>.*?</a>\s*</div>)',
        re.DOTALL,
    )

    match = pattern.search(src)
    if not match:
        # Fallback: find any closing </div> immediately before the SDK section
        fallback = re.search(
            r'(</div>\s*</div>\s*</section>\s*<!--\s*DEVELOPER SDK)',
            src,
        )
        if fallback:
            src = src[:fallback.start()] + LIVE_TX_CARD + "\n" + src[fallback.start():]
            print("✅ Inserted live settlement card (fallback marker)")
        else:
            print("❌ Could not find insertion point")
            print("   Please paste the output of: grep -n 'EIP-7702' index.html")
            return
    else:
        insert_pos = match.end()
        src = src[:insert_pos] + "\n" + LIVE_TX_CARD + src[insert_pos:]
        print("✅ Inserted live settlement card after EIP-7702 card")

    HTML.write_text(src, encoding="utf-8")
    print(f"✅ Written: {HTML}")

    # Verify
    print("")
    print("=== Verification ===")
    checks = [
        ("First Atomic DvP Settlement", "Live settlement card"),
        ("0x1a04cf220d364b7a05a7492e32fe093831975f5636e49e4b17de9245cadc6101", "Settlement tx hash"),
    ]
    for needle, label in checks:
        count = src.count(needle)
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {label}: {count} occurrence(s)")

    print("")
    print("Next:")
    print("  cd ~/novaglobalkeys")
    print("  git add . && git commit -m 'Add live atomic DvP settlement proof card' && git push")


if __name__ == "__main__":
    main()
