from TrackerAX25 import TrackerAX25
t = TrackerAX25()

# Test the ping decoding from TrackerAX25.py

# A raw file was dumped using od:
# od -t u1 2023-11-15-TrackerFinder.raw
# 0000000   192   0  46   0 110 116  16 242  57 111 192 192   0  46   0 110
# 0000020   116  16 242  57 111 192 192   0  46   0 110 116  16 242  57 111
# 0000040   192 192   0  46   0 110 116  16 242  57 111 192 192   0  46   0
# 0000060   110 116  16 242  57 111 192 192   0 130 160 164 166  64  64  96
# 0000100   150 138  96 160 164 160 118 174 146 136 138  98  64  98 174 146
# 0000120   136 138 100  64 101   3 240  47  48  48  48  53  48  55 122  55
# 0000140    55  52  48  46  48  57  83  47  49  55  48  49  57  46  53  56
# 0000160    69  79  48  48  48  47  50  52  48  47  65  61  50  53  56  56
# 0000200    48  57  49  48  52  54  95  84  82  75 192 192   0  46   0 110
# 0000220   116  16 242  57 111 192 192   0  46   0 110 116  16 242  57 111
# 0000240   192
# 
# The first 11 bytes provide one ping message:
msg = bytearray([192  , 0,  46,   0, 110, 116,  16, 242,  57, 111, 192])

def toDegsMin(decDegs) -> str:
    degsInt = int(decDegs)
    mins = 60.0*(decDegs - degsInt)
    return(f'{degsInt:d}{mins:02.2f}')

print(f'{t.pingId(msg)} {t.pingAge(msg)} {t.pingLat(msg):.4f} {t.pingLon(msg):.4f} {toDegsMin(t.pingLat(msg))} {toDegsMin(t.pingLon(msg))}')


