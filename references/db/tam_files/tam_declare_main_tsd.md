# 计提底稿任务-tam_declare_main_tsd

## 计提底稿任务-主表 t_tpo_declare_main_tsd

- **表名称：** 计提底稿任务-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 6 | fremarks | fremarks | varchar | 2000 |  | √ | ' ' |  |
| 7 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 8 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 9 | ftemplatetype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: draft_qysdsjb :企业所得税预缴计提底稿 sdsjt_bd :递延所得税计提（本地） sdsjt_jt :递延所得税计提（集团） yhs :印花税计提底稿 fcs :房产税计提底稿 cztdsys :城镇土地使用税计提底稿 hjbhs :环保税计提底稿 ccs :车船税计提底稿 szys :水资源税计提底稿 draft_zzsybnsr_sjjt :增值税计提底稿_一般纳税人 draft_zzsxgmnsr_sjjt :增值税计提底稿_小规模纳税人 draft_zzsybnsr_ybhz_sjjt :增值税计提底稿_一般企业汇总申报 draft_zzsybnsr_hz_zjg_sjjt :增值税计提底稿_一般企业汇总申报仅汇总 draft_zzsybnsr_yz_zjg_sjjt :增值税计提底稿_一般企业汇总申报预征方式总机构 |
| 10 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 15 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fskssqz | 所属期至 | timestamp | 0 |  |  | null | 所属期至 |
| 18 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 19 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 20 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 21 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 22 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 23 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 24 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 25 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fgeneratebusinessdoc | 生成计提单 | bpchar | 1 |  | √ | '0' | 生成计提单 |
| 28 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 29 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 30 | fbusinessdocno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 31 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 34 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 37 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 38 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 39 | fnsrmc | fnsrmc | varchar | 50 |  | √ | ' ' |  |
| 40 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 41 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 43 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
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
