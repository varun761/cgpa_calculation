import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

xValues, yValues = [], []
scatteredness = 0.6
m = 2
c = 3
xValues = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9713173954877199, 1.0928721356923226, 1.0625086309362242, 0.8737110887933616, 0.5830920125180852, 1.7180941328460224, -0.3109069031254128, 1.6811473916406023, 1.0714248114887612, -0.38973052208643844, 0.43908708289442333, 1.1205602358426214, 2.091271463777937, 1.5530394891538835, 0.7190955511238692, 1.3177966418126057, 0.49327716704350744, 2.1430912884651954, 0.3415528158522141, 0.7447025261589497, 0.2625201238070458, -0.12977376728266998, 0.7037403664165481, 1.6313116600731603, 0.82944866484717, 0.7907253704572064, 1.2988768477558648, 1.6756669861137263, 0.5226856934840924, 1.2493607678595686, 1.2041779874967389, 0.5715176359216081, 0.4034878210417774, -0.2525478522807052, 1.1099809053833323, 1.0414798648513706, 0.49072894813387746, 0.07075801141560134, 1.1167469399572043, 2.2772169244253675, 0.9916053467452945, 0.9888117915270043, 0.11491369365257631, 1.4055375058795656, 1.8743423117507618, 1.9522488025165894, 1.5238594890999069, 1.8599755390663515, 2.7817311268181832, 0.1269817007926024, 2.608071134698273, 4.74000411690964, 1.10208354299529, 3.404439412717152, 0.7974701458661997, 3.4425284682265236, 1.1642340276525873, 1.074277329549477, 2.094992365770081, 2.071830473388265, 0.4602849428989124, 1.2227027086527973, 2.2052152229313626, 1.332691097612066, 0.3317215072501667, 2.7828578841563045, 4.3004327102184465, -0.621214837294461, 1.3095400398212806, 2.6020244732380644, 2.36809679268031, 2.9658344131083045, 1.0800795247506525, 1.3850406179800006, 1.3950525866233512, 2.8631668139054995, 2.3503468612529725, 5.06477862785034, 2.520115050892003, 0.7770440659645517, 3.7199362085542997, 3.283662668874638, 8.427141043829657, 0.7572035659721967, 4.4510527566884726, 2.1006840293679567, 4.8136473856169975, 3.3802969330117847, 2.185471747713195, 2.940843963612234, 3.2283666520343757, 2.8308353924725287, 1.3445382343056866, 4.286238007456234, 3.4753990414689495, -0.28446834204075255, 2.4514278118281885, 0.6174460826264756, 2.6000470359739944, 4.716950084213461, 0.481931836901599, 2.5085530630305795, 4.905342973298864, 4.5141261848528, 3.7011533099176965, 1.156857371162101, 6.898089311971141, 0.2894259940821966, 2.9959828840517835, 4.76559057315179, 4.796262092995519, 4.599648859814222, 2.7428017909021993, 1.7597204537551596, 5.566428255703012, 5.7807859938420165, 3.8590266630576675, -0.4364010176848252, 3.375058361595403, 2.8263501069259718, 5.823298646592655, 0.5100006885803041, 2.5415319171615067, 4.901974855719014, 6.090823506805671, 6.220348812219804, 7.388188878088037, -0.13781734334752382, 4.438397013702103, 4.755590016777285, 3.7957249272208484, -0.3740539488224979, 5.251641831774424, -1.606569922225992, 5.48487400596545, 3.5386078907078247, 0.892923889690171, 4.664208451053654, 8.681627656333797, 4.7250185211304965, 5.109815739675442, 2.0871570317476946, 3.8081271141829873, 3.3758927193554786, 3.376461921329472, 3.315236846076675, 6.068103628129133, -0.7641152850065307, 1.3905153911934236, 2.3837581088585003, 3.5229366465427967, 1.8007401592018928, 4.784506445338955, 9.688476996854995, 3.891088537340428, 8.821935851750965, 4.598843775639148, 9.472069086103167, 7.32225958329388, 1.7040862632148586, 7.959365678704355, 7.727575481735776, 9.987247358421731, 7.170557664077454, 6.894322240328086, 10.054931635246032, 5.2268895835344, 6.292421028897005, 4.604592797233523, 7.189290215777456, 4.366483533543398, 6.051965832239919, 3.9281972403542165, 11.99744788990457, 3.4093513108184843, 1.5227901212327626, 8.078539825986908, 2.0248175664224215, 3.3605541104880245, 3.6002681134665577, 2.124570728445576, 6.7233288436324266, 4.496089506237674, -0.2057689026209708, 7.919969502101641, 2.8105667846070794, 6.689539904289684, 7.034519629809509, 10.30559915970415, 8.141965313953124, 8.653005187102135, 3.5604997026255707, 4.726525919973389, 6.3145122146611055, 3.197496120159492, 9.827505916155896, 9.532306041791824, 4.135967921327843, 2.0570029180165275, 12.082827497735863, 3.224251150072826, 3.201991133241874, 6.472627966659098, 5.893876299435982, 4.386146996738963, 3.7712129918675776, 6.298189179590743, 12.222669382493331, 8.8633134485023, 2.645060059982886, 2.212947891631342, 10.265910930398968, 6.64675612714662, 9.005307866851243, 5.544158897136127, 3.8395920417643445, 1.7138627779231648, 6.290480166872918, 15.629860581586248, 9.649418792614597, 6.149330349310378, 8.139001531407052, 12.322547599458876, 7.026812721016478, 8.407348743505814, -1.15325343326902, 13.787937075082862, 10.336332424852408, 10.05245476362375, 8.99317531755276, 13.048594322782117, 12.809531792009857, 12.972585217850014, 1.782636040963478, 11.820097549512518, 9.053502304740691, 14.770382341252715, 11.401332782833272, -4.952336004073462, 7.701636922640511, 8.889483502074983, 6.092011771223598, 5.657468084830672, 13.540020789948741, 9.320464225537265, 8.80044809570298, 2.8560087890259984, 8.85680181733829, 9.434905464273946, 4.712656326406313, 14.849656152047345, 8.536339464340086, 7.8123802196954735, 6.36368084681493, 5.8491220532243045, 8.14322958371624, 2.526855974222925, 9.037330946788357, 11.542310830771799, 5.101051675129632, 4.8182506528180244, 7.127430191294912, 5.120013889892753, 4.054814836617425, 5.35187293041144, 15.649214134308156, 5.011855175092547, 11.124298897272924, -1.6432532761287, 3.967463038535243, 11.957814134172212, 2.6432226733979016, 8.845715491353936, 7.618194511288528, 11.639096950411494, 7.308863842806973, 2.2058765265723297, 8.818936804531447, -0.04939851259511485, 7.995905619744402, -0.10260885605920755, 4.835380258640682, 7.945664883839297, 10.324694092600655, 13.740903588062817, 12.344851400862229, 7.616012344042191, 9.68244741321892, 3.1108889735438634, 11.922640530201745, 11.259808990690296, 12.025677610560948, 2.9592363848991523, 15.187215492817725, 12.21323775742626, 8.214962293629089, 12.816600728897981, 7.904549325932364, 2.458029585209685, 18.655631419926763, 14.600407871100437, 9.071487388463588, 9.617508286155205, 9.097309503777183, 6.099183625844251, 6.932433182064788, 6.75590819029796, 7.08129622939116, 10.792096289757632, 9.632263401265769, 4.083844331000959, 14.25141379304543, 12.923619719173047, 2.729800929208473, 13.922339577829092, 14.279929998129184, 11.21024199608044, 18.00106392722808, 4.9201528932337855, 13.784480964663636, 13.915806189247876, 10.215837796251185, 27.14963741479282, 9.419022364364265, 13.123545111784619, 10.930277318473607, 10.023902335622305, -1.2228377612154802, 13.720071918850916, 7.37526059804478, 16.877453522921492, 6.427637238631849, 10.320284763930287, 10.546130375802711, 3.1034172134139624, 3.6608439444821625, 13.2457745100054, 12.73119089445492, 14.028961851116637, 9.154986002034287, 12.40334447847853, 3.982754156258114, 2.6315660152925417, 16.00336799714147, 15.401412559288072, 18.06821923303995, 9.275855105347556, 14.959246587039328, 11.016583406215435, 9.87410691044846, 20.724244659005734, 22.526700070245205, 20.51189411767617, 9.969357047023829, -3.9016059955689517, 4.405067341171989, -1.4106153833367063, 7.176234843913843, 4.6680921571412926, 9.661559891984137, 5.369327498432152, -0.1529548103178957, 19.320281416544162, 10.220405869807957, 15.635615367042025, 21.79790919082535, 12.640256239876123, -4.0700398488818035, 12.448870559746016, 5.515891273189958, -5.7252932705772785, 7.87216793243581, 12.070832816885263, 16.756514867015692, 14.181312361517106, 18.637792552033112, 11.616943697949077, 13.129888490272272, 9.562418757837232, 17.75630440918946, 12.94332921446392, 2.866771478198446, 11.469797486193642, 8.345484500997973, 10.16213494720209, 12.457667058040254, 18.012498388185815, 15.634252918459488, 28.27745406528038, 11.503055576218754, 14.944644866704547, 14.625925901711808, 11.796672011265763, 17.101945108093034, 9.446827729730394, 2.0799085406904005, 9.436374261842614, 15.93075704306608, 12.251815308130512, 11.672387587996784, 7.7285439361009285, 5.1570094070787675, 15.463644710361205, 3.526288934590493, 28.19590724341903, 5.815650682429155, 8.885559708436544, 1.1349873713044332, 12.28080428449585, 12.88035499360015, 3.2362368418813183, 18.362877660356986, 24.603192840084244, 18.308050870542278, 
4.818677433779428, -5.8516761138466045, 13.30715760942202, 15.21943089049032, 14.717080032209049, 19.61691359540418, 26.550069285717782, 21.285905487601134, 6.7938857784604565, 1.4322662041698937, 16.21865406030192, 13.52566589176711, 17.006321438384756, 7.104117531651905, 9.61481186901622, 1.4052851305562477, 13.2652769761118, -1.32288233370166, 3.9429001199722418, 12.217817032923426, 14.807573940324971, 8.045790410683598, 18.389296046593792, 19.652428967612853, 15.408457220487321, 21.50721707906287, 7.3831026278257665, 12.653231835189356, 21.01911812252522, 14.942526783989054, -7.611515061575041, 3.8950217224707178, 4.206134595382835, 24.127021284902103, 7.850281366890944, 7.677719930327087, 1.2490200451837818, 14.902577489186536, 20.291453303285294, -8.727024970834481, 19.530843038055707, 28.102914360723496, -5.002935255745122, 30.794068973069052, 24.448634718399326, 17.458850717038658, 13.98956435484041, 13.558305434351547, 21.426782695592358, 21.664385751395752, 15.380967579440616, 16.68833118784857, 8.955258427226838, 12.875109727226508, 7.852212560058477, 15.721047740358044, 0.8347256344613374, 5.671457822063131, 1.732190624972942, 16.683412370616466, 17.55270820853731, 17.605076465644938, -4.488209182984935, 10.490468790877843, 14.851129665800789, 13.919484147053609, 9.60016803882477, 12.82290784036673, 6.826908208886898, 16.257435710062566, 11.193026177685345, 23.964098827892883, 26.601516913316416, 13.180780123834579, 14.999582434790714, 19.275216829371846, 8.22571762588308, 9.134743851770368, 12.458696488866373, 21.651325367566123, 18.199603757044464, 26.19247571289187, 5.038965723774458, 23.541071483520035, 5.928412491204668, 19.68857578745221, 2.5130653985497755, 18.02786376237264, 12.222517978030094, 34.779064465615164, 25.221499652618874, 19.94015456916487, 20.54521916985105, 12.573573288379983, -2.5428630331507804, 26.264824637680917, 19.06005783385284, 3.4114608007956733, -1.4776819758433, 11.106379624723818, 22.385695849726524, 8.38270954658709, -7.890394271240041, 22.392476598622387, 19.77347416372959, 19.064248143573284, 18.595258704841143, 32.102633536965726, 9.170133760366394, 10.451218858906763, 22.078298023167772, 17.6604096808092, 27.443647002198187, 35.88751973319835, 18.49460241130461, 28.42749397370323, 36.88419792693263, 12.051855070863185, 23.86711933192646, 23.932679861140258, 23.361209231764022, 24.742540945712843, 14.884188797035524, -7.916633532853922, 16.88550241296641, 20.368401483220367, -6.121433223966076, 21.602504287983084, 23.985361381159883, 10.723608199701069, 7.119027012483858, 15.066435922152582, 12.67655035988043, 15.470416906150202, 8.007829413459909, 5.002151283498655, 15.435178335968535, 0.911627517224801, 29.129921612444047, 20.508843841700635, 11.085166327199225, 4.142201378603248, 9.11379172578411, 19.366467927939198, 25.488432654837638, 39.513334130917556, 
32.54690257058552, 42.52713982022121, 13.62895267072799, 24.078710901778102, 13.65426961747865, 2.6005619567472777, 16.515720149376445, 4.14135324525393, 30.699425207179154, 25.936956815829014, 26.09045235272792, 14.521648533582088, 37.82791039450002, 3.2308937568351617, 16.181501196593352, 9.834324661542526, 29.978007978578432, 4.1148631271865135, -0.7152659231217307, 28.107685898952063, 0.9998549405546733, 12.477265205390097, 27.65102345038499, 19.546880910821848, 21.61647718706723, 36.43192952180429, 26.73915058359027, 11.447981948007408, 12.094630491843962, 33.23578133123678, 20.918956329503686, 16.866128033420086, 8.7439247350924, 22.028718849889497, 15.290514799414522, 9.58063537216672, 40.30386255460709, 6.232921881126435, 15.238231810035401, 27.918846078753724, 12.80311896219089, 8.405731552880496, 28.718674952944777, 12.990215656553714, 
7.098297514219535, 1.4426981087771011, 18.8645343930762, 5.224427268597726, 9.404749828702968, 23.248251825214588, 33.92578097636729, 19.738374026155554, 24.594580273296295, 42.04595085996168, 19.768192498217157, 18.377625935172944, 32.3852983863202, 39.89201894069694, -0.457086012405167, 12.875731703086258, 14.219816253616013, 40.532489568694125, 29.22666558967521, 4.835134676679765, 22.542161051418876, 11.263978954519736, 25.03058673065746, 9.139764631652069, 22.443547811788104, -12.26027756223764, 22.616474346540585, 24.73977507277208, 0.40539355134779953, 30.362288144810293, 29.465781530920875, 49.30487006666965, 13.646162831412182, 3.683127893874641, 55.16005933183867, 17.617585259240325, 27.17881908981127, 3.7311787066816677, 9.058503081470652, 38.54647041047499, -1.3881376513847563, 6.050834593676683, 13.387274947036516, 18.71870793839132, 25.350956963125668, 16.703489697820025, 15.383905199594984, 46.362482848088234, 33.47808870698332, 11.207020178751337, 24.027797454129036, 16.19128879339116, 26.579963394955236, 22.117659122839203, 37.79102083029717, 29.049924029322476, 46.11989543784797, 10.15789279057205, 12.937510037090009, 29.747358785329684, 24.805709095116974, 16.627705129220757, 23.128228090548944, 23.80859580389779, 30.249642368048143, 24.038914520358908, 32.835862435645524, 37.084962727015004, 39.651477455232985, 51.70895349906758, 7.3461309978154326, 27.763888587129756, 11.48510081861847, 20.910368469779783, 26.216962936784252, 21.038722124383828, 4.227050003713671, 45.50051021512529, 24.80474598308398, 43.535364915268815, 24.631312455010324, 24.38552598405037, 42.84336713947435, 0.16310517576804529, 28.079833999699876, 9.682545711341415, 26.07421602946748, 31.674694589342707, 21.263259979348625, 5.609058087927153, 38.93008599098883, -7.113684587545919, 29.981557807369892, 15.101239134206969, -14.69402079074439, 40.779805970463094, 11.826872262506868, 26.653725821766166, 37.75299916882415, 63.596931284257664, 33.40050231767092, 21.50852612247602, 29.951134853651908, 21.82553729350115, 38.93834402077385, 62.53325845640513, 29.25392128216882, 19.559129995535002, 36.010720786063445, -20.705256978814056, 28.563331099322067, 14.855542193350933, 26.80196383749433, 17.823278352954436, 24.16781994822523, -9.36680747061385, 37.04089412690851, 12.859251824415082, 22.678136749552735, 14.481043974616963, 46.9954213145274, -1.2415742770555802, 20.511430688015462, 56.64214755316624, 
-0.781853603407157, 27.09814783607745, 36.1760624629496, 66.18158217121425, 24.22659869221614, 43.78399873919675, 44.31806733937157, 35.656791011203794, 41.51952558924128, 29.66137396428896, 35.351343709689786, 36.40899219410256, 40.51430834307888, 29.53849194553648, 59.12083165541675, 18.345926937350423, 28.59427986859032, 13.700457137723191, 21.188684429509415, 14.0365712756727, 33.42958345554291, 6.848187116150402, 21.75098199551436, 33.49647230518017, 36.419795720997215, 32.52965694902368, 19.305567409750203, 46.66360133076167, 54.28639610345857, 18.556827391391224, 18.252174877214074, 30.926479927567605, 23.167605086634886, 32.30206694847171, 50.75042271065981, -3.290397679979151, 40.7700281445847, 3.1410369217079364, 20.450837898189334, 41.723512977061645, 41.40717579087827, 20.219212411528105, 24.347615916977745, 96.23024607755173, 18.925162115466463, 20.52141933867864, 12.283522691464071, 31.50298560025511, 52.614304276315565, 30.10164017452997, -6.803047849520297, -4.623988919889619]
yValues = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 5.58496170606192, 5.052683964798172, 4.4338063702570825, 4.3958104358380705, 4.780284639267062, 5.067639119426607, 5.492041810887226, 5.139557333674697, 4.365253211803591, 4.214616538991667, 5.224090777720674, 5.710847093192242, 4.823564710818024, 5.262483428667903, 4.845255770423141, 4.92037283987367, 4.986853635350085, 4.498117352394883, 4.830230176606988, 4.518457840173333, 5.03374063476054, 6.139577412689311, 5.465906871054486, 4.4845214731516165, 5.944381254108746, 4.847793758981542, 5.58555860959425, 4.840291082074034, 5.176239665435355, 4.926405903795762, 4.442634197178396, 4.568221019220187, 5.499101522989437, 4.400574759056466, 3.534095511538615, 6.408030783698733, 4.65193365650693, 4.838313184883845, 4.883990006301188, 6.803057627783446, 8.464820405493665, 7.7813546812704235, 6.495271258206716, 7.2556005531790575, 6.997541043138282, 6.624284101240029, 7.408488792494343, 6.3651769049516655, 6.126160615935858, 7.17036823521366, 6.4540319433300954, 7.359494389021048, 6.894257686540314, 8.549726690932502, 6.171231283111631, 7.0982895188617405, 5.690288321309992, 6.975811461367913, 9.085192677690223, 8.39961474266903, 6.003608213819669, 5.792849907444105, 7.627470826056243, 7.1448833332764545, 5.163110926713299, 5.8727779335761205, 6.590332249082225, 8.350804830030768, 5.785757973608219, 8.705550016356092, 5.282871710118204, 8.042458858750724, 4.441083223976005, 8.08353208364782, 5.989126631946527, 7.671041971995552, 5.206264611936774, 9.02267244119228, 5.73647065082921, 7.433617133883516, 10.939432734576613, 11.170524382667091, 9.630652188935622, 8.525679427786644, 12.042268662654703, 8.776717256129391, 9.93983822584605, 7.987056148944153, 10.291256040104445, 7.315167499745057, 8.531353153714214, 8.33184429749954, 8.419365809354233, 9.308980887158807, 11.328125875208825, 6.573777608415364, 9.221411713309127, 8.807692618225573, 10.31932149710895, 8.080044510046331, 8.496082693800217, 7.428546948932598, 10.534908267410463, 7.758207308833075, 6.775562792973155, 9.757520016066934, 7.949516302902874, 7.349408198931622, 7.780577796498446, 12.865190090051282, 10.310185062550568, 7.529497654029399, 11.199961242098851, 9.154266992599673, 7.807758804681511, 13.444976101048901, 8.837150675670134, 16.45678948894286, 14.915431167203462, 9.346647874811016, 11.31977849895316, 10.772996395894793, 12.753975488127196, 9.289968952570929, 10.119908054905341, 15.626750660843847, 11.43511444602891, 10.58288327483525, 11.428067612530366, 10.702781057777123, 10.933680431445739, 15.205912917995573, 10.691053322566884, 14.076556494533659, 11.632016662953822, 10.368844714472537, 16.40073649191079, 16.256539888950993, 10.28155418332129, 14.456085105379566, 10.928284177107813, 9.35721092455946, 13.29562153762297, 7.550011078061479, 16.846671788718805, 14.63226731149015, 11.019434755695325, 13.006583198685277, 10.672396824073846, 11.277511183468562, 12.56033623815242, 16.98843455627639, 13.632788304281437, 11.490025945179848, 16.641673087988075, 12.163027655666424, 14.568843641801008, 13.649822017187388, 18.403883236375606, 10.185990054577069, 14.337556481492113, 13.151788115300008, 11.19694622058388, 15.180280282147002, 14.734596714117519, 14.025977890193069, 15.883995243694006, 11.020683515040202, 9.248893915529592, 15.483114712799942, 8.655653543553905, 16.384973684939467, 7.545615822948658, 11.482355136903694, 4.746090439776358, 10.917929613991388, 8.533236113517521, 9.80866038106267, 14.513109281952005, 11.82571498753583, 12.590395330484235, 17.90390424266937, 10.891607843710405, 11.55868661959512, 11.321382584904596, 11.653761236162076, 18.71484190932222, 16.13735708629566, 15.11095974893784, 19.33910077089765, 12.775256800356718, 10.924090069006954, 20.050479277992867, 15.637356673787671, 12.022094660272522, 20.85084732302556, 10.293999283959016, 11.38600831023862, 16.912871306939575, 22.810470535281752, 21.40579883767132, 13.54994663512811, 8.16063888865298, 20.212870457195145, 20.069454191184757, 7.610953728194964, 17.958669105916076, 13.450928801229646, 17.199001433121577, 11.776624235268638, 18.832469054974332, 16.091029412947, 10.219523974686552, 12.216448993783434, 19.51124820977111, 15.93512059161159, 9.094400846628059, 8.275867414371973, 11.658087802044477, 18.879399369445366, 17.089860070662056, 17.67115196108928, 16.22250908067908, 14.95985711228293, 8.940371759224243, 16.09588625257573, 19.116667520435374, 21.93275203252667, 15.509200742714738, 18.838965156549477, 11.114562451750231, 17.55062123857695, 14.411687808819298, 17.580226902441773, 19.01482427508413, 21.563484421707006, 13.604228582070501, 9.225047971787998, 21.1206162359967, 18.405488279842864, 19.151688523350355, 8.651754670354816, 17.010807002432387, 15.30356893988323, 25.501695473331807, 20.11820628207338, 15.279955961805447, 22.56074913347628, 11.902146056164504, 13.247362899158613, 19.922764636967294, 13.315942842960316, 16.5645264136756, 20.067640268924567, 27.757070349583024, 17.459960836883504, 16.880544838422296, 16.279898960148394, 19.72853241944037, 10.888817649928585, 15.64951801769526, 24.363221713251164, 14.08908222893415, 16.50186692385524, 19.678037751350498, 13.31546415661634, 18.937147856359417, 14.476025303473108, 13.298775328345151, 19.119652343121338, 15.032920758253004, 18.94302893146667, 18.484255403638226, 12.724948566766287, 30.195300362716374, 20.17162655650035, 17.780450108635044, 12.738069466111519, 20.32619984503165, 14.81823398029168, 17.03682448983215, 18.151017246348776, 17.85959232842109, 20.869899008843554, 11.243969903057007, 
26.949505378175406, 22.883877456032415, 26.747800997690092, 20.385275191893232, 23.797486585556136, 23.9934474229646, 13.191481076260882, 19.221440643067613, 19.998701959162705, 22.051967949948647, 22.52583192432625, 23.798707281854988, 16.690461462050525, 21.50016263365724, 18.20425575855516, 16.01924051644179, 26.059815491756986, 18.164637351708766, 23.522564532589087, 12.706382690885068, 20.85734020441442, 25.774697856020822, 20.950099885766697, 26.633710972996553, 20.609469454179145, 12.425697968273438, 34.028759585301145, 14.319895662138329, 23.888360172447417, 19.171142522629594, 6.875955590089244, 17.39585376488941, 24.536230613476487, 21.71505163837372, 19.178732201943753, 20.67173188033056, 19.69829279075551, 29.231671850753713, 15.898273281746262, 17.390413325013576, 16.112446384195934, 16.76566721068814, 15.216892901351947, 21.6369553465127, 17.663385462565586, 19.38351606379383, 17.27839672506721, 25.230664826880393, 17.687281257785443, 21.265858948748274, 26.459178778623013, 32.18042196137292, 27.597461455479774, 14.932983901517312, 22.604447019071944, 29.261815100190223, 19.590513050212238, 23.4233962440331, 12.61516740047829, 23.773397793342046, 25.437766531237564, 19.816627908530613, 26.164334885007452, 27.129489139941654, 29.25330895538673, 30.459265314157815, 22.553590659702376, 22.823507475655916, 27.17209527678603, 9.106173841519748, 19.481383721968804, 14.800881245151103, 26.349281805875822, 16.604886058552353, 37.09062796989216, 32.44837241009506, 27.46064970045353, 22.625178819401345, 34.473035900622165, 20.75118340776244, 20.424747677716383, 38.95219006908185, 27.084240191683932, 19.156426896820324, 38.750877228027356, 23.67384725994606, 25.24299464933156, 28.864687309448662, 17.285588204065665, 29.77725110910534, 24.093624034649746, 19.603404687844467, 35.123393393979576, 35.57318214418542, 37.00820644890446, 24.317000125829367, 23.81865053639415, 20.970884297223648, 17.53975284815588, 32.42754366802799, 27.595704522089125, 35.57028439736376, 
36.87345610676687, 27.497423028264368, 19.998403453775403, 19.173513820815714, 32.11719997936933, 27.278840909328043, 21.507569850655628, 36.83127382039069, 21.583787873714503, 14.708274008281258, 35.22864757532303, 26.069276379286244, 47.37842334747347, 31.746545099705727, 23.392329750955188, 33.19630630373315, 26.103694859114295, 28.56930050311067, 30.306756985622627, 20.183637837282127, 28.259763783837688, 18.971583525116827, 29.236580461487637, 26.929354084209287, 33.15179362996385, 31.39287187392257, 25.009976717883895, 44.03029616017436, 21.845660756290034, 25.447929905523097, 29.64730390719117, 23.666909274746665, 29.09999554253529, 19.36719718920387, 20.641849836644468, 29.89089666924317, 41.15527378166367, 22.60500448492999, 30.25829640563586, 26.47807957921877, 34.99026454424046, 19.51358940917848, 25.795145508393123, 33.50036148721797, 46.22787827693278, 27.93938449861301, 25.173261351593847, 30.830962572372147, 49.00176926444655, 29.54754092131233, 33.00795104508619, 27.554399014105876, 30.652817313123364, 41.308021614274594, 31.205018379157654, 38.6588780179911, 37.02251951990418, 27.760492524027676, 30.411981885121953, 29.5162045975607, 31.59061795759598, 32.066820016235255, 24.30202671541162, 35.449403800552574, 2.6375013838543637, 29.33665227690578, 30.764758284741045, 36.571070416630484, 29.427712601255294, 37.22381538504468, 27.48729202765906, 39.1602074548517, 34.71718094983672, 43.075979275127445, 29.04838252901143, 36.42565805457527, 35.81710901210677, 27.453599586620577, 34.93505756712999, 24.838592049581017, 23.768470852381697, 40.04426238268312, 53.18108579499693, 24.899873749731615, 16.094131209030603, 43.99943266445697, 40.865380189118596, 28.83087986195444, 26.566317127422373, 31.43630514365228, 52.85669392586872, 36.27851932028257, 38.342721066573816, 36.23991430560969, 31.691260104682677, 14.847922275879792, 47.3984813937485, 32.073205834889485, 33.42042957486924, 34.05389111302846, 42.21348438600289, 29.693138288974712, 35.7735790329098, 
40.704677129776876, 54.35038282365206, 21.23450534805351, 39.69459721775593, 23.624907391721663, 32.854191529570386, 31.824532822981322, 30.843232946148724, 33.714489781724815, 25.808593770954467, 38.725519496415515, 29.66395272679318, 31.094626191900794, 32.208298640798006, 47.32819513278353, 25.841116429164, 37.74926168980329, 55.06141941289185, 54.316453695760714, 32.948257410193705, 37.235885953644114, 48.3414424562464, 35.566988035323625, 46.3454921697077, 27.326834242504034, 42.56570804659591, 26.156356660149463, 23.88134536149972, 59.576646795513376, 45.24798459084452, 47.50617841869684, 28.655085060599234, 40.4211489918731, 56.82332575640653, 36.9642551700083, 34.28256760653548, 42.86473910366738, 
40.875713272098736, 49.83584272925376, 43.52558210358565, 53.43811003806316, 47.486695550936936, 40.0193728866046, 43.821613195457886, 50.51904905623286, 17.237251694064426, 40.50002667611247, 59.698432451826115, 35.8206684605363, 40.82899253507376, 33.04579606929649, 36.1346364908889, 44.29636432031587, 34.15888930222576, 53.607149825502994, 36.680087766724895, 54.898646108515976, 43.298449406218076, 29.20997550428399, 43.52371151893545, 57.02254182791733, 45.00708384640634, 21.19809650450205, 46.32793631044942, 29.313398554945405, 64.91502057166355, 30.28230375421812, 38.54123586110665, 34.52951067803903, 47.3851837381951, 42.32161725803622, 43.825102533747845, 36.64831430118728, 30.742001420093736, 28.086069552219477, 41.7855455987804, 22.38414174665559, 41.295863160609855, 35.011222047062624, 23.240224459371365, 68.89707194684836, 22.12368660829381, 58.86861433732185, 61.000056252672856, 53.38043190183089, 41.510329283481425, 51.797791425213845, 40.09267465916944, 37.77154912968707, 48.1371135301087, 51.59080424572868, 47.18985852284442, 52.83779517287607, 40.70998619217489, 22.002836890888922, 22.709811132248817, 41.231970093786316, 44.76236093917432, 34.71298730753153, 71.51163903255953, 69.24406523806476, 46.367900916593555, 34.280266117721396, 18.69973134186509, 21.62688203982681, 54.067083993126865, 59.359860048351145, 56.91444497164557, 39.45070532552626, 46.194589494090536, 51.86924645803658, 27.506100414431653, 55.80114238073131, 38.05352693653759, 45.6288096319816, 35.14542282047873, 61.82789807016335, 49.27719859087924, 29.024434430799253, 37.959864264296584, 49.36688879672668, 52.674250483690614, 42.89219654326603, 54.93811336391348, 47.668010913408814, 57.158236339353195, 46.04341406945536, 52.01650143295391, 62.88780569228592, 44.04160306536385, 36.98276731538433, 48.75218379070888, 68.2995130803859, 45.66093599512937, 52.29057015849093, 30.27885383451675, 42.37077428470647, 37.85406998289189, 74.14831862493547, 17.040685601524157, 62.32380530071779, 
33.77749299782642, 56.84659861865087, 33.97100655368237, 61.92319387917279, 40.088131671327325, 47.49405405476196, 54.099177904963994, 72.46572675933979, 37.26379577443717, 59.651888876719376, 39.51272238505682, 69.95240160311384, 5.452211931304198, 36.4387055355202, 49.81798551342537, 46.02607920983691, 41.99266811472974, 47.76266007307469, 57.2347387646728, 69.2295569191084, 69.88694615237607, 25.86539847635028, 46.85193261978722, 37.18870900607616, 63.370164371238815, 34.412752858289224, 60.66048434182774, 45.36956136417724, 44.91357819452844, 33.849906307092866, 50.77873386864002, 58.06410778651701, 26.716436783172202, 50.084821374330964, 67.51522769448844, 29.774085317217587, 50.704565445587576, 54.56838200381914, 33.805477879246695, 54.48605017257401, 55.48274173919932, 61.95500820866994, 71.38701788508004, 51.75140247522416, 34.189475582818375, 28.74837676771366, 49.05421200569191, 58.20987244079708, 48.244412193304356, 38.30279267841816, 41.00311563020264, 45.71114157993115, 82.7464269142103, 38.20626032277765, 44.074801393638744, 33.169964642293, 26.622469725780345, 54.84159567876232, 35.16054331066902, 60.04376337932174, 27.620600453190733, 57.37197672890328, 46.699974222610734, 57.85861141660063, 27.21646268615357, 61.19323504692656, 57.841080924122025, 58.7529515840359, 29.778661393783654, 48.25118157513775, 52.1014232397829, 60.62838267610403, 37.93119715915523, 61.74143026141638, 37.476586121013696, 60.19506573749282, 78.98338901737333, 57.22046329814282, 50.775324133801874, 75.48763304087286, 58.91316369535515, 73.89699729224604, 40.96991264605419, 62.805678951321106, 80.00524732147986, 60.98483398871751, 64.70594803101994, 69.68106000667984, 64.06043574414123, 61.137811895477796, 58.41781481379076, 97.6778344655658, 47.29883036795906, 57.16742559020748, 91.2526412661646, 54.538033560653304, 37.885352153817095, 54.70173143880201, 15.072800064091382, 39.109646909432115, 53.445472544666735, 87.26554639237327, 89.50410941135416, 47.83556030040188, 65.78545709390336, 78.79882932319356, 60.28463502627651, 69.73202942909693, 66.29722569012642, 80.12378069446453, 74.87240661890142, 63.91865141546668, 69.25801982135057, 65.4989996921933, 21.08574948564671, 100.64589210951127, 91.98132228291797, 82.1904486342527, 35.2491151978013, 75.74331999780838, 42.454557572907774, 64.29412042710891, 28.401099696416715, 11.956508411159092, 95.77855944110355, 68.21236080703197, 73.14651028439535, 38.29906812247808, 96.80968724848148, 63.58107857025602, 60.88317816984696, 63.35932500142439, 63.02787031330553, 74.68872209887094, 81.45795331026306, 49.025592687419966, 75.02566054120145, 51.94229686472957, 111.4865289761565, 81.71066943380937, 77.5721995067009, 74.62494614509909, 
47.54681638773427, 79.78545020993796, 120.16562244074748, 83.37949452795719, 61.39389833479997, 92.99555163629651, 59.39093000522818]
# for i in range(40):
#     for j in range(40 - i):
#         xValues.append(i + i * np.random.normal(0, scatteredness))
#         yValues.append(m*i + i*np.random.normal(0, scatteredness) + c)

plt.scatter(xValues, yValues)

linear=LinearRegression()
linear.fit(np.array(xValues).reshape(-1,1), yValues)
m = linear.coef_
c = linear.intercept_
print('m: {}'.format(m))
print('c: {}'.format(c))

x = np.linspace(0, 50, 100)

y = (m * x) + c

plt.plot(x, y, linewidth=2, color='blue')
plt.show()