# 机动车发票-tdm_input_vehicle_invoice

## 机动车发票-分表 t_tdm_input_vehicle_inv_a

- **表名称：** 机动车发票-分表
- **表名：** t_tdm_input_vehicle_inv_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxperiod | 发票采集所属税期 | varchar | 20 |  | √ | ' ' | 发票采集所属税期 |
| 3 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 4 | fisgeneratevoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 5 | fcheckcode | 校验码 | varchar | 100 |  | √ | ' ' | 校验码 |
| 6 | ftaxperioddate | 税期所属日期 | timestamp | 0 |  |  | null | 税期所属日期 |
| 7 | ftotalton | 吨位 | varchar | 20 |  | √ | ' ' | 吨位 |
| 8 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 9 | fovertaxcode | 完税凭证号码 | varchar | 30 |  | √ | ' ' | 完税凭证号码 |
| 10 | fcertstatus | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未认证 1 :勾选认证 2 :扫描认证 |
| 11 | ftaxauthoritycode | 税务机关代码 | varchar | 100 |  | √ | ' ' | 税务机关代码 |
| 12 | fselectresult | 勾选结果 | varchar | 50 |  | √ | ' ' | 勾选结果,枚举: 0 :- 1 :抵扣 2 :不抵扣 |
| 13 | ftaxauthorityname | 税务机关名称 | varchar | 100 |  | √ | ' ' | 税务机关名称 |
| 14 | fauthdate | 认证日期 | timestamp | 0 |  |  | null | 认证日期 |
| 15 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 16 | fsignstatus | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: 1 :已签收 0 :未签收 |
| 17 | fselectstatus | 勾选状态 | varchar | 50 |  | √ | ' ' | 勾选状态,枚举: 1 :已勾选 0 :未勾选 |
| 18 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 19 | fsenddate | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_vehicle_inv_a |  | ftaxperiod |
| 2 | t_tdm_input_vehicle_inv_a_pkey |  | fid |

---

## 机动车发票-主表 t_tdm_input_vehicle_inv

- **表名称：** 机动车发票-主表
- **表名：** t_tdm_input_vehicle_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawer | 开票人 | varchar | 16 |  | √ | ' ' | 开票人 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 6 | fbuyercardno | 买方身份证号/组织机构代码 | varchar | 200 |  | √ | ' ' | 买方身份证号/组织机构代码 |
| 7 | fcertificatenum | 合格证号 | varchar | 64 |  | √ | ' ' | 合格证号 |
| 8 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 2 :勾选认证 3 :扫描认证 4 :未认证 0 :未勾选 1 :勾选 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsaleraccount | 销方银行帐号 | varchar | 300 |  | √ | ' ' | 销方银行帐号 |
| 11 | fmachineno | 机器编号 | varchar | 60 |  | √ | ' ' | 机器编号 |
| 12 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 13 | fsalerbankname | 销方开户银行 | varchar | 100 |  | √ | ' ' | 销方开户银行 |
| 14 | finvoicecode | 发票代码 | varchar | 64 |  | √ | ' ' | 发票代码 |
| 15 | fbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 16 | finvoiceno | 发票号码 | varchar | 64 |  | √ | ' ' | 发票号码 |
| 17 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 18 | fsalertaxno | 销方税号 | varchar | 40 |  | √ | ' ' | 销方税号 |
| 19 | fvehicleidenticode | 车辆识别代码 | varchar | 64 |  | √ | ' ' | 车辆识别代码 |
| 20 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fbrandmodel | 厂牌型号 | varchar | 160 |  | √ | ' ' | 厂牌型号 |
| 23 | foriginalinvoiceno | 原发票号码 | varchar | 64 |  | √ | ' ' | 原发票号码 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fvehicletype | 车辆类型 | varchar | 60 |  | √ | ' ' | 车辆类型 |
| 26 | fcommodityinspectionnum | 商检单号 | varchar | 64 |  | √ | ' ' | 商检单号 |
| 27 | foriginalinvoicecode | 原发票代码 | varchar | 64 |  | √ | ' ' | 原发票代码 |
| 28 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 31 | feffectivetaxamount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 32 | fenginenum | 发动机编号 | varchar | 112 |  | √ | ' ' | 发动机编号 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fopentype | 开票类型 | varchar | 30 |  | √ | ' ' | 开票类型,枚举: 0 :蓝字发票 1 :红字发票 |
| 35 | fscanauthenticatetime | 扫描认证时间 | timestamp | 0 |  |  | null | 扫描认证时间 |
| 36 | fselecttime | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 37 | finvoicedata | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 38 | fbuyertaxno | 购方税号 | varchar | 40 |  | √ | ' ' | 购方税号 |
| 39 | fremark | 备注 | varchar | 480 |  | √ | ' ' | 备注 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fsalerphone | 销方电话 | varchar | 60 |  | √ | ' ' | 销方电话 |
| 43 | fimportcertificate | 进口证明书号 | varchar | 64 |  | √ | ' ' | 进口证明书号 |
| 44 | fsaleraddress | 销方地址 | varchar | 100 |  | √ | ' ' | 销方地址 |
| 45 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 12 :机动车销售统一发票 |
| 46 | flimitepeople | 限乘人数 | varchar | 20 |  | √ | ' ' | 限乘人数 |
| 47 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 48 | fproducingarea | 产地 | varchar | 60 |  | √ | ' ' | 产地 |
| 49 | fproxymark | 代开标识 | varchar | 30 |  | √ | ' ' | 代开标识,枚举: 0 :默认 1 :代开 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_vehicle_inv |  | forgid,finvoicecode,finvoiceno |
| 2 | t_tdm_input_vehicle_inv_pkey |  | fid |
