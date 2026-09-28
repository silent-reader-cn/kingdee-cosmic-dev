# 销售价目表-sm_salepricelist

## 销售价目表-多语言表 t_sm_salpricelist_l

- **表名称：** 销售价目表-多语言表
- **表名：** t_sm_salpricelist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salpricelist_l_fid |  | fid,flocaleid |
| 2 | t_sm_salpricelist_l_pkey |  | fpkid |

---

## 客户明细单据体-子表 t_sm_splcusentry

- **表名称：** 客户明细单据体-子表
- **表名：** t_sm_splcusentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomergroupid | 客户分类编码 | int8 | 64 |  | √ | 0 | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 3 | fdefpricelist | 默认价目表 | bpchar | 1 |  | √ | '0' | 默认价目表 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcustomerid | 客户编码 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_splcusentry_fid |  | fid |
| 2 | t_sm_splcusentry_pkey |  | fentryid |

---

## 销售价目表-主表 t_sm_salpricelist

- **表名称：** 销售价目表-主表
- **表名：** t_sm_salpricelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | feffectdate | 价目生效日期 | timestamp | 0 |  |  | null | 价目生效日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fisstair | 启用阶梯（废弃） | bpchar | 1 |  | √ | '0' | 启用阶梯（废弃） |
| 12 | fapplymaterial | 价目对象 | varchar | 5 |  | √ | ' ' | 价目对象,枚举: A :物料 B :物料分类 |
| 13 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fapplycustomer | 限定客户 | varchar | 5 |  | √ | ' ' | 限定客户,枚举: B :客户 C :客户分类 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fdescription | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 20 | fctrlstrategy | fctrlstrategy | varchar | 5 |  | √ | ' ' |  |
| 21 | fpricelisttypeid | 价目类型 | int8 | 64 |  | √ | 0 | [价目类型 bd_pricelisttype](../sbd_files/bd_pricelisttype.md) |
| 22 | fpricelistgroupid | 价目表分组 | int8 | 64 |  | √ | 0 | [销售价目表分组 sm_salepricelistgroup](../sm_files/sm_salepricelistgroup.md) |
| 23 | fexpirydate | 价目失效日期 | timestamp | 0 |  |  | null | 价目失效日期 |
| 24 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 27 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_salpricelist_pkey |  | fid |
| 2 | idx_sm_salpl_fnumber |  | fnumber |

---

## 阶梯价格（废弃）-子表 t_sm_salstairpriceentry

- **表名称：** 阶梯价格（废弃）-子表
- **表名：** t_sm_salstairpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstairprice | 阶梯价格 | numeric | 23 | 10 | √ | 0 | 阶梯价格 |
| 2 | fstairqtyend | 阶梯数量(至) | numeric | 23 | 10 | √ | 0 | 阶梯数量(至) |
| 3 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fstairqtystart | 阶梯数量(从) | numeric | 23 | 10 | √ | 0 | 阶梯数量(从) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_salstairpriceentry |  | fdetailid |
| 2 | idx_sm_salstairpriceentry |  | fentryid |

---

## 价格明细单据体-子表 t_sm_splentry

- **表名称：** 价格明细单据体-子表
- **表名：** t_sm_splentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricefloor | 最低限价 | numeric | 23 | 10 | √ | 0.0000000000 | 最低限价 |
| 3 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 6 | fadjustbillno | 调整单编号 | varchar | 80 |  | √ | ' ' | 调整单编号 |
| 7 | fisstairprice | 阶梯价格（废弃） | bpchar | 1 |  | √ | '0' | 阶梯价格（废弃） |
| 8 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | funitpriceqty | 每单价数量 | numeric | 23 | 10 | √ | 0.0000000000 | 每单价数量 |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fqtyfrom | 从 | numeric | 23 | 10 | √ | 0.0000000000 | 从 |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 18 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 19 | fbaseqtyfrom | 从(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 从(基本单位) |
| 20 | fbaseqtyto | 至(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 至(基本单位) |
| 21 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fpriceexpirydate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 23 | fadjustbillid | 调整单ID | int8 | 64 |  | √ | 0 | 调整单ID |
| 24 | fpriceceiling | 最高限价 | numeric | 23 | 10 | √ | 0.0000000000 | 最高限价 |
| 25 | fqtyto | 至 | numeric | 23 | 10 | √ | 0.0000000000 | 至 |
| 26 | fpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_splentry_fid |  | fid |
| 2 | t_sm_splentry_pkey |  | fentryid |
