# 费用方案-fbd_feescheme

## 费用方案-多语言表 t_fbd_feescheme_l

- **表名称：** 费用方案-多语言表
- **表名：** t_fbd_feescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_feescheme_l |  | fpkid |
| 2 | idx_fbd_feescheme_l |  | fid |

---

## 费用方案-主表 t_fbd_feescheme

- **表名称：** 费用方案-主表
- **表名：** t_fbd_feescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountrate | 金额/费率（%） | numeric | 23 | 10 | √ | 0 | 金额/费率（%） |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsetamountrate | 按交易对手设置金额/费率 | bpchar | 1 |  | √ | '0' | 按交易对手设置金额/费率 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbusinessprocess | 交易业务处理 | varchar | 50 |  | √ | ' ' | 交易业务处理,枚举: defer :展期 exratecfg :汇率确认 flat :平盘 bdelivery :提前交割 expiredey :到期交割 ratecfg :利率确认 pay :利息/本金支付 redemption :赎回 sellback :卖回 exercise :行权 giveup :放弃行权 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcontractsize | 每单位合约规模 | int8 | 64 |  | √ | 0 | 每单位合约规模 |
| 15 | ffeepayer | 费用支付方 | varchar | 50 |  | √ | ' ' | 费用支付方,枚举: buy :买方 sell :卖方 |
| 16 | fhandsettle | 手动结算 | bpchar | 1 |  | √ | '0' | 手动结算 |
| 17 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 费用类型 fbd_feetype |
| 18 | ftradetypeid | 产品类型 | int8 | 64 |  | √ | 0 | 产品类型 tbd_tradetype |
| 19 | ffeecaltype | 费用计算类型 | varchar | 50 |  | √ | ' ' | 费用计算类型,枚举: fixed :固定 ratio :比例 |
| 20 | famountbase | 金额基数 | varchar | 50 |  | √ | ' ' | 金额基数,枚举: principal :本金 fullprice :全价 |
| 21 | fenable | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :启用 |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | ftimeconvention | 发生时间惯例 | varchar | 50 |  | √ | ' ' | 发生时间惯例,枚举: trade_success :交易成交 trade_effective :交易生效 trade_expire :交易到期 trade_business :交易业务处理 user_specify :用户指定 |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_feescheme |  | fid |
| 2 | idx_fbd_feescheme |  | fnumber |

---

## 单据体-子表 t_fbd_feescheme_entity

- **表名称：** 单据体-子表
- **表名：** t_fbd_feescheme_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextamountrate | 金额/费率（%） | numeric | 23 | 10 | √ | 0 | 金额/费率（%） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcounterpartyid | 交易对手 | int8 | 64 |  | √ | 0 | 交易对手 tbd_counterparty |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_feescheme_entity |  | fid |
| 2 | pk_t_fbd_feescheme_entity |  | fentryid |

---

## 市场-多选基础资料表 t_fbd_feescheme_mk

- **表名称：** 市场-多选基础资料表
- **表名：** t_fbd_feescheme_mk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 市场信息 tbd_marketinfo |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_feescheme_mk |  | fid |
| 2 | pk_t_fbd_feescheme_mk |  | fpkid |
