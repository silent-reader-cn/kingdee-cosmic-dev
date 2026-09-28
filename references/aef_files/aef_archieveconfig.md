# 归档配置记录-aef_archieveconfig

## 归档配置记录-主表 t_aef_archiveconfig

- **表名称：** 归档配置记录-主表
- **表名：** t_aef_archiveconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchcode | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 3 | fisneedattachfile | 是否归档附件 | bpchar | 1 |  | √ | '0' | 是否归档附件,枚举: 1 :是 0 :否 |
| 4 | farchiverange | 归档范围 | varchar | 500 |  | √ | ' ' | 归档范围 |
| 5 | farchiverange_tag | 归档范围_详情 | text | 0 |  |  | null | 归档范围_详情 |
| 6 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_archiveconfig |  | fid |
| 2 | idx_aef_archiveconfig |  | fbatchcode |
