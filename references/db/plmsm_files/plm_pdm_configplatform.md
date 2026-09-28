# 配置平台-plm_pdm_configplatform

## 字典配置-子表 t_plm_pdm_relation

- **表名称：** 字典配置-子表
- **表名：** t_plm_pdm_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeltagnum_tag | fdeltagnum_tag | text | 0 |  |  | null |  |
| 3 | febomentryid | febomentryid | int8 | 64 |  | √ | 0 |  |
| 4 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: A :关联关系 B :组合关系 C :聚合关系 |
| 5 | flayer | flayer | varchar | 50 |  | √ | ' ' |  |
| 6 | fconfigcategory | 业务类型 | varchar | 255 |  | √ | ' ' | 业务类型,枚举: A :配置字典 B :选项组 C :选项 D :选项值 |
| 7 | fmodelid | 模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 8 | foptype | foptype | varchar | 50 |  | √ | ' ' |  |
| 9 | flocation | flocation | varchar | 255 |  | √ | ' ' |  |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fconfigname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | faddtagnum_tag | faddtagnum_tag | text | 0 |  |  | null |  |
| 14 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 15 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 16 | fprinttemplateid | fprinttemplateid | varchar | 50 |  | √ | ' ' |  |
| 17 | finputmethod | 输入方式 | varchar | 50 |  | √ | ' ' | 输入方式,枚举: enum :枚举 input :输入 |
| 18 | foptiontype | 选项类型 | varchar | 50 |  | √ | ' ' | 选项类型,枚举: A :销售 B :工程 |
| 19 | flineno | flineno | int4 | 32 |  | √ | 0 |  |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 21 | fconfigmaxvalue | 最大值 | numeric | 23 | 10 | √ | 0 | 最大值 |
| 22 | freplacemethod | freplacemethod | varchar | 50 |  | √ | ' ' |  |
| 23 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 24 | fismodify | fismodify | bpchar | 1 |  | √ | '0' |  |
| 25 | frepinvaliddate | frepinvaliddate | timestamp | 0 |  |  | null |  |
| 26 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fenablestatus | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 1 :启用 0 :禁用 |
| 28 | freplacestra | freplacestra | varchar | 50 |  | √ | ' ' |  |
| 29 | fdeno | fdeno | numeric | 23 | 10 | √ | 1 |  |
| 30 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | ftagnum | ftagnum | varchar | 2000 |  | √ | ' ' |  |
| 32 | fplannedexpireddate | fplannedexpireddate | timestamp | 0 |  |  | null |  |
| 33 | fderive | fderive | varchar | 50 |  | √ | ' ' |  |
| 34 | fparent_material | fparent_material | int8 | 64 |  | √ | 0 |  |
| 35 | fcompletedstate | fcompletedstate | bpchar | 1 |  | √ | ' ' |  |
| 36 | fconfigdescription_tag | 描述_详情 | text | 0 |  |  | null | 描述_详情 |
| 37 | frowkey | frowkey | varchar | 50 |  | √ | ' ' |  |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | ftargetid | 配置对象 | int8 | 64 |  | √ | 0 | [字典配置业务模型 plm_pdm_dictconfig](../plmsm_files/plm_pdm_dictconfig.md) |
| 40 | fdeltagnum | fdeltagnum | varchar | 2000 |  | √ | ' ' |  |
| 41 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :文本 qty :数量 date :日期 basedata :基础资料 Assistant :辅助资料 |
| 42 | fchangeobjectid | fchangeobjectid | int8 | 64 |  | √ | 0 |  |
| 43 | fendid | fendid | int8 | 64 |  | √ | 0 |  |
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
| 58 | fbeginid | fbeginid | int8 | 64 |  | √ | 0 |  |
| 59 | ffromtab | ffromtab | varchar | 50 |  | √ | ' ' |  |
| 60 | feffectdate | feffectdate | timestamp | 0 |  |  | null |  |
| 61 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | fmfgbomentryid | fmfgbomentryid | int8 | 64 |  | √ | 0 |  |
| 63 | factualusage | factualusage | numeric | 23 | 10 | √ | 0 |  |
| 64 | frepeffectdate | frepeffectdate | timestamp | 0 |  |  | null |  |
| 65 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 66 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
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

---

## 配置平台-使用范围表 t_plm_pdm_basic_u

- **表名称：** 配置平台-使用范围表
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

## 配置平台-多语言表 t_plm_pdm_basic_l

