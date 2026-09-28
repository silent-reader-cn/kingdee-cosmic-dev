# 月末关账-ap_closeaccount

## 失败原因分录-子表 t_ap_closefailedentry

- **表名称：** 失败原因分录-子表
- **表名：** t_ap_closefailedentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fduedate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 3 | fstatus | 单据统计状态 | varchar | 30 |  | √ | ' ' | 单据统计状态,枚举: A :暂存 B :提交 C :审核 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcount | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: ap_businessapbill :业务应付单 ap_finapbill :财务应付单 ap_otherbill :其他应付单 ap_invoice :发票 |
| 8 | ffailedmessage | 失败原因 | varchar | 1000 |  | √ | ' ' | 失败原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_closefailedentry_pkey |  | fentryid |
| 2 | idx_ap_cfe_fid |  | fid |

---

## 月末关账-主表 t_ap_init

- **表名称：** 月末关账-主表
- **表名：** t_ap_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcurrentdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 4 | fbillstatus | fbillstatus | varchar | 5 |  | √ | ' ' |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fxkisenabled | fxkisenabled | bpchar | 1 |  | √ | '0' |  |
| 8 | fisfinishinit | 是否结束初始化 | bpchar | 1 |  | √ | '0' | 是否结束初始化 |
| 9 | fmigdata | fmigdata | varchar | 300 |  | √ | ' ' |  |
| 10 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 11 | fmigsrc | fmigsrc | int4 | 32 |  | √ | 0 |  |
| 12 | fstartperiodid | fstartperiodid | int8 | 64 |  | √ | 0 |  |
| 13 | fsettlemodel | fsettlemodel | varchar | 30 |  | √ | ' ' |  |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fsettleseq | fsettleseq | int8 | 64 |  | √ | 0 |  |
| 16 | fperiodtypeid | fperiodtypeid | int8 | 64 |  | √ | 0 |  |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | fstartdate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 19 | fstacurrencyid | 业务主币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 21 | fcurrentperiodid | fcurrentperiodid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 23 | fbillno | 单据编号1 | varchar | 30 |  | √ | ' ' | 单据编号1 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_init_pkey |  | fid |
| 2 | idx_ap_init_orgid |  | forgid |
