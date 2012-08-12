#!/usr/bin/env python2.7

import time
import random

import pyo
from musicob.utils.pitch import Pitch


def setup():
    # Boot and start the pyo synthesis server
    server = pyo.Server().boot()
    server.start()
    return server


def get_scale():
    # Scale from Erv Wilson
    # "The Harmonic and Subharmonic Ogdoads with 12 Tones"
    # http://wilsonarchives.blogspot.com.au/2012/08/the-harmonic-and-subharmonic-ogdoads.html
    ratios = [
        1.0,
        15.0 / 14,
        9.0 / 8,
        15.0 / 13,
        5.0 / 4,
        15.0 / 11,
        11.0 / 8,
        3.0 / 2,
        13.0 / 8,
        5.0 / 3,
        7.0 / 4,
        15.0 / 8
    ]

    # Build the scale in a few octaves
    base = Pitch(60.0)
    pitches = [Pitch(fq=base.fq * r) for r in ratios]

    octaves = []
    for p in pitches:
        for octave in [-24, -12, 12, 24]:
            octaves.append(Pitch(ps=p.ps + octave))

    pitches.extend(octaves)

    return pitches


def next_chord(prev, scale):
    """Return a new chord with one pitch different than `prev`."""
    # Choose which pitch should be replaced
    replace = random.sample(range(len(prev)), 1)[0]

    next = []
    for i, pitch in enumerate(prev):
        prev_pitchspaces = [p.ps for p in prev]
        if i == replace:
            # Possible replacement pitches are within a minor third of the
            # pitch being replaced, not in the previous chord, and not already
            # in the next chord.
            options = scale

            # Not more than a major third lower
            options = [p for p in options if p.ps > pitch.ps - 4]

            # Not more than a major third higher
            options = [p for p in options if p.ps < pitch.ps + 4]

            # Not in the previous chord
            options = [p for p in options if p.ps not in prev_pitchspaces]

            # Not in this chord
            next_pitchspaces = [p.ps for p in next]
            options = [p for p in options if p.ps not in next_pitchspaces]

            # Choose the replacement pitch from the options
            choice = random.choice(options)
            next.append(Pitch(choice.ps))
        else:
            next.append(Pitch(pitch.ps))
    return next


def run():
    # Set the volume
    volume = 0.3

    # Set the timbre
    timbre = pyo.SawTable(order=12).normalize()

    # Set some options for note durations in seconds
    durs = [0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 1, 1, 1.5, 2.0]

    # Build a scale of pitches to use
    scale = get_scale()

    # Choose an initial chord
    # @todo: add changes in number of notes per chord
    num_notes = random.randint(4, 4)
    initial_options = [p for p in scale if p.ps >= 48 and p.ps <= 72]
    chord = random.sample(initial_options, num_notes)

    print [p.ps for p in chord]

    # Number of notes in the sequence
    length = 200

    for tick in range(length):
        # Choose the note duration
        dur = random.choice(durs)

        # Get the next chord
        chord = next_chord(chord, scale)
        print [p.ps for p in chord]

        # Play the note
        # Note: pyo requires that this is assigned to a variable, even though
        # it is never used.
        o = pyo.Osc(table=timbre, freq=[p.fq for p in chord],
            mul=volume).out()
        time.sleep(dur)


def teardown(server):
    server.stop()
    time.sleep(0.25)
    server.shutdown()


if __name__ == '__main__':
    server = setup()
    run()
    teardown(server)