- **表名称：** 配置平台-多语言表
- **表名：** t_plm_pdm_basic_l

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
| 1 | pk_plm_pdm_basic_l |  | fpkid |
| 2 | idx_plm_pdm_basic_l_0 |  | fid,flocaleid |

---

## 配置平台-分表 t_plm_pdm_basic_mb

- **表名称：** 配置平台-分表
- **表名：** t_plm_pdm_basic_mb

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
| 12 | fchangemode | fchangemode | bpchar | 1 |  | √ | 'A' |  |
| 13 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 14 | fplannedexpireddate | 计划失效时间 | timestamp | 0 |  |  | null | 计划失效时间 |
| 15 | fminiorversion | 当前小版本 | varchar | 50 |  | √ | ' ' | 当前小版本 |
| 16 | fprocno | fprocno | int8 | 64 |  | √ | 0 |  |
| 17 | fcollapsible | fcollapsible | bpchar | 1 |  | √ | '0' |  |
| 18 | flinkmodeltype | flinkmodeltype | int8 | 64 |  | √ | 0 |  |
| 19 | frelobjcount | frelobjcount | int4 | 32 |  | √ | 0 |  |
| 20 | fmfgbomid | fmfgbomid | int8 | 64 |  | √ | 0 |  |
| 21 | fflowstatus | 流程标识 | varchar | 50 |  | √ | ' ' | 流程标识,枚举: A : B :流程中 C : |
| 22 | freceiveuserid | freceiveuserid | int8 | 64 |  | √ | 0 |  |
| 23 | flistcontrol | 列表控制 | int8 | 64 |  | √ | 0 | 列表控制 |
| 24 | fchangesource | fchangesource | bpchar | 1 |  | √ | 'A' |  |
| 25 | fcustomversiondetails | 客制版本 | varchar | 50 |  | √ | ' ' | 客制版本 |
| 26 | fmainid | fmainid | int8 | 64 |  | √ | 0 |  |
| 27 | fsyncid_result | ID同步结果 | varchar | 255 |  | √ | ' ' | ID同步结果 |
| 28 | fdocvisible | fdocvisible | bpchar | 1 |  | √ | 'B' |  |
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
| 47 | flatestbranch | flatestbranch | int8 | 64 |  | √ | 0 |  |
| 48 | fmatapplycode | fmatapplycode | int8 | 64 |  | √ | 0 |  |
| 49 | flargeversion | 当前大版本 | varchar | 50 |  | √ | ' ' | 当前大版本 |
| 50 | finvetory_type | finvetory_type | int8 | 64 |  | √ | 0 |  |
| 51 | fpicinstance | 对象图标 | varchar | 255 |  | √ | ' ' | 对象图标 |
| 52 | fisfirstversion | fisfirstversion | int4 | 32 |  | √ | 0 |  |
| 53 | freceivetime | freceivetime | timestamp | 0 |  |  | null |  |
| 54 | flcstageid | 生命周期阶段 | int8 | 64 |  | √ | 0 | [生命周期阶段 plm_lc_stage](../plmsm_files/plm_lc_stage.md) |
| 55 | flatestversion | flatestversion | varchar | 10 |  | √ | ' ' |  |
| 56 | fobjlink | fobjlink | int8 | 64 |  | √ | 0 |  |
| 57 | fhead | fhead | int8 | 64 |  | √ | 0 |  |
| 58 | fdescriptionld | fdescriptionld | varchar | 255 |  | √ | ' ' |  |
| 59 | fpicflowstatus | 数据状态图标 | varchar | 255 |  | √ | ' ' | 数据状态图标 |
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
| 72 | fismarked | 标记 | bpchar | 1 |  | √ | '0' | 标记 |
| 73 | foptionmulchoose | foptionmulchoose | varchar | 50 |  | √ | ' ' |  |
| 74 | fbaseunits | fbaseunits | int8 | 64 |  | √ | 0 |  |
| 75 | ftoptime | 置顶日期 | timestamp | 0 |  |  | null | 置顶日期 |
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
| 87 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 88 | fitemmasterid | 主数据 | int8 | 64 |  | √ | 0 | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
| 89 | fworkingtime | fworkingtime | numeric | 23 | 10 | √ | 0 |  |
| 90 | fsynctime | fsynctime | timestamp | 0 |  |  | null |  |
| 91 | fworkcenterid | fworkcenterid | int8 | 64 |  | √ | 0 |  |
| 92 | fassociatedwpid | fassociatedwpid | int8 | 64 |  | √ | 0 |  |
| 93 | fchangetext | fchangetext | varchar | 2000 |  | √ | ' ' |  |
| 94 | ffactoryid | ffactoryid | int8 | 64 |  | √ | 0 |  |
| 95 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 96 | fisvirtualdoc | 是否虚文档 | bpchar | 1 |  | √ | '0' | 是否虚文档 |
| 97 | fchangereason | fchangereason | bpchar | 1 |  | √ | 'A' |  |
| 98 | fexecapplystatus | fexecapplystatus | bpchar | 1 |  | √ | 'A' |  |
| 99 | foptionmaxvalue | foptionmaxvalue | numeric | 23 | 10 | √ | 0 |  |
| 100 | fproctemp | fproctemp | varchar | 150 |  | √ | ' ' |  |
| 101 | fhasdraw | fhasdraw | bpchar | 1 |  | √ | 'N' |  |
| 102 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 103 | fsubnewversion | 次新版本 | int8 | 64 |  | √ | 0 | [业务模型 plm_pdm_basicbiz](../plmsm_files/plm_pdm_basicbiz.md) |
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

