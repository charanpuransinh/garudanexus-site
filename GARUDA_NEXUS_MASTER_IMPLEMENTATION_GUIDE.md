# GARUDA NEXUS

## Master Website --- Complete Design, Content & Implementation Guide

**दस्तावेज़:** आधिकारिक Master Implementation Guide\
**संस्करण:** 1.0.0\
**मुख्य डोमेन:** `https://garudanexus.com`\
**उद्देश्य:** इस दस्तावेज़ को पढ़कर एजेंट मौजूदा Garuda Nexus वेबसाइट की जाँच करे और
एकीकृत, बहु-सेक्टर कॉर्पोरेट वेबसाइट को सही ढंग से लागू करे।\
**स्थिति:** कार्यान्वयन निर्देश; अपने-आप में उत्पादन स्वीकृति नहीं।

------------------------------------------------------------------------

# 1. एजेंट के लिए सर्वोच्च निर्देश

इस फ़ाइल को शुरू से अंत तक पढ़ें। इसके बाद repository, मौजूदा वेबसाइट, उपलब्ध ZIP,
HTML, CSS, JavaScript/TypeScript, JSON, CSV, images और अन्य सामग्री का
निरीक्षण करें। फिर इस मार्गदर्शिका और वास्तविक उपलब्ध सामग्री के अनुसार सिस्टम लागू
करें।

यह केवल एक सुंदर landing page बनाने का काम नहीं है। अंतिम परिणाम एक ऐसा Master
Corporate Website होना चाहिए जिसमें:

1.  आगंतुक सबसे पहले Welcome Page देखे।
2.  Welcome से वास्तविक Home Page पर जाए।
3.  Home Page से About Garuda Nexus और सभी Business Divisions तक पहुँचे।
4.  हर Sector Card पर क्लिक करने से उसी सेक्टर का अलग पूर्ण पृष्ठ खुले।
5.  हर सेक्टर में अपनी categories, products, images, specifications और
    enquiry व्यवस्था हो।
6.  सभी पृष्ठ एक ही Garuda Nexus ब्रांड और डिज़ाइन प्रणाली का पालन करें।
7.  सार्वजनिक वेबसाइट और निजी IT application के access rules अलग रहें।

## अनिवार्य कार्य नियम

-   पहले निरीक्षण, फिर बदलाव। मौजूदा repository को समझे बिना rewrite न करें।
-   उपयोगकर्ता की मौजूदा सामग्री, उत्पाद डेटा, images, routes और काम कर रहे
    फीचर न हटाएँ।
-   duplicate pages, duplicate product records और duplicate navigation न
    बनाएँ।
-   कोई product, yarn count, technical specification, certification,
    warranty, company address, phone या business claim अनुमान से न लिखें।
-   उपलब्ध स्रोतों में विरोध हो तो चुपचाप एक को सही न मानें। conflict report करें।
-   मौजूदा सही URL को बिना कारण न बदलें। बदलाव जरूरी हो तो redirect और link
    audit करें।
-   secrets, API keys, passwords और private customer data को public
    repository या frontend में न रखें।
-   केवल "tests passed" को production-ready घोषित न करें। नीचे दिए गए सभी
    acceptance checks पूरे होने चाहिए।
-   किसी external system या application को बिना अधिकृत configuration के
    खुला access न दें।

------------------------------------------------------------------------

# 2. वेबसाइट का मुख्य अनुभव और Page Flow

मुख्य उपयोगकर्ता यात्रा:

`WELCOME PAGE → HOME PAGE → ABOUT / SECTOR CARDS → SELECTED SECTOR → CATEGORY → PRODUCT DETAIL → ENQUIRY`

## 2.1 Welcome Page

-   Garuda Nexus का स्वीकृत लोगो प्रमुखता से दिखे।
-   लोगो का उड़ता हुआ प्रवेश/animation सुरुचिपूर्ण और हल्का हो; अत्यधिक चमक, तेज़
    flashing या भारी animation न हो।
-   ब्रांड नाम: **GARUDA NEXUS**
-   ब्रांड descriptor: **GLOBAL TRADING SYSTEM**
-   मौजूदा स्वीकृत स्वागत-पंक्ति/धार्मिक वाक्य को अक्षरशः सुरक्षित रखें; उसे स्वयं बदलें
    या नया दावा न जोड़ें।
-   "Enter Website" वास्तविक Home Page route पर ले जाए। केवल text बदलना या
    `#home` पर रुकना स्वीकार्य नहीं।
-   मोबाइल पर animation हल्का हो और `prefers-reduced-motion` का सम्मान करे।
-   Welcome Page से Home Page पर जाने का स्पष्ट बटन हो।

## 2.2 Home Page

