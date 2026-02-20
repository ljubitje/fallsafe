#!/usr/bin/env python3
"""
fallsafe Integrity Verification Tool
Usage: python3 verify.py <conversation_file>
Generates SHA-256 hash for conversation integrity checking.
"""

import hashlib
import sys
import json
from datetime import datetime

def hash_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    h = hashlib.sha256(content.encode('utf-8')).hexdigest()
    return h, len(content)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify.py <conversation_file> [--check <expected_hash>]")
        sys.exit(1)
    
    filepath = sys.argv[1]
    file_hash, char_count = hash_file(filepath)
    
    # Rough token estimate (1 token ≈ 4 chars)
    token_est = char_count // 4
    
    if '--check' in sys.argv:
        expected = sys.argv[sys.argv.index('--check') + 1]
        match = file_hash == expected
        print(f"Expected: {expected}")
        print(f"Got:      {file_hash}")
        print(f"MATCH: {match}")
        if not match:
            print("WARNING: Content has been modified!")
    else:
        print(f"Hash:     {file_hash}")
        print(f"Chars:    {char_count}")
        print(f"Tokens:   ~{token_est}")
        print(f"Time:     {datetime.now().isoformat()}")
        print(f"\nStore this hash in the seed document for verification.")

if __name__ == '__main__':
    main()
