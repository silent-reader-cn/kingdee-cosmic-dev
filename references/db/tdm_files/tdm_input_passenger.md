# 客运票-tdm_input_passenger

## 客运票-主表 t_tdm_input_passenger

- **表名称：** 客运票-主表
- **表名：** t_tdm_input_passenger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountsperiod | 记账期间 | varchar | 50 |  | √ | ' ' | 记账期间 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | ftaxperioddate | 税期所属日期 | timestamp | 0 |  |  | null | 税期所属日期 |
| 5 | ftotalamount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 6 | ftaxtotalamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 7 | fticketcreatetime | 创建时间(票据) | timestamp | 0 |  |  | null | 创建时间(票据) |
| 8 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fpassengername | 乘客姓名 | varchar | 40 |  | √ | ' ' | 乘客姓名 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | faccountssign | 记账标识 | varchar | 30 |  | √ | ' ' | 记账标识,枚举: |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 15 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 16 | finvoicecode | 发票代码 | varchar | 64 |  | √ | ' ' | 发票代码 |
| 17 | fseatno | 座位号 | varchar | 20 |  | √ | ' ' | 座位号 |
| 18 | finvoicedata | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 19 | finvoiceno | 发票号码 | varchar | 64 |  | √ | ' ' | 发票号码 |
| 20 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 21 | fstationgeton | 上车站点 | varchar | 20 |  | √ | ' ' | 上车站点 |
| 22 | fcurrencytype | 币种 | varchar | 20 |  | √ | ' ' | 币种 |
| 23 | ftime | 乘车时间 | varchar | 40 |  | √ | ' ' | 乘车时间 |
| 24 | ftaxperiod | 所属税期 | varchar | 20 |  | √ | ' ' | 所属税期 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fisgeneratevoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 31 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 16 :客运票 20 :轮船票 |
| 32 | fstationgetoff | 下车站点 | varchar | 20 |  | √ | ' ' | 下车站点 |
| 33 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_input_passenger_pkey |  | fid |
| 2 | idx_tdm_input_passenger |  | forg,ftaxperiod |
