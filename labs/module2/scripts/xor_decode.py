#!/usr/bin/env python3

# Define the byte arrays
dmsvSuiXSL = [
    200, 182, 183, 203, 243, 157, 189, 248, 215, 153, 170, 203,
    249, 148, 132, 241, 231, 148, 170, 132, 208, 144, 172, 197
]

EcnQYYmuTK = [
    200, 188, 183, 222, 253, 157, 180, 197, 200, 183, 177, 214,
    241, 151, 183, 220, 200, 161, 170, 203, 242, 152, 180, 193, 231
]

z5DZSzKjVN = [
    200, 188, 177, 199, 230, 158, 171, 203, 242, 133, 132, 225,
    240, 150, 189, 248, 193, 130, 189, 214, 180, 181, 185, 208, 245, 173
]

# The key is the last 4 bytes (gvQm657G5J)
key = [148, 241, 216, 164]

blobs = {
    "dmsvSuiXSL": dmsvSuiXSL,
    "EcnQYYmuTK": EcnQYYmuTK,
    "z5DZSzKjVN": z5DZSzKjVN
}

def xor_decode(data, key):
    decoded_bytes = bytearray()
    for i, b in enumerate(data):
        decoded_bytes.append(b ^ key[i % len(key)])
    return decoded_bytes

for name, blob in blobs.items():
    dec_bytes = xor_decode(blob, key)
    try:
        dec_string = dec_bytes.decode('utf-8', errors='replace')
    except Exception:
        dec_string = "<failed to decode as utf-8>"
        
    print(f"--- {name} ---")
    print(f"Decoded Bytes:  {list(dec_bytes)}")
    print(f"Decoded String: {dec_string}\n")
