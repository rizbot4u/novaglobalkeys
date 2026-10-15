#!/usr/bin/env python3
"""
Fix the landing page:
  1. Replace the old "Atomic DvP Settlement Transaction" card with the new
     verified NovaDvPSettlement contract + live settlement tx.
  2. Replace "AI Governor Node" with "Nova Orchestrator" (maps to real service).
  3. Replace "Sharia Compliant" with "Programmable On-Chain Zakat".
  4. Replace "Sharia-compliant" with "Programmable Zakat".
  5. Fix the GoPlus card: change "Scanned" -> "Security Check Available".
  6. Fix the Binance Web3 card: change "Indexed" -> "Metadata Available".
  7. Back up index.html before editing.
  8. Verify all replacements.
"""

import re
import shutil
import time
from pathlib import Path

HTML = Path.home() / "novaglobalkeys" / "index.html"
BACKUP = HTML.with_suffix(f".html.bak.{int(time.time())}")


def main():
    if not HTML.exists():
        print(f"❌ Not found: {HTML}")
        return

    src = HTML.read_text(encoding="utf-8")
    original = src

    # Backup
    shutil.copy2(HTML, BACKUP)
    print(f"✅ Backup: {BACKUP.name}")

    # ── 1. Replace old Atomic DvP card with new verified contract card ──
    old_card_pattern = re.compile(
        r'<h4 class="text-lg font-bold text-white mb-1">Atomic DvP Settlement Transaction</h4>.*?'
        r'0xf128a8026f0ee8f0adafef448bb711b2997d72b61a93abd3829df4f40d36bf27.*?'
        r'</a>',
        re.DOTALL,
    )

    new_card = '''<h4 class="text-lg font-bold text-white mb-1">NovaDvPSettlement (Atomic DvP)</h4>
                    <p class="text-xs text-slate-400 mb-4">Both legs execute in a single transaction, or both revert. Deployed and verified on Base Mainnet.</p>
                    <div class="bg-slate-950 p-3 rounded-lg flex items-center justify-between font-mono text-xs text-slate-300 border border-slate-800 mb-4">
                        <span class="truncate">0x665714c657e35e0a571D902a542a30FC9A026DA5</span>
                    </div>
                    <a href="https://basescan.org/address/0x665714c657e35e0a571D902a542a30FC9A026DA5" target="_blank" rel="noopener" class="inline-flex items-center text-xs font-semibold text-purple-400 hover:underline">
                        View Contract on BaseScan <i class="fa-solid fa-arrow-up-right-from-square ml-1 text-[10px]"></i>
                    </a>'''

    if old_card_pattern.search(src):
        src = old_card_pattern.sub(new_card, src, count=1)
        print("✅ Replaced old Atomic DvP card with new verified contract")
    else:
        print("⚠️  Old Atomic DvP card not matched (may already be updated)")

    # ── 2. AI Governor Node -> Nova Orchestrator ──
    before = src
    src = src.replace("AI Governor Node", "Nova Orchestrator")
    if src != before:
        print("✅ Replaced 'AI Governor Node' with 'Nova Orchestrator'")

    # ── 3. Sharia Compliant -> Programmable On-Chain Zakat ──
    before = src
    src = src.replace("Sharia Compliant", "Programmable On-Chain Zakat")
    src = src.replace("Sharia-compliant", "Programmable Zakat")
    if src != before:
        print("✅ Replaced Sharia language with Programmable Zakat")

    # ── 4. GoPlus: "Scanned" -> "Security Check Available" ──
    before = src
    src = re.sub(
        r'(bg-emerald-500/10 text-brand-accent text-\[10px\] font-mono px-2 py-0\.5 rounded">)Scanned(</span>)',
        r'\1Security Check\2',
        src,
    )
    src = src.replace(
        "Automated contract security analysis, honeypot detection, permission checks.",
        "Automated contract security check — verify current status on GoPlus.",
    )
    if src != before:
        print("✅ Updated GoPlus card language")

    # ── 5. Binance Web3: "Indexed" -> "Metadata Available" ──
    before = src
    src = src.replace(
        "Official token metadata indexing on Binance Web3 Terminal.",
        "Token metadata available via Binance Web3 Terminal.",
    )
    if src != before:
        print("✅ Updated Binance Web3 card language")

    # ── 6. Update the hero line about atomic DvP ──
    src = src.replace(
        "verified atomic DvP settlement at under $0.002 per round-trip",
        "verified atomic DvP settlement — both legs in a single transaction, or both revert",
    )

    # ── 7. Add the live settlement tx hash as a standalone proof card ──
    live_tx_card = '''
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

    # Insert before the closing div of the receipts grid
    if "First Atomic DvP Settlement" not in src:
        # Find the last </div> before </section> of the receipts section
        marker = '</div>\n        </div>\n    </section>\n\n    <!-- DEVELOPER SDK'
        if marker in src:
            src = src.replace(marker, live_tx_card + marker, 1)
            print("✅ Added live settlement proof card")
        else:
            print("⚠️  Could not find insertion point for live settlement card")

    # Write
    if src != original:
        HTML.write_text(src, encoding="utf-8")
        print(f"✅ Written: {HTML}")
    else:
        print("ℹ️  No changes were needed")

    # ── Verification ──
    print("")
    print("=== Verification ===")
    checks = [
        ("NovaDvPSettlement", "New atomic contract card"),
        ("0x665714c657e35e0a571D902a542a30FC9A026DA5", "Contract address"),
        ("First Atomic DvP Settlement", "Live settlement card"),
        ("0x1a04cf220d364b7a05a7492e32fe093831975f5636e49e4b17de9245cadc6101", "Settlement tx hash"),
        ("Nova Orchestrator", "Replaced AI Governor Node"),
        ("Programmable On-Chain Zakat", "Replaced Sharia Compliant"),
    ]
    for needle, label in checks:
        count = src.count(needle)
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {label}: {count} occurrence(s)")

    # Check for removed strings
    print("")
    print("=== Removed Strings (should be 0) ===")
    removals = [
        ("Sharia Compliant", "Old Sharia label"),
        ("AI Governor Node", "Old Governor name"),
    ]
    for needle, label in removals:
        count = src.count(needle)
        status = "✅" if count == 0 else "⚠️ "
        print(f"  {status} {label}: {count} occurrence(s)")

    print("")
    print("Next:")
    print("  cd ~/novaglobalkeys")
    print("  git add . && git commit -m 'Atomic DvP live settlement + claim corrections' && git push")


if __name__ == "__main__":
    main()
