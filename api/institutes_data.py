"""
institutes_data.py
Comprehensive list of government and private institutes across all 29 Indian states.
Each institute includes: name, type (Government/Deemed/Private/Central), category
(Engineering/Medical/Arts/Commerce/Law/Management), ranking, entrance exams, website.
"""

INSTITUTES_DATA = {
    "Andhra Pradesh": {
        "emoji": "🌴", "color": "#059669",
        "institutes": [
            # Government / Central
            {"name": "IIT Tirupati", "type": "Central", "category": "Engineering", "established": 2015, "ranking": "IIT", "entrance_exams": ["JEE Advanced"], "website": "https://www.iittp.ac.in", "location": "Tirupati"},
            {"name": "IIM Visakhapatnam", "type": "Central", "category": "Management", "established": 2015, "ranking": "NIRF #25 (MBA)", "entrance_exams": ["CAT"], "website": "https://www.iimv.ac.in", "location": "Visakhapatnam"},
            {"name": "Andhra University", "type": "Government", "category": "Multi-disciplinary", "established": 1926, "ranking": "NIRF #101-150", "entrance_exams": ["AU PGCET", "APEAMCET"], "website": "https://www.andhrauniversity.edu.in", "location": "Visakhapatnam"},
            {"name": "Sri Venkateswara University", "type": "Government", "category": "Multi-disciplinary", "established": 1954, "ranking": "NIRF #151-200", "entrance_exams": ["APEAMCET", "APICET"], "website": "https://www.svuniversity.edu.in", "location": "Tirupati"},
            {"name": "JNTU Kakinada", "type": "Government", "category": "Engineering", "established": 1946, "ranking": "NIRF #201-250", "entrance_exams": ["APEAMCET"], "website": "https://www.jntuk.edu.in", "location": "Kakinada"},
            {"name": "RGUKT Basar (IIIT)", "type": "Government", "category": "Engineering", "established": 2008, "ranking": "Top State IIIT", "entrance_exams": ["RGUKT CET"], "website": "https://www.rgukt.in", "location": "Basar"},
            # Private
            {"name": "Koneru Lakshmaiah (KL) University", "type": "Deemed Private", "category": "Engineering", "established": 1980, "ranking": "NIRF #51-100", "entrance_exams": ["KLEEE", "JEE Main"], "website": "https://www.kluniversity.in", "location": "Vijayawada"},
            {"name": "VIT-AP University", "type": "Deemed Private", "category": "Engineering", "established": 2017, "ranking": "Top Private AP", "entrance_exams": ["VITEEE"], "website": "https://vitap.ac.in", "location": "Amaravati"},
            {"name": "GITAM University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1980, "ranking": "NIRF #101-150", "entrance_exams": ["GAT (GITAM App Test)"], "website": "https://www.gitam.edu", "location": "Visakhapatnam"},
            {"name": "SRM University AP", "type": "Private", "category": "Engineering/Management", "established": 2017, "ranking": "Top Private AP", "entrance_exams": ["SRMJEEE"], "website": "https://srmap.edu.in", "location": "Amaravati"},
            {"name": "Vignan's University", "type": "Deemed Private", "category": "Engineering", "established": 2008, "ranking": "NIRF #151-200", "entrance_exams": ["Vignan EEE", "JEE Main"], "website": "https://www.vignan.ac.in", "location": "Guntur"},
        ]
    },
    "Arunachal Pradesh": {
        "emoji": "🏔️", "color": "#7c3aed",
        "institutes": [
            {"name": "Rajiv Gandhi University", "type": "Central", "category": "Multi-disciplinary", "established": 1984, "ranking": "NIRF #201-250", "entrance_exams": ["RGU Entrance Test", "CUET PG"], "website": "https://www.rgu.ac.in", "location": "Doimukh"},
            {"name": "NERIST (NIT)", "type": "Government (NIT)", "category": "Engineering", "established": 1984, "ranking": "NIT", "entrance_exams": ["JEE Main", "NERIST Entrance"], "website": "https://www.nerist.ac.in", "location": "Nirjuli"},
            {"name": "Government Degree College Tezu", "type": "Government", "category": "Arts & Science", "established": 1976, "ranking": "State", "entrance_exams": ["State Board Merit", "CUET UG"], "website": "https://arunachal.gov.in", "location": "Tezu"},
        ]
    },
    "Assam": {
        "emoji": "🍵", "color": "#0891b2",
        "institutes": [
            {"name": "IIT Guwahati", "type": "Central", "category": "Engineering", "established": 1994, "ranking": "NIRF #7", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitg.ac.in", "location": "Guwahati"},
            {"name": "Gauhati University", "type": "Government", "category": "Multi-disciplinary", "established": 1948, "ranking": "NIRF #101-150", "entrance_exams": ["GU Admission Test", "CEE Assam"], "website": "https://www.gauhati.ac.in", "location": "Guwahati"},
            {"name": "NIT Silchar", "type": "Government (NIT)", "category": "Engineering", "established": 1967, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nits.ac.in", "location": "Silchar"},
            {"name": "Dibrugarh University", "type": "Government", "category": "Multi-disciplinary", "established": 1965, "ranking": "NIRF #151-200", "entrance_exams": ["DU Entrance", "CUET PG"], "website": "https://dibru.ac.in", "location": "Dibrugarh"},
            {"name": "Assam University", "type": "Central", "category": "Multi-disciplinary", "established": 1994, "ranking": "NIRF #151-200", "entrance_exams": ["CUET PG", "University Entrance"], "website": "https://www.aus.ac.in", "location": "Silchar"},
            {"name": "Royal Global University", "type": "Private", "category": "Multi-disciplinary", "established": 2013, "ranking": "Top Private Assam", "entrance_exams": ["Direct Merit / RGU Test"], "website": "https://rgu.ac", "location": "Guwahati"},
            {"name": "Kaziranga University", "type": "Private", "category": "Multi-disciplinary", "established": 2012, "ranking": "State Private", "entrance_exams": ["Direct Merit"], "website": "https://kazirangauniversity.in", "location": "Jorhat"},
        ]
    },
    "Bihar": {
        "emoji": "🏛️", "color": "#b45309",
        "institutes": [
            {"name": "IIT Patna", "type": "Central", "category": "Engineering", "established": 2008, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitp.ac.in", "location": "Patna"},
            {"name": "AIIMS Patna", "type": "Central", "category": "Medical", "established": 2012, "ranking": "NIRF #25 (Medical)", "entrance_exams": ["NEET UG"], "website": "https://www.aiimspatna.edu.in", "location": "Patna"},
            {"name": "IIM Bodh Gaya", "type": "Central", "category": "Management", "established": 2015, "ranking": "NIRF #51-100 (MBA)", "entrance_exams": ["CAT"], "website": "https://iimbg.ac.in", "location": "Bodh Gaya"},
            {"name": "NIT Patna", "type": "Government (NIT)", "category": "Engineering", "established": 1924, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nitp.ac.in", "location": "Patna"},
            {"name": "Patna University", "type": "Government", "category": "Multi-disciplinary", "established": 1917, "ranking": "NIRF #101-150", "entrance_exams": ["PU PAT", "CUET UG/PG"], "website": "http://www.patnauniversity.ac.in", "location": "Patna"},
            {"name": "Magadh University", "type": "Government", "category": "Multi-disciplinary", "established": 1962, "ranking": "State", "entrance_exams": ["State Board Merit"], "website": "https://magadhuniversity.ac.in", "location": "Bodh Gaya"},
            {"name": "Bihar Agricultural University", "type": "Government", "category": "Agriculture", "established": 2010, "ranking": "ICAR Accredited", "entrance_exams": ["ICAR AIEEA", "BAU Entrance"], "website": "https://bausabour.ac.in", "location": "Sabour"},
            {"name": "Amity University Patna", "type": "Private", "category": "Multi-disciplinary", "established": 2015, "ranking": "Top Private Bihar", "entrance_exams": ["Amity JEE", "Direct Merit"], "website": "https://www.amity.edu/patna", "location": "Patna"},
            {"name": "Sandip University", "type": "Private", "category": "Multi-disciplinary", "established": 2017, "ranking": "Regional Emerging", "entrance_exams": ["SUJEE"], "website": "https://www.sandipuniversity.edu.in", "location": "Madhubani"},
            {"name": "Gopal Narayan Singh University", "type": "Private", "category": "Medical/Engineering", "established": 2018, "ranking": "State Private", "entrance_exams": ["GNSU Entrance"], "website": "https://gnsu.ac.in", "location": "Jamuhar"},
        ]
    },
    "Chhattisgarh": {
        "emoji": "🌿", "color": "#65a30d",
        "institutes": [
            {"name": "IIT Bhilai", "type": "Central", "category": "Engineering", "established": 2016, "ranking": "IIT", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitbhilai.ac.in", "location": "Bhilai"},
            {"name": "AIIMS Raipur", "type": "Central", "category": "Medical", "established": 2012, "ranking": "NIRF #25 (Medical)", "entrance_exams": ["NEET UG"], "website": "https://www.aiimsraipur.edu.in", "location": "Raipur"},
            {"name": "IIM Raipur", "type": "Central", "category": "Management", "established": 2010, "ranking": "NIRF #15 (MBA)", "entrance_exams": ["CAT"], "website": "https://www.iimraipur.ac.in", "location": "Raipur"},
            {"name": "NIT Raipur", "type": "Government (NIT)", "category": "Engineering", "established": 1956, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nitrr.ac.in", "location": "Raipur"},
            {"name": "Pt. Ravishankar Shukla University", "type": "Government", "category": "Multi-disciplinary", "established": 1964, "ranking": "NIRF #151-200", "entrance_exams": ["PRSU Entrance", "CUET PG"], "website": "https://www.prsu.ac.in", "location": "Raipur"},
            {"name": "CSVTU Bhilai", "type": "Government", "category": "Engineering", "established": 2004, "ranking": "State", "entrance_exams": ["APEAMCET-equivalent CG", "JEE Main"], "website": "https://www.csvtu.ac.in", "location": "Bhilai"},
            {"name": "Kalinga University", "type": "Private", "category": "Multi-disciplinary", "established": 2008, "ranking": "Top Private CG", "entrance_exams": ["Direct Merit / KLEEE"], "website": "https://kalingauniversity.ac.in", "location": "Raipur"},
            {"name": "ITM University Raipur", "type": "Private", "category": "Multi-disciplinary", "established": 2012, "ranking": "State Leading", "entrance_exams": ["ITM Entrance"], "website": "https://itmuniversity.org", "location": "Raipur"},
            {"name": "ICFAI University Raipur", "type": "Private", "category": "Management/Law", "established": 2011, "ranking": "Regional Management", "entrance_exams": ["Direct Merit"], "website": "https://www.iuraipur.edu.in", "location": "Raipur"},
        ]
    },
    "Goa": {
        "emoji": "🏖️", "color": "#0ea5e9",
        "institutes": [
            {"name": "NIT Goa", "type": "Government (NIT)", "category": "Engineering", "established": 2010, "ranking": "NIT", "entrance_exams": ["JEE Main"], "website": "https://www.nitgoa.ac.in", "location": "Farmagudi"},
            {"name": "Goa University", "type": "Government", "category": "Multi-disciplinary", "established": 1985, "ranking": "NIRF #101-150", "entrance_exams": ["Goa CET", "CUET PG"], "website": "https://www.unigoa.ac.in", "location": "Panaji"},
            {"name": "BITS Pilani (Goa Campus)", "type": "Deemed Private", "category": "Engineering", "established": 2004, "ranking": "NIRF #25", "entrance_exams": ["BITSAT"], "website": "https://www.bits-pilani.ac.in/goa", "location": "Zuari Nagar"},
            {"name": "Don Bosco College of Engineering", "type": "Private", "category": "Engineering", "established": 1998, "ranking": "State", "entrance_exams": ["Goa CET", "JEE Main"], "website": "https://dbcegoa.ac.in", "location": "Fatorda"},
        ]
    },
    "Gujarat": {
        "emoji": "🦁", "color": "#d97706",
        "institutes": [
            {"name": "IIT Gandhinagar", "type": "Central", "category": "Engineering", "established": 2008, "ranking": "NIRF #10", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitgn.ac.in", "location": "Gandhinagar"},
            {"name": "IIM Ahmedabad", "type": "Central", "category": "Management", "established": 1961, "ranking": "NIRF MBA #1", "entrance_exams": ["CAT"], "website": "https://www.iima.ac.in", "location": "Ahmedabad"},
            {"name": "GNLU Gandhinagar", "type": "Government", "category": "Law", "established": 2003, "ranking": "NIRF Law #7", "entrance_exams": ["CLAT"], "website": "https://www.gnlu.ac.in", "location": "Gandhinagar"},
            {"name": "NIT Surat", "type": "Government (NIT)", "category": "Engineering", "established": 1961, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.svnit.ac.in", "location": "Surat"},
            {"name": "Gujarat University", "type": "Government", "category": "Multi-disciplinary", "established": 1949, "ranking": "NIRF #101-150", "entrance_exams": ["GUJCET", "CUET PG"], "website": "https://www.gujaratuniversity.ac.in", "location": "Ahmedabad"},
            {"name": "Gujarat Technological University (GTU)", "type": "Government", "category": "Engineering", "established": 2007, "ranking": "State Technical", "entrance_exams": ["GUJCET", "JEE Main"], "website": "https://www.gtu.ac.in", "location": "Ahmedabad"},
            {"name": "PDPU (PDEU)", "type": "Government", "category": "Engineering/Energy", "established": 2007, "ranking": "Top State", "entrance_exams": ["JEE Main", "PDEU Entrance"], "website": "https://www.pdpuniversity.ac.in", "location": "Gandhinagar"},
            {"name": "Nirma University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1995, "ranking": "NIRF #51-100", "entrance_exams": ["NUAT", "JEE Main"], "website": "https://www.nirmauni.ac.in", "location": "Ahmedabad"},
            {"name": "Ahmedabad University", "type": "Private", "category": "Multi-disciplinary", "established": 2009, "ranking": "Top Private Gujarat", "entrance_exams": ["AU SAT", "Direct Merit"], "website": "https://ahduni.edu.in", "location": "Ahmedabad"},
            {"name": "Marwadi University", "type": "Private", "category": "Multi-disciplinary", "established": 2016, "ranking": "State Leading", "entrance_exams": ["GUJCET", "JEE Main"], "website": "https://www.marwadiuniversity.ac.in", "location": "Rajkot"},
            {"name": "Ganpat University", "type": "Private", "category": "Multi-disciplinary", "established": 2005, "ranking": "Regional Private", "entrance_exams": ["GUJCET", "Direct Merit"], "website": "https://www.ganpatuniversity.ac.in", "location": "Mehsana"},
            {"name": "Parul University", "type": "Private", "category": "Multi-disciplinary", "established": 2015, "ranking": "State Private", "entrance_exams": ["GUJCET", "Direct Merit"], "website": "https://www.paruluniversity.ac.in", "location": "Vadodara"},
        ]
    },
    "Haryana": {
        "emoji": "🌾", "color": "#16a34a",
        "institutes": [
            {"name": "IIT Kurukshetra (NIT)", "type": "Government (NIT)", "category": "Engineering", "established": 1963, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nitkkr.ac.in", "location": "Kurukshetra"},
            {"name": "Kurukshetra University", "type": "Government", "category": "Multi-disciplinary", "established": 1956, "ranking": "NIRF #101-150", "entrance_exams": ["KUK Entrance", "CUET PG"], "website": "https://www.kuk.ac.in", "location": "Kurukshetra"},
            {"name": "MDU Rohtak", "type": "Government", "category": "Multi-disciplinary", "established": 1975, "ranking": "NIRF #101-150", "entrance_exams": ["MDU Entrance", "CUET PG"], "website": "https://www.mdurohtak.ac.in", "location": "Rohtak"},
            {"name": "Ashoka University", "type": "Private", "category": "Liberal Arts", "established": 2014, "ranking": "Top Liberal Arts India", "entrance_exams": ["Ashoka SAT/Merit"], "website": "https://www.ashoka.edu.in", "location": "Sonipat"},
            {"name": "O.P. Jindal Global University", "type": "Deemed Private", "category": "Law/Management", "established": 2009, "ranking": "NIRF Law #1", "entrance_exams": ["JGLS Entrance", "CLAT"], "website": "https://jgu.edu.in", "location": "Sonipat"},
            {"name": "BML Munjal University", "type": "Private", "category": "Multi-disciplinary", "established": 2014, "ranking": "Top Private HR", "entrance_exams": ["SAT", "ACT", "BMU Entrance"], "website": "https://www.bmu.edu.in", "location": "Gurgaon"},
            {"name": "Manav Rachna University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 2014, "ranking": "NIRF #151-200", "entrance_exams": ["MRIU Entrance", "JEE Main"], "website": "https://manavrachna.edu.in", "location": "Faridabad"},
            {"name": "GD Goenka University", "type": "Private", "category": "Multi-disciplinary", "established": 2013, "ranking": "Regional Private", "entrance_exams": ["GATA (Goenka App Test)"], "website": "https://www.gdgoenkauniversity.com", "location": "Gurgaon"},
        ]
    },
    "Himachal Pradesh": {
        "emoji": "⛰️", "color": "#6366f1",
        "institutes": [
            {"name": "IIT Mandi", "type": "Central", "category": "Engineering", "established": 2009, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitmandi.ac.in", "location": "Mandi"},
            {"name": "NIT Hamirpur", "type": "Government (NIT)", "category": "Engineering", "established": 1986, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nith.ac.in", "location": "Hamirpur"},
            {"name": "HPU Shimla", "type": "Government", "category": "Multi-disciplinary", "established": 1970, "ranking": "NIRF #101-150", "entrance_exams": ["HPCAT", "CUET PG"], "website": "https://www.hpuniv.ac.in", "location": "Shimla"},
            {"name": "Shoolini University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 2009, "ranking": "Top Private HP", "entrance_exams": ["Direct Merit", "JEE Main"], "website": "https://shooliniuniversity.com", "location": "Solan"},
        ]
    },
    "Jharkhand": {
        "emoji": "⛏️", "color": "#9333ea",
        "institutes": [
            {"name": "IIT (ISM) Dhanbad", "type": "Central", "category": "Engineering/Mining", "established": 1926, "ranking": "NIRF #15", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitism.ac.in", "location": "Dhanbad"},
            {"name": "IIM Ranchi", "type": "Central", "category": "Management", "established": 2010, "ranking": "NIRF #15 (MBA)", "entrance_exams": ["CAT"], "website": "https://www.iimranchi.ac.in", "location": "Ranchi"},
            {"name": "NIT Jamshedpur", "type": "Government (NIT)", "category": "Engineering", "established": 1960, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nitjsr.ac.in", "location": "Jamshedpur"},
            {"name": "Ranchi University", "type": "Government", "category": "Multi-disciplinary", "established": 1960, "ranking": "State", "entrance_exams": ["JCECE", "CUET PG"], "website": "https://www.ranchiuniversity.ac.in", "location": "Ranchi"},
            {"name": "XLRI Jamshedpur", "type": "Deemed Private", "category": "Management", "established": 1949, "ranking": "NIRF MBA #5", "entrance_exams": ["XAT"], "website": "https://www.xlri.edu", "location": "Jamshedpur"},
            {"name": "Vinoba Bhave University", "type": "Government", "category": "Multi-disciplinary", "established": 1992, "ranking": "State", "entrance_exams": ["State Merit", "CUET"], "website": "https://vbu.ac.in", "location": "Hazaribagh"},
        ]
    },
    "Karnataka": {
        "emoji": "🏯", "color": "#dc2626",
        "institutes": [
            {"name": "IISc Bangalore", "type": "Central", "category": "Science/Engineering", "established": 1909, "ranking": "NIRF #1 (Research)", "entrance_exams": ["JEE Advanced", "GATE", "KVPY", "JAM"], "website": "https://www.iisc.ac.in", "location": "Bangalore"},
            {"name": "IIM Bangalore", "type": "Central", "category": "Management", "established": 1973, "ranking": "NIRF MBA #2", "entrance_exams": ["CAT"], "website": "https://www.iimb.ac.in", "location": "Bangalore"},
            {"name": "NLSIU Bengaluru", "type": "Government", "category": "Law", "established": 1987, "ranking": "NIRF Law #1", "entrance_exams": ["CLAT"], "website": "https://www.nls.ac.in", "location": "Bangalore"},
            {"name": "IIT Dharwad", "type": "Central", "category": "Engineering", "established": 2016, "ranking": "IIT", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitdh.ac.in", "location": "Dharwad"},
            {"name": "NIT Karnataka (NITK)", "type": "Government (NIT)", "category": "Engineering", "established": 1960, "ranking": "NIRF #25", "entrance_exams": ["JEE Main"], "website": "https://www.nitk.ac.in", "location": "Surathkal"},
            {"name": "Bangalore University", "type": "Government", "category": "Multi-disciplinary", "established": 1964, "ranking": "NIRF #101-150", "entrance_exams": ["PGCET Karnataka", "CUET PG"], "website": "https://www.bangaloreuniversity.ac.in", "location": "Bangalore"},
            {"name": "VTU (Visvesvaraya Tech University)", "type": "Government", "category": "Engineering", "established": 1998, "ranking": "State Technical", "entrance_exams": ["KCET", "JEE Main"], "website": "https://vtu.ac.in", "location": "Belagavi"},
            {"name": "Manipal Academy of Higher Education", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1993, "ranking": "NIRF #7 (Private)", "entrance_exams": ["MET", "MAHE Online Test"], "website": "https://manipal.edu", "location": "Manipal"},
            {"name": "PES University", "type": "Deemed Private", "category": "Engineering", "established": 1972, "ranking": "Top Bangalore Private", "entrance_exams": ["PESSAT", "JEE Main"], "website": "https://www.pes.edu", "location": "Bangalore"},
            {"name": "Christ University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1969, "ranking": "NIRF #51-100", "entrance_exams": ["Christ Entrance Test (CUET)", "Direct Merit"], "website": "https://christuniversity.in", "location": "Bangalore"},
            {"name": "Alliance University", "type": "Private", "category": "Management/Law/Engineering", "established": 2010, "ranking": "NIRF #25 (Law)", "entrance_exams": ["AUSAT", "AMAT", "CLAT"], "website": "https://www.alliance.edu.in", "location": "Bangalore"},
            {"name": "Jain University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1990, "ranking": "NIRF #51-100", "entrance_exams": ["JET (Jain Entrance)"], "website": "https://www.jainuniversity.ac.in", "location": "Bangalore"},
            {"name": "REVA University", "type": "Private", "category": "Multi-disciplinary", "established": 2012, "ranking": "Top Emerging Bangalore", "entrance_exams": ["REVA EET"], "website": "https://reva.edu.in", "location": "Bangalore"},
        ]
    },
    "Kerala": {
        "emoji": "🌴", "color": "#15803d",
        "institutes": [
            {"name": "IIT Palakkad", "type": "Central", "category": "Engineering", "established": 2015, "ranking": "IIT", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitpkd.ac.in", "location": "Palakkad"},
            {"name": "NIT Calicut", "type": "Government (NIT)", "category": "Engineering", "established": 1961, "ranking": "NIRF #25", "entrance_exams": ["JEE Main"], "website": "https://www.nitc.ac.in", "location": "Kozhikode"},
            {"name": "IIM Kozhikode", "type": "Central", "category": "Management", "established": 1996, "ranking": "NIRF MBA #3", "entrance_exams": ["CAT"], "website": "https://www.iimk.ac.in", "location": "Kozhikode"},
            {"name": "CUSAT (Cochin University)", "type": "Government", "category": "Science/Engineering", "established": 1971, "ranking": "NIRF #51-100", "entrance_exams": ["CUSAT CAT"], "website": "https://www.cusat.ac.in", "location": "Kochi"},
            {"name": "University of Kerala", "type": "Government", "category": "Multi-disciplinary", "established": 1937, "ranking": "NIRF #101-150", "entrance_exams": ["CET Kerala", "CUET PG"], "website": "https://www.keralauniversity.ac.in", "location": "Thiruvananthapuram"},
            {"name": "Calicut University", "type": "Government", "category": "Multi-disciplinary", "established": 1968, "ranking": "NIRF #101-150", "entrance_exams": ["Calicut Entrance", "CUET PG"], "website": "https://www.uoc.ac.in", "location": "Malappuram"},
            {"name": "Amrita Vishwa Vidyapeetham", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 2003, "ranking": "NIRF #8", "entrance_exams": ["AEEE", "JEE Main"], "website": "https://www.amrita.edu", "location": "Coimbatore/Kochi"},
        ]
    },
    "Madhya Pradesh": {
        "emoji": "🐯", "color": "#f59e0b",
        "institutes": [
            {"name": "IIT Indore", "type": "Central", "category": "Engineering", "established": 2009, "ranking": "NIRF #25", "entrance_exams": ["JEE Advanced"], "website": "https://www.iiti.ac.in", "location": "Indore"},
            {"name": "AIIMS Bhopal", "type": "Central", "category": "Medical", "established": 2012, "ranking": "NIRF #15 (Medical)", "entrance_exams": ["NEET UG"], "website": "https://www.aiimsbhopal.edu.in", "location": "Bhopal"},
            {"name": "IIM Indore", "type": "Central", "category": "Management", "established": 1996, "ranking": "NIRF MBA #5", "entrance_exams": ["CAT", "GMAT"], "website": "https://www.iimidr.ac.in", "location": "Indore"},
            {"name": "MANIT Bhopal", "type": "Government (NIT)", "category": "Engineering", "established": 1960, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.manit.ac.in", "location": "Bhopal"},
            {"name": "VIT Bhopal University", "type": "Private", "category": "Engineering", "established": 2017, "ranking": "Top Private MP", "entrance_exams": ["VITEEE"], "website": "https://vitbhopal.ac.in", "location": "Bhopal"},
            {"name": "Amity University Gwalior", "type": "Private", "category": "Multi-disciplinary", "established": 2010, "ranking": "NIRF #151-200", "entrance_exams": ["Amity JEE"], "website": "https://www.amity.edu/gwalior", "location": "Gwalior"},
            {"name": "SRM University Gwalior", "type": "Private", "category": "Multi-disciplinary", "established": 2014, "ranking": "State Private", "entrance_exams": ["SRMJEEE"], "website": "https://www.srmist.edu.in", "location": "Gwalior"},
        ]
    },
    "Maharashtra": {
        "emoji": "🏙️", "color": "#f97316",
        "institutes": [
            {"name": "IIT Bombay", "type": "Central", "category": "Engineering", "established": 1958, "ranking": "NIRF #3", "entrance_exams": ["JEE Advanced", "GATE"], "website": "https://www.iitb.ac.in", "location": "Mumbai"},
            {"name": "TISS Mumbai", "type": "Deemed Public", "category": "Social Sciences", "established": 1936, "ranking": "NIRF #10 (Research)", "entrance_exams": ["TISSNET", "CUET PG"], "website": "https://www.tiss.edu", "location": "Mumbai"},
            {"name": "IIM Mumbai (NITIE)", "type": "Central", "category": "Management", "established": 1963, "ranking": "NIRF #7 (MBA)", "entrance_exams": ["CAT"], "website": "https://iimmumbai.ac.in", "location": "Mumbai"},
            {"name": "AIIMS Nagpur", "type": "Central", "category": "Medical", "established": 2018, "ranking": "NIRF #51-100", "entrance_exams": ["NEET UG"], "website": "https://aiimsnagpur.edu.in", "location": "Nagpur"},
            {"name": "University of Mumbai", "type": "Government", "category": "Multi-disciplinary", "established": 1857, "ranking": "NIRF #101-150", "entrance_exams": ["MHT-CET", "MH-SET"], "website": "https://mu.ac.in", "location": "Mumbai"},
            {"name": "Pune University (SPPU)", "type": "Government", "category": "Multi-disciplinary", "established": 1949, "ranking": "NIRF #51-100", "entrance_exams": ["MHT-CET", "CUET PG"], "website": "https://www.unipune.ac.in", "location": "Pune"},
            {"name": "COEP Technological University", "type": "Government", "category": "Engineering", "established": 1854, "ranking": "NIRF #51-100", "entrance_exams": ["MHT-CET", "JEE Main"], "website": "https://www.coep.org.in", "location": "Pune"},
            {"name": "VJTI Mumbai", "type": "Government", "category": "Engineering", "established": 1887, "ranking": "State Top", "entrance_exams": ["MHT-CET", "JEE Main"], "website": "https://vjti.ac.in", "location": "Mumbai"},
            {"name": "ICT Mumbai (UDCT)", "type": "Government (Deemed)", "category": "Chemical/Technology", "established": 1933, "ranking": "NIRF #25", "entrance_exams": ["ICT Mumbai CET"], "website": "https://www.ictmumbai.edu.in", "location": "Mumbai"},
            {"name": "NIT Nagpur (VNIT)", "type": "Government (NIT)", "category": "Engineering", "established": 1960, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://vnit.ac.in", "location": "Nagpur"},
            {"name": "Symbiosis International University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 2002, "ranking": "NIRF #51-100", "entrance_exams": ["SNAP", "SET"], "website": "https://siu.edu.in", "location": "Pune"},
            {"name": "MIT World Peace University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 2017, "ranking": "Top Private MH", "entrance_exams": ["MHT-CET", "Direct Merit"], "website": "https://mitwpu.edu.in", "location": "Pune"},
            {"name": "NMIMS University", "type": "Deemed Private", "category": "Management/Engineering", "established": 1985, "ranking": "NIRF #51-100", "entrance_exams": ["NMAT", "NPAT"], "website": "https://www.nmims.edu", "location": "Mumbai"},
            {"name": "FLAME University", "type": "Private", "category": "Liberal Arts", "established": 2015, "ranking": "Top Liberal Arts India", "entrance_exams": ["FEAT", "SAT", "ACT"], "website": "https://www.flame.edu.in", "location": "Pune"},
            {"name": "D.Y. Patil University", "type": "Deemed Private", "category": "Medical/Engineering", "established": 2002, "ranking": "NIRF #51-100", "entrance_exams": ["NEET UG", "MHT-CET"], "website": "https://dypatil.edu", "location": "Navi Mumbai"},
            {"name": "Bharati Vidyapeeth University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1964, "ranking": "NIRF #101-150", "entrance_exams": ["BVP CET"], "website": "https://bvuniversity.edu.in", "location": "Pune"},
        ]
    },
    "Manipur": {
        "emoji": "🎭", "color": "#8b5cf6",
        "institutes": [
            {"name": "Manipur University", "type": "Central", "category": "Multi-disciplinary", "established": 1980, "ranking": "NIRF #151-200", "entrance_exams": ["Manipur CET", "CUET PG"], "website": "https://www.manipuruniv.ac.in", "location": "Imphal"},
            {"name": "NIT Manipur", "type": "Government (NIT)", "category": "Engineering", "established": 2010, "ranking": "NIT", "entrance_exams": ["JEE Main"], "website": "https://www.nitmanipur.ac.in", "location": "Langol"},
            {"name": "RIMS Imphal (Medical)", "type": "Government", "category": "Medical", "established": 1972, "ranking": "State Medical", "entrance_exams": ["NEET UG"], "website": "https://rimims.ac.in", "location": "Imphal"},
        ]
    },
    "Meghalaya": {
        "emoji": "🌧️", "color": "#0369a1",
        "institutes": [
            {"name": "North Eastern Hill University (NEHU)", "type": "Central", "category": "Multi-disciplinary", "established": 1973, "ranking": "NIRF #151-200", "entrance_exams": ["NEHU Entrance", "CUET PG"], "website": "https://www.nehu.ac.in", "location": "Shillong"},
            {"name": "NIT Meghalaya", "type": "Government (NIT)", "category": "Engineering", "established": 2010, "ranking": "NIT", "entrance_exams": ["JEE Main"], "website": "https://www.nitm.ac.in", "location": "Shillong"},
            {"name": "IIM Shillong", "type": "Central", "category": "Management", "established": 2007, "ranking": "NIRF MBA #25", "entrance_exams": ["CAT"], "website": "https://www.iimshillong.ac.in", "location": "Shillong"},
            {"name": "Martin Luther Christian University", "type": "Private", "category": "Multi-disciplinary", "established": 2005, "ranking": "State Private", "entrance_exams": ["MLCU Entrance"], "website": "https://www.mlcuniv.in", "location": "Shillong"},
        ]
    },
    "Mizoram": {
        "emoji": "🏔️", "color": "#0f766e",
        "institutes": [
            {"name": "Mizoram University", "type": "Central", "category": "Multi-disciplinary", "established": 2001, "ranking": "NIRF #201-250", "entrance_exams": ["MZU Entrance", "CUET PG"], "website": "https://www.mzu.edu.in", "location": "Aizawl"},
            {"name": "NIT Mizoram", "type": "Government (NIT)", "category": "Engineering", "established": 2010, "ranking": "NIT", "entrance_exams": ["JEE Main"], "website": "https://www.nitmz.ac.in", "location": "Aizawl"},
        ]
    },
    "Nagaland": {
        "emoji": "🦅", "color": "#1d4ed8",
        "institutes": [
            {"name": "Nagaland University", "type": "Central", "category": "Multi-disciplinary", "established": 1994, "ranking": "State", "entrance_exams": ["NU Entrance", "CUET PG"], "website": "https://www.nagalanduniversity.ac.in", "location": "Lumami"},
            {"name": "NIT Nagaland", "type": "Government (NIT)", "category": "Engineering", "established": 2010, "ranking": "NIT", "entrance_exams": ["JEE Main"], "website": "https://www.nitnagaland.ac.in", "location": "Dimapur"},
            {"name": "NIAS (Nagaland Inst. of Advanced Studies)", "type": "Government", "category": "Arts & Science", "established": 2003, "ranking": "State", "entrance_exams": ["State Merit"], "website": "https://nagaland.gov.in", "location": "Zunheboto"},
        ]
    },
    "Odisha": {
        "emoji": "🏛️", "color": "#b91c1c",
        "institutes": [
            {"name": "IIT Bhubaneswar", "type": "Central", "category": "Engineering", "established": 2008, "ranking": "NIRF #25", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitbbs.ac.in", "location": "Bhubaneswar"},
            {"name": "AIIMS Bhubaneswar", "type": "Central", "category": "Medical", "established": 2012, "ranking": "NIRF #15 (Medical)", "entrance_exams": ["NEET UG"], "website": "https://aiimsbhubaneswar.nic.in", "location": "Bhubaneswar"},
            {"name": "NIT Rourkela", "type": "Government (NIT)", "category": "Engineering", "established": 1961, "ranking": "NIRF #15", "entrance_exams": ["JEE Main"], "website": "https://www.nitrkl.ac.in", "location": "Rourkela"},
            {"name": "NLUO Cuttack", "type": "Government", "category": "Law", "established": 2009, "ranking": "NIRF Law #6", "entrance_exams": ["CLAT"], "website": "https://www.nluo.ac.in", "location": "Cuttack"},
            {"name": "IIM Sambalpur", "type": "Central", "category": "Management", "established": 2015, "ranking": "NIRF #51-100 (MBA)", "entrance_exams": ["CAT"], "website": "https://www.iimsambalpur.ac.in", "location": "Sambalpur"},
            {"name": "Utkal University", "type": "Government", "category": "Multi-disciplinary", "established": 1943, "ranking": "NIRF #101-150", "entrance_exams": ["Odisha OJEE", "CUET PG"], "website": "https://www.utkaluniversity.ac.in", "location": "Bhubaneswar"},
            {"name": "SOA University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1996, "ranking": "NIRF #51-100", "entrance_exams": ["SAAT", "NEET", "JEE Main"], "website": "https://soauniversity.ac.in", "location": "Bhubaneswar"},
            {"name": "KIIT University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1992, "ranking": "NIRF #51-100", "entrance_exams": ["KIITEE"], "website": "https://kiit.ac.in", "location": "Bhubaneswar"},
            {"name": "C.V. Raman Global University", "type": "Private", "category": "Engineering", "established": 1997, "ranking": "NIRF #101-150", "entrance_exams": ["CGET"], "website": "https://cgu-odisha.ac.in", "location": "Bhubaneswar"},
            {"name": "Centurion University", "type": "Private", "category": "Multi-disciplinary", "established": 2010, "ranking": "Top Private Odisha", "entrance_exams": ["CUEE"], "website": "https://cutm.ac.in", "location": "Bhubaneswar"},
        ]
    },
    "Punjab": {
        "emoji": "🌾", "color": "#ca8a04",
        "institutes": [
            {"name": "IIT Ropar", "type": "Central", "category": "Engineering", "established": 2008, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitrpr.ac.in", "location": "Rupnagar"},
            {"name": "IIM Amritsar", "type": "Central", "category": "Management", "established": 2015, "ranking": "NIRF #51-100 (MBA)", "entrance_exams": ["CAT"], "website": "https://iimamritsar.ac.in", "location": "Amritsar"},
            {"name": "NIT Jalandhar", "type": "Government (NIT)", "category": "Engineering", "established": 1987, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nitj.ac.in", "location": "Jalandhar"},
            {"name": "AIIMS Bathinda", "type": "Central", "category": "Medical", "established": 2019, "ranking": "State Medical Hub", "entrance_exams": ["NEET UG"], "website": "https://aiimsbathinda.edu.in", "location": "Bathinda"},
            {"name": "Panjab University", "type": "Government", "category": "Multi-disciplinary", "established": 1882, "ranking": "NIRF #51-100", "entrance_exams": ["PUCAT", "CUET PG"], "website": "https://puchd.ac.in", "location": "Chandigarh"},
            {"name": "Guru Nanak Dev University", "type": "Government", "category": "Multi-disciplinary", "established": 1969, "ranking": "NIRF #101-150", "entrance_exams": ["GNDU Entrance", "CUET PG"], "website": "https://www.gndu.ac.in", "location": "Amritsar"},
            {"name": "Thapar Institute", "type": "Deemed Private", "category": "Engineering", "established": 1956, "ranking": "NIRF #25", "entrance_exams": ["JEE Main"], "website": "https://www.thapar.edu", "location": "Patiala"},
            {"name": "Chandigarh University", "type": "Private", "category": "Multi-disciplinary", "established": 2012, "ranking": "NIRF #1 (Private)", "entrance_exams": ["CUCET"], "website": "https://www.cuchd.in", "location": "Mohali"},
            {"name": "Chitkara University", "type": "Private", "category": "Multi-disciplinary", "established": 2010, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main", "CHITKARA Test"], "website": "https://www.chitkara.edu.in", "location": "Rajpura"},
            {"name": "Lovely Professional University", "type": "Private", "category": "Multi-disciplinary", "established": 2005, "ranking": "NIRF #38 (Overall)", "entrance_exams": ["LPUNEST", "JEE Main"], "website": "https://www.lpu.in", "location": "Jalandhar"},
        ]
    },
    "Rajasthan": {
        "emoji": "🏜️", "color": "#ea580c",
        "institutes": [
            {"name": "IIT Jodhpur", "type": "Central", "category": "Engineering", "established": 2008, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitj.ac.in", "location": "Jodhpur"},
            {"name": "IIM Udaipur", "type": "Central", "category": "Management", "established": 2011, "ranking": "NIRF #15 (MBA)", "entrance_exams": ["CAT"], "website": "https://www.iimu.ac.in", "location": "Udaipur"},
            {"name": "AIIMS Jodhpur", "type": "Central", "category": "Medical", "established": 2012, "ranking": "NIRF #13 (Medical)", "entrance_exams": ["NEET UG"], "website": "https://www.aiimsjodhpur.edu.in", "location": "Jodhpur"},
            {"name": "MNIT Jaipur", "type": "Government (NIT)", "category": "Engineering", "established": 1963, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.mnit.ac.in", "location": "Jaipur"},
            {"name": "NLU Jodhpur", "type": "Government", "category": "Law", "established": 1999, "ranking": "NIRF Law #5", "entrance_exams": ["CLAT"], "website": "http://www.nlujodhpur.ac.in", "location": "Jodhpur"},
            {"name": "University of Rajasthan", "type": "Government", "category": "Multi-disciplinary", "established": 1947, "ranking": "NIRF #101-150", "entrance_exams": ["RU Entrance", "CUET PG"], "website": "https://www.uniraj.ac.in", "location": "Jaipur"},
            {"name": "BITS Pilani (Main Campus)", "type": "Deemed Private", "category": "Engineering", "established": 1964, "ranking": "NIRF #25", "entrance_exams": ["BITSAT"], "website": "https://www.bits-pilani.ac.in", "location": "Pilani"},
            {"name": "Banasthali Vidyapith", "type": "Deemed Private", "category": "Women's University", "established": 1935, "ranking": "NIRF Top Women's", "entrance_exams": ["BVP Entrance", "Direct Merit"], "website": "https://www.banasthali.org", "location": "Banasthali"},
            {"name": "NIIT University", "type": "Private", "category": "Engineering/Management", "established": 2009, "ranking": "Top Private Rajasthan", "entrance_exams": ["NUAT"], "website": "https://www.niituniversity.in", "location": "Neemrana"},
            {"name": "Jaipur National University", "type": "Private", "category": "Multi-disciplinary", "established": 2007, "ranking": "Regional Top", "entrance_exams": ["JNU Combined Entrance"], "website": "https://www.jnujaipur.ac.in", "location": "Jaipur"},
            {"name": "Poornima University", "type": "Private", "category": "Engineering/Management", "established": 2012, "ranking": "State", "entrance_exams": ["JEE Main", "Direct Merit"], "website": "https://poornima.edu.in", "location": "Jaipur"},
            {"name": "JECRC University", "type": "Private", "category": "Engineering/Management", "established": 2012, "ranking": "Regional Private", "entrance_exams": ["JECRC Entrance", "Direct Merit"], "website": "https://jecrcuniversity.edu.in", "location": "Jaipur"},
        ]
    },
    "Sikkim": {
        "emoji": "🌸", "color": "#9d174d",
        "institutes": [
            {"name": "Sikkim University", "type": "Central", "category": "Multi-disciplinary", "established": 2007, "ranking": "State", "entrance_exams": ["SU Entrance", "CUET PG"], "website": "https://cus.ac.in", "location": "Gangtok"},
            {"name": "NIT Sikkim", "type": "Government (NIT)", "category": "Engineering", "established": 2010, "ranking": "NIT", "entrance_exams": ["JEE Main"], "website": "https://www.nitsikkim.ac.in", "location": "Ravangla"},
            {"name": "Sikkim Manipal University", "type": "Deemed Private", "category": "Medical/Engineering", "established": 1995, "ranking": "Top Private Sikkim", "entrance_exams": ["NEET", "JEE Main", "SMU Entrance"], "website": "https://smude.edu.in", "location": "Gangtok"},
        ]
    },
    "Tamil Nadu": {
        "emoji": "🕌", "color": "#be185d",
        "institutes": [
            {"name": "IIT Madras", "type": "Central", "category": "Engineering", "established": 1959, "ranking": "NIRF #1", "entrance_exams": ["JEE Advanced", "GATE", "JAM"], "website": "https://www.iitm.ac.in", "location": "Chennai"},
            {"name": "NIFT Chennai", "type": "Central", "category": "Design/Arts", "established": 1986, "ranking": "Top Design Hub", "entrance_exams": ["NIFT Entrance"], "website": "https://nift.ac.in/chennai", "location": "Chennai"},
            {"name": "Anna University", "type": "Government", "category": "Engineering", "established": 1978, "ranking": "NIRF #10", "entrance_exams": ["TNEA", "TANCET"], "website": "https://www.annauniv.edu", "location": "Chennai"},
            {"name": "University of Madras", "type": "Government", "category": "Multi-disciplinary", "established": 1857, "ranking": "NIRF #51-100", "entrance_exams": ["Madras Univ Entrance", "CUET PG"], "website": "https://www.unom.ac.in", "location": "Chennai"},
            {"name": "NIT Trichy", "type": "Government (NIT)", "category": "Engineering", "established": 1964, "ranking": "NIRF #10", "entrance_exams": ["JEE Main"], "website": "https://www.nitt.edu", "location": "Tiruchirappalli"},
            {"name": "VIT Vellore", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1984, "ranking": "NIRF #15", "entrance_exams": ["VITEEE"], "website": "https://vit.ac.in", "location": "Vellore"},
            {"name": "SASTRA University", "type": "Deemed Private", "category": "Engineering", "established": 1984, "ranking": "NIRF #51-100", "entrance_exams": ["SASTRA entrance", "JEE Main"], "website": "https://www.sastra.edu", "location": "Thanjavur"},
            {"name": "SRM Institute of Science & Technology", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1985, "ranking": "NIRF #18 (Universities)", "entrance_exams": ["SRMJEEE"], "website": "https://www.srmist.edu.in", "location": "Chennai"},
            {"name": "PSG College of Technology", "type": "Private (Aided)", "category": "Engineering", "established": 1951, "ranking": "NIRF #51-100", "entrance_exams": ["TNEA"], "website": "https://www.psgtech.edu", "location": "Coimbatore"},
            {"name": "Sathyabama Institute of Science and Tech", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1987, "ranking": "NIRF #51-100", "entrance_exams": ["SAEEE"], "website": "https://www.sathyabama.ac.in", "location": "Chennai"},
            {"name": "Kalasalingam Academy", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 1984, "ranking": "NIRF #51-100", "entrance_exams": ["KUEEE"], "website": "https://kalasalingam.ac.in", "location": "Krishnankoil"},
            {"name": "Hindustan Institute of Tech & Science", "type": "Deemed Private", "category": "Engineering/Aviation", "established": 1985, "ranking": "Top Private TN", "entrance_exams": ["HITSEEE"], "website": "https://hindustanuniv.ac.in", "location": "Chennai"},
        ]
    },
    "Telangana": {
        "emoji": "💎", "color": "#0e7490",
        "institutes": [
            {"name": "IIT Hyderabad", "type": "Central", "category": "Engineering", "established": 2008, "ranking": "NIRF #10", "entrance_exams": ["JEE Advanced", "GATE"], "website": "https://www.iith.ac.in", "location": "Hyderabad"},
            {"name": "University of Hyderabad", "type": "Central", "category": "Multi-disciplinary", "established": 1974, "ranking": "NIRF #10", "entrance_exams": ["CUET PG", "UoH Entrance"], "website": "https://uohyd.ac.in", "location": "Hyderabad"},
            {"name": "NIT Warangal", "type": "Government (NIT)", "category": "Engineering", "established": 1959, "ranking": "NIRF #25", "entrance_exams": ["JEE Main"], "website": "https://www.nitw.ac.in", "location": "Warangal"},
            {"name": "Osmania University", "type": "Government", "category": "Multi-disciplinary", "established": 1918, "ranking": "NIRF #101-150", "entrance_exams": ["TS EAMCET", "TSPGECET"], "website": "https://www.osmania.ac.in", "location": "Hyderabad"},
            {"name": "JNTU Hyderabad", "type": "Government", "category": "Engineering", "established": 1972, "ranking": "State Technical", "entrance_exams": ["TS EAMCET"], "website": "https://www.jntuh.ac.in", "location": "Hyderabad"},
            {"name": "BITS Pilani Hyderabad", "type": "Deemed Private", "category": "Engineering", "established": 2008, "ranking": "NIRF #25", "entrance_exams": ["BITSAT"], "website": "https://www.bits-pilani.ac.in/hyderabad", "location": "Hyderabad"},
            {"name": "IIIT Hyderabad", "type": "Deemed Private (IIIT)", "category": "Engineering/CS", "established": 1998, "ranking": "NIRF #10 (CS)", "entrance_exams": ["UGEE", "GATE", "JEE Main"], "website": "https://www.iiit.ac.in", "location": "Hyderabad"},
            {"name": "ICFAI Foundation for Higher Education", "type": "Deemed Private", "category": "Management/Law", "established": 1984, "ranking": "NIRF MBA #25", "entrance_exams": ["IBSAT"], "website": "https://www.ifheindia.org", "location": "Hyderabad"},
            {"name": "CBIT Hyderabad", "type": "Private (Aided)", "category": "Engineering", "established": 1979, "ranking": "Top State Private", "entrance_exams": ["TS EAMCET", "JEE Main"], "website": "https://www.cbit.ac.in", "location": "Hyderabad"},
            {"name": "Vasavi College of Engineering", "type": "Private", "category": "Engineering", "established": 1981, "ranking": "Regional Premium", "entrance_exams": ["TS EAMCET"], "website": "https://vce.ac.in", "location": "Hyderabad"},
        ]
    },
    "Tripura": {
        "emoji": "🌿", "color": "#115e59",
        "institutes": [
            {"name": "Tripura University", "type": "Central", "category": "Multi-disciplinary", "established": 1987, "ranking": "State", "entrance_exams": ["TU Entrance", "CUET PG"], "website": "https://www.tripurauniv.ac.in", "location": "Agartala"},
            {"name": "NIT Agartala", "type": "Government (NIT)", "category": "Engineering", "established": 1965, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nita.ac.in", "location": "Agartala"},
        ]
    },
    "Uttar Pradesh": {
        "emoji": "🕌", "color": "#92400e",
        "institutes": [
            {"name": "IIT Kanpur", "type": "Central", "category": "Engineering", "established": 1959, "ranking": "NIRF #4", "entrance_exams": ["JEE Advanced", "GATE"], "website": "https://www.iitk.ac.in", "location": "Kanpur"},
            {"name": "IIM Lucknow", "type": "Central", "category": "Management", "established": 1984, "ranking": "NIRF MBA #5", "entrance_exams": ["CAT"], "website": "https://www.iiml.ac.in", "location": "Lucknow"},
            {"name": "IIT BHU Varanasi", "type": "Central", "category": "Engineering", "established": 1919, "ranking": "NIRF #10", "entrance_exams": ["JEE Advanced"], "website": "https://www.iitbhu.ac.in", "location": "Varanasi"},
            {"name": "BHU (Banaras Hindu University)", "type": "Central", "category": "Multi-disciplinary", "established": 1916, "ranking": "NIRF #10", "entrance_exams": ["CUET UG/PG", "BHU RET"], "website": "https://www.bhu.ac.in", "location": "Varanasi"},
            {"name": "AMU Aligarh", "type": "Central", "category": "Multi-disciplinary", "established": 1875, "ranking": "NIRF #10", "entrance_exams": ["AMU Entrance Test"], "website": "https://www.amu.ac.in", "location": "Aligarh"},
            {"name": "NLUA Lucknow (RMLNLU)", "type": "Government", "category": "Law", "established": 2005, "ranking": "NIRF Law #10", "entrance_exams": ["CLAT"], "website": "https://www.rmlnlu.ac.in", "location": "Lucknow"},
            {"name": "MNNIT Allahabad", "type": "Government (NIT)", "category": "Engineering", "established": 1961, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.mnnit.ac.in", "location": "Prayagraj"},
            {"name": "AKTU Lucknow", "type": "Government", "category": "Engineering", "established": 2000, "ranking": "State Technical", "entrance_exams": ["UPCET / JEE Main"], "website": "https://aktu.ac.in", "location": "Lucknow"},
            {"name": "IIM Lucknow", "type": "Central", "category": "Management", "established": 1984, "ranking": "NIRF MBA #5", "entrance_exams": ["CAT"], "website": "https://www.iiml.ac.in", "location": "Lucknow"},
            {"name": "Amity University Noida", "type": "Private", "category": "Multi-disciplinary", "established": 2005, "ranking": "NIRF #35 (Universities)", "entrance_exams": ["Amity JEE", "Direct Merit"], "website": "https://www.amity.edu", "location": "Noida"},
            {"name": "Shiv Nadar University", "type": "Deemed Private", "category": "Multi-disciplinary", "established": 2011, "ranking": "NIRF #51-100", "entrance_exams": ["SNUSAT", "JEE Main"], "website": "https://snu.edu.in", "location": "Greater Noida"},
            {"name": "Galgotias University", "type": "Private", "category": "Multi-disciplinary", "established": 2011, "ranking": "NIRF #101-150", "entrance_exams": ["GUMEE", "JEE Main"], "website": "https://www.galgotiasuniversity.edu.in", "location": "Greater Noida"},
            {"name": "Bennett University", "type": "Private", "category": "Media/Engineering/Management", "established": 2016, "ranking": "Top Emerging", "entrance_exams": ["BUAT", "JEE Main"], "website": "https://www.bennett.edu.in", "location": "Greater Noida"},
            {"name": "Sharda University", "type": "Private", "category": "Multi-disciplinary", "established": 2009, "ranking": "NIRF #151-200", "entrance_exams": ["SUAT"], "website": "https://www.sharda.ac.in", "location": "Greater Noida"},
            {"name": "Jaypee Institute of Information Technology", "type": "Deemed Private", "category": "Engineering", "established": 2001, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main", "PGET"], "website": "https://www.jiit.ac.in", "location": "Noida"},
        ]
    },
    "Uttarakhand": {
        "emoji": "🏔️", "color": "#1e40af",
        "institutes": [
            {"name": "IIT Roorkee", "type": "Central", "category": "Engineering", "established": 1847, "ranking": "NIRF #7", "entrance_exams": ["JEE Advanced", "GATE", "JAM"], "website": "https://www.iitr.ac.in", "location": "Roorkee"},
            {"name": "AIIMS Rishikesh", "type": "Central", "category": "Medical", "established": 2012, "ranking": "NIRF #22 (Medical)", "entrance_exams": ["NEET UG"], "website": "https://aiimsrishikesh.edu.in", "location": "Rishikesh"},
            {"name": "HNB Garhwal University", "type": "Central", "category": "Multi-disciplinary", "established": 1973, "ranking": "NIRF #101-150", "entrance_exams": ["HNBGU Entrance", "CUET PG"], "website": "https://www.hnbgu.ac.in", "location": "Srinagar"},
            {"name": "Graphic Era University", "type": "Deemed Private", "category": "Engineering", "established": 1993, "ranking": "Top Private UK", "entrance_exams": ["JEE Main", "GEU SAT"], "website": "https://www.geu.ac.in", "location": "Dehradun"},
            {"name": "UPES (University of Petroleum)", "type": "State Private", "category": "Engineering/Management", "established": 2003, "ranking": "NIRF #51-100", "entrance_exams": ["UPESEAT", "JEE Main"], "website": "https://www.upes.ac.in", "location": "Dehradun"},
            {"name": "Dehradun Institute of Technology", "type": "Private", "category": "Engineering", "established": 1998, "ranking": "State", "entrance_exams": ["JEE Main", "Direct Merit"], "website": "https://dituniversity.edu.in", "location": "Dehradun"},
            {"name": "IMS Unison University", "type": "Private", "category": "Management/Law", "established": 1996, "ranking": "Regional Premium", "entrance_exams": ["Direct Merit"], "website": "https://www.iuu.ac", "location": "Dehradun"},
            {"name": "Tulas Institute", "type": "Private", "category": "Engineering/Management", "established": 2006, "ranking": "Regional Lead", "entrance_exams": ["Direct Merit"], "website": "https://tulas.edu.in", "location": "Dehradun"},
        ]
    },
    "West Bengal": {
        "emoji": "🎨", "color": "#5b21b6",
        "institutes": [
            {"name": "IIT Kharagpur", "type": "Central", "category": "Engineering", "established": 1951, "ranking": "NIRF #5", "entrance_exams": ["JEE Advanced", "GATE", "JAM"], "website": "https://www.iitkgp.ac.in", "location": "Kharagpur"},
            {"name": "IIM Calcutta", "type": "Central", "category": "Management", "established": 1961, "ranking": "NIRF MBA #3", "entrance_exams": ["CAT"], "website": "https://www.iimcal.ac.in", "location": "Kolkata"},
            {"name": "WBNUJS Kolkata", "type": "Government", "category": "Law", "established": 1999, "ranking": "NIRF Law #4", "entrance_exams": ["CLAT"], "website": "https://www.nujs.edu", "location": "Kolkata"},
            {"name": "Jadavpur University", "type": "Government", "category": "Engineering/Arts", "established": 1906, "ranking": "NIRF #10", "entrance_exams": ["WBJEE", "JU Entrance"], "website": "https://jadavpuruniversity.in", "location": "Kolkata"},
            {"name": "University of Calcutta", "type": "Government", "category": "Multi-disciplinary", "established": 1857, "ranking": "NIRF #25", "entrance_exams": ["CU Entrance", "CUET PG"], "website": "https://www.caluniv.ac.in", "location": "Kolkata"},
            {"name": "Presidency University", "type": "Government", "category": "Science/Arts", "established": 1817, "ranking": "NIRF #51-100", "entrance_exams": ["Presidency Entrance Test (Merit)"], "website": "https://www.presiuniv.ac.in", "location": "Kolkata"},
            {"name": "NIT Durgapur", "type": "Government (NIT)", "category": "Engineering", "established": 1960, "ranking": "NIRF #51-100", "entrance_exams": ["JEE Main"], "website": "https://www.nitdgp.ac.in", "location": "Durgapur"},
            {"name": "Techno India University", "type": "Private", "category": "Engineering", "established": 2012, "ranking": "State Private", "entrance_exams": ["WBJEE", "JEE Main"], "website": "https://www.technoindiauniversity.ac.in", "location": "Kolkata"},
            {"name": "Adamas University", "type": "Private", "category": "Multi-disciplinary", "established": 2014, "ranking": "Top Private WB", "entrance_exams": ["AUAT"], "website": "https://adamasuniversity.ac.in", "location": "Kolkata"},
            {"name": "Sister Nivedita University", "type": "Private", "category": "Multi-disciplinary", "established": 2017, "ranking": "State Private", "entrance_exams": ["SNUET"], "website": "https://snuniv.ac.in", "location": "Kolkata"},
            {"name": "JIS University", "type": "Private", "category": "Multi-disciplinary", "established": 2014, "ranking": "Regional Private", "entrance_exams": ["JISUEE"], "website": "https://jisuniversity.ac.in", "location": "Kolkata"},
        ]
    },
    "Delhi": {
        "emoji": "🏛️", "color": "#dc2626",
        "institutes": [
            {"name": "IIT Delhi", "type": "Central", "category": "Engineering", "established": 1961, "ranking": "NIRF #2", "entrance_exams": ["JEE Advanced", "GATE", "JAM"], "website": "https://www.iitd.ac.in", "location": "New Delhi"},
            {"name": "AIIMS New Delhi", "type": "Central", "category": "Medical", "established": 1956, "ranking": "NIRF #1 (Medical)", "entrance_exams": ["NEET UG"], "website": "https://www.aiims.edu", "location": "New Delhi"},
            {"name": "FMS Delhi", "type": "Government", "category": "Management", "established": 1954, "ranking": "Top Management India", "entrance_exams": ["CAT"], "website": "http://fms.edu", "location": "New Delhi"},
            {"name": "NLU Delhi", "type": "Government", "category": "Law", "established": 2008, "ranking": "NIRF Law #2", "entrance_exams": ["AILET"], "website": "https://nludelhi.ac.in", "location": "New Delhi"},
            {"name": "Delhi University", "type": "Central", "category": "Multi-disciplinary", "established": 1922, "ranking": "NIRF #15", "entrance_exams": ["CUET UG", "DUET PG"], "website": "https://www.du.ac.in", "location": "New Delhi"},
            {"name": "JNU", "type": "Central", "category": "Multi-disciplinary", "established": 1969, "ranking": "NIRF #2", "entrance_exams": ["CUET PG", "JNUEE"], "website": "https://www.jnu.ac.in", "location": "New Delhi"},
            {"name": "Jamia Millia Islamia", "type": "Central", "category": "Multi-disciplinary", "established": 1920, "ranking": "NIRF #10", "entrance_exams": ["JMI Entrance Test", "CUET"], "website": "https://www.jmi.ac.in", "location": "New Delhi"},
            {"name": "IGNOU", "type": "Central (Open)", "category": "Distance Education", "established": 1985, "ranking": "Largest Open University", "entrance_exams": ["OPENMAT (MBA)", "Direct Merit"], "website": "https://www.ignou.ac.in", "location": "New Delhi"},
            {"name": "IIIT Delhi", "type": "Government (IIIT)", "category": "Engineering/CS", "established": 2008, "ranking": "NIRF #25", "entrance_exams": ["JEE Main", "IIIT Delhi Entrance"], "website": "https://www.iiitd.ac.in", "location": "New Delhi"},
            {"name": "NSUT (NSIT)", "type": "Government", "category": "Engineering", "established": 1983, "ranking": "NIRF #51-100", "entrance_exams": ["JAC Delhi / JEE Main"], "website": "https://www.nsut.ac.in", "location": "New Delhi"},
            {"name": "DTU Delhi", "type": "Government", "category": "Engineering", "established": 1941, "ranking": "NIRF #51-100", "entrance_exams": ["JAC Delhi / JEE Main"], "website": "https://dtu.ac.in", "location": "New Delhi"},
            {"name": "Amity University Delhi", "type": "Private", "category": "Multi-disciplinary", "established": 2005, "ranking": "Top Private Delhi", "entrance_exams": ["Amity JEE", "Direct Merit"], "website": "https://www.amity.edu", "location": "New Delhi"},
        ]
    },
}

# Common national entrance exams for reference
NATIONAL_ENTRANCE_EXAMS = [
    {
        "name": "JEE Main", 
        "full_name": "Joint Entrance Exam Main", 
        "for": "Engineering UG (NITs, IIITs, GFTIs)", 
        "date": "Jan & Apr 2026", 
        "link": "https://jeemain.nta.nic.in",
        "eligibility": "10+2 with Physics, Chemistry, and Mathematics. Minimum 75% marks for NITs/IIITs.",
        "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics (NCERT Curriculum). Topics include Calculus, Mechanics, Thermodynamics, Organic Chemistry.",
        "top_colleges": ["NIT Trichy", "NIT Surathkal", "IIIT Hyderabad", "DTU Delhi"]
    },
    {
        "name": "JEE Advanced", 
        "full_name": "Joint Entrance Exam Advanced", 
        "for": "Engineering UG (IITs)", 
        "date": "May 2026", 
        "link": "https://jeeadv.ac.in",
        "eligibility": "Must clear JEE Main cutoff. Ranked among the top 2,50,000 candidates.",
        "syllabus": "Advanced level Physics, Chemistry, and Mathematics. Focus on application of concepts and problem-solving.",
        "top_colleges": ["IIT Madras", "IIT Delhi", "IIT Bombay", "IIT Kanpur"]
    },
    {
        "name": "NEET UG", 
        "full_name": "National Eligibility cum Entrance Test", 
        "for": "MBBS / BDS / BAMS", 
        "date": "May 2026", 
        "link": "https://neet.nta.nic.in",
        "eligibility": "10+2 with Physics, Chemistry, and Biology. Minimum age 17 years.",
        "syllabus": "Class 11 & 12 Physics, Chemistry, Botany, and Zoology (NCERT Curriculum).",
        "top_colleges": ["AIIMS New Delhi", "CMC Vellore", "JIPMER Puducherry", "KGMU Lucknow"]
    },
    {
        "name": "CUET UG", 
        "full_name": "Common University Entrance Test (UG)", 
        "for": "Central University UG admissions", 
        "date": "May 2026", 
        "link": "https://cuet.samarth.ac.in",
        "eligibility": "10+2 passed from a recognized board. No age limit for appearing.",
        "syllabus": "Language Test, Domain-Specific Subjects (up to 27), and General Test (Reasoning, Current Affairs).",
        "top_colleges": ["Delhi University", "JNU", "BHU", "Jamia Millia Islamia"]
    },
    {
        "name": "CLAT", 
        "full_name": "Common Law Admission Test", 
        "for": "LLB / LLM at NLUs", 
        "date": "Dec 2025", 
        "link": "https://consortiumofnlus.ac.in",
        "eligibility": "10+2 or equivalent examination with a minimum of 45% marks.",
        "syllabus": "English Language, Current Affairs (including GK), Legal Reasoning, Logical Reasoning, and Quantitative Techniques.",
        "top_colleges": ["NLSIU Bengaluru", "NALSAR Hyderabad", "NLU Delhi", "WBNUJS Kolkata"]
    },
    {
        "name": "GATE", 
        "full_name": "Graduate Aptitude Test in Engineering", 
        "for": "M.Tech / PSU Jobs", 
        "date": "Feb 2026", 
        "link": "https://gate.iitkgp.ac.in",
        "eligibility": "3rd or higher year of any undergraduate degree program (B.E./B.Tech/B.Arch/B.Sc. Research/B.S./M.Sc.).",
        "syllabus": "General Aptitude, Engineering Mathematics, and Core Subject (e.g., CS, ME, CE, EE).",
        "top_colleges": ["IISc Bangalore", "IIT Bombay", "IIT Delhi", "IIT Madras"]
    },
    {
        "name": "UPSC", 
        "full_name": "Civil Services Examination", 
        "for": "IAS, IPS, IFS, IFoS", 
        "date": "May 2026 (Prelims)", 
        "link": "https://upsc.gov.in",
        "eligibility": "Degree from a recognized university. Age 21-32 years.",
        "syllabus": "CSAT, General Studies (History, Geography, Polity, Economy, Environment), Optional Subject, Essay.",
        "top_colleges": ["LBSNAA Mussoorie (Training)", "SVPNPA Hyderabad (Training)"]
    },
    {
        "name": "CAT", 
        "full_name": "Common Admission Test", 
        "for": "MBA at IIMs & top B-schools", 
        "date": "Nov 2025", 
        "link": "https://iimcat.ac.in",
        "eligibility": "Bachelor's degree with at least 50% marks or equivalent CGPA.",
        "syllabus": "Verbal Ability & Reading Comprehension (VARC), Data Interpretation & Logical Reasoning (DILR), Quantitative Ability (QA).",
        "top_colleges": ["IIM Ahmedabad", "IIM Bangalore", "IIM Calcutta", "FMS Delhi"]
    }
]
