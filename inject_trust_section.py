#!/usr/bin/env python3
"""
Injects the Institution Verification & Trust Matrix section into index.html.
Only includes links verified as working.
"""

import re
from pathlib import Path

HTML_FILE = Path.home() / "novaglobalkeys" / "index.html"

# --- The trust section (only verified links) ---
TRUST_SECTION = """
    <!-- INSTITUTIONAL VERIFICATION & INDEXING SECTION -->
    <section id="verification" class="py-20 border-t border-slate-800/60 bg-slate-950/40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <span class="inline-block bg-emerald-500/10 text-brand-accent text-xs font-bold uppercase tracking-widest px-3 py-1 rounded-md mb-3">Trust &amp; Audit Matrix</span>
                <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">Live Verification &amp; Exchange Integration</h2>
                <p class="text-slate-400 max-w-2xl mx-auto">Exchange OAuth authorization, contract security analysis, and open-source developer resources — each independently verifiable.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

                <!-- Bybit OAuth -->
                <div class="glass-panel p-6 rounded-2xl border border-slate-800">
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-amber-500 font-bold text-sm">Bybit CeFi Rails</span>
                        <span class="bg-amber-500/10 text-amber-500 text-[10px] font-mono px-2 py-0.5 rounded">OAuth 2.0</span>
                    </div>
                    <h4 class="text-base font-bold text-white mb-2">Broker Authorization</h4>
                    <p class="text-xs text-slate-400 mb-3">Client ID: <code class="text-brand-accent font-mono">x9dmxAGkDDoa</code> — Level 3 Broker (Kr000820)</p>
                    <a href="https://www.bybit.com/en/oauth?client_id=x9dmxAGkDDoa" target="_blank" rel="noopener" class="text-brand-accent text-xs font-semibold hover:underline">OAuth Portal &rarr;</a>
                </div>

                <!-- GoPlus Security -->
                <div class="glass-panel p-6 rounded-2xl border border-slate-800">
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-brand-accent font-bold text-sm">GoPlus Security</span>
                        <span class="bg-emerald-500/10 text-brand-accent text-[10px] font-mono px-2 py-0.5 rounded">Scanned</span>
                    </div>
                    <h4 class="text-base font-bold text-white mb-2">DKHYR Token Security</h4>
                    <p class="text-xs text-slate-400 mb-3">Automated contract security analysis, honeypot detection, permission checks.</p>
                    <a href="https://console.gopluslabs.io/token-security/8453/0x9991be994829601F90328CCF9cee4D1A55ADae70" target="_blank" rel="noopener" class="text-brand-accent text-xs font-semibold hover:underline">View Report &rarr;</a>
                </div>

                <!-- Binance Web3 -->
                <div class="glass-panel p-6 rounded-2xl border border-slate-800">
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-yellow-500 font-bold text-sm">Binance Web3</span>
                        <span class="bg-yellow-500/10 text-yellow-500 text-[10px] font-mono px-2 py-0.5 rounded">Indexed</span>
                    </div>
                    <h4 class="text-base font-bold text-white mb-2">Token Discovery</h4>
                    <p class="text-xs text-slate-400 mb-3">Official token metadata indexing on Binance Web3 Terminal.</p>
                    <a href="https://web3.binance.com/en/token/base/0x9991be994829601f90328ccf9cee4D1A55ADae70" target="_blank" rel="noopener" class="text-brand-accent text-xs font-semibold hover:underline">View on Binance Web3 &rarr;</a>
                </div>

                <!-- EIP-7702 -->
                <div class="glass-panel p-6 rounded-2xl border border-slate-800">
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-purple-400 font-bold text-sm">EIP-7702 Delegation</span>
                        <span class="bg-purple-500/10 text-purple-400 text-[10px] font-mono px-2 py-0.5 rounded">BaseScan</span>
                    </div>
                    <h4 class="text-base font-bold text-white mb-2">Uniswap V4 State Inspection</h4>
                    <p class="text-xs text-slate-400 mb-3">Authorization lists, state changes, and event logs verified on BaseScan.</p>
                    <a href="https://basescan.org/tx/0x53bd4a8c3f5ef4f6852efd0e17f8d742d80f274e779b4459266d47c3523481c7#eventlog" target="_blank" rel="noopener" class="text-brand-accent text-xs font-semibold hover:underline">Inspect Tx &rarr;</a>
                </div>

                <!-- PyPI SDK -->
                <div class="glass-panel p-6 rounded-2xl border border-slate-800">
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-pink-400 font-bold text-sm">Open SDK</span>
                        <span class="bg-pink-500/10 text-pink-400 text-[10px] font-mono px-2 py-0.5 rounded">PyPI</span>
                    </div>
                    <h4 class="text-base font-bold text-white mb-2">Python SDK</h4>
                    <p class="text-xs text-slate-400 mb-3">Publicly published packages for developer integration.</p>
                    <a href="https://pypi.org/user/nova_sdk/" target="_blank" rel="noopener" class="text-brand-accent text-xs font-semibold hover:underline">View on PyPI &rarr;</a>
                </div>

                <!-- Jarvis Skill Registry -->
                <div class="glass-panel p-6 rounded-2xl border border-slate-800">
                    <div class="flex items-center justify-between mb-4">
                        <span class="text-cyan-400 font-bold text-sm">MCP Registry</span>
                        <span class="bg-cyan-500/10 text-cyan-400 text-[10px] font-mono px-2 py-0.5 rounded">GitHub</span>
                    </div>
                    <h4 class="text-base font-bold text-white mb-2">Jarvis Skill Registry</h4>
                    <p class="text-xs text-slate-400 mb-3">Open-source MCP skill orchestration and versioned tool dispatch.</p>
                    <a href="https://github.com/rizbot4u/jarvis-skills-registry" target="_blank" rel="noopener" class="text-brand-accent text-xs font-semibold hover:underline">View on GitHub &rarr;</a>
                </div>

            </div>
        </div>
    </section>
"""

def main():
    if not HTML_FILE.exists():
        print(f"❌ File not found: {HTML_FILE}")
        return

    html = HTML_FILE.read_text(encoding="utf-8")

    # Check if section already exists
    if 'id="verification"' in html:
        print("⚠️  Verification section already present. Removing old one first...")
        html = re.sub(
            r'\s*<!-- INSTITUTIONAL VERIFICATION.*?</section>',
            '',
            html,
            flags=re.DOTALL
        )

    # Find the footer
    footer_match = re.search(r'(\s*<footer)', html)
    if not footer_match:
        print("❌ Could not find <footer> tag. Aborting.")
        return

    # Insert the trust section just before the footer
    insert_position = footer_match.start()
    new_html = html[:insert_position] + "\n" + TRUST_SECTION + html[insert_position:]

    HTML_FILE.write_text(new_html, encoding="utf-8")

    print("✅ Injected Trust & Audit Matrix section")
    print(f"   File: {HTML_FILE}")
    print(f"   Size: {len(new_html):,} bytes")
    print("")
    print("Next: git add . && git commit -m 'Add trust & audit matrix' && git push")


if __name__ == "__main__":
    main()
