# 经营流水账来源方案-xkoac_voucherimptplan

## 经营流水账来源方案-多语言表 t_xkoac_vchimptplan_l

- **表名称：** 经营流水账来源方案-多语言表
- **表名：** t_xkoac_vchimptplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_vchimptplan_l |  | fid,flocaleid |
| 2 | pk_t_xkoac_vchimptplan_l |  | fpkid |

---

## 分录设置-子表 t_xkoac_vchsubentry

- **表名称：** 分录设置-子表
- **表名：** t_xkoac_vchsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexplantiondesc | 摘要 | varchar | 500 |  | √ | ' ' | 摘要 |
| 2 | fchange | 增减项 | bpchar | 1 |  | √ | '1' | 增减项,枚举: 1 :增加 2 :减少 |
| 3 | fambsrcdesc | 内部交易方所属组织来源 | varchar | 100 |  | √ | ' ' | 内部交易方所属组织来源 |
| 4 | faccountlang | 经营科目多语言 | varchar | 500 |  | √ | ' ' | 经营科目多语言 |
| 5 | fpricelang | 单价多语言 | varchar | 100 |  | √ | ' ' | 单价多语言 |
| 6 | famountforlang | 原币金额多语言 | varchar | 500 |  | √ | ' ' | 原币金额多语言 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fexplantion | 摘要设置 | text | 0 |  |  | null | 摘要设置 |
| 9 | faccount | 经营科目设置 | text | 0 |  |  | null | 经营科目设置 |
| 10 | fbaseunit | 基本单位设置 | varchar | 500 |  | √ | ' ' | 基本单位设置 |
| 11 | fmaterialsrcdesc | 结算物料来源 | varchar | 100 |  | √ | ' ' | 结算物料来源 |
| 12 | fprice | 单价设置 | varchar | 500 |  | √ | ' ' | 单价设置 |
| 13 | fcurrencylang | 原币币别多语言 | varchar | 100 |  | √ | ' ' | 原币币别多语言 |
| 14 | fcondition | 分录生成条件设置 | text | 0 |  |  | null | 分录生成条件设置 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fconditionlang | 分录生成条件 | varchar | 2000 |  | √ | ' ' | 分录生成条件 |
| 17 | famountfor | 原币金额设置 | text | 0 |  |  | null | 原币金额设置 |
| 18 | fbaseunitlang | 基本单位多语言 | varchar | 100 |  | √ | ' ' | 基本单位多语言 |
| 19 | fquantity | 数量设置 | text | 0 |  |  | null | 数量设置 |
| 20 | fpricedesc | 单价 | varchar | 100 |  | √ | ' ' | 单价 |
| 21 | fquantitydesc | 数量 | varchar | 500 |  | √ | ' ' | 数量 |
| 22 | fmaterialsrclang | 结算物料来源多语言 | varchar | 100 |  | √ | ' ' | 结算物料来源多语言 |
| 23 | fmaterialsrc | 结算物料来源设置 | varchar | 500 |  | √ | ' ' | 结算物料来源设置 |
| 24 | fambsrclang | 内部交易方业务组织来源多语言 | varchar | 100 |  | √ | ' ' | 内部交易方业务组织来源多语言 |
| 25 | fcurrency | 原币币别设置 | varchar | 500 |  | √ | ' ' | 原币币别设置 |
| 26 | fambdesc | 内部交易方 | varchar | 2000 |  | √ | ' ' | 内部交易方 |
| 27 | fexplantionlang | 摘要多语言 | varchar | 500 |  | √ | ' ' | 摘要多语言 |
| 28 | fcurrencydesc | 原币币别 | varchar | 100 |  | √ | ' ' | 原币币别 |
| 29 | famountfordesc | 原币金额 | varchar | 500 |  | √ | ' ' | 原币金额 |
| 30 | fesq | fesq | int4 | 32 |  | √ | 0 |  |
| 31 | fconditiondesc | 分录生成条件 | varchar | 2000 |  | √ | ' ' | 分录生成条件 |
| 32 | famblang | 内部交易方多语言 | varchar | 2000 |  | √ | ' ' | 内部交易方多语言 |
| 33 | faccountdesc | 经营科目 | varchar | 500 |  | √ | ' ' | 经营科目 |
| 34 | fquantitylang | 数量多语言 | varchar | 500 |  | √ | ' ' | 数量多语言 |
| 35 | fambsrc | 内部交易方业务组织来源设置 | varchar | 500 |  | √ | ' ' | 内部交易方业务组织来源设置 |
| 36 | fbaseunitdesc | 基本单位 | varchar | 100 |  | √ | ' ' | 基本单位 |
| 37 | faccounttype1 | 经营要素 | bpchar | 2 |  | √ | ' ' | 经营要素,枚举: -1 :收入 1 :费用 2 :资产 3 :负债 4 :取来源单据字段 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | famb | 内部交易方设置 | text | 0 |  |  | null | 内部交易方设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_vchsubentry |  | fdetailid |
| 2 | idx_xkoac_vchsubentry |  | fentryid |

