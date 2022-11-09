# evans terrible and scuffed audio visualizer

a quick thing i made to generate live audio waveforms. basically hundreds of frames generated and put together with superglue


incredibly scuffed, only released for [educational](https://www.youtube.com/watch?v=1SMJ04RO_JM&t=278s) purposes

if you know how to use it ya know


```py
from etsav import wavgen
```

website: https://evan.systems


# but.. daddy how does it work uwu

using `matplotlib` and `opencv` to calculate the amplitudes and frequencies of an audio, to calculate one frame. Then, use a graphics rendering library to smooth out frameby transitions and a renderfutureframe function to skip by each frame to create every last output. mask it in white and blend it in, profit

example of xtreme math:
```py
   if span != None:
            # start, end = span 
            start = int(span[0]*self.samplerate)
            end = int(span[1]*self.samplerate)
        fig = plt.figure("Audio")
        if is_stereo:
            for i in range(2):
                ax = plt.subplot(2, 1, i+1)
                ax.plot(self.data[start:end, i], lw=0.5)
                ```

# but i want an actual working one lmao

search them up lmao