Home Page पर यह क्रम रखें:

1.  Header और मुख्य navigation
2.  Hero section: Garuda Nexus का संक्षिप्त, सत्यापित परिचय
3.  About Garuda Nexus का संक्षिप्त परिचय और "Read More"
4.  Business Divisions के Sector Cards
5.  प्रमुख Products & Solutions
6.  Garuda Nexus की कार्य-प्रणाली/व्यावसायिक दृष्टिकोण --- केवल सत्यापित तथ्य
7.  Enquiry / Contact section
8.  Footer

Home Page पर सभी सेक्टर कार्ड स्पष्ट रूप से दिखें। आगंतुक को किसी सेक्टर तक पहुँचने के
लिए अनावश्यक कई पृष्ठ पार न करने पड़ें।

## 2.3 मुख्य Navigation

प्रस्तावित navigation:

-   Home
-   About Garuda Nexus
-   Business Divisions
-   Products & Solutions
-   Knowledge / Resources
-   Contact / Enquiry

मोबाइल पर यह साफ़ और उपयोग में आसान menu में बदले। हर आंतरिक पृष्ठ पर logo,
navigation, आवश्यक breadcrumb और footer उपलब्ध हों।

------------------------------------------------------------------------

# 3. About Garuda Nexus --- कंपनी का मुख्य परिचय

`/about/`

यह पृष्ठ कंपनी की आधिकारिक पहचान का मुख्य स्रोत होगा। इसे केवल एक छोटा परिचय न
रखें। व्यवस्थित corporate profile बनाएँ।

## 3.1 प्रस्तावित Sections

1.  **Company Overview:** Garuda Nexus क्या है और इसका व्यावसायिक स्वरूप क्या
    है।
2.  **Business Philosophy / Vision:** उपयोगकर्ता द्वारा स्वीकृत दृष्टि और
    उद्देश्य।
3.  **Business Divisions:** सभी सेक्टरों का परिचय और उनके पृष्ठों के links।
4.  **Products & Services:** कंपनी के वास्तविक उत्पाद और सेवाएँ।
5.  **Business Model:** Trading, sourcing, supply, services या software
    development जैसे कार्य केवल वहीं लिखें जहाँ वे वास्तविक परियोजना सामग्री से
    प्रमाणित हों।
6.  **Quality & Documentation:** उपलब्ध quality documents, specifications
    और compliance जानकारी।
7.  **Contact & Enquiry:** सत्यापित संपर्क माध्यम।
8.  **Group Information:** समूह/संस्था संबंधी सामग्री केवल स्वीकृत आधिकारिक विवरण
    के आधार पर।

## 3.2 कंपनी की जानकारी भरने के नियम

नीचे के fields के लिए repository और user-provided documents में खोजें:

-   Registered / Business Name
-   Official business address
-   Official email
-   Business phone
-   GSTIN / CIN / अन्य पंजीकरण, यदि लागू और उपलब्ध हों
-   स्थापना वर्ष
-   नेतृत्व/टीम का परिचय, यदि स्वीकृत हो
-   वास्तविक कार्यक्षेत्र और सेवाएँ
-   आधिकारिक social links

**यदि जानकारी उपलब्ध नहीं है तो placeholder रखें और `CONTENT_REQUIRED.md` या
content status report में लिखें।** काल्पनिक पता, पंजीकरण, वर्ष, कर्मचारी संख्या,
ग्राहक, प्रमाणपत्र या उपलब्धि न जोड़ें।

------------------------------------------------------------------------

# 4. Home Page के मुख्य Sector Cards

Home Page पर प्रत्येक सेक्टर का अलग card हो। हर card में:

-   संबंधित sector की वास्तविक फोटो/चित्र
-   Sector Name
-   एक या दो पंक्तियों का सत्यापित परिचय
-   "Explore" / "View Products" action
-   पूरा card clickable हो, लेकिन accessibility के लिए स्पष्ट link भी रहे।

## 4.1 अनिवार्य सेक्टर

1.  **IT & Software Systems**
2.  **Textile & Yarn**
3.  **Mining Machinery & Repair Parts**
4.  **Solar Energy**
5.  **Agriculture & Herbal Products**
6.  **About Garuda Nexus / Group Information**

जहाँ Cotton Trading या अन्य उप-व्यवसाय अलग उपलब्ध हों, उन्हें Agriculture या
संबंधित सेक्टर के भीतर उचित स्थान दें; बिना कारण duplicate top-level cards न
बनाएँ।

------------------------------------------------------------------------

# 5. Textile & Yarn Division

**मुख्य route:** `/textile-yarn/`\
**Products route:** `/textile-yarn/products/`

