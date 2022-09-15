# Corporate credential generator

Using
---
```
[>] Wordlist Module
usage: wordlist [-h] [-m MODE] [-p PATTERN] [-d DOMAIN] [-o OUTNAME]

Generate a wordlist by pattern

options:
  -h, --help  show this help message and exit
  -m MODE     mode
  -p PATTERN  pattern
  -d DOMAIN   domain
  -o OUTNAME  outname
```
Examples
-----

Generate a list of users with different patterns (N, AAL, AL, N.L)

```

python wordlist.py -m user -p AL -d midomain.com -o out-aal.txt
[>] Wordlist Module
[?] Domain can be used with -d domain.com
[?] Valid Options Are N, AL, AAL, N.L
[+] Generating under AL pattern
[+] Adding domain AL@midomain.com
[+] Top3 is arodriguez@midomain.com agonzalez@midomain.com amartinez@midomain.com
[+] Saving 1300 users into out.txt


```
