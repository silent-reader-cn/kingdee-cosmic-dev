# 更改内容-plm_plmcm_changereport

## 视图变更-子表 t_plmcm_viewchange

- **表名称：** 视图变更-子表
- **表名：** t_plmcm_viewchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fviewentryid | fviewentryid | int8 | 64 |  | √ | 0 | id |
| 2 | fviewid | 视图 | int8 | 64 |  | √ | 0 | [BOM视图 plm_plmpsm_newbomview](../plmpsm_files/plm_plmpsm_newbomview.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fviewentryid | fviewentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmcm_viewchange_fk |  | fentryid |
| 2 | pk_plmcm_viewchange |  | fviewentryid |

---

## 分类属性-子表 t_plmcm_classifychange

- **表名称：** 分类属性-子表
- **表名：** t_plmcm_classifychange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fclassifyproname | 属性字段 | varchar | 50 |  | √ | ' ' | 属性字段 |
| 2 | fdetialid | fdetialid | int8 | 64 |  | √ | 0 | id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbeforeclassify | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 5 | fclassifypro | 属性标识 | varchar | 50 |  | √ | ' ' | 属性标识 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fafterclassify | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetialid | fdetialid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmcm_classifychange_fk |  | fentryid |
| 2 | pk_plmcm_classifychange |  | fdetialid |

---

## 基本属性-子表 t_plmcm_propertychange

- **表名称：** 基本属性-子表
- **表名：** t_plmcm_propertychange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetialid | fdetialid | int8 | 64 |  | √ | 0 | id |
| 2 | fbeforechange | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fproperty | 属性标识 | varchar | 50 |  | √ | ' ' | 属性标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpropertyname | 属性字段 | varchar | 50 |  | √ | ' ' | 属性字段 |
| 7 | fafterchange | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetialid | fdetialid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmcm_propertychange_fk |  | fentryid |
| 2 | pk_plmcm_propertychange |  | fdetialid |

---

## 更改内容-主表 t_plm_pdm_relation

- **表名称：** 更改内容-主表
- **表名：** t_plm_pdm_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeltagnum_tag | fdeltagnum_tag | text | 0 |  |  | null |  |
| 3 | febomentryid | febomentryid | int8 | 64 |  | √ | 0 |  |
| 4 | frelationtype | frelationtype | varchar | 50 |  | √ | ' ' |  |
| 5 | flayer | flayer | varchar | 50 |  | √ | ' ' |  |
| 6 | fconfigcategory | fconfigcategory | varchar | 255 |  | √ | ' ' |  |
| 7 | fmodelid | fmodelid | int8 | 64 |  | √ | 0 |  |
| 8 | foptype | foptype | varchar | 50 |  | √ | ' ' |  |
| 9 | flocation | flocation | varchar | 255 |  | √ | ' ' |  |
| 10 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 11 | fconfigname | fconfigname | varchar | 255 |  | √ | ' ' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | faddtagnum_tag | faddtagnum_tag | text | 0 |  |  | null |  |
| 14 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 15 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 16 | fprinttemplateid | fprinttemplateid | varchar | 50 |  | √ | ' ' |  |
| 17 | finputmethod | finputmethod | varchar | 50 |  | √ | ' ' |  |
| 18 | foptiontype | foptiontype | varchar | 50 |  | √ | ' ' |  |
| 19 | flineno | flineno | int4 | 32 |  | √ | 0 |  |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 21 | fconfigmaxvalue | fconfigmaxvalue | numeric | 23 | 10 | √ | 0 |  |
| 22 | freplacemethod | freplacemethod | varchar | 50 |  | √ | ' ' |  |
| 23 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 24 | fismodify | fismodify | bpchar | 1 |  | √ | '0' |  |
| 25 | frepinvaliddate | frepinvaliddate | timestamp | 0 |  |  | null |  |
| 26 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fenablestatus | fenablestatus | varchar | 50 |  | √ | ' ' |  |
| 28 | freplacestra | freplacestra | varchar | 50 |  | √ | ' ' |  |
| 29 | fdeno | fdeno | numeric | 23 | 10 | √ | 1 |  |
| 30 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 31 | ftagnum | ftagnum | varchar | 2000 |  | √ | ' ' |  |
| 32 | fplannedexpireddate | fplannedexpireddate | timestamp | 0 |  |  | null |  |
| 33 | fderive | fderive | varchar | 50 |  | √ | ' ' |  |
| 34 | fparent_material | fparent_material | int8 | 64 |  | √ | 0 |  |
| 35 | fcompletedstate | fcompletedstate | bpchar | 1 |  | √ | ' ' |  |
| 36 | fconfigdescription_tag | fconfigdescription_tag | text | 0 |  |  | null |  |
| 37 | frowkey | frowkey | varchar | 50 |  | √ | ' ' |  |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | ftargetid | 变更对象 | int8 | 64 |  | √ | 0 | [版本模型 plm_pdm_itemrevision](../plmsm_files/plm_pdm_itemrevision.md) |
| 40 | fdeltagnum | fdeltagnum | varchar | 2000 |  | √ | ' ' |  |
| 41 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 42 | fchangeobjectid | fchangeobjectid | int8 | 64 |  | √ | 0 |  |
| 43 | fendid | fendid | int8 | 64 |  | √ | 0 |  |
| 44 | fnocontains | fnocontains | varchar | 50 |  | √ | ' ' |  |
| 45 | ftagnum_tag | ftagnum_tag | text | 0 |  |  | null |  |
| 46 | fmustchoose | fmustchoose | bpchar | 1 |  | √ | '0' |  |
| 47 | fnew_parent_material | fnew_parent_material | int8 | 64 |  | √ | 0 |  |
| 48 | fpriority | fpriority | int4 | 32 |  | √ | 0 |  |
| 49 | ftargetstage | ftargetstage | int8 | 64 |  | √ | 0 |  |
| 50 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 51 | fprocessno | fprocessno | int4 | 32 |  | √ | 0 |  |
| 52 | fconfignumber | fconfignumber | varchar | 255 |  | √ | ' ' |  |
| 53 | fchangemethod | fchangemethod | varchar | 50 |  | √ | ' ' |  |
| 54 | fmaterialversion | fmaterialversion | varchar | 50 |  | √ | ' ' |  |
| 55 | fconfigminvalue | fconfigminvalue | numeric | 23 | 10 | √ | 0 |  |
| 56 | fsourcestage | fsourcestage | int8 | 64 |  | √ | 0 |  |
| 57 | flineallowedit | flineallowedit | bpchar | 1 |  | √ | '1' |  |
| 58 | fbeginid | fbeginid | int8 | 64 |  | √ | 0 |  |
| 59 | ffromtab | ffromtab | varchar | 50 |  | √ | ' ' |  |
| 60 | feffectdate | feffectdate | timestamp | 0 |  |  | null |  |
| 61 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 62 | fmfgbomentryid | fmfgbomentryid | int8 | 64 |  | √ | 0 |  |
| 63 | factualusage | factualusage | numeric | 23 | 10 | √ | 0 |  |
| 64 | frepeffectdate | frepeffectdate | timestamp | 0 |  |  | null |  |
| 65 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 66 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 67 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 68 | fprocurementtype | fprocurementtype | varchar | 50 |  | √ | ' ' |  |
| 69 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 70 | faddtagnum | faddtagnum | varchar | 2000 |  | √ | ' ' |  |
| 71 | fisuseversion | fisuseversion | varchar | 50 |  | √ | ' ' |  |
| 72 | fcompressstatus | fcompressstatus | varchar | 50 |  | √ | ' ' |  |
| 73 | fconfigdescription | fconfigdescription | varchar | 2000 |  | √ | ' ' |  |
| 74 | fmulchoose | fmulchoose | varchar | 50 |  | √ | ' ' |  |
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

---

## 结构变更-子表 t_plmcm_bomchange

- **表名称：** 结构变更-子表
- **表名：** t_plmcm_bomchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fviewentryid | fviewentryid | int8 | 64 |  | √ | 0 |  |
| 2 | ftagnum_tag | 位号_详情 | text | 0 |  |  | null | 位号_详情 |
| 3 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: A :关联关系 B :组合关系 C :聚合关系 |
| 4 | fpriority | 替代优先级 | int4 | 32 |  | √ | 0 | 替代优先级 |
| 5 | fmodelid | 模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 6 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 10 | fbomid | 子项BOM编码 | int8 | 64 |  | √ | 0 | [结构视图 plm_pdm_structure_view](../plmsm_files/plm_pdm_structure_view.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | frowstatus | 行标识 | bpchar | 1 |  | √ | ' ' | 行标识,枚举: A :新增 B :删除 C :修改前 D :修改后 E :替代修改 F :替代新增 G :替代删除 |
| 13 | fmfgbomentryid | 制造Bom分录id | int8 | 64 |  | √ | 0 | 制造Bom分录id |
| 14 | flineno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 15 | freplacemethod | 替代方式 | varchar | 50 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 18 | frepeffectdate | 替代生效时间 | timestamp | 0 |  |  | null | 替代生效时间 |
| 19 | frepinvaliddate | 替代失效时间 | timestamp | 0 |  |  | null | 替代失效时间 |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | freplacestra | 替代策略 | varchar | 50 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 24 | fdeno | 基数 | numeric | 23 | 10 | √ | 1 | 基数 |
| 25 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 26 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | ftagnum | 位号 | varchar | 2000 |  | √ | ' ' | 位号 |
| 28 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 29 | fisuseversion | 使用指定版本 | varchar | 50 |  | √ | ' ' | 使用指定版本,枚举: N :否 Y :是 |
| 30 | fparentdetailid | fparentdetailid | int8 | 64 |  | √ | 0 | pid |
| 31 | frowkey | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 32 | ftargetid | 子物料编码 | int8 | 64 |  | √ | 0 | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
| 33 | freplaceplanid | 替代方案编码 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmcm_bomchange_fk |  | fviewentryid |
| 2 | pk_plmcm_bomchange |  | fdetailid |