यह सेक्टर केवल एक सामान्य परिचय पृष्ठ नहीं होगा। आगंतुक Yarn Card पर क्लिक करे तो
उसे yarn की अलग-अलग श्रेणियाँ दिखें। किसी category पर क्लिक करने पर उस yarn की
पूरी product detail खुले।

## 5.1 मुख्य Yarn Categories

उपलब्ध Garuda Nexus textile सामग्री के अनुसार निम्न categories को शामिल करें:

1.  Cotton Yarn
2.  Polyester Cotton (PC) Yarn
3.  Polyester Viscose (PV) Yarn
4.  Denim Yarn
5.  Viscose, Modal & Lyocell Yarn
6.  Melange & Fancy Yarn
7.  Recycled & Sustainable Yarn
8.  Acrylic Yarn
9.  Wool & Wool Blend Yarn
10. Silk Yarn
11. Polyester Filament / Filament Yarn
12. Denim Fabric
13. Suiting & Shirting Fabric
14. Thermal Knit Fabric
15. Polyester Filament Fabrics --- Surat

यदि मौजूदा approved data में अतिरिक्त yarn या fabric categories हों तो उन्हें भी
शामिल करें। सूची को hard-code करके भविष्य में बढ़ने से न रोकें।

## 5.2 उपलब्ध Yarn Variants

जहाँ संबंधित उत्पाद और supplier data में पुष्टि हो, वहाँ ये variants दिखाएँ:

-   Cotton: Carded, Combed, Open-End, Compact
-   Denim: Open-End, Ring Spun, Slub, Core-Spun
-   PC / PV: blend ratio और spinning system केवल वास्तविक supplier data के
    अनुसार
-   Viscose / Modal / Lyocell: प्रत्येक fibre का नाम और composition स्पष्ट रखें
-   Melange / Fancy: वास्तविक effect, shade और composition के अनुसार
-   Filament: POY, DTY --- उपलब्धता की पुष्टि के बाद

## 5.3 हर Yarn Product Detail Page

प्रत्येक yarn product के लिए अलग detail page या data-driven product view हो।
उसमें:

-   Product name
-   Yarn category
-   Yarn type / variant
-   Yarn Count (Ne), जहाँ उपलब्ध हो
-   Count range और count variation, केवल सत्यापित डेटा से
-   Fibre composition / blend ratio
-   Spinning process
-   Application / end use
-   Technical specifications
-   Product images / cone images / close-up texture
-   Manufacturer / supplier information, यदि साझा करने योग्य और सत्यापित हो
-   Availability / lead time, केवल current data से
-   Packing details
-   MOQ, यदि supplier ने दिया हो
-   Sample availability
-   Quality / test documents, यदि उपलब्ध हों
-   Buyer enquiry / RFQ form

### तकनीकी डेटा के संभावित fields

-   CSP
-   Twist per inch (TPI)
-   Strength
-   Elongation
-   Hairiness
-   Evenness
-   Count variation
-   Composition
-   Moisture / contamination limits, जहाँ supplier sheet में हों

**महत्वपूर्ण:** ये fields डेटा संरचना के लिए हैं। इनकी कोई संख्या या सीमा अनुमान से न
भरें। जहाँ डेटा उपलब्ध नहीं है वहाँ "Specification on request" या "Not provided"
दिखाएँ।

## 5.4 Textile Images

मौजूदा textile image assets और `textile_image_generator.py` जैसे उपलब्ध
स्रोतों की जाँच करें। मौजूदा filenames/paths सुरक्षित रखें। image generator का
उपयोग तभी करें जब आवश्यक API configuration और अनुमति उपलब्ध हो।

उपलब्ध category image filename slugs:

-   `cotton-yarn`
-   `polyester-cotton-pc-yarn`
-   `polyester-viscose-pv-yarn`
-   `denim-yarn`
-   `viscose-modal-lyocell-yarn`
-   `melange-fancy-yarn`
-   `recycled-sustainable-yarn`
-   `acrylic-yarn`
-   `wool-wool-blend-yarn`
-   `silk-yarn`
-   `denim-fabric`
-   `suiting-shirting-fabric`
-   `thermal-knit-fabric`
-   `polyester-filament-fabrics-surat`

Images को product के अनुरूप रखें। एक ही generic image सभी yarn categories पर
न लगाएँ। AI/reference image को वास्तविक supplier product photo बताकर प्रस्तुत
न करें। वास्तविक product image उपलब्ध न हो तो उसे illustrative/reference
image के रूप में चिह्नित करें।

------------------------------------------------------------------------

# 6. Solar Energy Division

**मुख्य route:** `/solar/`\
**Products route:** `/solar/products/`

