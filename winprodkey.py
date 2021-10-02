#!/usr/bin/env python

import sys
from Registry import Registry

def decode_product_key(prodid):
    prodid = list(prodid)
    prodid[66] = prodid[66] & 0xf7

    key_offset = 52
    valid_chars = "BCDFGHJKMPQRTVWXY2346789"

    key = ""
    for _ in range(25):
        current = 0
        for y in range(14,-1,-1):
            current = current * 256
            current = int(prodid[y + key_offset] + current)
            prodid[y + key_offset] = int(current/24)
            current = current % 24
            last = current
        key = valid_chars[current] + key

    key = key[1:last+1] + "N" + key[last+1 : len(key)]
    key = "-".join([key[i:i+5] for i in range(0, len(key), 5)])

    return key

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: winprodkey.py <SOFTWARE_HIVE>")
        sys.exit(-1)
    
    reg = Registry.Registry(sys.argv[1])
    
    try:
        key = reg.open("Microsoft\\Windows NT\\CurrentVersion")
        value = key.value("DigitalProductID").value()
        if not isinstance(value, bytes):
            print("Unexpected value type")
            sys.exit(-1)
        product_key = decode_product_key(value)
        print(f"Key: {product_key}")
    except Registry.RegistryKeyNotFoundException:
        print("Registry key not found")
        sys.exit(-1)
    
