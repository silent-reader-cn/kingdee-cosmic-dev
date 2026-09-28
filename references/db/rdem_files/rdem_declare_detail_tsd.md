# 底稿体系数据子表(多维数据表)-rdem_declare_detail_tsd

## 底稿体系数据子表(多维数据表)-主表 t_rdem_declare_detail_tsd

- **表名称：** 底稿体系数据子表(多维数据表)-主表
- **表名：** t_rdem_declare_detail_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | varchar | 1000 |  | √ | ' ' | 值 |
| 3 | fdynrowno | 动态行标识 | varchar | 200 |  | √ | ' ' | 动态行标识 |
| 4 | frow | 行维 | int8 | 64 |  | √ | 0 | [行维成员管理 rdem_row_member](../rdem_files/rdem_row_member.md) |
| 5 | findex | 动态行所在行数 | int8 | 64 |  | √ | 0 | 动态行所在行数 |
| 6 | fcolumn | 列维 | int8 | 64 |  | √ | 0 | [列维成员管理 rdem_col_member](../rdem_files/rdem_col_member.md) |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fvaluetype | 值类型 | varchar | 50 |  | √ | ' ' | 值类型 |
| 9 | fentryid | 底稿id（外键） | int8 | 64 |  | √ | 0 | 底稿id（外键） |
| 10 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 11 | fcellnumber | 报表项标识 | varchar | 128 |  | √ | ' ' | 报表项标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_declare_detail_tsd_m0 |  | fcolumn |
| 2 | pk_rdem_declare_detail_tsd |  | fid |