Solar सेक्टर में केवल "Solar Panels" का एक card न रखें। इसे पूर्ण Solar PV
Products & Components Catalogue बनाएं। उपयोगकर्ता द्वारा पहले उपलब्ध कराए गए
Solar catalogue images और source assets को repository में खोजें और वास्तविक
assets का पुनः उपयोग करें।

## 6.1 मुख्य Solar Categories

-   Solar Panels
-   Solar Inverters
-   Solar Batteries
-   Charge Controllers
-   Solar Charger Kits
-   Structure & Mounting System
-   Cables & Connectors
-   DC / AC Distribution and Protection
-   Earthing & Safety
-   Monitoring & Metering
-   Maintenance & Cleaning Tools
-   On-Grid Solar Systems
-   Off-Grid Solar Systems
-   Hybrid Solar Systems
-   Solar Installation & Services

## 6.2 उपलब्ध Solar Catalogue Items

मौजूदा Solar catalogue source में निम्न numbered items दिखाई देते हैं। इन्हें
category-wise व्यवस्थित करें; उपलब्ध image/source को प्राथमिकता दें।

### Solar Panels & Power Equipment (01--08)

1.  Mono Solar Panel --- source label: 540W\
2.  Bifacial Solar Panel --- source label: 580W\
3.  On-Grid Inverter --- source label: 5kW--110kW\
4.  Hybrid Inverter --- source label: 5kW--10kW\
5.  Micro Inverter --- source label: 800W\
6.  Lithium Battery --- source label: 5kWh--10kWh\
7.  MPPT Charge Controller --- source label: 60A\
8.  Solar Charger Kit --- source label: 12V / 24V

### Structure & Mounting System (09--17)

9.  Rooftop Structure\
10. Ground Structure\
11. Carport Structure\
12. Rail\
13. Purlin\
14. Mid Clamp\
15. End Clamp\
16. Bolt Nut Kit\
17. Foundation Bolt

### Cables & Connectors (18--25)

18. DC Cable Red\
19. DC Cable Black\
20. AC Cable\
21. Earthing Cable\
22. MC4 Male\
23. MC4 Female\
24. Cable Tie\
25. Cable Clip

### Protection & Distribution (26--32)

इस group के लिए repository में मूल catalogue image/source पढ़कर exact item
names और specifications दर्ज करें। उपलब्ध source से बाहर के नाम या ratings
अनुमान से न बनाएं।

### Earthing & Safety (33--36)

33. Earthing Rod\
34. Lightning Arrester\
35. Earthing Strip\
36. Earth Pit Cover

### Monitoring & Metering (37--41)

37. Data Logger\
38. WiFi Dongle\
39. Energy Meter\
40. Net Meter\
41. CT Coil

### Maintenance & Tools (42--45)

42. Cleaning Brush\
43. Cleaning Sprinkler\
44. Spare MC4 Kit\
45. Tool Kit

## 6.3 Solar Product Detail Page

हर Solar item पर:

-   Product name और catalogue number
-   Category
-   Product photo
-   Model / capacity / rating, केवल source से
-   Technical specifications
-   Material / construction
-   Compatibility, यदि सत्यापित हो
-   Application
-   Warranty, केवल manufacturer documentation से
-   Datasheet / manual download, यदि उपलब्ध हो
-   Availability और enquiry

**महत्वपूर्ण:** ऊपर दिए गए wattage, voltage, current, dimensions और ranges
catalogue source के labels/उदाहरण हैं। इन्हें किसी specific brand/model की
verified guarantee न बताएं। हर item की actual datasheet से जाँच करें।
Catalogue में items 26--32 के exact नाम source image से पढ़ें; अनुमान न लगाएँ।

------------------------------------------------------------------------

# 7. Agriculture & Herbal Products Division

**मुख्य route:** `/agriculture/`\
**Products route:** `/agriculture/products/`

Agriculture division में उपलब्ध Garuda Nexus सामग्री के अनुसार ये छह products
शामिल करें:

1.  Psyllium Husk (Isabgol)
2.  Senna Leaves & Pods
3.  Ashwagandha Root
4.  Moringa Leaf Powder
5.  Fenugreek Seeds
6.  Aloe Vera Gel Powder 200:1

## 7.1 उपलब्ध product data

