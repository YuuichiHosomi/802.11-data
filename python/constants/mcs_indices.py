from ..mcs_table import MCS_Table


def __init__():
    pass


        
#Table 20-30: 20 MHz, N_SS=1, N_ES=1
_TABLE_20_30_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
0	BPSK	1/2	1	52	4	52	26	6.5	7.2
1	QPSK	1/2	2	52	4	104	52	13.0	14.4
2	QPSK	3/4	2	52	4	104	78	19.5	21.7
3	16-QAM	1/2	4	52	4	208	104	26.0	28.9
4	16-QAM	3/4	4	52	4	208	156	39.0	43.3
5	64-QAM	2/3	6	52	4	312	208	52.0	57.8
6	64-QAM	3/4	6	52	4	312	234	58.5	65.0
7	64-QAM	5/6	6	52	4	312	260	65.0	72.2
"""
TABLE_20_30 = MCS_Table(_TABLE_20_30_txt, 'HT', 20, 1, 1, True)

# Table 20-31: 20 MHz, N_SS=2, N_ES=1, EQM
_TABLE_20_31_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
8	BPSK	1/2	1	52	4	104	52	13.0	14.4
9	QPSK	1/2	2	52	4	208	104	26.0	28.9
10	QPSK	3/4	2	52	4	208	156	39.0	43.3
11	16-QAM	1/2	4	52	4	416	208	52.0	57.8
12	16-QAM	3/4	4	52	4	416	312	78.0	86.7
13	64-QAM	2/3	6	52	4	624	416	104.0	115.6
14	64-QAM	3/4	6	52	4	624	468	117.0	130.0
15	64-QAM	5/6	6	52	4	624	520	130.0	144.4"""
TABLE_20_31 = MCS_Table(_TABLE_20_31_txt, 'HT', 20, 2, 1, True)

# Table 20-32: 20 MHz, N_SS = 3, N_ES = 1, EQM
_TABLE_20_32_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
16	BPSK	1/2	1	52	4	156	78	19.5	21.7
17	QPSK	1/2	2	52	4	312	156	39.0	43.3
18	QPSK	3/4	2	52	4	312	234	58.5	65.0
19	16-QAM	1/2	4	52	4	624	312	78.0	86.7
20	16-QAM	3/4	4	52	4	624	468	117.0	130.0
21	64-QAM	2/3	6	52	4	936	624	156.0	173.3
22	64-QAM	3/4	6	52	4	936	702	175.5	195.0
23	64-QAM	5/6	6	52	4	936	780	195.0	216.7"""
TABLE_20_32 = MCS_Table(_TABLE_20_32_txt, 'HT', 20, 3, 1, True)

# Table 20-33: 20 MHz, N_SS = 4, N_ES = 1, EQM
_TABLE_20_33_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
24	BPSK	1/2	1	52	4	208	104	26.0	28.9
25	QPSK	1/2	2	52	4	416	208	52.0	57.8
26	QPSK	3/4	2	52	4	416	312	78.0	86.7
27	16-QAM	1/2	4	52	4	832	416	104.0	115.6
28	16-QAM	3/4	4	52	4	832	624	156.0	173.3
29	64-QAM	2/3	6	52	4	1248	832	208.0	231.1
30	64-QAM	3/4	6	52	4	1248	936	234.0	260.0
31	64-QAM	5/6	6	52	4	1248	1040	260.0	288.9"""
TABLE_20_33 = MCS_Table(_TABLE_20_33_txt, 'HT', 20, 4, 1, True)

