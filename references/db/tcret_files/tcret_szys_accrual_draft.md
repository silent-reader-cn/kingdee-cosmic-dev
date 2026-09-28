# 水资源税计提底稿编制（旧）-tcret_szys_accrual_draft

## 单据体-子表 t_tcret_accrual_entry

- **表名称：** 单据体-子表
- **表名：** t_tcret_accrual_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemno | fitemno | varchar | 50 |  | √ | ' ' |  |
| 3 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 4 | ftaxrate | ftaxrate | varchar | 50 |  | √ | ' ' |  |
| 5 | ftaxitem | ftaxitem | varchar | 50 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbosorg | fbosorg | int8 | 64 |  | √ | 0 |  |
| 8 | fdetails | fdetails | varchar | 255 |  | √ | ' ' |  |
| 9 | fsyse | 适用税额 | numeric | 23 | 10 | √ | 0 | 适用税额 |
| 10 | fdetails_tag | fdetails_tag | text | 0 |  |  | null |  |
| 11 | fsqljqsl | 上期累计取水量 | numeric | 23 | 10 | √ | 0 | 上期累计取水量 |
| 12 | fzszmid | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_szys_bizdef_entry |
| 13 | fbizdimensiontype | fbizdimensiontype | varchar | 50 |  | √ | ' ' |  |
| 14 | fcreatetype | 生成来源 | varchar | 50 |  | √ | ' ' | 生成来源,枚举: system :系统生成 hand :手工添加 |
| 15 | fsubtaxitem | fsubtaxitem | int8 | 64 |  | √ | 0 |  |
| 16 | ftaxmonth | ftaxmonth | timestamp | 0 |  |  | null |  |
| 17 | fhbssl | fhbssl | numeric | 23 | 10 | √ | 0 |  |
| 18 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 19 | ftaxsourceid | 税源编号 | int8 | 64 |  | √ | 0 | [水资源税税源登记信息 tdm_water_source_dj](../tdm_files/tdm_water_source_dj.md) |
| 20 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 21 | fdeductiontype | fdeductiontype | varchar | 50 |  | √ | ' ' |  |
| 22 | fhdbl | fhdbl | numeric | 23 | 10 |  | null |  |
| 23 | fjsje | fjsje | numeric | 23 | 10 | √ | 0 |  |
| 24 | fbizdimensionname | fbizdimensionname | varchar | 200 |  | √ | ' ' |  |
| 25 | ftaxlimit | ftaxlimit | varchar | 50 |  | √ | ' ' |  |
| 26 | fbusdimensionmap | fbusdimensionmap | int8 | 64 |  | √ | 0 |  |
| 27 | fjtynse | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 28 | fprojectname | fprojectname | varchar | 50 |  | √ | ' ' |  |
| 29 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 30 | fbusdimension | fbusdimension | int8 | 64 |  | √ | 0 |  |
| 31 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 32 | fbizdimensionid | fbizdimensionid | varchar | 50 |  | √ | ' ' |  |
| 33 | fedit | fedit | bpchar | 1 |  | √ | '0' |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fcalsource | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_accrual_entry_fk |  | fid |
| 2 | pk_tcret_accrual_entry |  | fentryid |

---

## 水资源税计提底稿编制（旧）-主表 t_tpo_declare_main_tsd

- **表名称：** 水资源税计提底稿编制（旧）-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fremarks | fremarks | varchar | 2000 |  | √ | ' ' |  |
| 5 | ftemplatetype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: yhs :印花税计提底稿 fcs :房产税计提底稿 cztdsys :城镇土地使用税计提底稿 |
| 6 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 7 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 8 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 11 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 14 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 15 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 计提底稿编号 | varchar | 100 |  | √ | ' ' | 计提底稿编号 |
| 17 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 18 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 19 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 20 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 25 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 26 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 27 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 28 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 29 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fpzhc | 凭证红冲 | varchar | 50 |  | √ | ' ' | 凭证红冲,枚举: 1 :是 0 :否 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 34 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | faccrualdate | 计提日期 | timestamp | 0 |  |  | null | 计提日期 |
| 36 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | faccrualplan | 计提方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 38 | fhjybtse | fhjybtse | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 43 | fjtnumber | fjtnumber | varchar | 100 |  | √ | ' ' |  |
| 44 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 45 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 46 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
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
