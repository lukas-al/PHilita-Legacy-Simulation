import csv
import numpy as np
import random

from random import choices
from collections import Counter

'''
population = [1, 2, 3, 4, 5, 6]
weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]

choices(population, weights)
'''
journeys		=	int(0.0001*10**6)
combined 		=	[]

#population 		= 	["EntPT2",	"EntPT5",	"EntPT8",	"EntPT11",	"EntPT14",	"EntPT17",	"EntPT20",	"EntPT23",	"EntPT26",	"EntPT29",	"EntPT32",	"EntPT35",	"EntPT38",	"EntPT41",	"EntPT44",	"EntPT47",	"EntPT50",	"EntPT53",	"EntPT56",	"EntPT59",	"EntPT62",	"EntPT65",	"EntPT68",	"EntPT71",	"EntPT74",	"EntPT77",	"EntPT80",	"EntPT83",	"EntPT86",	"EntPT89",	"EntPT92",	"EntPT95",	"EntPT98",	"EntPT101",	"EntPT104",	"EntPT107",	"EntPT110",	"EntPT113",	"EntPT116",	"EntPT119",	"EntPT122",	"EntPT125",	"EntPT128",	"EntPT131",	"EntPT134",	"EntPT137",	"EntPT140",	"EntPT143",	"EntPT146",	"EntPT149",	"EntPT152",	"EntPT155",	"EntPT158",	"EntPT161",	"EntPT164",	"EntPT167",	"EntPT170",	"EntPT173",	"EntPT176",	"EntPT179",	"EntPT182",	"EntPT185",	"EntPT188",	"EntPT191",	"EntPT194",	"EntPT197",	"EntPT200",	"EntPT203",	"EntPT206",	"EntPT209",	"EntPT212",	"EntPT215",	"EntPT218",	"EntPT221",	"EntPT224",	"EntPT227",	"EntPT230",	"EntPT233",	"EntPT236",	"EntPT239",	"EntPT242",	"EntPT245",	"EntPT248",	"EntPT251",	"EntPT254",	"EntPT257",	"EntPT260",	"EntPT263",	"EntPT266",	"EntPT269",	"EntPT272",	"EntPT275",	"EntPT278",	"EntPT281",	"EntPT284",	"EntPT287"]
timestamps		=	["T0",	"T3",	"T6",	"T9",	"T12",	"T15",	"T18",	"T21", 	"T24", 	"T27", 	"T30", 	"T33", 	"T36", 	"T39", 	"T42", 	"T45", 	"T48", 	"T51", 	"T54", 	"T57", 	"T60", 	"T63", 	"T66", 	"T69", 	"T72", 	"T75", 	"T78", 	"T81", 	"T84", 	"T87", 	"T90", 	"T93", 	"T96", 	"T99", 	"T102", "T105", "T108", "T111", "T114", "T117", 	"T120", 	"T123", 	"T126", 	"T129", 	"T132", 	"T135", 	"T138", 	"T141", 	"T144", 	"T147", 	"T150", 	"T153", 	"T156", 	"T159", 	"T162", 	"T165", 	"T168", 	"T171", 	"T174", 	"T177", 	"T180", 	"T183", 	"T186", 	"T189", 	"T192", 	"T195", 	"T198", 	"T201", 	"T204", 	"T207", 	"T210", 	"T213", 	"T216", 	"T219", 	"T222", 	"T225", 	"T228", "T231", "T234", "T237", "T240", "T243", "T246", "T249", "T252", "T255", "T258", "T261", "T264", "T267", "T270", "T273", "T276", "T279", "T282", "T285"]
times 			= 	["500",	"515",	"530",	"545",	"600",	"615",	"630",	"645", 	"700", 	"715", 	"730", 	"745", 	"800", 	"815", 	"830", 	"845", 	"900", 	"915", 	"930", 	"945", 	"1000",	"1015", "1030", "1045", "1100", "1115", "1130", "1145", "1200", "1215", "1230", "1245", "1300", "1315", "1330", "1345", "1400", "1415", "1430", "1445", 	"1500", 	"1515", 	"1530", 	"1545", 	"1600", 	"1615", 	"1630", 	"1645", 	"1700", 	"1715", 	"1730", 	"1745", 	"1800", 	"1815", 	"1830", 	"1845", 	"1900", 	"1915", 	"1930", 	"1945", 	"2000", 	"2015", 	"2030", 	"2045", 	"2100", 	"2115", 	"2130", 	"2145", 	"2200", 	"2215", 	"2230", 	"2245", 	"2300", 	"2315", 	"2330", 	"2345", 	"0", 	"15", 	"30", 	"45", 	"100", 	"115", 	"130", 	"145", 	"200", 	"215", 	"230", 	"245", 	"300", 	"315", 	"330", 	"345", 	"400", 	"415", 	"430", 	"445"]
entWeights 		= 	[0.000867584812850233,	0.00162561078032617,	0.0027560652456038,	0.00426891799377433,	0.00590027234922984,	0.0077884398901218,	0.00990096514550392,	0.0120477644400412,	0.0142045216031207,	0.0165731005257555,	0.0193210572259244,	0.0218290849124919,	0.0235731510503133,	0.0240729550699688,	0.0235482204809098,	0.0216450145584683,	0.0190682015266262,	0.0162749585062886,	0.0141309344747254,	0.0124185243203452,	0.0111536373599164,	0.0101482203679133,	0.00978350133817316,	0.00959748042135389,	0.0094482894538737,	0.00934616012032922,	0.00959445985314406,	0.00982094724785319,	0.0100001251104372,	0.0101184220115829,	0.0104167074635125,	0.0105269590648254,	0.0105642439885388,	0.0105503361418661,	0.0107489981854957,	0.0108454888997824,	0.0109798656770261,	0.0111527389040977,	0.0117381915408086,	0.0122947833624132,	0.0129837973172829,	0.0138139837052937,	0.0152897421559068,	0.0164272395518765,	0.0176978509149184,	0.018884285463044,	0.0210619847657527,	0.0225302945028048,	0.0241663951902797,	0.0251704181844163,	0.026092432971173,	0.0253828551463135,	0.0241332400330555,	0.0221844031326809,	0.020348838887553,	0.0180871355682658,	0.0159053922076925,	0.0140564894455768,	0.012618712753756,	0.0112651864100787,	0.0101388988271727,	0.00930704894344716,	0.00873958505254575,	0.00819769876167465,	0.00774858763280895,	0.00749440491420504,	0.00749288446116329,	0.00753470079354994,	0.00757251229828742,	0.00758823262182501,	0.00766054281117604,	0.00743317596878307,	0.00696888915174808,	0.00635525373450491,	0.00570347367732152,	0.00485595624143592,	0.00386572067538437,	0.00294273905239775,	0.00223774142390938,	0.00165711600371819,	0.00118416310562815,	0.000983924989892111,	0.000894573925802716,	0.000819247534483219,	0.00073861250317592,	0.000683400701919248,	0.000640969397001205,	0.000609731566394685,	0.000561681168780544,	0.000523583123855722,	0.000495047375989374,	0.000464526111258826,	0.000409229903123727,	0.000337157120043757,	0.000251040278097134,	0.000162368414439912]
# Probability of ENTRY at a given time slot
extWeights		=	[0.000179494866468656,	0.000496717444653623,	0.00098913845232102,	0.00180226932206859,	0.00298778280167296,	0.00448035763339177,	0.00626058785462258,	0.00844233173824301,	0.0107203116341413,	0.0130434966209003,	0.0154626956609314,	0.0181638670067372,	0.0207660985549003,	0.0227827509016264,	0.0238210989728908,	0.0238999959228214,	0.0227031206771551,	0.0203913283729109,	0.0177816204193846,	0.0154118129366419,	0.0133728714764288,	0.0117762046152839,	0.0106927885909629,	0.0100491965961806,	0.00971204086910527,	0.0095622889334066,	0.00949667955139675,	0.00964743925768287,	0.00983619754508258,	0.010033647289449,	0.0101727564095039,	0.0103607658026909,	0.0104572576281992,	0.0105309616013121,	0.0105487137199041,	0.0106590732220082,	0.0107506165557882,	0.0108985437381647,	0.0110900955840887,	0.0115414738101451,	0.012040197979367,	0.0127251381712393,	0.0135158720064102,	0.0145254738821151,	0.0156854857695268,	0.0169252040997051,	0.0181879653335823,	0.0198773676629059,	0.0216993532666677,	0.023342351056514,	0.024647056190257,	0.0256141995792419,	0.0255744661818935,	0.0247531566268609,	0.0231994260781796,	0.021436119634218,	0.0193154981551403,	0.0172505426273042,	0.015243935212165,	0.013575284452581,	0.0120690995173672,	0.0108401946889158,	0.00982903073277828,	0.00908139289817356,	0.00848828959811356,	0.00800728252027277,	0.0076653700002467,	0.00758307702042783,	0.0075793350266734,	0.00760843566033945,	0.00763416751449549,	0.00764597580860357,	0.00745259460261124,	0.0071016044026413,	0.00657282701549904,	0.00595092572606813,	0.00521867499985552,	0.00435929680635258,	0.00345091009822492,	0.00265660492582763,	0.00198621429537123,	0.00144746190829958,	0.001105176928988,	0.000936044928035573,	0.00084060614704003,	0.000769117419394646,	0.000706289945277693,	0.000657334157783744,	0.000620353687321886,	0.000578554246138637,	0.000535091404759836,	0.000500564007030934,	0.000476617890491467,	0.000475549678801517,	0.000374487874987738,	0.000284861359646555]
# Probability of EXIT at a given time slot

Ents			=	choices(times, entWeights, k = journeys)
Exts			=	choices(times, extWeights, k = journeys)

numEnts			= 	Counter(Ents)
numExts			= 	Counter(Exts)

#print(numEnts)
#print(numEnts['415'])

tEnts 			= 	[]
tEnts.append(numEnts['500'])
tEnts.append(numEnts['515'])
tEnts.append(numEnts['530'])
tEnts.append(numEnts['545'])
tEnts.append(numEnts['600'])
tEnts.append(numEnts['615'])
tEnts.append(numEnts['630'])
tEnts.append(numEnts['645'])
tEnts.append(numEnts['700'])
tEnts.append(numEnts['715'])
tEnts.append(numEnts['730'])
tEnts.append(numEnts['745'])
tEnts.append(numEnts['800'])
tEnts.append(numEnts['815'])
tEnts.append(numEnts['830'])
tEnts.append(numEnts['845'])
tEnts.append(numEnts['900'])
tEnts.append(numEnts['915'])
tEnts.append(numEnts['930'])
tEnts.append(numEnts['945'])
tEnts.append(numEnts['1000'])
tEnts.append(numEnts['1015'])
tEnts.append(numEnts['1030'])
tEnts.append(numEnts['1045'])
tEnts.append(numEnts['1100'])
tEnts.append(numEnts['1115'])
tEnts.append(numEnts['1130'])
tEnts.append(numEnts['1145'])
tEnts.append(numEnts['1200'])
tEnts.append(numEnts['1215'])
tEnts.append(numEnts['1230'])
tEnts.append(numEnts['1245'])
tEnts.append(numEnts['1300'])
tEnts.append(numEnts['1315'])
tEnts.append(numEnts['1330'])
tEnts.append(numEnts['1345'])
tEnts.append(numEnts['1400'])
tEnts.append(numEnts['1415'])
tEnts.append(numEnts['1430'])
tEnts.append(numEnts['1445'])
tEnts.append(numEnts['1500'])
tEnts.append(numEnts['1515'])
tEnts.append(numEnts['1530'])
tEnts.append(numEnts['1545'])
tEnts.append(numEnts['1600'])
tEnts.append(numEnts['1615'])
tEnts.append(numEnts['1630'])
tEnts.append(numEnts['1645'])
tEnts.append(numEnts['1700'])
tEnts.append(numEnts['1715'])
tEnts.append(numEnts['1730'])
tEnts.append(numEnts['1745'])
tEnts.append(numEnts['1800'])
tEnts.append(numEnts['1815'])
tEnts.append(numEnts['1830'])
tEnts.append(numEnts['1845'])
tEnts.append(numEnts['1900'])
tEnts.append(numEnts['1915'])
tEnts.append(numEnts['1930'])
tEnts.append(numEnts['1945'])
tEnts.append(numEnts['2000'])
tEnts.append(numEnts['2015'])
tEnts.append(numEnts['2030'])
tEnts.append(numEnts['2045'])
tEnts.append(numEnts['2100'])
tEnts.append(numEnts['2115'])
tEnts.append(numEnts['2130'])
tEnts.append(numEnts['2145'])
tEnts.append(numEnts['2200'])
tEnts.append(numEnts['2215'])
tEnts.append(numEnts['2230'])
tEnts.append(numEnts['2245'])
tEnts.append(numEnts['2300'])
tEnts.append(numEnts['2315'])
tEnts.append(numEnts['2330'])
tEnts.append(numEnts['2345'])
tEnts.append(numEnts['0'])
tEnts.append(numEnts['15'])
tEnts.append(numEnts['30'])
tEnts.append(numEnts['45'])
tEnts.append(numEnts['100'])
tEnts.append(numEnts['115'])
tEnts.append(numEnts['130'])
tEnts.append(numEnts['145'])
tEnts.append(numEnts['200'])
tEnts.append(numEnts['215'])
tEnts.append(numEnts['230'])
tEnts.append(numEnts['245'])
tEnts.append(numEnts['300'])
tEnts.append(numEnts['315'])
tEnts.append(numEnts['330'])
tEnts.append(numEnts['345'])
tEnts.append(numEnts['400'])
tEnts.append(numEnts['415'])
tEnts.append(numEnts['430'])
tEnts.append(numEnts['445'])

