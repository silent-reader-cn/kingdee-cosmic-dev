# 水利基金预缴底稿取数明细-totf_wafund_accunt_detail

## 水利基金预缴底稿取数明细-主表 t_totf_wafund_accunt_deta

- **表名称：** 水利基金预缴底稿取数明细-主表
- **表名：** t_totf_wafund_accunt_deta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjustamount | 调整数值 | numeric | 23 | 10 | √ | 0 | 调整数值 |
| 3 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | ftzsm | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 5 | fprepaytype | 预缴项目类型 | varchar | 50 |  | √ | ' ' | 预缴项目类型,枚举: VAT_YJXMLX_001 :异地建筑服务 VAT_YJXMLX_002 :建筑服务预收款 VAT_YJXMLX_003 :房地产项目预售 VAT_YJXMLX_004 :不动产转让 VAT_YJXMLX_005 :异地不动产出租 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftotalamount | 总数 | numeric | 23 | 10 | √ | 0 | 总数 |
| 8 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 9 | ftaxorgid | 取数组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | famount | 数值 | numeric | 23 | 10 | √ | 0 | 数值 |
| 11 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_accunt_detail_no_org_date |  | ftaxaccountserialno,forgid,fskssqq,fskssqz |
| 2 | pk_totf_wafund_accunt_deta |  | fid |
