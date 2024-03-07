

def Change_Name(name):
    name.strip()
    item = {
        "GBP": '英镑',
        "HKD": '港币',
        "USD": '美元',
        "CHF": '瑞士法郎',
        "DEM": '德国马克',
        "FRF": '法国法郎',
        "SGD": '新加坡元',
        "SEK": '瑞典克朗',
        "DKK": '丹麦克朗',
        "NOK": '挪威克朗',
        "JPY": '日元',
        "CAD": '加拿大元',
        "AUD": '澳大利亚元',
        "EUR": '欧元',
        "MOP": '澳门元',
        "PHP": '菲律宾比索',
        "THP": '泰国铢',
        "NZD": '新西兰元',
        "无": '韩国元',
        "SUR": '卢布',
        "wu": '林吉特',
        "taiwan": '新台币',
        "ESP": '西班牙比塞塔',
        "ITL": '意大利里拉',
        "NLG": '荷兰盾',
        "BEF": '比利时法郎',
        "FIM": '芬兰马克',
        "INR": '印度卢比',
        "IDR": '印尼卢比',
        "BRC": '巴西里亚尔',
        "alianqiu": '阿联酋迪拉姆',
        "nanfei": '南非兰特',
        "SAR": '沙特里亚尔',
        "TRL": '土耳其里拉',
    }
    return item[name]




