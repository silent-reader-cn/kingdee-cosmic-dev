# 飞机票_继承-tdm_input_ariport_inh

## 飞机票_继承-主表 t_tdm_input_airport

- **表名称：** 飞机票_继承-主表
- **表名：** t_tdm_input_airport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountsperiod | 记账期间 | varchar | 50 |  | √ | ' ' | 记账期间 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | ftaxperioddate | 税期所属日期 | timestamp | 0 |  |  | null | 税期所属日期 |
| 5 | ftotalamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 6 | fsalesunitcode | 销售单位代码 | varchar | 64 |  | √ | ' ' | 销售单位代码 |
| 7 | ftaxtotalamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 8 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcarrier | 承运人 | varchar | 64 |  | √ | ' ' | 承运人 |
| 12 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | faccountssign | 记账标识 | varchar | 30 |  | √ | ' ' | 记账标识,枚举: |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0.0000000000 | 燃油附加费 |
| 17 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 18 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 19 | fflight_num | 航班号 | varchar | 64 |  | √ | ' ' | 航班号 |
| 20 | finvoicedate | 乘机日期 | timestamp | 0 |  |  | null | 乘机日期 |
| 21 | fairnum | 机票编号 | varchar | 64 |  | √ | ' ' | 机票编号 |
| 22 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 23 | fprintnum | 印刷序列号 | varchar | 64 |  | √ | ' ' | 印刷序列号 |
| 24 | felectronicticketnum | 电子客票号码 | varchar | 64 |  | √ | ' ' | 电子客票号码 |
| 25 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fisgeneratevoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 28 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fcustomername | 顾客姓名 | varchar | 40 |  | √ | ' ' | 顾客姓名 |
| 31 | fdestination | 目的地 | varchar | 64 |  | √ | ' ' | 目的地 |
| 32 | fseatgrade | 座位等级 | varchar | 20 |  | √ | ' ' | 座位等级 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fplaceofdeparture | 出发地 | varchar | 64 |  | √ | ' ' | 出发地 |
| 35 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 36 | fissuedate | 机票填开日期 | timestamp | 0 |  |  | null | 机票填开日期 |
| 37 | fairtime | 乘机时间 | varchar | 64 |  | √ | ' ' | 乘机时间 |
| 38 | fcustomeridentitynum | 身份证号 | varchar | 60 |  | √ | ' ' | 身份证号 |
| 39 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 10 :飞机票 |
| 40 | fairportconstructionfee | 机场建设费 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费 |
| 41 | ffillingunit | 填开单位 | varchar | 200 |  | √ | ' ' | 填开单位 |
| 42 | finvoiceamount | 票价 | numeric | 23 | 10 | √ | 0.0000000000 | 票价 |
| 43 | fothertax | 其他税费(注：不是税额) | numeric | 23 | 10 | √ | 0.0000000000 | 其他税费(注：不是税额) |
| 44 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 45 | fendorsement | 签注 | varchar | 64 |  | √ | ' ' | 签注 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_airport |  | forg,ftaxperiod |
| 2 | t_tdm_input_airport_pkey |  | fid |

---

## 单据体-子表 t_tdm_input_air_msg

- **表名称：** 单据体-子表
- **表名：** t_tdm_input_air_msg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsg_seatgrade | 座位等级 | varchar | 20 |  | √ | ' ' | 座位等级 |
| 3 | fmsg_invoicedate | 乘机日期 | timestamp | 0 |  |  | null | 乘机日期 |
| 4 | fmsg_placeofdeparture | 出发地 | varchar | 64 |  | √ | ' ' | 出发地 |
| 5 | fflight_num | 航班号 | varchar | 64 |  | √ | ' ' | 航班号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmsg_takeplanetime | 乘机时间 | varchar | 20 |  | √ | ' ' | 乘机时间 |
| 8 | fmsg_destination | 目的地 | varchar | 64 |  | √ | ' ' | 目的地 |
| 9 | fmsg_createdate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmsg_carrier | 承运人 | varchar | 64 |  | √ | ' ' | 承运人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_air_msg_fk |  | fid |
| 2 | t_tdm_input_air_msg_pkey |  | fentryid |