#print(tEnts)

i = 0

while i <= 95:
	combined.append(timestamps[i])
	combined.append(int(times[i]))
	combined.append(tEnts[i])
	#combined.append(entWeights[i])
	#combined.append(extWeights[i])
	i = i+1
	pass
# gives: ["T#", T, n, p[Ent(t)], p[Ext(t)] {repeat}]
#print("combined", combined)

Lats   =    []
Longs  =    []

pET0 =    []
pET3 =    []
pET6 =    []
pET9 =    []
pET12 =    []
pET15 =    []
pET18 =    []
pET21 =    []
pET24 =    []
pET27 =    []
pET30 =    []
pET33 =    []
pET36 =    []
pET39 =    []
pET42 =    []
pET45 =    []
pET48 =    []
pET51 =    []
pET54 =    []
pET57 =    []
pET60 =    []
pET63 =    []
pET66 =    []
pET69 =    []
pET72 =    []
pET75 =    []
pET78 =    []
pET81 =    []
pET84 =    []
pET87 =    []
pET90 =    []
pET93 =    []
pET96 =    []
pET99 =    []
pET102 =    []
pET105 =    []
pET108 =    []
pET111 =    []
pET114 =    []
pET117 =    []
pET120 =    []
pET123 =    []
pET126 =    []
pET129 =    []
pET132 =    []
pET135 =    []
pET138 =    []
pET141 =    []
pET144 =    []
pET147 =    []
pET150 =    []
pET153 =    []
pET156 =    []
pET159 =    []
pET162 =    []
pET165 =    []
pET168 =    []
pET171 =    []
pET174 =    []
pET177 =    []
pET180 =    []
pET183 =    []
pET186 =    []
pET189 =    []
pET192 =    []
pET195 =    []
pET198 =    []
pET201 =    []
pET204 =    []
pET207 =    []
pET210 =    []
pET213 =    []
pET216 =    []
pET219 =    []
pET222 =    []
pET225 =    []
pET228 =    []
pET231 =    []
pET234 =    []
pET237 =    []
pET240 =    []
pET243 =    []
pET246 =    []
pET249 =    []
pET252 =    []
pET255 =    []
pET258 =    []
pET261 =    []
pET264 =    []
pET267 =    []
pET270 =    []
pET273 =    []
pET276 =    []
pET279 =    []
pET282 =    []
pET285 =    []

pXT0 =    []
pXT3 =    []
pXT6 =    []
pXT9 =    []
pXT12 =    []
pXT15 =    []
pXT18 =    []
pXT21 =    []
pXT24 =    []
pXT27 =    []
pXT30 =    []
pXT33 =    []
pXT36 =    []
pXT39 =    []
pXT42 =    []
pXT45 =    []
pXT48 =    []
pXT51 =    []
pXT54 =    []
pXT57 =    []
pXT60 =    []
pXT63 =    []
pXT66 =    []
pXT69 =    []
pXT72 =    []
pXT75 =    []
pXT78 =    []
pXT81 =    []
pXT84 =    []
pXT87 =    []
pXT90 =    []
pXT93 =    []
pXT96 =    []
pXT99 =    []
pXT102 =    []
pXT105 =    []
pXT108 =    []
pXT111 =    []
pXT114 =    []
pXT117 =    []
pXT120 =    []
pXT123 =    []
pXT126 =    []
pXT129 =    []
pXT132 =    []
pXT135 =    []
pXT138 =    []
pXT141 =    []
pXT144 =    []
pXT147 =    []
pXT150 =    []
pXT153 =    []
pXT156 =    []
pXT159 =    []
pXT162 =    []
pXT165 =    []
pXT168 =    []
pXT171 =    []
pXT174 =    []
pXT177 =    []
pXT180 =    []
pXT183 =    []
pXT186 =    []
pXT189 =    []
pXT192 =    []
pXT195 =    []
pXT198 =    []
pXT201 =    []
pXT204 =    []
pXT207 =    []
pXT210 =    []
pXT213 =    []
pXT216 =    []
pXT219 =    []
pXT222 =    []
pXT225 =    []
pXT228 =    []
pXT231 =    []
pXT234 =    []
pXT237 =    []
pXT240 =    []
pXT243 =    []
pXT246 =    []
pXT249 =    []
pXT252 =    []
pXT255 =    []
pXT258 =    []
pXT261 =    []
pXT264 =    []
pXT267 =    []
pXT270 =    []
pXT273 =    []
pXT276 =    []
pXT279 =    []
pXT282 =    []
pXT285 =    []


NAMES  =	[]

with open('FRY_Fracs_FULL_ENTRY.csv', 'r') as csv_file:
	csv_reader	=	csv.reader(csv_file)

	for line in csv_reader:
		NLC		= 	line[0]
		ASC 	= 	line[1]
		NAME	= 	line[2]

		pEntT0 	= 	line[3]
		pEntT3	= 	line[4]
		pEntT6	= 	line[5]
		pEntT9	= 	line[6]
		pEntT12	= 	line[7]
		pEntT15	= 	line[8]
		pEntT18	= 	line[9]
		pEntT21	= 	line[10]
		pEntT24	= 	line[11]
		pEntT27	= 	line[12]
		pEntT30	= 	line[13]
		pEntT33	= 	line[14]
		pEntT36	= 	line[15]
		pEntT39	= 	line[16]
		pEntT42	= 	line[17]
		pEntT45	= 	line[18]
		pEntT48	= 	line[19]
		pEntT51	= 	line[20]
		pEntT54	= 	line[21]
		pEntT57	= 	line[22]
		pEntT60	= 	line[23]
		pEntT63	= 	line[24]
		pEntT66	= 	line[25]
		pEntT69	= 	line[26]
		pEntT72	= 	line[27]
		pEntT75	= 	line[28]
		pEntT78	= 	line[29]
		pEntT81	= 	line[30]
		pEntT84	= 	line[31]
		pEntT87	= 	line[32]
		pEntT90	= 	line[33]
		pEntT93	= 	line[34]
		pEntT96	= 	line[35]
		pEntT99	= 	line[36]
		pEntT102	= 	line[37]
		pEntT105	= 	line[38]
		pEntT108	= 	line[39]
		pEntT111	= 	line[40]
		pEntT114	= 	line[41]
		pEntT117	= 	line[42]
		pEntT120	= 	line[43]
		pEntT123	= 	line[44]
		pEntT126	= 	line[45]
		pEntT129	= 	line[46]
		pEntT132	= 	line[47]
		pEntT135	= 	line[48]
		pEntT138	= 	line[49]
		pEntT141	= 	line[50]
		pEntT144	= 	line[51]
		pEntT147	= 	line[52]
		pEntT150	= 	line[53]
		pEntT153	= 	line[54]
		pEntT156	= 	line[55]
		pEntT159	= 	line[56]
		pEntT162	= 	line[57]
		pEntT165	= 	line[58]
		pEntT168	= 	line[59]
		pEntT171	= 	line[60]
		pEntT174	= 	line[61]
		pEntT177	= 	line[62]
		pEntT180	= 	line[63]
		pEntT183	= 	line[64]
		pEntT186	= 	line[65]
		pEntT189	= 	line[66]
		pEntT192	= 	line[67]
		pEntT195	= 	line[68]
		pEntT198	= 	line[69]
		pEntT201	= 	line[70]
		pEntT204	= 	line[71]
		pEntT207	= 	line[72]
		pEntT210	= 	line[73]
		pEntT213	= 	line[74]
		pEntT216	= 	line[75]
		pEntT219	= 	line[76]
		pEntT222	= 	line[77]
		pEntT225	= 	line[78]
		pEntT228	= 	line[79]
		pEntT231	= 	line[80]
		pEntT234	= 	line[81]
		pEntT237	= 	line[82]
		pEntT240	= 	line[83]
		pEntT243	= 	line[84]
		pEntT246	= 	line[85]
		pEntT249	= 	line[86]
		pEntT252	= 	line[87]
		pEntT255	= 	line[88]
		pEntT258	= 	line[89]
		pEntT261	= 	line[90]
		pEntT264	= 	line[91]
		pEntT267	= 	line[92]
		pEntT270	= 	line[93]
		pEntT273	= 	line[94]
		pEntT276	= 	line[95]
		pEntT279	= 	line[96]
		pEntT282	= 	line[97]
		pEntT285	= 	line[98]

		Lat			= 	line[99]
		Long		= 	line[100]

		NAMES.append(NAME)
		Lats.append(float(Lat))
		Longs.append(float(Long))
		pET0.append(float(pEntT0))
		pET3.append(float(pEntT3))
		pET6.append(float(pEntT6))
		pET9.append(float(pEntT9))
		pET12.append(float(pEntT12))
		pET15.append(float(pEntT15))
		pET18.append(float(pEntT18))
		pET21.append(float(pEntT21))
		pET24.append(float(pEntT24))
		pET27.append(float(pEntT27))
		pET30.append(float(pEntT30))
		pET33.append(float(pEntT33))
		pET36.append(float(pEntT36))
		pET39.append(float(pEntT39))
		pET42.append(float(pEntT42))
		pET45.append(float(pEntT45))
		pET48.append(float(pEntT48))
		pET51.append(float(pEntT51))
		pET54.append(float(pEntT54))
		pET57.append(float(pEntT57))
		pET60.append(float(pEntT60))
		pET63.append(float(pEntT63))
		pET66.append(float(pEntT66))
		pET69.append(float(pEntT69))
		pET72.append(float(pEntT72))
		pET75.append(float(pEntT75))
		pET78.append(float(pEntT78))
		pET81.append(float(pEntT81))
		pET84.append(float(pEntT84))
		pET87.append(float(pEntT87))
		pET90.append(float(pEntT90))
		pET93.append(float(pEntT93))
		pET96.append(float(pEntT96))
		pET99.append(float(pEntT99))
		pET102.append(float(pEntT102))
		pET105.append(float(pEntT105))
		pET108.append(float(pEntT108))
		pET111.append(float(pEntT111))
		pET114.append(float(pEntT114))
		pET117.append(float(pEntT117))
		pET120.append(float(pEntT120))
		pET123.append(float(pEntT123))
		pET126.append(float(pEntT126))
		pET129.append(float(pEntT129))
		pET132.append(float(pEntT132))
		pET135.append(float(pEntT135))
		pET138.append(float(pEntT138))
		pET141.append(float(pEntT141))
		pET144.append(float(pEntT144))
		pET147.append(float(pEntT147))
		pET150.append(float(pEntT150))
		pET153.append(float(pEntT153))
		pET156.append(float(pEntT156))
		pET159.append(float(pEntT159))
		pET162.append(float(pEntT162))
		pET165.append(float(pEntT165))
		pET168.append(float(pEntT168))
		pET171.append(float(pEntT171))
		pET174.append(float(pEntT174))
		pET177.append(float(pEntT177))
		pET180.append(float(pEntT180))
		pET183.append(float(pEntT183))
		pET186.append(float(pEntT186))
		pET189.append(float(pEntT189))
		pET192.append(float(pEntT192))
		pET195.append(float(pEntT195))
		pET198.append(float(pEntT198))
		pET201.append(float(pEntT201))
		pET204.append(float(pEntT204))
		pET207.append(float(pEntT207))
		pET210.append(float(pEntT210))
		pET213.append(float(pEntT213))
		pET216.append(float(pEntT216))
		pET219.append(float(pEntT219))
		pET222.append(float(pEntT222))
		pET225.append(float(pEntT225))
		pET228.append(float(pEntT228))
		pET231.append(float(pEntT231))
		pET234.append(float(pEntT234))
		pET237.append(float(pEntT237))
		pET240.append(float(pEntT240))
		pET243.append(float(pEntT243))
		pET246.append(float(pEntT246))
		pET249.append(float(pEntT249))
		pET252.append(float(pEntT252))
		pET255.append(float(pEntT255))
		pET258.append(float(pEntT258))
		pET261.append(float(pEntT261))
		pET264.append(float(pEntT264))
		pET267.append(float(pEntT267))
		pET270.append(float(pEntT270))
		pET273.append(float(pEntT273))
		pET276.append(float(pEntT276))
		pET279.append(float(pEntT279))
		pET282.append(float(pEntT282))
		pET285.append(float(pEntT285))
		pass



