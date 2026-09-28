# 经营费用分摊结果单-xkoac_allocationresults

## 经营费用分摊结果单-主表 t_xkoac_costshare

- **表名称：** 经营费用分摊结果单-主表
- **表名：** t_xkoac_costshare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 来源单据分录id | int8 | 64 |  | √ | 0 | 来源单据分录id |
| 3 | ftotalamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 4 | forgstructure | 经营组织架构版本 | int8 | 64 |  | √ | 0 | [经营组织架构版本 xkoac_orgsystem](../xkoac_files/xkoac_orgsystem.md) |
| 5 | fexpensetype | 费用录入方式 | bpchar | 1 |  | √ | '1' | 费用录入方式,枚举: 1 :费用项目 2 :经营科目 |
| 6 | faccount | 经营科目 | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 7 | fbusdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsrcseq | 来源单据分录行序号 | int4 | 32 |  | √ | 0 | 来源单据分录行序号 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | faccountbook | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fsrcbillid | 来源单据id | varchar | 100 |  | √ | ' ' | 来源单据id |
| 17 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 18 | fsrcno | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fsenderoperateunit | 发送方经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 22 | fallocationcriteria | 分摊规则 | int8 | 64 |  | √ | 0 | [分摊规则 xkoac_shareweights](../xkoac_files/xkoac_shareweights.md) |
| 23 | fsourcebillid | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 25 | fvchimptplan | 来源方案 | int8 | 64 |  | √ | 0 | [经营费用分摊方案 xkoac_allocationplan](../xkoac_files/xkoac_allocationplan.md) |
| 26 | fvchplanseq | 来源方案行ID | int4 | 32 |  | √ | 0 | 来源方案行ID |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_costshare |  | fbillno |
| 2 | pk_xkoac_costshare |  | fid |

---

## 单据体-子表 t_xkoac_costshareentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_costshareentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalweight | 总权重 | numeric | 23 | 10 | √ | 0 | 总权重 |
| 3 | fweightvalue | 权重值 | numeric | 23 | 10 | √ | 0 | 权重值 |
| 4 | fallocationcompleted | 分摊完成 | bpchar | 1 |  | √ | '0' | 分摊完成 |
| 5 | frecassgrp | 接收方经营核算维度值 | int8 | 64 |  | √ | 0 | null 008 |
| 6 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | frecorded | 已入账 | bpchar | 1 |  | √ | '0' | 已入账 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fen_acct | 经营科目 | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 10 | freceiveoperateunit | 接收方经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fallocatedamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_costshareentry |  | fentryid |
| 2 | idx_xkoac_costshareentry |  | fseq |
