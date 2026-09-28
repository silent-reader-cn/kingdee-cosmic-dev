# 进项待抵扣抵扣台账单据-tcvat_wait_deduct_summary

## 进项待抵扣抵扣台账单据-主表 t_tcvat_waitdeduc_summary

- **表名称：** 进项待抵扣抵扣台账单据-主表
- **表名：** t_tcvat_waitdeduc_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 4 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fcount | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 9 | fdeductiontype | 抵扣类型 | int8 | 64 |  | √ | 0 | 业务定义 tpo_tcvat_bizdef |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_waitdeduc_summa_1 |  | forgid,fserialno |
| 2 | pk_tcvat_waitdeduc_summary |  | fid |
