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
| 4 | fprofitamount | 利润总额 | numeric | 23 | 10 | √ | 0.0000000000 | 利润总额 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |

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
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ffetchstatus | ffetchstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | ftemplatetype | 纳税人类型 | varchar | 36 |  | √ | ' ' | 纳税人类型,枚举: |
| 10 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fenddate | 所属期至 | timestamp | 0 |  |  | null | 所属期至 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ftype | 底稿类型 | varchar | 36 |  | √ | ' ' | 底稿类型,枚举: WP11 :查账征收底稿 WP12 :居民企业分支机构底稿 WP13 :核定征收底稿 WP14 :非居民企业底稿 |
| 17 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 18 | fjtnumber | 计提单号 | varchar | 50 |  | √ | ' ' | 计提单号 |
| 19 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 20 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 21 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 22 | fbillno | 底稿编号 | varchar | 30 |  | √ | ' ' | 底稿编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fsbbno | fsbbno | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_draft_main |  | forgid,ftemplatetype,fstartdate,fenddate,fbillno |
| 2 | pk_tctb_draft_main |  | fid |