with open('FRY_Fracs_FULL_EXIT.csv', 'r') as csv_file:
	csv_reader	=	csv.reader(csv_file)

	for line in csv_reader:
		pExtT0 	= 	line[3]
		pExtT3	= 	line[4]
		pExtT6	= 	line[5]
		pExtT9	= 	line[6]
		pExtT12	= 	line[7]
		pExtT15	= 	line[8]
		pExtT18	= 	line[9]
		pExtT21	= 	line[10]
		pExtT24	= 	line[11]
		pExtT27	= 	line[12]
		pExtT30	= 	line[13]
		pExtT33	= 	line[14]
		pExtT36	= 	line[15]
		pExtT39	= 	line[16]
		pExtT42	= 	line[17]
		pExtT45	= 	line[18]
		pExtT48	= 	line[19]
		pExtT51	= 	line[20]
		pExtT54	= 	line[21]
		pExtT57	= 	line[22]
		pExtT60	= 	line[23]
		pExtT63	= 	line[24]
		pExtT66	= 	line[25]
		pExtT69	= 	line[26]
		pExtT72	= 	line[27]
		pExtT75	= 	line[28]
		pExtT78	= 	line[29]
		pExtT81	= 	line[30]
		pExtT84	= 	line[31]
		pExtT87	= 	line[32]
		pExtT90	= 	line[33]
		pExtT93	= 	line[34]
		pExtT96	= 	line[35]
		pExtT99	= 	line[36]
		pExtT102	= 	line[37]
		pExtT105	= 	line[38]
		pExtT108	= 	line[39]
		pExtT111	= 	line[40]
		pExtT114	= 	line[41]
		pExtT117	= 	line[42]
		pExtT120	= 	line[43]
		pExtT123	= 	line[44]
		pExtT126	= 	line[45]
		pExtT129	= 	line[46]
		pExtT132	= 	line[47]
		pExtT135	= 	line[48]
		pExtT138	= 	line[49]
		pExtT141	= 	line[50]
		pExtT144	= 	line[51]
		pExtT147	= 	line[52]
		pExtT150	= 	line[53]
		pExtT153	= 	line[54]
		pExtT156	= 	line[55]
		pExtT159	= 	line[56]
		pExtT162	= 	line[57]
		pExtT165	= 	line[58]
		pExtT168	= 	line[59]
		pExtT171	= 	line[60]
		pExtT174	= 	line[61]
		pExtT177	= 	line[62]
		pExtT180	= 	line[63]
		pExtT183	= 	line[64]
		pExtT186	= 	line[65]
		pExtT189	= 	line[66]
		pExtT192	= 	line[67]
		pExtT195	= 	line[68]
		pExtT198	= 	line[69]
		pExtT201	= 	line[70]
		pExtT204	= 	line[71]
		pExtT207	= 	line[72]
		pExtT210	= 	line[73]
		pExtT213	= 	line[74]
		pExtT216	= 	line[75]
		pExtT219	= 	line[76]
		pExtT222	= 	line[77]
		pExtT225	= 	line[78]
		pExtT228	= 	line[79]
		pExtT231	= 	line[80]
		pExtT234	= 	line[81]
		pExtT237	= 	line[82]
		pExtT240	= 	line[83]
		pExtT243	= 	line[84]
		pExtT246	= 	line[85]
		pExtT249	= 	line[86]
		pExtT252	= 	line[87]
		pExtT255	= 	line[88]
		pExtT258	= 	line[89]
		pExtT261	= 	line[90]
		pExtT264	= 	line[91]
		pExtT267	= 	line[92]
		pExtT270	= 	line[93]
		pExtT273	= 	line[94]
		pExtT276	= 	line[95]
		pExtT279	= 	line[96]
		pExtT282	= 	line[97]
		pExtT285	= 	line[98]

		pXT0.append(float(pExtT0))
		pXT3.append(float(pExtT3))
		pXT6.append(float(pExtT6))
		pXT9.append(float(pExtT9))
		pXT12.append(float(pExtT12))
		pXT15.append(float(pExtT15))
		pXT18.append(float(pExtT18))
		pXT21.append(float(pExtT21))
		pXT24.append(float(pExtT24))
		pXT27.append(float(pExtT27))
		pXT30.append(float(pExtT30))
		pXT33.append(float(pExtT33))
		pXT36.append(float(pExtT36))
		pXT39.append(float(pExtT39))
		pXT42.append(float(pExtT42))
		pXT45.append(float(pExtT45))
		pXT48.append(float(pExtT48))
		pXT51.append(float(pExtT51))
		pXT54.append(float(pExtT54))
		pXT57.append(float(pExtT57))
		pXT60.append(float(pExtT60))
		pXT63.append(float(pExtT63))
		pXT66.append(float(pExtT66))
		pXT69.append(float(pExtT69))
		pXT72.append(float(pExtT72))
		pXT75.append(float(pExtT75))
		pXT78.append(float(pExtT78))
		pXT81.append(float(pExtT81))
		pXT84.append(float(pExtT84))
		pXT87.append(float(pExtT87))
		pXT90.append(float(pExtT90))
		pXT93.append(float(pExtT93))
		pXT96.append(float(pExtT96))
		pXT99.append(float(pExtT99))
		pXT102.append(float(pExtT102))
		pXT105.append(float(pExtT105))
		pXT108.append(float(pExtT108))
		pXT111.append(float(pExtT111))
		pXT114.append(float(pExtT114))
		pXT117.append(float(pExtT117))
		pXT120.append(float(pExtT120))
		pXT123.append(float(pExtT123))
		pXT126.append(float(pExtT126))
		pXT129.append(float(pExtT129))
		pXT132.append(float(pExtT132))
		pXT135.append(float(pExtT135))
		pXT138.append(float(pExtT138))
		pXT141.append(float(pExtT141))
		pXT144.append(float(pExtT144))
		pXT147.append(float(pExtT147))
		pXT150.append(float(pExtT150))
		pXT153.append(float(pExtT153))
		pXT156.append(float(pExtT156))
		pXT159.append(float(pExtT159))
		pXT162.append(float(pExtT162))
		pXT165.append(float(pExtT165))
		pXT168.append(float(pExtT168))
		pXT171.append(float(pExtT171))
		pXT174.append(float(pExtT174))
		pXT177.append(float(pExtT177))
		pXT180.append(float(pExtT180))
		pXT183.append(float(pExtT183))
		pXT186.append(float(pExtT186))
		pXT189.append(float(pExtT189))
		pXT192.append(float(pExtT192))
		pXT195.append(float(pExtT195))
		pXT198.append(float(pExtT198))
		pXT201.append(float(pExtT201))
		pXT204.append(float(pExtT204))
		pXT207.append(float(pExtT207))
		pXT210.append(float(pExtT210))
		pXT213.append(float(pExtT213))
		pXT216.append(float(pExtT216))
		pXT219.append(float(pExtT219))
		pXT222.append(float(pExtT222))
		pXT225.append(float(pExtT225))
		pXT228.append(float(pExtT228))
		pXT231.append(float(pExtT231))
		pXT234.append(float(pExtT234))
		pXT237.append(float(pExtT237))
		pXT240.append(float(pExtT240))
		pXT243.append(float(pExtT243))
		pXT246.append(float(pExtT246))
		pXT249.append(float(pExtT249))
		pXT252.append(float(pExtT252))
		pXT255.append(float(pExtT255))
		pXT258.append(float(pExtT258))
		pXT261.append(float(pExtT261))
		pXT264.append(float(pExtT264))
		pXT267.append(float(pExtT267))
		pXT270.append(float(pExtT270))
		pXT273.append(float(pExtT273))
		pXT276.append(float(pExtT276))
		pXT279.append(float(pExtT279))
		pXT282.append(float(pExtT282))
		pXT285.append(float(pExtT285))
		pass


pET 	= 	[pET0, 	pET3, 	pET6, 	pET9, 	pET12, 	pET15, 	pET18, 	pET21, 	pET24, 	pET27, 	pET30, 	pET33, 	pET36, 	pET39, 	pET42, 	pET45, 	pET48, 	pET51, 	pET54, 	pET57, 	pET60, 	pET63, 	pET66, 	pET69, 	pET72, 	pET75, 	pET78, 	pET81, 	pET84, 	pET87, 	pET90, 	pET93, 	pET96, 	pET99, 	pET102, 	pET105, 	pET108, 	pET111, 	pET114, 	pET117, 	pET120, 	pET123, 	pET126, 	pET129, 	pET132, 	pET135, 	pET138, 	pET141, 	pET144, 	pET147, 	pET150, 	pET153, 	pET156, 	pET159, 	pET162, 	pET165, 	pET168, 	pET171, 	pET174, 	pET177, 	pET180, 	pET183, 	pET186, 	pET189, 	pET192, 	pET195, 	pET198, 	pET201, 	pET204, 	pET207, 	pET210, 	pET213, 	pET216, 	pET219, 	pET222, 	pET225, 	pET228, 	pET231, 	pET234, 	pET237, 	pET240, 	pET243, 	pET246, 	pET249, 	pET252, 	pET255, 	pET258, 	pET261, 	pET264, 	pET267, 	pET270, 	pET273, 	pET276, 	pET279, 	pET282, 	pET285]
pXT 	= 	[pXT0, 	pXT3, 	pXT6, 	pXT9, 	pXT12, 	pXT15, 	pXT18, 	pXT21, 	pXT24, 	pXT27, 	pXT30, 	pXT33, 	pXT36, 	pXT39, 	pXT42, 	pXT45, 	pXT48, 	pXT51, 	pXT54, 	pXT57, 	pXT60, 	pXT63, 	pXT66, 	pXT69, 	pXT72, 	pXT75, 	pXT78, 	pXT81, 	pXT84, 	pXT87, 	pXT90, 	pXT93, 	pXT96, 	pXT99, 	pXT102, 	pXT105, 	pXT108, 	pXT111, 	pXT114, 	pXT117, 	pXT120, 	pXT123, 	pXT126, 	pXT129, 	pXT132, 	pXT135, 	pXT138, 	pXT141, 	pXT144, 	pXT147, 	pXT150, 	pXT153, 	pXT156, 	pXT159, 	pXT162, 	pXT165, 	pXT168, 	pXT171, 	pXT174, 	pXT177, 	pXT180, 	pXT183, 	pXT186, 	pXT189, 	pXT192, 	pXT195, 	pXT198, 	pXT201, 	pXT204, 	pXT207, 	pXT210, 	pXT213, 	pXT216, 	pXT219, 	pXT222, 	pXT225, 	pXT228, 	pXT231, 	pXT234, 	pXT237, 	pXT240, 	pXT243, 	pXT246, 	pXT249, 	pXT252, 	pXT255, 	pXT258, 	pXT261, 	pXT264, 	pXT267, 	pXT270, 	pXT273, 	pXT276, 	pXT279, 	pXT282, 	pXT285]
#print(pET[0][0])	#	First reference [i] = timestamp of entry probabilities for all stations
#print(pXT[0][0])	#	Second reference [j] = station exit probability

#combined	=	["T#", T, n {repeat}]
#pET 		=	[[All entry probabilities for time T0], [All entry probabilities for time T3], ...]
#pXT 		=	[[All exit probabilities for time T0], [All exit probabilities for time T3], ...]

TNP		=	[]

j = 0

while j <= 95:
	k = 0
	while k <=2:
		TNP.append(combined[3*j+k])
		k = k+1
		pass
	TNP.append(pET[j])
	TNP.append(pXT[j])
	j = j+1
	pass
#print("pET[0]", pET[0])
 
# gives: ["T#", T, n, pdistE, pdistX {repeat}]
#print("TNP", TNP)
#print("len(TNP)", len(TNP))
"""
print("NAMES", NAMES)
print("NAMES[416]", NAMES[416])
print("len(TNP[3])", len(TNP[3]))
print("len(NAMES)", len(NAMES))
print("len(TNP[3])", len(TNP[3]))
"""

# TNP = [(0),	(1),	(2),	(3),		(4),		(5),	(6),	(7),	(8),		(9),		(10),		(11),	(12),	(13),		(14)... ]
# TNP = ["T#0",	T0,		n0,		pdistE0,	pdistX0,	"T#1",	T1,		n1,		pdistE1,	pdistX1,	"T#2",		T2,		n2,		pdistE2,	pdistX2... ]

# aJs = [(0),	(1),	(2),	(3),		(4),				(5),	(6),	(7),	(8),		(9),				(10),		(11),	(12),	(13),		(14)... ]
# aJs = ["T#0",	T0,		n0,		[jSts0],	[jEns0],			"T#1",	T1,		n1,		[jSts1],	[jEns1],			"T#2",		T2,		n2,		[jSts2],	[jEns2]... ]

