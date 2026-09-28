# 制造费用分配（成本中心）_历史单据-aca_mfgfeeallocco

## 单据体-子表 t_aca_mfgfeealloccoentry

- **表名称：** 单据体-子表
- **表名：** t_aca_mfgfeealloccoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0.0000000000 | 分配标准值 |
| 4 | fallocamt | 分配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分配金额 |
| 5 | fmaterialid | 所属产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 9 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_mfgfeealloccoentry |  | fid,fcostobjectid |
| 2 | pk_t_aca_mfgfeealloccoentry |  | fentryid |

---

## 制造费用分配（成本中心）_历史单据-多语言表 t_aca_mfgfeeallocco_l

- **表名称：** 制造费用分配（成本中心）_历史单据-多语言表
- **表名：** t_aca_mfgfeeallocco_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_mfgfeeallocco_l |  | fpkid |
| 2 | idx_aca_mfgfeeallocco_l |  | fid,flocaleid |

---

## 制造费用分配（成本中心）_历史单据-主表 t_aca_mfgfeeallocco

- **表名称：** 制造费用分配（成本中心）_历史单据-主表
- **表名：** t_aca_mfgfeeallocco

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | 产品组 cad_productintogroup |
| 5 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: A :制造费用归集 B :制造费用分配（成本中心间） |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 13 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |
| 14 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fvouchernum | 凭证号 | varchar | 60 |  | √ | ' ' | 凭证号 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手工分配 |
| 23 | fusetype | 耗用类型 | varchar | 30 |  | √ | ' ' | 耗用类型,枚举: 1 :共耗 2 :直接 |
| 24 | fallocorid | 分配人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 26 | falloctime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 27 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 28 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_mfgfeeallocco |  | fid |
| 2 | idx_aca_mfgfeeallocco |  | forgid,fbenefcostcenterid |

---

## 子单据体-子表 t_aca_feeallocsubentry

- **表名称：** 子单据体-子表
- **表名：** t_aca_feeallocsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcostobjectgroupid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 2 | fsubelementgroupid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fauxptygroupid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | felementgroupid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 5 | fallocvaluegroup | 分配标准值 | numeric | 23 | 10 | √ | 0.0000000000 | 分配标准值 |
| 6 | fmaterialgroupid | 所属产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fproducttypegroup | fproducttypegroup | varchar | 30 |  | √ | ' ' |  |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fallocamtgroup | 分配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分配金额 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_feeallocsubentry |  | fentryid,fcostobjectgroupid |
| 2 | pk_t_aca_feeallocsubentry |  | fdetailid |
