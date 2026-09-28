# 实例详情-plm_plmsm_instance_detail

## 实例详情-分表 t_plm_pdm_basic_mb

- **表名称：** 实例详情-分表
- **表名：** t_plm_pdm_basic_mb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flcstageid | flcstageid | int8 | 64 |  | √ | 0 |  |
| 3 | flcstatusid | flcstatusid | int8 | 64 |  | √ | 0 |  |
| 4 | flatestversion | flatestversion | varchar | 10 |  | √ | ' ' |  |
| 5 | fsyncid_result | fsyncid_result | varchar | 255 |  | √ | ' ' |  |
| 6 | fbomversion | fbomversion | varchar | 50 |  | √ | ' ' |  |
| 7 | fcheckoutstatus | fcheckoutstatus | varchar | 50 |  | √ | ' ' |  |
| 8 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 9 | fattachmenturl | fattachmenturl | varchar | 500 |  | √ | ' ' |  |
| 10 | fhead | fhead | int8 | 64 |  | √ | 0 |  |
| 11 | fsyncid | fsyncid | int8 | 64 |  | √ | 0 |  |
| 12 | fclassattrid | fclassattrid | int8 | 64 |  | √ | 0 |  |
| 13 | fchangetype | fchangetype | bpchar | 1 |  | √ | 'A' |  |
| 14 | fdescriptionld | fdescriptionld | varchar | 255 |  | √ | ' ' |  |
| 15 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 16 | fchangestatus | fchangestatus | bpchar | 1 |  | √ | 'A' |  |
| 17 | fparentfolderid | fparentfolderid | int8 | 64 |  | √ | 0 |  |
| 18 | fpicflowstatus | fpicflowstatus | varchar | 255 |  | √ | ' ' |  |
| 19 | fcheckouttorid | fcheckouttorid | int8 | 64 |  | √ | 0 |  |
| 20 | flatestversiondetails | flatestversiondetails | varchar | 50 |  | √ | ' ' |  |
| 21 | fsynctime | fsynctime | timestamp | 0 |  |  | null |  |
| 22 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 23 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |
| 24 | fownerld | fownerld | int8 | 64 |  | √ | 0 |  |
| 25 | fisvirtualdoc | fisvirtualdoc | bpchar | 1 |  | √ | '0' |  |
| 26 | fchangemode | fchangemode | bpchar | 1 |  | √ | 'A' |  |
| 27 | fenablestatus | fenablestatus | bpchar | 1 |  | √ | 'A' |  |
| 28 | fapplyorgid | fapplyorgid | int8 | 64 |  | √ | 0 |  |
| 29 | fchangereason | fchangereason | bpchar | 1 |  | √ | 'A' |  |
| 30 | fviewid | fviewid | int8 | 64 |  | √ | 0 |  |
| 31 | fbaseunits | fbaseunits | int8 | 64 |  | √ | 0 |  |
| 32 | fsubnewbomversion | fsubnewbomversion | int8 | 64 |  | √ | 0 |  |
| 33 | fexecapplystatus | fexecapplystatus | bpchar | 1 |  | √ | 'A' |  |
| 34 | fmfgbomid | fmfgbomid | int8 | 64 |  | √ | 0 |  |
| 35 | fflowstatus | fflowstatus | varchar | 50 |  | √ | ' ' |  |
| 36 | flatestbranch | flatestbranch | int8 | 64 |  | √ | 0 |  |
| 37 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 38 | fmaterial_attr | fmaterial_attr | varchar | 50 |  | √ | ' ' |  |
| 39 | finvetory_type | finvetory_type | int8 | 64 |  | √ | 0 |  |
| 40 | ferpmaterialid | ferpmaterialid | int8 | 64 |  | √ | 0 |  |
| 41 | flistcontrol | flistcontrol | int8 | 64 |  | √ | 0 |  |
| 42 | fpicinstance | fpicinstance | varchar | 255 |  | √ | ' ' |  |
| 43 | fchangesource | fchangesource | bpchar | 1 |  | √ | 'A' |  |
| 44 | fisfirstversion | fisfirstversion | int4 | 32 |  | √ | 0 |  |
| 45 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
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

## 实例详情-主表 t_plm_pdm_basic

