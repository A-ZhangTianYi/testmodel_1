import pytest
import requests

# Request_header = "http://spv1-spv.skyworthpv.cn"
# 创建订单路径
createurl = "http://spv1-gateway.skyworthpv.cn/icmanager/orderInfo/create"
informationurl = "http://spv1-gateway.skyworthpv.cn/icmanager/orderInfo/list"
tycaudit = "http://spv1-gateway.skyworthpv.cn/icmanager/orderInfo/tycVerify"

# APP接口 踏勘
# 业务人员踏勘选择
reconnaissance1 = "http://spv1-gateway.skyworthpv.cn/partner/survey/businessChooseType"
# 选择踏勘方式
reconnaissance2 = "http://spv1-gateway.skyworthpv.cn/partner/survey/chooseSurveyType"
# 踏勘-添加单位及人员信息
reconnaissance3 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyBasicPersonAdd"
# 踏勘-厂区基本信息查询
reconnaissance4 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyFactoryAdd"
# 踏勘-添加建筑厂房基本信息
reconnaissance5 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantAdd"
# 踏勘-建筑结构形式信息完善
reconnaissance6 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantStructurePerfect"
# 踏勘-建筑图纸信息完善
reconnaissance7 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantDrawingPerfect"
# 踏勘-建筑屋面信息完善
reconnaissance8 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantRoofPerfect"
# 踏勘-建筑屋面维护状况信息完善
reconnaissance9 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantMaintainPerfect"
# 踏勘-建筑屋面污染源信息完善
reconnaissance10 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantPollutePerfect"
# 踏勘-建筑屋面漏水情况信息完善
reconnaissance11 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantLeakPerfect"
# 踏勘-建筑厂房信息维护
reconnaissance12 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveyPlantPerfect"
# 配电路线
reconnaissance13 = "http://spv1-gateway.skyworthpv.cn/partner/survey/pdLineAdd"
# 新增配电室
reconnaissance14 = "http://spv1-gateway.skyworthpv.cn/partner/survey/pdRoomAdd"
# 新增变压器等。。。
reconnaissance15 = "http://spv1-gateway.skyworthpv.cn/partner/survey/pdRoomDetailsAdd"
# 踏勘总结
reconnaissance16 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveySummaryAdd"
# 踏勘完成-提交
reconnaissance17 = "http://spv1-gateway.skyworthpv.cn/partner/survey/surveySuccessCommit/{}"

# 绑定金融机构
financialone = "http://spv1-gateway.skyworthpv.cn/icmanager/orderInfo/bindFc"

# 踏勘列表信息
ratone = "http://spv1-gateway.skyworthpv.cn/icmanager/surveyQueryManager/list"
# 踏勘审核
rattwo = "http://spv1-gateway.skyworthpv.cn/icmanager/surveyCommandManager/businessApprove"
# 踏勘技术审核
rattheer = "http://spv1-gateway.skyworthpv.cn/icmanager/surveyCommandManager/initApprove"
#荷载数据
loadlistone ="http://spv1-gateway.skyworthpv.cn/icmanager/orderLoadManager/list"
#荷载提交
loadone  = "http://spv1-gateway.skyworthpv.cn/icmanager/orderLoadManager/submit"
#荷载审核
loadtwo = "http://spv1-gateway.skyworthpv.cn/icmanager/orderLoadManager/approve"
# # 创建订单接口
# def orderInfo_create_url():
#     return createurl
#
#
# def orderInfo_create_url_1():
#     return informationurl
