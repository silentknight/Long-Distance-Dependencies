#!/usr/bin/env python

import numpy as np

# ptb = np.array([6618,19024,99706700,116857,149690,1111,6345,31401,99598086,168077,195084,1007,4615,38715,99556104,188263,211241,1062,3461,40468,99541383,203587,210206,895,2926,41143,99534088,210106,210788,949,2673,41825,99529113,213191,212273,925,2537,41955,99526539,214983,213036,950,2443,42386,99524121,216248,213862,940,2355,42475,99523726,216871,213582,991,2251,42602,99521837,217583,214795,932,2228,42451,99521383,218776,214247,915,2284,42578,99520335,219300,214540,963,2135,43078,99519581,219715,214561,930,2074,43014,99519287,219940,214734,951,2159,42853,99519015,220063,214967,943,2084,42611,99518372,221010,215003,920,2103,42983,99517945,220742,215276,951,2082,42908,99517879,221025,215187,919,2063,43113,99517010,221237,215677,900,1993,42912,99517563,221570,215023,939,2031,42989,99517005,221654,215453,868,1983,43233,99516992,221694,215135,963,2037,42954,99516680,222268,215112,949,2039,43143,99516193,222501,215250,874,1951,43160,99516310,222606,215035,938,1995,43075,99516405,222603,215016,906,1984,43310,99515906,222048,215787,965,1963,43078,99516215,222533,215368,843,1947,42948,99516210,222966,214958,971,1908,43123,99516031,222788,215215,935,2011,43047,99515628,222828,215622,864,1922,42927,99515790,223056,215399,906,1918,43300,99515180,223208,215470,924,1943,43082,99514947,223938,215196,894,1896,43156,99515123,223830,215099,896,1899,43036,99515044,223949,215158,914,1926,43235,99514719,223771,215492,857,1920,43446,99514503,223187,216054,890,1889,43206,99514036,224173,215780,916,1828,43297,99514480,223666,215861,868,1924,43142,99514174,224331,215521,908,1872,43228,99514218,223916,215858,908,1831,43173,99514814,223835,215441,906,1877,43309,99514151,223767,215971,925,1831,43346,99514117,224599,215247,860,1920,43149,99513869,224185,215929,948,1887,42996,99514307,224773,215136,901,1860,43374,99513768,224358,215724,916,1842,43074,99514206,224306,215687,885,1797,43166,99514149,224467,215495,926,1874,43042,99513546,224950,215677,911,1880,43272,99513554,224685,215714,895,1845,43148,99513361,224991,215772,883,1799,43304,99513269,224748,215961,919,1865,43093,99513543,224568,216062,869,1866,43337,99513248,224739,215950,860,1801,43100,99513521,224755,215960,863,1784,43145,99513775,224566,215826,904,1808,43460,99513157,224624,216060,891,1882,43394,99512662,224927,216288,847,1873,43270,99513097,225052,215836,872,1880,43059,99513228,225234,215730,869,1849,43350,99513389,224927,215556,929,1872,43207,99512916,225329,215796,880,1866,43201,99513153,224764,216063,953,1846,43324,99513158,224777,215996,899,1826,43246,99513281,225041,215719,887,1774,43485,99512461,225057,216313,910,1790,43096,99513118,225506,215584,906,1807,43362,99512979,225212,215739,901,1826,43284,99513023,224787,216219,861,1875,43199,99512929,224844,216231,922,1810,43304,99512932,224872,216205,877,1744,43153,99512659,225803,215748,893,1750,43433,99512771,224690,216509,847,1787,43170,99512848,225730,215611,854,1792,43268,99512295,225719,216041,885,1820,43233,99512788,225109,216162,888,1784,43190,99512610,225587,215961,868,1815,43501,99512397,225510,215881,896,1841,43355,99512088,225955,215847,914,1755,43359,99512351,225753,215937,845,1773,43269,99512672,225214,216208,864,1814,43339,99512400,225860,215750,837,1778,43492,99511981,225669,216230,850,1779,43531,99512238,225420,216173,859,1715,43421,99512255,225421,216336,852,1800,43108,99512504,225890,215833,865,1818,43261,99512399,225462,216207,853,1802,43095,99511998,225956,216269,880,1792,43005,99512024,226390,215915,874,1734,43164,99512366,225974,215916,846,1748,43169,99512305,225803,216105,870,1744,43627,99511851,225620,216301,857,1757,43449,99512044,226087,215778,885,1760,43221,99512145,226002,216038,834,1774,43484,99511966,226053,215861,862,1810,42944,99512623,226051,215686,886,1725,43500,99512032,225796,216085,862,1726,43470,99512106,225629,216151,918]).reshape(100,6)
# wiki2 = np.array([8273,42395,1106725105,311867,336555,1089,7713,70439,1106467008,419823,459277,1024,4837,85866,1106350846,467217,515607,911,3231,89531,1106314868,504191,512652,811,2559,91081,1106294128,520585,516232,699,2229,92645,1106280272,525209,524202,727,2044,93025,1106272845,530725,525922,723,1816,93475,1106268199,533229,527829,736,1670,94018,1106265017,535460,528357,762,1627,93934,1106263421,538109,527456,737,1496,94589,1106260701,539645,528155,698,1465,94223,1106260041,541771,527057,727,1378,94108,1106259488,542021,527586,703,1422,93822,1106257954,543472,527950,664,1366,94388,1106256601,544000,528173,756,1319,94644,1106256777,543818,528062,664,1292,94799,1106255947,544316,528225,705,1235,94549,1106254736,545874,528237,653,1230,94840,1106254855,545154,528508,697,1285,94781,1106253837,545248,529448,685,1213,95010,1106253521,546792,527999,749,1179,95056,1106252816,547191,528337,705,1179,94785,1106252734,547319,528602,665,1130,94836,1106251963,547793,528866,696,1193,94373,1106252409,547018,529605,686,1192,94721,1106251709,547477,529537,648,1198,94811,1106251436,548253,528901,685,1143,94920,1106251351,547716,529488,666,1224,95066,1106250582,548674,529075,663,1206,95078,1106250052,548619,529693,636,1194,94571,1106250875,548527,529441,676,1154,94965,1106250553,548147,529798,667,1122,94644,1106250461,548391,530028,638,1149,94794,1106249561,549553,529536,691,1141,95029,1106249544,549322,529612,636,1113,94977,1106249645,548907,529985,657,1183,94849,1106249614,548723,530257,658,1181,94865,1106248959,549371,530274,634,1199,94727,1106248906,549371,530447,634,1121,95299,1106247791,550318,530119,636,1169,95143,1106249110,548779,530435,648,1147,95064,1106248409,549038,530989,637,1154,94904,1106248637,549771,530184,634,1141,95047,1106248543,550096,529816,641,1057,94966,1106247952,550012,530652,645,1197,95389,1106247917,549767,530342,672,1125,94797,1106248495,549839,530372,656,1125,94947,1106248316,549779,530483,634,1161,95400,1106247405,549943,530687,688,1131,94980,1106247734,551005,529831,603,1173,95112,1106247049,550840,530478,632,1137,95061,1106247128,550595,530742,621,1066,95315,1106247278,549251,531732,642,1171,95035,1106247622,550032,530791,633,1148,95412,1106247003,550989,530145,587,1063,95189,1106246635,550890,530874,633,1123,94741,1106247704,550208,530875,633,1096,94944,1106247028,551086,530504,626,1154,94904,1106247383,550305,530891,647,1092,95177,1106246634,550554,531248,579,1130,94650,1106246943,551090,530849,622,1133,95234,1106246425,550353,531585,554,1097,95568,1106246031,550614,531330,644,1125,94779,1106247146,550411,531189,634,1125,95169,1106246106,550974,531266,644,1075,94815,1106247062,550969,530766,597,1094,95364,1106245966,550768,531527,565,1117,94718,1106246496,551143,531223,587,1054,95121,1106247108,549905,531427,669,1084,94769,1106246845,550599,531409,578,1118,94987,1106246040,550887,531623,629,1087,95089,1106246396,551144,530907,661,1070,94985,1106246904,550890,530842,593,1097,95025,1106246598,550661,531319,584,1082,95362,1106245823,551327,531070,620,1108,95524,1106245620,551283,531129,620,1133,95118,1106245910,550725,531815,583,1099,95339,1106246159,551507,530568,612,1066,95364,1106245270,551800,531203,581,1122,94955,1106246101,552016,530448,642,1155,94965,1106245802,552007,530737,618,1112,95541,1106245389,550959,531644,639,1115,95341,1106245480,551468,531278,602,1102,95366,1106245475,551146,531614,581,1117,94835,1106245933,552272,530546,581,1097,94802,1106245745,552243,530820,577,1181,94893,1106245979,551477,531111,643,1137,94732,1106245581,551927,531295,612,1132,95020,1106245614,551744,531168,606,1068,95376,1106245410,551612,531211,607,1043,95323,1106244986,552339,531019,574,1108,95031,1106245889,552243,530387,626,1108,95205,1106245109,552330,530916,616,1107,95187,1106245069,551083,532224,614,1078,95089,1106245169,551841,531474,633,1061,95014,1106246106,552012,530487,604,1062,95541,1106244620,552051,531406,604,1141,95300,1106246036,550771,531454,582,1077,95234,1106245796,551489,531090,598,1061,94945,1106244910,552785,530990,593]).reshape(100,6)
# wiki103 = np.array([255500,1084984,71670961219,4998715,4724766,5041,232375,1912273,71663671317,8492501,7717194,4565,138149,2383345,71660030085,10627197,8848631,2818,90897,2512515,71659012922,11530096,8881262,2533,68887,2554330,71658361582,12064738,8978738,1950,58712,2596428,71657781813,12367161,9223900,2211,51573,2615937,71657495163,12588591,9277104,1857,47242,2627494,71657309854,12729862,9313799,1974,43762,2638694,71657181672,12830266,9334089,1742,40934,2644695,71657103914,12900240,9338708,1734,39487,2649190,71657034355,12964043,9341489,1661,37872,2654632,71656970051,13007815,9358034,1821,36707,2658522,71656922967,13054506,9355893,1630,35677,2659771,71656870319,13095876,9366857,1725,34257,2666276,71656811438,13130645,9385995,1614,33975,2667711,71656772687,13164458,9389811,1583,33386,2671954,71656728671,13195324,9399343,1547,32648,2673443,71656690527,13223220,9408802,1585,32291,2674557,71656664305,13242540,9414957,1575,31795,2675110,71656637329,13266707,9417718,1566,31077,2676234,71656606778,13290972,9423633,1531,30968,2678509,71656579113,13310530,9429634,1471,30492,2680488,71656553802,13330374,9433619,1450,30508,2681911,71656529265,13346405,9440724,1412,29758,2682277,71656510977,13362451,9443315,1447,29924,2685531,71656480982,13381789,9450552,1447,29344,2681926,71656472110,13396590,9448896,1359,29021,2684870,71656448127,13411303,9455500,1404,28801,2684915,71656430724,13426860,9457486,1439,28624,2686621,71656410866,13436326,9466469,1319,28449,2686961,71656397811,13450985,9464685,1334,28613,2688643,71656378543,13466477,9466582,1367,28199,2689120,71656359339,13483297,9468954,1316,27906,2690177,71656347271,13490920,9472651,1300,27946,2689438,71656335842,13502894,9472812,1293,27498,2690752,71656320820,13508494,9481353,1308,27405,2692476,71656305260,13518631,9485134,1319,27315,2691140,71656296729,13532392,9481371,1278,26827,2694072,71656277764,13541269,9488962,1331,26982,2690948,71656273222,13553911,9483856,1306,26545,2692489,71656261025,13561458,9487410,1298,26853,2695043,71656244830,13569301,9492932,1266,26583,2694547,71656240859,13573661,9493301,1274,26476,2695119,71656227617,13582092,9497641,1280,26543,2695516,71656217117,13593155,9496723,1171,26009,2698100,71656209056,13597396,9498460,1204,26183,2694790,71656200781,13605941,9501345,1185,26078,2695997,71656188326,13614798,9503813,1213,25707,2697102,71656179503,13620329,9506370,1214,25735,2699409,71656172910,13624643,9506291,1237,25825,2698795,71656161903,13636680,9505787,1235,25493,2696560,71656162547,13636825,9507656,1144,25340,2696674,71656150562,13646554,9509904,1191,25578,2699649,71656144132,13650020,9509715,1131,25420,2699692,71656135596,13654064,9514318,1135,25443,2698672,71656129388,13659905,9515698,1119,25182,2699662,71656122445,13665349,9516479,1108,25202,2699661,71656112931,13673179,9518122,1130,25472,2700991,71656108225,13674616,9519810,1111,24898,2699109,71656098530,13687025,9519566,1097,24892,2699792,71656098140,13686160,9520147,1094,24654,2701693,71656084578,13698127,9520077,1093,24515,2702688,71656081956,13693493,9526523,1050,25013,2700466,71656077597,13702970,9523055,1124,24540,2701819,71656071808,13708724,9522202,1132,24573,2702512,71656064396,13709197,9528451,1096,24446,2701930,71656060453,13713588,9528723,1085,24451,2700937,71656054876,13723563,9525309,1089,24446,2702836,71656047005,13726039,9528790,1109,24424,2702303,71656044474,13726807,9531144,1073,24205,2701090,71656035645,13738100,9530086,1099,24112,2702667,71656037060,13735539,9529813,1034,24187,2704155,71656030124,13740968,9529803,988,23844,2703987,71656019529,13744158,9537613,1094,23697,2701415,71656023917,13749159,9531027,1010,24005,2702890,71656012820,13753536,9535835,1139,24263,2704349,71656008532,13754125,9537887,1069,23835,2704571,71656006602,13757979,9536166,1072,23823,2704300,71655997320,13764673,9539046,1063,23767,2705871,71655992126,13768232,9539196,1033,23666,2704414,71655992391,13773443,9535261,1050,23649,2704643,71655988721,13771871,9540335,1006,23574,2707619,71655980752,13769366,9547844,1070,23632,2704504,71655979095,13781615,9540418,961,23452,2705858,71655977346,13779758,9542833,978,23537,2707435,71655973128,13784477,9540603,1045,23379,2707434,71655967779,13785774,9544850,1009,23495,2707035,71655960909,13793481,9544281,1024,23286,2708653,71655963097,13789866,9544322,1001,23289,2708985,71655950381,13797471,9549070,1029,23039,2705412,71655954218,13798910,9547675,971,22967,2706783,71655948108,13802007,9549339,1021,23138,2706815,71655945179,13802643,9551505,945,23011,2708096,71655940678,13810176,9547237,1027,23107,2707157,71655938797,13811085,9549078,1001,22846,2710014,71655936003,13809124,9551306,932,22730,2707755,71655933164,13821069,9544525,982,22971,2707940,71655928848,13818038,9551351,1077,23028,2707007,71655922837,13823773,9552623,957,22890,2706447,71655922931,13825017,9551953,987]).reshape(100,6)

