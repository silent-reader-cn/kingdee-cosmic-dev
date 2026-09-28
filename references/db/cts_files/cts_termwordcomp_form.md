# 重命名-cts_termwordcomp_form

## 重命名-主表 t_cts_termwordcomp

- **表名称：** 重命名-主表
- **表名：** t_cts_termwordcomp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcategory | fcategory | varchar | 10 |  | √ | ' ' |  |
| 4 | fwordcomp | 原名称 | varchar | 1024 |  | √ | ' ' | 原名称 |
| 5 | flanid | flanid | int8 | 64 |  | √ | 0 |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 8 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 9 | fsubjectid | fsubjectid | varchar | 36 |  | √ | ' ' |  |
| 10 | fsubjectcategory | fsubjectcategory | varchar | 10 |  | √ | ' ' |  |
| 11 | fsubjectname | fsubjectname | varchar | 255 |  | √ | ' ' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fappid | fappid | varchar | 36 |  | √ | ' ' |  |
| 14 | fstatus | fstatus | varchar | 10 |  | √ | ' ' |  |
| 15 | fwordcompcust | 新名称 | varchar | 1024 |  | √ | ' ' | 新名称 |
| 16 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 17 | fwordstatus | 词条状态 | varchar | 10 |  | √ | '0' | 词条状态,枚举: 1 :待替换 2 :替换中 3 :已替换 |
| 18 | fwordid | fwordid | int8 | 64 |  | √ | 0 |  |
| 19 | fkey | fkey | varchar | 255 |  | √ | ' ' |  |
| 20 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cts_termwordcomp_pkey |  | fid |
| 2 | idx_cts_termwordcomp_complex |  | fappid,flanid |
| 3 | idx_cts_termwordcomp_fwordid |  | fwordid |
