# 机动车销售发票查询-sim_vatinvoice_vehicles

## 机动车销售发票查询-主表 t_sim_vatinvoice_vehicles

- **表名称：** 机动车销售发票查询-主表
- **表名：** t_sim_vatinvoice_vehicles

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 3 | fproducingname | 生产企业名称 | varchar | 150 |  | √ | ' ' | 生产企业名称 |
| 4 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 5 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.04 :4% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 6 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 7 | forgid | 组织： | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fvehicleidcode | 车辆识别代码/车架号码 | varchar | 50 |  | √ | ' ' | 车辆识别代码/车架号码 |
| 9 | fbuyercardno | 购方身份证号/组织机构代码 | varchar | 50 |  | √ | ' ' | 购方身份证号/组织机构代码 |
| 10 | fcertificatenum | 合格证 | varchar | 50 |  | √ | ' ' | 合格证 |
| 11 | fresult | 开票结果 | varchar | 255 |  | √ | ' ' | 开票结果 |
| 12 | ftaxauthoritycode | 税务机关代码 | varchar | 50 |  | √ | ' ' | 税务机关代码 |
| 13 | fsaleraccount | 销方银行账号 | varchar | 50 |  | √ | ' ' | 销方银行账号 |
| 14 | fsaleraddr | fsaleraddr | varchar | 100 |  | √ | ' ' |  |
| 15 | fsalerbankname | 销方银行 | varchar | 100 |  | √ | ' ' | 销方银行 |
| 16 | finvoicecode | 发票代码 | varchar | 30 |  | √ | ' ' | 发票代码 |
| 17 | fzzstsgl | 增值税特殊管理 | varchar | 80 |  | √ | ' ' | 增值税特殊管理 |
| 18 | fbuyername | 购买方名称 | varchar | 100 |  | √ | ' ' | 购买方名称 |
| 19 | finvoiceno | 发票号码 | varchar | 30 |  | √ | ' ' | 发票号码 |
| 20 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 21 | fversion | 版本号： | varchar | 30 |  | √ | ' ' | 版本号：,枚举: 0 :旧版 1 :新版 |
| 22 | fsalertaxno | 销方税号 | varchar | 50 |  | √ | ' ' | 销方税号 |
| 23 | fmaintaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 25 | fbrandmodel | 厂牌型号 | varchar | 80 |  | √ | ' ' | 厂牌型号 |
| 26 | foriginalinvoiceno | 原发票号码 | varchar | 30 |  | √ | ' ' | 原发票号码 |
| 27 | fzerotaxmark | 零税率标识 | varchar | 30 |  | √ | ' ' | 零税率标识,枚举: 1 :免税 2 :不征税 3 :普通零税率 |
| 28 | fovertaxcode | 完税凭证号码 | varchar | 50 |  | √ | ' ' | 完税凭证号码 |
| 29 | forderno | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 30 | ftaxpremark | 税收优惠政策标识 | varchar | 30 |  | √ | ' ' | 税收优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 31 | fcommodityinspectionnum | 商检单号 | varchar | 50 |  | √ | ' ' | 商检单号 |
| 32 | fvehicletype | 车辆类型 | varchar | 50 |  | √ | ' ' | 车辆类型 |
| 33 | fissuesource | 开票来源 | varchar | 30 |  | √ | ' ' | 开票来源,枚举: 0 :税务ukey 1 :税控盘 2 :金税盘 3 :虚拟ukey 4 :托管 5 :区块链 |
| 34 | fabolishreason | 作废原因 | varchar | 50 |  | √ | ' ' | 作废原因 |
| 35 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 006 :机动车发票 |
| 36 | foriginalinvoicecode | 原发票代码 | varchar | 30 |  | √ | ' ' | 原发票代码 |
| 37 | ftaxauthorityname | 税务机关名称 | varchar | 50 |  | √ | ' ' | 税务机关名称 |
| 38 | fbillsource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: 1 :进项下载 2 :手工新增 3 :excel导入 4 :接口开票 5 :待开导入 |
| 39 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 40 | fissuetype | 开票类型： | varchar | 30 |  | √ | ' ' | 开票类型：,枚举: 0 :正数发票 1 :负数发票 |
| 41 | fissuestatus | 开票状态 | varchar | 30 |  | √ | ' ' | 开票状态,枚举: 2 :未开票 4 :已提交 1 :开票中 0 :开票成功 3 :开票失败 |
| 42 | fcheckcode | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 43 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 44 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 45 | fabolishtype | 作废类型 | varchar | 30 |  | √ | ' ' | 作废类型,枚举: 0 :发票作废 1 :空白作废 |
| 46 | fenginenum | 发动机编号 | varchar | 80 |  | √ | ' ' | 发动机编号 |
| 47 | ftotaltax | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 48 | fissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 49 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 50 | fprintflag | 打印标识 | varchar | 30 |  | √ | ' ' | 打印标识,枚举: 0 :未打印 1 :已打印 2 :打印失败 |
| 51 | fvehicleid | 车辆类型 | int8 | 64 |  | √ | 0 | [车辆信息管理 bdm_vehicle_info](../bdm_files/bdm_vehicle_info.md) |
| 52 | fskm | 多行文本 | varchar | 255 |  | √ | ' ' | 多行文本 |
| 53 | fbuyertaxno | 购方纳税人识别号 | varchar | 50 |  | √ | ' ' | 购方纳税人识别号 |
| 54 | fsalerbank | fsalerbank | varchar | 100 |  | √ | ' ' |  |
| 55 | fremark | 一车一票 | varchar | 250 |  | √ | ' ' | 一车一票 |
| 56 | finvalider | 作废人 | varchar | 50 |  | √ | ' ' | 作废人 |
| 57 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 58 | ftotalton | 吨位 | varchar | 50 |  | √ | ' ' | 吨位 |
| 59 | fsalerphone | 销方电话 | varchar | 30 |  | √ | ' ' | 销方电话 |
| 60 | fimportcertificate | 进口证明书号 | varchar | 50 |  | √ | ' ' | 进口证明书号 |
| 61 | fsaleraddress | 销方地址 | varchar | 100 |  | √ | ' ' | 销方地址 |
| 62 | foriginalissuetime | 原开票日期 | timestamp | 0 |  |  | null | 原开票日期 |
| 63 | fgoodscode | 税收分类编码 | varchar | 30 |  | √ | ' ' | 税收分类编码 |
| 64 | flimitepeople | 限乘人数 | varchar | 50 |  | √ | ' ' | 限乘人数 |
| 65 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 66 | fproducingarea | 产地 | varchar | 30 |  | √ | ' ' | 产地 |
| 67 | fproxymark | 代开标识 | varchar | 30 |  | √ | ' ' | 代开标识,枚举: 0 :默认 1 :代开 |
| 68 | fjqbh | 设备信息： | varchar | 50 |  | √ | ' ' | 设备信息：,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invoice_vehicles_billno |  | forgid,fbillno |
| 2 | idx_invoice_vehicles_code |  | finvoicecode,finvoiceno |
| 3 | idx_invoice_vehicles_issuetime |  | fissuetime |
| 4 | pk_t_sim_vatinvoice_vehicles |  | fid |
