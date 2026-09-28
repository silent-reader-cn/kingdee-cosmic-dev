# 信用控制方案-ccm_schemes

## 信用控制方案-多语言表 t_ccm_schemes_l

- **表名称：** 信用控制方案-多语言表
- **表名：** t_ccm_schemes_l

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
| 1 | pk_t_ccm_schemes_l |  | fpkid |
| 2 | idx_ccm_schemel_fid_flocale_n |  | fid,flocaleid |

---

## 单据策略分录-子表 t_ccm_schemes_entry

- **表名称：** 单据策略分录-子表
- **表名：** t_ccm_schemes_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckformulaqty | 检查信用数量 | bpchar | 1 |  | √ | ' ' | 检查信用数量 |
| 3 | fupdateformulaqty | 更新信用数量 | bpchar | 1 |  | √ | ' ' | 更新信用数量 |
| 4 | fchecksinglebalance | 检查单笔限额 | bpchar | 1 |  | √ | '0' | 检查单笔限额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbillstrategyid | 单据策略 | int8 | 64 |  | √ | 0 | [信用单据策略 ccm_billstrategy_new](../ccm_files/ccm_billstrategy_new.md) |
| 7 | fcheckassingday | 检查信用天数 | bpchar | 1 |  | √ | ' ' | 检查信用天数 |
| 8 | fupdateformula | 更新信用额度 | bpchar | 1 |  | √ | ' ' | 更新信用额度 |
| 9 | fcheckpresscontrol | 压批控制 | bpchar | 1 |  | √ | '0' | 压批控制 |
| 10 | fcheckassingbalance | 检查逾期额度 | bpchar | 1 |  | √ | ' ' | 检查逾期额度 |
| 11 | fmode | 信用控制强度 | varchar | 30 |  | √ | ' ' | 信用控制强度,枚举: cancel :取消交易 warning :预警提示 billspec :单笔特批 |
| 12 | fcheckformula | 检查信用额度 | bpchar | 1 |  | √ | ' ' | 检查信用额度 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_schemes_entry |  | fentryid |
| 2 | idx_ccm_se_fid_n |  | fid |

---

## 额度共享范围-子表 t_ccm_schemes_orgentry

- **表名称：** 额度共享范围-子表
- **表名：** t_ccm_schemes_orgentry

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
| 1 | idx_ccm_soe_fid_n |  | fid |
| 2 | pk_ccm_schemes_orgentry |  | fentryid |

---

## 信用控制方案-主表 t_ccm_schemes

- **表名称：** 信用控制方案-主表
- **表名：** t_ccm_schemes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsinglecurcontrol | 币种隔离 | bpchar | 1 |  | √ | '0' | 币种隔离 |
| 3 | fdimensionid | 信用控制维度 | int8 | 64 |  | √ | 0 | [信控维度 ccm_dimension](../ccm_files/ccm_dimension.md) |
| 4 | fyearbegindate | 年度起始日 | timestamp | 0 |  |  | null | 年度起始日 |
| 5 | foverdueset | 信用逾期设置 | int8 | 64 |  | √ | 0 | [信用逾期设置 ccm_overdueset](../ccm_files/ccm_overdueset.md) |
| 6 | fdefaultquota | 默认额度 | numeric | 23 | 10 | √ | 0 | 默认额度 |
| 7 | fyearenddate | 年度结束日 | timestamp | 0 |  |  | null | 年度结束日 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fvalidity | 有效期 | varchar | 30 |  | √ | ' ' | 有效期,枚举: PERPETUAL :永久 YEAR :按年 |
| 13 | fmode | 信用控制强度(废弃) | varchar | 30 |  | √ | ' ' | 信用控制强度(废弃),枚举: cancel :取消交易 warning :预警提示 |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 15 | fchecktypeid | 信用控制形式 | int8 | 64 |  | √ | 0 | [（废弃）信用控制形式 ccm_checktype](../ccm_files/ccm_checktype.md) |
| 16 | fbizstate | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: normal :正常 initing :初始化/重算中 |
| 17 | fautocratearchive | 自动创建档案 | bpchar | 1 |  | √ | '0' | 自动创建档案 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | forgscope | 控制组织范围 | varchar | 10 |  | √ | ' ' | 控制组织范围,枚举: GLOBAL :集团范围 GROUP :法人范围 SINGLE :业务组织范围 |
| 22 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | forgfunc | 组织职能 | varchar | 10 |  | √ | ' ' | 组织职能,枚举: XSZZ :销售组织 HSZZ :核算组织 ZJZZ :资金组织 |
| 24 | fmainorgid | 授信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fdefaultdays | 默认信用天数 | int8 | 64 |  | √ | 0 | 默认信用天数 |
| 26 | fissys | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 27 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fpresscontrol | 信用压批设置 | int8 | 64 |  | √ | 0 | [信用压批设置 ccm_presscontrol](../ccm_files/ccm_presscontrol.md) |
| 29 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fishistory | 是否历史数据升级 | bpchar | 1 |  | √ | ' ' | 是否历史数据升级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_scheme_number_n |  | fnumber |
| 2 | pk_t_ccm_schemes |  | fid |
