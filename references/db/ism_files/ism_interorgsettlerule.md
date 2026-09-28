# 结算取价规则-ism_interorgsettlerule

## 取价信息-子表 t_ism_interorgpriceinfo

- **表名称：** 取价信息-子表
- **表名：** t_ism_interorgpriceinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddnfixedprice | 加成固定价格 | numeric | 23 | 10 | √ | 0.0000000000 | 加成固定价格 |
| 3 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 5 | fcustompriceplugin | 自定义取价插件 | varchar | 255 |  | √ | ' ' | 自定义取价插件 |
| 6 | fsettlesource | 结算价来源 | varchar | 50 |  | √ | ' ' | 结算价来源,枚举: 2 :来源业务单据价格 3 :来源订单价格 4 :配置成本价 5 :自定义插件 6 :指定固定价格 7 :实际成本价 8 :结算价目表 9 :结算取价策略 10 :最新入库成本价 11 :往期最新出库成本价 12 :期初加权平均成本价 13 :当期加权平均成本价 14 :来源业务单据金额 |
| 7 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 8 | faddnratio | 加成比率% | numeric | 23 | 10 | √ | 0.0000000000 | 加成比率% |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fcurrencyinfo | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fcurrencysource | 币种来源 | varchar | 50 |  | √ | ' ' | 币种来源,枚举: 0 :供应方结算组织本位币 1 :需求方结算组织本位币 2 :内部客户交易币种 3 :内部供应商交易币种 4 :来源业务单据币种 5 :来源订单币种 6 :指定固定币种 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fpricescheme | fpricescheme | int8 | 64 |  | √ | 0 |  |
| 14 | flevel | 取价优先级 | bpchar | 1 |  | √ | '1' | 取价优先级,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 |
| 15 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 16 | ftaxsource | 税率来源 | varchar | 50 |  | √ | ' ' | 税率来源,枚举: 0 :内部客户交易税率 1 :内部供应商交易税率 2 :销售价格政策税率 3 :采购价格政策税率 4 :来源业务单据税率 5 :来源订单税率 6 :指定固定税率 7 :物料默认税率 |
| 17 | finvprice | finvprice | bpchar | 1 |  | √ | ' ' |  |
| 18 | fentryendeffectivedate | 生效日期范围.结束 | timestamp | 0 |  |  | null | 生效日期范围.结束 |
| 19 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | fsettleprice | 结算取价 | bpchar | 1 |  | √ | '0' | 结算取价 |
| 21 | faccountsys | faccountsys | int8 | 64 |  |  | null |  |
| 22 | fentrystarteffectivedate | 生效日期范围.开始 | timestamp | 0 |  |  | null | 生效日期范围.开始 |
| 23 | fbillentity | 业务单据 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_interorgpriceinfo_pkey |  | fentryid |
| 2 | idx_ism_int_ope_fid |  | fid |

---

## 结算取价规则-主表 t_ism_interorgprice

- **表名称：** 结算取价规则-主表
- **表名：** t_ism_interorgprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexratesrc | 汇率来源 | varchar | 50 |  | √ | ' ' | 汇率来源,枚举: 0 :按源单业务日期+N天取汇率 1 :按源单创建日期+N天取汇率 2 :按当前系统日期+N天取汇率 |
| 6 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fstarteffectivedate | 生效日期范围.开始 | timestamp | 0 |  |  | null | 生效日期范围.开始 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fdays | 天数 | int8 | 64 |  | √ | 0 | 天数 |
| 12 | fsupplier | 供应方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fdemand | 需求方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fdepict | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 16 | fissys | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fendeffectivedate | 生效日期范围.结束 | timestamp | 0 |  |  | null | 生效日期范围.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_interorgprice_pkey |  | fid |
| 2 | idx_ism_int_op_fct |  | fcreatetime |
| 3 | idx_ism_int_op_fno |  | fnumber |

---

## 结算取价规则-多语言表 t_ism_interorgprice_l

- **表名称：** 结算取价规则-多语言表
- **表名：** t_ism_interorgprice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fdepict | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_int_op_l_flid |  | fid,flocaleid |
| 2 | t_ism_interorgprice_l_pkey |  | fpkid |