# for i in range(5,20):
# 	for j in range(0,6):
# 		print("PTB: w1={ptb_1:12d}, w2={ptb_2:12d}, p_i={ptb_p:9.5f} - WikiText2: w1={w2_1:12d}, w2={w2_2:12d}, p_i={w2_p:9.5f} - WikiText103: w1={w103_1:12d}, w2={w103_2:12d}, p_i={w103_p:9.5f}".format(ptb_1=ptb[i-1,j],ptb_2=ptb[i,j],ptb_p=(ptb[i,j]-ptb[i-1,j])/ptb[i-1,j]*100,w2_1=wiki2[i-1,j],w2_2=wiki2[i,j],w2_p=(wiki2[i,j]-wiki2[i-1,j])/wiki2[i-1,j]*100,w103_1=wiki103[i-1,j],w103_2=wiki103[i,j],w103_p=(wiki103[i,j]-wiki103[i-1,j])/wiki103[i-1,j]*100))
# 		# print("PTB: {ptb_p:9.5f}, WikiText2: {w2_p:9.5f}, WikiText103: {w103_p:9.5f}".format(ptb_1=ptb[i-1,j],ptb_2=ptb[i,j],ptb_p=(ptb[i,j]-ptb[i-1,j])/ptb[i-1,j]*100,w2_1=wiki2[i-1,j],w2_2=wiki2[i,j],w2_p=(wiki2[i,j]-wiki2[i-1,j])/wiki2[i-1,j]*100,w103_1=wiki103[i-1,j],w103_2=wiki103[i,j],w103_p=(wiki103[i,j]-wiki103[i-1,j])/wiki103[i-1,j]*100))
# 	print("===============================================================")

