# 实例详情-plm_plmsm_instance_detail

## 实例详情-多语言表 t_plm_pdm_basic_l

- **表名称：** 实例详情-多语言表
- **表名：** t_plm_pdm_basic_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 4 | fsyncresult | fsyncresult | varchar | 500 |  | √ | ' ' |  |
| 5 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 6 | fdisplayname | fdisplayname | varchar | 2000 |  | √ | ' ' |  |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 9 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 10 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_basic_l |  | fpkid |
| 2 | idx_plm_pdm_basic_l_0 |  | fid,flocaleid |

---

## 实例详情-分表 t_plm_pdm_basic_mb

- **表名称：** 实例详情-分表
- **表名：** t_plm_pdm_basic_mb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfigdictid | fconfigdictid | int8 | 64 |  | √ | 0 |  |
| 3 | fsyncid | fsyncid | int8 | 64 |  | √ | 0 |  |
| 4 | fislatestrevision | fislatestrevision | varchar | 10 |  | √ | 'A' |  |
| 5 | fstatusindict | fstatusindict | varchar | 50 |  | √ | ' ' |  |
| 6 | fbomindexid | fbomindexid | int8 | 64 |  | √ | 0 |  |
| 7 | fparentfolderid | fparentfolderid | int8 | 64 |  | √ | 0 |  |
| 8 | flatestversiondetails | flatestversiondetails | varchar | 50 |  | √ | ' ' |  |
| 9 | foptiontype | foptiontype | varchar | 50 |  | √ | ' ' |  |
| 10 | foptiondatatype | foptiondatatype | varchar | 50 |  | √ | ' ' |  |
| 11 | fproccharacteristic | fproccharacteristic | varchar | 255 |  | √ | ' ' |  |
| 12 | fchangemode | fchangemode | bpchar | 1 |  | √ | 'A' |  |
| 13 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 14 | fplannedexpireddate | fplannedexpireddate | timestamp | 0 |  |  | null |  |
| 15 | fminiorversion | fminiorversion | varchar | 50 |  | √ | ' ' |  |
| 16 | fprocno | fprocno | int8 | 64 |  | √ | 0 |  |
| 17 | fcollapsible | fcollapsible | bpchar | 1 |  | √ | '0' |  |
| 18 | flinkmodeltype | flinkmodeltype | int8 | 64 |  | √ | 0 |  |
| 19 | frelobjcount | frelobjcount | int4 | 32 |  | √ | 0 |  |
| 20 | fmfgbomid | fmfgbomid | int8 | 64 |  | √ | 0 |  |
| 21 | fflowstatus | fflowstatus | varchar | 50 |  | √ | ' ' |  |
| 22 | freceiveuserid | freceiveuserid | int8 | 64 |  | √ | 0 |  |
| 23 | flistcontrol | flistcontrol | int8 | 64 |  | √ | 0 |  |
| 24 | fchangesource | fchangesource | bpchar | 1 |  | √ | 'A' |  |
| 25 | fcustomversiondetails | fcustomversiondetails | varchar | 50 |  | √ | ' ' |  |
| 26 | fmainid | fmainid | int8 | 64 |  | √ | 0 |  |
| 27 | fsyncid_result | fsyncid_result | varchar | 255 |  | √ | ' ' |  |
| 28 | fdocvisible | fdocvisible | bpchar | 1 |  | √ | 'B' |  |
| 29 | fbomversion | fbomversion | varchar | 50 |  | √ | ' ' |  |
| 30 | fattachmenturl | fattachmenturl | varchar | 500 |  | √ | ' ' |  |
| 31 | fcontrolprotocol | fcontrolprotocol | varchar | 255 |  | √ | ' ' |  |
| 32 | fconfignumber | fconfignumber | varchar | 255 |  | √ | ' ' |  |
| 33 | fistop | fistop | bpchar | 1 |  | √ | '0' |  |
| 34 | fchangestatus | fchangestatus | bpchar | 1 |  | √ | 'A' |  |
| 35 | fcheckouttorid | fcheckouttorid | int8 | 64 |  | √ | 0 |  |
| 36 | freceivestatus | freceivestatus | bpchar | 1 |  | √ | 'N' |  |
| 37 | fflowid | fflowid | int8 | 64 |  | √ | 0 |  |
| 38 | fcontrolruletype | fcontrolruletype | varchar | 50 |  | √ | ' ' |  |
| 39 | fapplyorgid | fapplyorgid | int8 | 64 |  | √ | 0 |  |
| 40 | fconfigurable | fconfigurable | varchar | 50 |  | √ | ' ' |  |
| 41 | fcomment | fcomment | varchar | 256 |  | √ | ' ' |  |
| 42 | fspecialty | fspecialty | varchar | 50 |  | √ | ' ' |  |
| 43 | fviewid | fviewid | int8 | 64 |  | √ | 0 |  |
| 44 | fsubnewbomversion | fsubnewbomversion | int8 | 64 |  | √ | 0 |  |
| 45 | fsenduserid | fsenduserid | int8 | 64 |  | √ | 0 |  |
| 46 | fvalueaddedtype | fvalueaddedtype | bpchar | 1 |  | √ | 'A' |  |
| 47 | flatestbranch | flatestbranch | int8 | 64 |  | √ | 0 |  |
| 48 | fmatapplycode | fmatapplycode | int8 | 64 |  | √ | 0 |  |
| 49 | flargeversion | flargeversion | varchar | 50 |  | √ | ' ' |  |
| 50 | finvetory_type | finvetory_type | int8 | 64 |  | √ | 0 |  |
| 51 | fpicinstance | fpicinstance | varchar | 255 |  | √ | ' ' |  |
| 52 | fisfirstversion | fisfirstversion | int4 | 32 |  | √ | 0 |  |
| 53 | freceivetime | freceivetime | timestamp | 0 |  |  | null |  |
| 54 | flcstageid | flcstageid | int8 | 64 |  | √ | 0 |  |
| 55 | flatestversion | flatestversion | varchar | 10 |  | √ | ' ' |  |
| 56 | fobjlink | fobjlink | int8 | 64 |  | √ | 0 |  |
| 57 | fhead | fhead | int8 | 64 |  | √ | 0 |  |
| 58 | fdescriptionld | fdescriptionld | varchar | 255 |  | √ | ' ' |  |
| 59 | fpicflowstatus | fpicflowstatus | varchar | 255 |  | √ | ' ' |  |
| 60 | foperationtype | foperationtype | bpchar | 1 |  | √ | 'A' |  |
| 61 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 62 | fispushed | fispushed | bpchar | 1 |  | √ | '0' |  |
| 63 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 64 | felementdesc | felementdesc | varchar | 255 |  | √ | ' ' |  |
| 65 | fownerld | fownerld | int8 | 64 |  | √ | 0 |  |
| 66 | felementname | felementname | varchar | 50 |  | √ | ' ' |  |
| 67 | foptioninputmethod | foptioninputmethod | varchar | 50 |  | √ | ' ' |  |
| 68 | foptionminvalue | foptionminvalue | numeric | 23 | 10 | √ | 0 |  |
| 69 | foptionunitid | foptionunitid | int8 | 64 |  | √ | 0 |  |
| 70 | fenablestatus | fenablestatus | bpchar | 1 |  | √ | 'A' |  |
| 71 | foptionmustchoose | foptionmustchoose | bpchar | 1 |  | √ | '0' |  |
| 72 | fismarked | fismarked | bpchar | 1 |  | √ | '0' |  |
| 73 | foptionmulchoose | foptionmulchoose | varchar | 50 |  | √ | ' ' |  |
| 74 | fbaseunits | fbaseunits | int8 | 64 |  | √ | 0 |  |
| 75 | ftoptime | ftoptime | timestamp | 0 |  |  | null |  |
| 76 | fpiccheckout | fpiccheckout | varchar | 255 |  | √ | ' ' |  |
| 77 | fmaterial_attr | fmaterial_attr | varchar | 50 |  | √ | ' ' |  |
| 78 | ferpmaterialid | ferpmaterialid | int8 | 64 |  | √ | 0 |  |
| 79 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 80 | fheadrevision | fheadrevision | varchar | 50 |  | √ | ' ' |  |
| 81 | flcstatusid | flcstatusid | int8 | 64 |  | √ | 0 |  |
| 82 | fcheckoutstatus | fcheckoutstatus | varchar | 50 |  | √ | ' ' |  |
| 83 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 84 | fversiondetails | fversiondetails | varchar | 50 |  | √ | ' ' |  |
| 85 | fclassattrid | fclassattrid | int8 | 64 |  | √ | 0 |  |
| 86 | fchangetype | fchangetype | bpchar | 1 |  | √ | 'A' |  |
| 87 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 88 | fitemmasterid | fitemmasterid | int8 | 64 |  | √ | 0 |  |
| 89 | fworkingtime | fworkingtime | numeric | 23 | 10 | √ | 0 |  |
| 90 | fsynctime | fsynctime | timestamp | 0 |  |  | null |  |
| 91 | fworkcenterid | fworkcenterid | int8 | 64 |  | √ | 0 |  |
| 92 | fassociatedwpid | fassociatedwpid | int8 | 64 |  | √ | 0 |  |
| 93 | fchangetext | fchangetext | varchar | 2000 |  | √ | ' ' |  |
| 94 | ffactoryid | ffactoryid | int8 | 64 |  | √ | 0 |  |
| 95 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 96 | fisvirtualdoc | fisvirtualdoc | bpchar | 1 |  | √ | '0' |  |
| 97 | fchangereason | fchangereason | bpchar | 1 |  | √ | 'A' |  |
| 98 | fexecapplystatus | fexecapplystatus | bpchar | 1 |  | √ | 'A' |  |
| 99 | foptionmaxvalue | foptionmaxvalue | numeric | 23 | 10 | √ | 0 |  |
| 100 | fproctemp | fproctemp | varchar | 150 |  | √ | ' ' |  |
| 101 | fhasdraw | fhasdraw | bpchar | 1 |  | √ | 'N' |  |
| 102 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 103 | fsubnewversion | fsubnewversion | int8 | 64 |  | √ | 0 |  |
| 104 | fiscritical | fiscritical | bpchar | 1 |  | √ | '0' |  |

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
| 2 | flcstatusid | flcstatusid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 5 | frdmversion | frdmversion | varchar | 10 |  | √ | ' ' |  |
| 6 | fconfigcollectid | fconfigcollectid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 9 | fdatastagebit | fdatastagebit | int8 | 64 |  | √ | 1 |  |
| 10 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '-' |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fdomainid | fdomainid | int8 | 64 |  | √ | 0 |  |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 16 | fsyncresult | fsyncresult | varchar | 255 |  | √ | ' ' |  |
| 17 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 18 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 19 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 20 | fcontainerid | fcontainerid | int8 | 64 |  | √ | 0 |  |
| 21 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 22 | fbizorg | fbizorg | int8 | 64 |  | √ | 0 |  |
| 23 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | fdisplayname | fdisplayname | varchar | 1024 |  | √ | ' ' |  |
| 28 | fsummary_tag | fsummary_tag | text | 0 |  |  | null |  |
| 29 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 30 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 31 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 32 | ffolderdomain | ffolderdomain | int8 | 64 |  | √ | 0 |  |
| 33 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 34 | fnumber | 编码 | varchar | 85 |  | √ | ' ' | 编码 |
| 35 | fcadeditstatus | fcadeditstatus | bpchar | 1 |  | √ | '0' |  |
| 36 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 37 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 38 | fsummary | fsummary | varchar | 255 |  | √ | ' ' |  |

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
| 2 | fpriceandtax_ds | fpriceandtax_ds | varchar | 2000 |  | √ | ' ' |  |
| 3 | fversiondetails | fversiondetails | varchar | 50 |  | √ | ' ' |  |
| 4 | fmaterialnum | fmaterialnum | varchar | 50 |  | √ | ' ' |  |
| 5 | fcolor | fcolor | varchar | 255 |  | √ | ' ' |  |
| 6 | fislatestrevision | fislatestrevision | varchar | 10 |  | √ | ' ' |  |
| 7 | fitemmasterid | fitemmasterid | int8 | 64 |  | √ | 0 |  |
| 8 | finventoryqty_ds | finventoryqty_ds | varchar | 2000 |  | √ | ' ' |  |
| 9 | fprioritylevel | fprioritylevel | bpchar | 1 |  | √ | 'A' |  |
| 10 | fdrawnogroup | fdrawnogroup | int8 | 64 |  | √ | 0 |  |
| 11 | ficon | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 12 | fsecondaryversionid | fsecondaryversionid | int8 | 64 |  | √ | 0 |  |
| 13 | flargeversioncode | flargeversioncode | varchar | 50 |  | √ | ' ' |  |
| 14 | fupgradedesc | fupgradedesc | varchar | 2000 |  | √ | ' ' |  |
| 15 | fmaterial | fmaterial | varchar | 255 |  | √ | ' ' |  |
| 16 | feplanfullpagename | feplanfullpagename | varchar | 255 |  | √ | ' ' |  |
| 17 | ffixedleadtime | ffixedleadtime | int4 | 32 |  | √ | 0 |  |
| 18 | fpriceandtax | fpriceandtax | varchar | 50 |  | √ | ' ' |  |
| 19 | fperiodendprice | fperiodendprice | varchar | 50 |  | √ | ' ' |  |
| 20 | fcheckoutpath | fcheckoutpath | varchar | 500 |  | √ | ' ' |  |
| 21 | fcadtype | fcadtype | int8 | 64 |  | √ | 0 |  |
| 22 | fperiodendprice_ds | fperiodendprice_ds | varchar | 2000 |  | √ | ' ' |  |
| 23 | fdocmodel | fdocmodel | int8 | 64 |  | √ | 0 |  |
| 24 | fdocumenttemplate | fdocumenttemplate | int8 | 64 |  | √ | 0 |  |
| 25 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 26 | ffiletype | ffiletype | int4 | 32 |  | √ | 0 |  |
| 27 | fminiorversion | fminiorversion | varchar | 50 |  | √ | ' ' |  |
| 28 | fmatunitid | fmatunitid | int8 | 64 |  | √ | 0 |  |
| 29 | fminiorversioncode | fminiorversioncode | varchar | 50 |  | √ | ' ' |  |
| 30 | fversionid | fversionid | int8 | 64 |  | √ | 0 |  |
| 31 | fpictureno | fpictureno | varchar | 50 |  | √ | ' ' |  |
| 32 | funitfield | funitfield | int4 | 32 |  | √ | 0 |  |
| 33 | fpdffile | fpdffile | int8 | 64 |  | √ | 0 |  |
| 34 | fdocthumbnail | fdocthumbnail | varchar | 255 |  | √ | ' ' |  |
| 35 | fvisuallizationfile | fvisuallizationfile | int8 | 64 |  | √ | 0 |  |
| 36 | finventoryqty | finventoryqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fqtyfield | fqtyfield | numeric | 23 | 10 | √ | 0 |  |
| 38 | fphysicalfile | fphysicalfile | int8 | 64 |  | √ | 0 |  |
| 39 | fspec | fspec | varchar | 255 |  | √ | ' ' |  |
| 40 | fmaincontentsource | fmaincontentsource | varchar | 50 |  | √ | ' ' |  |
| 41 | fsubnewversion | fsubnewversion | int8 | 64 |  | √ | 0 |  |
| 42 | flargeversion | flargeversion | varchar | 50 |  | √ | ' ' |  |
| 43 | fmatqty | fmatqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fbaseqty_ds | fbaseqty_ds | varchar | 2000 |  | √ | ' ' |  |
| 45 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | ffqty | ffqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | funit | funit | int8 | 64 |  | √ | 0 |  |
| 48 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_basic_r_ver |  | fversionid |
| 2 | pk_plm_pdm_basic_mr |  | fid |
