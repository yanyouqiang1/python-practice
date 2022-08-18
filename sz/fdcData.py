import requests
from save import save

cookies = {
    'cookie_3.36_8080': '85416334',
    'ftzjjszgovcn': '0',
    'zlpt-session-id_test': '0e09db6d-e882-4616-bb4f-5994d286cffc',
    'historyKeyW': '%2C%2C%E4%BD%8F%E6%88%BF',
    'Hm_lvt_ddaf92bcdd865fd907acdaba0285f9b1': '1659796162,1659796176,1659796195',
    'pgv_pvi': '2084242432',
    'pgv_si': 's9974370304',
    'JSESSIONID': 'z3xzlCS4JvU4cMdpedA74YlZwpUiPGMilwVEHafu_m311FLTvyVb!1473770112',
    'Hm_lpvt_ddaf92bcdd865fd907acdaba0285f9b1': '1659796614',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'cookie_3.36_8080=85416334; ftzjjszgovcn=0; zlpt-session-id_test=0e09db6d-e882-4616-bb4f-5994d286cffc; historyKeyW=%2C%2C%E4%BD%8F%E6%88%BF; Hm_lvt_ddaf92bcdd865fd907acdaba0285f9b1=1659796162,1659796176,1659796195; pgv_pvi=2084242432; pgv_si=s9974370304; JSESSIONID=z3xzlCS4JvU4cMdpedA74YlZwpUiPGMilwVEHafu_m311FLTvyVb!1473770112; Hm_lpvt_ddaf92bcdd865fd907acdaba0285f9b1=1659796614',
    'Origin': 'http://zjj.sz.gov.cn:8004',
    'Referer': 'http://zjj.sz.gov.cn:8004/public/marketInfo/housePriceTrendInfo.html',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

json_data = {
    'startDate': '2010-07-01',
    'endDate': '2022-08-01',
    'dateType': '',
}

response = requests.post('http://zjj.sz.gov.cn:8004/api/marketInfoShow/getFjzsInfoData', cookies=cookies, headers=headers, json=json_data, verify=False)

save(response.text,"fdc.txt")