नीचे की जानकारी मौजूदा परियोजना सामग्री में उपलब्ध product notes के रूप में मिली
है। प्रकाशित करने से पहले वर्तमान supplier COA/specification से सत्यापित करें।

  -----------------------------------------------------------------------------
  Product                 उपलब्ध विवरण /           Image path
                          specification note      
  ----------------------- ----------------------- -----------------------------
  Psyllium Husk (Isabgol) Pharma; 99%; swelling   `/images/psyllium-husk.jpg`
                          40 ml+; mesh 40--60     

  Senna Leaves & Pods     Pharma; Sennoside A+B   `/images/senna-leaves.jpg`
                          2.5--3.5%; moisture     
                          \<10%                   

  Ashwagandha Root        Root cut / powder /     `/images/ashwagandha.jpg`
                          extract; 5%             
                          Withanolides            

  Moringa Leaf Powder     Superfood; protein      `/images/moringa.jpg`
                          27%+; moisture \<7%;    
                          100 mesh                

  Fenugreek Seeds         Pharma / Spice; 99%     `/images/fenugreek.jpg`
                          Sortex; moisture \<9%   

  Aloe Vera Gel Powder    Cosmetic / Pharma;      `/images/aloe-vera.jpg`
  200:1                   Aloin \<10 ppm;         
                          solubility 100%         
  -----------------------------------------------------------------------------

हर product page में grade, form, application, specifications, packing,
origin, quality documents, photos और enquiry के लिए fields रखें। जो जानकारी
उपलब्ध नहीं है उसे न गढ़ें।

Agriculture/Guar business में trading/sourcing का वर्णन तभी करें जब source
material इसकी पुष्टि करे। उपयोगकर्ता की परियोजना में Guar के लिए manufacturing
का दावा न करें।

------------------------------------------------------------------------

# 8. Mining Machinery & Repair Parts Division

**मुख्य route:** `/mining/`\
**Products route:** `/mining/products/`

इस सेक्टर के लिए अलग landing page और product catalogue बनाएं। मौजूदा
repository, ZIP, spreadsheets, images और product lists से वास्तविक
machine/parts data निकालें।

प्रस्तावित page structure:

-   Mining Machinery
-   Equipment
-   Repair Parts
-   Wear Parts / Replacement Parts --- केवल वास्तविक catalogue में उपलब्ध हों
-   Product categories
-   Product detail
-   Technical specifications
-   Compatible machine/model
-   Part number / SKU
-   Material / dimensions, जहाँ उपलब्ध हों
-   Product photos
-   Enquiry / quotation

**किसी मशीन, part number, brand compatibility, material grade या
dimension का अनुमान न लगाएँ।** यदि mining product data repository में नहीं
मिलता, तो page structure बनाएं और missing catalogue data को स्पष्ट रूप से
लंबित दिखाएं।

------------------------------------------------------------------------

# 9. IT & Software Systems Division

**मुख्य route:** `/it-solutions/`

IT सेक्टर के सार्वजनिक पृष्ठ पर केवल परिचय और अधिकृत परियोजनाओं का सार दिखे। इसमें
उपलब्ध परियोजनाएँ:

-   Global Trading System (GTS)
-   GTS Tools
-   Backtesting Setup
-   Invoice & Billing Software
-   अन्य स्वीकृत software projects

## 9.1 Access Control --- अनिवार्य

-   IT सेक्टर का सार्वजनिक परिचय पृष्ठ खुल सकता है।
-   निजी dashboard, source code, admin tools, trading controls और
    internal systems सार्वजनिक रूप से उपलब्ध न हों।
-   वास्तविक application entry पर authentication और authorization लागू हो।
-   केवल frontend में button छिपाना सुरक्षा नहीं है। Server/API स्तर पर भी
    access control अनिवार्य है।
-   बाकी सार्वजनिक Garuda Nexus सेक्टरों पर IT lock लागू न करें।
-   public website और private IT applications के secrets, sessions और
    data अलग रखें।
-   बिना अनुमति किसी live broker, trading account या production system से
    कनेक्शन न बनाएं।

------------------------------------------------------------------------

# 10. Group Information / About Card

Home Page के "About Garuda Nexus / Group Information" card से विस्तृत About
पृष्ठ खुले। इसमें company overview, business divisions, working model,
approved group information और verified contact details हों।

यदि कोई group phrase, logo text या religious/cultural line पहले से
approved है तो उसे उसी रूप में रखें। स्वयं से कोई नया धार्मिक, कानूनी या corporate
दावा न जोड़ें।

------------------------------------------------------------------------

# 11. Design System --- रंग, थीम और दृश्य पहचान

Garuda Nexus के लिए एक ही global design system लागू करें।

## 11.1 मुख्य रंग

  उपयोग                  रंग
  ---------------------- ---------------------
  Primary background     Deep Navy `#071A33`
  Secondary background   `#0B2545`
  Card background        `#102F52`
  Gold accent / border   `#D4AF37`
  Light gold             `#F1D77A`
  Main text              `#F5F7FA`
  Muted text             `#C5D0DC`
  Light content panel    `#F4F6F8`
  Dark body text         `#17212B`
  Success                `#238636`
  Warning                `#D29922`
  Error                  `#DA3633`