aJs		=	[]
aJsS	=	[]
aJsE	=	[]

l = 0

#print("TNP[2]", TNP[2])

while l <= 0: #95
	m = 0
	while m <=2:
		aJs.append(TNP[5*l + m])
		m = m+1
		n = 0
		pass
	while n <= 5: #95
		JSts = choices(NAMES, TNP[5*n + 3], k = TNP[5*n + 2])
		JEns = choices(NAMES, TNP[5*n + 4], k = TNP[5*n + 2])
		
		#aJsS.append(k)
		#aJsE.append(k)

		aJsS.append([JSts])
		aJsE.append([JEns])

		journeystarts 	= 	Counter(JSts)
		journeyends 	= 	Counter(JEns)

		starts			=	[]
		ends			=	[]

		starts.append(journeystarts["Abbey Road"])
		starts.append(journeystarts["Acton Central"])
		starts.append(journeystarts["Acton Main Line"])
		starts.append(journeystarts["Acton Town"])
		starts.append(journeystarts["Aldgate"])
		starts.append(journeystarts["Aldgate East"])
		starts.append(journeystarts["All Saints"])
		starts.append(journeystarts["Alperton"])
		starts.append(journeystarts["Amersham"])
		starts.append(journeystarts["Anerley"])
		starts.append(journeystarts["Angel"])
		starts.append(journeystarts["Archway"])
		starts.append(journeystarts["Arnos Grove"])
		starts.append(journeystarts["Arsenal"])
		starts.append(journeystarts["Baker Street"])
		starts.append(journeystarts["Balham LU"])
		starts.append(journeystarts["Bank and Monument"])
		starts.append(journeystarts["Barbican"])
		starts.append(journeystarts["Barking"])
		starts.append(journeystarts["Barkingside"])
		starts.append(journeystarts["Barons Court"])
		starts.append(journeystarts["Battersea Park"])
		starts.append(journeystarts["Bayswater"])
		starts.append(journeystarts["Beckton"])
		starts.append(journeystarts["Beckton Park"])
		starts.append(journeystarts["Becontree"])
		starts.append(journeystarts["Belsize Park"])
		starts.append(journeystarts["Bermondsey"])
		starts.append(journeystarts["Bethnal Green LO"])
		starts.append(journeystarts["Bethnal Green LU"])
		starts.append(journeystarts["Blackfriars LU"])
		starts.append(journeystarts["Blackhorse Road"])
		starts.append(journeystarts["Blackwall"])
		starts.append(journeystarts["Bond Street"])
		starts.append(journeystarts["Borough"])
		starts.append(journeystarts["Boston Manor"])
		starts.append(journeystarts["Bounds Green"])
		starts.append(journeystarts["Bow Church"])
		starts.append(journeystarts["Bow Road"])
		starts.append(journeystarts["Brent Cross"])
		starts.append(journeystarts["Brentwood"])
		starts.append(journeystarts["Brixton LU"])
		starts.append(journeystarts["Brockley"])
		starts.append(journeystarts["Bromley-by-Bow"])
		starts.append(journeystarts["Brondesbury"])
		starts.append(journeystarts["Brondesbury Park"])
		starts.append(journeystarts["Bruce Grove"])
		starts.append(journeystarts["Buckhurst Hill"])
		starts.append(journeystarts["Burnt Oak"])
		starts.append(journeystarts["Bush Hill Park"])
		starts.append(journeystarts["Bushey"])
		starts.append(journeystarts["Caledonian Road"])
		starts.append(journeystarts["Caledonian Road & Barnsbury"])
		starts.append(journeystarts["Cambridge Heath"])
		starts.append(journeystarts["Camden Road"])
		starts.append(journeystarts["Camden Town"])
		starts.append(journeystarts["Canada Water"])
		starts.append(journeystarts["Canary Wharf DLR"])
		starts.append(journeystarts["Canary Wharf LU"])
		starts.append(journeystarts["Canning Town"])
		starts.append(journeystarts["Cannon Street LU"])
		starts.append(journeystarts["Canonbury"])
		starts.append(journeystarts["Canons Park"])
		starts.append(journeystarts["Carpenders Park"])
		starts.append(journeystarts["Chadwell Heath"])
		starts.append(journeystarts["Chalfont & Latimer"])
		starts.append(journeystarts["Chalk Farm"])
		starts.append(journeystarts["Chancery Lane"])
		starts.append(journeystarts["Charing Cross LU"])
		starts.append(journeystarts["Chesham"])
		starts.append(journeystarts["Cheshunt"])
		starts.append(journeystarts["Chigwell"])
		starts.append(journeystarts["Chingford"])
		starts.append(journeystarts["Chiswick Park"])
		starts.append(journeystarts["Chorleywood"])
		starts.append(journeystarts["Clapham Common"])
		starts.append(journeystarts["Clapham High Street"])
		starts.append(journeystarts["Clapham Junction"])
		starts.append(journeystarts["Clapham North"])
		starts.append(journeystarts["Clapham South"])
		starts.append(journeystarts["Clapton"])
		starts.append(journeystarts["Cockfosters"])
		starts.append(journeystarts["Colindale"])
		starts.append(journeystarts["Colliers Wood"])
		starts.append(journeystarts["Covent Garden"])
		starts.append(journeystarts["Crossharbour"])
		starts.append(journeystarts["Crouch Hill"])
		starts.append(journeystarts["Croxley"])
		starts.append(journeystarts["Crystal Palace"])
		starts.append(journeystarts["Custom House"])
		starts.append(journeystarts["Cutty Sark"])
		starts.append(journeystarts["Cyprus"])
		starts.append(journeystarts["Dagenham East"])
		starts.append(journeystarts["Dagenham Heathway"])
		starts.append(journeystarts["Dalston Junction"])
		starts.append(journeystarts["Dalston Kingsland"])
		starts.append(journeystarts["Debden"])
		starts.append(journeystarts["Denmark Hill"])
		starts.append(journeystarts["Deptford Bridge"])
		starts.append(journeystarts["Devons Road"])
		starts.append(journeystarts["Dollis Hill"])
		starts.append(journeystarts["Ealing Broadway"])
		starts.append(journeystarts["Ealing Common"])
		starts.append(journeystarts["Earl's Court"])
		starts.append(journeystarts["East Acton"])
		starts.append(journeystarts["East Finchley"])
		starts.append(journeystarts["East Ham"])
		starts.append(journeystarts["East India"])
		starts.append(journeystarts["East Putney"])
		starts.append(journeystarts["Eastcote"])
		starts.append(journeystarts["Edgware"])
		starts.append(journeystarts["Edgware Road (Bak)"])
		starts.append(journeystarts["Edgware Road (DIS)"])
		starts.append(journeystarts["Edmonton Green"])
		starts.append(journeystarts["Elephant & Castle LU"])
		starts.append(journeystarts["Elm Park"])
		starts.append(journeystarts["Elverson Road"])
		starts.append(journeystarts["Embankment"])
		starts.append(journeystarts["Emerson Park"])
		starts.append(journeystarts["Enfield Town"])
		starts.append(journeystarts["Epping"])
		starts.append(journeystarts["Euston LU"])
		starts.append(journeystarts["Euston NR"])
		starts.append(journeystarts["Euston Square"])
		starts.append(journeystarts["Fairlop"])
		starts.append(journeystarts["Farringdon"])
		starts.append(journeystarts["Finchley Central"])
		starts.append(journeystarts["Finchley Road"])
		starts.append(journeystarts["Finchley Road & Frognal"])
		starts.append(journeystarts["Finsbury Park LU"])
		starts.append(journeystarts["Finsbury Park NR"])
		starts.append(journeystarts["Forest Gate"])
		starts.append(journeystarts["Forest Hill"])
		starts.append(journeystarts["Fulham Broadway"])
		starts.append(journeystarts["Gallions Reach"])
		starts.append(journeystarts["Gants Hill"])
		starts.append(journeystarts["Gidea Park"])
		starts.append(journeystarts["Gloucester Road"])
		starts.append(journeystarts["Golders Green"])
		starts.append(journeystarts["Goldhawk Road"])
		starts.append(journeystarts["Goodge Street"])
		starts.append(journeystarts["Goodmayes"])
		starts.append(journeystarts["Gospel Oak"])
		starts.append(journeystarts["Grange Hill"])
		starts.append(journeystarts["Great Portland Street"])
		starts.append(journeystarts["Green Park"])
		starts.append(journeystarts["Greenford"])
		starts.append(journeystarts["Greenwich"])
		starts.append(journeystarts["Gunnersbury"])
		starts.append(journeystarts["Hackney Central"])
		starts.append(journeystarts["Hackney Downs"])
		starts.append(journeystarts["Hackney Wick"])
		starts.append(journeystarts["Haggerston"])
		starts.append(journeystarts["Hainault"])
		starts.append(journeystarts["Hammersmith (DIS)"])
		starts.append(journeystarts["Hammersmith (H&C)"])
		starts.append(journeystarts["Hampstead"])
		starts.append(journeystarts["Hampstead Heath"])
		starts.append(journeystarts["Hanger Lane"])
		starts.append(journeystarts["Hanwell"])
		starts.append(journeystarts["Harlesden"])
		starts.append(journeystarts["Harold Wood"])
		starts.append(journeystarts["Harringay Green Lanes"])
		starts.append(journeystarts["Harrow & Wealdstone"])
		starts.append(journeystarts["Harrow-on-the-Hill"])
		starts.append(journeystarts["Hatch End"])
		starts.append(journeystarts["Hatton Cross"])
		starts.append(journeystarts["Hayes & Harlington"])
		starts.append(journeystarts["Headstone Lane"])
		starts.append(journeystarts["Heathrow Terminal 4 EL"])
		starts.append(journeystarts["Heathrow Terminal 4 LU"])
		starts.append(journeystarts["Heathrow Terminal 5 LU"])
		starts.append(journeystarts["Heathrow Terminals 123 LU"])
		starts.append(journeystarts["Heathrow Terminals 2 & 3 EL"])
		starts.append(journeystarts["Hendon Central"])
		starts.append(journeystarts["Heron Quays"])
		starts.append(journeystarts["High Barnet"])
		starts.append(journeystarts["High Street Kensington"])
		starts.append(journeystarts["Highams Park"])
		starts.append(journeystarts["Highbury & Islington"])
		starts.append(journeystarts["Highgate"])
		starts.append(journeystarts["Hillingdon"])
		starts.append(journeystarts["Holborn"])
		starts.append(journeystarts["Holland Park"])
		starts.append(journeystarts["Holloway Road"])
		starts.append(journeystarts["Homerton"])
		starts.append(journeystarts["Honor Oak Park"])
		starts.append(journeystarts["Hornchurch"])
		starts.append(journeystarts["Hounslow Central"])
		starts.append(journeystarts["Hounslow East"])
		starts.append(journeystarts["Hounslow West"])
		starts.append(journeystarts["Hoxton"])
		starts.append(journeystarts["Hyde Park Corner"])
		starts.append(journeystarts["Ickenham"])
		starts.append(journeystarts["Ilford"])
		starts.append(journeystarts["Imperial Wharf"])
		starts.append(journeystarts["Island Gardens"])
		starts.append(journeystarts["Kennington"])
		starts.append(journeystarts["Kensal Green"])
		starts.append(journeystarts["Kensal Rise"])
		starts.append(journeystarts["Kensington (Olympia)"])
		starts.append(journeystarts["Kentish Town"])
		starts.append(journeystarts["Kentish Town West"])
		starts.append(journeystarts["Kenton"])
		starts.append(journeystarts["Kew Gardens"])
		starts.append(journeystarts["Kilburn"])
		starts.append(journeystarts["Kilburn High Road"])
		starts.append(journeystarts["Kilburn Park"])
		starts.append(journeystarts["King George V"])
		starts.append(journeystarts["King's Cross St. Pancras"])
		starts.append(journeystarts["Kingsbury"])
		starts.append(journeystarts["Knightsbridge"])
		starts.append(journeystarts["Ladbroke Grove"])
		starts.append(journeystarts["Lambeth North"])
		starts.append(journeystarts["Lancaster Gate"])
		starts.append(journeystarts["Langdon Park"])
		starts.append(journeystarts["Latimer Road"])
		starts.append(journeystarts["Leicester Square"])
		starts.append(journeystarts["Lewisham DLR"])
		starts.append(journeystarts["Leyton"])
		starts.append(journeystarts["Leyton Midland Road"])
		starts.append(journeystarts["Leytonstone"])
		starts.append(journeystarts["Leytonstone High Road"])
		starts.append(journeystarts["Limehouse DLR"])
		starts.append(journeystarts["Liverpool Street LU"])
		starts.append(journeystarts["Liverpool Street NR"])
		starts.append(journeystarts["London Bridge LU"])
		starts.append(journeystarts["London City Airport"])
		starts.append(journeystarts["London Fields"])
		starts.append(journeystarts["Loughton"])
		starts.append(journeystarts["Maida Vale"])
		starts.append(journeystarts["Manor House"])
		starts.append(journeystarts["Manor Park"])
		starts.append(journeystarts["Mansion House"])
		starts.append(journeystarts["Marble Arch"])
		starts.append(journeystarts["Maryland"])
		starts.append(journeystarts["Marylebone LU"])
		starts.append(journeystarts["Mile End"])
		starts.append(journeystarts["Mill Hill East"])
		starts.append(journeystarts["Moor Park"])
		starts.append(journeystarts["Moorgate"])
		starts.append(journeystarts["Morden"])
		starts.append(journeystarts["Mornington Crescent"])
		starts.append(journeystarts["Mudchute"])
		starts.append(journeystarts["Neasden"])
		starts.append(journeystarts["New Cross"])
		starts.append(journeystarts["New Cross Gate"])
		starts.append(journeystarts["Newbury Park"])
		starts.append(journeystarts["North Acton"])
		starts.append(journeystarts["North Ealing"])
		starts.append(journeystarts["North Greenwich"])
		starts.append(journeystarts["North Harrow"])
		starts.append(journeystarts["North Wembley"])
		starts.append(journeystarts["Northfields"])
		starts.append(journeystarts["Northolt"])
		starts.append(journeystarts["Northwick Park"])
		starts.append(journeystarts["Northwood"])
		starts.append(journeystarts["Northwood Hills"])
		starts.append(journeystarts["Norwood Junction"])
		starts.append(journeystarts["Notting Hill Gate"])
		starts.append(journeystarts["Oakwood"])
		starts.append(journeystarts["Old Street"])
		starts.append(journeystarts["Osterley"])
		starts.append(journeystarts["Oval"])
		starts.append(journeystarts["Oxford Circus"])
		starts.append(journeystarts["Paddington NR"])
		starts.append(journeystarts["Paddington TfL"])
		starts.append(journeystarts["Park Royal"])
		starts.append(journeystarts["Parsons Green"])
		starts.append(journeystarts["Peckham Rye"])
		starts.append(journeystarts["Penge West"])
		starts.append(journeystarts["Perivale"])
		starts.append(journeystarts["Piccadilly Circus"])
		starts.append(journeystarts["Pimlico"])
		starts.append(journeystarts["Pinner"])
		starts.append(journeystarts["Plaistow"])
		starts.append(journeystarts["Pontoon Dock"])
		starts.append(journeystarts["Poplar"])
		starts.append(journeystarts["Preston Road"])
		starts.append(journeystarts["Prince Regent"])
		starts.append(journeystarts["Pudding Mill Lane"])
		starts.append(journeystarts["Putney Bridge"])
		starts.append(journeystarts["Queen's Park"])
		starts.append(journeystarts["Queens Road Peckham"])
		starts.append(journeystarts["Queensbury"])
		starts.append(journeystarts["Queensway"])
		starts.append(journeystarts["Ravenscourt Park"])
		starts.append(journeystarts["Rayners Lane"])
		starts.append(journeystarts["Rectory Road"])
		starts.append(journeystarts["Redbridge"])
		starts.append(journeystarts["Regent's Park"])
		starts.append(journeystarts["Richmond"])
		starts.append(journeystarts["Rickmansworth"])
		starts.append(journeystarts["Roding Valley"])
		starts.append(journeystarts["Romford"])
		starts.append(journeystarts["Rotherhithe"])
		starts.append(journeystarts["Royal Albert"])
		starts.append(journeystarts["Royal Oak"])
		starts.append(journeystarts["Royal Victoria"])
		starts.append(journeystarts["Ruislip"])
		starts.append(journeystarts["Ruislip Gardens"])
		starts.append(journeystarts["Ruislip Manor"])
		starts.append(journeystarts["Russell Square"])
		starts.append(journeystarts["Seven Kings"])
		starts.append(journeystarts["Seven Sisters"])
		starts.append(journeystarts["Shadwell DLR"])
		starts.append(journeystarts["Shadwell LO"])
		starts.append(journeystarts["Shenfield"])
		starts.append(journeystarts["Shepherd's Bush LU"])
		starts.append(journeystarts["Shepherd's Bush Market"])
		starts.append(journeystarts["Shepherd's Bush NR"])
		starts.append(journeystarts["Shoreditch High Street"])
		starts.append(journeystarts["Silver Street"])
		starts.append(journeystarts["Sloane Square"])
		starts.append(journeystarts["Snaresbrook"])
		starts.append(journeystarts["South Acton"])
		starts.append(journeystarts["South Ealing"])
		starts.append(journeystarts["South Hampstead"])
		starts.append(journeystarts["South Harrow"])
		starts.append(journeystarts["South Kensington"])
		starts.append(journeystarts["South Kenton"])
		starts.append(journeystarts["South Quay"])
		starts.append(journeystarts["South Ruislip"])
		starts.append(journeystarts["South Tottenham"])
		starts.append(journeystarts["South Wimbledon"])
		starts.append(journeystarts["South Woodford"])
		starts.append(journeystarts["Southall"])
		starts.append(journeystarts["Southbury"])
		starts.append(journeystarts["Southfields"])
		starts.append(journeystarts["Southgate"])
		starts.append(journeystarts["Southwark"])
		starts.append(journeystarts["St James Street"])
		starts.append(journeystarts["St. James's Park"])
		starts.append(journeystarts["St. John's Wood"])
		starts.append(journeystarts["St. Paul's"])
		starts.append(journeystarts["Stamford Brook"])
		starts.append(journeystarts["Stamford Hill"])
		starts.append(journeystarts["Stanmore"])
		starts.append(journeystarts["Star Lane"])
		starts.append(journeystarts["Stepney Green"])
		starts.append(journeystarts["Stockwell"])
		starts.append(journeystarts["Stoke Newington"])
		starts.append(journeystarts["Stonebridge Park"])
		starts.append(journeystarts["Stratford"])
		starts.append(journeystarts["Stratford High Street"])
		starts.append(journeystarts["Stratford International DLR"])
		starts.append(journeystarts["Sudbury Hill"])
		starts.append(journeystarts["Sudbury Town"])
		starts.append(journeystarts["Surrey Quays"])
		starts.append(journeystarts["Swiss Cottage"])
		starts.append(journeystarts["Sydenham"])
		starts.append(journeystarts["Temple"])
		starts.append(journeystarts["Theobalds Grove"])
		starts.append(journeystarts["Theydon Bois"])
		starts.append(journeystarts["Tooting Bec"])
		starts.append(journeystarts["Tooting Broadway"])
		starts.append(journeystarts["Tottenham Court Road"])
		starts.append(journeystarts["Tottenham Hale LU"])
		starts.append(journeystarts["Totteridge & Whetstone"])
		starts.append(journeystarts["Tower Gateway"])
		starts.append(journeystarts["Tower Hill"])
		starts.append(journeystarts["Tufnell Park"])
		starts.append(journeystarts["Turkey Street"])
		starts.append(journeystarts["Turnham Green"])
		starts.append(journeystarts["Turnpike Lane"])
		starts.append(journeystarts["Upminster"])
		starts.append(journeystarts["Upminster Bridge"])
		starts.append(journeystarts["Upney"])
		starts.append(journeystarts["Upper Holloway"])
		starts.append(journeystarts["Upton Park"])
		starts.append(journeystarts["Uxbridge"])
		starts.append(journeystarts["Vauxhall LU"])
		starts.append(journeystarts["Victoria LU"])
		starts.append(journeystarts["Walthamstow Central"])
		starts.append(journeystarts["Walthamstow Queen's Road"])
		starts.append(journeystarts["Wandsworth Road"])
		starts.append(journeystarts["Wanstead"])
		starts.append(journeystarts["Wanstead Park"])
		starts.append(journeystarts["Wapping"])
		starts.append(journeystarts["Warren Street"])
		starts.append(journeystarts["Warwick Avenue"])
		starts.append(journeystarts["Waterloo LU"])
		starts.append(journeystarts["Watford"])
		starts.append(journeystarts["Watford High Street"])
		starts.append(journeystarts["Watford Junction"])
		starts.append(journeystarts["Wembley Central"])
		starts.append(journeystarts["Wembley Park"])
		starts.append(journeystarts["West Acton"])
		starts.append(journeystarts["West Brompton"])
		starts.append(journeystarts["West Croydon NR"])
		starts.append(journeystarts["West Ealing"])
		starts.append(journeystarts["West Finchley"])
		starts.append(journeystarts["West Ham"])
		starts.append(journeystarts["West Hampstead LO"])
		starts.append(journeystarts["West Hampstead LU"])
		starts.append(journeystarts["West Harrow"])
		starts.append(journeystarts["West India Quay"])
		starts.append(journeystarts["West Kensington"])
		starts.append(journeystarts["West Ruislip"])
		starts.append(journeystarts["West Silvertown"])
		starts.append(journeystarts["Westbourne Park"])
		starts.append(journeystarts["Westferry"])
		starts.append(journeystarts["Westminster"])
		starts.append(journeystarts["White City"])
		starts.append(journeystarts["White Hart Lane"])
		starts.append(journeystarts["Whitechapel"])
		starts.append(journeystarts["Willesden Green"])
		starts.append(journeystarts["Willesden Junction"])
		starts.append(journeystarts["Wimbledon"])
		starts.append(journeystarts["Wimbledon Park"])
		starts.append(journeystarts["Wood Green"])
		starts.append(journeystarts["Wood Lane"])
		starts.append(journeystarts["Wood Street"])
		starts.append(journeystarts["Woodford"])
		starts.append(journeystarts["Woodgrange Park"])
		starts.append(journeystarts["Woodside Park"])
		starts.append(journeystarts["Woolwich Arsenal"])

		ends.append(journeyends["Abbey Road"])
		ends.append(journeyends["Acton Central"])
		ends.append(journeyends["Acton Main Line"])
		ends.append(journeyends["Acton Town"])
		ends.append(journeyends["Aldgate"])
		ends.append(journeyends["Aldgate East"])
		ends.append(journeyends["All Saints"])
		ends.append(journeyends["Alperton"])
		ends.append(journeyends["Amersham"])
		ends.append(journeyends["Anerley"])
		ends.append(journeyends["Angel"])
		ends.append(journeyends["Archway"])
		ends.append(journeyends["Arnos Grove"])
		ends.append(journeyends["Arsenal"])
		ends.append(journeyends["Baker Street"])
		ends.append(journeyends["Balham LU"])
		ends.append(journeyends["Bank and Monument"])
		ends.append(journeyends["Barbican"])
		ends.append(journeyends["Barking"])
		ends.append(journeyends["Barkingside"])
		ends.append(journeyends["Barons Court"])
		ends.append(journeyends["Battersea Park"])
		ends.append(journeyends["Bayswater"])
		ends.append(journeyends["Beckton"])
		ends.append(journeyends["Beckton Park"])
		ends.append(journeyends["Becontree"])
		ends.append(journeyends["Belsize Park"])
		ends.append(journeyends["Bermondsey"])
		ends.append(journeyends["Bethnal Green LO"])
		ends.append(journeyends["Bethnal Green LU"])
		ends.append(journeyends["Blackfriars LU"])
		ends.append(journeyends["Blackhorse Road"])
		ends.append(journeyends["Blackwall"])
		ends.append(journeyends["Bond Street"])
		ends.append(journeyends["Borough"])
		ends.append(journeyends["Boston Manor"])
		ends.append(journeyends["Bounds Green"])
		ends.append(journeyends["Bow Church"])
		ends.append(journeyends["Bow Road"])
		ends.append(journeyends["Brent Cross"])
		ends.append(journeyends["Brentwood"])
		ends.append(journeyends["Brixton LU"])
		ends.append(journeyends["Brockley"])
		ends.append(journeyends["Bromley-by-Bow"])
		ends.append(journeyends["Brondesbury"])
		ends.append(journeyends["Brondesbury Park"])
		ends.append(journeyends["Bruce Grove"])
		ends.append(journeyends["Buckhurst Hill"])
		ends.append(journeyends["Burnt Oak"])
		ends.append(journeyends["Bush Hill Park"])
		ends.append(journeyends["Bushey"])
		ends.append(journeyends["Caledonian Road"])
		ends.append(journeyends["Caledonian Road & Barnsbury"])
		ends.append(journeyends["Cambridge Heath"])
		ends.append(journeyends["Camden Road"])
		ends.append(journeyends["Camden Town"])
		ends.append(journeyends["Canada Water"])
		ends.append(journeyends["Canary Wharf DLR"])
		ends.append(journeyends["Canary Wharf LU"])
		ends.append(journeyends["Canning Town"])
		ends.append(journeyends["Cannon Street LU"])
		ends.append(journeyends["Canonbury"])
		ends.append(journeyends["Canons Park"])
		ends.append(journeyends["Carpenders Park"])
		ends.append(journeyends["Chadwell Heath"])
		ends.append(journeyends["Chalfont & Latimer"])
		ends.append(journeyends["Chalk Farm"])
		ends.append(journeyends["Chancery Lane"])
		ends.append(journeyends["Charing Cross LU"])
		ends.append(journeyends["Chesham"])
		ends.append(journeyends["Cheshunt"])
		ends.append(journeyends["Chigwell"])
		ends.append(journeyends["Chingford"])
		ends.append(journeyends["Chiswick Park"])
		ends.append(journeyends["Chorleywood"])
		ends.append(journeyends["Clapham Common"])
		ends.append(journeyends["Clapham High Street"])
		ends.append(journeyends["Clapham Junction"])
		ends.append(journeyends["Clapham North"])
		ends.append(journeyends["Clapham South"])
		ends.append(journeyends["Clapton"])
		ends.append(journeyends["Cockfosters"])
		ends.append(journeyends["Colindale"])
		ends.append(journeyends["Colliers Wood"])
		ends.append(journeyends["Covent Garden"])
		ends.append(journeyends["Crossharbour"])
		ends.append(journeyends["Crouch Hill"])
		ends.append(journeyends["Croxley"])
		ends.append(journeyends["Crystal Palace"])
		ends.append(journeyends["Custom House"])
		ends.append(journeyends["Cutty Sark"])
		ends.append(journeyends["Cyprus"])
		ends.append(journeyends["Dagenham East"])
		ends.append(journeyends["Dagenham Heathway"])
		ends.append(journeyends["Dalston Junction"])
		ends.append(journeyends["Dalston Kingsland"])
		ends.append(journeyends["Debden"])
		ends.append(journeyends["Denmark Hill"])
		ends.append(journeyends["Deptford Bridge"])
		ends.append(journeyends["Devons Road"])
		ends.append(journeyends["Dollis Hill"])
		ends.append(journeyends["Ealing Broadway"])
		ends.append(journeyends["Ealing Common"])
		ends.append(journeyends["Earl's Court"])
		ends.append(journeyends["East Acton"])
		ends.append(journeyends["East Finchley"])
		ends.append(journeyends["East Ham"])
		ends.append(journeyends["East India"])
		ends.append(journeyends["East Putney"])
		ends.append(journeyends["Eastcote"])
		ends.append(journeyends["Edgware"])
		ends.append(journeyends["Edgware Road (Bak)"])
		ends.append(journeyends["Edgware Road (DIS)"])
		ends.append(journeyends["Edmonton Green"])
		ends.append(journeyends["Elephant & Castle LU"])
		ends.append(journeyends["Elm Park"])
		ends.append(journeyends["Elverson Road"])
		ends.append(journeyends["Embankment"])
		ends.append(journeyends["Emerson Park"])
		ends.append(journeyends["Enfield Town"])
		ends.append(journeyends["Epping"])
		ends.append(journeyends["Euston LU"])
		ends.append(journeyends["Euston NR"])
		ends.append(journeyends["Euston Square"])
		ends.append(journeyends["Fairlop"])
		ends.append(journeyends["Farringdon"])
		ends.append(journeyends["Finchley Central"])
		ends.append(journeyends["Finchley Road"])
		ends.append(journeyends["Finchley Road & Frognal"])
		ends.append(journeyends["Finsbury Park LU"])
		ends.append(journeyends["Finsbury Park NR"])
		ends.append(journeyends["Forest Gate"])
		ends.append(journeyends["Forest Hill"])
		ends.append(journeyends["Fulham Broadway"])
		ends.append(journeyends["Gallions Reach"])
		ends.append(journeyends["Gants Hill"])
		ends.append(journeyends["Gidea Park"])
		ends.append(journeyends["Gloucester Road"])
		ends.append(journeyends["Golders Green"])
		ends.append(journeyends["Goldhawk Road"])
		ends.append(journeyends["Goodge Street"])
		ends.append(journeyends["Goodmayes"])
		ends.append(journeyends["Gospel Oak"])
		ends.append(journeyends["Grange Hill"])
		ends.append(journeyends["Great Portland Street"])
		ends.append(journeyends["Green Park"])
		ends.append(journeyends["Greenford"])
		ends.append(journeyends["Greenwich"])
		ends.append(journeyends["Gunnersbury"])
		ends.append(journeyends["Hackney Central"])
		ends.append(journeyends["Hackney Downs"])
		ends.append(journeyends["Hackney Wick"])
		ends.append(journeyends["Haggerston"])
		ends.append(journeyends["Hainault"])
		ends.append(journeyends["Hammersmith (DIS)"])
		ends.append(journeyends["Hammersmith (H&C)"])
		ends.append(journeyends["Hampstead"])
		ends.append(journeyends["Hampstead Heath"])
		ends.append(journeyends["Hanger Lane"])
		ends.append(journeyends["Hanwell"])
		ends.append(journeyends["Harlesden"])
		ends.append(journeyends["Harold Wood"])
		ends.append(journeyends["Harringay Green Lanes"])
		ends.append(journeyends["Harrow & Wealdstone"])
		ends.append(journeyends["Harrow-on-the-Hill"])
		ends.append(journeyends["Hatch End"])
		ends.append(journeyends["Hatton Cross"])
		ends.append(journeyends["Hayes & Harlington"])
		ends.append(journeyends["Headstone Lane"])
		ends.append(journeyends["Heathrow Terminal 4 EL"])
		ends.append(journeyends["Heathrow Terminal 4 LU"])
		ends.append(journeyends["Heathrow Terminal 5 LU"])
		ends.append(journeyends["Heathrow Terminals 123 LU"])
		ends.append(journeyends["Heathrow Terminals 2 & 3 EL"])
		ends.append(journeyends["Hendon Central"])
		ends.append(journeyends["Heron Quays"])
		ends.append(journeyends["High Barnet"])
		ends.append(journeyends["High Street Kensington"])
		ends.append(journeyends["Highams Park"])
		ends.append(journeyends["Highbury & Islington"])
		ends.append(journeyends["Highgate"])
		ends.append(journeyends["Hillingdon"])
		ends.append(journeyends["Holborn"])
		ends.append(journeyends["Holland Park"])
		ends.append(journeyends["Holloway Road"])
		ends.append(journeyends["Homerton"])
		ends.append(journeyends["Honor Oak Park"])
		ends.append(journeyends["Hornchurch"])
		ends.append(journeyends["Hounslow Central"])
		ends.append(journeyends["Hounslow East"])
		ends.append(journeyends["Hounslow West"])
		ends.append(journeyends["Hoxton"])
		ends.append(journeyends["Hyde Park Corner"])
		ends.append(journeyends["Ickenham"])
		ends.append(journeyends["Ilford"])
		ends.append(journeyends["Imperial Wharf"])
		ends.append(journeyends["Island Gardens"])
		ends.append(journeyends["Kennington"])
		ends.append(journeyends["Kensal Green"])
		ends.append(journeyends["Kensal Rise"])
		ends.append(journeyends["Kensington (Olympia)"])
		ends.append(journeyends["Kentish Town"])
		ends.append(journeyends["Kentish Town West"])
		ends.append(journeyends["Kenton"])
		ends.append(journeyends["Kew Gardens"])
		ends.append(journeyends["Kilburn"])
		ends.append(journeyends["Kilburn High Road"])
		ends.append(journeyends["Kilburn Park"])
		ends.append(journeyends["King George V"])
		ends.append(journeyends["King's Cross St. Pancras"])
		ends.append(journeyends["Kingsbury"])
		ends.append(journeyends["Knightsbridge"])
		ends.append(journeyends["Ladbroke Grove"])
		ends.append(journeyends["Lambeth North"])
		ends.append(journeyends["Lancaster Gate"])
		ends.append(journeyends["Langdon Park"])
		ends.append(journeyends["Latimer Road"])
		ends.append(journeyends["Leicester Square"])
		ends.append(journeyends["Lewisham DLR"])
		ends.append(journeyends["Leyton"])
		ends.append(journeyends["Leyton Midland Road"])
		ends.append(journeyends["Leytonstone"])
		ends.append(journeyends["Leytonstone High Road"])
		ends.append(journeyends["Limehouse DLR"])
		ends.append(journeyends["Liverpool Street LU"])
		ends.append(journeyends["Liverpool Street NR"])
		ends.append(journeyends["London Bridge LU"])
		ends.append(journeyends["London City Airport"])
		ends.append(journeyends["London Fields"])
		ends.append(journeyends["Loughton"])
		ends.append(journeyends["Maida Vale"])
		ends.append(journeyends["Manor House"])
		ends.append(journeyends["Manor Park"])
		ends.append(journeyends["Mansion House"])
		ends.append(journeyends["Marble Arch"])
		ends.append(journeyends["Maryland"])
		ends.append(journeyends["Marylebone LU"])
		ends.append(journeyends["Mile End"])
		ends.append(journeyends["Mill Hill East"])
		ends.append(journeyends["Moor Park"])
		ends.append(journeyends["Moorgate"])
		ends.append(journeyends["Morden"])
		ends.append(journeyends["Mornington Crescent"])
		ends.append(journeyends["Mudchute"])
		ends.append(journeyends["Neasden"])
		ends.append(journeyends["New Cross"])
		ends.append(journeyends["New Cross Gate"])
		ends.append(journeyends["Newbury Park"])
		ends.append(journeyends["North Acton"])
		ends.append(journeyends["North Ealing"])
		ends.append(journeyends["North Greenwich"])
		ends.append(journeyends["North Harrow"])
		ends.append(journeyends["North Wembley"])
		ends.append(journeyends["Northfields"])
		ends.append(journeyends["Northolt"])
		ends.append(journeyends["Northwick Park"])
		ends.append(journeyends["Northwood"])
		ends.append(journeyends["Northwood Hills"])
		ends.append(journeyends["Norwood Junction"])
		ends.append(journeyends["Notting Hill Gate"])
		ends.append(journeyends["Oakwood"])
		ends.append(journeyends["Old Street"])
		ends.append(journeyends["Osterley"])
		ends.append(journeyends["Oval"])
		ends.append(journeyends["Oxford Circus"])
		ends.append(journeyends["Paddington NR"])
		ends.append(journeyends["Paddington TfL"])
		ends.append(journeyends["Park Royal"])
		ends.append(journeyends["Parsons Green"])
		ends.append(journeyends["Peckham Rye"])
		ends.append(journeyends["Penge West"])
		ends.append(journeyends["Perivale"])
		ends.append(journeyends["Piccadilly Circus"])
		ends.append(journeyends["Pimlico"])
		ends.append(journeyends["Pinner"])
		ends.append(journeyends["Plaistow"])
		ends.append(journeyends["Pontoon Dock"])
		ends.append(journeyends["Poplar"])
		ends.append(journeyends["Preston Road"])
		ends.append(journeyends["Prince Regent"])
		ends.append(journeyends["Pudding Mill Lane"])
		ends.append(journeyends["Putney Bridge"])
		ends.append(journeyends["Queen's Park"])
		ends.append(journeyends["Queens Road Peckham"])
		ends.append(journeyends["Queensbury"])
		ends.append(journeyends["Queensway"])
		ends.append(journeyends["Ravenscourt Park"])
		ends.append(journeyends["Rayners Lane"])
		ends.append(journeyends["Rectory Road"])
		ends.append(journeyends["Redbridge"])
		ends.append(journeyends["Regent's Park"])
		ends.append(journeyends["Richmond"])
		ends.append(journeyends["Rickmansworth"])
		ends.append(journeyends["Roding Valley"])
		ends.append(journeyends["Romford"])
		ends.append(journeyends["Rotherhithe"])
		ends.append(journeyends["Royal Albert"])
		ends.append(journeyends["Royal Oak"])
		ends.append(journeyends["Royal Victoria"])
		ends.append(journeyends["Ruislip"])
		ends.append(journeyends["Ruislip Gardens"])
		ends.append(journeyends["Ruislip Manor"])
		ends.append(journeyends["Russell Square"])
		ends.append(journeyends["Seven Kings"])
		ends.append(journeyends["Seven Sisters"])
		ends.append(journeyends["Shadwell DLR"])
		ends.append(journeyends["Shadwell LO"])
		ends.append(journeyends["Shenfield"])
		ends.append(journeyends["Shepherd's Bush LU"])
		ends.append(journeyends["Shepherd's Bush Market"])
		ends.append(journeyends["Shepherd's Bush NR"])
		ends.append(journeyends["Shoreditch High Street"])
		ends.append(journeyends["Silver Street"])
		ends.append(journeyends["Sloane Square"])
		ends.append(journeyends["Snaresbrook"])
		ends.append(journeyends["South Acton"])
		ends.append(journeyends["South Ealing"])
		ends.append(journeyends["South Hampstead"])
		ends.append(journeyends["South Harrow"])
		ends.append(journeyends["South Kensington"])
		ends.append(journeyends["South Kenton"])
		ends.append(journeyends["South Quay"])
		ends.append(journeyends["South Ruislip"])
		ends.append(journeyends["South Tottenham"])
		ends.append(journeyends["South Wimbledon"])
		ends.append(journeyends["South Woodford"])
		ends.append(journeyends["Southall"])
		ends.append(journeyends["Southbury"])
		ends.append(journeyends["Southfields"])
		ends.append(journeyends["Southgate"])
		ends.append(journeyends["Southwark"])
		ends.append(journeyends["St James Street"])
		ends.append(journeyends["St. James's Park"])
		ends.append(journeyends["St. John's Wood"])
		ends.append(journeyends["St. Paul's"])
		ends.append(journeyends["Stamford Brook"])
		ends.append(journeyends["Stamford Hill"])
		ends.append(journeyends["Stanmore"])
		ends.append(journeyends["Star Lane"])
		ends.append(journeyends["Stepney Green"])
		ends.append(journeyends["Stockwell"])
		ends.append(journeyends["Stoke Newington"])
		ends.append(journeyends["Stonebridge Park"])
		ends.append(journeyends["Stratford"])
		ends.append(journeyends["Stratford High Street"])
		ends.append(journeyends["Stratford International DLR"])
		ends.append(journeyends["Sudbury Hill"])
		ends.append(journeyends["Sudbury Town"])
		ends.append(journeyends["Surrey Quays"])
		ends.append(journeyends["Swiss Cottage"])
		ends.append(journeyends["Sydenham"])
		ends.append(journeyends["Temple"])
		ends.append(journeyends["Theobalds Grove"])
		ends.append(journeyends["Theydon Bois"])
		ends.append(journeyends["Tooting Bec"])
		ends.append(journeyends["Tooting Broadway"])
		ends.append(journeyends["Tottenham Court Road"])
		ends.append(journeyends["Tottenham Hale LU"])
		ends.append(journeyends["Totteridge & Whetstone"])
		ends.append(journeyends["Tower Gateway"])
		ends.append(journeyends["Tower Hill"])
		ends.append(journeyends["Tufnell Park"])
		ends.append(journeyends["Turkey Street"])
		ends.append(journeyends["Turnham Green"])
		ends.append(journeyends["Turnpike Lane"])
		ends.append(journeyends["Upminster"])
		ends.append(journeyends["Upminster Bridge"])
		ends.append(journeyends["Upney"])
		ends.append(journeyends["Upper Holloway"])
		ends.append(journeyends["Upton Park"])
		ends.append(journeyends["Uxbridge"])
		ends.append(journeyends["Vauxhall LU"])
		ends.append(journeyends["Victoria LU"])
		ends.append(journeyends["Walthamstow Central"])
		ends.append(journeyends["Walthamstow Queen's Road"])
		ends.append(journeyends["Wandsworth Road"])
		ends.append(journeyends["Wanstead"])
		ends.append(journeyends["Wanstead Park"])
		ends.append(journeyends["Wapping"])
		ends.append(journeyends["Warren Street"])
		ends.append(journeyends["Warwick Avenue"])
		ends.append(journeyends["Waterloo LU"])
		ends.append(journeyends["Watford"])
		ends.append(journeyends["Watford High Street"])
		ends.append(journeyends["Watford Junction"])
		ends.append(journeyends["Wembley Central"])
		ends.append(journeyends["Wembley Park"])
		ends.append(journeyends["West Acton"])
		ends.append(journeyends["West Brompton"])
		ends.append(journeyends["West Croydon NR"])
		ends.append(journeyends["West Ealing"])
		ends.append(journeyends["West Finchley"])
		ends.append(journeyends["West Ham"])
		ends.append(journeyends["West Hampstead LO"])
		ends.append(journeyends["West Hampstead LU"])
		ends.append(journeyends["West Harrow"])
		ends.append(journeyends["West India Quay"])
		ends.append(journeyends["West Kensington"])
		ends.append(journeyends["West Ruislip"])
		ends.append(journeyends["West Silvertown"])
		ends.append(journeyends["Westbourne Park"])
		ends.append(journeyends["Westferry"])
		ends.append(journeyends["Westminster"])
		ends.append(journeyends["White City"])
		ends.append(journeyends["White Hart Lane"])
		ends.append(journeyends["Whitechapel"])
		ends.append(journeyends["Willesden Green"])
		ends.append(journeyends["Willesden Junction"])
		ends.append(journeyends["Wimbledon"])
		ends.append(journeyends["Wimbledon Park"])
		ends.append(journeyends["Wood Green"])
		ends.append(journeyends["Wood Lane"])
		ends.append(journeyends["Wood Street"])
		ends.append(journeyends["Woodford"])
		ends.append(journeyends["Woodgrange Park"])
		ends.append(journeyends["Woodside Park"])
		ends.append(journeyends["Woolwich Arsenal"])

		aJs.append(starts)
		aJs.append(ends)

		n = n+1
		pass

	l = l+1
	pass

