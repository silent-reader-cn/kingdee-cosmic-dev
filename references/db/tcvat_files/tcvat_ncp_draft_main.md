# 农产品核定扣除计算抵扣-tcvat_ncp_draft_main

## 附件字段-附件表 t_tpo_sbzb_tsd_at

- **表名称：** 附件字段-附件表
- **表名：** t_tpo_sbzb_tsd_at

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tpo_sbzb_tsd_at |  | fpkid |
| 2 | idx_t_tpo_sbzb_tsd_at_fid |  | fid |

---

## 农产品核定扣除计算抵扣-主表 t_tpo_declare_main_tsd

- **表名称：** 农产品核定扣除计算抵扣-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 7 | fcurrentperiodamount | 本期数 | numeric | 23 | 10 | √ | 0 | 本期数 |
| 8 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 9 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 10 | fcurrentyearamount | 本年数 | numeric | 23 | 10 | √ | 0 | 本年数 |
| 11 | fhyncpmcid | 耗用农产品名称 | int8 | 64 |  | √ | 0 | 耗用农产品名称 tcvat_hyncp_name |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 14 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 15 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 18 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 19 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 20 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 21 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 22 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 23 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 24 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 25 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fgeneratebusinessdoc | 生成业务单据 | bpchar | 1 |  | √ | '0' | 生成业务单据 |
| 28 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 29 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |
| 30 | fbusinessdocno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 31 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 34 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 37 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 38 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 39 | fnsrmc | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 40 | ftype | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型,枚举: WP11 :居民企业底稿 WP12 :居民企业分支机构底稿 WP13 :核定征收底稿 WP14 :非居民企业底稿 |
| 41 | fdraftstatus | 底稿状态 | varchar | 50 |  | √ | ' ' | 底稿状态,枚举: |
| 42 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 43 | fpzhc | 凭证红冲 | varchar | 50 |  | √ | ' ' | 凭证红冲,枚举: 1 :是 0 :否 |
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

---

## 单据体-子表 t_tcvat_ncp_draft

- **表名称：** 单据体-子表
- **表名：** t_tcvat_ncp_draft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhyncpcount | 耗用农产品数量 | numeric | 23 | 10 | √ | 0 | 耗用农产品数量 |
| 3 | fselfproductsale | 自产货物销售数量 | numeric | 23 | 10 | √ | 0 | 自产货物销售数量 |
| 4 | fdirectsalescount | 直接销售农产品数量 | numeric | 23 | 10 | √ | 0 | 直接销售农产品数量 |
| 5 | fallowdeducttax | 允许抵扣进项税额合计 | numeric | 23 | 10 | √ | 0 | 允许抵扣进项税额合计 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffarmdeducttype | 核定扣除计算方法 | varchar | 50 |  | √ | ' ' | 核定扣除计算方法,枚举: none :不适用 in-out :投入产出法 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ncp_draft |  | fentryid |
| 2 | idx_tcvat_ncp_draft_fk |  | fid |
