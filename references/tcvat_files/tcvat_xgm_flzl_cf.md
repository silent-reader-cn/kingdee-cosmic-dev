# 小规模附列资料拆分表-tcvat_xgm_flzl_cf

## 小规模附列资料拆分表-主表 t_tcvat_xgm_flzl_cf

- **表名称：** 小规模附列资料拆分表-主表
- **表名：** t_tcvat_xgm_flzl_cf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: qcye :1.期初余额3% bqfse :2.本期发生额3% bqkce :3.本期扣除额3% qmye :4.期末余额3% qbhssr :5.全部含税收入3% hsxse :7.含税销售额3% bhsxse :8.不含税销售额3% qcye1 :1.期初余额3%-初始值 bqfse1 :2.本期发生额3%-初始值 bqkce1 :3.本期扣除额3%-初始值 qmye1 :4.期末余额3%-初始值 qbhssr1 :5.全部含税收入3%-初始值 hsxse1 :7.含税销售额3%-初始值 bhsxse1 :8.不含税销售额3%-初始值 |
| 3 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 4 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 5 | fje3 | 3%金额 | numeric | 23 | 10 | √ | 0 | 3%金额 |
| 6 | fje1 | 1%金额 | numeric | 23 | 10 | √ | 0 | 1%金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_xgm_flzl_cf_sbb |  | fsbbid,fewblxh |
| 2 | pk_tcvat_xgm_flzl_cf |  | fid |
