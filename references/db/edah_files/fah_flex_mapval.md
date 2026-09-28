# 映射键值对弹性域数据表-fah_flex_mapval

## 映射键值对弹性域数据表-主表 t_fah_flex_mapval

- **表名称：** 映射键值对弹性域数据表-主表
- **表名：** t_fah_flex_mapval

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhashcode | 值集数据的HashCode | int8 | 64 |  | √ | 0 | 值集数据的HashCode |
| 3 | fgroupid | 组织分组id | int8 | 64 |  | √ | 0 | 组织分组id |
| 4 | fmaptypeid | 通用数据映射类型id | int8 | 64 |  | √ | 0 | 业财数据映射 fah_valmap_typenew |
| 5 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 6 | forgtype | 适用组织类型 | varchar | 2 |  | √ | ' ' | 适用组织类型,枚举: 10 :核算组织 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :暂存态 C :发布态 |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fexpiredate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 11 | ftxtattr12 | 文本字段12 | varchar | 150 |  | √ | ' ' | 文本字段12 |
| 12 | fidattr2 | ID字段2 | int8 | 64 |  | √ | 0 | ID字段2 |
| 13 | ftxtattr13 | 文本字段13 | varchar | 150 |  | √ | ' ' | 文本字段13 |
| 14 | fidattr3 | ID字段3 | int8 | 64 |  | √ | 0 | ID字段3 |
| 15 | ftxtattr14 | 文本字段14 | varchar | 150 |  | √ | ' ' | 文本字段14 |
| 16 | fidattr4 | ID字段4 | int8 | 64 |  | √ | 0 | ID字段4 |
| 17 | ftxtattr15 | 文本字段15 | varchar | 150 |  | √ | ' ' | 文本字段15 |
| 18 | fidattr5 | ID字段5 | int8 | 64 |  | √ | 0 | ID字段5 |
| 19 | fidattr6 | ID字段6 | int8 | 64 |  | √ | 0 | ID字段6 |
| 20 | fidattr7 | ID字段7 | int8 | 64 |  | √ | 0 | ID字段7 |
| 21 | ftxtattr10 | 文本字段10 | varchar | 150 |  | √ | ' ' | 文本字段10 |
| 22 | fidattr8 | ID字段8 | int8 | 64 |  | √ | 0 | ID字段8 |
| 23 | ftxtattr11 | 文本字段11 | varchar | 150 |  | √ | ' ' | 文本字段11 |
| 24 | fidattr9 | ID字段9 | int8 | 64 |  | √ | 0 | ID字段9 |
| 25 | ftxtattr2 | 文本字段2 | varchar | 150 |  | √ | ' ' | 文本字段2 |
| 26 | ftxtattr1 | 文本字段1 | varchar | 150 |  | √ | ' ' | 文本字段1 |
| 27 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 28 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 29 | fidattr1 | ID字段1 | int8 | 64 |  | √ | 0 | ID字段1 |
| 30 | ftxtattr9 | 文本字段9 | varchar | 150 |  | √ | ' ' | 文本字段9 |
| 31 | ftxtattr8 | 文本字段8 | varchar | 150 |  | √ | ' ' | 文本字段8 |
| 32 | ftxtattr7 | 文本字段7 | varchar | 150 |  | √ | ' ' | 文本字段7 |
| 33 | ftxtattr6 | 文本字段6 | varchar | 150 |  | √ | ' ' | 文本字段6 |
| 34 | fserialnumber | 流水号 | int4 | 32 |  | √ | 0 | 流水号 |
| 35 | ftxtattr5 | 文本字段5 | varchar | 150 |  | √ | ' ' | 文本字段5 |
| 36 | fownorgid | 适用组织 | int8 | 64 |  | √ | 0 | 适用组织 |
| 37 | ftxtattr4 | 文本字段4 | varchar | 150 |  | √ | ' ' | 文本字段4 |
| 38 | ftxtattr3 | 文本字段3 | varchar | 150 |  | √ | ' ' | 文本字段3 |
| 39 | fhasmulvalue | 是否存在多选值 | bpchar | 1 |  | √ | ' ' | 是否存在多选值,枚举: 0 :没有 1 :存在 |
| 40 | fenable | 启用状态 | bpchar | 1 |  | √ | ' ' | 启用状态 |
| 41 | fmapvaluetype | 键值对数据类型 | bpchar | 1 |  | √ | ' ' | 键值对数据类型,枚举: 0 :入参 1 :出参 |
| 42 | fidattr10 | ID字段10 | int8 | 64 |  | √ | 0 | ID字段10 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fah_flex_mapval |  | fid |
| 2 | idx_fah_flex_mapval_th |  | fmaptypeid,fhashcode |
