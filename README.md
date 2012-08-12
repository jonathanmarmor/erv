# erv

A demonstration of a just intonation tuning system created by Erv Wilson.

Hear an audio sample at http://ex.fm/song/ovy9p.

Yesterday I started playing around with the Python audio digital signal processing library pyo (http://code.google.com/p/pyo/).  This morning my friend Kraig Grady posted on Facebook a link (http://wilsonarchives.blogspot.com.au/2012/08/the-harmonic-and-subharmonic-ogdoads.html) to his blog post about one of many tuning systems sketched by his late friend and mentor Erv Wilson.  I wanted to hear what that tuning system sounded like, so I thought this would be a good opportunity to try out pyo.

The music is very simple.  It is a sequence of four-pitch chords, played by a simple saw tooth synth.  The first chord consists of four pitches randomly chosen from the scale in a two octave range.  Each subsequent chord is a repetition of the preceding chord with one pitch replaced with a randomly chosen new pitch.  The new pitch is always within an equal tempered major third above or below the removed pitch, was not in the preceding chord, and is not unison with another note in the new chord.  Of course the new pitches are always also in the same scale, and within a five octave range.  There is a little rhythmic variation to make it easier to hear melodic patterns that sound like music.

I didn't mess with the envelope of the sound, or the balance between the voices.  I'll leave that for another day to learn more about pyo.

There is almost certainly a better way to deal with rhythm than using time.sleep all the time.  It was not immediately obvious from the docs how to do this with pyo, so I just winged it.


## Dependencies

- pyo (http://code.google.com/p/pyo/)
- MusicOb (https://github.com/jonathanmarmor/MusicOb)


## To Do

- Remove external dependency on my MusicOb library.
