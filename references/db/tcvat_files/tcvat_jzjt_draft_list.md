# 退税计算底稿资料-tcvat_jzjt_draft_list

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

## 退税计算底稿资料-主表 t_tpo_declare_main_tsd

- **表名称：** 退税计算底稿资料-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 3 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 6 | fremarks | fremarks | varchar | 2000 |  | √ | ' ' |  |
| 7 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 8 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 9 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 10 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 15 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 18 | fismodified | fismodified | varchar | 50 |  | √ | '0' |  |
| 19 | ftaxareagroup | ftaxareagroup | int8 | 64 |  | √ | 0 |  |
| 20 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 21 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 22 | fbillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 23 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 24 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 25 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 26 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 27 | fgeneratebusinessdoc | fgeneratebusinessdoc | bpchar | 1 |  | √ | '0' |  |
| 28 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 29 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 30 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 31 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | faccountsettype | faccountsettype | varchar | 50 |  | √ | ' ' |  |
| 34 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 35 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 36 | ftaxsystem | ftaxsystem | int8 | 64 |  | √ | 0 |  |
| 37 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 38 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 39 | fnsrmc | fnsrmc | varchar | 50 |  | √ | ' ' |  |
| 40 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 41 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 42 | fjtynsesum | fjtynsesum | numeric | 23 | 10 | √ | 0 |  |
| 43 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 44 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
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

---

## 单据体-子表 t_tcvat_jzjt_draft

- **表名称：** 单据体-子表
- **表名：** t_tcvat_jzjt_draft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftssqb | 退税申请表 | int8 | 64 |  | √ | 0 | 退税申请资料 tcvat_jzjt_tssqb_list |
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
