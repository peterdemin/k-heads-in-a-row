import random
import textwrap

toss = lambda: random.randint(0, 1)
tosses = lambda n: (toss() for i in xrange(n))

def sequence_lengths(results):
    sequence_length = {}
    prev = None
    seq = 1
    for coin in results:
        if coin == prev:
            seq+= 1
        else:
            if prev is not None:
                sequence_length[seq] = sequence_length.get(seq, 0) + 1
            seq = 1
        prev = coin
    sequence_length[seq] = sequence_length.get(seq, 0) + 1
    return sequence_length

def random_generator():
    eamt = 1000
    tamt = 1000
    sequence_length = {}
    for eid in xrange(eamt):
        for k, v in sequence_lengths(tosses(tamt)).iteritems():
            sequence_length[k] = sequence_length.get(k, 0) + v
    for k in sorted(sequence_length.keys()):
        print '%2d - 1/%.0f' % (k, (tamt*eamt)/sequence_length[k])

random_generator()

real_tosses = ''.join('''
    oooppopppopppooppop
    ppooopopopppppooooo
    ooppoppooopppoopppo
    oppppooooppppoppoop
    opooppooopoooooopoo
    oopooopoppoppoppoop
    ooopoppppppoopoppoo
    opppppoppoppoooppop
    '''.split())
real_lengths = sequence_lengths(real_tosses)
for k in sorted(real_lengths.keys()):
    print '%2d - 1/%f' % (k, 1.*len(real_tosses) / real_lengths[k])

