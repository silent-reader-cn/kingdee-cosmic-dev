# 预缴底稿查询-tccit_seasonal_dg_bill

## 单据体-子表 t_tccit_seasonal_dg_bill

- **表名称：** 单据体-子表
- **表名：** t_tccit_seasonal_dg_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbqyjtsdse | fbqyjtsdse | numeric | 23 | 10 | √ | 0 |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fisxxwlqy | 小型微利企业 | varchar | 50 |  | √ | ' ' | 小型微利企业,枚举: 0 : 1 :是 2 :否 |
| 5 | fprofitamount | 利润总额 | numeric | 23 | 10 | √ | 0.0000000000 | 利润总额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_seasonal_dg_bill_fk |  | fid |
| 2 | pk_tccit_seasonal_dg_bill |  | fentryid |

---

## 预缴底稿查询-主表 t_tctb_draft_main

- **表名称：** 预缴底稿查询-主表
- **表名：** t_tctb_draft_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 5 | ffetchstatus | ffetchstatus | varchar | 50 |  | √ | ' ' |  |
| 6 | ftemplatetype | 纳税人类型 | varchar | 36 |  | √ | ' ' | 纳税人类型,枚举: |
| 7 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fenddate | 所属期至 | timestamp | 0 |  |  | null | 所属期至 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fjtnumber | 计提单号 | varchar | 50 |  | √ | ' ' | 计提单号 |
| 13 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 14 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 15 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 底稿编号 | varchar | 30 |  | √ | ' ' | 底稿编号 |
| 17 | fsbbno | fsbbno | varchar | 50 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 24 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 25 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 26 | fdataversion | fdataversion | varchar | 50 |  | √ | ' ' |  |
| 27 | ftype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: WP11 :查账征收底稿 WP12 :居民企业分支机构底稿 WP13 :核定征收底稿 WP14 :非居民企业底稿 |
| 28 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 29 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 30 | fdeadline | fdeadline | varchar | 50 |  | √ | ' ' |  |
| 31 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_draft_main |  | forgid,ftemplatetype,fstartdate,fenddate,fbillno |
| 2 | pk_tctb_draft_main |  | fid |
