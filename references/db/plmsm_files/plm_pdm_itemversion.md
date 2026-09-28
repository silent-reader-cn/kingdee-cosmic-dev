# 版次模型-plm_pdm_itemversion

## 版次模型-多语言表 t_plm_pdm_version_l

- **表名称：** 版次模型-多语言表
- **表名：** t_plm_pdm_version_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 4 | fsyncresult | 同步结果 | varchar | 500 |  | √ | ' ' | 同步结果 |
| 5 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 6 | fdisplayname | 显示名称 | varchar | 2000 |  | √ | ' ' | 显示名称 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 10 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |

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
| 2 | fconfigdictid | fconfigdictid | int8 | 64 |  | √ | 0 |  |
| 3 | fsyncid | fsyncid | int8 | 64 |  | √ | 0 |  |
| 4 | fislatestrevision | 是否最新版本 | varchar | 10 |  | √ | 'A' | 是否最新版本,枚举: A :是最新版 B :不是最新版 C :变更中版本 |
| 5 | fstatusindict | fstatusindict | varchar | 50 |  | √ | ' ' |  |
| 6 | fbomindexid | fbomindexid | int8 | 64 |  | √ | 0 |  |
| 7 | fparentfolderid | 位置 | int8 | 64 |  | √ | 0 | [系统文件夹 plm_pdm_folder_hub](../plmsm_files/plm_pdm_folder_hub.md) |
| 8 | flatestversiondetails | flatestversiondetails | varchar | 50 |  | √ | ' ' |  |
| 9 | foptiontype | foptiontype | varchar | 50 |  | √ | ' ' |  |
| 10 | foptiondatatype | foptiondatatype | varchar | 50 |  | √ | ' ' |  |
| 11 | fproccharacteristic | fproccharacteristic | varchar | 255 |  | √ | ' ' |  |
| 12 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 13 | fchangemode | fchangemode | bpchar | 1 |  | √ | 'A' |  |
| 14 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 15 | fplannedexpireddate | 计划失效时间 | timestamp | 0 |  |  | null | 计划失效时间 |
| 16 | fminiorversion | 当前小版本 | varchar | 50 |  | √ | ' ' | 当前小版本 |
| 17 | fprocno | fprocno | int8 | 64 |  | √ | 0 |  |
| 18 | fcollapsible | fcollapsible | bpchar | 1 |  | √ | '0' |  |
| 19 | frelobjcount | 相关对象数量 | int4 | 32 |  | √ | 0 | 相关对象数量 |
| 20 | fmfgbomid | fmfgbomid | int8 | 64 |  | √ | 0 |  |
| 21 | fflowstatus | 流程标识 | varchar | 50 |  | √ | ' ' | 流程标识,枚举: A : B :流程中 C : |
| 22 | freceiveuserid | freceiveuserid | int8 | 64 |  | √ | 0 |  |
| 23 | flistcontrol | 列表控制 | int8 | 64 |  | √ | 0 | 列表控制 |
| 24 | fchangesource | fchangesource | bpchar | 1 |  | √ | 'A' |  |
| 25 | fcustomversiondetails | 客制版本 | varchar | 50 |  | √ | ' ' | 客制版本 |
| 26 | fmainid | fmainid | int8 | 64 |  | √ | 0 |  |
| 27 | fsyncid_result | ID同步结果 | varchar | 255 |  | √ | ' ' | ID同步结果 |
| 28 | fdocvisible | fdocvisible | bpchar | 1 |  | √ | 'A' |  |
| 29 | fbomversion | fbomversion | varchar | 50 |  | √ | ' ' |  |
| 30 | fattachmenturl | 附件地址 | varchar | 500 |  | √ | ' ' | 附件地址 |
| 31 | fcontrolprotocol | fcontrolprotocol | varchar | 255 |  | √ | ' ' |  |
| 32 | fconfignumber | fconfignumber | varchar | 255 |  | √ | ' ' |  |
| 33 | fistop | 是否置顶 | bpchar | 1 |  | √ | '0' | 是否置顶 |
| 34 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A : B :变更中 |
| 35 | fcheckouttorid | 检出人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | freceivestatus | freceivestatus | bpchar | 1 |  | √ | 'N' |  |
| 37 | fflowid | fflowid | int8 | 64 |  | √ | 0 |  |
| 38 | fcontrolruletype | fcontrolruletype | varchar | 50 |  | √ | ' ' |  |
| 39 | fapplyorgid | fapplyorgid | int8 | 64 |  | √ | 0 |  |
| 40 | fconfigurable | fconfigurable | varchar | 50 |  | √ | ' ' |  |
| 41 | fcomment | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 42 | fspecialty | fspecialty | varchar | 50 |  | √ | ' ' |  |
| 43 | fviewid | fviewid | int8 | 64 |  | √ | 0 |  |
| 44 | fsubnewbomversion | fsubnewbomversion | int8 | 64 |  | √ | 0 |  |
| 45 | fsenduserid | fsenduserid | int8 | 64 |  | √ | 0 |  |
| 46 | fvalueaddedtype | fvalueaddedtype | bpchar | 1 |  | √ | 'A' |  |
| 47 | fsync_result | fsync_result | varchar | 255 |  | √ | ' ' |  |
| 48 | flatestbranch | flatestbranch | int8 | 64 |  | √ | 0 |  |
| 49 | fmatapplycode | fmatapplycode | int8 | 64 |  | √ | 0 |  |
| 50 | flargeversion | 当前大版本 | varchar | 50 |  | √ | ' ' | 当前大版本 |
| 51 | finvetory_type | finvetory_type | int8 | 64 |  | √ | 0 |  |
| 52 | fpicinstance | 对象图标 | varchar | 255 |  | √ | ' ' | 对象图标 |
| 53 | fisfirstversion | fisfirstversion | int4 | 32 |  | √ | 0 |  |
| 54 | freceivetime | freceivetime | timestamp | 0 |  |  | null |  |
| 55 | flcstageid | 生命周期阶段 | int8 | 64 |  | √ | 0 | [生命周期阶段 plm_lc_stage](../plmsm_files/plm_lc_stage.md) |
| 56 | flatestversion | flatestversion | varchar | 10 |  | √ | ' ' |  |
| 57 | fhead | fhead | int8 | 64 |  | √ | 0 |  |
| 58 | fpicflowstatus | 数据状态图标 | varchar | 255 |  | √ | ' ' | 数据状态图标 |
| 59 | foperationtype | foperationtype | bpchar | 1 |  | √ | 'A' |  |
| 60 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 61 | fispushed | fispushed | bpchar | 1 |  | √ | '0' |  |
| 62 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 63 | felementdesc | felementdesc | varchar | 255 |  | √ | ' ' |  |
| 64 | fownerld | fownerld | int8 | 64 |  | √ | 0 |  |
| 65 | felementname | felementname | varchar | 50 |  | √ | ' ' |  |
| 66 | foptioninputmethod | foptioninputmethod | varchar | 50 |  | √ | ' ' |  |
| 67 | foptionminvalue | foptionminvalue | numeric | 23 | 10 | √ | 0 |  |
| 68 | foptionunitid | foptionunitid | int8 | 64 |  | √ | 0 |  |
| 69 | fenablestatus | fenablestatus | bpchar | 1 |  | √ | 'A' |  |
| 70 | foptionmustchoose | foptionmustchoose | bpchar | 1 |  | √ | '0' |  |
| 71 | fismarked | 标记 | bpchar | 1 |  | √ | '0' | 标记 |
| 72 | foptionmulchoose | foptionmulchoose | varchar | 50 |  | √ | ' ' |  |
| 73 | fbaseunits | fbaseunits | int8 | 64 |  | √ | 0 |  |
| 74 | ftoptime | 置顶日期 | timestamp | 0 |  |  | null | 置顶日期 |
| 75 | fbommasterid | fbommasterid | int8 | 64 |  | √ | 0 |  |
| 76 | fpiccheckout | 检出图标 | varchar | 255 |  | √ | ' ' | 检出图标 |
| 77 | fmaterial_attr | fmaterial_attr | varchar | 50 |  | √ | ' ' |  |
| 78 | ferpmaterialid | ferpmaterialid | int8 | 64 |  | √ | 0 |  |
| 79 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 80 | fheadrevision | fheadrevision | varchar | 50 |  | √ | ' ' |  |
| 81 | flcstatusid | flcstatusid | int8 | 64 |  | √ | 0 |  |
| 82 | fcheckoutstatus | 检出状态 | varchar | 50 |  | √ | ' ' | 检出状态,枚举: N :未检出 Y :已检出 |
| 83 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 84 | fversiondetails | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 85 | fclassattrid | 分类属性 | int8 | 64 |  | √ | 0 | [分类属性仓库 plm_plmsm_lib_attributes](../plmsm_files/plm_plmsm_lib_attributes.md) |
| 86 | fchangetype | fchangetype | bpchar | 1 |  | √ | 'A' |  |
| 87 | fitemmasterid | 主数据 | int8 | 64 |  | √ | 0 | [版本主业务模型 plm_pdm_itemmaster](../plmsm_files/plm_pdm_itemmaster.md) |
| 88 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 89 | fworkingtime | fworkingtime | numeric | 23 | 10 | √ | 0 |  |
| 90 | fsynctime | fsynctime | timestamp | 0 |  |  | null |  |
| 91 | fworkcenterid | fworkcenterid | int8 | 64 |  | √ | 0 |  |
| 92 | fassociatedwpid | fassociatedwpid | int8 | 64 |  | √ | 0 |  |
| 93 | fchangetext | fchangetext | varchar | 2000 |  | √ | ' ' |  |
| 94 | ffactoryid | ffactoryid | int8 | 64 |  | √ | 0 |  |
| 95 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 96 | fisvirtualdoc | 是否虚文档 | bpchar | 1 |  | √ | '0' | 是否虚文档 |
| 97 | fchangereason | fchangereason | bpchar | 1 |  | √ | 'A' |  |
| 98 | fexecapplystatus | fexecapplystatus | varchar | 50 |  | √ | 'A' |  |
| 99 | foptionmaxvalue | foptionmaxvalue | numeric | 23 | 10 | √ | 0 |  |
| 100 | fhasdraw | fhasdraw | bpchar | 1 |  | √ | 'N' |  |
| 101 | fproctemp | fproctemp | varchar | 150 |  | √ | ' ' |  |
| 102 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 103 | fsubnewversion | 次新版本 | int8 | 64 |  | √ | 0 | [版本模型 plm_pdm_itemrevision](../plmsm_files/plm_pdm_itemrevision.md) |
| 104 | fiscritical | fiscritical | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_version_mb_classid |  | fclassifyid |
| 2 | pk_t_plm_pdm_version_mb |  | fid |
| 3 | idx_plm_version_fitemmasterid |  | fitemmasterid |

