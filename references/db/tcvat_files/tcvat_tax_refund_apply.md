# 留抵退税申请查询-tcvat_tax_refund_apply

## 单据体-子表 t_tcvat_refund_apply

- **表名称：** 单据体-子表
- **表名：** t_tcvat_refund_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbljd | 办理进度 | varchar | 50 |  | √ | ' ' | 办理进度,枚举: wsq :未申请 ysq :已申请 zyts :准予退税 yts :已退税 |
| 3 | fzytssj | 准予退税时间 | varchar | 50 |  | √ | ' ' | 准予退税时间 |
| 4 | fbqsqthdclldse | 本期申请退还的存量留抵税额 | numeric | 23 | 10 | √ | 0 | 本期申请退还的存量留抵税额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsqthxm | 申请退还项目 | varchar | 50 |  | √ | ' ' | 申请退还项目,枚举: clldse :存量留抵税额 zlldse :增量留抵税额 clzl :存量留抵税额、增量留抵税额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbqsqthdzlldse | 本期申请退还的增量留抵税额 | numeric | 23 | 10 | √ | 0 | 本期申请退还的增量留抵税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_refund_apply_fk |  | fid |
| 2 | pk_tcvat_refund_apply |  | fentryid |

---

## 留抵退税申请查询-主表 t_tpo_declare_main_tsd

- **表名称：** 留抵退税申请查询-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 3 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
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
| 22 | fbillno | 申请表编码 | varchar | 100 |  | √ | ' ' | 申请表编码 |
| 23 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 24 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 25 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fgeneratebusinessdoc | 生成业务单据 | bpchar | 1 |  | √ | '0' | 生成业务单据 |
| 28 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 29 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |
| 30 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 31 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | faccountsettype | faccountsettype | varchar | 50 |  | √ | ' ' |  |
| 34 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 37 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 38 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 39 | fnsrmc | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 40 | ftype | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型,枚举: WP11 :居民企业底稿 WP12 :居民企业分支机构底稿 WP13 :核定征收底稿 WP14 :非居民企业底稿 tcvat_taxrefund :留抵退税申请表 |
| 41 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fjtynsesum | fjtynsesum | numeric | 23 | 10 | √ | 0 |  |
| 43 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 |

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
