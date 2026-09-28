# 比对底稿查询-tcvat_rta_query

## 单据体-子表 t_tcvat_rta_entry

- **表名称：** 单据体-子表
- **表名：** t_tcvat_rta_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcswhjsscyje | 城市维护建设税差异金额 | numeric | 23 | 10 | √ | 0 | 城市维护建设税差异金额 |
| 3 | fynsecyje | 应纳税额差异金额 | numeric | 23 | 10 | √ | 0 | 应纳税额差异金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fjxsezccyje | 进项税额转出差异金额 | numeric | 23 | 10 | √ | 0 | 进项税额转出差异金额 |
| 6 | fxsecyje | 销售额差异金额 | numeric | 23 | 10 | √ | 0 | 销售额差异金额 |
| 7 | fjjdjsecyje | 加计抵减税额差异金额 | numeric | 23 | 10 | √ | 0 | 加计抵减税额差异金额 |
| 8 | fjxsecyje | 进项税额差异金额 | numeric | 23 | 10 | √ | 0 | 进项税额差异金额 |
| 9 | fxxsecyje | 销项税额差异金额 | numeric | 23 | 10 | √ | 0 | 销项税额差异金额 |
| 10 | fjyffjcyje | 教育费附加差异金额 | numeric | 23 | 10 | √ | 0 | 教育费附加差异金额 |
| 11 | fzzsybtsecye | 增值税应补（退）税额差异额 | numeric | 23 | 10 | √ | 0 | 增值税应补（退）税额差异额 |
| 12 | fyjsecyje | 已缴税额差异金额 | numeric | 23 | 10 | √ | 0 | 已缴税额差异金额 |
| 13 | fdfjyfjcyje | 地方教育附加差异金额 | numeric | 23 | 10 | √ | 0 | 地方教育附加差异金额 |
| 14 | fynsejzecyje | 应纳税额减征额差异金额 | numeric | 23 | 10 | √ | 0 | 应纳税额减征额差异金额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_rta_entry |  | fentryid |
| 2 | idx_tcvat_rta_entry_fk |  | fid |

---

## 比对底稿查询-主表 t_tpo_declare_main_tsd

- **表名称：** 比对底稿查询-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 3 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 6 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 7 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 8 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 9 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 10 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 15 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 18 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 19 | ftaxareagroup | ftaxareagroup | int8 | 64 |  | √ | 0 |  |
| 20 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 21 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 22 | fbillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
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
| 37 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 38 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 39 | fnsrmc | fnsrmc | varchar | 50 |  | √ | ' ' |  |
| 40 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 41 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fjtynsesum | fjtynsesum | numeric | 23 | 10 | √ | 0 |  |
| 43 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :引入 1 :系统生成 |

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
