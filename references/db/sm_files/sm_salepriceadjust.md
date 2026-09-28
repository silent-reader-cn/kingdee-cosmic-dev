# 销售基价调整单-sm_salepriceadjust

## 调整明细单据体-子表 t_sm_adjprientry

- **表名称：** 调整明细单据体-子表
- **表名：** t_sm_adjprientry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricefloor | 原最低限价 | numeric | 23 | 10 | √ | 0 | 原最低限价 |
| 3 | fadjpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 4 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 7 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fprice | 原单价 | numeric | 23 | 10 | √ | 0 | 原单价 |
| 11 | fadjustflag | 调整标识 | varchar | 5 |  | √ | ' ' | 调整标识,枚举: A :保留 B :新增 |
| 12 | ftaxrateid | 原税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 14 | fqtyfrom | 从 | numeric | 23 | 10 | √ | 0 | 从 |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fsrcpriceentryid | 原价目表行ID | int8 | 64 |  | √ | 0 | 原价目表行ID |
| 17 | fadjtaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | fpriceandtax | 原含税单价 | numeric | 23 | 10 | √ | 0 | 原含税单价 |
| 19 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 20 | fsrcpricelistid | 原价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 21 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fadjpricefloor | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 23 | fadjpriceceiling | 最高限价 | numeric | 23 | 10 | √ | 0 | 最高限价 |
| 24 | fadjprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 25 | fpriceexpirydate | 原价格失效日期 | timestamp | 0 |  |  | null | 原价格失效日期 |
| 26 | fadjpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 27 | fpriceceiling | 原最高限价 | numeric | 23 | 10 | √ | 0 | 原最高限价 |
| 28 | fqtyto | 至 | numeric | 23 | 10 | √ | 0 | 至 |
| 29 | fpriceeffectdate | 原价格生效日期 | timestamp | 0 |  |  | null | 原价格生效日期 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fadjpriceexpirydate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_adjprientry_fid |  | fid |
| 2 | pk_t_sm_adjprientry |  | fentryid |

---

## 销售基价调整单-主表 t_sm_salepriceadjust

- **表名称：** 销售基价调整单-主表
- **表名：** t_sm_salepriceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fvalidtime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | feffectdate | 价目生效日期 | timestamp | 0 |  |  | null | 价目生效日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbatchadjnumber | 批量调整单号 | varchar | 80 |  | √ | ' ' | 批量调整单号 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fapplymaterial | 价目对象 | varchar | 5 |  | √ | ' ' | 价目对象,枚举: A :物料 B :物料分类 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fapplycustomer | 限定客户 | varchar | 5 |  | √ | ' ' | 限定客户,枚举: B :客户 C :客户分类 |
| 17 | fsalepricelistid | 原价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 18 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 19 | fadjustmode | 调整方式 | varchar | 10 |  | √ | ' ' | 调整方式,枚举: batch :批量调整 single :单一调整 |
| 20 | fpricelisttypeid | 价目类型 | int8 | 64 |  | √ | 0 | 价目类型 bd_pricelisttype |
| 21 | fpricelistgroupid | 价目表分组 | int8 | 64 |  | √ | 0 | 销售价目表分组 sm_salepricelistgroup |
| 22 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 23 | fexpirydate | 价目失效日期 | timestamp | 0 |  |  | null | 价目失效日期 |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_salepriceadjust |  | fid |
| 2 | idx_sm_salpriadj_fnumber |  | fbillno |

---

## 销售基价调整单-多语言表 t_sm_salepriceadjust_l

- **表名称：** 销售基价调整单-多语言表
- **表名：** t_sm_salepriceadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salepriceadjust_l_fid |  | fid,flocaleid |
| 2 | pk_t_sm_salepriceadjust_l |  | fpkid |

---

## 客户明细单据体-子表 t_sm_adjcusentry

- **表名称：** 客户明细单据体-子表
- **表名：** t_sm_adjcusentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrccustomerentryid | 原客户明细行ID | int8 | 64 |  | √ | 0 | 原客户明细行ID |
| 3 | fcustomergroupid | 客户分类编码 | int8 | 64 |  | √ | 0 | 客户分类 bd_customergroup |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcusadjustflag | 调整标识 | varchar | 5 |  | √ | ' ' | 调整标识,枚举: A :保留 B :新增 C :取消 |
| 7 | fcustomerid | 客户编码 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_adjcusentry_fid |  | fid |
| 2 | pk_t_sm_adjcusentry |  | fentryid |