# print("Between 1 and 5")
# for j in range(6):
# 		print("PTB: w1={ptb_1:12d}, w2={ptb_2:12d}, p_i={ptb_p:9.5f} - WikiText2: w1={w2_1:12d}, w2={w2_2:12d}, p_i={w2_p:9.5f} - WikiText103: w1={w103_1:12d}, w2={w103_2:12d}, p_i={w103_p:9.5f}".format(ptb_1=ptb[0,j],ptb_2=ptb[4,j],ptb_p=(ptb[4,j]-ptb[0,j])/ptb[0,j]*100,w2_1=wiki2[0,j],w2_2=wiki2[4,j],w2_p=(wiki2[4,j]-wiki2[0,j])/wiki2[0,j]*100,w103_1=wiki103[0,j],w103_2=wiki103[4,j],w103_p=(wiki103[4,j]-wiki103[0,j])/wiki103[0,j]*100))

# print("Between 6 and 20")
# for j in range(6):
# 		print("PTB: w1={ptb_1:12d}, w2={ptb_2:12d}, p_i={ptb_p:9.5f} - WikiText2: w1={w2_1:12d}, w2={w2_2:12d}, p_i={w2_p:9.5f} - WikiText103: w1={w103_1:12d}, w2={w103_2:12d}, p_i={w103_p:9.5f}".format(ptb_1=ptb[5,j],ptb_2=ptb[19,j],ptb_p=(ptb[19,j]-ptb[5,j])/ptb[5,j]*100,w2_1=wiki2[5,j],w2_2=wiki2[19,j],w2_p=(wiki2[19,j]-wiki2[5,j])/wiki2[5,j]*100,w103_1=wiki103[5,j],w103_2=wiki103[19,j],w103_p=(wiki103[19,j]-wiki103[5,j])/wiki103[5,j]*100))

