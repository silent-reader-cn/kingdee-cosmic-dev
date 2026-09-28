# 物料库-plm_pdm_material_revi_lib

## 物料库-分表 t_plm_pdm_basic_mb

- **表名称：** 物料库-分表
- **表名：** t_plm_pdm_basic_mb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flcstageid | 生命周期阶段 | int8 | 64 |  | √ | 0 | 生命周期阶段 plm_lc_stage |
| 3 | flcstatusid | 生命周期状态 | int8 | 64 |  | √ | 0 | 生命周期状态 plm_lc_status |
| 4 | flatestversion | flatestversion | varchar | 10 |  | √ | ' ' |  |
| 5 | fsyncid_result | ID同步结果 | varchar | 255 |  | √ | ' ' | ID同步结果 |
| 6 | fbomversion | fbomversion | varchar | 50 |  | √ | ' ' |  |
| 7 | fcheckoutstatus | 检出状态 | varchar | 50 |  | √ | ' ' | 检出状态,枚举: N :未检出 Y :已检出 |
| 8 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 9 | fattachmenturl | 附件地址 | varchar | 500 |  | √ | ' ' | 附件地址 |
| 10 | fhead | fhead | int8 | 64 |  | √ | 0 |  |
| 11 | fsyncid | 第一次成功同步id | int8 | 64 |  | √ | 0 | 第一次成功同步id |
| 12 | fclassattrid | 分类属性 | int8 | 64 |  | √ | 0 | 分类属性仓库 plm_plmsm_lib_attributes |
| 13 | fchangetype | fchangetype | bpchar | 1 |  | √ | 'A' |  |
| 14 | fdescriptionld | fdescriptionld | varchar | 255 |  | √ | ' ' |  |
| 15 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 16 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A : B :变更中 |
| 17 | fparentfolderid | 所属文件夹 | int8 | 64 |  | √ | 0 | 系统文件夹 plm_pdm_folder_hub |
| 18 | fpicflowstatus | 数据状态图标 | varchar | 255 |  | √ | ' ' | 数据状态图标 |
| 19 | fcheckouttorid | 检出人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | flatestversiondetails | flatestversiondetails | varchar | 50 |  | √ | ' ' |  |
| 21 | fsynctime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 22 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 23 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |
| 24 | fownerld | 所有者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fisvirtualdoc | 是否虚文档 | bpchar | 1 |  | √ | '0' | 是否虚文档 |
| 26 | fchangemode | fchangemode | bpchar | 1 |  | √ | 'A' |  |
| 27 | fenablestatus | fenablestatus | bpchar | 1 |  | √ | 'A' |  |
| 28 | fapplyorgid | fapplyorgid | int8 | 64 |  | √ | 0 |  |
| 29 | fchangereason | fchangereason | bpchar | 1 |  | √ | 'A' |  |
| 30 | fviewid | fviewid | int8 | 64 |  | √ | 0 |  |
| 31 | fbaseunits | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 32 | fsubnewbomversion | fsubnewbomversion | int8 | 64 |  | √ | 0 |  |
| 33 | fexecapplystatus | fexecapplystatus | bpchar | 1 |  | √ | 'A' |  |
| 34 | fmfgbomid | fmfgbomid | int8 | 64 |  | √ | 0 |  |
| 35 | fflowstatus | 流程状态 | varchar | 50 |  | √ | ' ' | 流程状态,枚举: A :未开始 B :流程中 C :流程结束 |
| 36 | flatestbranch | flatestbranch | int8 | 64 |  | √ | 0 |  |
| 37 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 38 | fmaterial_attr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10070 :特征件 |
| 39 | finvetory_type | 存货类别 | int8 | 64 |  | √ | 0 | 存货类别 bd_materialcategory |
| 40 | ferpmaterialid | ERP 物料id | int8 | 64 |  | √ | 0 | ERP 物料id |
| 41 | flistcontrol | 列表控制 | int8 | 64 |  | √ | 0 | 列表控制 |
| 42 | fpicinstance | 对象图标 | varchar | 255 |  | √ | ' ' | 对象图标 |
| 43 | fchangesource | fchangesource | bpchar | 1 |  | √ | 'A' |  |
| 44 | fisfirstversion | 是否是第一次checkin版本 | int4 | 32 |  | √ | 0 | 是否是第一次checkin版本 |
| 45 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 46 | fmainid | fmainid | int8 | 64 |  | √ | 0 |  |
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

## 物料库-主表 t_plm_pdm_basic

- **表名称：** 物料库-主表
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
| 13 | fspecification | 规格 | varchar | 50 |  | √ | ' ' | 规格 |
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
| 28 | fmodelnum | 型号 | varchar | 255 |  | √ | ' ' | 型号 |
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

## 物料库-分表 t_plm_pdm_basic_mr

