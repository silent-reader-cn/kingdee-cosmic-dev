# 的士票-tdm_input_taxi

## 的士票-主表 t_tdm_input_taxi

- **表名称：** 的士票-主表
- **表名：** t_tdm_input_taxi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalamount | 打车金额 | numeric | 23 | 10 | √ | 0.0000000000 | 打车金额 |
| 3 | fplace | 乘车地地名 | varchar | 40 |  | √ | ' ' | 乘车地地名 |
| 4 | fticketcreatetime | 创建时间(票据) | timestamp | 0 |  |  | null | 创建时间(票据) |
| 5 | flicensenumber | 车牌号 | varchar | 24 |  | √ | ' ' | 车牌号 |
| 6 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 7 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 11 | finvoicedate | 乘车日期 | timestamp | 0 |  |  | null | 乘车日期 |
| 12 | finvoicecode | 发票代码 | varchar | 24 |  | √ | ' ' | 发票代码 |
| 13 | finvoiceno | 发票号码 | varchar | 16 |  | √ | ' ' | 发票号码 |
| 14 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fmileage | 里程 | numeric | 23 | 10 | √ | 0.0000000000 | 里程 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 21 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 8 :的士票 |
| 22 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 23 | ftimegetoff | 下车时间 | varchar | 20 |  | √ | ' ' | 下车时间 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | ftimegeton | 上车时间 | varchar | 20 |  | √ | ' ' | 上车时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_taxi |  | forg,finvoicecode,finvoiceno |
| 2 | t_tdm_input_taxi_pkey |  | fid |