रंगों को CSS variables/design tokens में रखें। अलग-अलग पृष्ठों में मनमाने नए रंग न
जोड़ें।

## 11.2 Logo और Brand Placement

-   स्वीकृत Garuda Nexus logo ही उपयोग करें।
-   logo को distort, stretch या crop न करें।
-   Header में साफ़ और संतुलित logo placement हो।
-   Welcome page में मुख्य logo animation हो।
-   प्रत्येक page के shared layout में corner brand mark/छोटा logo रखें, लेकिन
    content को ढके नहीं।
-   mobile पर corner logo का आकार और स्थान responsive हो।
-   लोगो को हर पृष्ठ में अलग-अलग copy करने के बजाय shared Header/Layout
    component से लागू करें।

## 11.3 UI Style

-   Classic, professional, premium B2B corporate appearance।
-   Deep navy background और gold border/accent।
-   Gold का उपयोग सीमित और स्पष्ट हो; हर element को gold न करें।
-   Cards में consistent radius, spacing, image ratio और typography।
-   product pages पर readable light content panels उपयोग किए जा सकते हैं।
-   अनावश्यक gradients, चमक, flashing, excessive shadows और भारी
    animation न रखें।
-   एक ही button style, card style, form style और heading scale रखें।

## 11.4 Typography

-   स्पष्ट, पढ़ने योग्य sans-serif font stack।
-   Hindi और English दोनों सही render हों।
-   Heading hierarchy सुसंगत हो।
-   छोटे mobile screen पर body text पढ़ने योग्य रहे।
-   किसी image में लिखे text को product specification का एकमात्र स्रोत न
    बनाएं; महत्वपूर्ण जानकारी HTML text में भी उपलब्ध हो।

------------------------------------------------------------------------

# 12. Images और Media Management

-   सभी images repository में वास्तविक उपलब्ध assets से map करें।
-   product images का सही product/category से संबंध सत्यापित करें।
-   image filenames descriptive और consistent रखें।
-   duplicate images और broken image paths की जाँच करें।
-   उचित `alt` text दें।
-   responsive image sizing और lazy loading लागू करें।
-   thumbnails और detail images के लिए consistent aspect ratio रखें।
-   original assets को बिना अनुमति overwrite न करें।
-   AI-generated / reference images को वास्तविक product photograph या
    manufacturer image के रूप में प्रस्तुत न करें।
-   image न मिले तो broken icon के बजाय साफ़ placeholder और missing asset
    report दिखाएँ।

प्रस्तावित asset structure (मौजूदा project structure देखकर समायोजित करें):

``` text
public/
  images/
    brand/
    sectors/
    textile/
    solar/
    agriculture/
    mining/
    software/
```

------------------------------------------------------------------------

# 13. Data Architecture और Content Management

Product pages को reusable और data-driven बनाएं। प्रत्येक product के लिए
अलग-अलग hard-coded page बनाने के बजाय समान schema और reusable components
का उपयोग करें।

प्रस्तावित structure:

``` text
src/
  app-or-pages/
  components/
    layout/
    navigation/
    sector-cards/
    product-cards/
    product-detail/
    enquiry/
  data/
    company/
    sectors/
    textile/
    solar/
    agriculture/
    mining/
  styles/
  lib/
  types/
public/
  images/
    brand/
    sectors/
    textile/
    solar/
    agriculture/
    mining/
```

यह एक प्रस्तावित logical structure है। मौजूदा framework और repository
architecture को देखकर ही वास्तविक folder names तय करें। बिना कारण project को
दूसरे framework में migrate न करें।

## 13.1 Product Data Fields

सामान्य fields:

-   `id`
-   `slug`
-   `name`
-   `sector`
-   `category`
-   `shortDescription`
-   `fullDescription`
-   `images`
-   `specifications`
-   `applications`
-   `availability`
-   `documents`
-   `enquiryEnabled`
-   `status`
-   `sourceReference`
-   `lastVerifiedAt`

सभी fields हर product के लिए अनिवार्य नहीं हैं। उपलब्ध डेटा के अनुसार खाली/अनुपलब्ध
fields को छिपाएँ या "जानकारी अनुरोध पर" दिखाएँ।

## 13.2 Source of Truth

-   मूल product spreadsheets/JSON/CSV/technical sheets को source of truth
    मानें।
-   वेबसाइट के data records का source file और source path दर्ज करें।
-   manual copy-paste से data duplication न बनाएं।
-   product ID और slug स्थिर रखें।
-   data update होने पर सभी संबंधित pages में एकसमान जानकारी दिखे।
-   data import के समय duplicate detection और validation करें।

------------------------------------------------------------------------

# 14. Enquiry / RFQ System

हर सेक्टर और product page से enquiry की सुविधा हो।

