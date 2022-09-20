import json

from databases import *
from test_json import *
from test_time import x_time as time
from test_url import *
import pytest
import requests

permissions_headers = {  # Web端Token
    "accessToken": None,
    "Content-Type": "application/json;charset=UTF-8"

}

# permissions_headers1 = {
#     "accessToken": "d3a35c78-2f56-47bb-917f-bdfda51ee51a",
#     "Content-Type": "application/json;charset=UTF-8"
#
# }
apppermissions_headers = {  # APPToken
    "accessToken": "",
    "Content-Type": "application/json;charset=UTF-8"
}
# 71af727e-0f21-4bf2-a87d-7567ebfc6826
# 项目订单全局guid
test_guid = 1
x_time = time


class Test_ss_xx:

    def test_choose1(self):  # 创建订单
        # key1 = str(input("输入校验密钥accessToken："))
        keyliong = {
            'Content-Type': 'application/json',
            'platform': 'MANAGER',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
        hj = 'http://spv1-spv.skyworthpv.cn/'
        hj1 = requests.get(hj, headers=keyliong)
        hj1.encoding = 'UTF-8'
        print("访问结果：", hj1)
        users = str(input("工商业Test账号："))
        # passwords = str(input("密码："))
        url1 = "http://spv1-gateway.skyworthpv.cn/login"
        url2 = 'http://spv1-gateway.skyworthpv.cn/public/sendSms'
        json1 = {
            "type": 1,
            "phone": None
        }
        json1['phone'] = users
        project2 = requests.post(url2, json=json1, headers=keyliong)
        print(json1)
        print("验证码状态:", project2.json())
        toobtain1 = json.loads(project2.text)

        # 访问t1环境
        json2 = {
            "username": None,
            "password": "Xp4YtK84rmD07AyNKAtcAJ5IJE5I57x0ss7AjSaIlRF643FpCCF8iIuuOvip9YTFFseC5Kc06XhiicKcrtgz1nSnxSaffvnWD7SBLJpKxciuQ62wSBgN/lCftqcXlcOIbNNPH9tRskznMBXPFU9OSLel3WIN/vnejLWtry301EI=",
            "code": None,
            "type": 1
        }
        json2['username'] = users
        # json2['password'] = passwords
        code1 = toobtain1.get('data')
        json2['code'] = code1
        session1 = requests.session()

        project1 = session1.post(url1, json=json2, headers=keyliong)
        project1.encoding = 'UTF-8'
        print(json2)
        print("登录状态：", project1.json())
        toobtain2 = json.loads(project1.text)
        code2 = toobtain2.get('data').get('accessToken')
        print("accessToken:", code2)
        permissions_headers['accessToken']=code2
        print("查看web端捕捉密钥：", permissions_headers)

        digitalone = 1
        digitaltwo = 2
        while True:
            print("创建订单：")
            # keyone = str(input("请输入密钥TOKEN："))  # 及时更新token
            # print(permissions_headers)
            print("请选择输入：【1】是公司合伙人，【2】是业务合伙人")
            textstr = int(input("选择关联的合伙人请选择："))
            if textstr == digitalone:
                rep = requests.post(url=createurl, headers=permissions_headers, json=createdataone)  # 新增订单关联公司合伙人
                print(rep.json())
                break
            if textstr == digitaltwo:
                rep = requests.post(url=createurl, headers=permissions_headers, json=createdatatwo)  # 新增订单关联业务合伙人
                print(rep.json())
                break
            else:
                print("输入错误")

    def test_information(self):  # 信用评估
        global test_guid
        global x_time
        information_rep = requests.post(informationurl, headers=permissions_headers, json=information)  # 项目订单列表获取guid
        # print(json.loads(information_rep.text))
        test_guid = json.loads(information_rep.text)
        print(test_guid)
        guid = test_guid.get("data").get("data")[0].get("guid")
        print(guid)  # get guid
        time1 = x_time
        time2 = x_time
        time3 = x_time
        print(time1, time2, time3)  # 输出 时间
        ss = spv_tyc.format(guid, time1, time2, time3)
        print(ss)
        # 天眼查插入数据执行数据
        cursor.execute(ss)
        db.commit()
        tycone['orderGuid'] = guid
        tyctextone = requests.post(tycaudit, headers=permissions_headers, json=tycone)  # 信用评估审核通过
        print(tycone)
        print(tyctextone.text)

    def test_appreconnaissance(self):  # 踏勘关联
        personnelone = 1
        personneltwo = 2
        while True:
            print("App合伙人踏勘")
            tokentwo = str(input("请输入app合伙人accessToken："))
            apppermissions_headers['accessToken'] = tokentwo
            print("指派类型(1-直接踏勘 2-关联合伙人踏勘)")
            personnes = int(input("请选择："))
            guidone = test_guid.get("data").get("data")[0].get("guid")
            appreconnaissance1['orderGuid'] = guidone
            if personnes == personnelone:
                appreconnaissance1['assignType'] = personnelone
                tk1 = requests.post(reconnaissance1, headers=apppermissions_headers, json=appreconnaissance1)
                print(appreconnaissance1)
                print(tk1.json())
            if personnes == personneltwo:
                appreconnaissance1['assignType'] = personneltwo
                tk1 = requests.post(reconnaissance1, headers=apppermissions_headers, json=appreconnaissance1)
                print(appreconnaissance1)
                print(tk1.json())
            print("===================================================================================================")
            break

    def test_appeconnaissances(self):  # 立即踏勘/开始踏勘
        guidone = test_guid.get("data").get("data")[0].get("guid")
        appreconnaissance1['orderGuid'] = guidone
        print("根据选择的合伙人踏勘")
        tokenthree = str(input("请输入app踏勘相关的accessToken："))
        apppermissions_headers['accessToken'] = tokenthree
        appreconnaissance2['orderGuid'] = guidone
        tk2 = requests.post(reconnaissance2, headers=apppermissions_headers, json=appreconnaissance2)
        print(tk2.text)
        print(tk2.json())
        appreconnaissance3['orderGuid'] = guidone
        tk3 = requests.post(reconnaissance3, headers=apppermissions_headers, json=appreconnaissance3)
        print(tk3.text)
        print(tk3.json())
        appreconnaissance4['orderGuid'] = guidone
        tk4 = requests.post(reconnaissance4, headers=apppermissions_headers, json=appreconnaissance4)
        print(tk4.text)
        print(tk4.json())
        appreconnaissance5['orderGuid'] = guidone
        tk5 = requests.post(reconnaissance5, headers=apppermissions_headers, json=appreconnaissance5)
        print(tk5.text)
        print(tk5.json())
        appplantId = json.loads(tk5.text)
        lantIdone = appplantId.get("data").get("id")
        appreconnaissance6['orderGuid'] = guidone
        appreconnaissance6['plantId'] = lantIdone
        tk6 = requests.post(reconnaissance6, headers=apppermissions_headers, json=appreconnaissance6)
        print(tk6.text)
        print(tk6.json())
        appreconnaissance7['orderGuid'] = guidone
        appreconnaissance7['plantId'] = lantIdone
        tk7 = requests.post(reconnaissance7, headers=apppermissions_headers, json=appreconnaissance7)
        print(tk7.text)
        print(tk7.json())
        appreconnaissance8['orderGuid'] = guidone
        appreconnaissance8['plantId'] = lantIdone
        tk8 = requests.post(reconnaissance8, headers=apppermissions_headers, json=appreconnaissance8)
        print(tk8.text)
        print(tk8.json())
        appreconnaissance9['orderGuid'] = guidone
        appreconnaissance9['plantId'] = lantIdone
        tk9 = requests.post(reconnaissance9, headers=apppermissions_headers, json=appreconnaissance9)
        print(tk9.text)
        print(tk9.json())
        appreconnaissance10['orderGuid'] = guidone
        appreconnaissance10['plantId'] = lantIdone
        tk10 = requests.post(reconnaissance10, headers=apppermissions_headers, json=appreconnaissance10)
        print(tk10.text)
        print(tk10.json())
        appreconnaissance11['orderGuid'] = guidone
        appreconnaissance11['plantId'] = lantIdone
        tk11 = requests.post(reconnaissance11, headers=apppermissions_headers, json=appreconnaissance11)
        print(tk11.text)
        print(tk11.json())
        appreconnaissance12['orderGuid'] = guidone
        appreconnaissance12['id'] = lantIdone
        tk12 = requests.post(reconnaissance12, headers=apppermissions_headers, json=appreconnaissance12)
        print(tk12.text)
        print(tk12.json())
        appreconnaissance13['orderGuid'] = guidone
        tk13 = requests.post(reconnaissance13, headers=apppermissions_headers, json=appreconnaissance13)
        print(tk13.text)
        print(tk13.json())
        appsplId = json.loads(tk13.text)
        splidone = appsplId.get("data").get("id")
        appreconnaissance14['orderGuid'] = guidone
        appreconnaissance14['splId'] = splidone
        tk14 = requests.post(reconnaissance14, headers=apppermissions_headers, json=appreconnaissance14)
        print(tk14.text)
        print(tk14.json())
        appsprId = json.loads(tk14.text)
        spridone = appsprId.get("data").get("id")
        appreconnaissance15['sprId'] = spridone
        appreconnaissance15['transformerList'][0]['sprId'] = spridone
        appreconnaissance15['orderGuid'] = guidone
        appreconnaissance15['transformerList'][0]['orderGuid'] = guidone
        tk15 = requests.post(reconnaissance15, headers=apppermissions_headers, json=appreconnaissance15)
        print(tk15.text)
        print(tk15.json())
        print(appreconnaissance15)
        appreconnaissance16['orderGuid'] = guidone
        tk16 = requests.post(reconnaissance16, headers=apppermissions_headers, json=appreconnaissance16)
        print(tk16.text)
        print(tk16.json())
        appreconnaissance17['orderGuid'] = guidone
        interfaceone = reconnaissance17.format(guidone)
        print(interfaceone)
        tk17 = requests.post(interfaceone, headers=apppermissions_headers, json=appreconnaissance17)
        print(tk17.text)
        print(tk17.json())

    def test_financial(self):  # 融资机构
        financialguid = test_guid.get("data").get("data")[0].get("guid")
        financial1['orderGuid'] = financialguid
        financialrep = requests.post(financialone, headers=permissions_headers, json=financial1)

        print(financialrep.json())

    def test_rat(self):  # 后台踏勘审核
        ratrep = requests.post(ratone, headers=permissions_headers, json=rat1)
        print(ratrep.text)
        rattext = json.loads(ratrep.text)
        rraatt = rattext.get("data").get("data")[0].get("id")
        print(rraatt)
        rat2['id'] = rraatt
        ratrep1 = requests.post(rattwo, headers=permissions_headers, json=rat2)
        print(ratrep1.json)
        rat3['id'] = rraatt
        ratrep2 = requests.post(rattheer, headers=permissions_headers, json=rat3)
        print(ratrep2.text)

    def test_load(self):
        loadarr = requests.post(loadlistone, headers=permissions_headers, json=loadlist)
        print(loadarr.text)
        loadss = json.loads(loadarr.text)
        rraattss = loadss.get("data").get("data")[0].get("id")
        loadjosnone['id'] = rraattss
        loadarrs = requests.post(loadone, headers=permissions_headers, json=loadjosnone)
        print(loadarrs.json())
        loadjosntwo['id'] = rraattss
        loadarrss = requests.post(loadtwo, headers=permissions_headers, json=loadjosntwo)
        print(loadarrss.json())


if __name__ == '__main__':
    print(pytest.main(['-vs']))
