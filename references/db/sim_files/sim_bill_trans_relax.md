# 单据转换关系实体(旧)-sim_bill_trans_relax

## 单据转换关系实体(旧)-主表 t_sim_bill_trans_relax

- **表名称：** 单据转换关系实体(旧)-主表
- **表名：** t_sim_bill_trans_relax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfirmbillid | 已确认单据id | int8 | 64 |  | √ | 0 | 已确认单据id |
| 3 | fchangedate | 关系转换时间 | timestamp | 0 |  |  | null | 关系转换时间 |
| 4 | fbillid | 原单据id | int8 | 64 |  | √ | 0 | 原单据id |
| 5 | fchangestate | 关系状态 | varchar | 50 |  | √ | ' ' | 关系状态,枚举: 0 :有效 1 :撤回（已确认单据有开票信息） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_bill_trans_relax |  | fid |
| 2 | idx_sim_bill_trans_relax |  | fconfirmbillid |
