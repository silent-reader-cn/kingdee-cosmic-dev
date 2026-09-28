# 结构视图关系_版次-plm_pdm_view_relation_v

## 结构视图关系_版次-主表 t_plm_pdm_relation_ver

- **表名称：** 结构视图关系_版次-主表
- **表名：** t_plm_pdm_relation_ver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 源 | int8 | 64 |  | √ | 0 | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
| 2 | fdeltagnum_tag | fdeltagnum_tag | text | 0 |  |  | null |  |
| 3 | febomentryid | febomentryid | int8 | 64 |  | √ | 0 |  |
| 4 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: A :关联关系 B :组合关系 C :聚合关系 |
| 5 | flayer | flayer | varchar | 50 |  | √ | ' ' |  |
| 6 | fconfigcategory | fconfigcategory | varchar | 255 |  | √ | ' ' |  |
| 7 | fmodelid | 业务类型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 8 | foptype | foptype | varchar | 50 |  | √ | ' ' |  |
| 9 | flocation | flocation | varchar | 255 |  | √ | ' ' |  |
| 10 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 11 | fconfigname | fconfigname | varchar | 255 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | faddtagnum_tag | faddtagnum_tag | text | 0 |  |  | null |  |
| 14 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 15 | fbomid | 子项结构单 | int8 | 64 |  | √ | 0 | [结构视图 plm_pdm_structure_view](../plmsm_files/plm_pdm_structure_view.md) |
| 16 | fprinttemplateid | fprinttemplateid | varchar | 50 |  | √ | ' ' |  |
| 17 | finputmethod | finputmethod | varchar | 50 |  | √ | ' ' |  |
| 18 | foptiontype | foptiontype | varchar | 50 |  | √ | ' ' |  |
| 19 | flineno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 21 | fconfigmaxvalue | fconfigmaxvalue | numeric | 23 | 10 | √ | 0 |  |
| 22 | freplacemethod | freplacemethod | varchar | 50 |  | √ | ' ' |  |
| 23 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 24 | fismodify | 是否修改 | bpchar | 1 |  | √ | ' ' | 是否修改 |
| 25 | frepinvaliddate | frepinvaliddate | timestamp | 0 |  |  | null |  |
| 26 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | fenablestatus | fenablestatus | varchar | 50 |  | √ | ' ' |  |
| 28 | freplacestra | freplacestra | varchar | 50 |  | √ | ' ' |  |
| 29 | fdeno | fdeno | numeric | 23 | 10 | √ | 1 |  |
| 30 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | ftagnum | 位号 | varchar | 2000 |  | √ | ' ' | 位号 |
| 32 | fplannedexpireddate | 计划失效时间 | timestamp | 0 |  |  | null | 计划失效时间 |
| 33 | fderive | 来源 | varchar | 50 |  | √ | ' ' | 来源 |
| 34 | fparent_material | fparent_material | int8 | 64 |  | √ | 0 |  |
| 35 | fcompletedstate | fcompletedstate | bpchar | 1 |  | √ | ' ' |  |
| 36 | fconfigdescription_tag | fconfigdescription_tag | text | 0 |  |  | null |  |
| 37 | frowkey | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | ftargetid | 目标 | int8 | 64 |  | √ | 0 | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
| 40 | fdeltagnum | fdeltagnum | varchar | 2000 |  | √ | ' ' |  |
| 41 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 42 | fchangeobjectid | fchangeobjectid | int8 | 64 |  | √ | 0 |  |
| 43 | fendid | 结束ID | int8 | 64 |  | √ | 0 | 结束ID |
| 44 | fnocontains | 不包括在材料明细表中 | varchar | 50 |  | √ | ' ' | 不包括在材料明细表中,枚举: Y :是 N : |
| 45 | ftagnum_tag | 位号_详情 | text | 0 |  |  | null | 位号_详情 |
| 46 | fmustchoose | fmustchoose | bpchar | 1 |  | √ | '0' |  |
| 47 | fnew_parent_material | fnew_parent_material | int8 | 64 |  | √ | 0 |  |
| 48 | fpriority | fpriority | int4 | 32 |  | √ | 0 |  |
| 49 | ftargetstage | ftargetstage | int8 | 64 |  | √ | 0 |  |
| 50 | fprocessno | fprocessno | int4 | 32 |  | √ | 0 |  |
| 51 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 52 | fconfignumber | fconfignumber | varchar | 255 |  | √ | ' ' |  |
| 53 | fchangemethod | fchangemethod | varchar | 50 |  | √ | ' ' |  |
| 54 | fmaterialversion | fmaterialversion | varchar | 50 |  | √ | ' ' |  |
| 55 | fconfigminvalue | fconfigminvalue | numeric | 23 | 10 | √ | 0 |  |
| 56 | fsourcestage | fsourcestage | int8 | 64 |  | √ | 0 |  |
| 57 | flineallowedit | 行是否允许编辑 | bpchar | 1 |  | √ | '1' | 行是否允许编辑 |
| 58 | fbeginid | 开始ID | int8 | 64 |  | √ | 0 | 开始ID |
| 59 | ffromtab | ffromtab | varchar | 50 |  | √ | ' ' |  |
| 60 | feffectdate | feffectdate | timestamp | 0 |  |  | null |  |
| 61 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | fmfgbomentryid | fmfgbomentryid | int8 | 64 |  | √ | 0 |  |
| 63 | factualusage | factualusage | numeric | 23 | 10 | √ | 0 |  |
| 64 | frepeffectdate | frepeffectdate | timestamp | 0 |  |  | null |  |
| 65 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 66 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 68 | fprocurementtype | 采购类型 | varchar | 50 |  | √ | ' ' | 采购类型,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10070 :特征件 |
| 69 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 70 | faddtagnum | faddtagnum | varchar | 2000 |  | √ | ' ' |  |
| 71 | fisuseversion | 是否指定版本 | varchar | 50 |  | √ | ' ' | 是否指定版本 |
| 72 | fcompressstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: Normal : Lightening :轻化 Compress :压缩 Hidden :隐藏 InternalSave :内部保存 |
| 73 | fconfigdescription | fconfigdescription | varchar | 2000 |  | √ | ' ' |  |
| 74 | fmulchoose | fmulchoose | varchar | 50 |  | √ | ' ' |  |
| 75 | fchild_material | fchild_material | int8 | 64 |  | √ | 0 |  |
| 76 | frepeatetimes | frepeatetimes | int4 | 32 |  | √ | 1 |  |
| 77 | fchangedversion | fchangedversion | varchar | 50 |  | √ | ' ' |  |
| 78 | fsourcerowkey | fsourcerowkey | varchar | 2000 |  | √ | ' ' |  |
| 79 | freplaceplanid | 替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_relation_ver_fk |  | fpriority |
| 2 | pk_plm_pdm_relation_ver |  | fentryid |
| 3 | idx_plm_pdm_relation_ver_fid |  | fid |