---

## 数据来源-多语言表 t_xkoac_vchplanentry_l

- **表名称：** 数据来源-多语言表
- **表名：** t_xkoac_vchplanentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgsrclang | 业务组织来源多语言 | varchar | 100 |  | √ | ' ' | 业务组织来源多语言 |
| 2 | ffilterlang | 过滤条件多语言 | varchar | 2000 |  | √ | ' ' | 过滤条件多语言 |
| 3 | funitsrclang | 经营单元来源多语言 | varchar | 2000 |  | √ | ' ' | 经营单元来源多语言 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fsrcdatelang | 日期来源多语言 | varchar | 100 |  | √ | ' ' | 日期来源多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_vchplanentry_l |  | fpkid |
| 2 | idx_xkoac_vchplanentry_l |  | fentryid,flocaleid |

---

## 适用经营单元-多选基础资料表 t_xkoac_vchplanunit

- **表名称：** 适用经营单元-多选基础资料表
- **表名：** t_xkoac_vchplanunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_vchplanunit |  | fpkid |
| 2 | idx_xkoac_vchplanunit |  | fbasedataid |

---

## 分录设置-多语言表 t_xkoac_vchsubentry_l

- **表名称：** 分录设置-多语言表
- **表名：** t_xkoac_vchsubentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialsrclang | 结算物料来源多语言 | varchar | 100 |  | √ | ' ' | 结算物料来源多语言 |
| 2 | faccountlang | 经营科目多语言 | varchar | 2000 |  | √ | ' ' | 经营科目多语言 |
| 3 | fambsrclang | 内部交易方业务组织来源多语言 | varchar | 100 |  | √ | ' ' | 内部交易方业务组织来源多语言 |
| 4 | fpricelang | 单价多语言 | varchar | 100 |  | √ | ' ' | 单价多语言 |
| 5 | famountforlang | 原币金额多语言 | varchar | 500 |  | √ | ' ' | 原币金额多语言 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fexplantionlang | 摘要多语言 | varchar | 500 |  | √ | ' ' | 摘要多语言 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 9 | fcurrencylang | 原币币别多语言 | varchar | 100 |  | √ | ' ' | 原币币别多语言 |
| 10 | famblang | 内部交易方多语言 | varchar | 2000 |  | √ | ' ' | 内部交易方多语言 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 12 | fconditionlang | 分录生成条件 | varchar | 2000 |  | √ | ' ' | 分录生成条件 |
| 13 | fquantitylang | 数量多语言 | varchar | 500 |  | √ | ' ' | 数量多语言 |
| 14 | fbaseunitlang | 基本单位多语言 | varchar | 100 |  | √ | ' ' | 基本单位多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_vchsubentry_l |  | fdetailid,flocaleid |
| 2 | pk_t_xkoac_vchsubentry_l |  | fpkid |

---

## 经营流水账来源方案-主表 t_xkoac_vchimptplan

