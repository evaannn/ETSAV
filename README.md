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
