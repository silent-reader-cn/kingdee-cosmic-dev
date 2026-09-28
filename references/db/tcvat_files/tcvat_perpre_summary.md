# 分次预缴底稿单据-tcvat_perpre_summary

## 分次预缴底稿单据-主表 t_tcvat_perpre_summary

- **表名称：** 分次预缴底稿单据-主表
- **表名：** t_tcvat_perpre_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 5 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 9 | fperpreproject | 分次预缴项目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 10 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 11 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 12 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 13 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 14 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 15 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_perpre_summary |  | fid |
| 2 | idx_taxc_perpre_sum_org_date |  | forgid,ftaxperiod,fdeadline |
| 3 | idx_taxc_perpre_sum_serialno |  | fserialno |
