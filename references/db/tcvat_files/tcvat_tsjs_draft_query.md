# 即征即退退税计算底稿查询-tcvat_tsjs_draft_query

## 单据体-子表 t_tcvat_jzjt_draft

- **表名称：** 单据体-子表
- **表名：** t_tcvat_jzjt_draft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftssqb | 退税申请表 | int8 | 64 |  | √ | 0 | [退税申请资料 tcvat_jzjt_tssqb_list](../tcvat_files/tcvat_jzjt_tssqb_list.md) |
| 5 | fjzjtybtse | 即征即退应补（退）税额 | numeric | 23 | 10 | √ | 0 | 即征即退应补（退）税额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fjzjtytsje | 即征即退应退税金额 | numeric | 23 | 10 | √ | 0 | 即征即退应退税金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_jzjt_draft |  | fentryid |
| 2 | idx_tcvat_jzjt_draft_fk |  | fid |

---

## 即征即退类型-多选基础资料表 t_tcvat_jzjtdraft_type

- **表名称：** 即征即退类型-多选基础资料表
- **表名：** t_tcvat_jzjtdraft_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_jzjtdraft_type_fk |  | fid |
| 2 | pk_tcvat_jzjtdraft_type |  | fpkid |

---

## 即征即退退税计算底稿查询-主表 t_tpo_declare_main_tsd

- **表名称：** 即征即退退税计算底稿查询-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 6 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 7 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 8 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 11 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 12 | ftaxareagroup | ftaxareagroup | int8 | 64 |  | √ | 0 |  |
| 13 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 14 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 15 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 17 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 18 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 19 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 20 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 25 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 26 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 27 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 28 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 29 | fjtynsesum | fjtynsesum | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :引入 1 :系统生成 |
| 34 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 35 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 36 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 38 | fhjybtse | fhjybtse | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 43 | fjtnumber | fjtnumber | varchar | 100 |  | √ | ' ' |  |
| 44 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 45 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 46 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsbbno | fsbbno | varchar | 100 |  | √ | ' ' |  |
| 48 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fgeneratebusinessdoc | fgeneratebusinessdoc | bpchar | 1 |  | √ | '0' |  |
| 51 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | faccountsettype | faccountsettype | varchar | 50 |  | √ | ' ' |  |
| 54 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 55 | ftaxsystem | ftaxsystem | int8 | 64 |  | √ | 0 |  |
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
