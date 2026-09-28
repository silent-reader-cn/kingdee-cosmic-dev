# BOMF7模版用-plm_pdm_agg_bomview_f7

## BOMF7模版用-分表 t_plm_pdm_basic_mb

- **表名称：** BOMF7模版用-分表
- **表名：** t_plm_pdm_basic_mb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flcstageid | 生命周期阶段 | int8 | 64 |  | √ | 0 | 生命周期阶段 plm_lc_stage |
| 3 | flcstatusid | 生命周期状态 | int8 | 64 |  | √ | 0 | 生命周期状态 plm_lc_status |
| 4 | flatestversion | 是否最新版 | varchar | 10 |  | √ | ' ' | 是否最新版,枚举: A :非最新版 B :最新版 C :变更中版本 |
| 5 | fsyncid_result | ID同步结果 | varchar | 255 |  | √ | ' ' | ID同步结果 |
| 6 | fbomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 7 | fcheckoutstatus | 检出状态 | varchar | 50 |  | √ | ' ' | 检出状态,枚举: N :未检出 Y :已检出 |
| 8 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 9 | fattachmenturl | 附件地址 | varchar | 500 |  | √ | ' ' | 附件地址 |
| 10 | fhead | fhead | int8 | 64 |  | √ | 0 |  |
| 11 | fsyncid | fsyncid | int8 | 64 |  | √ | 0 |  |
| 12 | fclassattrid | fclassattrid | int8 | 64 |  | √ | 0 |  |
| 13 | fchangetype | fchangetype | bpchar | 1 |  | √ | 'A' |  |
| 14 | fdescriptionld | fdescriptionld | varchar | 255 |  | √ | ' ' |  |
| 15 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 16 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A : B :变更中 |
| 17 | fparentfolderid | 所属文件夹 | int8 | 64 |  | √ | 0 | 系统文件夹 plm_pdm_folder_hub |
| 18 | fpicflowstatus | 数据状态图标 | varchar | 255 |  | √ | ' ' | 数据状态图标 |
| 19 | fcheckouttorid | 检出人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | flatestversiondetails | flatestversiondetails | varchar | 50 |  | √ | ' ' |  |
| 21 | fsynctime | 最后同步时间 | timestamp | 0 |  |  | null | 最后同步时间 |
| 22 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 23 | fclassifyid | fclassifyid | int8 | 64 |  | √ | 0 |  |
| 24 | fownerld | 所有者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fisvirtualdoc | 是否虚文档 | bpchar | 1 |  | √ | '0' | 是否虚文档 |
| 26 | fchangemode | fchangemode | bpchar | 1 |  | √ | 'A' |  |
| 27 | fenablestatus | fenablestatus | bpchar | 1 |  | √ | 'A' |  |
| 28 | fapplyorgid | fapplyorgid | int8 | 64 |  | √ | 0 |  |
| 29 | fchangereason | fchangereason | bpchar | 1 |  | √ | 'A' |  |
| 30 | fviewid | 视图 | int8 | 64 |  | √ | 0 | BOM视图 plm_plmpsm_newbomview |
| 31 | fbaseunits | fbaseunits | int8 | 64 |  | √ | 0 |  |
| 32 | fsubnewbomversion | 次新版本 | int8 | 64 |  | √ | 0 | 结构视图 plm_pdm_structure_view |
| 33 | fexecapplystatus | fexecapplystatus | bpchar | 1 |  | √ | 'A' |  |
| 34 | fmfgbomid | 制造BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 35 | fflowstatus | 流程状态 | varchar | 50 |  | √ | ' ' | 流程状态,枚举: A :未开始 B :流程中 C :流程结束 |
| 36 | flatestbranch | flatestbranch | int8 | 64 |  | √ | 0 |  |
| 37 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 38 | fmaterial_attr | fmaterial_attr | varchar | 50 |  | √ | ' ' |  |
| 39 | finvetory_type | finvetory_type | int8 | 64 |  | √ | 0 |  |
| 40 | ferpmaterialid | ferpmaterialid | int8 | 64 |  | √ | 0 |  |
| 41 | flistcontrol | 列表控制 | int8 | 64 |  | √ | 0 | 列表控制 |
| 42 | fpicinstance | 对象图标 | varchar | 255 |  | √ | ' ' | 对象图标 |
| 43 | fchangesource | fchangesource | bpchar | 1 |  | √ | 'A' |  |
| 44 | fisfirstversion | fisfirstversion | int4 | 32 |  | √ | 0 |  |
| 45 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 46 | fmainid | 主物料编码 | int8 | 64 |  | √ | 0 | 物料版本 plm_pdm_material_revision |
| 47 | fheadrevision | fheadrevision | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_basic_mb_cls |  | fclassifyid |
| 2 | pk_plm_pdm_basic_mb |  | fid |
| 3 | idx_plm_pdm_basic_b_des |  | fdescriptionld |

---

## BOMF7模版用-主表 t_plm_pdm_basic