# Table 20-34 40 MHz, N_SS = 1, N_ES = 1 NOTE: MCS indices reset
_TABLE_20_34_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
0	BPSK	1/2	1	108	6	108	54	13.5	15.0
1	QPSK	1/2	2	108	6	216	108	27.0	30.0
2	QPSK	3/4	2	108	6	216	162	40.5	45.0
3	16-QAM	1/2	4	108	6	432	216	54.0	60.0
4	16-QAM	3/4	4	108	6	432	324	81.0	90.0
5	64-QAM	2/3	6	108	6	648	432	108.0	120.0
6	64-QAM	3/4	6	108	6	648	486	121.5	135.0
7	64-QAM	5/6	6	108	6	648	540	135.0	150.0"""
TABLE_20_34 = MCS_Table(_TABLE_20_34_txt, 'HT', 40, 1, 1, True)

# Table 20-35 40 MHz, N_SS = 2, N_ES = 1, EQM
_TABLE_20_35_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
8	BPSK	1/2	1	108	6	216	108	27.0	30.0
9	QPSK	1/2	2	108	6	432	216	54.0	60.0
10	QPSK	3/4	2	108	6	432	324	81.0	90.0
11	16-QAM	1/2	4	108	6	864	432	108.0	120.0
12	16-QAM	3/4	4	108	6	864	648	162.0	180.0
13	64-QAM	2/3	6	108	6	1296	864	216.0	240.0
14	64-QAM	3/4	6	108	6	1296	972	243.0	270.0
15	64-QAM	5/6	6	108	6	1296	1080	270.0	300.0"""
TABLE_20_35 = MCS_Table(_TABLE_20_35_txt, 'HT', 40, 2, 1, True)


# Table 20-36 40 MHz, N_SS = 3, EQM
# COLUMNS DIFFER FROM PRECEDING TABLE(S)!
_TABLE_20_36_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	N_ES	DR 800 ns	DR 400 ns
16	BPSK	1/2	1	108	6	324	162	1	40.5	45.0
17	QPSK	1/2	2	108	6	648	324	1	81.0	90.0
18	QPSK	3/4	2	108	6	648	486	1	121.5	135.0
19	16-QAM	1/2	4	108	6	1296	648	1	162.0	180.0
20	16-QAM	3/4	4	108	6	1296	972	1	243.0	270.0
21	64-QAM	2/3	6	108	6	1944	1296	2	324.0	360.0
22	64-QAM	3/4	6	108	6	1944	1458	2	364.5	405.0
23	64-QAM	5/6	6	108	6	1944	1620	2	405.0	450.0"""
TABLE_20_36 = MCS_Table(_TABLE_20_36_txt, 'HT', 40, 3, None, True)

# Table 20-37 40 MHz, N_SS = 4, EQM
_TABLE_20_37_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	N_ES	DR 800 ns	DR 400 ns
24	BPSK	1/2	1	108	6	432	216	1	54.0	60.0
25	QPSK	1/2	2	108	6	864	432	1	108.0	120.0
26	QPSK	3/4	2	108	6	864	648	1	162.0	180.0
27	16-QAM	1/2	4	108	6	1728	864	1	216.0	240.0
28	16-QAM	3/4	4	108	6	1728	1296	2	324.0	360.0
29	64-QAM	2/3	6	108	6	2592	1728	2	432.0	480.0
30	64-QAM	3/4	6	108	6	2592	1944	2	486.0	540.0
31	64-QAM	5/6	6	108	6	2592	2160	2	540.0	600.0"""
TABLE_20_37 = MCS_Table(_TABLE_20_37_txt, 'HT', 40, 4, None, True)

#Table 20-38 40 MHz MCS 32 format, N_SS = 1, N_ES = 1
_TABLE_20_38_txt = """MCS Index	Mod.	R	NBPSCS(iSS)	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
32	BPSK	1/2	1	48	4	48	24	6.0	6.7"""
TABLE_20_38 = MCS_Table(_TABLE_20_38_txt, 'HT', 40, 1, 1, True)

## Unequal modulation from here on out!
#Table 20-39 20 MHz, N_SS = 2, N_ES = 1, UEQM
_TABLE_20_39_txt = """MCS Index	Mod. Stream 1	Mod. Stream 2	R	NBPSC	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
33	16-QAM	QPSK	1/2	6	52	4	312	156	39	43.3
34	64-QAM	QPSK	1/2	8	52	4	416	208	52	57.8
35	64-QAM	16-QAM	1/2	10	52	4	520	260	65	72.2
36	16-QAM	QPSK	3/4	6	52	4	312	234	58.5	65.0
37	64-QAM	QPSK	3/4	8	52	4	416	312	78	86.7
38	64-QAM	16-QAM	3/4	10	52	4	520	390	97.5	108.3"""
TABLE_20_39 = MCS_Table(_TABLE_20_39_txt, 'HT', 20, 2, 1, False)

