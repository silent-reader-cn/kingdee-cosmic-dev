# 影响对象-plm_plmcm_effected_object

## 单据体-子表 t_plmcm_effectedobject

- **表名称：** 单据体-子表
- **表名：** t_plmcm_effectedobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 2 | fobjectid | fobjectid | int8 | 64 |  | √ | 0 | id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fobject | 对象编码 | int8 | 64 |  | √ | 0 | 版本模型 plm_pdm_itemrevision |
| 5 | fisdirectadd | 直接添加标识 | int4 | 32 |  | √ | 1 | 直接添加标识 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fobjectid | fobjectid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmcm_effectedobject |  | fobjectid |
| 2 | idx_plmcm_effectedobject_fk |  | fentryid |

---

## 影响对象-主表 t_plm_pdm_relation

- **表名称：** 影响对象-主表
- **表名：** t_plm_pdm_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangeobjectid | fchangeobjectid | int8 | 64 |  | √ | 0 |  |
| 3 | fendid | fendid | int8 | 64 |  | √ | 0 |  |
| 4 | fnocontains | fnocontains | varchar | 50 |  | √ | ' ' |  |
| 5 | frelationtype | frelationtype | varchar | 50 |  | √ | ' ' |  |
| 6 | fnew_parent_material | fnew_parent_material | int8 | 64 |  | √ | 0 |  |
| 7 | flayer | flayer | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodelid | fmodelid | int8 | 64 |  | √ | 0 |  |
| 9 | foptype | foptype | varchar | 50 |  | √ | ' ' |  |
| 10 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 11 | flocation | flocation | varchar | 255 |  | √ | ' ' |  |
| 12 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 13 | fmaterialversion | fmaterialversion | varchar | 50 |  | √ | ' ' |  |
| 14 | flineallowedit | flineallowedit | bpchar | 1 |  | √ | '1' |  |
| 15 | fbeginid | fbeginid | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 17 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 18 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 19 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 20 | fmfgbomentryid | fmfgbomentryid | int8 | 64 |  | √ | 0 |  |
| 21 | flineno | flineno | int4 | 32 |  | √ | 0 |  |
| 22 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 23 | freplacemethod | freplacemethod | varchar | 50 |  | √ | ' ' |  |
| 24 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 25 | frepeffectdate | frepeffectdate | timestamp | 0 |  |  | null |  |
| 26 | frepinvaliddate | frepinvaliddate | timestamp | 0 |  |  | null |  |
| 27 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 29 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 30 | freplacestra | freplacestra | varchar | 50 |  | √ | ' ' |  |
| 31 | fdeno | fdeno | numeric | 23 | 10 | √ | 1 |  |
| 32 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
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
| 45 | ftargetid | ftargetid | int8 | 64 |  | √ | 0 |  |
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
