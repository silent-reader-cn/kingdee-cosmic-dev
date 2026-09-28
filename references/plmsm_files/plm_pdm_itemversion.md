# 版次模型-plm_pdm_itemversion

## 版次模型-多语言表 t_plm_pdm_version_l

- **表名称：** 版次模型-多语言表
- **表名：** t_plm_pdm_version_l

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
| 1 | idx_plm_pdm_version_l_0 |  | fid,flocaleid |
| 2 | pk_plm_pdm_version_l |  | fpkid |

---

## 版次模型-使用范围表 t_plm_pdm_version_u

- **表名称：** 版次模型-使用范围表
- **表名：** t_plm_pdm_version_u

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
| 1 | idx_t_plm_pdm_version_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pdm_version_u |  | fdataid,fuseorgid |

---

## 版次模型-分表 t_plm_pdm_version_mb

- **表名称：** 版次模型-分表
- **表名：** t_plm_pdm_version_mb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flcstageid | 生命周期阶段 | int8 | 64 |  | √ | 0 | 生命周期阶段 plm_lc_stage |
| 3 | flcstatusid | 生命周期状态 | int8 | 64 |  | √ | 0 | 生命周期状态 plm_lc_status |
| 4 | fsyncid_result | ID同步结果 | varchar | 255 |  | √ | ' ' | ID同步结果 |
| 5 | fcheckoutstatus | 检出状态 | varchar | 50 |  | √ | ' ' | 检出状态,枚举: N :未检出 Y :已检出 |
| 6 | fattachmenturl | 附件地址 | varchar | 500 |  | √ | ' ' | 附件地址 |
| 7 | fsyncid | fsyncid | int8 | 64 |  | √ | 0 |  |
| 8 | fclassattrid | 分类属性 | int8 | 64 |  | √ | 0 | 分类属性仓库 plm_plmsm_lib_attributes |
| 9 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A : B :变更中 |
| 10 | fparentfolderid | 所属文件夹 | int8 | 64 |  | √ | 0 | 系统文件夹 plm_pdm_folder_hub |
| 11 | fpicflowstatus | 数据状态图标 | varchar | 255 |  | √ | ' ' | 数据状态图标 |
| 12 | fcheckouttorid | 检出人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsynctime | fsynctime | timestamp | 0 |  |  | null |  |
| 14 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 15 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |
| 16 | fownerld | 所有者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fisvirtualdoc | 是否虚文档 | bpchar | 1 |  | √ | '0' | 是否虚文档 |
| 18 | fbaseunits | fbaseunits | int8 | 64 |  | √ | 0 |  |
| 19 | fsync_result | fsync_result | varchar | 255 |  | √ | ' ' |  |
| 20 | fflowstatus | 流程状态 | varchar | 50 |  | √ | ' ' | 流程状态,枚举: A :未开始 B :流程中 C :流程结束 |
| 21 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 22 | fmaterial_attr | fmaterial_attr | varchar | 50 |  | √ | ' ' |  |
| 23 | finvetory_type | finvetory_type | int8 | 64 |  | √ | 0 |  |
| 24 | ferpmaterialid | ferpmaterialid | int8 | 64 |  | √ | 0 |  |
| 25 | flistcontrol | 列表控制 | int8 | 64 |  | √ | 0 | 列表控制 |
| 26 | fpicinstance | 对象图标 | varchar | 255 |  | √ | ' ' | 对象图标 |
| 27 | fisfirstversion | fisfirstversion | int4 | 32 |  | √ | 0 |  |
| 28 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_version_mb_classid |  | fclassifyid |
| 2 | pk_t_plm_pdm_version_mb |  | fid |

---

## 版次模型-分表 t_plm_pdm_version_mr

