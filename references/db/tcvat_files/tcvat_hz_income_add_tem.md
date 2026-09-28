# 总机构进项税额加计抵减模板-tcvat_hz_income_add_tem

## 总机构进项税额加计抵减模板-主表 t_tcvat_hz_income_add_tem

- **表名称：** 总机构进项税额加计抵减模板-主表
- **表名：** t_tcvat_hz_income_add_tem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 3 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcurrentdecrease | 本期调减额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期调减额 |
| 6 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 7 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 8 | fservicetype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 9 | frowno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 10 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_hz_income_add_tem |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_hz_income_add_tem |  | fid |
