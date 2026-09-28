# 期初半成品结构单-sca_halfprdstructure

## 期初半成品结构单-主表 t_sca_halfprdstructure

- **表名称：** 期初半成品结构单-主表
- **表名：** t_sca_halfprdstructure

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fmaterialid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | ftotalamount | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 10 | fprdorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fversionno | 批号 | varchar | 150 |  |  | null | 批号 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 16 | fisimport | 数据首次引入标识 | varchar | 2 |  | √ | '0' | 数据首次引入标识 |
| 17 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 18 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fismodify | 手工维护 | varchar | 2 |  | √ | '1' | 手工维护 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_hpstr_orgcostacct |  | forgid,fcostaccountid |
| 2 | pk_t_sca_halfprdstructure |  | fid |
| 3 | t_sca_hpstr_billno |  | fbillno |
| 4 | t_sca_hpstr_product |  | fmaterialid |

---

## 成本构成明细-子表 t_sca_halfprdstructentry

- **表名称：** 成本构成明细-子表
- **表名：** t_sca_halfprdstructentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fisunabsorb | 来源未吸收 | varchar | 2 |  | √ | 'A' | 来源未吸收,枚举: B :是 A :否 |
| 5 | ftmptotalamt | 实际金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实际金额 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | famount | famount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | felement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 9 | fsubmaterialversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 10 | fvrtdionno | 批号 | varchar | 150 |  | √ | ' ' | 批号 |
| 11 | fsubmaterialauxpropid | 子项物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fmaterielunitid | 子项物料基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fsubmaterialid | 子项物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_hpsety_subelement |  | fsubelementid |
| 2 | t_sca_hpsety_autofid |  | fid |
| 3 | t_sca_hpsety_element |  | felement |
| 4 | pk_t_sca_halfprdstructentry |  | fentryid |

---

## 期初半成品结构单-多语言表 t_sca_halfprdstructure_l

- **表名称：** 期初半成品结构单-多语言表
- **表名：** t_sca_halfprdstructure_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemo | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_hpsetyl_autofid |  | fid |
| 2 | pk_t_sca_halfprdstructure_l |  | fpkid |
