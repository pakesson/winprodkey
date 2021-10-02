Decode and print the Windows 10 product key from a given registry hive file.
The `SOFTWARE` hive can be found at `%SystemRoot%\System32\Config\SOFTWARE`.

# Usage

With a Windows 10 partition mounted at `/mnt/windows`:
```
$ ./winprodkey.py /mnt/windows/Windows/System32/Config/SOFTWARE
Key: xxxxx-xxxxx-xxxxx-xxxxx-xxxxx
```