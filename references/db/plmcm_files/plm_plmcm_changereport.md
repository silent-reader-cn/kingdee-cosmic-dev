# 更改内容-plm_plmcm_changereport

## 视图变更-子表 t_plmcm_viewchange

- **表名称：** 视图变更-子表
- **表名：** t_plmcm_viewchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fviewentryid | fviewentryid | int8 | 64 |  | √ | 0 | id |
| 2 | fviewid | 视图 | int8 | 64 |  | √ | 0 | BOM视图 plm_plmpsm_newbomview |
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
| 45 | ftargetid | 变更对象 | int8 | 64 |  | √ | 0 | 版本模型 plm_pdm_itemrevision |
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

---

## 结构变更-子表 t_plmcm_bomchange

- **表名称：** 结构变更-子表
- **表名：** t_plmcm_bomchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fviewentryid | fviewentryid | int8 | 64 |  | √ | 0 |  |
| 5 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: A :关联关系 B :组合关系 C :聚合关系 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fmodelid | 模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 8 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | ftagnum | 位号 | varchar | 2000 |  | √ | ' ' | 位号 |
| 10 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fisuseversion | 使用指定版本 | varchar | 50 |  | √ | ' ' | 使用指定版本,枚举: N :否 Y :是 |
| 13 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fbomid | BOMID | int8 | 64 |  | √ | 0 | 结构视图 plm_pdm_structure_view |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | frowstatus | 行比较状态 | bpchar | 1 |  | √ | ' ' | 行比较状态,枚举: A :新增 B :删除 C :修改前 D :修改后 |
| 17 | fmfgbomentryid | 制造Bom分录id | int8 | 64 |  | √ | 0 | 制造Bom分录id |
| 18 | flineno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | frowkey | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 21 | ftargetid | 子物料编码 | int8 | 64 |  | √ | 0 | 业务模型 plm_pdm_basicbiz |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmcm_bomchange |  | fdetailid |
| 2 | idx_plmcm_bomchange_fk |  | fviewentryid |