- **表名称：** 实例详情-主表
- **表名：** t_plm_pdm_basic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 4 | frdmversion | frdmversion | varchar | 10 |  | √ | ' ' |  |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 7 | fdatastagebit | fdatastagebit | int8 | 64 |  | √ | 1 |  |
| 8 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '-' |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fspecification | fspecification | varchar | 50 |  | √ | ' ' |  |
| 14 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 15 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fbizorg | fbizorg | int8 | 64 |  | √ | 0 |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 21 | fdisplayname | fdisplayname | varchar | 1024 |  | √ | ' ' |  |
| 22 | fsummary_tag | fsummary_tag | text | 0 |  |  | null |  |
| 23 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 24 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 25 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 28 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 29 | fsummary | fsummary | varchar | 255 |  | √ | ' ' |  |

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

## 实例详情-分表 t_plm_pdm_basic_mr

- **表名称：** 实例详情-分表
- **表名：** t_plm_pdm_basic_mr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fversiondetails | fversiondetails | varchar | 50 |  | √ | ' ' |  |
| 3 | fmaterialnum | fmaterialnum | varchar | 50 |  | √ | ' ' |  |
| 4 | fcolor | fcolor | varchar | 50 |  | √ | ' ' |  |
| 5 | fislatestrevision | fislatestrevision | varchar | 10 |  | √ | ' ' |  |
| 6 | fitemmasterid | fitemmasterid | int8 | 64 |  | √ | 0 |  |
| 7 | fprioritylevel | fprioritylevel | bpchar | 1 |  | √ | 'A' |  |
| 8 | ficon | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 9 | fsecondaryversionid | fsecondaryversionid | int8 | 64 |  | √ | 0 |  |
| 10 | flargeversioncode | flargeversioncode | varchar | 50 |  | √ | ' ' |  |
| 11 | fmaterial | fmaterial | varchar | 50 |  | √ | ' ' |  |
| 12 | feplanfullpagename | feplanfullpagename | varchar | 255 |  | √ | ' ' |  |
| 13 | ffixedleadtime | ffixedleadtime | int4 | 32 |  | √ | 0 |  |
| 14 | fpriceandtax | fpriceandtax | varchar | 50 |  | √ | ' ' |  |
| 15 | fperiodendprice | fperiodendprice | varchar | 50 |  | √ | ' ' |  |
| 16 | fcheckoutpath | fcheckoutpath | varchar | 500 |  | √ | ' ' |  |
| 17 | fcadtype | fcadtype | int8 | 64 |  | √ | 0 |  |
| 18 | fdocmodel | fdocmodel | int8 | 64 |  | √ | 0 |  |
| 19 | fdocumenttemplate | fdocumenttemplate | int8 | 64 |  | √ | 0 |  |
| 20 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 21 | fminiorversion | fminiorversion | varchar | 50 |  | √ | ' ' |  |
| 22 | fmatunitid | fmatunitid | int8 | 64 |  | √ | 0 |  |
| 23 | fminiorversioncode | fminiorversioncode | varchar | 50 |  | √ | ' ' |  |
| 24 | fversionid | fversionid | int8 | 64 |  | √ | 0 |  |
| 25 | fpictureno | fpictureno | varchar | 50 |  | √ | ' ' |  |
| 26 | funitfield | funitfield | int4 | 32 |  | √ | 0 |  |
| 27 | fpdffile | fpdffile | int8 | 64 |  | √ | 0 |  |
| 28 | fdocthumbnail | fdocthumbnail | varchar | 255 |  | √ | ' ' |  |
| 29 | fvisuallizationfile | fvisuallizationfile | int8 | 64 |  | √ | 0 |  |
| 30 | finventoryqty | finventoryqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fqtyfield | fqtyfield | numeric | 23 | 10 | √ | 0 |  |
| 32 | fphysicalfile | fphysicalfile | int8 | 64 |  | √ | 0 |  |
| 33 | fspec | fspec | varchar | 50 |  | √ | ' ' |  |
| 34 | fmaincontentsource | fmaincontentsource | varchar | 50 |  | √ | ' ' |  |
| 35 | fsubnewversion | fsubnewversion | int8 | 64 |  | √ | 0 |  |
| 36 | flargeversion | flargeversion | varchar | 50 |  | √ | ' ' |  |
| 37 | fmatqty | fmatqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | ffqty | ffqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |
| 41 | funit | funit | int8 | 64 |  | √ | 0 |  |

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

## 实例详情-多语言表 t_plm_pdm_basic_l

- **表名称：** 实例详情-多语言表
- **表名：** t_plm_pdm_basic_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fspecification | fspecification | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisplayname | fdisplayname | varchar | 2000 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
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
