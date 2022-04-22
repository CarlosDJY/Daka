from abc import ABCMeta, abstractmethod
from typing import Optional
import os


"""
USERS=[("学号","密码","姓名/昵称",0)]
WECOM=("企业ID③", "应用ID①", "应用secret②")
"""
USERS = eval(os.environ['USERS'])
WECOM = eval(os.environ['WECOM'])

LOGIN_API = 'https://auth.bupt.edu.cn/authserver/login'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'
# 重要: CAS认证的跳转地址记录
SERVICE = 'https://app.bupt.edu.cn/a_bupt/api/sso/cas?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&from=wap'
# 模拟浏览器信息
USER_AGENT = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
# Execution信息的xpath
EXECUTION_XPATH = '/html/body/div[1]/div/form/div[5]/input[2]/@value'
GETEven_API = 'https://app.bupt.edu.cn/xisuncov/wap/open-report/index'
POSTEven_API = 'https://app.bupt.edu.cn/xisuncov/wap/open-report/save'


# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
INFO = r"""{
        address: "上海市宝山区张庙街道南北高架路宝山购物中心"
        area: "上海市  宝山区"
        bztcyy: ""
        city: "上海市"
        created: 1650585636
        created_uid: 0
        csmjry: "0"
        date: "20220422"
        fxyy: ""
        geo_api_info: "{\"type\":\"complete\",\"position\":{\"Q\":31.325374077691,\"R\":121.44423611111199,\"lng\":121.444236,\"lat\":31.325374},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":94,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310113\",\"businessAreas\":[{\"name\":\"共康\",\"id\":\"310113\",\"location\":{\"Q\":31.320874,\"R\":121.43926299999998,\"lng\":121.439263,\"lat\":31.320874}},{\"name\":\"庙行镇\",\"id\":\"310113\",\"location\":{\"Q\":31.329455,\"R\":121.43615599999998,\"lng\":121.436156,\"lat\":31.329455}},{\"name\":\"通河\",\"id\":\"310113\",\"location\":{\"Q\":31.333801,\"R\":121.44710800000001,\"lng\":121.447108,\"lat\":31.333801}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"共和新路\",\"streetNumber\":\"5199甲\",\"country\":\"中国\",\"province\":\"上海市\",\"city\":\"\",\"district\":\"宝山区\",\"towncode\":\"310113008000\",\"township\":\"张庙街道\"},\"formattedAddress\":\"上海市宝山区张庙街道南北高架路宝山购物中心\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}"
        glksrq: ""
        gllx: ""
        gtjzzfjsj: ""
        gwszdd: ""
        id: 19786025
        ismoved: 0
        jcbhlx: ""
        jcbhrq: ""
        jchbryfs: ""
        jcjg: ""
        jcjgqr: "0"
        jcqzrq: ""
        jcwhryfs: ""
        jhfjhbcc: ""
        jhfjjtgj: ""
        jhfjrq: ""
        jrsfqzfy: ""
        jrsfqzys: ""
        mjry: "0"
        province: "上海市"
        qksm: ""
        remark: ""
        sfcxtz: "0"
        sfcxzysx: "0"
        sfcyglq: "0"
        sfjcbh: "0"
        sfjchbry: "0"
        sfjcqz: ""
        sfjcwhry: "0"
        sfjzdezxgym: 0
        sfjzxgym: 0
        sfsfbh: 0
        sfsqhzjkk: 0
        sftjhb: "0"
        sftjwh: "0"
        sfxk: 0
        sfygtjzzfj: 0
        sfyqjzgc: ""
        sfyyjc: "0"
        sfzx: 0
        sqhzjkkys: ""
        szcs: ""
        szgj: ""
        szsqsfybl: "1"
        tw: "3"
        uid: "83798"
        xjzd: ""
        xkqq: ""
        xwxgymjzqk: 3
        ymjzxgqk: "无"
        zgfxdq: "0"
        }"""

INFO_E = r"""{
    "sfzx": "0",
    "tw":"3",
    "area":"上海市  宝山区",
    "city":"上海市",
    "province":"上海市",
    "address":"上海市宝山区张庙街道南北高架路宝山购物中心",
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":31.325374077691,\"R\":121.44423611111199,\"lng\":121.444236,\"lat\":31.325374},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":94,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310113\",\"businessAreas\":[{\"name\":\"共康\",\"id\":\"310113\",\"location\":{\"Q\":31.320874,\"R\":121.43926299999998,\"lng\":121.439263,\"lat\":31.320874}},{\"name\":\"庙行镇\",\"id\":\"310113\",\"location\":{\"Q\":31.329455,\"R\":121.43615599999998,\"lng\":121.436156,\"lat\":31.329455}},{\"name\":\"通河\",\"id\":\"310113\",\"location\":{\"Q\":31.333801,\"R\":121.44710800000001,\"lng\":121.447108,\"lat\":31.333801}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"共和新路\",\"streetNumber\":\"5199甲\",\"country\":\"中国\",\"province\":\"上海市\",\"city\":\"\",\"district\":\"宝山区\",\"towncode\":\"310113008000\",\"township\":\"张庙街道\"},\"formattedAddress\":\"上海市宝山区张庙街道南北高架路宝山购物中心\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "sfcyglq": "0",
    "sfyzz": "0","qtqk": "","askforleave": "0"
    }"""


REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25


class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError


COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}
