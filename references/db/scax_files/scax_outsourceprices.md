# 产品委外标准价目表-scax_outsourceprices

## 成本子要素信息-子表 t_scax_outpricedetail

- **表名称：** 成本子要素信息-子表
- **表名：** t_scax_outpricedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fprice | 标准单价 | numeric | 23 | 10 | √ | 0 | 标准单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_outpricedetail |  | fentryid |
| 2 | pk_scax_outpricedetail |  | fdetailid |

---

## 产品委外标准价目表-多语言表 t_scax_outsourceprices_l

- **表名称：** 产品委外标准价目表-多语言表
- **表名：** t_scax_outsourceprices_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_outsourceprices_l |  | fpkid |
| 2 | idx_scax_outsourceprices_l |  | fid,flocaleid |

---

## 物料信息-子表 t_scax_outpriceentry

- **表名称：** 物料信息-子表
- **表名：** t_scax_outpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 价格来源单据编码 | varchar | 255 |  | √ | ' ' | 价格来源单据编码 |
| 3 | fpricetype | 价格类型 | varchar | 255 |  | √ | 'A' | 价格类型,枚举: A :标准采购 B :VMI采购 C :产品委外采购 D :工序委外采购 E :工序协作 |
| 4 | fsrcbillsupid | 价格来源供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 5 | fsrcbillid | 价格来源单据id | int8 | 64 |  | √ | 0 | 价格来源单据id |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdatasrc | 价格来源 | varchar | 10 |  | √ | 'manual' | 价格来源,枚举: manual :手工新增 costupdate :成本更新 order :采购订单 purchase :采购价目表 |
| 8 | famount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 9 | fsrcbillentryid | 价格来源单据分录id | int8 | 64 |  | √ | 0 | 价格来源单据分录id |
| 10 | fsrcbillentryseq | 价格来源单据行号 | int8 | 64 |  | √ | 0 | 价格来源单据行号 |
| 11 | fsrcbillsupnumber | 价格来源供应商编码 | varchar | 255 |  | √ | ' ' | 价格来源供应商编码 |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fworkprocessesid | 工序 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_outpriceentry |  | fid |
| 2 | pk_scax_outpriceentry |  | fentryid |

---

## 产品委外标准价目表-主表 t_scax_outsourceprices

- **表名称：** 产品委外标准价目表-主表
- **表名：** t_scax_outsourceprices

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdatasrc | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源,枚举: manual :手工新增 costupdate :成本更新 purprice :采购取价 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_outsourceprices |  | fbillno |
| 2 | idx_scax_outsourceprices_c |  | fcosttypeid |
| 3 | pk_scax_outsourceprices |  | fid |
