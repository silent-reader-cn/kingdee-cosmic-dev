# 农产品核定扣除计算抵扣查询-tcvat_ncp_draft_main

## 附件字段-附件表 t_tpo_sbzb_tsd_at

- **表名称：** 附件字段-附件表
- **表名：** t_tpo_sbzb_tsd_at

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
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

---

## 农产品核定扣除计算抵扣查询-主表 t_tpo_declare_main_tsd

- **表名称：** 农产品核定扣除计算抵扣查询-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 4 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 6 | fcurrentyearamount | 本年数 | numeric | 23 | 10 | √ | 0 | 本年数 |
| 7 | fhyncpmcid | 耗用农产品名称 | int8 | 64 |  | √ | 0 | [耗用农产品名称 tcvat_hyncp_name](../tcvat_files/tcvat_hyncp_name.md) |
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
| 20 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |
| 21 | fbusinessdocno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 25 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 26 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 27 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 28 | fdraftstatus | 底稿状态 | varchar | 50 |  | √ | ' ' | 底稿状态,枚举: |
| 29 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fpzhc | 凭证红冲 | varchar | 50 |  | √ | ' ' | 凭证红冲,枚举: 1 :是 0 :否 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 2 :数据导入 1 :系统生成 |
| 34 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 36 | fcurrentperiodamount | 本期数 | numeric | 23 | 10 | √ | 0 | 本期数 |
| 37 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 38 | fhjybtse | fhjybtse | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 40 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 43 | fjtnumber | fjtnumber | varchar | 100 |  | √ | ' ' |  |
| 44 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 45 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 46 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsbbno | fsbbno | varchar | 100 |  | √ | ' ' |  |
| 48 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fgeneratebusinessdoc | 生成业务单据 | bpchar | 1 |  | √ | '0' | 生成业务单据 |
| 51 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 54 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 55 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 56 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 57 | ftype | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型,枚举: WP11 :居民企业底稿 WP12 :居民企业分支机构底稿 WP13 :核定征收底稿 WP14 :非居民企业底稿 |
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
