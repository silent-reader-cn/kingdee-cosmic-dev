# 销售折扣表-sm_salediscountlist

## 销售折扣表-多语言表 t_sm_salediscountlist_l

- **表名称：** 销售折扣表-多语言表
- **表名：** t_sm_salediscountlist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salediscountlist_l |  | fid,flocaleid |
| 2 | pk_t_sm_salediscountlist_l |  | fpkid |

---

## 客户明细单据体-子表 t_sm_discountcusentry

- **表名称：** 客户明细单据体-子表
- **表名：** t_sm_discountcusentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomergroupid | 客户分类编码 | int8 | 64 |  | √ | 0 | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcustomerid | 客户编码 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_discountcusentry |  | fentryid |
| 2 | idx_sm_discountcusentry |  | fid |

---

## 折扣明细单据体-子表 t_sm_discountentry

- **表名称：** 折扣明细单据体-子表
- **表名：** t_sm_discountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountbasis | 折扣依据 | varchar | 50 |  | √ | ' ' | 折扣依据,枚举: A :按数量 B :按金额 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 7 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fbasisfrom | 从 | numeric | 23 | 10 | √ | 0 | 从 |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fdisexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 13 | fdiseffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fbasisto | 至 | numeric | 23 | 10 | √ | 0 | 至 |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_discountentry_materid |  | fmaterialid |
| 2 | pk_t_sm_discountentry |  | fentryid |
| 3 | idx_sm_discountentry_grp |  | fmaterialgroupid |

---

## 销售折扣表-主表 t_sm_salediscountlist

- **表名称：** 销售折扣表-主表
- **表名：** t_sm_salediscountlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fapplycustomer | 限定客户 | varchar | 50 |  | √ | ' ' | 限定客户,枚举: B :客户 C :客户分类 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 10 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | feffectdate | 折扣生效日期 | timestamp | 0 |  |  | null | 折扣生效日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fdiscountgroupid | 折扣表分组 | int8 | 64 |  | √ | 0 | [销售折扣表分组 sm_salediscountlistgroup](../sm_files/sm_salediscountlistgroup.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fexpirydate | 折扣失效日期 | timestamp | 0 |  |  | null | 折扣失效日期 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fapplymaterial | 折扣对象 | varchar | 50 |  | √ | ' ' | 折扣对象,枚举: A :物料 B :物料分类 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_saledislist_num |  | fnumber |
| 2 | pk_t_sm_salediscountlist |  | fid |
