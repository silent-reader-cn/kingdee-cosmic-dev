# 风险报告数据-scrim_riskreportdata

## 风险报告数据-主表 t_scrim_riskreportdata

- **表名称：** 风险报告数据-主表
- **表名：** t_scrim_riskreportdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | friskreport_tag | 风险报告_详情 | text | 0 |  |  | null | 风险报告_详情 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | frisklevel | 风险等级 | varchar | 50 |  | √ | ' ' | 风险等级 |
| 5 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 7 | friskreport | 风险报告 | varchar | 255 |  | √ | ' ' | 风险报告 |
| 8 | fentityid | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_scrim_riskrptdata_bill |  | fentityid,fbillid |
| 2 | pk_t_scrim_riskreportdata |  | fid |
