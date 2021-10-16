from __future__ import division
# SeqCal module
def gcContent(seq):
    # G+C/(A+T+G+C)
    return (countBase(seq, 'G') + countBase(seq, 'C'))/len(seq)

def atContent(seq):
    # A+T/(A+T+G+C)
    return (countBase(seq, 'A') + countBase(seq, 'T'))/len(seq)

def countBase(seq, base):
    return seq.count(base.upper())

def countBasesDict(seq):
    basesM = {}
    for base in seq:
        basesM[base] = basesM.get(base, 0)+1
    return basesM

if __name__ == "__main__":
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = seq.upper()
    print("GC Content:", gcContent(seq))