#print("aJs", aJs)
#print("len(aJs)", len(aJs))

#print("aJsS", aJsS)
#print("aJsE", aJsE)

#print("aJsS[0]", aJsS[0])
#print("aJsS[1]", aJsS[1])
#print("aJsS[2]", aJsS[2])
#print("aJsS[3]", aJsS[3])
#print("aJsS[4]", aJsS[4])
#print("aJsS[5]", aJsS[5])

"""
print("len(aJsS[0][0])", len(aJsS[0][0]))
print("len(aJsS[1][0])", len(aJsS[1][0]))
print("len(aJsS[2][0])", len(aJsS[2][0]))
print("len(aJsS[3][0])", len(aJsS[3][0]))
print("len(aJsS[4][0])", len(aJsS[4][0]))
print("len(aJsS[5][0])", len(aJsS[5][0]))

print("len(aJsE[0][0])", len(aJsE[0][0]))
print("len(aJsE[1][0])", len(aJsE[1][0]))
print("len(aJsE[2][0])", len(aJsE[2][0]))
print("len(aJsE[3][0])", len(aJsE[3][0]))
print("len(aJsE[4][0])", len(aJsE[4][0]))
print("len(aJsE[5][0])", len(aJsE[5][0]))
"""

# aJs = [(0),	(1),	(2),	(3),		(4),				(5),	(6),	(7),	(8),		(9),				(10),		(11),	(12),	(13),		(14)... ]
# aJs = ["T#0",	T0,		n0,		[jSts0],	[jEns0],			"T#1",	T1,		n1,		[jSts1],	[jEns1],			"T#2",		T2,		n2,		[jSts2],	[jEns2]... ]