- **表名称：** 经营流水账来源方案-主表
- **表名：** t_xkoac_vchimptplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcglacct | 来源总账科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 3 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | faccttblid | 经营科目表 | int8 | 64 |  | √ | 0 | [经营科目表 xkoac_accounttable](../xkoac_files/xkoac_accounttable.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 11 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 12 | ftovoucherstatus | 生成流水账状态 | bpchar | 1 |  | √ | 'A' | 生成流水账状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsrcglstatus | 来源凭证状态 | varchar | 10 |  | √ | ' ' | 来源凭证状态,枚举: 1 :已审核 2 :已提交 3 :已过账 4 :创建 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fmaxrownum | 行编码最大号 | int4 | 32 |  | √ | 0 | 行编码最大号 |
| 20 | fsrctype | 来源类型 | bpchar | 1 |  | √ | '1' | 来源类型,枚举: 1 :业务单据 2 :总账凭证 |
| 21 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | '5' |  |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 25 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_vchimptplan_fnum |  | fnumber |
| 2 | pk_t_xkoac_vchimptplan |  | fid |

---

## 适用经营账簿-多选基础资料表 t_xkoac_vchplanbook

- **表名称：** 适用经营账簿-多选基础资料表
- **表名：** t_xkoac_vchplanbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_vchplanbook |  | fpkid |
| 2 | idx_xkoac_vchplanbook |  | fbasedataid |

---

## 数据来源-子表 t_xkoac_vchplanentry

- **表名称：** 数据来源-子表
- **表名：** t_xkoac_vchplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frownumber | 行ID | int4 | 32 |  | √ | 0 | 行ID |
| 3 | fvouchertype | 流水账类型 | bpchar | 1 |  | √ | '1' | 流水账类型,枚举: 1 :费用 2 :收入 3 :转账 |
| 4 | fsrcdate | 日期来源设置 | varchar | 500 |  | √ | ' ' | 日期来源设置 |
| 5 | fdc | 借贷方向 | varchar | 2 |  | √ | '1' | 借贷方向,枚举: 1 :借 -1 :贷 |
| 6 | fimptstatus | 是否引入 | bpchar | 1 |  | √ | '1' | 是否引入 |
| 7 | funitsrcdesc | 经营单元来源 | varchar | 2000 |  | √ | ' ' | 经营单元来源 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fsrcdatedesc | 日期来源 | varchar | 100 |  | √ | ' ' | 日期来源 |
| 10 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fsrcdatelang | 日期来源多语言 | varchar | 100 |  | √ | ' ' | 日期来源多语言 |
| 12 | fglaccountview | 总账科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 13 | forgsrclang | 业务组织来源多语言 | varchar | 100 |  | √ | ' ' | 业务组织来源多语言 |
| 14 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 15 | ftradingtype | 交易类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 16 | ffilterlang | 过滤条件多语言 | varchar | 2000 |  | √ | ' ' | 过滤条件多语言 |
| 17 | forgsrcdesc | 所属组织来源 | varchar | 100 |  | √ | ' ' | 所属组织来源 |
| 18 | funitsrclang | 经营单元来源多语言 | varchar | 2000 |  | √ | ' ' | 经营单元来源多语言 |
| 19 | ffilter | 过滤条件设置 | text | 0 |  |  | null | 过滤条件设置 |
| 20 | forgsrc | 业务组织来源设置 | varchar | 500 |  | √ | ' ' | 业务组织来源设置 |
| 21 | ffilterdesc | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | funitsrc | 经营单元来源设置 | text | 0 |  |  | null | 经营单元来源设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_vchplanentry |  | fentryid |
| 2 | idx_xkoac_vchplanentry |  | fid |

---

## 来源总账账簿-多选基础资料表 t_xkoac_vchplanglbook

- **表名称：** 来源总账账簿-多选基础资料表
- **表名：** t_xkoac_vchplanglbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_vchplanglbook |  | fpkid |
| 2 | idx_vchimptglbook |  | fbasedataid |
