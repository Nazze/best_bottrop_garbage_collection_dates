BASE_URL: str = "https://www.best-bottrop.de"
DEFAULT_TIMEOUT: int = 10
STREET_ID_DICT: dict = { 
    "Adelsbredde": "241D7097",
    "Adolf-Kolping-Straße" : "4807D8DB",
    "Aegidistraße" : "D38A6339",
    "Agathastraße" : "1291D88D",
    "Agnes-Miegel-Straße" : "42CE70C8",
    "Ahornweg" : "EE95B714",
    "Albrecht-Dürer-Straße" : "E462E40B",
    "Alleestraße" : "1079C0C6",
    "Alsenstraße" : "A10852F6",
    "Alter Postweg" : "A1BA28D8",
    "Alter Südring" : "7245B7FD",
    "Althansstraße" : "69C901FD",
    "Altmarkt" : "DB771464",
    "Am alten Bahnhof" : "8C060AB8",
    "Am alten Kirchplatz" : "30B12D95",
    "Am alten Sägewerk" : "CF1C9DA2",
    "Am Beelertskotten" : "F67BF383",
    "Am Dahlberg" : "155C355E",
    "Am Dornbusch" : "BA92C92A",
    "Am Eickholtshof" : "13BE0493",
    "Am Feuerwachturm" : "E0CFF36C",
    "Am Freitagshof" : "9B2518FE",
    "Am Hagelkreuz" : "B2393B72",
    "Am Hang" : "47DCE77F",
    "Am Hasebrink" : "CA5D38BF",
    "Am Hauptbahnhof" : "B0465E2C",
    "Am Hölscherskotten" : "D6F41C98",
    "Am Holzgrund" : "A92FED80",
    "Am Kämpchen" : "AA8DEE9C",
    "Am Kirchschemmsbach" : "18D59FA6",
    "Am Kirchsteig" : "E1161305",
    "Am Köllnischen Wald" : "698E2D16",
    "Am Kruppwald" : "1B1239D1",
    "Am Kuhberg" : "A63CFEC3",
    "Am Lamperfeld" : "F8788BA3",
    "Am Langen Damm" : "8552313A",
    "Am Limberg" : "7A89F492",
    "Am Lohdick" : "AD41DB82",
    "Am Lohehof" : "299A2337",
    "Am Marienhospital" : "9C0AF200",
    "Am Nappenfeld" : "4E34929E",
    "Am Pastors Busch" : "04D2926E",
    "Am Pferdemarkt" : "DC5AB3CB",
    "Am Piekenbrocksbach" : "46A2364F",
    "Am Quellenbusch" : "C741387B",
    "Am Rhein-Herne-Kanal" : "A2E8A5EE",
    "Am Ringofen" : "9086F506",
    "Am Sandknappen" : "15385FD1",
    "Am Scheidgensbach" : "502B7E01",
    "Am Schlangenholt" : "B1A8EE3E",
    "Am Schleitkamp" : "A68DD198",
    "Am Schölsbach" : "7ED0C1A7",
    "Am Schoolkamp" : "2709CD3C",
    "Am Schürenbusch" : "69D07B35",
    "Am Sellbrocksberg" : "A5FD7927",
    "Am Skipschacht" : "4397AA33",
    "Am Spengelsberg" : "DD4B6FE7",
    "Am Südbahnhof" : "F265E56F",
    "Am Südring-Center" : "1AAC7070",
    "Am Timpenkotten" : "46620BA2",
    "Am Tollstock" : "917402E4",
    "Am Trappenhof" : "E23D2080",
    "Am Venn" : "87E4CBFB",
    "Am Vogelpoth" : "A02483ED",
    "Am Vöingholz" : "BAB7E49F",
    "Am Vorthbach" : "FF213C27",
    "Am Weckelsberg" : "998490D9",
    "Am Wienberg" : "F2144626",
    "Amselweg" : "80DE4E33",
    "An der Berufsschule" : "EA4BCBEF",
    "An der Dringenburg" : "441D87FD",
    "An der Gräfte" : "9DDBF4F4",
    "An der Harre" : "305D44A8",
    "An der Hasenhegge" : "27FF8603",
    "An der Knippenburg" : "4AAFB096",
    "An der Kommende" : "BEA86445",
    "An der Kornbecke" : "61D63B58",
    "An der Linde" : "7EDF1473",
    "An der Martinskirche" : "410D2E8C",
    "An der Sandbahn" : "DE66C886",
    "An der Sandgrube" : "341A84D3",
    "An der Windmühle" : "6E61DD69",
    "An Liebfrauen" : "B6D9837D",
    "An Luggesmühle" : "16C34FA2",
    "An St. Franziskus" : "C55C205D",
    "An St. Johannes" : "9A79D882",
    "Andreas-Hofer-Straße" : "054E63D4",
    "Andresen Strang" : "46CD76C0",
    "Anton-Brandt-Weg" : "9F6FB26D",
    "Antonius-Küster-Weg" : "940C0C06",
    "Antoniusstraße" : "8C241A87",
    "Arenbergstraße" : "A264B2EE",
    "Armelerstraße" : "5E260648",
    "Arminiusstraße" : "68DEF932",
    "Arnsmannstraße" : "62CB8DC8",
    "Arwinkel" : "90D70C1E",
    "Asbeckstraße" : "EC26BFAB",
    "Aspelstraße" : "BBB8609D",
    "Auf dem Espel" : "B7CBB3DD",
    "Auf dem Schimmel" : "2D6EDC65",
    "Auf dem Timpen" : "BC22200D",
    "Auf der Bette" : "F69AD57E",
    "Auf der Bredde" : "A6E96C8E",
    "Auf der Höhe" : "A8B1F6E1",
    "Auf der Kämpe" : "911CF662",
    "Auf der Koppe" : "86DD0890",
    "August-Schmidt-Weg" : "F4883EEE",
    "Augustin-Wibbelt-Straße" : "81149ED5",
    "Aulkestraße" : "CFA073A3",
    "Bachstraße" : "7D14579A",
    "Bahnhofstraße" : "F5503A3F",
    "Bannizastraße" : "0D92E935",
    "Barbarastraße" : "3309FCC3",
    "Batenbrockstraße" : "A7660940",
    "Baukelstraße" : "130CF83E",
    "Baurstraße" : "98AAC7BA",
    "Beckheide" : "CA63237F",
    "Beckstraße" : "99E8C12A",
    "Beethovenstraße" : "83DCCA58",
    "Beisenstraße" : "D4C17A31",
    "Bellenbrockstraße" : "B19D43F5",
    "Benzstraße" : "22AFEF85",
    "Bergbaustraße" : "BD0A053F",
    "Bergendahlstraße" : "313D604D",
    "Bergiusstraße" : "1B5D9127",
    "Bergstraße" : "5E407ED6",
    "Berliner Berg" : "B2428172",
    "Berliner Platz" : "3307F620",
    "Bernestraße" : "F6799C7E",
    "Bernhard-Poether-Weg" : "EFE99015",
    "Bernsmannweg" : "0B1DB078",
    "Beyrichstraße" : "3041DD29",
    "Binsenkamp" : "C6A659BB",
    "Birkenstraße" : "F8E9887D",
    "Birkenweg" : "C9482F31",
    "Birkhahnweg" : "1471C98A",
    "Blankenstraße" : "AC05AF8A",
    "Blaufärberweg" : "7D53A41B",
    "Blücherstraße" : "A9D753D3",
    "Blumenstraße" : "B03FB4CB",
    "Böckenhoffstraße" : "BAF9DA31",
    "Böcklinstraße" : "FB79C287",
    "Bodelschwinghstraße" : "5922F297",
    "Bögelsheide" : "AC64389E",
    "Bogenstraße" : "F7748124",
    "Bohnekamp" : "FFF960EB",
    "Bonhoefferstraße" : "060C6485",
    "Börenstraße" : "BA8CED75",
    "Börker Feld" : "836E24CB",
    "Borsigweg" : "48FF40D7",
    "Boschstraße" : "44A6EED7",
    "Bothenstraße" : "F061F5FB",
    "Böttcherstraße" : "DD92068C",
    "Bottroper Straße" : "3864475B",
    "Boyer Markt" : "2B7A79A2",
    "Brabecker Feld" : "B98C156D",
    "Brabecker Weg" : "8EC573E0",
    "Brabus Allee" : "00AA2110",
    "Brahmweg" : "7C9C75BB",
    "Brakerstraße" : "8DAC934C",
    "Brandenheide" : "B476893B",
    "Brauerstraße" : "4F568A1F",
    "Braukstraße" : "D8F20275",
    "Brennerweg" : "C8FC376F",
    "Brentanostraße" : "3A3E7478",
    "Breslauer Straße" : "C51C9706",
    "Brinkstraße" : "5EFD2F0C",
    "Brockmannweg" : "BCE2A47E",
    "Brömerstraße" : "9001C583",
    "Bruder-Andreas-Weg" : "E8059590",
    "Brüggemannsweg" : "AEBDFF8A",
    "Brukterer Straße" : "68F9CE16",
    "Brünerstraße" : "E6856C31",
    "Brunhildenweg" : "20B969BA",
    "Brunsmannstraße" : "53FA39F5",
    "Buchbinderstraße" : "6C063F49",
    "Buchenstraße" : "CA5B15FD",
    "Bügelstraße" : "BABE47DF",
    "Bülowstraße" : "441FD08D",
    "Burenbrock" : "F5916CAA",
    "Burghof" : "C1B51CB5",
    "Burgstraße" : "A3562E2B",
    "Carl-Heinz-Stephan Straße" : "EB95C357",
    "Carl-Heinz-Stephan-Straße" : "38489165",
    "Christfurth" : "026A19FF",
    "Christian-Fabian-Straße" : "09ABEDEB",
    "Christine-Teusch-Straße" : "AC0CC7F8",
    "Cleffstraße" : "FAB1FD5F",
    "Clemens-Hofbauer-Straße" : "BDA4F23C",
    "Clemens-Kraienhorst-Straße" : "1A11134E",
    "Corinthweg" : "E7512591",
    "Daimlerstraße" : "F6E6178C",
    "Dännenkamp" : "DBF48ED4",
    "Danziger Straße" : "B73A59F5",
    "Devensstraße" : "4ADF815B",
    "Dickebank" : "406D0DE4",
    "Dieselstraße" : "19E49B84",
    "Dinslakener Straße" : "1CB74553",
    "Döckelhorst" : "BE48CDB6",
    "Dorfheide" : "3FC34ADB",
    "Dorstener Straße" : "9457591C",
    "Dr.-Kock-am-Brink-Weg" : "6E50BD3B",
    "Drechslerstraße" : "CD105329",
    "Dresdener Straße" : "28CC1216",
    "Dreufte" : "C2F58C3B",
    "Droßlingstraße" : "41BF1926",
    "Drosselweg" : "F0CBE5B7",
    "Droste-Hülshoff-Platz" : "30B83D41",
    "Droste-Hülshoff-Straße" : "FAA382F4",
    "Düppelstraße" : "1B13EFD7",
    "Ebelstraße" : "25970BEE",
    "Ehrenplatz" : "30DF63B4",
    "Eichendorffstraße" : "CDB59E69",
    "Eichenkamp" : "6443B7D0",
    "Eichenstraße" : "659A1F4F",
    "Einbleckstraße" : "DB1EF55C",
    "Ekampsweg" : "5004125E",
    "Elisabeth-Giese-Straße" : "80A6A394",
    "Emscherstraße" : "A0CFC695",
    "Erlengasse" : "93DBFCEA",
    "Ernst-Ender-Straße" : "580DCE96",
    "Ernst-Moritz-Arndt-Straße" : "D2E8AC03",
    "Ernst-Wilczok-Platz" : "EEEB657D",
    "Essener Straße" : "44FB7348",
    "Eupenstraße" : "28863629",
    "Everstraße" : "92FF1BC5",
    "Fähndrichsweg" : "10D38C93",
    "Falkenweg" : "9D6ECDFE",
    "Färberweg" : "67C321EB",
    "Fasanenweg" : "B149911C",
    "Feldhausener Straße" : "84CBC627",
    "Feldstraße" : "7D2CB127",
    "Fernewaldstraße" : "C55DBB3B",
    "Feuerbachstraße" : "48C693EA",
    "Feuerwerkerstraße" : "145C863B",
    "Fichtestraße" : "744303A7",
    "Finkenweg" : "87D109F2",
    "Fischedickstraße" : "0FFDD1BD",
    "Florianweg" : "F34C3382",
    "Flöttestraße" : "3AABA526",
    "Fontanestraße" : "6B0AB7BE",
    "Förenkamp" : "796F58FA",
    "Forststraße" : "12E6AA00",
    "Fortkamp" : "A84B57E8",
    "Fortsetzungsstraße" : "210028DF",
    "Frankestraße" : "3D9DFBAE",
    "Franz-Kafka-Straße" : "97894AFA",
    "Freiherr-vom-Stein-Straße" : "6203E81C",
    "Freiligrathstraße" : "5F710FBA",
    "Friedenstraße" : "71AC4FCF",
    "Friedrich-Bitter-Weg" : "05390E96",
    "Friedrich-Ebert-Straße" : "2C4E71E5",
    "Fries Kamp" : "4546F685",
    "Fritz-Reuter-Straße" : "61C0E7FC",
    "Fröbelstraße" : "1564CD51",
    "Fuchsstraße" : "2BF3B700",
    "Fundermannsweg" : "8633859D",
    "Funkestraße" : "88EDEDA4",
    "Gabelsbergerstraße" : "A2D3E7D3",
    "Gahlener Straße" : "2D61F361",
    "Gartenstraße" : "9A3B54E5",
    "Geibelstraße" : "7B7523CC",
    "Geitlingsweg" : "B8741FC2",
    "Gerberstraße" : "C0193A39",
    "Gerhard-Küchen-Straße" : "976271E0",
    "Gerhart-Hauptmann-Straße" : "E9D02382",
    "Gerichtsstraße" : "013B3ABD",
    "Germaniahof" : "87BFE3FA",
    "Germaniastraße" : "A0546C29",
    "Gernotstraße" : "15AD2E58",
    "Gertskamp" : "9F6FC8F9",
    "Geschwister-Scholl-Weg" : "3501754D",
    "Giesenfort" : "29991C53",
    "Gildestraße" : "EDE60EF7",
    "Ginsterweg" : "698B7008",
    "Gladbecker Straße" : "60C28030",
    "Glasbläserweg" : "1E4FAE2A",
    "Glaserhüttenheide" : "E222E710",
    "Gleiwitzer Platz" : "73B1ADEA",
    "Glückaufstraße" : "DFC6F14D",
    "Goebenstraße" : "216923C7",
    "Goethestraße" : "56E21859",
    "Gohrweide" : "8FE1A3C0",
    "Goldammerweg" : "400742D1",
    "Gorch-Fock-Straße" : "300547E9",
    "Görkenstraße" : "E7BBCF67",
    "Gottfried-Kappen-Weg" : "A057EAA0",
    "Gräffstraße" : "4E7DC5C7",
    "Gregorstraße" : "3D5A3390",
    "Grenzstraße" : "2F6CC989",
    "Grotenweg" : "E837D1EB",
    "Grüner Weg" : "7AE9EE02",
    "Grünewaldstraße" : "7F714E1F",
    "Grüteringsfeld" : "719A79C4",
    "Grüterstraße" : "46958E6F",
    "Güldenberg" : "54782324",
    "Gungstraße" : "355AB072",
    "Gustav-Freytag-Straße" : "3D3D6DF8",
    "Gustav-Ohm-Straße" : "86F57C83",
    "Gutenbergstraße" : "5E614817",
    "Haardtstraße" : "2C42754F",
    "Habichtweg" : "2797BE3E",
    "Hackfurthstraße" : "03659FDE",
    "Hafenstraße" : "46F511C7",
    "Hagenbrockstraße" : "50743ECB",
    "Hagenstraße" : "0C54E949",
    "Händelstraße" : "A4E490BE",
    "Hanielstraße" : "D906F388",
    "Hans-Böckler-Straße" : "8D00BA2D",
    "Hans-Dringenberg-Weg" : "7AE35E51",
    "Hans-Sachs-Platz" : "6CB5CCDA",
    "Hans-Sachs-Straße" : "471F593F",
    "Hansastraße" : "67621920",
    "Hansiepenbusch" : "15A33221",
    "Hardenbergstraße" : "57D0B331",
    "Harkortstraße" : "6284A1AD",
    "Haßlacher Straße" : "B2553933",
    "Hauptstraße" : "9CBCBFFF",
    "Haus-Hove-Straße" : "08256317",
    "Haverkamp" : "D1E26F57",
    "Hebeleckstraße" : "6DCBC8E3",
    "Heckenweg" : "C124165F",
    "Hegelstraße" : "B17DC3C2",
    "Hegestraße" : "5F523FC9",
    "Heidenheck" : "BEF9D420",
    "Heidestraße" : "EDA882F8",
    "Heideweg" : "5069599A",
    "Heimannstraße" : "57DFCA3A",
    "Heimbruch" : "043F207C",
    "Heimersfeld" : "DDD6BB0D",
    "Heinrich-Grewer-Straße" : "A5AE040D",
    "Heinrich-Gutermuth-Straße" : "4D85F3AA",
    "Heinrich-Heine-Straße" : "7BC510C1",
    "Heinrich-Hertz-Straße" : "28498F2D",
    "Heinrich-Kämpchen-Straße" : "BEF103D7",
    "Heinrich-Lersch-Straße" : "9EFA076E",
    "Heinrich-Theißen-Straße" : "06608F42",
    "Hellen Str." : "98B32402",
    "Hemmers Pöhlken" : "EFAE8F7A",
    "Henry-Dunant-Straße" : "78EEA881",
    "Herderstraße" : "2D44EEEA",
    "Hermann-Löns-Straße" : "01C670A0",
    "Herzogstraße" : "D53BF04B",
    "Hetkamp" : "AE7DE4EA",
    "Heuweg" : "2103C78F",
    "Hiberniastraße" : "BFB07C69",
    "Hiesfelder Straße" : "A8C1F9AC",
    "Hochstraße" : "9AC5EC6D",
    "Hofkamp" : "C0F835ED",
    "Hofwiese" : "9C751972",
    "Hohe Heide" : "840C40BD",
    "Hoheheideweg" : "534ADE85",
    "Höhenweg" : "E3DE9D8A",
    "Hohes Feld" : "783D58C6",
    "Holbeinstraße" : "34AB73E5",
    "Hölderlinstraße" : "085D6131",
    "Holtfortstraße" : "2EF3833D",
    "Holthausener Straße" : "B2BD0998",
    "Holunderweg" : "1E20C89B",
    "Holzfällerweg" : "F42C4158",
    "Horstbruch" : "EEC8F867",
    "Horster Straße" : "EAEBB2F3",
    "Horsthofstraße" : "AD61A883",
    "Horstkamp" : "0FB023EE",
    "Höttkesweg" : "05113CD4",
    "Hövekesweg" : "F4B7578B",
    "Hovermannstraße" : "CA7CBEE4",
    "Hugo-Reckmann-Straße" : "12988F57",
    "Hugo-Stinnes-Straße" : "303E4434",
    "Humboldtstraße" : "2F128C57",
    "Hünefeldstraße" : "361383BF",
    "Husemannstraße" : "8B49EDC0",
    "Hüskensheide" : "443EA9BC",
    "Huyssenstraße" : "8C222094",
    "Im Acker" : "DE741EB9",
    "Im Beckedal" : "498E4817",
    "Im Beckram" : "91D383ED",
    "Im Blankenfeld" : "4447F915",
    "Im Boytal" : "3FAACF8E",
    "Im Brahmkamp" : "CAAAEC3D",
    "Im Breil" : "6F43B815",
    "Im Brinkmannsfeld" : "149F9813",
    "Im Dorbusch" : "8AEB2BFA",
    "Im Emscherbruch" : "85DA5E0D",
    "Im Flaßviertel" : "ABA196CE",
    "Im Fuhlenbrock" : "3F17CC1A",
    "Im Gewerbepark" : "AC1560E8",
    "Im Grund" : "8E614621",
    "Im Gungfeld" : "DFE0FBCB",
    "Im Hülsfeld" : "35C22BBA",
    "Im Johannestal" : "0C983AB8",
    "Im Kamp" : "EB55D0BF",
    "Im Loh" : "5ED175B4",
    "Im Mallingforst" : "069C5F6F",
    "Im Mandel" : "72AFD44E",
    "Im Nieland" : "BD1ED5F1",
    "Im Pinntal" : "3F6F04A5",
    "Im Scheierbruch" : "E35D7DAA",
    "Im Schwarzwald" : "D743FFC4",
    "Im Spring" : "A214D09E",
    "Im Springfeld" : "6112A9BD",
    "Im Stadtgarten" : "AF30C1CE",
    "Im Sundern" : "1D9C4097",
    "Im Tauschlag" : "0A61313E",
    "Im Venn" : "BD355679",
    "Im Wenkendiek" : "C9B31F9B",
    "Im Werth" : "6DD4A39A",
    "Im Wildland" : "1FFF0B13",
    "Im Wilmkesfeld" : "259361EB",
    "Im Winkel" : "153A3295",
    "Imbuschstraße" : "8E932AF3",
    "Imkerweg" : "3AE2DAAD",
    "Immermannstraße" : "6265A27F",
    "In Boymannsheide" : "8FD9965A",
    "In den Höfen" : "0BD9D16B",
    "In den Weywiesen" : "615BA6FD",
    "In den Weywiesen (nach der Sperre)" : "9A9D0D49",
    "In der Boverheide" : "D61837E9",
    "In der Bräuke" : "C481A0A0",
    "In der Koppel" : "B24B6A73",
    "In der Littersheide" : "D6AC48D8",
    "In der Miere" : "61423351",
    "In der Schanze" : "4E53D301",
    "In der Welheimer Mark" : "9B4516C2",
    "Industriestraße" : "516BF5E9",
    "Jahnstraße" : "30616C40",
    "Johann-Breuker-Platz" : "0C0495E6",
    "Johannesstraße" : "8BA69D74",
    "Josef-Albers-Straße" : "90D50F13",
    "Josefstraße" : "47255709",
    "Kalverkamp" : "979BFA7B",
    "Kampstraße" : "AEB9E687",
    "Kantstraße" : "14CE83D4",
    "Kapellenstraße" : "BEEEC465",
    "Kapitän-Lehmann-Straße" : "6F18319D",
    "Kaplan-Xanten-Straße" : "99E4BFE5",
    "Kardinal-Hengsbach-Straße" : "5816B01A",
    "Karl-Englert-Straße" : "885402D8",
    "Karl-Peters-Straße" : "0E8CEFC6",
    "Karl-Rahner-Straße" : "030F4A23",
    "Karl-Wessels-Straße" : "1DC6885A",
    "Kastanienweg" : "78330484",
    "Käthe-Kollwitz-Straße" : "30A269C2",
    "Kaulbachstraße" : "CE8BCCFE",
    "Kellermannstraße" : "8D9C73C4",
    "Kettelerstraße" : "665623F0",
    "Kiefernweg" : "863238DE",
    "Kirchhellener Ring" : "16DC2C9B",
    "Kirchhellener Straße" : "2F2B391A",
    "Kirchplatz" : "B828F1A1",
    "Kirchstraße" : "B13B83BA",
    "Klaus-Groth-Straße" : "5DD11573",
    "Kleinebrechtshof" : "C32DE63E",
    "Kleiststraße" : "E7860A44",
    "Klopriesstraße" : "13F9E527",
    "Klosterstraße" : "0580E202",
    "Knappenstraße" : "74853538",
    "Köckenkamp" : "A280BA3D",
    "Köhlerstraße" : "C2B195C2",
    "Kolkenbrockstraße" : "891CC7A9",
    "Kolpingplatz" : "3D5E4285",
    "Königsberger Straße" : "239A7F47",
    "Koppenborgsweg" : "C7A4DE30",
    "Körnerstraße" : "FAAD726C",
    "Körtlingsfeld" : "C76BFC9E",
    "Korzmannstraße" : "30C776F7",
    "Kösterstraße" : "5F17E641",
    "Kraneburgstraße" : "75ADF557",
    "Kreienkampsweg" : "B35701EC",
    "Kreulshof" : "833DD172",
    "Kreuzkamp" : "FA40C6DC",
    "Kriemhildenweg" : "A2D8AECF",
    "Krümmerstraße" : "394F60BF",
    "Krusestraße" : "C53F5BCF",
    "Küferstraße" : "FBA0F3EC",
    "Kurt-Feller-Straße" : "05794E15",
    "Laerkamp" : "79F1F215",
    "Ledderkesweg" : "841A48A1",
    "Lehmkuhler Straße" : "E335696C",
    "Lehmschlenke" : "BEABD7B7",
    "Leiblstraße" : "13B42EBE",
    "Leibnizstraße" : "A4007F2A",
    "Lemmhof" : "BD4B5BE0",
    "Lenbachstraße" : "2373D582",
    "Lerchenweg" : "F4880105",
    "Lessingstraße" : "25D3833C",
    "Liboriweg" : "321B5374",
    "Lichtenhorst" : "175B92B4",
    "Liebrechtstraße" : "D591AC83",
    "Liesenfeldstraße" : "A47AD86F",
    "Lilienthalstraße" : "362283EF",
    "Lindenstraße" : "416CAA1B",
    "Lindhorststraße" : "630B9D59",
    "Lippweg" : "2AA8EC54",
    "Loewenfeldstraße" : "05CC199B",
    "Lohbraucksweg" : "4E8AE944",
    "Lortzingstraße" : "3F5ACEA4",
    "Lossenstraße" : "3547A2A0",
    "Lüderitzstraße" : "54F2E9BB",
    "Ludgeristraße" : "8B816B7D",
    "Ludwig-Richter-Straße" : "A11611AB",
    "Luise-Hensel-Straße" : "EE5DA8F6",
    "Lukas-Cranach-Straße" : "4D13C81E",
    "Lüningstraße" : "DDECE292",
    "Lütkestraße" : "75B279E0",
    "Lützowstraße" : "8ED5F860",
    "Marienstraße" : "C6A6503C",
    "Martin-Luther-Straße" : "3BFEFAF1",
    "Mathias-Stinnes-Platz" : "7A073FAB",
    "Matthias-Claudius-Straße" : "22BF835A",
    "Matthias-Kirch-Weg" : "9917DE7D",
    "Max-Schwarze-Weg" : "2D3104C9",
    "Max-Stieler-Straße" : "C696C80F",
    "Maybachweg" : "E41A17DC",
    "Maystraße" : "D6CA0214",
    "Meisenweg" : "6AE06B82",
    "Memelstraße" : "7E46C2F9",
    "Menzelstraße" : "13626849",
    "Mercatorstraße" : "ADCDC6B2",
    "Mesteroth" : "E68F62CC",
    "Middeweg" : "9AD63AFA",
    "Mirkstraße" : "0336E88E",
    "Möddericher Straße" : "329704AF",
    "Moltkestraße" : "60767122",
    "Mommkamp" : "F27FBE91",
    "Mönchenort" : "5EB79E90",
    "Morianstraße" : "878CF33E",
    "Mozartstraße" : "35DC37C0",
    "Mühlenflötte" : "B74F23CE",
    "Mühlenpatt" : "9EB19352",
    "Mühlenstraße" : "C1134683",
    "Münsterstraße" : "61A8ABEB",
    "Mutter-Theresa-Straße" : "C880D14E",
    "Nathrathstraße" : "77D61800",
    "Nesselstraße" : "B2C637AB",
    "Neue Heide" : "D1083718",
    "Neuenkamp" : "6C89C5C7",
    "Neustraße" : "0F7F6E4C",
    "Nibelungenweg" : "A8756590",
    "Nikolaus-Groß-Straße" : "DAD82C13",
    "Nordhellenstraße" : "09E6D865",
    "Nordring" : "763DCF13",
    "Norpothstraße" : "29E4374B",
    "Oberhausener Straße" : "321F8137",
    "Oberhofstraße" : "44C8C552",
    "Oppenbergstraße" : "F3C66DEB",
    "Ortbergstraße" : "8D66CD47",
    "Oskarstraße" : "5600D96E",
    "Osterfelder Straße" : "5B8341FD",
    "Ostring" : "E8C5734F",
    "Ottenkamp" : "5F1AD226",
    "Ottenschlag" : "83F51016",
    "Otto-Joschko-Straße" : "80DFF3CD",
    "Otto-Krawehl-Straße" : "EDE3131B",
    "Overbeckstraße" : "9A13BC74",
    "Overhagener Feld" : "7D7229B2",
    "Packskamp" : "CF34BC49",
    "Papenheide" : "501E94A0",
    "Parkstraße" : "A913A56F",
    "Paßstraße" : "74981B40",
    "Pastor-Abel-Straße" : "799E1394",
    "Pastor-Dahlmann-Str." : "6C3C5B79",
    "Pastor-Dahlmann-Straße" : "65311D86",
    "Pater-Delp-Straße" : "DBA0790A",
    "Pater-Dieckmann-Straße" : "11AD3259",
    "Pater-Diekmann-Str." : "D439D81E",
    "Pater-Diekmann-Straße" : "0A3ABF4C",
    "Pater-Gahlen-Str." : "0B0E39B5",
    "Pater-Gahlen-Straße" : "FE1EA51A",
    "Pater-Markus-Weg" : "A84CA4A4",
    "Paul-Gerhardt-Allee" : "8FD13066",
    "Paul-Moor-Weg" : "0312E0C6",
    "Paul-Schlesinger-Straße" : "F38F809D",
    "Pelsstraße" : "488DB5B5",
    "Perdekampsheide" : "4E1D31AF",
    "Pestalozzistraße" : "92ED8187",
    "Peterstraße" : "571E5EA0",
    "Pfarrstraße" : "A3AB7C9A",
    "Pferdekampsheide" : "84211F5E",
    "Pferdemarkt" : "64F021EF",
    "Plaggenbahn" : "7C9ECAFB",
    "Plankenschemm" : "E24A6D2F",
    "Polderstraße" : "C3526D37",
    "Poststraße" : "170E4FBC",
    "Pöttering" : "75238D7C",
    "Prosperstraße" : "5E59A65D",
    "Prozessionsweg" : "B95574A3",
    "Raiffeisenstraße" : "83FA1D7D",
    "Randebrockstraße" : "6B9D0133",
    "Räuwenkamp" : "B04410E1",
    "Reckelsberg" : "09BC376C",
    "Reckmannallee" : "F5FBEF47",
    "Rentforter Straße" : "34D7A8C7",
    "Repeler Heide" : "8943F75A",
    "Repeler Weg" : "AD338915",
    "Reulstraße" : "D415A6E1",
    "Rhaland" : "91A84493",
    "Rheinbabenstraße" : "8368694D",
    "Rheinstahlstraße" : "B8FC1961",
    "Richard-Wagner-Straße" : "295D072C",
    "Rilkeweg" : "77B986A3",
    "Rippelbeckstraße" : "4D88A285",
    "Robert-Brenner-Straße" : "AD589D14",
    "Robert-Florin-Straße" : "22AB9882",
    "Rochusstraße" : "04418CA5",
    "Rohrbrauk" : "B0519980",
    "Rolandstraße" : "A2AD4AD7",
    "Röntgenstraße" : "0CD36D19",
    "Roonstraße" : "9F08FC65",
    "Röttgersbank" : "8187BE2C",
    "Rotthardt" : "09A504C3",
    "Rübenkamp" : "D925A825",
    "Rubensstraße" : "1BD1B015",
    "Ruhehorst" : "F0B4A926",
    "Ruhrölstraße" : "D64D414C",
    "Saarstraße" : "3CF55EFD",
    "Sarterstraße" : "5C0E0A5C",
    "Sattlerweg" : "5C429CBD",
    "Schäferweg" : "015A8B45",
    "Schantzstraße" : "CF1E87E0",
    "Scharfstraße" : "32F7EEA5",
    "Scharnhölzfeld" : "A691A4EA",
    "Scharnhölzstraße" : "E6AF4763",
    "Scheideweg" : "14750805",
    "Schellingstraße" : "45115693",
    "Schildstraße" : "64583584",
    "Schillerstraße" : "73F63CE4",
    "Schillstraße" : "CFDA2711",
    "Schlagkamp" : "13AAB6EB",
    "Schlaunstraße" : "252C9D14",
    "Schlesierstraße" : "85BD39DA",
    "Schloßgasse" : "DF110323",
    "Schmiedestraße" : "203746F1",
    "Schneiderstraße" : "3896F883",
    "Schnepfenweg" : "E5C50ABF",
    "Schubertstraße" : "1E6763D4",
    "Schuhmacherstraße" : "28539CD1",
    "Schulstraße" : "E8F7A27F",
    "Schulten Brauk" : "FBF3877F",
    "Schultenkamp" : "A6E2E81E",
    "Schültingstraße" : "99F17AEB",
    "Schulze-Delitzsch-Straße" : "EB48AA97",
    "Schumannstraße" : "593D1E00",
    "Schürbrink" : "7E0D55F1",
    "Schürmannstraße" : "EAB1EBA4",
    "Schützenstraße" : "7C8BDA24",
    "Schwarthoffstr." : "259A551C",
    "Schwarwiese" : "91168365",
    "Senheimer Straße" : "CE0C1D14",
    "Sensenfeld" : "1FB57C96",
    "Siegfriedstraße" : "CD797286",
    "Siemensstraße" : "772D30E4",
    "Siepenstraße" : "EB369F59",
    "Sonnenschein" : "5F23D324",
    "Spechtstraße" : "481BED22",
    "Speckenbruch" : "2D587A5B",
    "Spenglerweg" : "4444CF21",
    "Sperberweg" : "79AB18FB",
    "Sperlingsweg" : "9249889C",
    "Spickenbaumsweg" : "B2261AF2",
    "Spitzwegstraße" : "11A5F6DF",
    "Steigerstraße" : "74FA9423",
    "Steinbrinkstraße" : "C0953965",
    "Steinmannswiese" : "E261B010",
    "Steinmetzstraße" : "2D705592",
    "Stellmacherstraße" : "F0EA7923",
    "Stenkhoffstraße" : "17FBC6B7",
    "Sterkrader Straße" : "F2A2738E",
    "Stettiner Straße" : "E01EF4C3",
    "Streuwiese" : "1E3567AA",
    "Sturmshof" : "07DEA151",
    "Südring" : "7389285C",
    "Südring-Center-Promenade" : "5BEBADDD",
    "Suitbertstraße" : "49C68DD4",
    "Sydowstraße" : "2240FC40",
    "Taeglichsbeckstraße" : "CC62CCBE",
    "Tannenstraße" : "0CF840E7",
    "Tappenhof" : "41DCFF45",
    "Theo-Kleppe-Weg" : "698ECA16",
    "Theodor-Storm-Straße" : "FCE3CC20",
    "Thomastraße" : "68F9BEAC",
    "Tilsiter Straße" : "126C4A18",
    "Töfflinger Straße" : "38176D0F",
    "Töpferstraße" : "AC68F4E7",
    "Töttelberg" : "85C347D4",
    "Tourcoingstraße" : "F8FE060B",
    "Tourneaustraße" : "82F1C145",
    "Trappenstraße" : "F9C52345",
    "Tuchmacherstraße" : "6F9EC841",
    "Uhlandstraße" : "204D5969",
    "Ulmenplatz" : "3490E329",
    "Unterberg" : "A4DE6F40",
    "Up De Wälle" : "767653B7",
    "Utschlagstraße" : "A4796E74",
    "Veenstraße" : "17EE935A",
    "Velsenstraße" : "D8357026",
    "Veszpremer Straße" : "27422F13",
    "Vienkenstraße" : "C9C3F552",
    "Vikars Kamp" : "3DAAA122",
    "Viktoriastraße" : "F212ACB6",
    "Virchowstraße" : "F3D18FAC",
    "Vogelsrauh" : "9ECC71A7",
    "Von-Braun-Straße" : "22B71A3C",
    "Von-Galen-Straße" : "F61B9345",
    "Vonderbergstraße" : "EB4F49ED",
    "Vonderorter Straße" : "4E180683",
    "Vossundern" : "47A37D49",
    "Wacholderweg" : "B5EE9BBE",
    "Wachtmeisters Kamp" : "3D425EFC",
    "Wagenfeldstraße" : "61C7351C",
    "Waldstraße" : "D83AF3BB",
    "Waldthausenstraße" : "E9547B6F",
    "Wallmannstraße" : "1B9FBA16",
    "Walter-Flex-Straße" : "36A6816E",
    "Walter-Höfer-Weg" : "B3AF3B5A",
    "Walter-Spindler-Straße" : "1876C385",
    "Wankelstraße" : "718099EB",
    "Warner-Allee" : "F9CB722B",
    "Waterkampstraße" : "C4E8DDE2",
    "Weberstraße" : "D741BA94",
    "Weilbrock" : "42C8CB4B",
    "Weißfeld" : "998A5B05",
    "Welheimer Straße" : "DF012D2D",
    "Wellbraucksweg" : "89B41EEF",
    "Werkstraße" : "567AD575",
    "Weseler Weg" : "C31591F8",
    "Westring" : "E7EDC08E",
    "Weusterstraße" : "3952612B",
    "Wiedau" : "204666E2",
    "Wielandstraße" : "7858444D",
    "Wienkamp" : "FD6C2016",
    "Wiesengrund" : "6F8D93DB",
    "Wiesental" : "468BB36D",
    "Wiggermannstraße" : "9217AFF4",
    "Wildbruch" : "C771A4C4",
    "Wildenhoff" : "C785B242",
    "Wildestraße" : "6E83E4ED",
    "Wilhelm-Busch-Straße" : "34E99065",
    "Wilhelm-Raabe-Straße" : "C54647F3",
    "Wilhelm-Tell-Straße" : "AA7AA730",
    "Wilhelm-Tenhagen-Straße" : "99D36DF1",
    "Windmühlenweg" : "E7D41B64",
    "Winkelsheide" : "62CD1743",
    "Wissmannstraße" : "F0E49002",
    "Wittekindstraße" : "E0E82B3C",
    "Wittstammstraße" : "6B7C74F8",
    "Wohlgemuthstraße" : "88326A3B",
    "Wörkamp" : "30708047",
    "Wortmannstraße" : "6AFEE94C",
    "Wrangelstraße" : "DB1A26FD",
    "Zeppelinstraße" : "E3F42272",
    "Ziegelstraße" : "12B71F4F",
    "Zieroth" : "FF4C3E24",
    "Zollverein" : "1C8700DC",
    "Zum Haldenblick" : "4BA79B15",
    "Zum Heidhof" : "EFA9BD8E",
    "Zum Kletterpoth" : "1B0222DA",
    "Zum Prosperpark" : "C4D49F08",
    "Zunftstraße" : "F6E4CB09",
    "Zur Grafenmühle" : "C5A03A66"
}