#print("NAMES", NAMES)
"""
#idx = random.randrange(0, NAMES) - does not work! 
#idx = random.randrange(0, len(NAMES))
#print("idx", idx)
#print("type(idx)", type(idx))

#print("NAMEs(idx)", NAMES[int(idx)])

#test_TS		=	["T0",	"T3",	"T6",	"T9",	"T12",	"T15",	"T18",	"T21", 	"T24", 	"T27", 	"T30", 	"T33", 	"T36", 	"T39", 	"T42", 	"T45", 	"T48", 	"T51", 	"T54", 	"T57", 	"T60", 	"T63", 	"T66", 	"T69", 	"T72", 	"T75", 	"T78", 	"T81", 	"T84", 	"T87", 	"T90", 	"T93", 	"T96", 	"T99", 	"T102", "T105", "T108", "T111", "T114", "T117", 	"T120", 	"T123", 	"T126", 	"T129", 	"T132", 	"T135", 	"T138", 	"T141", 	"T144", 	"T147", 	"T150", 	"T153", 	"T156", 	"T159", 	"T162", 	"T165", 	"T168", 	"T171", 	"T174", 	"T177", 	"T180", 	"T183", 	"T186", 	"T189", 	"T192", 	"T195", 	"T198", 	"T201", 	"T204", 	"T207", 	"T210", 	"T213", 	"T216", 	"T219", 	"T222", 	"T225", 	"T228", "T231", "T234", "T237", "T240", "T243", "T246", "T249", "T252", "T255", "T258", "T261", "T264", "T267", "T270", "T273", "T276", "T279", "T282", "T285"]
#test_T		= 	["500",	"515",	"530",	"545",	"600",	"615",	"630",	"645", 	"700", 	"715", 	"730", 	"745", 	"800", 	"815", 	"830", 	"845", 	"900", 	"915", 	"930", 	"945", 	"1000",	"1015", "1030", "1045", "1100", "1115", "1130", "1145", "1200", "1215", "1230", "1245", "1300", "1315", "1330", "1345", "1400", "1415", "1430", "1445", 	"1500", 	"1515", 	"1530", 	"1545", 	"1600", 	"1615", 	"1630", 	"1645", 	"1700", 	"1715", 	"1730", 	"1745", 	"1800", 	"1815", 	"1830", 	"1845", 	"1900", 	"1915", 	"1930", 	"1945", 	"2000", 	"2015", 	"2030", 	"2045", 	"2100", 	"2115", 	"2130", 	"2145", 	"2200", 	"2215", 	"2230", 	"2245", 	"2300", 	"2315", 	"2330", 	"2345", 	"0", 	"15", 	"30", 	"45", 	"100", 	"115", 	"130", 	"145", 	"200", 	"215", 	"230", 	"245", 	"300", 	"315", 	"330", 	"345", 	"400", 	"415", 	"430", 	"445"]

test_TS		=	aJsS[0][0]
test_T		= 	aJsE[0][0]

my_list = []
its = len(test_TS)

while its > 0:
	num1 = random.randint(0, its-1)
	num2 = random.randint(0, its-1)
	#print("num1", num1)
	#print("num2", num2)
	both = []
	both.append(test_TS[num1])
	both.append(test_T[num2])
	my_list.append(both)
	#print("test_TS[num1]", test_TS[num1])
	#print("test_T[num2]", test_T[num2])
	test_TS.remove(test_TS[num1])
	test_T.remove(test_T[num2])
	its = len(test_TS)
	#print("its", its)
	pass

#print("test_TS", test_TS)
#print("test_T", test_T)
print("my_list", my_list)
"""

