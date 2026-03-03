# 2026 WinterGames Day 1: Opening Day

# Today marks the start of the 2026 WinterGames. The next 17 days will bring you coding challenges inspired by them.

# For the first one, you aregiven a two-letter country code and need to return the flag emoji for that country.

# Use this list:
flags = {
    "AL": "🇦🇱",
    "AD": "🇦🇩",
    "AR": "🇦🇷",
    "AM": "🇦🇲",
    "AU": "🇦🇺",
    "AT": "🇦🇹",
    "AZ": "🇦🇿",
    "BE": "🇧🇪",
    "BJ": "🇧🇯",
    "BO": "🇧🇴",
    "BA": "🇧🇦",
    "BR": "🇧🇷",
    "BG": "🇧🇬",
    "CA": "🇨🇦",
    "CL": "🇨🇱",
    "CN": "🇨🇳",
    "CO": "🇨🇴",
    "HR": "🇭🇷",
    "CY": "🇨🇾",
    "CZ": "🇨🇿",
    "DK": "🇩🇰",
    "EC": "🇪🇨",
    "ER": "🇪🇷",
    "EE": "🇪🇪",
    "FI": "🇫🇮",
    "FR": "🇫🇷",
    "GE": "🇬🇪",
    "DE": "🇩🇪",
    "GB": "🇬🇧",
    "GR": "🇬🇷",
    "GW": "🇬🇼",
    "HT": "🇭🇹",
    "HK": "🇭🇰",
    "HU": "🇭🇺",
    "IS": "🇮🇸",
    "IN": "🇮🇳",
    "IR": "🇮🇷",
    "IE": "🇮🇪",
    "IL": "🇮🇱",
    "IT": "🇮🇹",
    "JM": "🇯🇲",
    "JP": "🇯🇵",
    "KZ": "🇰🇿",
    "KE": "🇰🇪",
    "XK": "🇽🇰",
    "KG": "🇰🇬",
    "LV": "🇱🇻",
    "LB": "🇱🇧",
    "LI": "🇱🇮",
    "LT": "🇱🇹",
    "LU": "🇱🇺",
    "MG": "🇲🇬",
    "MY": "🇲🇾",
    "MT": "🇲🇹",
    "MX": "🇲🇽",
    "MD": "🇲🇩",
    "MC": "🇲🇨",
    "MN": "🇲🇳",
    "ME": "🇲🇪",
    "MA": "🇲🇦",
    "NL": "🇳🇱",
    "NZ": "🇳🇿",
    "NG": "🇳🇬",
    "MK": "🇲🇰",
    "NO": "🇳🇴",
    "PK": "🇵🇰",
    "PH": "🇵🇭",
    "PL": "🇵🇱",
    "PT": "🇵🇹",
    "PR": "🇵🇷",
    "RO": "🇷🇴",
    "SM": "🇸🇲",
    "SA": "🇸🇦",
    "RS": "🇷🇸",
    "SG": "🇸🇬",
    "SK": "🇸🇰",
    "SI": "🇸🇮",
    "ZA": "🇿🇦",
    "KR": "🇰🇷",
    "ES": "🇪🇸",
    "SE": "🇸🇪",
    "CH": "🇨🇭",
    "TH": "🇹🇭",
    "TT": "🇹🇹",
    "TR": "🇹🇷",
    "UA": "🇺🇦",
    "AE": "🇦🇪",
    "US": "🇺🇸",
    "UY": "🇺🇾",
    "UZ": "🇺🇿",
    "VE": "🇻🇪",
}

def get_flag(code):
    try:
        return flags[code]
    except:
        return 'Flag not found'


print(get_flag("AL"))
print(get_flag("AD"))
print(get_flag("AR"))
print(get_flag("AM"))
print(get_flag("AU"))
print(get_flag("AT"))
print(get_flag("AZ"))
print(get_flag("BE"))
print(get_flag("BJ"))
print(get_flag("BO"))
print(get_flag("BA"))
print(get_flag("BR"))
print(get_flag("BG"))
print(get_flag("CA"))
print(get_flag("CL"))
print(get_flag("CN"))
print(get_flag("CO"))
print(get_flag("HR"))
print(get_flag("CY"))
print(get_flag("CZ"))
print(get_flag("DK"))
print(get_flag("EC"))
print(get_flag("ER"))
print(get_flag("EE"))
print(get_flag("FI"))
print(get_flag("FR"))
print(get_flag("GE"))
print(get_flag("DE"))
print(get_flag("GB"))
print(get_flag("GR"))
print(get_flag("GW"))
print(get_flag("HT"))
print(get_flag("HK"))
print(get_flag("HU"))
print(get_flag("IS"))
print(get_flag("IN"))
print(get_flag("IR"))
print(get_flag("IE"))
print(get_flag("IL"))
print(get_flag("IT"))
print(get_flag("JM"))
print(get_flag("JP"))
print(get_flag("KZ"))
print(get_flag("KE"))
print(get_flag("XK"))
print(get_flag("KG"))
print(get_flag("LV"))
print(get_flag("LB"))
print(get_flag("LI"))
print(get_flag("LT"))
print(get_flag("LU"))
print(get_flag("MG"))
print(get_flag("MY"))
print(get_flag("MT"))
print(get_flag("MX"))
print(get_flag("MD"))
print(get_flag("MC"))
print(get_flag("MN"))
print(get_flag("ME"))
print(get_flag("MA"))
print(get_flag("NL"))
print(get_flag("NZ"))
print(get_flag("NG"))
print(get_flag("MK"))
print(get_flag("NO"))
print(get_flag("PK"))
print(get_flag("PH"))
print(get_flag("PL"))
print(get_flag("PT"))
print(get_flag("PR"))
print(get_flag("RO"))
print(get_flag("SM"))
print(get_flag("SA"))
print(get_flag("RS"))
print(get_flag("SG"))
print(get_flag("SK"))
print(get_flag("SI"))
print(get_flag("ZA"))
print(get_flag("KR"))
print(get_flag("ES"))
print(get_flag("SE"))
print(get_flag("CH"))
print(get_flag("TH"))
print(get_flag("TT"))
print(get_flag("TR"))
print(get_flag("UA"))
print(get_flag("AE"))
print(get_flag("US"))
print(get_flag("UY"))
print(get_flag("UZ"))
print(get_flag("VE"))