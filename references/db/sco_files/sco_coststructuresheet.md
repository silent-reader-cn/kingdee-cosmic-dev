# 成本结构单-sco_coststructuresheet

## 成本结构单-多语言表 t_sco_coststructuresheet_l

- **表名称：** 成本结构单-多语言表
- **表名：** t_sco_coststructuresheet_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_coststructuresheet_l |  | fpkid |
| 2 | idx_sco_coststructuresheet_l |  | fid |

---

## 成本构成明细-子表 t_sco_structuresheet_dtl

- **表名称：** 成本构成明细-子表
- **表名：** t_sco_structuresheet_dtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsonauxpropid | 子项物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fmodel | 规格型号 | varchar | 80 |  | √ | ' ' | 规格型号 |
| 5 | fmaterialid | 子项物料编码/费用项目编码 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 6 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 9 | fcvertvkpd | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 10 | fsonnum | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 11 | fhidematerielid | 影藏物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fsubjectormateriel | 子项物料/费用项目 | varchar | 80 |  | √ | ' ' | 子项物料/费用项目,枚举: er_expenseitemedit :费用项目 bd_material :物料 |
| 13 | fsonversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fmaterialname | 子项物料名称/费用项目名称 | varchar | 255 |  | √ | ' ' | 子项物料名称/费用项目名称 |
| 16 | fsunamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_structuresheet_dtl |  | fentryid |
| 2 | idx_sco_structuresheet_dtl |  | fsubelementid,fid |

---

## 成本结构单-主表 t_sco_coststructuresheet

- **表名称：** 成本结构单-主表
- **表名：** t_sco_coststructuresheet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fitemversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fversionno | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 16 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_coststructuresheet |  | forgid,fcostaccountid |
| 2 | pk_sco_coststructuresheet |  | fid |
