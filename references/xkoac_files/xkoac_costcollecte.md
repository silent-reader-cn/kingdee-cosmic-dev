# 经营费用归集单-xkoac_costcollecte

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
| 3 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 4 | fcurrency | 原币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 原币金额 | numeric | 23 | 10 | √ | 0 | 原币金额 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fdatefield | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fbaseamount | 本位币金额 | numeric | 23 | 10 | √ | 0 | 本位币金额 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_costcollectentry |  | fid |
| 2 | pk_xkoac_costcollectentry |  | fentryid |

---

## 经营费用归集单-主表 t_xkoac_costcollecte

- **表名称：** 经营费用归集单-主表
- **表名：** t_xkoac_costcollecte

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbusinessunit | 经营单元 | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcollectsch | fcollectsch | int8 | 64 |  | √ | 0 |  |
| 5 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fremarks | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 9 | forgstructure | 经营组织架构版本 | int8 | 64 |  | √ | 0 | 经营组织架构版本 xkoac_orgsystem |
| 10 | fsourceobjectid | 费用来源对象 | varchar | 50 |  | √ | ' ' | 费用来源对象 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcetype | 费用来源类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 17 | fperiod | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fcheckboxfield | 系统生成 | bpchar | 1 |  | √ | '0' | 系统生成 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | faccountbook | 经营账簿 | int8 | 64 |  | √ | 0 | 经营账簿 xkoac_operatingbook |
| 22 | collectscheme | collectscheme | int8 | 64 |  | √ | 0 |  |
| 23 | fsourceobject | 费用来源对象 | varchar | 255 |  | √ | ' ' | 费用来源对象 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_costcollecte |  | fid |
| 2 | idx_xkoac_collectte |  | fbillno |
