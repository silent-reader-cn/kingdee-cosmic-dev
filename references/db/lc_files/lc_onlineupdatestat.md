# 修改状态-lc_onlineupdatestat

## 修改状态-主表 t_lc_onlineupdatestat

- **表名称：** 修改状态-主表
- **表名：** t_lc_onlineupdatestat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: lc_lettercredit :开证处理 lc_arrival :到单处理 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_onlineupdatestat_forgid |  | forgid |
| 2 | pk_t_lc_onlineupdatestat |  | fid |

---

## 单据体-子表 t_lc_onlineupdateentry

- **表名称：** 单据体-子表
- **表名：** t_lc_onlineupdateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 3 | fbebankstatus | 操作状态 | varchar | 50 |  | √ | ' ' | 操作状态,枚举: OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 |
| 4 | fsrcbillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 5 | fcompletedate | 业务完成日期 | timestamp | 0 |  |  | null | 业务完成日期 |
| 6 | fstatusnew | 修改后操作状态 | varchar | 50 |  | √ | ' ' | 修改后操作状态,枚举: TS :交易成功 TF :交易失败 |
| 7 | fopetype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: online :在线开证 accept :承兑 payment :付款 protest :拒付 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freason | 原因 | varchar | 255 |  | √ | ' ' | 原因 |
| 10 | fcreditno | 信用证号 | varchar | 50 |  | √ | ' ' | 信用证号 |
| 11 | freturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_onlineupdateentry |  | fentryid |
| 2 | idx_onlineupdateentry_fid |  | fid |

---

## 单据体-多语言表 t_lc_onlineupdateentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_lc_onlineupdateentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 2 | freason | 原因 | varchar | 255 |  | √ | ' ' | 原因 |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_onlineupdateentry_l |  | fpkid |
| 2 | idx_lc_onupentryl_fentryid |  | fentryid |