# print("Between 20 and 100")
# for j in range(6):
# 		print("PTB: w1={ptb_1:12d}, w2={ptb_2:12d}, p_i={ptb_p:9.5f} - WikiText2: w1={w2_1:12d}, w2={w2_2:12d}, p_i={w2_p:9.5f} - WikiText103: w1={w103_1:12d}, w2={w103_2:12d}, p_i={w103_p:9.5f}".format(ptb_1=ptb[19,j],ptb_2=ptb[99,j],ptb_p=(ptb[99,j]-ptb[19,j])/ptb[19,j]*100,w2_1=wiki2[19,j],w2_2=wiki2[99,j],w2_p=(wiki2[99,j]-wiki2[19,j])/wiki2[19,j]*100,w103_1=wiki103[19,j],w103_2=wiki103[99,j],w103_p=(wiki103[99,j]-wiki103[19,j])/wiki103[19,j]*100))



# text8 = np.array([74785,287560,64437960321,1617650,2067996,98858,56761,436144,64436583726,2338717,2593503,98319,36078,507649,64436036790,2659805,2779624,87224,24256,514966,64435959774,2808122,2717040,83012,19831,518380,64435881223,2874921,2733662,79153,18171,524051,64435822643,2909553,2753478,79274,16800,526425,64435789286,2935674,2761448,77537,15959,527464,64435773195,2952586,2759245,78721,15250,528949,64435754987,2964435,2766633,76916,14756,531016,64435728467,2974911,2782110,75910,14388,532656,64435714473,2983401,2787653,74599,14083,533643,64435702897,2991586,2789379,75582,13784,534569,64435690031,2997131,2796323,75332,13640,535057,64435682323,3001558,2799574,75018,13373,534936,64435674898,3009428,2800708,73827,13213,534857,64435669389,3014261,2801718,73732,13074,534631,64435666271,3021969,2798998,72227,12899,535209,64435662192,3026140,2798451,72279,12818,536208,64435659830,3029717,2797991,70606,12638,535877,64435661786,3029295,2796541,71033,12581,536608,64435656064,3037788,2793863,70266,12532,535834,64435652703,3039922,2796547,69632,12379,536836,64435646378,3041143,2801442,68992,12352,537626,64435639161,3042671,2806016,69344,12150,536774,64435635970,3044804,2807931,69541,12093,538006,64435628563,3046511,2811846,70151,12035,539478,64435623600,3047545,2814776,69736,11845,538591,64435620787,3050817,2815519,69611,11976,537827,64435617738,3054822,2815842,68965,11737,538356,64435617556,3056316,2814423,68782,11703,538342,64435615387,3060466,2812944,68328,11566,538372,64435615855,3062240,2811273,67864,11601,538052,64435616056,3063518,2810364,67579,11416,538346,64435617115,3063911,2809130,67252,11534,537549,64435615744,3068430,2807445,66468,11394,538004,64435614572,3068313,2808201,66686,11218,538251,64435611616,3070654,2809079,66352,11250,538728,64435608336,3071409,2811453,65994,11095,539007,64435605214,3073627,2812313,65914,11036,539801,64435601273,3073242,2815145,66673,10960,539628,64435598326,3071490,2820393,66373,11123,538522,64435597823,3074795,2818254,66653,11105,539629,64435593054,3076872,2820435,66075,11074,540152,64435592906,3078280,2818594,66164,11103,539697,64435592103,3079861,2818798,65608,10906,540092,64435339408,3082155,2815385,65369,10946,539715,64435338772,3084214,2814788,64880,10918,539449,64435338496,3084851,2814934,64667,10719,540171,64435339120,3084794,2813993,64518,10717,539153,64435339100,3087174,2813009,64162,10704,539516,64435336120,3087858,2815183,63934,10496,539246,64435334505,3089696,2814988,64384,10679,540596,64435332695,3087592,2817665,64088,10478,540703,64435330536,3089481,2817707,64410,10463,541215,64435327644,3087313,2822612,64068,10462,541039,64435325702,3089407,2822580,64125,10510,540862,64435325771,3091670,2820597,63905,10414,540798,64435325471,3092644,2820329,63659,10500,540566,64435323401,3094405,2821093,63350,10530,540969,64435322647,3094541,2821394,63234,10424,540115,64435324603,3094963,2819912,63298,10448,540868,64435324567,3096519,2817615,63298,10201,540722,64435323998,3095778,2819667,62949,10234,540417,64435323396,3100429,2816199,62640,10140,540723,64435322307,3098154,2819670,62321,10135,540743,64435321680,3099091,2819148,62518,10125,540865,64435319151,3101903,2819064,62207,10278,541339,64435318610,3098056,2822145,62887,10041,540649,64435315729,3101965,2822396,62535,10270,540572,64435316711,3101821,2821611,62330,10158,540829,64435314213,3104643,2821220,62252,10081,540844,64435315062,3101993,2823198,62137,10105,540841,64435312916,3104458,2823294,61698,10064,541753,64435312694,3104591,2822147,62066,9861,541695,64435313589,3104307,2822119,61744,9965,541271,64435312239,3106693,2821551,61596,10090,541933,64435310540,3106425,2823234,61093,9889,541383,64435313039,3104979,2822912,61113,9976,541713,64435311503,3108092,2821233,60798,9852,541931,64435309841,3108101,2822545,61045,9913,542304,64435307943,3107162,2824861,61132,9884,541484,64435307223,3110712,2822745,61267,9684,540973,64435308292,3109356,2823598,61412,9774,541377,64435307394,3110592,2823120,61058,9739,542076,64435304730,3110755,2825296,60719,9772,541109,64435305802,3110509,2825455,60668,9651,540640,64435304388,3112338,2825788,60510,9669,541830,64435304326,3111369,2825561,60560,9673,541119,64435303008,3115775,2823344,60396,9819,540824,64435304337,3114947,2823166,60222,9665,541855,64435304827,3113315,2823381,60272,9632,541639,64435303387,3115581,2822383,60693,9794,541839,64435303926,3112881,2824359,60516,9592,541520,64435301258,3117681,2823307,59957,9535,541658,64435301782,3116641,2823577,60122,9561,541765,64435301929,3114766,2824892,60402,9471,543471,64435297975,3117011,2825526,59861,9654,541988,64435299907,3114827,2826738,60201,9503,542005,64435300589,3117306,2823969,59943,9629,541937,64435297498,3118556,2825830,59865]).reshape(100,6)
text8 = np.array([57637,304708,64437960321,1617650,2150362,16492,38929,453976,64436583726,2338717,2676244,15578,22109,521618,64436036790,2659805,2854503,12345,13597,525625,64435959774,2808122,2788047,12005,10539,527672,64435881223,2874921,2802392,10423,9494,532728,64435822643,2909553,2821855,10897,8590,534635,64435789286,2935674,2829119,9866,8176,535247,64435773195,2952586,2827670,10296,7711,536488,64435754987,2964435,2833997,9552,7326,538446,64435728467,2974911,2848279,9741,7023,540021,64435714473,2983401,2853273,8979,6803,540923,64435702897,2991586,2855661,9300,6636,541717,64435690031,2997131,2862817,8838,6614,542083,64435682323,3001558,2865666,8926,6424,541885,64435674898,3009428,2865994,8541,6273,541797,64435669389,3014261,2866799,8651,6112,541593,64435666271,3021969,2863014,8211,6111,541997,64435662192,3026140,2862306,8424,5996,543030,64435659830,3029717,2860628,7969,5893,542622,64435661786,3029295,2859334,8240,5797,543392,64435656064,3037788,2856221,7908,5919,542447,64435652703,3039922,2858264,7915,5851,543364,64435646378,3041143,2862726,7708,5730,544248,64435639161,3042671,2867526,7834,5582,543342,64435635970,3044804,2869824,7648,5687,544412,64435628563,3046511,2874306,7691,5594,545919,64435623600,3047545,2877097,7415,5481,544955,64435620787,3050817,2877600,7530,5552,544251,64435617738,3054822,2877429,7378,5430,544663,64435617556,3056316,2875757,7448,5358,544687,64435615387,3060466,2874042,7230,5301,544637,64435615855,3062240,2871837,7300,5253,544400,64435616056,3063518,2870824,7119,5148,544614,64435617115,3063911,2869249,7133,5377,543706,64435615744,3068430,2866980,6933,5215,544183,64435614572,3068313,2867849,7038,5085,544384,64435611616,3070654,2868508,6923,5076,544902,64435608336,3071409,2870557,6890,4925,545177,64435605214,3073627,2871464,6763,5000,545837,64435601273,3073242,2874900,6918,4934,545654,64435598326,3071490,2880025,6741,4995,544650,64435597823,3074795,2878128,6779,4919,545815,64435593054,3076872,2879843,6667,4997,546229,64435592906,3078280,2878118,6640,5011,545789,64435592103,3079861,2877839,6567,4837,546161,64435339408,3082155,2874085,6669,4884,545777,64435338772,3084214,2873214,6454,4900,545467,64435338496,3084851,2873203,6398,4792,546098,64435339120,3084794,2872066,6445,4790,545080,64435339100,3087174,2870612,6559,4866,545354,64435336120,3087858,2872789,6328,4683,545059,64435334505,3089696,2872941,6431,4743,546532,64435332695,3087592,2875425,6328,4633,546548,64435330536,3089481,2875802,6315,4639,547039,64435327644,3087313,2880445,6235,4723,546778,64435325702,3089407,2880422,6283,4645,546727,64435325771,3091670,2878322,6180,4602,546610,64435325471,3092644,2877754,6234,4657,546409,64435323401,3094405,2878368,6075,4671,546828,64435322647,3094541,2878488,6140,4569,545970,64435324603,3094963,2877160,6050,4589,546727,64435324567,3096519,2874795,6118,4517,546406,64435323998,3095778,2876554,6062,4486,546165,64435323396,3100429,2872768,6071,4551,546312,64435322307,3098154,2876091,5900,4523,546355,64435321680,3099091,2875802,5864,4340,546650,64435319151,3101903,2875377,5894,4569,547048,64435318610,3098056,2879229,5803,4421,546269,64435315729,3101965,2879203,5728,4479,546363,64435316711,3101821,2878160,5781,4497,546490,64435314213,3104643,2877681,5791,4389,546536,64435315062,3101993,2879539,5796,4417,546529,64435312916,3104458,2879279,5713,4455,547362,64435312694,3104591,2878463,5750,4337,547219,64435313589,3104307,2878223,5640,4312,546924,64435312239,3106693,2877463,5684,4332,547691,64435310540,3106425,2878706,5621,4378,546894,64435313039,3104979,2878463,5562,4396,547293,64435311503,3108092,2876528,5503,4292,547491,64435309841,3108101,2878070,5520,4326,547891,64435307943,3107162,2880488,5505,4341,547027,64435307223,3110712,2878525,5487,4193,546464,64435308292,3109356,2879482,5528,4301,546850,64435307394,3110592,2878724,5454,4298,547517,64435304730,3110755,2880488,5527,4278,546603,64435305802,3110509,2880676,5447,4144,546147,64435304388,3112338,2880964,5334,4089,547410,64435304326,3111369,2880772,5349,4172,546620,64435303008,3115775,2878247,5493,4170,546473,64435304337,3114947,2878142,5246,4149,547371,64435304827,3113315,2878252,5401,4149,547122,64435303387,3115581,2877571,5505,4202,547431,64435303926,3112881,2879595,5280,4140,546972,64435301258,3117681,2877996,5268,4064,547129,64435301782,3116641,2878364,5335,4132,547194,64435301929,3114766,2879966,5328,4061,548881,64435297975,3117011,2880179,5208,4126,547516,64435299907,3114827,2881664,5275,4085,547423,64435300589,3117306,2878822,5090,4134,547432,64435297498,3118556,2880465,5230]).reshape(100,6)
text8_subset = np.array([9947,46968,7947943084,336648,525964,18881,7576,71675,7947714052,444267,625089,18833,4928,84699,7947622858,486952,665962,16093,3291,86236,7947603180,522525,650847,15412,2701,86673,7947590861,534401,652509,14347,2448,87708,7947583609,537856,655183,14688,2296,87955,7947578125,541439,657699,13978,2217,88194,7947575601,543382,657502,14596,2091,88739,7947571332,546688,658564,14078,2061,89007,7947568960,546133,661230,14101,2008,89251,7947566693,547972,661846,13722,1985,89403,7947565378,548174,662510,14042,1894,89637,7947564062,548256,663496,14147,1861,90123,7947561442,548983,664935,14148,1865,89811,7947560944,550241,664846,13785,1863,89910,7947560459,550048,665348,13864,1893,89722,7947559748,551828,664681,13620,1802,89339,7947559911,552700,664171,13569,1752,89789,7947558461,553697,664728,13065,1829,89700,7947559777,553591,663293,13302,1749,89838,7947559199,554275,663435,12996,1734,89845,7947558495,554236,664423,12759,1710,89683,7947557613,555251,664584,12651,1779,90391,7947556275,554592,665414,13041,1733,90005,7947556507,554463,665578,13206,1678,90112,7947554692,555229,666581,13200,1657,90053,7947555212,554480,666836,13254,1716,90513,7947553664,555452,666829,13318,1655,90406,7947553386,554959,668155,12931,1612,90386,7947553912,555348,667203,13031,1666,90088,7947553193,557083,666647,12815,1577,90604,7947553418,556813,666282,12798,1639,90183,7947553369,557201,666434,12666,1582,90513,7947553443,557381,665824,12749,1636,90348,7947552735,558957,665169,12647,1629,90344,7947553162,557995,665831,12531,1596,90245,7947552714,559253,665244,12440,1633,90131,7947552473,558977,665786,12492,1610,90244,7947551369,558908,666887,12474,1579,90598,7947551725,558046,666827,12717,1586,90680,7947551144,557500,667953,12629,1589,90304,7947551347,558389,667027,12836,1549,90231,7947550399,558921,667683,12709,1586,90376,7947550885,559235,666785,12625,1515,90427,7947550215,559146,667833,12356,1547,90161,7947550298,559767,667522,12197,1541,90460,7947549785,560463,666952,12291,1484,90356,7947550192,560813,666541,12106,1555,90625,7947550348,560103,666682,12179,1512,90252,7947550549,560220,666959,12000,1533,90029,7947550307,561778,665781,12064,1526,90651,7947460533,560948,666516,12161,1511,90492,7947460364,560717,666936,12315,1531,90467,7947460101,560190,667756,12290,1457,90481,7947459464,561609,667335,11989,1549,90513,7947459762,560784,667650,12077,1541,90592,7947459976,560198,667754,12274,1566,90715,7947459268,561028,667567,12191,1523,90770,7947459092,560782,668055,12113,1422,90759,7947459424,561467,667042,12221,1478,90833,7947458422,561706,667906,11990,1488,90741,7947459445,561773,666836,12052,1471,90794,7947459522,561738,666953,11857,1476,90638,7947458744,562665,666954,11858,1495,90346,7947459552,562164,667020,11758,1470,90598,7947458747,561567,667939,12014,1462,91017,7947458068,562615,667356,11817,1436,90229,7947459345,562005,667476,11844,1447,90721,7947458788,561454,667936,11989,1438,90371,7947458688,561619,668177,12042,1487,90526,7947458167,561859,668565,11731,1477,90139,7947458721,562969,667415,11614,1457,90651,7947457458,562344,668704,11721,1464,90522,7947457656,563131,667842,11720,1389,90567,7947458001,562226,668400,11752,1478,90641,7947457569,562930,668041,11676,1486,90540,7947457455,563662,667601,11591,1450,90633,7947457760,562015,668846,11631,1392,90773,7947456882,564210,667657,11421,1418,90618,7947457525,563464,667674,11636,1417,90741,7947457121,563273,668148,11635,1406,91012,7947456625,563547,668130,11615,1424,90792,7947456938,563655,667800,11726,1370,90722,7947457606,563687,667139,11811,1411,91067,7947456995,562331,668875,11656,1405,90907,7947456453,563438,668495,11637,1384,90415,7947456739,563443,668793,11561,1370,90507,7947457170,563309,668388,11591,1427,90743,7947456589,564260,667825,11491,1405,91047,7947457135,562653,668531,11564,1392,91159,7947456623,563288,668486,11387,1397,90518,7947456681,563920,668354,11465,1337,90675,7947457197,564080,667510,11536,1432,90909,7947455994,564720,667934,11346,1371,91128,7947455896,564675,667756,11509,1365,90241,7947456706,564354,667938,11731,1385,90630,7947456801,564221,667733,11565,1279,90724,7947457172,563822,667710,11628,1412,90598,7947456080,565301,667516,11428,1348,91000,7947456310,563429,668757,11491]).reshape(100,6)
text8_subset_wor = np.array([10452,52093,1268621946,340784,434152,1843,7851,77129,1268392717,452593,529423,1557,5097,90145,1268304064,495031,565605,1328,3486,91828,1268285194,529087,550430,1244,2842,92289,1268273742,540740,550514,1143,2587,93339,1268266214,544774,553186,1170,2444,93529,1268261385,548343,554421,1148,2346,93833,1268258188,550401,555379,1123,2228,94321,1268254539,553372,555651,1159,2192,94589,1268252103,553001,558272,1113,2119,94931,1268250259,554680,558156,1125,2115,94831,1268248576,555105,559528,1115,2018,95161,1268247055,555482,560452,1102,1990,95657,1268244559,556135,561809,1120,1975,95358,1268244399,557136,561282,1120,1965,95397,1268243809,557045,561984,1070,2005,95146,1268243437,558783,560811,1088,1929,94905,1268243602,559124,560692,1018,1865,95371,1268242541,560252,560228,1013,1944,95213,1268243794,560103,559167,1049,1872,95490,1268243401,560451,559028,1028,1845,95415,1268242922,560164,559947,977,1803,95221,1268242097,561244,559901,1004,1880,95916,1268240538,560956,560960,1020,1835,95593,1268240495,560883,561406,1058,1775,95630,1268238665,561706,562473,1021,1755,95602,1268239185,561123,562574,1031,1829,96086,1268237533,561913,562863,1046,1747,95849,1268237579,561597,563519,979,1716,95846,1268238084,561978,562608,1038,1770,95566,1268237589,563410,561977,958,1679,96167,1268237740,563056,561569,1059,1748,95732,1268237765,563530,561509,986,1700,96052,1268237867,563669,560977,1005,1759,95833,1268237246,565208,560222,1002,1742,95843,1268237705,563987,561037,956,1687,95721,1268237431,565494,559973,964,1710,95683,1268237161,565233,560488,995,1726,95728,1268236000,564936,561929,951,1673,96130,1268236011,564612,561900,944,1697,96228,1268235504,563929,562946,966,1699,95843,1268235526,564976,562251,975,1646,95668,1268234999,565288,562685,984,1680,95883,1268235426,565507,561799,975,1625,95892,1268235050,565302,562437,964,1648,95646,1268235140,565740,562177,919,1653,95882,1268234712,566608,561446,969,1579,95934,1268235165,566941,560739,912,1650,96190,1268235240,566133,561131,926,1611,95725,1268235577,566413,561034,910,1639,95562,1268235248,567780,560052,989,1629,96049,1268234531,567122,561040,899,1603,96131,1268234481,566541,561534,980,1632,95956,1268234173,566134,562414,961,1560,95920,1268233697,567612,561549,932,1648,95983,1268233980,566680,562061,918,1633,96038,1268233983,566399,562244,973,1666,96190,1268233286,567238,561941,949,1610,96255,1268233260,566856,562347,942,1510,96277,1268233367,567431,561760,925,1576,96240,1268232833,567612,562107,902,1595,96154,1268233654,567857,561045,965,1574,96220,1268233850,567639,561058,929,1573,96063,1268233078,568433,561231,892,1575,95825,1268233954,567848,561190,878,1571,96103,1268232995,567516,562129,956,1557,96460,1268232314,568397,561626,916,1524,95744,1268233610,567896,561569,927,1551,96233,1268233006,567461,562108,911,1546,95842,1268232825,567770,562370,917,1591,96063,1268232450,567626,562631,909,1574,95621,1268233074,569101,561046,854,1552,96124,1268231852,568393,562452,897,1545,95997,1268232118,568855,561856,899,1482,96016,1268232341,568303,562232,896,1575,96082,1268232055,568877,561798,883,1577,95926,1268232065,569552,561237,913,1539,96027,1268232354,567860,562579,911,1484,96218,1268231522,569874,561298,874,1508,96182,1268232042,569217,561435,886,1512,96184,1268231678,568875,562099,922,1484,96447,1268231132,569329,561954,924,1507,96343,1268231309,569478,561738,895,1477,96206,1268231970,569625,561069,923,1516,96438,1268231520,568237,562669,890,1503,96314,1268231210,569160,562148,935,1495,95784,1268231290,569346,562488,867,1464,95912,1268231679,569257,562094,864,1536,96186,1268231308,569826,561471,943,1512,96480,1268231743,568618,562054,863,1486,96568,1268231372,569038,561948,858,1493,96048,1268231311,569552,561996,870,1418,96111,1268231752,569583,561527,879,1511,96364,1268230935,570055,561566,839,1467,96498,1268230655,570440,561345,865,1457,95691,1268231178,570134,561911,899,1477,95995,1268231409,570056,561400,933,1375,96197,1268231735,569688,561396,879,1513,95961,1268230727,571033,561158,878,1444,96457,1268230924,569171,562397,877]).reshape(100,6)
# text8_subset_wor_4 = np.array([10716,53972,621344865,328279,390252,222,7891,79186,621121022,440625,479514,68,5131,92283,621033887,483073,513897,35,3488,94190,621015637,515517,499455,18,2891,94440,621004655,527076,499228,16,2617,95494,620997526,530979,501678,12,2451,95736,620992793,534704,502611,11,2395,96042,620989599,536203,504061,6,2250,96536,620986096,539328,504088,8,2199,96807,620983732,539427,506132,9,2160,97016,620982009,540965,506153,3,2133,97100,620980411,541209,507444,9,2014,97392,620978924,541841,508131,4,1998,97783,620976536,542319,509663,7,1990,97509,620976313,543394,509093,7,1988,97619,620975811,543254,509628,6,2048,97314,620975457,544889,508590,8,1961,96998,620975593,545250,508501,3,1886,97506,620974684,546202,508025,3,1973,97523,620975739,546218,506850,3,1891,97723,620975368,546424,506897,3,1871,97595,620975031,546345,507459,5,1847,97423,620974175,547525,507335,1,1907,98099,620972732,546825,508741,2,1868,97594,620972673,547167,509002,2,1794,97713,620970839,547979,509979,2,1784,97624,620971348,547389,510159,2,1857,98090,620969785,548240,510332,2,1815,97801,620969836,547969,510884,1,1740,97897,620970409,547993,510262,5,1796,97559,620969844,549569,509535,3,1701,98175,620969974,549276,509178,2,1770,97654,620970037,549456,509240,0,1709,98266,620970148,549660,508523,0,1779,98024,620969453,551391,507657,2,1748,98023,620969937,550151,508447,0,1720,97992,620969622,551404,507566,2,1770,97932,620969392,551094,508115,3,1728,97913,620968247,551133,509283,2,1699,98249,620968344,550787,509226,1,1727,98296,620967815,550167,510299,2,1718,97989,620967924,551060,509614,1,1678,97759,620967313,551826,509728,2,1715,97921,620967806,551627,509237,0,1640,98018,620967370,551315,509963,0,1654,97774,620967473,551775,509628,2,1658,98091,620967070,552536,508948,3,1606,98011,620967634,552869,508184,2,1679,98255,620967661,552066,508645,0,1632,98017,620967865,552478,508314,0,1668,97707,620967672,553804,507454,1,1652,98184,620966991,553115,508364,0,1645,98252,620966795,552636,508975,3,1667,98096,620966388,552298,509857,0,1570,98123,620965912,553896,508804,1,1655,98074,620966409,552918,509248,2,1679,98108,620966493,552409,509617,0,1676,98422,620965719,553011,509476,2,1651,98307,620965801,552923,509623,1,1521,98391,620965805,553585,509002,2,1590,98449,620965096,553832,509338,1,1618,98388,620966054,553906,508339,1,1597,98403,620966254,553536,508515,1,1595,98252,620965501,554396,508561,1,1604,98127,620966375,553718,508480,2,1575,98307,620965519,553377,509527,1,1584,98606,620964736,554573,508806,1,1560,97875,620966083,553923,508864,1,1568,98371,620965417,553527,509422,1,1556,98004,620965277,553708,509759,2,1594,98091,620964864,553894,509862,1,1579,97789,620965594,555097,508247,0,1586,98231,620964416,554347,509726,0,1580,98038,620964615,554860,509211,2,1510,98195,620964826,554363,509412,0,1608,98177,620964629,554962,508930,0,1589,98222,620964498,555344,508653,0,1558,98170,620964819,554064,509693,2,1511,98455,620964022,555782,508536,0,1537,98212,620964487,555467,508603,0,1548,98478,620963998,555018,509262,2,1534,98592,620963519,555282,509379,0,1533,98423,620963862,555639,508849,0,1505,98332,620964470,555539,508459,1,1536,98589,620964017,554334,509829,1,1517,98429,620963703,555215,509441,1,1503,97987,620963797,555210,509809,0,1506,98092,620964151,555344,509210,3,1541,98438,620963762,555773,508791,1,1537,98609,620964320,554568,509272,0,1492,98688,620963877,555218,509030,1,1499,98203,620963883,555396,509325,0,1438,98377,620964195,555652,508644,0,1561,98549,620963447,556109,508638,2,1500,98708,620963194,556448,508456,0,1483,97858,620963857,555955,509153,0,1509,98216,620963942,555809,508830,0,1396,98353,620964111,555763,508681,2,1508,98138,620963202,557059,508399,0,1456,98512,620963503,555233,509601,1]).reshape(100,6)

