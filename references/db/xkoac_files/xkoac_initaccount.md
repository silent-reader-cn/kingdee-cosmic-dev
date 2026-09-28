# 经营科目初始化-xkoac_initaccount

## 树形单据体-子表 t_xkoac_initaccountentry

- **表名称：** 树形单据体-子表
- **表名：** t_xkoac_initaccountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountnum | 经营科目编码 | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 3 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 4 | fcurramount | 本位币金额 | numeric | 23 | 10 | √ | 0 | 本位币金额 |
| 5 | ffromcurramount | 原币金额 | numeric | 23 | 10 | √ | 0 | 原币金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizdim | 需录入经营核算维度 | varchar | 50 |  | √ | ' ' | 需录入经营核算维度,枚举: 1 :需在右侧录入经营核算维度 0 :0 |
| 8 | fquotation | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 9 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 11 | ffromcurr | 原币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fexrate | 汇率 | numeric | 23 | 2 | √ | 0 | 汇率 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_initaccountentry |  | fentryid |
| 2 | idx_xkoac_initaccountentry |  | fseq |

---

## 经营科目初始化-主表 t_xkoac_initaccount

- **表名称：** 经营科目初始化-主表
- **表名：** t_xkoac_initaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgstructure | 经营组织架构版本 | int8 | 64 |  | √ | 0 | [经营组织架构版本 xkoac_orgsystem](../xkoac_files/xkoac_orgsystem.md) |
| 7 | foperatingbookid | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 8 | fambaunitid | 经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 9 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_initaccount |  | foperatingbookid,fambaunitid |
| 2 | pk_t_xkoac_initaccount |  | fid |

---

## 子单据体-子表 t_xkoac_initsubentry

- **表名称：** 子单据体-子表
- **表名：** t_xkoac_initsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fassgrp | 经营核算维度 | int8 | 64 |  | √ | 0 | null 008 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | faccountid | 经营科目 | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 6 | fsubcurramount | 本位币金额 | numeric | 23 | 10 | √ | 0 | 本位币金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_initsubentry |  | fdetailid |
| 2 | idx_xkoac_initsubentry |  | fseq |
