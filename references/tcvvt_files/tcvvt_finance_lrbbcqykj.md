# 利润表补充资料（企业会计）-tcvvt_finance_lrbbcqykj

## 利润表补充资料（企业会计）-主表 t_tcvvt_finance_lrbbcqykj

- **表名称：** 利润表补充资料（企业会计）-主表
- **表名：** t_tcvvt_finance_lrbbcqykj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbnljsy | 本年累计数.一 | numeric | 23 | 10 | √ | 0 | 本年累计数.一 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1．出售、处置部门或被投资单位所得收益 2 :2．自然灾害发生的损失 3 :3．会计政策变更增加(或减少)利润总额 4 :4．会计估计变更增加(或减少)利润总额 5 :5．债务重组损失 6 :6．其他 |
| 4 | fbnljse | 本年累计数.二 | numeric | 23 | 10 | √ | 0 | 本年累计数.二 |
| 5 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 6 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 7 | fsnsjs | 上年实际数 | numeric | 23 | 10 | √ | 0 | 上年实际数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_finance_lrbbcqykj |  | fid |
| 2 | idx_tcvvt_finance_lrbbcqykj_1 |  | fsbbid |
| 3 | idx_tcvvt_finance_lrbbcqykj |  | fewblxh,fsbbid |
