# 成本主体类别关系-cal_costattype_relation

## 成本主体类别关系-主表 t_cal_costaccount_type

- **表名称：** 成本主体类别关系-主表
- **表名：** t_cal_costaccount_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 2 | fbasedataid | 成本主体类别 | int8 | 64 |  | √ | 0 | 成本主体类别 cal_bd_costaccounttype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costaccount_type_pkey |  | fpkid |
| 2 | idx_cal_costaccount_type_fid |  | fid |
