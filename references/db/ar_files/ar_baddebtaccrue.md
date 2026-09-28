# 坏账计提（废弃）-ar_baddebtaccrue

## 坏账计提（废弃）-主表 t_ar_baddebtaccrue

- **表名称：** 坏账计提（废弃）-主表
- **表名：** t_ar_baddebtaccrue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faginggroup | faginggroup | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fasstacttype | fasstacttype | varchar | 255 |  | √ | ' ' |  |
| 5 | flistperiod | 计提期间 | varchar | 255 |  | √ | ' ' | 计提期间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fotherbaddebtaccrue | fotherbaddebtaccrue | bpchar | 1 |  | √ | '0' |  |
| 8 | faginggroupdetail | faginggroupdetail | varchar | 255 |  | √ | ' ' |  |
| 9 | farbustobaddebtaccrue | farbustobaddebtaccrue | bpchar | 1 |  | √ | '0' |  |
| 10 | farbusagingstartdate | farbusagingstartdate | varchar | 30 |  |  | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | faccrualstatus | 计提状态 | varchar | 30 |  | √ | ' ' | 计提状态,枚举: 0 :未计提 1 :已计提 |
| 13 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 14 | faragingstartdate | faragingstartdate | varchar | 30 |  |  | ' ' |  |
| 15 | faccrualfrequency | faccrualfrequency | varchar | 30 |  | √ | ' ' |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fperiodid | 计提期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | frecedbaddebtaccrue | frecedbaddebtaccrue | bpchar | 1 |  | √ | '0' |  |
| 21 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 22 | faccrualschemeid | 计提方案 | int8 | 64 |  | √ | 0 | 计提方案（废弃） ar_baddebtaccrualplan |
| 23 | faginggroupdetail_tag | faginggroupdetail_tag | text | 0 |  |  | null |  |
| 24 | fpreperiodid | 上一期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fisperiod | 是否期初 | bpchar | 1 |  | √ | '0' | 是否期初 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_baddebtaccrue |  | fid |
| 2 | idx_ar_baddebt_scheme |  | faccrualschemeid |
| 3 | idx_ar_baddebt_period_org |  | fperiodid,forgid |
| 4 | idx_ar_baddebt_org |  | forgid |

---

## 个别认定单据体-子表 t_ar_baddebtaccrueentry

- **表名称：** 个别认定单据体-子表
- **表名：** t_ar_baddebtaccrueentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccrualentityobj | 计提对象下拉列表 | varchar | 50 |  | √ | ' ' | 计提对象下拉列表,枚举: ar_finarbill :财务应收单 ar_busbill :暂估应收单 ar_revcfmbill :收入确认单 ap_padibill :期初预付单 cas_paybill :付款处理 |
| 3 | fasstacttypeid | fasstacttypeid | int8 | 64 |  | √ | 0 |  |
| 4 | faccrualobjid | 计提对象 | int8 | 64 |  | √ | 0 | 计提对象 ar_accrualentityobj |
| 5 | fasstactid | fasstactid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | findividualreason | 个别认定原因 | varchar | 255 |  | √ | ' ' | 个别认定原因 |
| 8 | faccrualagingid | faccrualagingid | int8 | 64 |  | √ | 0 |  |
| 9 | fasstacttype | fasstacttype | varchar | 50 |  | √ | ' ' |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | faccrualpercent | 计提比率(%) | numeric | 23 | 10 | √ | 0 | 计提比率(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_baddebtaccrueentry |  | fentryid |
| 2 | idx_ar_bdaentry_fid |  | fid |

---

## 客户-多选基础资料表 t_ar_accrualcustomer

- **表名称：** 客户-多选基础资料表
- **表名：** t_ar_accrualcustomer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_acccustomer_entryid |  | fentryid |
| 2 | pk_t_ar_accrualcustomer |  | fpkid |
