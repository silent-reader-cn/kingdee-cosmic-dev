# 分摊规则-xkoac_shareweights

## 交易类型-多选基础资料表 t_xkoac_transtype

- **表名称：** 交易类型-多选基础资料表
- **表名：** t_xkoac_transtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_transtype |  | fpkid |
| 2 | idx_xkoac_transtype |  | fbasedataid |

---

## 单据体-子表 t_xkoac_shareweightentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_shareweightentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusunit | 经营单元编码 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fweight | 权重值 | numeric | 23 | 10 | √ | 0 | 权重值 |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_shareweightentry |  | fentryid |
| 2 | idx_xkoac_shareweightentry |  | fid |

---

## 分摊规则-主表 t_xkoac_shareweights

- **表名称：** 分摊规则-主表
- **表名：** t_xkoac_shareweights

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftextareafie | 分摊公式 | varchar | 255 |  | √ | ' ' | 分摊公式 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fassgrp | 经营核算维度 | int8 | 64 |  | √ | 0 | [经营核算维度 xkoac_dimension](../basedata_files/xkoac_dimension.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fallocaterules | 分摊方式 | bpchar | 1 |  | √ | '1' | 分摊方式,枚举: 2 :按经营科目金额 1 :按固定权重 3 :按经营科目的核算维度金额 |
| 10 | ftranexpr | 公式描述 | varchar | 1000 |  | √ | ' ' | 公式描述 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcomposite | 复合分摊 | bpchar | 1 |  | √ | '0' | 复合分摊 |
| 16 | fenable | 禁用状态 | bpchar | 1 |  | √ | '1' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 17 | ffilter | 经营核算维度值范围设置 | text | 0 |  |  | null | 经营核算维度值范围设置 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | ffilterdesc | 经营核算维度值范围 | varchar | 2000 |  | √ | ' ' | 经营核算维度值范围 |
| 20 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 21 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | faccountbook | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 23 | fisperiod | 按期间设置 | bpchar | 1 |  | √ | '0' | 按期间设置 |
| 24 | fdatatype | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 1 :本期发生数 2 :本期计划值 3 :上期发生额 4 :上期计划值 5 :期初余额 6 :本期增加 7 :本期减少 8 :期末余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_shareweights |  | fid |
| 2 | idx_xkoac_shareweights |  | fnumber |

---

## 分摊规则-多语言表 t_xkoac_shareweights_l

- **表名称：** 分摊规则-多语言表
- **表名：** t_xkoac_shareweights_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_shareweights_l |  | fpkid |
| 2 | idx_xkoac_shareweights_l |  | fid,flocaleid |