#Table 20-40 20 MHz, N_SS = 3, N_ES = 1, UEQM
# COLUMNS DIFFER FROM PRECEDING TABLE(S)!
_TABLE_20_40_txt = """MCS Index	Mod. Stream 1	Mod. Stream 2	Mod. Stream 3	R	NBPSC	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
39	16-QAM	QPSK	QPSK	1/2	8	52	4	416	208	52	57.8
40	16-QAM	16-QAM	QPSK	1/2	10	52	4	520	260	65	72.2
41	64-QAM	QPSK	QPSK	1/2	10	52	4	520	260	65	72.2
42	64-QAM	16-QAM	QPSK	1/2	12	52	4	624	312	78	86.7
43	64-QAM	16-QAM	16-QAM	1/2	14	52	4	728	364	91	101.1
44	64-QAM	64-QAM	QPSK	1/2	14	52	4	728	364	91	101.1
45	64-QAM	64-QAM	16-QAM	1/2	16	52	4	832	416	104	115.6
46	16-QAM	QPSK	QPSK	3/4	8	52	4	416	312	78	86.7
47	16-QAM	16-QAM	QPSK	3/4	10	52	4	520	390	97.5	108.3
48	64-QAM	QPSK	QPSK	3/4	10	52	4	520	390	97.5	108.3
49	64-QAM	16-QAM	QPSK	3/4	12	52	4	624	468	117	130.0
50	64-QAM	16-QAM	16-QAM	3/4	14	52	4	728	546	136.5	151.7
51	64-QAM	64-QAM	QPSK	3/4	14	52	4	728	546	136.5	151.7
52	64-QAM	64-QAM	16-QAM	3/4	16	52	4	832	624	156	173.3"""
TABLE_20_40 = MCS_Table(_TABLE_20_40_txt, 'HT', 20, 3, 1, False)

# Table 20-41 20 MHz, N_SS = 4, N_ES=1 UEQM
_TABLE_20_41_txt = """MCS Index	Mod. Stream 1	Mod. Stream 2	Mod. Stream 3	Mod. Stream 4	R	NBPSC	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
53	16-QAM	QPSK	QPSK	QPSK	1/2	10	52	4	520	260	65	72.2
54	16-QAM	16-QAM	QPSK	QPSK	1/2	12	52	4	624	312	78	86.7
55	16-QAM	16-QAM	16-QAM	QPSK	1/2	14	52	4	728	364	91	101.1
56	64-QAM	QPSK	QPSK	QPSK	1/2	12	52	4	624	312	78	86.7
57	64-QAM	16-QAM	QPSK	QPSK	1/2	14	52	4	728	364	91	101.1
58	64-QAM	16-QAM	16-QAM	QPSK	1/2	16	52	4	832	416	104	115.6
59	64-QAM	16-QAM	16-QAM	16-QAM	1/2	18	52	4	936	468	117	130.0
60	64-QAM	64-QAM	QPSK	QPSK	1/2	16	52	4	832	416	104	115.6
61	64-QAM	64-QAM	16-QAM	QPSK	1/2	18	52	4	936	468	117	130.0
62	64-QAM	64-QAM	16-QAM	16-QAM	1/2	20	52	4	1040	520	130	144.4
63	64-QAM	64-QAM	64-QAM	QPSK	1/2	20	52	4	1040	520	130	144.4
64	64-QAM	64-QAM	64-QAM	16-QAM	1/2	22	52	4	1144	572	143	158.9
65	16-QAM	QPSK	QPSK	QPSK	3/4	10	52	4	520	390	97.5	108.3
66	16-QAM	16-QAM	QPSK	QPSK	3/4	12	52	4	624	468	117	130.0
67	16-QAM	16-QAM	16-QAM	QPSK	3/4	14	52	4	728	546	136.5	151.7
68	64-QAM	QPSK	QPSK	QPSK	3/4	12	52	4	624	468	117	130.0
69	64-QAM	16-QAM	QPSK	QPSK	3/4	14	52	4	728	546	136.5	151.7
70	64-QAM	16-QAM	16-QAM	QPSK	3/4	16	52	4	832	624	156	173.3
71	64-QAM	16-QAM	16-QAM	16-QAM	3/4	18	52	4	936	702	175.5	195.0
72	64-QAM	64-QAM	QPSK	QPSK	3/4	16	52	4	832	624	156	173.3
73	64-QAM	64-QAM	16-QAM	QPSK	3/4	18	52	4	936	702	175.5	195.0
74	64-QAM	64-QAM	16-QAM	16-QAM	3/4	20	52	4	1040	780	195	216.7
75	64-QAM	64-QAM	64-QAM	QPSK	3/4	20	52	4	1040	780	195	216.7
76	64-QAM	64-QAM	64-QAM	16-QAM	3/4	22	52	4	1144	858	214.5	238.3"""
TABLE_20_41 = MCS_Table(_TABLE_20_41_txt, 'HT', 20, 4, 1, False)

