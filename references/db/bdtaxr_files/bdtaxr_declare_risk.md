# 申报风险事项单-bdtaxr_declare_risk

## 申报风险事项单-主表 t_bdtaxr_declare_risk

- **表名称：** 申报风险事项单-主表
- **表名：** t_bdtaxr_declare_risk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | friskresolveid | 风险处理id | int8 | 64 |  | √ | 0 | 风险处理id |
| 3 | fitemtype | 事项类型 | varchar | 50 |  | √ | ' ' | 事项类型,枚举: 1 :申报事项 2 :风险事项 |
| 4 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 5 | fitemname | 事项名称 | varchar | 1000 |  | √ | ' ' | 事项名称 |
| 6 | friskdesc | 风险说明 | varchar | 2000 |  | √ | ' ' | 风险说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_declare_risk |  | fid |
| 2 | idx_t_bdtaxr_declare_risk_sbid |  | fsbbid |