print("Between 1 and 5")
for j in range(6):
		print("text8: w1={text8_1:12d}, w2={text8_2:12d}, p_i={text8_p:9.5f} - text8_subset: w1={text8_subset_1:12d}, w2={text8_subset_2:12d}, p_i={text8_subset_p:9.5f} - text8_subset_wor: w1={text8_subset_wor_1:12d}, w2={text8_subset_wor_2:12d}, p_i={text8_subset_wor_p:9.5f}".format(text8_1=text8[0,j],text8_2=text8[4,j],text8_p=(text8[4,j]-text8[0,j])/text8[0,j]*100,text8_subset_1=text8_subset[0,j],text8_subset_2=text8_subset[4,j],text8_subset_p=(text8_subset[4,j]-text8_subset[0,j])/text8_subset[0,j]*100,text8_subset_wor_1=text8_subset_wor[0,j],text8_subset_wor_2=text8_subset_wor[4,j],text8_subset_wor_p=(text8_subset_wor[4,j]-text8_subset_wor[0,j])/text8_subset_wor[0,j]*100))

print("Between 6 and 20")
for j in range(6):
		print("text8: w1={text8_1:12d}, w2={text8_2:12d}, p_i={text8_p:9.5f} - text8_subset: w1={text8_subset_1:12d}, w2={text8_subset_2:12d}, p_i={text8_subset_p:9.5f} - text8_subset_wor: w1={text8_subset_wor_1:12d}, w2={text8_subset_wor_2:12d}, p_i={text8_subset_wor_p:9.5f}".format(text8_1=text8[5,j],text8_2=text8[19,j],text8_p=(text8[19,j]-text8[5,j])/text8[5,j]*100,text8_subset_1=text8_subset[5,j],text8_subset_2=text8_subset[19,j],text8_subset_p=(text8_subset[19,j]-text8_subset[5,j])/text8_subset[5,j]*100,text8_subset_wor_1=text8_subset_wor[5,j],text8_subset_wor_2=text8_subset_wor[19,j],text8_subset_wor_p=(text8_subset_wor[19,j]-text8_subset_wor[5,j])/text8_subset_wor[5,j]*100))

print("Between 20 and 100")
for j in range(6):
		print("text8: w1={text8_1:12d}, w2={text8_2:12d}, p_i={text8_p:9.5f} - text8_subset: w1={text8_subset_1:12d}, w2={text8_subset_2:12d}, p_i={text8_subset_p:9.5f} - text8_subset_wor: w1={text8_subset_wor_1:12d}, w2={text8_subset_wor_2:12d}, p_i={text8_subset_wor_p:9.5f}".format(text8_1=text8[19,j],text8_2=text8[99,j],text8_p=(text8[99,j]-text8[19,j])/text8[19,j]*100,text8_subset_1=text8_subset[19,j],text8_subset_2=text8_subset[99,j],text8_subset_p=(text8_subset[99,j]-text8_subset[19,j])/text8_subset[19,j]*100,text8_subset_wor_1=text8_subset_wor[19,j],text8_subset_wor_2=text8_subset_wor[99,j],text8_subset_wor_p=(text8_subset_wor[99,j]-text8_subset_wor[19,j])/text8_subset_wor[19,j]*100))