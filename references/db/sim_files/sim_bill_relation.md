# 单据关系表-sim_bill_relation

## 单据关系表-主表 t_sim_bill_relation

- **表名称：** 单据关系表-主表
- **表名：** t_sim_bill_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftbillid | 目标单id | int8 | 64 |  | √ | 0 | 目标单id |
| 3 | frelationtype | 关系类型 | varchar | 30 |  | √ | ' ' | 关系类型,枚举: 0 :普通 1 :重开 |
| 4 | fsbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 5 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_bill_relation |  | fid |
| 2 | idx_sim_bill_tbillid |  | ftbillid |
| 3 | idx_sim_bill_sbillid |  | fsbillid |
