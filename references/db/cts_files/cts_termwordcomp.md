# 术语词条表-cts_termwordcomp

## 术语词条表-主表 t_cts_termwordcomp

- **表名称：** 术语词条表-主表
- **表名：** t_cts_termwordcomp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcategory | 词条类型 | varchar | 10 |  | √ | ' ' | 词条类型 |
| 4 | fwordcomp | 词条项 | varchar | 1024 |  | √ | ' ' | 词条项 |
| 5 | flanid | 语言ID | int8 | 64 |  | √ | 0 | 语言ID |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsubjectid | 词条所属主体ID | varchar | 36 |  | √ | ' ' | 词条所属主体ID |
| 10 | fsubjectcategory | 词条所属主体类型 | varchar | 10 |  | √ | ' ' | 词条所属主体类型 |
| 11 | fsubjectname | 词条所属主体名称 | varchar | 255 |  | √ | ' ' | 词条所属主体名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 14 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: |
| 15 | fwordcompcust | 替换词条项 | varchar | 1024 |  | √ | ' ' | 替换词条项 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fwordstatus | 词条状态 | varchar | 10 |  | √ | '0' | 词条状态,枚举: 1 :待替换 2 :替换中 3 :已替换 4 :部分替换 |
| 18 | fwordid | 术语 | int8 | 64 |  | √ | 0 | [术语替换 cts_termword](../cts_files/cts_termword.md) |
| 19 | fkey | 词条key | varchar | 255 |  | √ | ' ' | 词条key |
| 20 | fenable | 启用 | bpchar | 1 |  | √ | '1' | 启用,枚举: |

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
