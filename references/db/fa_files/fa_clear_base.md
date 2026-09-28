# 清理申请单基础资料-fa_clear_base

## 单据体-子表 t_fa_clrapplybillentry

- **表名称：** 单据体-子表
- **表名：** t_fa_clrapplybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclearqty | fclearqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 3 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmeasureunitid | fmeasureunitid | int8 | 64 |  | √ | 0 |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frealcardid | frealcardid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_clrappbilent_fseq |  | fseq |
| 2 | t_fa_clrapplybillentry_pkey |  | fentryid |

---

## 清理申请单基础资料-主表 t_fa_clrapplybill

- **表名称：** 清理申请单基础资料-主表
- **表名：** t_fa_clrapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fbillstatus | fbillstatus | varchar | 50 |  | √ | 'A' |  |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 7 | fhandlerid | fhandlerid | int8 | 64 |  | √ | 0 |  |
| 8 | freason | 清理原因 | varchar | 255 |  |  | ' ' | 清理原因 |
| 9 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fchangemodeid | 减少方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 12 | fassetunitid | fassetunitid | int8 | 64 |  | √ | 0 |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fcleardate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 15 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_clrapplybill_pkey |  | fid |
| 2 | idx_fa_clrappbill_fbillno |  | fbillno |
