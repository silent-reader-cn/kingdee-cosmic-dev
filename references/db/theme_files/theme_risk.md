# 主题风险单据-theme_risk

## 主题风险单据-主表 t_theme_risk

- **表名称：** 主题风险单据-主表
- **表名：** t_theme_risk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | frisk_type_name | 风险类型名称 | varchar | 50 |  | √ | ' ' | 风险类型名称 |
| 6 | fanalysis_table_code | 分析表 | varchar | 50 |  | √ | ' ' | 分析表 |
| 7 | fanalysis_table_name | 分析表名称 | varchar | 50 |  | √ | ' ' | 分析表名称 |
| 8 | frisk_type | 风险类型 | varchar | 50 |  | √ | ' ' | 风险类型 |
| 9 | fipo_org | IPO主体 | int8 | 64 |  |  | null | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 10 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | frisk_desc | 风险描述 | varchar | 50 |  | √ | ' ' | 风险描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_risk_name |  | fanalysis_table_name,forgfield |
| 2 | pk_theme_risk |  | fid |
