# 尾盘调整明细-tcret_tdzzswp_adj_de

## 尾盘调整明细-主表 t_tcret_tdzzswp_adj_de

- **表名称：** 尾盘调整明细-主表
- **表名：** t_tcret_tdzzswp_adj_de

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyjxmid | 项目id | int8 | 64 |  | √ | 0 | 项目id |
| 3 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 4 | ftaxitem | 税目名称 | varchar | 50 |  | √ | ' ' | 税目名称 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | 总额 | numeric | 23 | 10 | √ | 0 | 总额 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fadjustexplain | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 9 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 10 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0 | 调整额 |
| 11 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 12 | frowindex | 调整行 | int8 | 64 |  | √ | 0 | 调整行 |
| 13 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 14 | fcolumntype | 调整列 | varchar | 50 |  | √ | ' ' | 调整列,枚举: hbsr :货币收入 swjqtsr :实物收入及其他收入 stxssr :视同销售收入 |
| 15 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 16 | fitemname | 项目名称 | varchar | 200 |  | √ | ' ' | 项目名称 |
| 17 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzswp_adj_de |  | forgid,fskssqz,fskssqq |
| 2 | pk_tcret_tdzzswp_adj_de |  | fid |
