# 印花税计提调整明细-tcret_yhsjt_adjust

## 印花税计提调整明细-主表 t_tcret_yhsjt_adjust

- **表名称：** 印花税计提调整明细-主表
- **表名：** t_tcret_yhsjt_adjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 4 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | 总额 | numeric | 23 | 10 | √ | 0 | 总额 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fadjustexplain | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 9 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 10 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0 | 调整额 |
| 11 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 12 | fsubtaxitem | 子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 13 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 14 | fitemname | fitemname | varchar | 200 |  | √ | ' ' |  |
| 15 | fbizdimensionid | 业务维度值ID | int8 | 64 |  | √ | 0 | 业务维度值ID |
| 16 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_yhsjt_adjust |  | fid |
| 2 | idx_t_tcret_yhsjt_adjust_0 |  | forgid,fskssqq,fskssqz |