# Table 20-42 40 MHz, N_SS = 2, N_ES = 1, UEQM
_TABLE_20_42_txt = """MCS Index	Mod. Stream 1	Mod. Stream 2	R	NBPSC	NSD	NSP	NCBPS	NDBPS	DR 800 ns	DR 400 ns
33	16-QAM	QPSK	1/2	6	108	6	648	324	81	90
34	64-QAM	QPSK	1/2	8	108	6	864	432	108	120
35	64-QAM	16-QAM	1/2	10	108	6	1080	540	135	150
36	16-QAM	QPSK	3/4	6	108	6	648	486	121.5	135
37	64-QAM	QPSK	3/4	8	108	6	864	648	162	180
38	64-QAM	16-QAM	3/4	10	108	6	1080	810	202.5	225"""
TABLE_20_42 = MCS_Table(_TABLE_20_42_txt, 'HT', 40, 2, 1, False)

# Table 20-43 40 MHz, N_SS = 3, UEQM
_TABLE_20_43_txt = """MCS Index	Mod. Stream 1	Mod. Stream 2	Mod. Stream 3	R	NBPSC	NSD	NSP	NCBPS	NDBPS	N_ES	DR 800 ns	DR 400 ns
39	16-QAM	QPSK	QPSK	1/2	8	108	6	864	432	1	108	120
40	16-QAM	16-QAM	QPSK	1/2	10	108	6	1080	540	1	135	150
41	64-QAM	QPSK	QPSK	1/2	10	108	6	1080	540	1	135	150
42	64-QAM	16-QAM	QPSK	1/2	12	108	6	1296	648	1	162	180
43	64-QAM	16-QAM	16-QAM	1/2	14	108	6	1512	756	1	189	210
44	64-QAM	64-QAM	QPSK	1/2	14	108	6	1512	756	1	189	210
45	64-QAM	64-QAM	16-QAM	1/2	16	108	6	1728	864	1	216	240
46	16-QAM	QPSK	QPSK	3/4	8	108	6	864	648	1	162	180
47	16-QAM	16-QAM	QPSK	3/4	10	108	6	1080	810	1	202.5	225
48	64-QAM	QPSK	QPSK	3/4	10	108	6	1080	810	1	202.5	225
49	64-QAM	16-QAM	QPSK	3/4	12	108	6	1296	972	1	243	270
50	64-QAM	16-QAM	16-QAM	3/4	14	108	6	1512	1134	1	283.5	315
51	64-QAM	64-QAM	QPSK	3/4	14	108	6	1512	1134	1	283.5	315
52	64-QAM	64-QAM	16-QAM	3/4	16	108	6	1728	1296	2	324	360"""
TABLE_20_43 = MCS_Table(_TABLE_20_43_txt, 'HT', 40, 3, None, False)

