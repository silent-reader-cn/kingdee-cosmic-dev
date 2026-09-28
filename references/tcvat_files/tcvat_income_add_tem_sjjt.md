# 一般纳税人计提进项税额加计抵减模板-tcvat_income_add_tem_sjjt

## 一般纳税人计提进项税额加计抵减模板-主表 t_tcvat_income_add_tem_jt

- **表名称：** 一般纳税人计提进项税额加计抵减模板-主表
- **表名：** t_tcvat_income_add_tem_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcurrentdecrease | 本期调减额 | numeric | 23 | 10 | √ | 0 | 本期调减额 |
| 5 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 6 | fservicetype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 7 | frowno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 8 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_income_add_tem_jt |  | fid |
| 2 | idx_income_add_tem_serialno |  | forgid,ftaxperiod |
