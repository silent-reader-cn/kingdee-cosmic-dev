# 水资源税计提底稿编制-tcret_szys_accrual_draft

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
| 19 | ftaxsourceid | 税源编号 | int8 | 64 |  | √ | 0 | 税源登记信息 tdm_water_source_dj |
| 20 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 21 | fdeductiontype | fdeductiontype | varchar | 50 |  | √ | ' ' |  |
| 22 | fhdbl | fhdbl | numeric | 23 | 10 |  | null |  |
| 23 | fjsje | fjsje | numeric | 23 | 10 | √ | 0 |  |
| 24 | fbizdimensionname | fbizdimensionname | varchar | 200 |  | √ | ' ' |  |
| 25 | ftaxlimit | ftaxlimit | varchar | 50 |  | √ | ' ' |  |
| 26 | fjtynse | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 27 | fprojectname | fprojectname | varchar | 50 |  | √ | ' ' |  |
| 28 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 29 | fbizdimensionid | fbizdimensionid | varchar | 50 |  | √ | ' ' |  |
| 30 | fedit | fedit | bpchar | 1 |  | √ | '0' |  |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fcalsource | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |

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

## 水资源税计提底稿编制-主表 t_tpo_declare_main_tsd

- **表名称：** 水资源税计提底稿编制-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | faccrualdate | 计提日期 | timestamp | 0 |  |  | null | 计提日期 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 6 | fremarks | fremarks | varchar | 2000 |  | √ | ' ' |  |
| 7 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 8 | faccrualplan | 计提方案 | int8 | 64 |  | √ | 0 | 计提方案 itp_proviston_plan |
| 9 | ftemplatetype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: yhs :印花税计提底稿 fcs :房产税计提底稿 cztdsys :城镇土地使用税计提底稿 |
| 10 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 15 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 18 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 19 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 20 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 21 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 22 | fbillno | 计提底稿编号 | varchar | 100 |  | √ | ' ' | 计提底稿编号 |
| 23 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 24 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 25 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fgeneratebusinessdoc | 生成计提单 | bpchar | 1 |  | √ | '0' | 生成计提单 |
| 28 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 29 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 30 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 31 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 34 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 37 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 38 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 39 | fnsrmc | fnsrmc | varchar | 50 |  | √ | ' ' |  |
| 40 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 41 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 43 | fpzhc | 凭证红冲 | varchar | 50 |  | √ | ' ' | 凭证红冲,枚举: 1 :是 0 :否 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |

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
