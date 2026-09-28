# 火车票-tdm_input_train

## 火车票-主表 t_tdm_input_train

- **表名称：** 火车票-主表
- **表名：** t_tdm_input_train

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprintingsequenceno | 印刷序号 | varchar | 64 |  | √ | ' ' | 印刷序号 |
| 3 | faccountsperiod | 记账期间 | varchar | 50 |  | √ | ' ' | 记账期间 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | ftaxperioddate | 税期所属日期 | timestamp | 0 |  |  | null | 税期所属日期 |
| 6 | ftotalamount | 票价 | numeric | 23 | 10 | √ | 0.0000000000 | 票价 |
| 7 | ftaxtotalamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 8 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpassengername | 乘客姓名 | varchar | 40 |  | √ | ' ' | 乘客姓名 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | faccountssign | 记账标识 | varchar | 30 |  | √ | ' ' | 记账标识,枚举: 是 :是 否 :否 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftraintime | 乘车时间 | varchar | 20 |  | √ | ' ' | 乘车时间 |
| 16 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 17 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 18 | finvoicedate | 乘车日期 | timestamp | 0 |  |  | null | 乘车日期 |
| 19 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 20 | fstationgeton | 上车站点 | varchar | 20 |  | √ | ' ' | 上车站点 |
| 21 | fupdatedate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 22 | ftaxperiod | 所属税期 | varchar | 20 |  | √ | ' ' | 所属税期 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fisgeneratevoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 29 | ftrainnum | 车次 | varchar | 20 |  | √ | ' ' | 车次 |
| 30 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 9 :火车票 |
| 31 | fstationgetoff | 下车站点 | varchar | 20 |  | √ | ' ' | 下车站点 |
| 32 | fseat | 座位等级 | varchar | 20 |  | √ | ' ' | 座位等级 |
| 33 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_train |  | forg,ftaxperiod |
| 2 | t_tdm_input_train_pkey |  | fid |
