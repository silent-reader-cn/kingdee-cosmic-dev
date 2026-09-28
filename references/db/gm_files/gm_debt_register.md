# 担保债务登记-gm_debt_register

## 担保债务登记-多语言表 t_gm_debtregister_l

- **表名称：** 担保债务登记-多语言表
- **表名：** t_gm_debtregister_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 80 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_debtregister_l |  | fpkid |
| 2 | idx_gm_debtregister_l |  | fid,flocaleid |

---

## 担保债务登记-主表 t_gm_debtregister

- **表名称：** 担保债务登记-主表
- **表名：** t_gm_debtregister

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fguaranteerate | 担保比例(%) | numeric | 23 | 10 | √ | 0 | 担保比例(%) |
| 3 | fgroupid | 组id | varchar | 80 |  | √ | ' ' | 组id |
| 4 | forgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fregisterdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 6 | fchangetype | 变动类型 | varchar | 80 |  | √ | ' ' | 变动类型,枚举: debtOccupy :债务占用 debtRelease :债务释放 |
| 7 | famount | 债务金额 | numeric | 23 | 10 | √ | 0 | 债务金额 |
| 8 | fgmbillno | 担保单据编号 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 9 | fbindid | 绑定占用单 | varchar | 80 |  | √ | ' ' | 绑定占用单 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fenddate | 债务结束日期 | timestamp | 0 |  |  | null | 债务结束日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fconvertrate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 14 | funiquecode | 单据唯一编码 | varchar | 80 |  | √ | ' ' | 单据唯一编码 |
| 15 | fguaranteedorgtext | 被担保人 | varchar | 255 |  | √ | ' ' | 被担保人 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | freleaseamount | 释放担保金额 | numeric | 23 | 10 | √ | 0 | 释放担保金额 |
| 18 | fguaranteedorg | 被担保人ID | int8 | 64 |  | √ | 0 | 被担保人ID |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | foccupyamount | 占用担保金额 | numeric | 23 | 10 | √ | 0 | 占用担保金额 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fcreditortext | 债权人 | varchar | 255 |  | √ | ' ' | 债权人 |
| 25 | fbegindate | 债务开始日期 | timestamp | 0 |  |  | null | 债务开始日期 |
| 26 | fisfinance | 融资性 | bpchar | 1 |  | √ | '0' | 融资性 |
| 27 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fbusinesscode | 业务编号 | varchar | 80 |  | √ | ' ' | 业务编号 |
| 30 | freguaranteetype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 31 | frootid | 关联占用单主键 | varchar | 80 |  | √ | ' ' | 关联占用单主键 |
| 32 | fcurrencyid | 债务币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fregisterpeople | 登记人 | varchar | 255 |  | √ | ' ' | 登记人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_unquecode |  | funiquecode |
| 2 | pk_t_gm_debtregister |  | fid |
| 3 | idx_gm_rootid |  | frootid |
| 4 | idx_gm_debtregister |  | fbillno |
| 5 | idx_gm_groupid |  | fgroupid |
