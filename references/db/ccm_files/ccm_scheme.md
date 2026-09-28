# （废弃）信控方案-ccm_scheme

## （废弃）信控方案-多语言表 t_ccm_scheme_l

- **表名称：** （废弃）信控方案-多语言表
- **表名：** t_ccm_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_schemel_fid_flocale |  | fid,flocaleid |
| 2 | t_ccm_scheme_l_pkey |  | fpkid |

---

## 单据策略分录-子表 t_ccm_scheme_entry

- **表名称：** 单据策略分录-子表
- **表名：** t_ccm_scheme_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fbillstrategyid | 单据策略 | int8 | 64 |  | √ | 0 | [（废弃）单据策略 ccm_billstrategy](../ccm_files/ccm_billstrategy.md) |
| 4 | fmode | 信用控制强度 | varchar | 30 |  | √ | ' ' | 信用控制强度,枚举: cancel :取消交易 warning :预警提示 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_scheme_entry_pkey |  | fentryid |
| 2 | idx_ccm_se_fid |  | fid |

---

## （废弃）信控方案-主表 t_ccm_scheme

- **表名称：** （废弃）信控方案-主表
- **表名：** t_ccm_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsinglecurcontrol | 币别隔离 | bpchar | 1 |  | √ | '0' | 币别隔离 |
| 3 | fdimensionid | 信用控制维度 | int8 | 64 |  | √ | 0 | [信控维度 ccm_dimension](../ccm_files/ccm_dimension.md) |
| 4 | fyearbegindate | 年度起始日 | timestamp | 0 |  |  | null | 年度起始日 |
| 5 | fdefaultquota | 默认额度 | numeric | 23 | 10 | √ | 0.0000000000 | 默认额度 |
| 6 | fyearenddate | 年度结束日 | timestamp | 0 |  |  | null | 年度结束日 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fvalidity | 有效期 | varchar | 30 |  | √ | ' ' | 有效期,枚举: PERPETUAL :永久 YEAR :按年 |
| 12 | fmode | 信用控制强度(废弃) | varchar | 30 |  | √ | ' ' | 信用控制强度(废弃),枚举: cancel :取消交易 warning :预警提示 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fchecktypeid | 信用控制形式 | int8 | 64 |  | √ | 0 | [（废弃）信用控制形式 ccm_checktype](../ccm_files/ccm_checktype.md) |
| 15 | fbizstate | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: normal :正常 initing :初始化/重算中 |
| 16 | fautocratearchive | 自动创建档案 | bpchar | 1 |  | √ | '0' | 自动创建档案 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | forgscope | 控制组织范围 | varchar | 10 |  | √ | ' ' | 控制组织范围,枚举: GLOBAL :集团范围 GROUP :法人范围 SINGLE :业务组织范围 |
| 21 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | forgfunc | 组织职能 | varchar | 10 |  | √ | ' ' | 组织职能,枚举: XSZZ :销售组织 HSZZ :核算组织 ZJZZ :资金组织 |
| 23 | fmainorgid | 授信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fdefaultdays | 默认信用天数 | int8 | 64 |  | √ | 0 | 默认信用天数 |
| 25 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 26 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_scheme_pkey |  | fid |
| 2 | idx_ccm_scheme_number |  | fnumber |

---

## 额度共享范围-子表 t_ccm_scheme_orgentry

- **表名称：** 额度共享范围-子表
- **表名：** t_ccm_scheme_orgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_soe_fid |  | fid |
| 2 | t_ccm_scheme_orgentry_pkey |  | fentryid |
