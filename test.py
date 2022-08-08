from matplotlib import pyplot as plt
from scipy import ifft

from thinkdsp import read_wave

wave1 = read_wave('do.wav')
wave1.normalize()
wave1.make_audio()

wave2 = read_wave('do_major.wav')
wave2.normalize()
wave2.make_audio()

wave1.plot()
wave2.plot()

segment1 = wave1.segment(start=1.1, duration=0.3)
segment1.make_audio()

segment2 = wave2.segment(start=1.1, duration=0.3)
segment2.make_audio()

segment1.plot()
segment2.plot()

segment1.segment(start=1.1, duration=0.005).plot()
segment2.segment(start=1.1, duration=0.005).plot()

spectrum1 = segment1.make_spectrum()
spectrum1.plot(high=7000)
spectrum2 = segment2.make_spectrum()
spectrum2.plot(high=7000)

spectrum1 = segment1.make_spectrum()
# print(spectrum1.__dict__)
a = spectrum1.__dict__.get("fs")[:20]
# print(a)
spectrum1.plot(high=1000)

spectrum2 = segment2.make_spectrum()
b = spectrum2.__dict__.get("fs")[:20]
# print(b)
# for i in b:
#     if i in a:
#         print("da", i)
#     else:
#         print("net")
spectrum2.plot(high=1000)

do = spectrum1.peaks()[:30]
# print(do)

spectrum1.low_pass(2000)
spectrum1.make_wave().make_audio()

do_major = spectrum2.peaks()[:30]

spectrum2.low_pass(2000)
spectrum2.make_wave().make_audio()


for i in do:
    for x in do_major:
        if i[1] == x[1]:
            do_major.remove(x)

print(do_major)

# plt.plot(do_major)
# plt.show()

# print(transform)

