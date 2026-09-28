# 抵销分录-xkcr_elimination

## 抵销分录-多语言表 t_xkcr_elimination_l

- **表名称：** 抵销分录-多语言表
- **表名：** t_xkcr_elimination_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_elimination_l |  | fpkid |
| 2 | idx_xkcr_elimination_l |  | fid,flocaleid |

---

## 单据体-子表 t_xkcr_eliminationentry

- **表名称：** 单据体-子表
- **表名：** t_xkcr_eliminationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forigin | 联动分录行 | varchar | 50 |  | √ | ' ' | 联动分录行 |
| 3 | frptitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 4 | fdebit | 借方 | numeric | 23 | 10 | √ | 0 | 借方 |
| 5 | fdetaildimnumber | 明细维度标识 | varchar | 2000 |  |  | null | 明细维度标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frptitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 8 | fislinkage | 是否联动分录 | bpchar | 1 |  | √ | '0' | 是否联动分录 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 11 | fcredit | 贷方 | numeric | 23 | 10 | √ | 0 | 贷方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_eliminationentry |  | fentryid |
| 2 | idx_xkcr_elientry_fid |  | fid |
| 3 | idx_xkcr_elientry_itemid |  | frptitemid |

---

## 单据体-多语言表 t_xkcr_eliminationentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_xkcr_eliminationentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_eliminationentry_l |  | fentryid,flocaleid |
| 2 | pk_xkcr_eliminationentry_l |  | fpkid |

---

## 抵销分录-主表 t_xkcr_elimination

- **表名称：** 抵销分录-主表
- **表名：** t_xkcr_elimination

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdebittotal | 借方调整总额 | numeric | 23 | 10 | √ | 0 | 借方调整总额 |
| 3 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 4 | fmaintype | 主附表类型 | bpchar | 1 |  | √ | '0' | 主附表类型,枚举: 0 :主表 1 :附表 |
| 5 | fisperpetuate | 延续分录 | bpchar | 1 |  | √ | '0' | 延续分录 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | foriginid | 源分录 | int8 | 64 |  | √ | 0 | 源分录 |
| 8 | fbuildtype | 创建方式 | bpchar | 1 |  | √ | ' ' | 创建方式,枚举: 1 :手工录入 2 :自动生成 3 :导入 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcompanyid2 | 对方/被投资方/购买方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fdate | 抵销日期 | timestamp | 0 |  |  | null | 抵销日期 |
| 12 | fbillno | 分录编码 | varchar | 30 |  | √ | ' ' | 分录编码 |
| 13 | fcredittotal | 贷方调整总额 | numeric | 23 | 10 | √ | 0 | 贷方调整总额 |
| 14 | ftranstypeid | 交易类型 | int8 | 64 |  | √ | 0 | [交易类型 xkcr_transactiontype](../xkcr_files/xkcr_transactiontype.md) |
| 15 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | felimcheckageid | 抵销核对id | int8 | 64 |  | √ | 0 | 抵销核对id |
| 18 | ftemplateid | 抵销分录模板 | int8 | 64 |  | √ | 0 | [抵销分录模板 xkcr_elimtemp](../xkcr_files/xkcr_elimtemp.md) |
| 19 | fdimvaluekey | 维度 | varchar | 2000 |  |  | null | 维度 |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | felimtypeid | 抵销类型 | int8 | 64 |  | √ | 0 | [抵销类型 xkcr_eliminationtype](../xkcr_files/xkcr_eliminationtype.md) |
| 24 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 25 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 26 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 27 | fcycleid | 周期类型 | bpchar | 1 |  | √ | ' ' | 周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 28 | fscopetypeid | 合并范围方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 29 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fcompanyid | 我方/投资方/销售方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_elimination |  | fid |
| 2 | idx_xkcr_eli_billno |  | fbillno |
| 3 | idx_xkcr_eli_tmpid |  | ftemplateid |
| 4 | idx_xkcr_eli_createtime |  | fcreatetime |