- **表名称：** 物料库-分表
- **表名：** t_plm_pdm_basic_mr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fversiondetails | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 3 | fmaterialnum | fmaterialnum | varchar | 50 |  | √ | ' ' |  |
| 4 | fcolor | fcolor | varchar | 50 |  | √ | ' ' |  |
| 5 | fislatestrevision | 是否最新版本 | varchar | 10 |  | √ | ' ' | 是否最新版本,枚举: A :是最新版 B :不是最新版 C :变更中版本 |
| 6 | fitemmasterid | 主数据 | int8 | 64 |  | √ | 0 | 物料 plm_pdm_material |
| 7 | fprioritylevel | 优选等级 | bpchar | 1 |  | √ | 'A' | 优选等级,枚举: A :优选 B :可选 C :禁选 |
| 8 | ficon | 图标 | varchar | 255 |  | √ | ' ' | 图标 |
| 9 | fsecondaryversionid | 次新版次 | int8 | 64 |  | √ | 0 | 次新版次 |
| 10 | flargeversioncode | 大版本内码 | varchar | 50 |  | √ | ' ' | 大版本内码 |
| 11 | fmaterial | fmaterial | varchar | 50 |  | √ | ' ' |  |
| 12 | feplanfullpagename | EPLAN完整页名 | varchar | 255 |  | √ | ' ' | EPLAN完整页名 |
| 13 | ffixedleadtime | 采购周期 | int4 | 32 |  | √ | 0 | 采购周期 |
| 14 | fpriceandtax | 采购价格（含税） | varchar | 50 |  | √ | ' ' | 采购价格（含税） |
| 15 | fperiodendprice | 存货价格 | varchar | 50 |  | √ | ' ' | 存货价格 |
| 16 | fcheckoutpath | fcheckoutpath | varchar | 500 |  | √ | ' ' |  |
| 17 | fcadtype | fcadtype | int8 | 64 |  | √ | 0 |  |
| 18 | fdocmodel | 业务模型（废弃） | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 19 | fdocumenttemplate | fdocumenttemplate | int8 | 64 |  | √ | 0 |  |
| 20 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 21 | fminiorversion | 当前小版本 | varchar | 50 |  | √ | ' ' | 当前小版本 |
| 22 | fmatunitid | fmatunitid | int8 | 64 |  | √ | 0 |  |
| 23 | fminiorversioncode | 小版本内码 | varchar | 50 |  | √ | ' ' | 小版本内码 |
| 24 | fversionid | 最新版次 | int8 | 64 |  | √ | 0 | 最新版次 |
| 25 | fpictureno | 图号 | varchar | 50 |  | √ | ' ' | 图号 |
| 26 | funitfield | funitfield | int4 | 32 |  | √ | 0 |  |
| 27 | fpdffile | fpdffile | int8 | 64 |  | √ | 0 |  |
| 28 | fdocthumbnail | 缩略图 | varchar | 255 |  | √ | ' ' | 缩略图 |
| 29 | fvisuallizationfile | fvisuallizationfile | int8 | 64 |  | √ | 0 |  |
| 30 | finventoryqty | 库存数量 | numeric | 23 | 10 | √ | 0 | 库存数量 |
| 31 | fqtyfield | fqtyfield | numeric | 23 | 10 | √ | 0 |  |
| 32 | fphysicalfile | 物理文件 | int8 | 64 |  | √ | 0 | 物理文件属性 plm_plmdc_physical_file |
| 33 | fspec | fspec | varchar | 50 |  | √ | ' ' |  |
| 34 | fmaincontentsource | fmaincontentsource | varchar | 50 |  | √ | ' ' |  |
| 35 | fsubnewversion | 次新版本 | int8 | 64 |  | √ | 0 | 物料版本 plm_pdm_material_revision |
| 36 | flargeversion | 当前大版本 | varchar | 50 |  | √ | ' ' | 当前大版本 |
| 37 | fmatqty | fmatqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fbaseqty | 呆滞数量 | numeric | 23 | 10 | √ | 0 | 呆滞数量 |
| 39 | ffqty | ffqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |
| 41 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_basic_r_ver |  | fversionid |
| 2 | pk_plm_pdm_basic_mr |  | fid |

---

## 物料库-使用范围表 t_plm_pdm_basic_u

- **表名称：** 物料库-使用范围表
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

## 物料库-多语言表 t_plm_pdm_basic_l

- **表名称：** 物料库-多语言表
- **表名：** t_plm_pdm_basic_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fspecification | 规格 | varchar | 50 |  | √ | ' ' | 规格 |
| 4 | fdisplayname | 显示名称 | varchar | 2000 |  | √ | ' ' | 显示名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fmodelnum | 型号 | varchar | 255 |  | √ | ' ' | 型号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_basic_l |  | fpkid |
| 2 | idx_plm_pdm_basic_l_0 |  | fid,flocaleid |
