# 业务对象关系模型-plm_pdm_relationbiz

## 业务对象关系模型-主表 t_plm_pdm_relation

- **表名称：** 业务对象关系模型-主表
- **表名：** t_plm_pdm_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 源 | int8 | 64 |  | √ | 0 | 业务模型 plm_pdm_basicbiz |
| 2 | fchangeobjectid | fchangeobjectid | int8 | 64 |  | √ | 0 |  |
| 3 | fendid | 结束ID | int8 | 64 |  | √ | 0 | 结束ID |
| 4 | fnocontains | fnocontains | varchar | 50 |  | √ | ' ' |  |
| 5 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: A :关联关系 B :组合关系 C :聚合关系 |
| 6 | fnew_parent_material | fnew_parent_material | int8 | 64 |  | √ | 0 |  |
| 7 | flayer | flayer | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodelid | 业务类型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 9 | foptype | foptype | varchar | 50 |  | √ | ' ' |  |
| 10 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 11 | flocation | flocation | varchar | 255 |  | √ | ' ' |  |
| 12 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 13 | fmaterialversion | fmaterialversion | varchar | 50 |  | √ | ' ' |  |
| 14 | flineallowedit | flineallowedit | bpchar | 1 |  | √ | '1' |  |
| 15 | fbeginid | 开始ID | int8 | 64 |  | √ | 0 | 开始ID |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 18 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fmfgbomentryid | fmfgbomentryid | int8 | 64 |  | √ | 0 |  |
| 21 | flineno | flineno | int4 | 32 |  | √ | 0 |  |
| 22 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 23 | freplacemethod | freplacemethod | varchar | 50 |  | √ | ' ' |  |
| 24 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 25 | frepeffectdate | frepeffectdate | timestamp | 0 |  |  | null |  |
| 26 | frepinvaliddate | frepinvaliddate | timestamp | 0 |  |  | null |  |
| 27 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 29 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | freplacestra | freplacestra | varchar | 50 |  | √ | ' ' |  |
| 31 | fdeno | fdeno | numeric | 23 | 10 | √ | 1 |  |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 34 | ftagnum | ftagnum | varchar | 2000 |  | √ | ' ' |  |
| 35 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 36 | fisuseversion | fisuseversion | varchar | 50 |  | √ | ' ' |  |
| 37 | fderive | fderive | varchar | 50 |  | √ | ' ' |  |
| 38 | fparent_material | fparent_material | int8 | 64 |  | √ | 0 |  |
| 39 | fcompressstatus | fcompressstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fcompletedstate | fcompletedstate | bpchar | 1 |  | √ | ' ' |  |
| 41 | frowkey | frowkey | varchar | 50 |  | √ | ' ' |  |
| 42 | fchild_material | fchild_material | int8 | 64 |  | √ | 0 |  |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | fchangedversion | fchangedversion | varchar | 50 |  | √ | ' ' |  |
| 45 | ftargetid | 目标 | int8 | 64 |  | √ | 0 | 业务模型 plm_pdm_basicbiz |
| 46 | freplaceplanid | freplaceplanid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_relation_fk |  | fid |
| 2 | pk_plm_pdm_relation |  | fentryid |
