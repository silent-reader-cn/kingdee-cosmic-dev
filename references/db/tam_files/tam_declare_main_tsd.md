# 计提底稿任务-tam_declare_main_tsd

## 计提底稿任务-主表 t_tpo_declare_main_tsd

- **表名称：** 计提底稿任务-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fremarks | fremarks | varchar | 2000 |  | √ | ' ' |  |
| 5 | ftemplatetype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: draft_qysdsjb :企业所得税预缴计提底稿 sdsjt_bd :递延所得税计提（本地） sdsjt_jt :递延所得税计提（集团） yhs :印花税计提底稿 fcs :房产税计提底稿 cztdsys :城镇土地使用税计提底稿 hjbhs :环保税计提底稿 ccs :车船税计提底稿 szys :水资源税计提底稿 draft_zzsybnsr_sjjt :增值税计提底稿_一般纳税人 draft_zzsxgmnsr_sjjt :增值税计提底稿_小规模纳税人 draft_zzsybnsr_ybhz_sjjt :增值税计提底稿_一般企业汇总申报 draft_zzsybnsr_hz_zjg_sjjt :增值税计提底稿_一般企业汇总申报仅汇总 draft_zzsybnsr_yz_zjg_sjjt :增值税计提底稿_一般企业汇总申报预征方式总机构 hwqysds :海外所得税计提底稿 hwzzs :海外增值税计提底稿 |
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
| 16 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 17 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 18 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 19 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 20 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusinessdocno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 25 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 26 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 27 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 28 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 29 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 34 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 36 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 38 | fhjybtse | fhjybtse | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 所属期至 | timestamp | 0 |  |  | null | 所属期至 |
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
