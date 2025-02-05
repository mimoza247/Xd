import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Конфигурация бота
BOT_TOKEN = "7308259069:AAGs4rzyQaZT5fjudGTbwM_uG67Pi83pEds"

senders = {
    "edikabakumovskih96@rambler.ru": "KsrI4b6WlU",
    "romanmekesh95@rambler.ru": "vkRr15mM",
    "baklakovarsenii93@rambler.ru": "JgsXE1QD",
    "garikpyatyjkin88@rambler.ru": "DvIn72F4y",
    "anatoliisavkin1994@rambler.ru": "JxL39BgBvRd",
    "barilkinasara@rambler.ru": "WDy2j4kRK",
    "dmitriifidelskii@rambler.ru": "cBBCMK06Q",
    "boryasigalin1998@rambler.ru": "4a5dVodAQ",
    "muravyhsvetlana@rambler.ru": "5WLEF0jltlJ",
    "ekaterinastruchkova1994@rambler.ru": "2zLvDlmHejS",
    "tarusovgleb1991@rambler.ru": "98vJ7a8Q",
    "kseniyateregulova@rambler.ru": "F1EWeAJDz",
    "jidenkovanina@rambler.ru": "hD8a9oRIGuK",
    "chichernikovaevgeniya@rambler.ru": "c2STlnHL",
    "dulimovkirill97@rambler.ru": "1NXtYjIXLS",
    "halilulinbogdan99@rambler.ru": "rPCLdMxTu9f",
    "aleksandramelichkina1993@rambler.ru": "Sj60kFtS",
    "lyubomirzyurnyaev1989@rambler.ru": "04nLMoKv5j",
    "arturfilchkov93@rambler.ru": "ZEa7UpylAOH",
    "lauren.sanders27@yahoo.com": "lupoolovesyou",
    "nsbabyblues17@yahoo.com": "nikkiz17",
    "brendapondvt@yahoo.com": "harold",
    "shanerogersadi@yahoo.com": "shanerogers",
    "dementor96999@gmail.com": "auov fern blju utwf",
    "narusenie9@gmail.com": "auov fern blju utwf",
    "dmivrn732@gmail.com": "auov fern blju utwf",
    "ministerstvovnutrisnihspravukr@gmail.com": "admu berc moli coco",
    "malibu2222221@gmail.com": "auov fern blju utwf",
    "zlotema12@gmail.com": "xxie yzkz wdyk ugxm",
    "maybelox231@gmail.com": "auov fern blju utwf",
    "andeybirum@gmail.com": "ouho uujv htlm rwaz",
    "faverokstandof@gmail.com": "nrsg kchi etta uuzh",
    "faveroktt@gmail.com": "dywo rgle jjwl hhbq",
    "mksmksergeev@gmail.com": "ycmw rqii rcbd isfd",
    "maksimafanacefish@gmail.com": "hdpn tbfp acwv jyro",
    "bzdunovartur@gmail.com": "zyzu fkge aqxw ufhv",
    "apirsokov@gmail.com": "aajc vpye buim ipgx",
    "raumonatuhadi@mail.ru": "a7r6U9J6KHDaguAsidDH",
    "floworadpewoodvi@mail.ru": "ZcyUg5MUq8jMr9i8aST1",
    "letzegebquirdisnui@mail.ru": "abniAcbrCjRskpysMc75",
    "millveramontmoni@mail.ru": "bLd8Zg4tqfxmUq7KW5jW",
    "letkixipromnussi@mail.ru": "bNraxddiagE9Sx23SxYt",
    "hotriosmartraverba@mail.ru": "cALqh0bjnPefyiu7WL0v",
    "pillgemisscritcomsa@mail.ru": "dHBUrMg6aqXhvx0m1cVf",
    "leigedeamvebig@mail.ru": "dVTsGqDbZYbjse9iHNR2",
    "knocrufridunringgent@mail.ru": "dn333DbbuEfGnqw08Rxm",
    "tworensodiapansaa@mail.ru": "dsGajJE1TtiAGgZsgyvQ",
    "korlithiobtennick@mail.ru": "feDLSiueGT89APb81v74",
    "terbgebuoviror@mail.ru": "gaqaKs06xg22kkXXW2LU",
    "tioreibunthandvahear@mail.ru": "ggKygTjxSLzwm4tWd43B",
    "sanya.dragonov@mail.ru": "RakuzanSnos",
    "avyavya.vyaavy@mail.ru": "zmARvx1MRvXppZV6xkXj",
    "gdfds98@mail.ru": "1CtFuHTaQxNda8X06CaQ",
    "dfsdfdsfdf51@mail.ru": "SXxrCndCR59s5G9sGc6L",
    "aria.therese.svensson@mail.com": "Zorro1ab",
    "taterbug@verizon.net": "Holly1!",
    "ejbrickner@comcast.net": "Pass1178",
    "teressapeart@cox.net": "Quinton2329!",
    "liznees@verizon.net": "Dancer008",
    "olajakubovich@mail.com": "OlaKub2106OlaKub2106",
    "kcdg@charter.net": "Jennifer3*",
    "bean_118@hotmail.com": "Liverpool118!",
    "dsdhjas@mail.com": "LONGHACH123",
    "robitwins@comcast.net": "May241996",
    "wasina@live.com": "Marlas21",
    "aruzhan.01@mail.com": "1234567!",
    "rob.tackett@live.com": "metallic",
    "lindahallenbeck@verizon.net": "Anakin@2014",
    "hlaw82@mail.com": "Snoopy37$$",
    "paintmadman@comcast.net": "mycat2200*",
    "prideandjoy@verizon.net": "Ihatejen12",
    "sdgdfg56@mail.com": "kenwood4201",
    "garrett.danelz@comcast.net": "N11golfer!",
    "gillian_1211@hotmail.com": "Gilloveu1211",
    "sunpit16@hotmail.com": "Putter34!",
    "fdshelor@verizon.net": "Masco123*",
    "yeags1@cox.net": "Zoomom1965!",
    "amine002@usa.com": "iScrRoXAei123",
    "bbarcelo16@cox.net": "Bsb161089$$",
    "laliebert@hotmail.com": "pirates2",
    "vallen285@comcast.net": "Delft285!1!",
    "sierra12@email.com": "tegen1111",
    "luanne.zapevalova@mail.com": "FqWtJdZ5iN@",
    "kmay@windstream.net": "Nascar98",
    'k1839u@mail.ru':'1BjdCeGCNcdsXkSRZibA',
    'r2000m@mail.ru':'mK2CSfCcBYTpWznMUYCj',
    'u200o@mail.ru':'hpXzRhGZbuEmKC6YkkFb',
    'zxcforumgei@mail.ru':'zr8dDwC3wfJ2mf87WFBH',
    'hxjdjdhdhdhdhrhrh@mail.ru':'L79En4jttW74jMfPPmd2',
    'hdhdhdhdheje@mail.ru':'4t0L5F7e1bVbYYnfi0X8',
    'r200y@mail.ru':'wJec5CtZ6cGeM9iRtStY',
    'ristislavchernyagam@bk.ru':'iPsbVY4kBffEzraQUysm',
    'gi2000km@mail.ru':'00aZwUGJtp551XSCgJqg',
    'bh1963hj@mail.ru':'dNbDC9R52hnb9fwM2Pq2',
    'j123i@mail.ru':'ihfjY7TWNDL88JGHCeMK',
    '192hkk@mail.ru':'64NJ7uEUcMkJ7cHxzRp3',
    'f193hj@mail.ru':'r26UzK7GkNJQKYHqwYb7',
    'j183j@mail.ru':'2VndP5kNNnXJthvDF729',
    't183tj@mail.ru':'Z4K8BUiukka1j1WphtJ5',
    'j378j@mail.ru':'ZiW71BFPFEriUi4CENQJ',
    'ik278j@mail.ru':'ayygGXd0BT9bKRBNgtS1',
    'qstkennethadams388@gmail.com':'itpz jkrh mtwp escx',
'usppaullewis171@gmail.com':'lpiy xqwi apmc xzmv',
'ftkgeorgeanderson367@gmail.com':'okut ecjk hstl nucy',
'nieedwardbrown533@gmail.com':'wvig utku ovjk appd',
'h56400139@gmail.com':'byrl egno xguy ksvf',
'den.kotelnikov220@gmail.com':'xprw tftm lldy ranp',
'trevorzxasuniga214@gmail.com':'egnr eucw jvxg jatq',
'dellapreston50@gmail.com':'qoit huon rzsd eewo',
'neilfdhioley765@gmail.com':'rgco uwiy qrdc gvqh',
'hhzcharlesbaker201@gmail.com':'mcxq vzgm quxy smhh',
'samuelmnjassey32@gmail.com':'lgct cjiw nufr zxjg',
'allisonikse1922@gmail.com':'tozo xrzu qndn mwuq',
'corysnja1996@gmail.com':'pfjk ocbf augx cgiy',
'maddietrdk1999@gmail.com':'rhqb ssiz csar cvot',
'yaitskaya.alya@mail.ru':'CeiYHA6GNpvuCz584eCp',
'yelena.polikarpova.1987@mail.ru':'70Ktuvrs1iYbvSnbK8hG',
'yeva.zuyeva.85@mail.ru':'EBjgRqq73hue9dGhUA2R',
'zina.yagovenko.69@mail.ru':'QKBmpXnzFZVu9w4ewSrA',
'ilya.yaroslavov.72@mail.ru':'A2gNkb8n54i4T7XdPdH5',
'maryamna.moskvina.62@mail.ru':'dT7ftdX72cMsVemqRRqu',
'zina.zhvikova@mail.ru':'7CwRkjeL3a5viE9we3bt',
'boyarinova.fisa@mail.ru':'NnJfmSBzQ9Eew09xirpY',
'prokhor.sveshnikov.73@mail.ru':'Ybunrxdf95gkzm6A6ipp',
'azhikelyamov.yulian@mail.ru':'r7hanfr0tMqcBE4Edmg0',
'prokhor.siyantsev@mail.ru':'yubs6kvtfpWT4Tram26e',
'yablonev90@mail.ru':'42krThdaYbWCrCbH8UgK',
'mari.dvornikova.86@mail.ru':'qdEzYLWSTz6UEM2E4i0u',
'vika.tobolenko.96@mail.ru':'3WQ2wFTwge9m2C09QsfK',
'koporikov.yura@mail.ru':'nJtyfjqYi91j7tk0udNx',
'zina.podshivalova.92@mail.ru':'u4CL3YxVutmiuTvmTrbu',
'leha.novitskiy.71@mail.ru':'qQZd1gMqkU906Xk2hgJJ',
'rimma.aleksandrovicha.72@mail.ru':'biL4m6h0h4xQrDB3PnPp',
'polina.karaseva.1987@mail.ru':'mxZUqPPTrZHK99jUfPhB',
'prokhor.sablin.82@mail.ru':'vN7FjmmCmAD0JnQsANyc',
'kade.kostya@mail.ru':'U0hdXu7y3c1AVeT1Vpn9',
'yelizaveta.novokshonova.71@mail.ru':'aKPpgaPDuwaKbX1pbcq3',
'pozdovp@mail.ru':'EGDd20c7s82Z0s9LmrXc',
'siyasinovy@mail.ru':'z2ZdsRL04JvBYZrrjrvv',
'nina.gref.73@mail.ru':'sitw1XTxCVgji061iqj7',
'fil.golubkin.80@mail.ru':'PeaLrzjbn408DEeiqmQq',
'venedikt.babinov.71@mail.ru':'tBewA1HQm29c2Zkira96',
'den.verderevskiy.67@mail.ru':'fndp7qr67dpfXBAu0ePH',
'olga.viranovskaya.92@mail.ru':'50QSPrecgk5cMdk1YsBm',
'uyankilovich@mail.ru':'Muw9kX9vAhhKxbZXZ3sh',
'clqdxtqbfj@rambler.ru':'8278384a3L51C',
'qeuvkzwxao@rambler.ru':'72325556pMFol',
'mgiwwgbjqt@rambler.ru':'3180204jCoAdt',
'olwogjcicw@rambler.ru':'3993480P4Gyth',
'qjdmjszsnc@rambler.ru':'6545403StkbOh',
'yqoibpcoki@rambler.ru':'695328653f9Wp',
'vnlhjjkbxr@rambler.ru':'4609313egqV59',
'vpgcdkunar@rambler.ru':'9936120R4LYh3',
'agycsnogqq@rambler.ru':'0234025nWwX5j',
'ctmhzsngse@rambler.ru':'2480571s1sZvW',
'ryztzlttdn@rambler.ru':'9416368kTX5jI',
'hqxybovebw@rambler.ru':'8245145VhX704',
'rejrjswkwb@rambler.ru':'5114881xCYqsB',
'xkbecjvxnx@rambler.ru':'5670524FiFi39',
'xnlqkfvwzx@rambler.ru':'7911186rp8L9P',
'gvzzmqtuzy@rambler.ru':'5133370ZstXEx',
'eijxsbjyfy@rambler.ru':'36196124YQZeI',
'bizdlfuahq@rambler.ru':'8374903tkk2gA',
'dhehumtsef@rambler.ru':'9126453AkhK0Z',
'zsotxpaxvi@rambler.ru':'46227528QryxI',
'ktsgdygeuc@rambler.ru':'1853586bnCyzK',
'uiacgqvgpe@rambler.ru':'65280104FvoJW',
'ynazuhytyd@rambler.ru':'1038469bD3PXc',
'ewmyymarvi@rambler.ru':'5023318Bh3tBg',
'wllhpdisuj@rambler.ru':'24856958LdTsS',
'ldqicaqxqo@rambler.ru':'3878601ZNDUtq',
'qnuumqoreq@rambler.ru':'97575207Is6tx',
'hlqhvdwpvn@rambler.ru':'6886684bPjiyd',
'mjjjxiuadq@rambler.ru':'0606032V81m1F',
'qmasujqfrk@rambler.ru':'277585511anUy',
'mfemvxqdcq@rambler.ru':'8831015UwqwWD',
'jauvxszfam@rambler.ru':'0711044gqzrVR',
'lkmujuagfk@rambler.ru':'08781007DLS8k',
'kcamwmzxjo@rambler.ru':'9812873rVr1MY',
'czkklwifon@rambler.ru':'74278883h9FP8',
'tsjsbqyrfk@rambler.ru':'0150917jIseH2',
'pbetvcnhzh@rambler.ru':'9952234XaKDFu',
'bsahxcpwkw@rambler.ru':'2860163ch8Ido',
'xphyesgbtc@rambler.ru':'6594341ERehhX',
'egmpjoufeq@rambler.ru':'2613441hfDuWr',
'jyaolatwam@rambler.ru':'7668835xdjLbg',
'istooplcmf@rambler.ru':'6592403JR47Wm',
'vxesoednot@rambler.ru':'35885918QZw94',
'oywtklayaz@rambler.ru':'4434448KsCuTf',
'tazxrlpjil@rambler.ru':'8342862p9Wyst',
'aumiycpxid@rambler.ru':'4109383BuuNcN',
'lrrztbfuzy@rambler.ru':'3646406sDO8ay',
'ocggavguxr@rambler.ru':'6406050SL2mZG',
'imprdsrnmd@rambler.ru':'4869746vpxksJ',
'eidyoikavp@rambler.ru':'1243890yXPyix',
'jtbcabsapw@rambler.ru':'566339497yHv3',
'szokdvnzrw@rambler.ru':'5285567I3Bil1',
'jqflrccfjs@rambler.ru':'7239478VeLuf1',
'nhmxjawemh@rambler.ru':'22695409fkCex',
'uoolwvvwdc@rambler.ru':'1073090zX6ebM',
'bdnptczren@rambler.ru':'2684430DcPEuk',
'bfghzdkurg@rambler.ru':'3874335d5hDQy',
'ljlexsfcvo@rambler.ru':'4102671EIquGo',
'byzjhysyyg@rambler.ru':'4637736mzdEcT',
'tlrjbuzcyj@rambler.ru':'2437827AhPaGW',
'denjsbmggh@rambler.ru':'228014585ayVe',
'ekkjrcskzo@rambler.ru':'6609442MFPeDO',
'ptpjocqobw@rambler.ru':'6047270EXk7Hb',
'nekrxmcklm@rambler.ru':'3532718I3vV4C',
'ulgqeqvdqy@rambler.ru':'6764301Nx25yL',
'ezofozvhyn@rambler.ru':'43181265tC6FQ',
'hwklsnkqky@rambler.ru':'2399374mHyEUJ',
'elglaqexoj@rambler.ru':'9803014pMNF9p',
'rgmjfwhhjs@rambler.ru':'3268611cfC3aR',
'vcvwvkntgb@rambler.ru':'6536007UgTXg4',
'phkohtlitv@rambler.ru':'0238010TXt5aN',
'pqqqyejlqi@rambler.ru':'0429804UwSSi2',
'toxevermnd@rambler.ru':'1801000MqDm87',
'dicfdqgxad@rambler.ru':'2062460Tbvjlz',
'sktsnxhcxe@rambler.ru':'35185285Pon91',
'jpljjnrrla@rambler.ru':'0815671xPHjiw',
'rtqpiimiid@rambler.ru':'6534672URa1mI',
'ldygdlpizk@rambler.ru':'6686886YWhL05',
'fqxqadaxfy@rambler.ru':'3195621x5qYdU',
'chybzpsglw@rambler.ru':'8032931YTKllg',
'vkctzanare@rambler.ru':'1157997LGySqk',
'repjncygun@rambler.ru':'3300691BqYJVG',
'khrarivdow@rambler.ru':'7168350Cmqkmj',
'aqbeitoqdl@rambler.ru':'87552792499tS',
'vhauhgmbnc@rambler.ru':'9276444y9YzY1',
'cfoqabqkbi@rambler.ru':'4601718gc2Zji',
'kmqnowhvjp@rambler.ru':'6667003L1jZxc',
'djsdksvzhj@rambler.ru':'7523251yAKPjZ',
'uztbbbfqbp@rambler.ru':'8265517naN9fx',
'ljrbpfuicp@rambler.ru':'39793362TjZIk',
'jzzdyxicjo@rambler.ru':'8117494s6CZVB',
'gjnbtrflkc@rambler.ru':'8623171iqXOD9',
'jfjtwncyeb@rambler.ru':'7066987lMSG2Z',
'rfphqkyyrj@rambler.ru':'8800207M5Nj7Y',
'ilynipkqwx@rambler.ru':'83333032WQo83',
'ifzenleixs@rambler.ru':'69679436xM9U4',
'oevwtysoel@rambler.ru':'6918228UC47Zs',
'hpdkdwqvzx@rambler.ru':'0605431xMVexd',
'ekbkufxdxx@rambler.ru':'1918712uEOQ9t',
'zstxwfwiof@rambler.ru':'4043772UwRp5o',
'rjmrbybhnd@rambler.ru':'5203792lDmxvC',
'eukygnfzno@rambler.ru':'3520959hXs1Zw',
'ljrolbwlad@rambler.ru':'0394475pK0dYa',
'gozpezocmj@rambler.ru':'8282635Gkvuvq',
'asytoiumwt@rambler.ru':'42141199FgP3H',
'fbiooohghv@rambler.ru':'7338453zMbWhb',
'ajwlalfqqu@rambler.ru':'3360915x1XVgt',
'cvegntetwm@rambler.ru':'8091607CSuKMf',
'jnhjnmicbt@rambler.ru':'6375986dokrgG',
'fnaauasmjz@rambler.ru':'4160248ztCRsJ',
'qnwmlvfwct@rambler.ru':'8367630XGXmxW',
'lkycbhjcwp@rambler.ru':'5255980KedZTc',
'bkyojwrkxl@rambler.ru':'1286663uHl4WQ',
'lxddybklck@rambler.ru':'1077242JFSyQN',
'chzhdkoxnp@rambler.ru':'0533445SI0q7c',
'ofjxkwwomf@rambler.ru':'04956317DKrSX',
'jlirgtapbl@rambler.ru':'8728917NdMxgN',
'dgcceghlse@rambler.ru':'2986381aT5V36',
'rkwfhcvlem@rambler.ru':'10022063K5qmY',
'orgjvhbrxw@rambler.ru':'0652659TopL8Z',
'opynskpmzp@rambler.ru':'2881423L4qs6x',
'pbqzrueeko@rambler.ru':'44469262tOGeK',
'raxzhngqti@rambler.ru':'3078265mgWYjl',
'ztnxozwuuj@rambler.ru':'0637919utKekj',
'gtxjzwlgio@rambler.ru':'3737088WWddrY',
'sjbflcwjgn@rambler.ru':'9791667kVGllD',
'znggdpfxzu@rambler.ru':'0209083jdisUI',
'gnvhlocnro@rambler.ru':'4361239Vu3OCl',
'vqeijhgrmo@rambler.ru':'5560137M1oKk2',
'meefvzfwqb@rambler.ru':'9793015vJE0qF',
'sclsjzvugn@rambler.ru':'4631432OQjvWt',
'ybbtiosefy@rambler.ru':'3511505pL04S1',
'agwqdadpkb@rambler.ru':'0930298CUZdLp',
'kudgvibwao@rambler.ru':'5791834nlLQtU',
'qyonxjqbxi@rambler.ru':'9390829m2Edz3',
'jhetdlhlqk@rambler.ru':'5530162MiLHZe',
'bsjvczarsc@rambler.ru':'5747155KvNjcL',
'wlcilpvzqu@rambler.ru':'2757580jLlM9M',
'xxdgcixidw@rambler.ru':'2867562O7zGft',
'wekduwrnkp@rambler.ru':'2646367TlIskI',
'keakcnrorg@rambler.ru':'9223165cV1Jj8',
'nzuspyevwr@rambler.ru':'2212416npkUqe',
'mgjfbgitts@rambler.ru':'7368986roeLXD',
'smfxvrnhmu@rambler.ru':'6947298Kau5qA',
'yvkelubdzf@rambler.ru':'5913332lXWtlC',
'bwywtjxybd@rambler.ru':'2766021wTSkeU',
'dlvyzavolw@rambler.ru':'274983252lHyu',
'oaudcugulf@rambler.ru':'4543030UHFWaV',
'zvqexaokhf@rambler.ru':'1453114PCheCq',
'pjuafpzpoo@rambler.ru':'8474216vNFUG0',
'ckryhpqogh@rambler.ru':'4791674aJHW43',
'vlkqstbhpd@rambler.ru':'3021260kBI3KU',
'jwuupemjpm@rambler.ru':'7769235y719L9',
'bmxuqrzcnk@rambler.ru':'1345552ExHXyu',
'fqrkonqkjc@rambler.ru':'4104158bVEORa',
'gizwbhyrfd@rambler.ru':'3863359lgfpTv',
'onghqwbvnz@rambler.ru':'8249537XWqpPk',
'aeyeyvlnkl@rambler.ru':'6025219f5mGom',
'qcwweqcqbx@rambler.ru':'2503306kHzKPD',
'vefmynztzu@rambler.ru':'1134939bhRpJS',
'qlkhitdctp@rambler.ru':'31621358ZPx5F',
'xhgfgecvrn@rambler.ru':'4116759TRhERi',
'globizrzui@rambler.ru':'9679753mLkmMd',
'vvfcuoibrf@rambler.ru':'13558992CDkJj',
'enccmwktap@rambler.ru':'7631476Lzr9hd',
'njbnyghvdq@rambler.ru':'48585907Qh2NS',
'cobadewaxd@rambler.ru':'6433228NMX7a0',
'zzvsuoiqfx@rambler.ru':'5067380KtnMTb',
'lkdcjpcqxu@rambler.ru':'8319085aRHdoT',
'zcabeofgox@rambler.ru':'0059181TJSaJq',
'rswrifhmtf@rambler.ru':'2987108xzf1Uy',
'gebzgyscic@rambler.ru':'6981082UOD1sL',
'yhncgfwjom@rambler.ru':'7866073mRMAal',
'pvvlmjmiwe@rambler.ru':'2807349CLUZie',
'towqdsigmc@rambler.ru':'48481486UnoRg',
'eyzwvxphxz@rambler.ru':'5532563Bskght',
'aruhbkpsud@rambler.ru':'8022722dNUe59',
'kckwnnvmwf@rambler.ru':'77502899D6ygI',
'emicquwuxf@rambler.ru':'2982514obBgCJ',
'pnefqbonja@rambler.ru':'1443294ZY7BgB',
'wlnecrzvkb@rambler.ru':'2016456ke4QRw',
'lucufydobd@rambler.ru':'4188202gvlmuR',
'obcheovoqy@rambler.ru':'34012721sYlv3',
'fjxwhhlhxp@rambler.ru':'1621680a9CbS0',
'rjggfmhckx@rambler.ru':'4470958ocoPjD',
'oqixhlbhlh@rambler.ru':'4902150aD8Tkr',
'zmlfdygkce@rambler.ru':'4809956HgOdyu',
'zdjqfhdafp@rambler.ru':'9142498RW8Ynh',
'cjoyoxsdby@rambler.ru':'108516737An82',
'hfrcbbwzgb@rambler.ru':'1732107RUVvSu',
'crkbywjfzg@rambler.ru':'9616254qbUhAG',
'luygpfibra@rambler.ru':'9488606qXIvQZ',
'xepjtcrrzo@rambler.ru':'3774977dMOr4c',
'ayrbethwst@rambler.ru':'4658060glYVyA',
'czhjnqqgdd@rambler.ru':'89865789wXqfK',
'oltotetppj@rambler.ru':'0936665mJL9H0',
'eaoeqvygrv@rambler.ru':'5348316HcEpsm',
'dkfvwvkotb@rambler.ru':'3366454MTGiOR',
'wavsfqiarg@rambler.ru':'4220587wVJ8gU',
'gkwlbrhwix@rambler.ru':'6383580cCHutT',
'uachryyzde@rambler.ru':'0643369cWRWhr',
'nuyfldwirg@rambler.ru':'29709163eKxWc',
'fnorovxtvk@rambler.ru':'469173140zLer',
'qrmnfyxdqj@rambler.ru':'7609701E9XfBC',
'ncupywgysj@rambler.ru':'8506439mTgrb6',
'ehhuextqqm@rambler.ru':'4136418EqGa4N',
'utasiosnxd@rambler.ru':'6230428wOiMLm',
'ppizzpzqod@rambler.ru':'6217530deEIGb',
'mgzczmjjpo@rambler.ru':'5974114gf7VLz',
'ezugyxxfkx@rambler.ru':'6920685aZVulS',
'vnuwwwuhuj@rambler.ru':'20889562nRk1x',
'xqkicchcbc@rambler.ru':'4345126XoitUD',
'hykbjrvqsw@rambler.ru':'8281493mLUbNt',
'etyqikxlam@rambler.ru':'1096360Cvg5n7',
'blnpfilkdh@rambler.ru':'6208964Fhgy1O',
'azawxjcfeh@rambler.ru':'8923382Pqo1jI',
'dyumumpgus@rambler.ru':'3454195S5FQ7d',
'ryejfejmef@rambler.ru':'1474062Y49oZE',
'uqyfeqyumv@rambler.ru':'4305431o270vK',
'vardlzqzas@rambler.ru':'8158325VAjymq',
'wvqbwbpofd@rambler.ru':'2037592lvIWZI',
'agsnpvxscg@rambler.ru':'676450330Gmzj',
'ctiwtwpowk@rambler.ru':'7004605qQOK5O',
'vvluscokds@rambler.ru':'2351339uVtaUb',
'gqtipysiyk@rambler.ru':'4672575GMSkQq',
'vwtjzupcul@rambler.ru':'6978060SRfKxQ',
'klvdgsoczb@rambler.ru':'8504791kNehzf',
'lavpussyin@rambler.ru':'1183746FmKlfU',
'xvzoptqyhd@rambler.ru':'7635851M7gCQO',
'yzkgydxjlr@rambler.ru':'3889248nBv9xb',
'tkuscgummb@rambler.ru':'2646861vfBmjy',
'ytbfnnlvuc@rambler.ru':'8680715wXqNoY',
'qrmyueqrpk@rambler.ru':'48163158cQzn3',
'nulburzrsp@rambler.ru':'4628721fbFYDx',
'xpsncakaar@rambler.ru':'8050121QgZtLE',
'rsfyuinlhi@rambler.ru':'7789677doEl7X',
'lruwhkjpmm@rambler.ru':'2407934PCrhbt',
'zqlboekoph@rambler.ru':'4540547BXedBD',
'djrmgdvpxk@rambler.ru':'2516345lt4GhI',
'cdyagajvqt@rambler.ru':'0457036J8b9x1',
'csbmtfyogo@rambler.ru':'8578398RoY5Me',
'mtgjgvchbf@rambler.ru':'6273263XOh0fb',
'hjovrkraea@rambler.ru':'1756354e4T9PL',
'wuasdmqayg@rambler.ru':'8983467Njjbfc',
'dnzaquycrh@rambler.ru':'3047369gLtNHO',
'rdptnhimnz@rambler.ru':'92217639LcTX1',
'yklofyaekj@rambler.ru':'0018913JhfLfv',
'zqfzplzlwp@rambler.ru':'6550676M1gwNy',
'fzcveyejbh@rambler.ru':'9098104PB57ol',
'qcpwhpqape@rambler.ru':'3277585gafS4o',
'xfitvnzvez@rambler.ru':'0023433CgWWiW',
'tiansbolvj@rambler.ru':'0200419d6c8hD',
'ibwukvjyxn@rambler.ru':'6846348Go4rB7',
'tfclkifgjn@rambler.ru':'9973469KBqk2S',
'yscehsgepj@rambler.ru':'0258935Wptd0G',
'webznumpmf@rambler.ru':'4342482ZhTyVk',
'xadehtuxys@rambler.ru':'94129234ZK2kl',
'wsfmuqnmjp@rambler.ru':'7886187uCcru0',
'mhovkuzfnl@rambler.ru':'3632660bLpvSw',
'pppuvtsuxu@rambler.ru':'6227635FqgnGa',
'vvezjeryic@rambler.ru':'7595367ZgjYIn',
'oiukjktkhx@rambler.ru':'35863397YZBFb',
'qswbndmblj@rambler.ru':'3563325a93EZ6',
'ztyfnsdrqa@rambler.ru':'7748929ZbfDrw',
'lrjduagkcj@rambler.ru':'8783147DV4pJe',
'fhrzanukuh@rambler.ru':'169703230lEf6',
'pqnnzwuuku@rambler.ru':'6446752B0qw8H',
'ndctkqjnfc@rambler.ru':'1534939xHfafC',
'tlzuekovcn@rambler.ru':'9668644RKjMla',
'ermdcrjyhu@rambler.ru':'9838788xXiLRC',
'qbfymlhpwj@rambler.ru':'3278597BlWafL',
'uuuzmgapoy@rambler.ru':'2535811Vz3dxV',
'chjolhsihy@rambler.ru':'8253848P8B5cd',
'rrakdmtsdb@rambler.ru':'0459246V4tjHK',
'ngkrbvqvha@rambler.ru':'9835759JQxkal',
'caxeoztjpa@rambler.ru':'1297098SSweKM',
'molnxkchzu@rambler.ru':'3122920NIh3iE',
'murnslgulf@rambler.ru':'1045964Oppb9c',
'qcjyautxca@rambler.ru':'6358075LUbp6R',
'amhlnrxaue@rambler.ru':'3401580IiYPYn',
'wexnexkcct@rambler.ru':'2157766eLIiqP',
'oplwkvkrct@rambler.ru':'7136350vkGkaT',
'pmddwbvmwv@rambler.ru':'3066705M2aCUh',
'aqjcdxeuuh@rambler.ru':'2077271RlOJ0c',
'baiivnfrdy@rambler.ru':'1327519LJwKyi',
'apvskvwhsv@rambler.ru':'2995739T8pCNZ',
'xsejblkgit@rambler.ru':'6224118EhnkyG',
'rxihtsvdxg@rambler.ru':'3045787jhQxfI',
'dgtmxgrdsm@rambler.ru':'0342058YAff0O',
'wuxaurjkuu@rambler.ru':'6231160X8CsYl',
'erimfuxfdl@rambler.ru':'1956070yzlgSl',
'ncklilvfts@rambler.ru':'5077711XhCUzu',
'eerlpvniie@rambler.ru':'6769422kteVgK',
'mcrtyjkbdi@rambler.ru':'5281059WC9HfI',
'izjnzlavcu@rambler.ru':'4201974Gjdy1B',
'tkrywugfgq@rambler.ru':'1037112WpAZzl',
'hpxzczhgwe@rambler.ru':'4522788wYVDJk',
'rtfanictwt@rambler.ru':'9292445IxACdk',
'lhschktxka@rambler.ru':'0731083E0ItX4',
'zfqfwvmnms@rambler.ru':'82390631NIbOF',
'rzaviakxlb@rambler.ru':'2230383uFiVmA',
'rmmueooozx@rambler.ru':'1531525wyFFSm',
'weasmvistt@rambler.ru':'7079364RGZCBs',
'qikszesoqz@rambler.ru':'6739326h2Wy4j',
'gosgrmonmh@rambler.ru':'7425012zw2LXl',
'vuhlehwstc@rambler.ru':'6477750sVXsV3',
'wcbmulbsbk@rambler.ru':'9889803qVwaj6',
'aejerwwnft@rambler.ru':'4598847uygrUg',
'rtrkjygdey@rambler.ru':'4810312JrG4Ti',
'uywyrkhuue@rambler.ru':'6593801fMGH6b',
'flqyimskwk@rambler.ru':'7856809GVZfzT',
'mqjqttpyui@rambler.ru':'3633261lxxEPt',
'asagkqfygx@rambler.ru':'90629300zd5Xm',
'bupfcjoqrc@rambler.ru':'7806644uXzkZy',
'twicbfjgoz@rambler.ru':'0187832xjeOz1',
'kseniya.pavlova.9898@mail.ru': 'GRVDAjqvvx9xz00L2wUx',
        'annakrasnova.1994@mail.ru': 'jUFMXba6wLFcuQBkqht2',
 'sanya.dragonov@mail.ru': 'RakuzanSnos',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123','rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'lyimbshsup@rambler.ru': '6463734rnAygg',
           'jdqukazixk@rambler.ru': '0225223ACFeq0',
           'baljufgcnc@rambler.ru': '4738678YMyCvO',
           'ruslanorlovimx4134@rambler.ru': 'Andersonnancy945',
           'vladislavkulikovxcr1902@rambler.ru': 'Allenkimberly021',
           'romasidorovdbj3700@rambler.ru': 'Clarkmargaret444',
           'lehabogdanovhdw1954@rambler.ru': 'Evanssandra913',
           'mihailtitovopr6182@rambler.ru': 'Younghelen407',
           'koljafedotovmqj2347@rambler.ru': 'Gonzalezsarah321',
           'genasemenovhvu9785@rambler.ru': 'Taylorlaura482',
           'vovafedorovmvu7067@rambler.ru': 'Collinsbetty976',
           'grishakulikovyyk8848@rambler.ru': 'Wilsonlaura931',
           'olegnikitinxwo3553@rambler.ru': 'Wrightkaren568',
           'gennadijkalininizb3132@rambler.ru': 'Turnerdorothy038',
           'bogdankarpovxad9304@rambler.ru': 'Carterlinda019',
           'koljakuznecovzfq8892@rambler.ru': 'Walkerhelen225',
           'vladdmitrievtpv8734@rambler.ru': 'Brownmary434',
           'arturkovalevdln7432@rambler.ru': 'Lewisnancy365',
           'konstantinbelovabq7348@rambler.ru': 'Allenmary923',
           'sashavorobevbml8362@rambler.ru': 'Hilllaura818',
           'ruslankozlovhji7240@rambler.ru': 'Hallnancy735',
           'olegzajcevepy8163@rambler.ru': 'Nelsonsharon117',
           'grigorijfominlxp0053@rambler.ru': 'Wrightpatricia686',
           'vitalijmaslovusv3737@rambler.ru': 'Garciabetty827',
           'olegbelovblx5518@rambler.ru': 'Phillipssharon437',
           'olegmaslovrde8926@rambler.ru': 'Mitchellbetty324',
           'vitalijdavydovtal6583@rambler.ru': 'Rodriguezmichelle351',
           'dmitrijmironovlaf9788@rambler.ru': 'Whitedeborah816',
           'vanjakulikovdpf6394@rambler.ru': 'Allencarol017',
           'andrejmaksimovwjw5202@rambler.ru': 'Cartersusan436',
           'zhenjaafanasevomj
}

