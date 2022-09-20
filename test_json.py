import pytest

# 创建订单json
createdataone = {
    "ownerId": 316,
    "partnerId": 33,
    "province": "110000",
    "city": "110100",
    "district": "110105",
    "address": "12347",
    "bpId": 1,
    "roofType": 2,
    "year": "2022",
    "area": "120.00",
    "transformerPower": "100.00",
    "annualPower": "100.00",
    "pattern": 1
}
createdatatwo = {
    "ownerId": 316,
    "partnerId": 142,
    "province": "110000",
    "city": "110100",
    "district": "110105",
    "address": "12347",
    "bpId": 1,
    "roofType": 2,
    "year": "2022",
    "area": "120.00",
    "transformerPower": "100.00",
    "annualPower": "100.00",
    "pattern": 1
}
information = {
    "menuId": 73,
    "pageNum": 1,
    "pageSize": 20
}
tycone = {"orderGuid": None, "verifyStatus": 2, "verifyReason": None}

# app合伙人踏勘josn
appreconnaissance1 = {
    "orderGuid": None,
    "assignType": None,
    "partnerId": None
}
appreconnaissance2 = {
    "orderGuid": None,
    "surveyType": 2
}
appreconnaissance3 = {
    "orderGuid": None,
    "xAxis": "116.9",
    "yAxis": "37",
    "electricCompany": "111",
    "developManager": "222",
    "initEscort": "333",
    "detailEscort": "444",
    "surveyPerson": "555"
}
appreconnaissance4 = {
    "isDrawing": 2,
    "orderGuid": None,
    "surveyType": 2
}
appreconnaissance5 = {
    "orderGuid": None,
    "name": "欧啦啦",
    "type": 1
}
appreconnaissance6 = {
    "orderGuid": None,
    "plantId": None,
    "structureType": 3,
    "surveyType": 2,
    "type": 1
}
appreconnaissance7 = {
    "builtLayer": 2,
    "builtYear": "2022",
    "estimateArea": 0,
    "isBuilding": 2,
    "isElec": 2,
    "isRoof": 2,
    "isStructure": 2,
    "orderGuid": None,
    "plantId": None,
    "roofHigh": 1.5,
    "surveyType": 2
}
appreconnaissance8 = {
    "orderGuid": None,
    "plantId": None,
    "positionAngle": None,
    "roofPics": [
        "http://minio-test.skyworthpv.cn/commerce/test1/2022/8/22/1009905239870328832/1661140387974GxLzSn.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20220822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220822T035308Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=bf4b1343936e48d2bc21aff4b9683559c916c63646519e743f87076533a4698e",
        "http://minio-test.skyworthpv.cn/commerce/test1/2022/8/22/1009905239870328832/16611403929087Okh98.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20220822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220822T035313Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8b26f56816d77166d0fb92d4d6b97249edcc97e1bd38e84b6ade272c28755e05",
        "http://minio-test.skyworthpv.cn/commerce/test1/2022/8/22/1009905239870328832/1661140396788DSrbNJ.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20220822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220822T035317Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=06205df2429a663a8b357e1e2d76d259b21d3fe368064473fff591bd8b8fec7d"],
    "structureType": 0,
    "style": 1,
    "surveyType": 2,
    "tiltAngle": "",
    "type": 1
}
appreconnaissance9 = {
    "isRepair": 2,
    "orderGuid": None,
    "plantId": None,
    "type": 2
}
appreconnaissance10 = {
    "isPollute": 2,
    "orderGuid": None,
    "plantId": None,
    "surveyType": 2,
    "type": 1
}
appreconnaissance11 = {
    "isFs": 2,
    "isLeak": 2,
    "orderGuid": None,
    "plantId": None,
    "surveyType": 2,
    "type": 1
}
appreconnaissance12 = {
    "orderGuid": None,
    "id": None,
    "type": 1
}
appreconnaissance13 = {
    "orderGuid": None,
    "name": "36525"
}
appreconnaissance14 = {
    "splId": None,
    "orderGuid": None,
    "name": "666"
}
appreconnaissance15 = {
    "isCable": 2,
    "orderGuid": None,
    "plantLoc": "142536",
    "scale": 100.0,
    "spareLoc": "14580",
    "sprId": None,
    "transformerList": [{
        "capacity": 6000,
        "highGrade": 6800,
        "lowGrade": 6000,
        "orderGuid": None,
        "pic": "http://minio-test.skyworthpv.cn/commerce/test1/2022/8/22/1009905239870328832/1661141963539mISVDm.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20220822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220822T041923Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e9e632e57d2d9387b6ac6cf2cc46d654c5a52779b3ee0d45e8c4b4f625ba9ce1",
        "sprId": None
    }]
}
appreconnaissance16 = {
    "installed": 6000.0,
    "ownerRequire": "444",
    "orderGuid": None,
    "progressPlan": "333",
    "needSupport": "555"
}
appreconnaissance17 = {
    "orderGuid": None
}

# 绑定金融机构json
financial1 = {
    "orderGuid": None,
    "fcId": "3"
}
# 踏勘列表信息
rat1 = {
    "startTime": None,
    "endTime": None,
    "orderGuid": None,
    "ownerId": None,
    "partnerId": None,
    "type": None,
    "status": None,
    "pageSize": 20,
    "pageNum": 1,
    "businessStatus": None
}
# 踏勘审核json
rat2 = {
    "id": None,
    "remark": "踏勘审核通过",
    "businessAudit": 1
}
rat3 = {
    "id": None,
    "model": 1,
    "biId": None,
    "remark":"踏勘审核通过"
}
loadlist = {
    "pageSize": 20,
    "pageNum": 1
}
loadjosnone = {
    "id": None,
    "url": "http://minio-test.skyworthpv.cn/public/test1/2022/8/30/1661837698318yUkzab.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T053458Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=96078e059d634af3b1eda193708f664352d6928333eb1f35450701fffa5b2590",
    "model": 1,
    "designType": 2
}
loadjosntwo = {
    "id": None,
    "status": 4,
    "remark": "666"
}
# # 创建订单json
# def test_create_json():
#     return createdata
#
#
# # 项目订单信息json
# def test_information_json():
#     return information
