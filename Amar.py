# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))