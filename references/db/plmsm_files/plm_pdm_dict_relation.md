# 配置字典关系-plm_pdm_dict_relation

## 配置字典关系-主表 t_plm_pdm_relation

- **表名称：** 配置字典关系-主表
- **表名：** t_plm_pdm_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 源 | int8 | 64 |  | √ | 0 | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
| 2 | fdeltagnum_tag | fdeltagnum_tag | text | 0 |  |  | null |  |
| 3 | febomentryid | febomentryid | int8 | 64 |  | √ | 0 |  |
| 4 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: A :关联关系 B :组合关系 C :聚合关系 |
| 5 | flayer | flayer | varchar | 50 |  | √ | ' ' |  |
| 6 | fconfigcategory | 配置业务类型 | varchar | 255 |  | √ | ' ' | 配置业务类型,枚举: A :字典 B :选项组 C :选项 D :选项值 |
| 7 | fmodelid | 业务类型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 8 | foptype | foptype | varchar | 50 |  | √ | ' ' |  |
| 9 | flocation | flocation | varchar | 255 |  | √ | ' ' |  |
| 10 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 11 | fconfigname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | faddtagnum_tag | faddtagnum_tag | text | 0 |  |  | null |  |
| 14 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 15 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 16 | fprinttemplateid | fprinttemplateid | varchar | 50 |  | √ | ' ' |  |
| 17 | finputmethod | 输入方式 | varchar | 50 |  | √ | ' ' | 输入方式,枚举: enum :枚举 input :输入 |
| 18 | foptiontype | 选项类型 | varchar | 50 |  | √ | ' ' | 选项类型,枚举: A :销售 B :工程 |
| 19 | flineno | flineno | int4 | 32 |  | √ | 0 |  |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 21 | fconfigmaxvalue | 最大值 | numeric | 23 | 10 | √ | 0 | 最大值 |
| 22 | freplacemethod | freplacemethod | varchar | 50 |  | √ | ' ' |  |
| 23 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 24 | fismodify | 是否修改 | bpchar | 1 |  | √ | '0' | 是否修改 |
| 25 | frepinvaliddate | frepinvaliddate | timestamp | 0 |  |  | null |  |
| 26 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fenablestatus | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 1 :启用 0 :禁用 |
| 28 | freplacestra | freplacestra | varchar | 50 |  | √ | ' ' |  |
| 29 | fdeno | fdeno | numeric | 23 | 10 | √ | 1 |  |
| 30 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | ftagnum | ftagnum | varchar | 2000 |  | √ | ' ' |  |
| 32 | fplannedexpireddate | 计划失效时间 | timestamp | 0 |  |  | null | 计划失效时间 |
| 33 | fderive | fderive | varchar | 50 |  | √ | ' ' |  |
| 34 | fparent_material | fparent_material | int8 | 64 |  | √ | 0 |  |
| 35 | fcompletedstate | fcompletedstate | bpchar | 1 |  | √ | ' ' |  |
| 36 | fconfigdescription_tag | 描述_详情 | text | 0 |  |  | null | 描述_详情 |
| 37 | frowkey | frowkey | varchar | 50 |  | √ | ' ' |  |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | ftargetid | 目标 | int8 | 64 |  | √ | 0 | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
| 40 | fdeltagnum | fdeltagnum | varchar | 2000 |  | √ | ' ' |  |
| 41 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :文本 integer :整数 float :小数 date :日期 basedata :基础资料 Assistant :辅助资料 |
| 42 | fchangeobjectid | fchangeobjectid | int8 | 64 |  | √ | 0 |  |
| 43 | fendid | 结束ID | int8 | 64 |  | √ | 0 | 结束ID |
| 44 | fnocontains | fnocontains | varchar | 50 |  | √ | ' ' |  |
| 45 | ftagnum_tag | ftagnum_tag | text | 0 |  |  | null |  |
| 46 | fmustchoose | 是否必选 | bpchar | 1 |  | √ | '0' | 是否必选 |
| 47 | fnew_parent_material | fnew_parent_material | int8 | 64 |  | √ | 0 |  |
| 48 | fpriority | fpriority | int4 | 32 |  | √ | 0 |  |
| 49 | ftargetstage | ftargetstage | int8 | 64 |  | √ | 0 |  |
| 50 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 51 | fprocessno | fprocessno | int4 | 32 |  | √ | 0 |  |
| 52 | fconfignumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 53 | fchangemethod | fchangemethod | varchar | 50 |  | √ | ' ' |  |
| 54 | fmaterialversion | fmaterialversion | varchar | 50 |  | √ | ' ' |  |
| 55 | fconfigminvalue | 最小值 | numeric | 23 | 10 | √ | 0 | 最小值 |
| 56 | fsourcestage | fsourcestage | int8 | 64 |  | √ | 0 |  |
| 57 | flineallowedit | flineallowedit | bpchar | 1 |  | √ | '1' |  |
| 58 | fbeginid | 开始ID | int8 | 64 |  | √ | 0 | 开始ID |
| 59 | ffromtab | ffromtab | varchar | 50 |  | √ | ' ' |  |
| 60 | feffectdate | feffectdate | timestamp | 0 |  |  | null |  |
| 61 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | fmfgbomentryid | fmfgbomentryid | int8 | 64 |  | √ | 0 |  |
| 63 | factualusage | factualusage | numeric | 23 | 10 | √ | 0 |  |
| 64 | frepeffectdate | frepeffectdate | timestamp | 0 |  |  | null |  |
| 65 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 66 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 68 | fprocurementtype | fprocurementtype | varchar | 50 |  | √ | ' ' |  |
| 69 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 70 | faddtagnum | faddtagnum | varchar | 2000 |  | √ | ' ' |  |
| 71 | fisuseversion | fisuseversion | varchar | 50 |  | √ | ' ' |  |
| 72 | fcompressstatus | fcompressstatus | varchar | 50 |  | √ | ' ' |  |
| 73 | fconfigdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 74 | fmulchoose | 单选多选 | varchar | 50 |  | √ | ' ' | 单选多选,枚举: single :单选 multi :多选 |
| 75 | fchild_material | fchild_material | int8 | 64 |  | √ | 0 |  |
| 76 | frepeatetimes | frepeatetimes | int4 | 32 |  | √ | 1 |  |
| 77 | fchangedversion | fchangedversion | varchar | 50 |  | √ | ' ' |  |
| 78 | fsourcerowkey | fsourcerowkey | varchar | 2000 |  | √ | ' ' |  |
| 79 | freplaceplanid | freplaceplanid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_relation_fk |  | fid |
| 2 | pk_plm_pdm_relation |  | fentryid |
