# 预缴信息-tdm_tdzzs_prepayment_info

## 预缴信息-主表 t_tdm_tdzzs_prepay_info

- **表名称：** 预缴信息-主表
- **表名：** t_tdm_tdzzs_prepay_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbuildingtype | 房产类型 | int8 | 64 |  | √ | 0 | 业务定义 tpo_tdzzs_bizdef |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fprelevyrate | 预征率 | numeric | 23 | 10 | √ | 0 | 预征率 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fsubbuildingtype | 房产类型子目 | int8 | 64 |  | √ | 0 | 业务定义 tpo_tdzzs_bizdef |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tdzzs_prepay_info |  | fentryid |
| 2 | idx_t_tdm_tdzzs_prepay_info_1 |  | fid |