---

## 版次模型-分表 t_plm_pdm_version_mr

- **表名称：** 版次模型-分表
- **表名：** t_plm_pdm_version_mr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcolor | fcolor | varchar | 255 |  | √ | ' ' |  |
| 3 | fislatestrevision | fislatestrevision | varchar | 10 |  | √ | ' ' |  |
| 4 | fprioritylevel | fprioritylevel | bpchar | 1 |  | √ | 'A' |  |
| 5 | ficon | 图标 | varchar | 255 |  | √ | ' ' | 图标 |
| 6 | fsecondaryversionid | 次新版次 | int8 | 64 |  | √ | 0 | 次新版次 |
| 7 | flargeversioncode | 大版本内码 | varchar | 50 |  | √ | ' ' | 大版本内码 |
| 8 | fmaterial | fmaterial | varchar | 255 |  | √ | ' ' |  |
| 9 | ffixedleadtime | ffixedleadtime | int4 | 32 |  | √ | 0 |  |
| 10 | fpriceandtax | fpriceandtax | varchar | 50 |  | √ | ' ' |  |
| 11 | fperiodendprice | fperiodendprice | varchar | 50 |  | √ | ' ' |  |
| 12 | fcheckoutpath | fcheckoutpath | varchar | 500 |  | √ | ' ' |  |
| 13 | fcadtype | fcadtype | int8 | 64 |  | √ | 0 |  |
| 14 | fperiodendprice_ds | fperiodendprice_ds | varchar | 2000 |  | √ | ' ' |  |
| 15 | fminiorversion | fminiorversion | varchar | 50 |  | √ | ' ' |  |
| 16 | fmatunitid | fmatunitid | int8 | 64 |  | √ | 0 |  |
| 17 | fversionid | 最新版次 | int8 | 64 |  | √ | 0 | 最新版次 |
| 18 | fpictureno | fpictureno | varchar | 50 |  | √ | ' ' |  |
| 19 | funitfield | funitfield | int4 | 32 |  | √ | 0 |  |
| 20 | fpdffile | fpdffile | int8 | 64 |  | √ | 0 |  |
| 21 | fvisuallizationfile | fvisuallizationfile | int8 | 64 |  | √ | 0 |  |
| 22 | fqtyfield | fqtyfield | numeric | 23 | 10 | √ | 0 |  |
| 23 | fbaseqty_ds | fbaseqty_ds | varchar | 2000 |  | √ | ' ' |  |
| 24 | ffqty | ffqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | funit | funit | int8 | 64 |  | √ | 0 |  |
| 26 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |
| 27 | fpriceandtax_ds | fpriceandtax_ds | varchar | 2000 |  | √ | ' ' |  |
| 28 | fversiondetails | fversiondetails | varchar | 50 |  | √ | ' ' |  |
| 29 | fmaterialnum | fmaterialnum | varchar | 50 |  | √ | ' ' |  |
| 30 | fitemmasterid | fitemmasterid | int8 | 64 |  | √ | 0 |  |
| 31 | finventoryqty_ds | finventoryqty_ds | varchar | 2000 |  | √ | ' ' |  |
| 32 | fdrawnogroup | fdrawnogroup | int8 | 64 |  | √ | 0 |  |
| 33 | frevisionid | 版本ID | int8 | 64 |  | √ | 0 | 版本ID |
| 34 | fupgradedesc | 升版描述 | varchar | 2000 |  | √ | ' ' | 升版描述 |
| 35 | feplanfullpagename | feplanfullpagename | varchar | 255 |  | √ | ' ' |  |
| 36 | fdocmodel | fdocmodel | int8 | 64 |  | √ | 0 |  |
| 37 | fdocumenttemplate | fdocumenttemplate | int8 | 64 |  | √ | 0 |  |
| 38 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 39 | ffiletype | ffiletype | int4 | 32 |  | √ | 0 |  |
| 40 | fminiorversioncode | 小版本内码 | varchar | 50 |  | √ | ' ' | 小版本内码 |
| 41 | fdocthumbnail | fdocthumbnail | varchar | 255 |  | √ | ' ' |  |
| 42 | finventoryqty | finventoryqty | numeric | 23 | 10 | √ | 0 |  |
| 43 | fphysicalfile | 物理文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 44 | fspec | fspec | varchar | 255 |  | √ | ' ' |  |
| 45 | fmaincontentsource | fmaincontentsource | varchar | 50 |  | √ | ' ' |  |
| 46 | fsubnewversion | fsubnewversion | int8 | 64 |  | √ | 0 |  |
| 47 | flargeversion | flargeversion | varchar | 50 |  | √ | ' ' |  |
| 48 | fmatqty | fmatqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fiteration | 迭代版本 | int8 | 64 |  | √ | 0 | 迭代版本 |

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
| 2 | flcstatusid | 流程状态 | int8 | 64 |  | √ | 0 | [流程状态 plm_lc_status](../plmsm_files/plm_lc_status.md) |
| 3 | fcheckoutstatus | fcheckoutstatus | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 6 | frdmversion | 系统版本 | varchar | 10 |  | √ | ' ' | 系统版本 |
| 7 | fconfigcollectid | fconfigcollectid | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | frevison | frevison | varchar | 50 |  | √ | ' ' |  |
| 11 | fdatastagebit | 数据阶段位 | int8 | 64 |  | √ | 1 | 数据阶段位 |
| 12 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '1' |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmasterbizid | fmasterbizid | int8 | 64 |  | √ | 0 |  |
| 15 | fdomainid | 域 | int8 | 64 |  | √ | 0 | 域 |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fcheckouttorid | fcheckouttorid | int8 | 64 |  | √ | 0 |  |
| 20 | fsyncresult | 同步结果 | varchar | 255 |  | √ | ' ' | 同步结果 |
| 21 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 22 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 23 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 24 | fupgradedesc | fupgradedesc | varchar | 255 |  | √ | ' ' |  |
| 25 | fcontainerid | 上下文 | int8 | 64 |  | √ | 0 | [上下文容器 plm_plmsm_container](../plmsm_files/plm_plmsm_container.md) |
| 26 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fbizorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 30 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 31 | fbranchid | fbranchid | int8 | 64 |  | √ | 0 |  |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fdisplayname | 显示名称 | varchar | 1024 |  | √ | ' ' | 显示名称 |
| 34 | fsummary_tag | 显示名称_作废_详情 | text | 0 |  |  | null | 显示名称_作废_详情 |
| 35 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 36 | flcstatusld | flcstatusld | int8 | 64 |  | √ | 0 |  |
| 37 | fctrlstrategy | 研发信息控制策略 | varchar | 50 |  | √ | ' ' | 研发信息控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 38 | fownerid | 所有者 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | ffolderdomain | ffolderdomain | int8 | 64 |  | √ | 0 |  |
| 40 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 42 | fcadeditstatus | fcadeditstatus | bpchar | 1 |  | √ | '0' |  |
| 43 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 44 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 45 | fsummary | 显示名称_作废 | varchar | 255 |  | √ | ' ' | 显示名称_作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_version |  | fid |
| 2 | idx_t_plm_pdm_version_createorg |  | fcreateorgid |
| 3 | idx_plm_pdm_version_fnumber |  | fnumber |
| 4 | idx_plm_pdm_version_modelid |  | fmodelid |
| 5 | idx_t_plm_pdm_version_master |  | fmasterid |
