# 分析框架-dfa_rptframework

## 分析框架-主表 t_dfa_rptframework

- **表名称：** 分析框架-主表
- **表名：** t_dfa_rptframework

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fframework_tag | 报告框架_详情 | text | 0 |  |  | null | 报告框架_详情 |
| 5 | fsourceurl | 来源url | varchar | 255 |  | √ | ' ' | 来源url |
| 6 | fframework | 报告框架 | varchar | 255 |  | √ | ' ' | 报告框架 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdatasrctype | 数据来源类型 | varchar | 3 |  | √ | ' ' | 数据来源类型 |
| 9 | fispin | 是否置顶 | varchar | 3 |  | √ | ' ' | 是否置顶 |
| 10 | fispreset | 是否预置 | varchar | 3 |  | √ | ' ' | 是否预置 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ftitle | 框架标题 | varchar | 50 |  | √ | ' ' | 框架标题 |
| 13 | fusedtimes | fusedtimes | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_rptframework |  | fid |
| 2 | idx_dfa_rptframework_m0 |  | fispin |