# Table 20-44 40 MHz, N_SS = 4, UEQM
_TABLE_20_44_txt = """MCS Index	Mod. Stream 1	Mod. Stream 2	Mod. Stream 3	Mod. Stream 4	R	NBPSC	NSD	NSP	NCBPS	NDBPS	N_ES	DR 800 ns	DR 400 ns
53	16-QAM	QPSK	QPSK	QPSK	1/2	10	108	6	1080	540	1	135	150
54	16-QAM	16-QAM	QPSK	QPSK	1/2	12	108	6	1296	648	1	162	180
55	16-QAM	16-QAM	16-QAM	QPSK	1/2	14	108	6	1512	756	1	189	210
56	64-QAM	QPSK	QPSK	QPSK	1/2	12	108	6	1296	648	1	162	180
57	64-QAM	16-QAM	QPSK	QPSK	1/2	14	108	6	1512	756	1	189	210
58	64-QAM	16-QAM	16-QAM	QPSK	1/2	16	108	6	1728	864	1	216	240
59	64-QAM	16-QAM	16-QAM	16-QAM	1/2	18	108	6	1944	972	1	243	270
60	64-QAM	64-QAM	QPSK	QPSK	1/2	16	108	6	1728	864	1	216	240
61	64-QAM	64-QAM	16-QAM	QPSK	1/2	18	108	6	1944	972	1	243	270
62	64-QAM	64-QAM	16-QAM	16-QAM	1/2	20	108	6	2160	1080	1	270	300
63	64-QAM	64-QAM	64-QAM	QPSK	1/2	20	108	6	2160	1080	1	270	300
64	64-QAM	64-QAM	64-QAM	16-QAM	1/2	22	108	6	2376	1188	1	297	330
65	16-QAM	QPSK	QPSK	QPSK	3/4	10	108	6	1080	810	1	202.5	225
66	16-QAM	16-QAM	QPSK	QPSK	3/4	12	108	6	1296	972	1	243	270
67	16-QAM	16-QAM	16-QAM	QPSK	3/4	14	108	6	1512	1134	1	283.5	315
68	64-QAM	QPSK	QPSK	QPSK	3/4	12	108	6	1296	972	1	243	270
69	64-QAM	16-QAM	QPSK	QPSK	3/4	14	108	6	1512	1134	1	283.5	315
70	64-QAM	16-QAM	16-QAM	QPSK	3/4	16	108	6	1728	1296	2	324	360
71	64-QAM	16-QAM	16-QAM	16-QAM	3/4	18	108	6	1944	1458	2	364.5	405
72	64-QAM	64-QAM	QPSK	QPSK	3/4	16	108	6	1728	1296	2	324	360
73	64-QAM	64-QAM	16-QAM	QPSK	3/4	18	108	6	1944	1458	2	364.5	405
74	64-QAM	64-QAM	16-QAM	16-QAM	3/4	20	108	6	2160	1620	2	405	450
75	64-QAM	64-QAM	64-QAM	QPSK	3/4	20	108	6	2160	1620	2	405	450
76	64-QAM	64-QAM	64-QAM	16-QAM	3/4	22	108	6	2376	1782	2	445.5	495"""
TABLE_20_44 = MCS_Table(_TABLE_20_44_txt, 'HT', 40, 4, None, False)

tables=[TABLE_20_30,
        TABLE_20_31,
        TABLE_20_32,
        TABLE_20_33,
        TABLE_20_34,
        TABLE_20_35,
        TABLE_20_36,
        TABLE_20_37,
        TABLE_20_38,
        TABLE_20_39,
        TABLE_20_40,
        TABLE_20_41,
        TABLE_20_42,
        TABLE_20_43,
        TABLE_20_44,
        ]


def main(args):
    """Test/demo"""
    import csv
    #table_20_30 = csv.DictReader(TABLE_20_30_txt.splitlines(), dialect=csv.excel_tab)
    #print list(table_20_30)

    print "\n\n".join([str(t) for t in tables])

    print tables[0]._panda()
    print tables[len(tables)-1]._panda()
            

            

    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


    
