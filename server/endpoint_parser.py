print("TEST")
import re
from urllib.parse import urlparse

_variations = [
    #                            6( h16 ":" ) ls32
    "(?:%(hex)s:){6}%(ls32)s",
    #                       "::" 5( h16 ":" ) ls32
    "::(?:%(hex)s:){5}%(ls32)s",
    # [               h16 ] "::" 4( h16 ":" ) ls32
    "(?:%(hex)s)?::(?:%(hex)s:){4}%(ls32)s",
    # [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32
    "(?:(?:%(hex)s:)?%(hex)s)?::(?:%(hex)s:){3}%(ls32)s",
    # [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32
    "(?:(?:%(hex)s:){0,2}%(hex)s)?::(?:%(hex)s:){2}%(ls32)s",
    # [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32
    "(?:(?:%(hex)s:){0,3}%(hex)s)?::%(hex)s:%(ls32)s",
    # [ *4( h16 ":" ) h16 ] "::"              ls32
    "(?:(?:%(hex)s:){0,4}%(hex)s)?::%(ls32)s",
    # [ *5( h16 ":" ) h16 ] "::"              h16
    "(?:(?:%(hex)s:){0,5}%(hex)s)?::%(hex)s",
    # [ *6( h16 ":" ) h16 ] "::"
    "(?:(?:%(hex)s:){0,6}%(hex)s)?::",
]

IPV4_PAT = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
IPV4_RE = re.compile("^" + IPV4_PAT + "$")
HEX_PAT = "[0-9A-Fa-f]{1,4}"
LS32_PAT = "(?:{hex}:{hex}|{ipv4})".format(hex=HEX_PAT, ipv4=IPV4_PAT)
_subs = {"hex": HEX_PAT, "ls32": LS32_PAT}

UNSAFE_URL_CHARS = frozenset('\t\r\n')

UNRESERVED_PAT = (
    r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._!\-~"
)
IPV6_PAT = "(?:" + "|".join([x % _subs for x in _variations]) + ")"
ZONE_ID_PAT = "(?:%25|%)(?:[" + UNRESERVED_PAT + "]|%[a-fA-F0-9]{2})+"
IPV6_ADDRZ_PAT = r"\[" + IPV6_PAT + r"(?:" + ZONE_ID_PAT + r")?\]"
IPV6_ADDRZ_RE = re.compile("^" + IPV6_ADDRZ_PAT + "$")

def is_valid_ipv6_endpoint_url(endpoint_url):
    breakpoint()
    if UNSAFE_URL_CHARS.intersection(endpoint_url):
        return False
    hostname = f'[{urlparse(endpoint_url).hostname}]'
    print(IPV6_ADDRZ_PAT)
    return IPV6_ADDRZ_RE.match(hostname) is not None

ENDPOINT="http://s3_emulator:9001"

print(f"Is valid: {is_valid_ipv6_endpoint_url(ENDPOINT)}")