प्रस्तावित fields:

-   Name
-   Company
-   Email
-   Phone / WhatsApp (जहाँ आवश्यक)
-   Country / Location
-   Sector
-   Product / Category
-   Quantity / Requirement
-   Message
-   Attachment (यदि सुरक्षित रूप से समर्थित हो)

नियम:

-   Form validation frontend और backend दोनों पर हो।
-   spam/rate limiting लागू करें।
-   user को स्पष्ट success/error feedback दें।
-   enquiries को सुरक्षित तरीके से अधिकृत business inbox/CRM में भेजें।
-   वास्तविक email addresses और credentials repository में hard-code न करें।
-   privacy notice और consent जहाँ लागू हो वहाँ दें।
-   test submissions को production customer records में न मिलाएँ।

------------------------------------------------------------------------

# 15. URL और Routing Blueprint

प्रस्तावित routes:

  Page                   URL
  ---------------------- ---------------------------------------
  Welcome                `/welcome/` या configured entry route
  Home                   `/`
  About                  `/about/`
  Divisions              `/divisions/`
  Textile & Yarn         `/textile-yarn/`
  Textile Products       `/textile-yarn/products/`
  Solar                  `/solar/`
  Solar Products         `/solar/products/`
  Agriculture            `/agriculture/`
  Agriculture Products   `/agriculture/products/`
  Mining                 `/mining/`
  Mining Products        `/mining/products/`
  IT Solutions           `/it-solutions/`
  Invoice & Billing      `/invoice-billing/`
  Knowledge              `/knowledge/`
  Contact                `/contact/`
  Privacy                `/privacy/`
  Terms                  `/terms/`
  Not Found              `/404`

ये प्रस्तावित paths हैं। पहले मौजूदा routes जाँचें। किसी पहले से उपयोग में मौजूद सही
route को बिना कारण न बदलें। route बदलने पर redirect, internal link update
और 404 audit करें।

------------------------------------------------------------------------

# 16. SEO, Accessibility और Performance

-   हर page का unique title और meta description हो।
-   सही heading order और semantic HTML उपयोग करें।
-   images के meaningful alt text हों।
-   keyboard navigation और visible focus states हों।
-   forms में labels और accessible error messages हों।
-   पर्याप्त color contrast हो।
-   mobile-first responsive layout हो।
-   images optimize करें और lazy load करें।
-   अनावश्यक scripts और dependencies न जोड़ें।
-   sitemap.xml और robots.txt को सही configuration दें।
-   canonical URLs और Open Graph metadata configure करें।
-   404 page और broken link checks हों।
-   page load और Core Web Vitals की जाँच करें।
-   reduced-motion preference का सम्मान करें।

------------------------------------------------------------------------

# 17. Security और Privacy

-   secrets केवल environment variables/secret manager में रखें।
-   `.env` और private keys को Git में commit न करें।
-   admin routes और APIs पर server-side authorization हो।
-   public product catalogue में private supplier/customer information न
    दिखाएँ।
-   uploads पर file type, size और access validation हो।
-   forms पर spam protection और rate limiting हो।
-   dependencies की vulnerability जाँच करें।
-   security headers और HTTPS configuration जाँचें।
-   error pages में stack traces या secrets न दिखाएँ।
-   IT systems के private access को बाकी public sectors से अलग रखें।

------------------------------------------------------------------------

# 18. Agent का अनिवार्य कार्य क्रम

## Phase 1 --- Discovery / Audit

1.  repository tree और framework पहचानें।
2.  मौजूदा routes और page flow जाँचें।
3.  उपलब्ध Welcome HTML/ZIP और logo assets जाँचें।
4.  Textile source files, yarn data और image assets जाँचें।
5.  Solar catalogue images और source data जाँचें।
6.  Agriculture product data जाँचें।
7.  Mining और company profile सामग्री खोजें।
8.  duplicate, missing, broken और conflicting data की सूची बनाएं।
9.  वर्तमान स्थिति की छोटी report दें।

## Phase 2 --- Design System

1.  color tokens और typography लागू करें।
2.  shared Header, Footer और navigation बनाएं।
3.  logo placement और corner brand mark shared layout से लागू करें।
4.  common sector card और product card बनाएं।
5.  responsive breakpoints और mobile menu लागू करें।

## Phase 3 --- Main Website

1.  Welcome Page बनाएं और वास्तविक Home route से जोड़ें।
2.  Home Page बनाएं।
3.  About Garuda Nexus page बनाएं।
4.  सभी Sector Cards जोड़ें।
5.  Contact और common enquiry व्यवस्था बनाएं।

## Phase 4 --- Sector Pages