# Функция определения SMTP-сервера
def get_smtp_server(email):
    if "@rambler.ru" in email:
        return "smtp.rambler.ru", 587
    elif "@gmail.com" in email:
        return "smtp.gmail.com", 587
    elif "@mail.ru" in email:
        return "smtp.mail.ru", 587
    elif "@yahoo.com" in email:
        return "smtp.mail.yahoo.com", 587
    return None, None

# Функция отправки email
def send_email(sender_email, sender_password, receiver_email, subject, body):
    smtp_server, port = get_smtp_server(sender_email)
    if not smtp_server:
        return False, f"Неизвестный почтовый сервер для {sender_email}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True, None
    except Exception as e:
        return False, str(e)

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Класс состояний (FSM)
class EmailState(StatesGroup):
    receiver = State()
    subject = State()
    body = State()

# Клавиатура
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("📩 Отправить письмо"))

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для отправки email 📧\n\nНажми кнопку, чтобы отправить письмо:", reply_markup=menu)

# Начало ввода email получателя
@dp.message_handler(lambda message: message.text == "📩 Отправить письмо")
async def start_email_process(message: types.Message):
    await message.answer("Введите e-mail получателя:")
    await EmailState.receiver.set()

# Получаем e-mail получателя
@dp.message_handler(state=EmailState.receiver)
async def get_receiver_email(message: types.Message, state: FSMContext):
    await state.update_data(receiver=message.text)
    await message.answer("Введите тему письма:")
    await EmailState.subject.set()

# Получаем тему письма
@dp.message_handler(state=EmailState.subject)
async def get_email_subject(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer("Введите текст письма:")
    await EmailState.body.set()

# Получаем текст письма и отправляем
@dp.message_handler(state=EmailState.body)
async def get_email_body(message: types.Message, state: FSMContext):
    await state.update_data(body=message.text)
    data = await state.get_data()
    
    receiver_email = data['receiver']
    subject = data['subject']
    body = data['body']

    success_count = 0
    fail_count = 0

    for sender_email, sender_password in senders:
        success, _ = send_email(sender_email, sender_password, receiver_email, subject, body)
        if success:
            success_count += 1
            break  # Останавливаемся после успешной отправки
        else:
            fail_count += 1

    await message.answer(f"📊 Статистика отправки:\n✅ Успешных попыток: {success_count}\n❌ Неудачных: {fail_count}", reply_markup=menu)
    await state.finish()

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)