my_list	= 	[]
p 		=	0

while p <= 0: #95
	this = aJsS[p][0]
	that = aJsE[p][0]
	its  = len(this)
	pass
	while its > 0:
		num1 = random.randint(0, its-1)
		num2 = random.randint(0, its-1)
		#print("num1", num1)
		#print("num2", num2)
		both = []
		both.append(this[num1])
		both.append(that[num2])
		my_list.append(both)
		#print("test_TS[num1]", test_TS[num1])
		#print("test_T[num2]", test_T[num2])
		this.remove(this[num1])
		that.remove(that[num2])
		its = len(this)
		#print("its", its)
		pass


print("my_list", my_list)















"""
with open('JourneysLong.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)
	thewriter.writerow(['Timestamp', 'Time', 'Journeys', 'ABR', 'ACC', 	'AML', 	'ACT', 	'ALD', 	'ALE', 	'ALS', 	'ALP', 	'AME', 	'ANY', 	'ANG', 	'ARC', 	'AGRu', 	'ARL', 	'BST', 	'BALu', 	'BNK', 	'BAR', 	'BKGu', 	'BDE', 	'BCT', 	'BAK', 	'BAY', 	'BECd', 	'BEP', 	'BECu', 	'BPK', 	'BER', 	'BET', 	'BNG', 	'BLF', 	'BHR', 	'BLA', 	'BDS', 	'BOR', 	'BOS', 	'BGR', 	'BOC', 	'BWR', 	'BTX', 	'BRE', 	'BRXu', 	'BCY', 	'BBB', 	'BSY', 	'BSP', 	'BCV', 	'BHLu', 	'BUR', 	'BHK', 	'BSH', 	'CRD', 	'CIR', 	'CBH', 	'CMD', 	'CTNu', 	'CWR', 	'CAW', 	'CWF', 	'CNT', 	'CSTu', 	'CNN', 	'CPKu', 	'CPKr', 	'CTH', 	'CLF', 	'CHF', 	'CYL', 	'CHXu', 	'CHM', 	'CHN', 	'CHG', 	'CHI', 	'CHPu', 	'CWD', 	'CPC', 	'CLP', 	'CLJ', 	'CPN', 	'CPS', 	'CPT', 	'CFS', 	'COL', 	'CLW', 	'COV', 	'CRO', 	'CRH', 	'CRX', 	'CYPr', 	'CUH', 	'CUS', 	'CYPd', 	'DGE', 	'DGH', 	'DLJ', 	'DLK', 	'DEBu', 	'DMK', 	'DEBd', 	'DER', 	'DHL', 	'EBY', 	'ECM', 	'ECT', 	'EAC', 	'EFY', 	'EHM', 	'EAI', 	'EPY', 	'ETE', 	'EDG', 	'ERB', 	'ERD', 	'EDR', 	'ELE', 	'EPK', 	'ELR', 	'EMB', 	'EMP', 	'ENF', 	'EPP', 	'EUSu', 	'EUSr', 	'ESQ', 	'FLP', 	'FAR', 	'FYC', 	'FRD', 	'FNY', 	'FPKu', 	'FPKr', 	'FOG', 	'FOH', 	'FBY', 	'GAR', 	'GHL', 	'GDP', 	'GRD', 	'GGR', 	'GHR', 	'GSTu', 	'GMY', 	'GPO', 	'GRH', 	'GPS', 	'GPKu', 	'GFD', 	'GRE', 	'GUNu', 	'HKC', 	'HAC', 	'HKW', 	'HGG', 	'HAI', 	'HMD', 	'HMS', 	'HMPu', 	'HDH', 	'HLN', 	'HAN', 	'HAR', 	'HRO', 	'HRY', 	'HAW', 	'HOH', 	'HTE', 	'HTX', 	'HAY', 	'HDL', 	'HAF', 	'HRF', 	'HRV', 	'HRC', 	'HXX', 	'HND', 	'HEQ', 	'HBT', 	'HST', 	'HIP', 	'HBY', 	'HIG', 	'HDNu', 	'HOL', 	'HPK', 	'HRDu', 	'HMN', 	'HPA', 	'HCH', 	'HNC', 	'HNE', 	'HNW', 	'HOX', 	'HPC', 	'ICK', 	'IFD', 	'IMW', 	'ISG', 	'KEN', 	'KGN', 	'KNR', 	'OLY', 	'KTN', 	'KTW', 	'KET', 	'KEW', 	'KIL', 	'KBN', 	'KPK', 	'KGV', 	'KXX', 	'KBY', 	'KNB', 	'LGR', 	'LAM', 	'LAN', 	'LAP', 	'LAT', 	'LSQ', 	'LEWd', 	'LEY', 	'LEM', 	'LYS', 	'LER', 	'LIM', 	'LSTu', 	'LSTr', 	'LON', 	'LCA', 	'LOF', 	'LTN', 	'MDV', 	'MNR', 	'MNP', 	'MAN', 	'MAR', 	'MYL', 	'MYBu', 	'MLE', 	'MHE', 	'MPKu', 	'MGT', 	'MOR', 	'MCR', 	'MUD', 	'NEA', 	'NWX', 	'NXG', 	'NEP', 	'NAC', 	'NEL', 	'NOG', 	'NHR', 	'NWB', 	'NFD', 	'NHT', 	'NWP', 	'NWDu', 	'NWH', 	'NWDr', 	'NHG', 	'OAK', 	'OLD', 	'OST', 	'OVL', 	'OXC', 	'PADr', 	'PADu', 	'PRY', 	'PGR', 	'PMR', 	'PNW', 	'PER', 	'PIC', 	'PIM', 	'PIN', 	'PLW', 	'PDK', 	'POP', 	'PRD', 	'PRR', 	'PML', 	'PUTu', 	'QPK', 	'QRP', 	'QBY', 	'QWY', 	'RCP', 	'RAYu', 	'REC', 	'RED', 	'RPK', 	'RMD', 	'RKY', 	'ROD', 	'RMF', 	'ROE', 	'ROA', 	'ROY', 	'ROV', 	'RUI', 	'RUG', 	'RUM', 	'RSQ', 	'SVK', 	'SVS', 	'SHA', 	'SDE', 	'SNF', 	'SBC', 	'SBMu', 	'SPB', 	'SDC', 	'SLV', 	'SSQ', 	'SNB', 	'SAT', 	'SEL', 	'SOH', 	'SHR', 	'SKN', 	'SKT', 	'SOQ', 	'SRP', 	'STO', 	'SWM', 	'SWF', 	'STLr', 	'SBU', 	'SFS', 	'SGT', 	'SWK', 	'SJS', 	'SJP', 	'SJW', 	'STPu', 	'STB', 	'SMH', 	'STA', 	'STLd', 	'STG', 	'STK', 	'SKW', 	'SPK', 	'SFD', 	'SHS', 	'STI', 	'SHL', 	'STN', 	'SQE', 	'SWC', 	'SYD', 	'TEM', 	'TEO', 	'THB', 	'TBE', 	'TBY', 	'TCR', 	'TTHu', 	'TOT', 	'TOG', 	'THL', 	'TPK', 	'TUR', 	'TGR', 	'TPLu', 	'UPM', 	'UPB', 	'UPY', 	'UHL', 	'UPK', 	'UXB', 	'VUX', 	'VICu', 	'WAL', 	'WMW', 	'WWR', 	'WAN', 	'WNP', 	'WPE', 	'WSTu', 	'WARu', 	'WLO', 	'WATu', 	'WFH', 	'WFJ', 	'WEM', 	'WPKu', 	'WAC', 	'WBT', 	'WCY', 	'WEA', 	'WFY', 	'WHM', 	'WHP', 	'WHDu', 	'WHR', 	'WIQ', 	'WKN', 	'WRP', 	'WSI', 	'WBPu', 	'WES', 	'WMS', 	'WCT', 	'WHL', 	'WCL', 	'WLG', 	'WJN', 	'WIM', 	'WMP', 	'WGN', 	'WDL', 	'WSTr', 	'WFD', 	'WGR', 	'WSP', 	'WOA', 'ABR', 'ACC', 	'AML', 	'ACT', 	'ALD', 	'ALE', 	'ALS', 	'ALP', 	'AME', 	'ANY', 	'ANG', 	'ARC', 	'AGRu', 	'ARL', 	'BST', 	'BALu', 	'BNK', 	'BAR', 	'BKGu', 	'BDE', 	'BCT', 	'BAK', 	'BAY', 	'BECd', 	'BEP', 	'BECu', 	'BPK', 	'BER', 	'BET', 	'BNG', 	'BLF', 	'BHR', 	'BLA', 	'BDS', 	'BOR', 	'BOS', 	'BGR', 	'BOC', 	'BWR', 	'BTX', 	'BRE', 	'BRXu', 	'BCY', 	'BBB', 	'BSY', 	'BSP', 	'BCV', 	'BHLu', 	'BUR', 	'BHK', 	'BSH', 	'CRD', 	'CIR', 	'CBH', 	'CMD', 	'CTNu', 	'CWR', 	'CAW', 	'CWF', 	'CNT', 	'CSTu', 	'CNN', 	'CPKu', 	'CPKr', 	'CTH', 	'CLF', 	'CHF', 	'CYL', 	'CHXu', 	'CHM', 	'CHN', 	'CHG', 	'CHI', 	'CHPu', 	'CWD', 	'CPC', 	'CLP', 	'CLJ', 	'CPN', 	'CPS', 	'CPT', 	'CFS', 	'COL', 	'CLW', 	'COV', 	'CRO', 	'CRH', 	'CRX', 	'CYPr', 	'CUH', 	'CUS', 	'CYPd', 	'DGE', 	'DGH', 	'DLJ', 	'DLK', 	'DEBu', 	'DMK', 	'DEBd', 	'DER', 	'DHL', 	'EBY', 	'ECM', 	'ECT', 	'EAC', 	'EFY', 	'EHM', 	'EAI', 	'EPY', 	'ETE', 	'EDG', 	'ERB', 	'ERD', 	'EDR', 	'ELE', 	'EPK', 	'ELR', 	'EMB', 	'EMP', 	'ENF', 	'EPP', 	'EUSu', 	'EUSr', 	'ESQ', 	'FLP', 	'FAR', 	'FYC', 	'FRD', 	'FNY', 	'FPKu', 	'FPKr', 	'FOG', 	'FOH', 	'FBY', 	'GAR', 	'GHL', 	'GDP', 	'GRD', 	'GGR', 	'GHR', 	'GSTu', 	'GMY', 	'GPO', 	'GRH', 	'GPS', 	'GPKu', 	'GFD', 	'GRE', 	'GUNu', 	'HKC', 	'HAC', 	'HKW', 	'HGG', 	'HAI', 	'HMD', 	'HMS', 	'HMPu', 	'HDH', 	'HLN', 	'HAN', 	'HAR', 	'HRO', 	'HRY', 	'HAW', 	'HOH', 	'HTE', 	'HTX', 	'HAY', 	'HDL', 	'HAF', 	'HRF', 	'HRV', 	'HRC', 	'HXX', 	'HND', 	'HEQ', 	'HBT', 	'HST', 	'HIP', 	'HBY', 	'HIG', 	'HDNu', 	'HOL', 	'HPK', 	'HRDu', 	'HMN', 	'HPA', 	'HCH', 	'HNC', 	'HNE', 	'HNW', 	'HOX', 	'HPC', 	'ICK', 	'IFD', 	'IMW', 	'ISG', 	'KEN', 	'KGN', 	'KNR', 	'OLY', 	'KTN', 	'KTW', 	'KET', 	'KEW', 	'KIL', 	'KBN', 	'KPK', 	'KGV', 	'KXX', 	'KBY', 	'KNB', 	'LGR', 	'LAM', 	'LAN', 	'LAP', 	'LAT', 	'LSQ', 	'LEWd', 	'LEY', 	'LEM', 	'LYS', 	'LER', 	'LIM', 	'LSTu', 	'LSTr', 	'LON', 	'LCA', 	'LOF', 	'LTN', 	'MDV', 	'MNR', 	'MNP', 	'MAN', 	'MAR', 	'MYL', 	'MYBu', 	'MLE', 	'MHE', 	'MPKu', 	'MGT', 	'MOR', 	'MCR', 	'MUD', 	'NEA', 	'NWX', 	'NXG', 	'NEP', 	'NAC', 	'NEL', 	'NOG', 	'NHR', 	'NWB', 	'NFD', 	'NHT', 	'NWP', 	'NWDu', 	'NWH', 	'NWDr', 	'NHG', 	'OAK', 	'OLD', 	'OST', 	'OVL', 	'OXC', 	'PADr', 	'PADu', 	'PRY', 	'PGR', 	'PMR', 	'PNW', 	'PER', 	'PIC', 	'PIM', 	'PIN', 	'PLW', 	'PDK', 	'POP', 	'PRD', 	'PRR', 	'PML', 	'PUTu', 	'QPK', 	'QRP', 	'QBY', 	'QWY', 	'RCP', 	'RAYu', 	'REC', 	'RED', 	'RPK', 	'RMD', 	'RKY', 	'ROD', 	'RMF', 	'ROE', 	'ROA', 	'ROY', 	'ROV', 	'RUI', 	'RUG', 	'RUM', 	'RSQ', 	'SVK', 	'SVS', 	'SHA', 	'SDE', 	'SNF', 	'SBC', 	'SBMu', 	'SPB', 	'SDC', 	'SLV', 	'SSQ', 	'SNB', 	'SAT', 	'SEL', 	'SOH', 	'SHR', 	'SKN', 	'SKT', 	'SOQ', 	'SRP', 	'STO', 	'SWM', 	'SWF', 	'STLr', 	'SBU', 	'SFS', 	'SGT', 	'SWK', 	'SJS', 	'SJP', 	'SJW', 	'STPu', 	'STB', 	'SMH', 	'STA', 	'STLd', 	'STG', 	'STK', 	'SKW', 	'SPK', 	'SFD', 	'SHS', 	'STI', 	'SHL', 	'STN', 	'SQE', 	'SWC', 	'SYD', 	'TEM', 	'TEO', 	'THB', 	'TBE', 	'TBY', 	'TCR', 	'TTHu', 	'TOT', 	'TOG', 	'THL', 	'TPK', 	'TUR', 	'TGR', 	'TPLu', 	'UPM', 	'UPB', 	'UPY', 	'UHL', 	'UPK', 	'UXB', 	'VUX', 	'VICu', 	'WAL', 	'WMW', 	'WWR', 	'WAN', 	'WNP', 	'WPE', 	'WSTu', 	'WARu', 	'WLO', 	'WATu', 	'WFH', 	'WFJ', 	'WEM', 	'WPKu', 	'WAC', 	'WBT', 	'WCY', 	'WEA', 	'WFY', 	'WHM', 	'WHP', 	'WHDu', 	'WHR', 	'WIQ', 	'WKN', 	'WRP', 	'WSI', 	'WBPu', 	'WES', 	'WMS', 	'WCT', 	'WHL', 	'WCL', 	'WLG', 	'WJN', 	'WIM', 	'WMP', 	'WGN', 	'WDL', 	'WSTr', 	'WFD', 	'WGR', 	'WSP', 	'WOA'])
	for i in range(1,len(aJs)+1):
		thewriter.writerow(aJs[i-1])
"""