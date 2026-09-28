# 在产品成本调整单-aca_wipadjustbill

## 子物料信息-子表 t_aca_wipadjustbilldetail

- **表名称：** 子物料信息-子表
- **表名：** t_aca_wipadjustbilldetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubmatadjamt | 子项物料调整金额 | numeric | 23 | 10 | √ | 0 | 子项物料调整金额 |
| 2 | fsubmatadjqty | 子项物料调整数量 | numeric | 23 | 10 | √ | 0 | 子项物料调整数量 |
| 3 | fauxptyid | 子项物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fsubmatamt | 子项物料金额 | numeric | 23 | 10 | √ | 0 | 子项物料金额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 7 | fsubmaterialid | 子项物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fsubmatqty | 子项物料数量 | numeric | 23 | 10 | √ | 0 | 子项物料数量 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fsubsubelementid | 子项物料成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aca_wipadjustbilldetail |  | fentryid |
| 2 | pk_t_aca_wipadjustbilldetail |  | fdetailid |

---

## 在产品成本调整单-多语言表 t_aca_wipadjustbill_l

- **表名称：** 在产品成本调整单-多语言表
- **表名：** t_aca_wipadjustbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 60 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aca_wipadjustbill_l |  | fid |
| 2 | pk_t_aca_wipadjustbill_l |  | fpkid |

---

## 在产品成本调整单-主表 t_aca_wipadjustbill

- **表名称：** 在产品成本调整单-主表
- **表名：** t_aca_wipadjustbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fadjustbillno | 调整单单号(废弃) | varchar | 60 |  | √ | ' ' | 调整单单号(废弃) |
| 4 | fmaterialid | 所属产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fadjustqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fadjusttype | 调整类型 | varchar | 30 |  | √ | ' ' | 调整类型,枚举: START :期初调整 END :期末调整 |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 11 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 14 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fmatauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fvouchernum | 凭证字号 | varchar | 100 |  | √ | ' ' | 凭证字号 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fadjustbillid | 调整单id(废弃) | int8 | 64 |  | √ | 0 | 调整单id(废弃) |
| 22 | fwipqty | 在产品数量 | numeric | 23 | 10 | √ | 0 | 在产品数量 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 25 | fcurrencyid | 账簿币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aca_wipadjustbill |  | forgid,fmanuorgid,fcostcenterid,fcostaccountid |
| 2 | pk_t_aca_wipadjustbill |  | fid |

---

## 成本信息-子表 t_aca_wipadjustbillentry

- **表名称：** 成本信息-子表
- **表名：** t_aca_wipadjustbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | foutsourcetype | 委外成本类型 | varchar | 30 |  | √ | ' ' | 委外成本类型,枚举: A :委外加工费 B :委外费用 C :制造费用 D :物料 |
| 4 | fsubadjustid | 调整单id | int8 | 64 |  | √ | 0 | 调整单id |
| 5 | fwipamt | 在产品金额 | numeric | 23 | 10 | √ | 0 | 在产品金额 |
| 6 | fsubadjustbillno | 调整单编号 | varchar | 60 |  | √ | ' ' | 调整单编号 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aca_wipadjustbillentry |  | fid |
| 2 | pk_t_aca_wipadjustbillentry |  | fentryid |
