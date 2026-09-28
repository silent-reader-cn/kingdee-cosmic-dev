# 姓名-cts_name

## 姓名-主表 t_cts_name

- **表名称：** 姓名-主表
- **表名：** t_cts_name

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 3 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源 |
| 4 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 5 | ftitle | 一般称谓 | varchar | 50 |  | √ | ' ' | 一般称谓 |
| 6 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 7 | fcustomfield1 | 自定义字段1 | varchar | 50 |  | √ | ' ' | 自定义字段1 |
| 8 | fcustomfield2 | 自定义字段2 | varchar | 50 |  | √ | ' ' | 自定义字段2 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | flastname | 尾名 | varchar | 50 |  | √ | ' ' | 尾名 |
| 11 | fpositionaltitle | 职称 | varchar | 50 |  | √ | ' ' | 职称 |
| 12 | ffixedtext2 | 固定文本2 | varchar | 50 |  | √ | ' ' | 固定文本2 |
| 13 | ffixedtext1 | 固定文本1 | varchar | 50 |  | √ | ' ' | 固定文本1 |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 最后修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fnameconfig | 单据格式 | int8 | 64 |  | √ | 0 | [姓名文本格式 cts_nameconfigformat](../cts_files/cts_nameconfigformat.md) |
| 17 | fabbreviation | 缩写 | varchar | 50 |  | √ | ' ' | 缩写 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcountryid | 国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 20 | ffirstname | 首名 | varchar | 50 |  | √ | ' ' | 首名 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fmiddlename | 中间名 | varchar | 50 |  | √ | ' ' | 中间名 |
| 23 | fnickname | 昵称 | varchar | 50 |  | √ | ' ' | 昵称 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_name_country |  | fcountryid |
| 2 | idx_cts_name_number |  | fnumber |
| 3 | pk_cts_name |  | fid |
