# 语言-inte_enabledlanguage

## 语言-主表 t_int_enabledlanguagenew

- **表名称：** 语言-主表
- **表名：** t_int_enabledlanguagenew

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 4 | fenabledmultilang | 多语言字段 | bpchar | 1 |  | √ | '1' | 多语言字段 |
| 5 | fenabledlang | 启用语言 | bpchar | 1 |  | √ | '1' | 启用语言 |
| 6 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fabbrcode | 简码 | varchar | 10 |  | √ | ' ' | 简码 |
| 9 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_int_enabledlangnew_number |  | fnumber |
| 2 | pk_t_int_enabledlanguagenew |  | fid |