- **表名称：** BOMF7模版用-主表
- **表名：** t_plm_pdm_basic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 4 | frdmversion | 系统版本 | varchar | 10 |  | √ | ' ' | 系统版本 |
| 5 | fseq | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdatastagebit | 数据阶段位 | int8 | 64 |  | √ | 1 | 数据阶段位 |
| 8 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '-' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fspecification | fspecification | varchar | 50 |  | √ | ' ' |  |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbizorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdisplayname | 显示名称 | varchar | 1024 |  | √ | ' ' | 显示名称 |
| 22 | fsummary_tag | 显示名称_作废_详情 | text | 0 |  |  | null | 显示名称_作废_详情 |
| 23 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 24 | fctrlstrategy | 研发信息控制策略 | varchar | 50 |  | √ | ' ' | 研发信息控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 29 | fsummary | 显示名称_作废 | varchar | 255 |  | √ | ' ' | 显示名称_作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pdm_basic_createorg |  | fcreateorgid |
| 2 | pk_plm_pdm_basic |  | fid |
| 3 | idx_t_plm_pdm_basic_master |  | fmasterid |
| 4 | idx_plm_pdm_basic_name |  | fname |
| 5 | idx_plm_pdm_basic_modelid |  | fmodelid |
| 6 | idx_plm_pdm_basic_number |  | fnumber |

---

## 组成-子表 t_plm_pdm_relation

- **表名称：** 组成-子表
- **表名：** t_plm_pdm_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangeobjectid | fchangeobjectid | int8 | 64 |  | √ | 0 |  |
| 3 | fendid | fendid | int8 | 64 |  | √ | 0 |  |
| 4 | fnocontains | fnocontains | varchar | 50 |  | √ | ' ' |  |
| 5 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: A :关联关系 B :组合关系 C :聚合关系 |
| 6 | fnew_parent_material | fnew_parent_material | int8 | 64 |  | √ | 0 |  |
| 7 | flayer | 层 | varchar | 50 |  | √ | ' ' | 层,枚举: Top :Top Bottom :Bottom |
| 8 | fmodelid | 模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 9 | foptype | foptype | varchar | 50 |  | √ | ' ' |  |
| 10 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 11 | flocation | 位置 | varchar | 255 |  | √ | ' ' | 位置 |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | fmaterialversion | fmaterialversion | varchar | 50 |  | √ | ' ' |  |
| 14 | flineallowedit | 行是否允许编辑 | bpchar | 1 |  | √ | '1' | 行是否允许编辑 |
| 15 | fbeginid | fbeginid | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 18 | fbomid | BOMID | int8 | 64 |  | √ | 0 | 结构视图 plm_pdm_structure_view |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fmfgbomentryid | 制造Bom分录id | int8 | 64 |  | √ | 0 | 制造Bom分录id |
| 21 | flineno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 22 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 23 | freplacemethod | 替代方式 | varchar | 50 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 |
| 24 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 25 | frepeffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 26 | frepinvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 27 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 28 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 29 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | freplacestra | 替代策略 | varchar | 50 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 31 | fdeno | 基数 | numeric | 23 | 10 | √ | 1 | 基数 |
| 32 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 33 | funitid | 子物料单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | ftagnum | 位号 | varchar | 2000 |  | √ | ' ' | 位号 |
| 35 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 36 | fisuseversion | 使用指定版本 | varchar | 50 |  | √ | ' ' | 使用指定版本,枚举: N :否 Y :是 |
| 37 | fderive | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: MANUAL :手动搭建 SOLIDWORKS :SOLIDWORKS导入 EPLAN :EPLAN导入 ALTIUMDESIGNER :ALTIUMDESIGNER导入 |
| 38 | fparent_material | fparent_material | int8 | 64 |  | √ | 0 |  |
| 39 | fcompressstatus | fcompressstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fcompletedstate | fcompletedstate | bpchar | 1 |  | √ | ' ' |  |
| 41 | frowkey | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 42 | fchild_material | fchild_material | int8 | 64 |  | √ | 0 |  |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | fchangedversion | fchangedversion | varchar | 50 |  | √ | ' ' |  |
| 45 | ftargetid | 子物料编码 | int8 | 64 |  | √ | 0 | 业务模型 plm_pdm_basicbiz |
| 46 | freplaceplanid | 替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |

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

## 具体值-子表 t_plm_pdm_tagnumber

- **表名称：** 具体值-子表
- **表名：** t_plm_pdm_tagnumber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 编码 | int8 | 64 |  | √ | 0 | 业务模型 plm_pdm_basicbiz |
| 3 | fcomposerowkey | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftagnumber | 位号 | varchar | 50 |  | √ | ' ' | 位号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_pdm_tagnumber |  | fentryid |
| 2 | idx_plm_pdm_tagnumber_fid |  | fid |

---

## BOMF7模版用-使用范围表 t_plm_pdm_basic_u

- **表名称：** BOMF7模版用-使用范围表
- **表名：** t_plm_pdm_basic_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pdm_basic_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pdm_basic_u |  | fdataid,fuseorgid |

---

## BOMF7模版用-多语言表 t_plm_pdm_basic_l

- **表名称：** BOMF7模版用-多语言表
- **表名：** t_plm_pdm_basic_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fspecification | fspecification | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisplayname | 显示名称 | varchar | 2000 |  | √ | ' ' | 显示名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_basic_l |  | fpkid |
| 2 | idx_plm_pdm_basic_l_0 |  | fid,flocaleid |
