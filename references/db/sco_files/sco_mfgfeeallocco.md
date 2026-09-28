# 成本中心内分配-sco_mfgfeeallocco

## 成本中心内分配-多语言表 t_sco_mfgfeeallocco_l

- **表名称：** 成本中心内分配-多语言表
- **表名：** t_sco_mfgfeeallocco_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfeeallocco_l |  | fpkid |
| 2 | idx_sco_mfgfeeallocco_l |  | fid,flocaleid |

---

## 来源信息-子表 t_sco_mfgfeecocomexpentry

- **表名称：** 来源信息-子表
- **表名：** t_sco_mfgfeecocomexpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsrcexpenseitemid | 来源费用项目(综合结转) | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 5 | fcolsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :制造费用归集单 B :制造费用分配单 C :非生产分配单 D :辅助生产分配单 E :基本生产分配单 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfeecocomexpentry |  | fentryid |
| 2 | idx_sco_mfgfeecocomexpentry_fk |  | fid |

---

## 分配结果-子表 t_sco_mfgfeealloccoentry

- **表名称：** 分配结果-子表
- **表名：** t_sco_mfgfeealloccoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | fsubelementid | int8 | 64 |  | √ | 0 |  |
| 3 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 4 | foutsourcetype | 委外标准成本方案 | varchar | 50 |  | √ | ' ' | 委外标准成本方案,枚举: A :委外加工费 B :委外费用 C :制造费用 |
| 5 | fallocamt | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 6 | fmaterialid | 所属产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | felementid | felementid | int8 | 64 |  | √ | 0 |  |
| 10 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgfeealloccoentry |  | fid,fcostobjectid |
| 2 | pk_sco_mfgfeealloccoentry |  | fentryid |

---

## 成本中心内分配-主表 t_sco_mfgfeeallocco

- **表名称：** 成本中心内分配-主表
- **表名：** t_sco_mfgfeeallocco

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | [产品组 sco_productweight](../sco_files/sco_productweight.md) |
| 7 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 D :成本中心内分配 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 10 | factualrate | 实际费率 | numeric | 23 | 10 | √ | 0 | 实际费率 |
| 11 | fsource | fsource | varchar | 30 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdirectalloc | 直接分配 | bpchar | 1 |  | √ | '0' | 直接分配 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 sco_costdriver](../sco_files/sco_costdriver.md) |
| 19 | fcostdriverqty | 分配标准值合计 | numeric | 23 | 10 | √ | 0 | 分配标准值合计 |
| 20 | fexpenseitemid | fexpenseitemid | int8 | 64 |  | √ | 0 |  |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 29 | fbookdatefield | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 30 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手工分配 |
| 31 | fusetype | fusetype | varchar | 30 |  | √ | ' ' |  |
| 32 | fallocorid | 分配人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fallocexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 34 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 35 | falloctime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 36 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 37 | fbenefcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 38 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfeeallocco |  | fid |
| 2 | idx_sco_mfgfeeallocco |  | forgid,fbenefcostcenterid |

---

## 来源费用项目-子表 t_sco_mfgfeecoexpentry

- **表名称：** 来源费用项目-子表
- **表名：** t_sco_mfgfeecoexpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fcolamt | 归集金额 | numeric | 23 | 10 | √ | 0 | 归集金额 |
| 4 | fexpbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :制造费用归集单 B :非生产分配单 C :辅助生产分配单 D :基本生产分配单 E :基本生产分配单(辅助) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfeecoexpentry |  | fentryid |
| 2 | idx_sco_mfgfeecoexpentry |  | fid,fseq |
