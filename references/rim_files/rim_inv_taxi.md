# 出租车票-rim_inv_taxi

## 出租车票-主表 t_rim_inv_taxi

- **表名称：** 出租车票-主表
- **表名：** t_rim_inv_taxi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | fplace | 地名 | varchar | 50 |  | √ | ' ' | 地名 |
| 4 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 5 | ftime_get_on | 上车时间 | varchar | 10 |  | √ | ' ' | 上车时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | ftime_get_off | 下车时间 | varchar | 10 |  | √ | ' ' | 下车时间 |
| 10 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 11 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 12 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 13 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftotal_amount | 打车金额 | numeric | 23 | 10 | √ | 0.0000000000 | 打车金额 |
| 16 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 17 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | finvoice_date | 乘车日期 | timestamp | 0 |  |  | null | 乘车日期 |
| 20 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 21 | fmileage | 里程 | numeric | 23 | 10 | √ | 0.0000000000 | 里程 |
| 22 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 26 | fexpense_status | 报销状态 | varchar | 2 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 27 | foriginal_state | 原件签收状态 | varchar | 2 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 28 | flicense_number | 车牌号 | varchar | 20 |  | √ | ' ' | 车牌号 |
| 29 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 30 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_inv_taxi |  | fid |
| 2 | idx_rim_inv_taxi_taxorg |  | ftax_org,finvoice_date |
| 3 | idx_rim_inv_taxi |  | fserial_no |
| 4 | idx_rim_inv_taxi_no |  | finvoice_code,finvoice_no |
