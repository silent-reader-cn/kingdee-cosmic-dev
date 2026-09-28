# 印花税比对底稿编制-tcret_compare_yhs

## 印花税比对底稿编制-主表 t_tpo_declare_main_tsd

- **表名称：** 印花税比对底稿编制-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fremarks | fremarks | varchar | 2000 |  | √ | ' ' |  |
| 5 | ftemplatetype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: yhs_bd :印花税计提比对底稿 |
| 6 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 7 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 8 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 11 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | ftotalsbse | 申报税额合计 | numeric | 23 | 10 | √ | 0 | 申报税额合计 |
| 14 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 15 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 17 | ffrequency | 比对频次 | varchar | 50 |  | √ | ' ' | 比对频次,枚举: season :季度 year :年度 |
| 18 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 19 | ftotalbtse | 补提税额合计 | numeric | 23 | 10 | √ | 0 | 补提税额合计 |
| 20 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 比对期间起 | timestamp | 0 |  |  | null | 比对期间起 |
| 25 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 26 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 27 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 28 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 29 | fjtynsesum | fjtynsesum | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 34 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 35 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 36 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 38 | fhjybtse | fhjybtse | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 比对期间止 | timestamp | 0 |  |  | null | 比对期间止 |
| 43 | fjtnumber | fjtnumber | varchar | 100 |  | √ | ' ' |  |
| 44 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 45 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 46 | ftotaljtse | 计提税额合计 | numeric | 23 | 10 | √ | 0 | 计提税额合计 |
| 47 | fsbbno | fsbbno | varchar | 100 |  | √ | ' ' |  |
| 48 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fgeneratebusinessdoc | 生成计提单 | bpchar | 1 |  | √ | '0' | 生成计提单 |
| 51 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 54 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 55 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 56 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 57 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 58 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 59 | fdeadline | fdeadline | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tpo_declare_main_tsd |  | fid |
| 2 | idx_declare_main_tsd_fbillno |  | fbillno |
| 3 | idx_decl_main_tsd_orgid_qzme |  | forgid,fskssqq,fskssqz,ftaxsystem,faccountsettype |

---

## 单据体-子表 t_tcret_compare_entry

- **表名称：** 单据体-子表
- **表名：** t_tcret_compare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbtse | 补提税额 | numeric | 23 | 10 | √ | 0 | 补提税额 |
| 4 | fprojectnumber | fprojectnumber | int8 | 64 |  | √ | 0 |  |
| 5 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 6 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: season :季度 year :年度 single :按次 |
| 7 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 8 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 9 | flandnumber | flandnumber | int8 | 64 |  | √ | 0 |  |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fjtse | 计提税额 | numeric | 23 | 10 | √ | 0 | 计提税额 |
| 12 | fprojectname | fprojectname | varchar | 50 |  | √ | ' ' |  |
| 13 | fsbse | 申报税额 | numeric | 23 | 10 | √ | 0 | 申报税额 |
| 14 | fbizdimensiontype | 业务维度 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fitemnumber | fitemnumber | varchar | 50 |  | √ | ' ' |  |
| 16 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 18 | ftaxoffice | ftaxoffice | int8 | 64 |  | √ | 0 |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_compare_entry_fk |  | fid |
| 2 | pk_tcret_compare_entry |  | fentryid |
