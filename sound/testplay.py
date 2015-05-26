import alsaaudio
from math import pi, sin, pow
import getch

SAMPLE_RATE = 44100
FORMAT = alsaaudio.PCM_FORMAT_U8
PERIOD_SIZE = 512
N_SAMPLES = 1024

notes = "abcdefg"
frequencies = {}
for i, note in enumerate(notes):
    frequencies[note] = 440 * pow(pow(2, 1/2), i)

# Generate the sine wave, centered at y=128 with 1024 samples
sine_wave = [int(sin(x * 2*pi/N_SAMPLES) * 127) for x in range(0, N_SAMPLES)]

square_wave = []
sawtooth_wave = []
triangle_wave = []
for i in range(0, N_SAMPLES):
    phase = (i * 2*pi / N_SAMPLES) % 2*pi

    if phase < pi:
        square_wave.append(127)
    else:
        square_wave.append(-128)

    sawtooth_wave.append(int(127 - (127 // pi * phase)))

    if phase < pi:
        triangle_wave.append(int(-127 + (2 * 127 * phase // pi)))
    else:
        triangle_wave.append(int(3 * 127 - (2 * 127 * phase // pi)))



def main():
    buf = bytearray(PERIOD_SIZE)
    
    # alsaaudio setup
    dev = alsaaudio.PCM(type=alsaaudio.PCM_PLAYBACK)
    dev.setchannels(1)
    dev.setrate(SAMPLE_RATE)
    dev.setformat(FORMAT)
    dev.setperiodsize(PERIOD_SIZE)

    #load_buf(buf, 440)
    f = 440
    w_half = [x//2 + 128 for x in make_wave(sine_wave, f)]
    #w_o1 = [x//4 for x in make_wave(f*2)]
    #w_o2 = [x//6 for x in make_wave(f*3)]
    #w_o3 = [x//8 for x in make_wave(f*4)]
    #w_o4 = [x//10 for x in make_wave(f*5)]
    #w_o4 = [x//12 for x in make_wave(f*6)]
    #w_o5 = [x//14 for x in make_wave(f*7)]
    #w_o6 = [x//16 for x in make_wave(f*8)]

    #for i, samp in enumerate(w_o1):
    #    w[i] += samp + w_o2[i] + w_o3[i] + w_o4[i] + w_o5[i] + w_o6[i] + 128
    #    print(w[i])
    #buf = bytearray(w)

    #for i, samp in enumerate(w):
    #    if samp > 0:
    #        samp = 127
    #    else:
    #        samp = -128

    w = [x + 128 for x in make_wave(square_wave, 440)]
    buf = bytearray(w)

    char = getch.getch()
    last = 'q'
    while char != 'q':
        if char != last:
            if char == '1':
                w = [x//2 + 128 for x in make_wave(sine_wave, 440)]
                buf = bytearray(w)
            elif char == '2':
                w = [x//2 + 128 for x in make_wave(square_wave, 440)]
                buf = bytearray(w)
            elif char == '3':
                w = [x//2 + 128 for x in make_wave(sawtooth_wave, 440)]
                buf = bytearray(w)
            elif char == '4':
                w = [x//2 + 128 for x in make_wave(triangle_wave, 440)]
                buf = bytearray(w)
            elif char == '5':
                buf = bytearray(w_half)
        dev.write(buf)
        dev.write(buf)
        dev.write(buf)

        last = char
        char = getch.getch()

    return 0

#def load_buf(buf, frequency):
#    step = N_SAMPLES * frequency // SAMPLE_RATE
#    for i in range(0, PERIOD_SIZE):
#        buf[i] = wave[(step * i * N_SAMPLES // PERIOD_SIZE) % N_SAMPLES]
#    return buf

def make_wave(wave, frequency):
    step = N_SAMPLES * frequency // SAMPLE_RATE
    w = []
    for i in range(0, PERIOD_SIZE):
        w.append(wave[(step * i * N_SAMPLES // PERIOD_SIZE) % N_SAMPLES])
    return w

if __name__ == '__main__':
    main()