1.  Textile & Yarn catalogue और detail pages।
2.  Solar catalogue और detail pages।
3.  Agriculture catalogue और detail pages।
4.  Mining catalogue structure और उपलब्ध product pages।
5.  IT public introduction page और secure application gate।
6.  Group/About information page।

## Phase 5 --- Data and Images

1.  मौजूदा source data import करें।
2.  product slugs/IDs स्थिर रखें।
3.  सही image mapping करें।
4.  missing data को स्पष्ट रूप से चिह्नित करें।
5.  duplicate और broken references हटाने से पहले सुरक्षित reconciliation करें;
    source files न हटाएँ।

## Phase 6 --- Testing

1.  सभी routes खोलें।
2.  Welcome → Home navigation जाँचें।
3.  हर Sector Card पर click करके सही sector खुलना जाँचें।
4.  हर category से सही products खुलना जाँचें।
5.  product images और specifications जाँचें।
6.  enquiry validation और delivery जाँचें।
7.  desktop, tablet और mobile पर जाँचें।
8.  keyboard navigation और accessibility जाँचें।
9.  console errors, broken links, 404 और missing images जाँचें।
10. security/access rules जाँचें।
11. build, lint, typecheck और automated tests चलाएँ।

## Phase 7 --- Handover

अंत में निम्न deliverables दें:

-   `README.md` --- setup और run instructions
-   `IMPLEMENTATION_REPORT.md` --- क्या लागू हुआ
-   `CONTENT_REQUIRED.md` --- कौन-सी company/product जानकारी अभी चाहिए
-   `ASSET_REPORT.md` --- images और missing assets
-   `ROUTES_REPORT.md` --- सभी routes और navigation checks
-   `TEST_REPORT.md` --- वास्तविक test commands और परिणाम
-   `SECURITY_REPORT.md` --- access-control और security status

किसी test को चलाया नहीं गया हो तो उसे PASS न लिखें। हर PASS के साथ command या
test evidence दें।

------------------------------------------------------------------------

# 19. Acceptance Criteria --- काम तभी पूरा माना जाएगा

-   [ ] Welcome Page सही तरह render होता है।
-   [ ] Welcome का Enter button वास्तविक Home Page खोलता है।
-   [ ] Home Page पर About और सभी मुख्य Sector Cards हैं।
-   [ ] About page पर केवल सत्यापित company information है।
-   [ ] हर Sector Card सही sector page खोलता है।
-   [ ] Textile में सभी उपलब्ध yarn/fabric categories हैं।
-   [ ] Yarn detail pages में उपलब्ध count, composition और technical
    details सही source से हैं।
-   [ ] Solar catalogue में उपलब्ध 01--45 items सही category में हैं।
-   [ ] Solar items 26--32 के नाम मूल source से verify किए गए हैं।
-   [ ] Agriculture के छह उपलब्ध products और उनके source-linked images सही
    हैं।
-   [ ] Mining में केवल उपलब्ध और सत्यापित catalogue data है।
-   [ ] IT public page और private application access अलग हैं।
-   [ ] सभी pages पर consistent logo, theme, header और footer हैं।
-   [ ] Desktop और mobile दोनों पर layout सही है।
-   [ ] कोई broken image, broken link या major console error नहीं है।
-   [ ] Enquiry forms सुरक्षित और validated हैं।
-   [ ] Build, lint, typecheck और automated tests के वास्तविक परिणाम दर्ज
    हैं।
-   [ ] Missing information और production blockers स्पष्ट रूप से सूचीबद्ध हैं।

**जब तक सभी आवश्यक acceptance criteria पूरे न हों, वेबसाइट को "Fully
Production Ready" न कहें।** स्थिति को `IN PROGRESS`, `READY FOR REVIEW` या
`BLOCKED` जैसे सही status से दिखाएँ।

------------------------------------------------------------------------

# 20. अंतिम निर्देश

Garuda Nexus एक Master Corporate Website है --- अलग-अलग असंबद्ध websites का
ढेर नहीं। सभी sectors एक ही मुख्य domain और brand के अंतर्गत होंगे। प्रत्येक sector
का अपना स्पष्ट landing page, category navigation और product detail system
होगा।

**सबसे महत्वपूर्ण बात:** उपयोगकर्ता द्वारा पहले से दिए गए वास्तविक product data,
images, catalogues और project files को खोजकर उपयोग करें। सामग्री को केवल सुंदर
दिखाने के लिए बदलें नहीं। जहाँ तथ्य उपलब्ध नहीं हैं, वहाँ अनुमान न लगाएँ। मौजूदा काम को
सुरक्षित रखते हुए एक व्यवस्थित, परस्पर जुड़ा हुआ, responsive और सुरक्षित सिस्टम लागू
करें।