- **表名称：** 版次模型-分表
- **表名：** t_plm_pdm_version_mr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fversiondetails | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 3 | fmaterialnum | fmaterialnum | varchar | 50 |  | √ | ' ' |  |
| 4 | fcolor | fcolor | varchar | 50 |  | √ | ' ' |  |
| 5 | fislatestrevision | 是否最新版本 | varchar | 10 |  | √ | ' ' | 是否最新版本,枚举: A :是最新版 B :不是最新版 C :变更中版本 |
| 6 | fitemmasterid | 主数据 | int8 | 64 |  | √ | 0 | 版本主业务模型 plm_pdm_itemmaster |
| 7 | fprioritylevel | fprioritylevel | bpchar | 1 |  | √ | 'A' |  |
| 8 | ficon | 图标 | varchar | 255 |  | √ | ' ' | 图标 |
| 9 | fsecondaryversionid | 次新版次 | int8 | 64 |  | √ | 0 | 次新版次 |
| 10 | flargeversioncode | 大版本内码 | varchar | 50 |  | √ | ' ' | 大版本内码 |
| 11 | frevisionid | 版本ID | int8 | 64 |  | √ | 0 | 版本ID |
| 12 | fmaterial | fmaterial | varchar | 50 |  | √ | ' ' |  |
| 13 | feplanfullpagename | feplanfullpagename | varchar | 255 |  | √ | ' ' |  |
| 14 | ffixedleadtime | ffixedleadtime | int4 | 32 |  | √ | 0 |  |
| 15 | fpriceandtax | fpriceandtax | varchar | 50 |  | √ | ' ' |  |
| 16 | fperiodendprice | fperiodendprice | varchar | 50 |  | √ | ' ' |  |
| 17 | fcheckoutpath | fcheckoutpath | varchar | 500 |  | √ | ' ' |  |
| 18 | fcadtype | fcadtype | int8 | 64 |  | √ | 0 |  |
| 19 | fdocmodel | fdocmodel | int8 | 64 |  | √ | 0 |  |
| 20 | fdocumenttemplate | fdocumenttemplate | int8 | 64 |  | √ | 0 |  |
| 21 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 22 | fminiorversion | 当前小版本 | varchar | 50 |  | √ | ' ' | 当前小版本 |
| 23 | fmatunitid | fmatunitid | int8 | 64 |  | √ | 0 |  |
| 24 | fminiorversioncode | 小版本内码 | varchar | 50 |  | √ | ' ' | 小版本内码 |
| 25 | fversionid | 最新版次 | int8 | 64 |  | √ | 0 | 最新版次 |
| 26 | fpictureno | fpictureno | varchar | 50 |  | √ | ' ' |  |
| 27 | funitfield | funitfield | int4 | 32 |  | √ | 0 |  |
| 28 | fpdffile | fpdffile | int8 | 64 |  | √ | 0 |  |
| 29 | fdocthumbnail | fdocthumbnail | varchar | 255 |  | √ | ' ' |  |
| 30 | fvisuallizationfile | fvisuallizationfile | int8 | 64 |  | √ | 0 |  |
| 31 | finventoryqty | finventoryqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fqtyfield | fqtyfield | numeric | 23 | 10 | √ | 0 |  |
| 33 | fphysicalfile | 物理文件 | int8 | 64 |  | √ | 0 | 物理文件属性 plm_plmdc_physical_file |
| 34 | fspec | fspec | varchar | 50 |  | √ | ' ' |  |
| 35 | fmaincontentsource | fmaincontentsource | varchar | 50 |  | √ | ' ' |  |
| 36 | fsubnewversion | 次新版本 | int8 | 64 |  | √ | 0 | 版本模型 plm_pdm_itemrevision |
| 37 | flargeversion | 当前大版本 | varchar | 50 |  | √ | ' ' | 当前大版本 |
| 38 | fmatqty | fmatqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | ffqty | ffqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |
| 42 | funit | funit | int8 | 64 |  | √ | 0 |  |
| 43 | fiteration | 迭代版本 | int8 | 64 |  | √ | 0 | 迭代版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_version_r_ver |  | fversionid |
| 2 | pk_plm_pdm_version_mr |  | fid |

---

## 版次模型-主表 t_plm_pdm_version

- **表名称：** 版次模型-主表
- **表名：** t_plm_pdm_version

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckoutstatus | fcheckoutstatus | varchar | 50 |  | √ | ' ' |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 5 | frdmversion | 系统版本 | varchar | 10 |  | √ | ' ' | 系统版本 |
| 6 | fseq | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | frevison | frevison | varchar | 50 |  | √ | ' ' |  |
| 9 | fdatastagebit | 数据阶段位 | int8 | 64 |  | √ | 1 | 数据阶段位 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmasterbizid | fmasterbizid | int8 | 64 |  | √ | 0 |  |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcheckouttorid | fcheckouttorid | int8 | 64 |  | √ | 0 |  |
| 16 | fspecification | fspecification | varchar | 50 |  | √ | ' ' |  |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | fupgradedesc | fupgradedesc | varchar | 255 |  | √ | ' ' |  |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbizorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 24 | fbranchid | fbranchid | int8 | 64 |  | √ | 0 |  |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fdisplayname | 显示名称 | varchar | 1024 |  | √ | ' ' | 显示名称 |
| 27 | fsummary_tag | 显示名称_作废_详情 | text | 0 |  |  | null | 显示名称_作废_详情 |
| 28 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 29 | flcstatusld | flcstatusld | int8 | 64 |  | √ | 0 |  |
| 30 | fctrlstrategy | 研发信息控制策略 | varchar | 50 |  | √ | ' ' | 研发信息控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 34 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 35 | fsummary | 显示名称_作废 | varchar | 255 |  | √ | ' ' | 显示名称_作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_version |  | fid |
| 2 | idx_plm_pdm_version_fnumber |  | fnumber |
| 3 | idx_t_plm_pdm_version_createorg |  | fcreateorgid |
| 4 | idx_t_plm_pdm_version_master |  | fmasterid |
