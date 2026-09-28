# 二手车发票-tdm_input_secondcar

## 二手车发票-主表 t_tdm_input_secondcar

- **表名称：** 二手车发票-主表
- **表名：** t_tdm_input_secondcar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmarkettaxpayerid | 二手市场税号 | varchar | 60 |  | √ | ' ' | 二手市场税号 |
| 3 | fdrawer | 开票人 | varchar | 40 |  | √ | ' ' | 开票人 |
| 4 | fsalerphonenumber | 销方电话 | varchar | 60 |  | √ | ' ' | 销方电话 |
| 5 | fsaleridno | 销方组织代码/身份证号码 | varchar | 60 |  | √ | ' ' | 销方组织代码/身份证号码 |
| 6 | fmarketphonenumber | 二手市场电话 | varchar | 60 |  | √ | ' ' | 二手市场电话 |
| 7 | fcheckcode | 校验码 | varchar | 60 |  | √ | ' ' | 校验码 |
| 8 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 9 | ftotalamount | 车价合计 | numeric | 23 | 10 | √ | 0.0000000000 | 车价合计 |
| 10 | fauctionphonenumber | 拍卖/经营电话 | varchar | 60 |  | √ | ' ' | 拍卖/经营电话 |
| 11 | fbuyeraddress | 购方地址 | varchar | 300 |  | √ | ' ' | 购方地址 |
| 12 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fvehiclemanagementname | 转入地车辆管理所名称 | varchar | 100 |  | √ | ' ' | 转入地车辆管理所名称 |
| 14 | fissuingoffice | 开票单位 | varchar | 100 |  | √ | ' ' | 开票单位 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fmarketbankaccout | 二手市场开户银行帐号 | varchar | 200 |  | √ | ' ' | 二手市场开户银行帐号 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmachineno | 机器编号 | varchar | 100 |  | √ | ' ' | 机器编号 |
| 19 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 20 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 21 | fvehicleidentificationno | 车辆识别代码/车驾号码 | varchar | 60 |  | √ | ' ' | 车辆识别代码/车驾号码 |
| 22 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 23 | fbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 24 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 25 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 26 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbandmodel | 厂牌型号 | varchar | 60 |  | √ | ' ' | 厂牌型号 |
| 29 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fbuyerphonenumber | 购方电话 | varchar | 60 |  | √ | ' ' | 购方电话 |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | flicenseplatenumber | 车牌照号 | varchar | 40 |  | √ | ' ' | 车牌照号 |
| 33 | fauctionaddress | 拍卖/经营地址 | varchar | 100 |  | √ | ' ' | 拍卖/经营地址 |
| 34 | fauctiontaxpayerid | 拍卖/经营税号 | varchar | 60 |  | √ | ' ' | 拍卖/经营税号 |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | fbuyeridno | 购方组织代码/身份证号码 | varchar | 60 |  | √ | ' ' | 购方组织代码/身份证号码 |
| 37 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 38 | fsaleraddress | 销方地址 | varchar | 300 |  | √ | ' ' | 销方地址 |
| 39 | fvehicletype | 车辆类型 | varchar | 60 |  | √ | ' ' | 车辆类型 |
| 40 | fmarketname | 二手市场单位 | varchar | 200 |  | √ | ' ' | 二手市场单位 |
| 41 | fauctionname | 拍卖/经营名称 | varchar | 100 |  | √ | ' ' | 拍卖/经营名称 |
| 42 | fsaler_name | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 43 | fmarketaddress | 二手市场地址 | varchar | 200 |  | √ | ' ' | 二手市场地址 |
| 44 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 13 :二手车发票 |
| 45 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 46 | fregistrationnumber | 登记证号 | varchar | 60 |  | √ | ' ' | 登记证号 |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fauctionbankaccout | 拍卖/经营开户银行帐号 | varchar | 200 |  | √ | ' ' | 拍卖/经营开户银行帐号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_input_secondcar_pkey |  | fid |
| 2 | idx_tdm_input_secondcar |  | forg,finvoicecode,finvoiceno |
