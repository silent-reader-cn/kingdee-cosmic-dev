# 抵销核对-xkcr_elimcheckage

## 核对单据体-子表 t_xkcr_elimcheckageentry

- **表名称：** 核对单据体-子表
- **表名：** t_xkcr_elimcheckageentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdc | 借贷方向 | varchar | 2 |  | √ | ' ' | 借贷方向,枚举: 1 :借方 -1 :贷方 2 :条件判断 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fitemid | 项目编码 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 6 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 7 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 8 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 10 | frelatecompanyid | 对方组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fdebit | 借方金额 | numeric | 23 | 10 | √ | 0 | 借方金额 |
| 12 | fdetaildimnumber | 明细维度标识 | varchar | 2000 |  |  | null | 明细维度标识 |
| 13 | fdatasource | 取数来源 | varchar | 10 |  | √ | ' ' | 取数来源 |
| 14 | fvalidcredit | 确认贷方金额 | numeric | 23 | 10 | √ | 0 | 确认贷方金额 |
| 15 | fdatadirect | 取数方 | varchar | 10 |  | √ | ' ' | 取数方,枚举: 1 :投资方 2 :被投资方 3 :购买方 4 :购买方 5 :我方 6 :对方 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fcredit | 贷方金额 | numeric | 23 | 10 | √ | 0 | 贷方金额 |
| 18 | fcompanyid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fvaliddebit | 确认借方金额 | numeric | 23 | 10 | √ | 0 | 确认借方金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_elimcheckageentry |  | fentryid |
| 2 | idx_xkcr_elimcheckageentry |  | fid |

---

## 抵销核对-多语言表 t_xkcr_elimcheckage_l

- **表名称：** 抵销核对-多语言表
- **表名：** t_xkcr_elimcheckage_l

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
| 1 | pk_xkcr_elimcheckage_l |  | fpkid |
| 2 | idx_xkcr_elimcheckage_l |  | fid,flocaleid |

---

## 核对单据体-多语言表 t_xkcr_elimcheckageentry_l

- **表名称：** 核对单据体-多语言表
- **表名：** t_xkcr_elimcheckageentry_l

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
| 1 | idx_xkcr_elimcheckageentry_l |  | fentryid,flocaleid |
| 2 | pk_xkcr_elimcheckageentry_l |  | fpkid |

---

## 调整单据体-子表 t_xkcr_elimadjustmap

- **表名称：** 调整单据体-子表
- **表名：** t_xkcr_elimadjustmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjustvalue | 调整数 | numeric | 23 | 10 | √ | 0 | 调整数 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fadjustid | 调整分录id | int8 | 64 |  | √ | 0 | 调整分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_elimadjustmap |  | fentryid |
| 2 | pk_xkcr_elimadjustmap |  | fdetailid |

---

## 抵销核对-主表 t_xkcr_elimcheckage

- **表名称：** 抵销核对-主表
- **表名：** t_xkcr_elimcheckage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifference | 借贷方差异 | numeric | 23 | 10 | √ | 0 | 借贷方差异 |
| 3 | fdiffmode | 差异处理 | varchar | 10 |  | √ | ' ' | 差异处理,枚举: 1 :取大 2 :取小 3 :取借方 4 :取贷方 5 :取平均数 6 :取零 7 :手工确认 |
| 4 | fmaintype | 主附表类型 | bpchar | 1 |  | √ | '0' | 主附表类型,枚举: 0 :主表 1 :附表 |
| 5 | ftotalcredit | 贷方总额 | numeric | 23 | 10 | √ | 0 | 贷方总额 |
| 6 | fdiffdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | ftotaldebit | 借方总额 | numeric | 23 | 10 | √ | 0 | 借方总额 |
| 10 | fbillno | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 11 | fdiffallocate | 差异分配 | varchar | 10 |  | √ | ' ' | 差异分配,枚举: 1 :首行 2 :末行 3 :平均 4 :金额最大 5 :金额最小 6 :报表项目 |
| 12 | ftranstypeid | 交易类型 | int8 | 64 |  | √ | 0 | [交易类型 xkcr_transactiontype](../xkcr_files/xkcr_transactiontype.md) |
| 13 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcurrencyunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 16 | fdimvaluekey | 维度key | varchar | 2000 |  |  | null | 维度key |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcreditcompanyid | 贷方公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | felimtypeid | 抵销类型 | int8 | 64 |  | √ | 0 | [抵销类型 xkcr_eliminationtype](../xkcr_files/xkcr_eliminationtype.md) |
| 22 | frptitemid | 报表项目 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 23 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 24 | felimtempid | 抵消模板 | int8 | 64 |  | √ | 0 | [抵销分录模板 xkcr_elimtemp](../xkcr_files/xkcr_elimtemp.md) |
| 25 | fdebitcompanyid | 借方公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fyear | 年度 | int8 | 64 |  | √ | 0 | 年度 |
| 27 | fperiod | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 28 | fcycleid | 周期类型 | varchar | 10 |  | √ | ' ' | 周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 29 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fdimvaluenumber | 核对维度编码 | varchar | 2000 |  |  | null | 核对维度编码 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_elimcheckage |  | fbillno |
| 2 | pk_xkcr_elimcheckage |  | fid |
