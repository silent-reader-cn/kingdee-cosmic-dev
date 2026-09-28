# 经营费用归集单-xkoac_costcollecte

## 经营费用归集单-主表 t_xkoac_costcollecte

- **表名称：** 经营费用归集单-主表
- **表名：** t_xkoac_costcollecte

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbusinessunit | 经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fcollectsch | fcollectsch | int8 | 64 |  | √ | 0 |  |
| 4 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 5 | fsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 6 | fcollplanid | 来源方案 | int8 | 64 |  | √ | 0 | [经营费用归集方案 xkoac_collplan](../xkoac_files/xkoac_collplan.md) |
| 7 | fremarks | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 8 | forgstructure | 经营组织架构版本 | int8 | 64 |  | √ | 0 | [经营组织架构版本 xkoac_orgsystem](../xkoac_files/xkoac_orgsystem.md) |
| 9 | fexpensetype | 费用录入方式 | bpchar | 1 |  | √ | '1' | 费用录入方式,枚举: 1 :费用项目 2 :经营科目 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcetype | 费用来源类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | faccountbook | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 15 | fsourceobject | 费用来源对象 | varchar | 255 |  | √ | ' ' | 费用来源对象 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsrcbillstrid | 来源单据对象字符id | varchar | 36 |  | √ | ' ' | 来源单据对象字符id |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsrcbillid | 来源单据对象id | int8 | 64 |  | √ | 0 | 来源单据对象id |
| 21 | fsourceobjectid | 费用来源对象 | varchar | 50 |  | √ | ' ' | 费用来源对象 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 26 | fcheckboxfield | 系统生成 | bpchar | 1 |  | √ | '0' | 系统生成 |
| 27 | fcollplanseq | 来源方案行编码 | int4 | 32 |  | √ | 0 | 来源方案行编码 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | collectscheme | collectscheme | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_costcollecte |  | fid |
| 2 | idx_xkoac_collectte |  | fbillno |

---

## 经营费用归集单-多语言表 t_xkoac_costcollecte_l

- **表名称：** 经营费用归集单-多语言表
- **表名：** t_xkoac_costcollecte_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremarks | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_costcollecte_l |  | fpkid |
| 2 | idx_xkoac_costcollecte_l |  | fid,flocaleid |

---

## 单据体-子表 t_xkoac_costcollectentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_costcollectentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fasscomplete | 分摊完成 | bpchar | 1 |  | √ | '0' | 分摊完成 |
| 3 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | fcurrency | 原币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 原币金额 | numeric | 23 | 10 | √ | 0 | 原币金额 |
| 7 | faccount | 经营科目 | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdatefield | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | fbaseamount | 本位币金额 | numeric | 23 | 10 | √ | 0 | 本位币金额 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_costcollectentry |  | fid |
| 2 | pk_xkoac_costcollectentry |  | fentryid |
