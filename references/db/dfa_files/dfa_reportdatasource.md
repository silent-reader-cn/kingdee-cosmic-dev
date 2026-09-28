# 报告数据来源-dfa_reportdatasource

## 报告数据来源-主表 t_dfa_reportdatasource

- **表名称：** 报告数据来源-主表
- **表名：** t_dfa_reportdatasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcedata_tag | 来源数据_详情 | text | 0 |  |  | null | 来源数据_详情 |
| 3 | freportid | 报告id | int8 | 64 |  | √ | 0 | 报告id |
| 4 | fsourcedesc | 来源数据简述 | varchar | 50 |  | √ | ' ' | 来源数据简述 |
| 5 | fsourcetype | 来源数据类型 | varchar | 10 |  | √ | ' ' | 来源数据类型 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsourcedata | 来源数据 | varchar | 255 |  | √ | ' ' | 来源数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_dsreportid |  | freportid |
| 2 | pk_dfa_reportds |  | fid |
