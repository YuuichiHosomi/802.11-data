def __init__():
    pass
#802.11 HT (N) PLCP

## See especially equations 20-91 through 20-94, in \s 20.4.3
## And tables 20-29 through 30-44? in \s 20.6 (Parameters for HT MCSs)

## PLCP sequences -- see \s 20.3
## Non-HT:
## L-STF (8 us),
## L-LTF (8 us),
## L-SIG (4 us)
## = 20 us

## HT-Mixed:
## L-STF,
## L-LTF,
## L-SIG,
## HT-SIG (8 us),
## HT-STF (4 us),
## Data HT-DLTFs (4 us per LTF) (may be 1, 2 or 4),
## Extension HT-ELTFs (4 us per LTF) (may be 0, 1, 2 or 4),
## = 32 us + data & extension LTFs

## HT-Greenfield:
## GT-GF-STF (8 us),
## HT-LTF1 (8 us),
## HT-SIG (8 us),
## Data HT-DLTFs (4 us per LTF) (may be 1, 2 or 4),
## Extension HT-ELTFs (4 us per LTF) (may be 0, 1, 2 or 4),
## = 24 us + data & extension LTFs


def N_STS_from_N_SS(N_SS, STBC):
    """ Number of space-time streams (N_{STS}) from number of spatial
    streams (N_{SS}), and the space-time block coding (STBC) used.

    The standard gives this a table (20-12), but it's just addition!
    """

    return N_SS + STBC

def N_HTDLTF_from_N_STS(N_STS):
    """Number of HT Data LTFs from number of space-time streams"""
    
    table_20_13 = {1 : 1,
                   2:  2,
                   3:  4,
                   4:  4}

    return table_20_13[N_STS]

def N_HTELTF_from_N_ESS(N_ESS):
    """Number of HT Extension LTFs from number of extension spatial streams"""

    table_20_14 = {0: 0,
                   1: 1,
                   2: 2,
                   3: 4}

    return table_20_14[N_ESS]

def N_SYM_BCC(length, STBC_p, N_ES, N_DBPS):
    """Number of symbols for data.  Equation 20-32 & discussion.

    length: # of data bits,
    N_DBPS: # of data bits per OFDM symbol
    N_ES = Number of BCC encoders
    """


    m_STBC = {True: 2,
              False: 1}[STBC_p]

    n_sym = m_STBC * math.ceil((8*length + 16 + 6*N_ES)/(m_STBC * N_DBPS))

    return n_sym

def N_SYM_LDPC(length):
    
    """The equations for LDPC are complicated, and I don't think they
    buy us anything important right now."""
    
    raise NotImplementedError()

        