## 配置平台-主表 t_plm_pdm_basic

- **表名称：** 配置平台-主表
- **表名：** t_plm_pdm_basic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flcstatusid | 流程状态 | int8 | 64 |  | √ | 0 | [流程状态 plm_lc_status](../plmsm_files/plm_lc_status.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 5 | frdmversion | 系统版本 | varchar | 10 |  | √ | ' ' | 系统版本 |
| 6 | fconfigcollectid | fconfigcollectid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdatastagebit | 数据阶段位 | int8 | 64 |  | √ | 1 | 数据阶段位 |
| 10 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '-' |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdomainid | 域 | int8 | 64 |  | √ | 0 | 域 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsyncresult | 同步结果 | varchar | 255 |  | √ | ' ' | 同步结果 |
| 17 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fcontainerid | 上下文 | int8 | 64 |  | √ | 0 | [上下文容器 plm_plmsm_container](../plmsm_files/plm_plmsm_container.md) |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbizorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fdisplayname | 显示名称 | varchar | 1024 |  | √ | ' ' | 显示名称 |
| 28 | fsummary_tag | 显示名称_作废_详情 | text | 0 |  |  | null | 显示名称_作废_详情 |
| 29 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 30 | fctrlstrategy | 研发信息控制策略 | varchar | 50 |  | √ | ' ' | 研发信息控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fownerid | 所有者 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | ffolderdomain | ffolderdomain | int8 | 64 |  | √ | 0 |  |
| 33 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 85 |  | √ | ' ' | 编码 |
| 35 | fcadeditstatus | fcadeditstatus | bpchar | 1 |  | √ | '0' |  |
| 36 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 37 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 38 | fsummary | 显示名称_作废 | varchar | 255 |  | √ | ' ' | 显示名称_作废 |

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

## 配置平台-分表 t_plm_pdm_basic_mr

- **表名称：** 配置平台-分表
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
| 11 | ficon | ficon | varchar | 255 |  | √ | ' ' |  |
| 12 | fsecondaryversionid | 次新版次 | int8 | 64 |  | √ | 0 | 次新版次 |
| 13 | flargeversioncode | flargeversioncode | varchar | 50 |  | √ | ' ' |  |
| 14 | fupgradedesc | 升版描述 | varchar | 2000 |  | √ | ' ' | 升版描述 |
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
| 30 | fversionid | 最新版次 | int8 | 64 |  | √ | 0 | 最新版次 |
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

---

## 约束规则单据体-子表 t_plmpcm_contrulerelation

- **表名称：** 约束规则单据体-子表
- **表名：** t_plmpcm_contrulerelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fruleresult | 结果 | varchar | 255 |  | √ | ' ' | 结果 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 1 :字典 2 :选项分配 |
| 6 | fcontrolruledynid | 约束规则 | int8 | 64 |  | √ | 0 | [约束规则 plm_pdm_controlrule](../plmsm_files/plm_pdm_controlrule.md) |
| 7 | ftipinformation | 提示信息 | varchar | 255 |  | √ | ' ' | 提示信息 |
| 8 | frulecondition | 条件 | varchar | 255 |  | √ | ' ' | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmpcm_contrulerelation |  | fentryid |
| 2 | idx_plmpcm_rulerelation_fid |  | fid |
