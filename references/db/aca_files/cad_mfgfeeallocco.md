# 成本中心内分配-cad_mfgfeeallocco

## 成本中心内分配-主表 t_cad_mfgfeeallocco

- **表名称：** 成本中心内分配-主表
- **表名：** t_cad_mfgfeeallocco

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fallocmold | 分配类型 | varchar | 50 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 D :成本中心内分配 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | factualrate | 实际费率 | numeric | 23 | 10 | √ | 0 | 实际费率 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fdirectalloc | 直接分配 | bpchar | 1 |  | √ | '0' | 直接分配 |
| 13 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 16 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |
| 17 | fcostdriverqty | 分配标准值合计 | numeric | 23 | 10 | √ | 0 | 分配标准值合计 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcostcenterid | fcostcenterid | int8 | 64 |  | √ | 0 |  |
| 20 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fvouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 26 | fbookdatefield | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 27 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手工分配 |
| 28 | fallocorid | 分配人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | falloctime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 31 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_mfgfeeallocco |  | forgid,fmanuorgid,fcostcenterid,fcostaccountid |
| 2 | pk_t_cad_mfgfeeallocco |  | fid |

---

## 来源信息-子表 t_cad_mfgfeecocomexpentry

- **表名称：** 来源信息-子表
- **表名：** t_cad_mfgfeecocomexpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsrcexpenseitemid | 来源费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 5 | fcolsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :制造费用归集单 B :制造费用分配单 C :非生产分配单 D :辅助生产分配单 E :基本生产分配单 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_mfgfeecocomexpentry |  | fentryid |
| 2 | idx_t_cad_mfgfeecocomexpentry |  | fid |

---

## 来源费用项目-子表 t_cad_mfgfeecoexpentry

- **表名称：** 来源费用项目-子表
- **表名：** t_cad_mfgfeecoexpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fcolamt | 归集金额 | numeric | 23 | 10 | √ | 0 | 归集金额 |
| 4 | fexpbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :制造费用归集单 B :非生产分配单 C :辅助生产分配单 D :基本生产分配单 E :基本生产分配单(辅助) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_mfgfeecoexpentry |  | fid |
| 2 | pk_t_cad_mfgfeecoexpentry |  | fentryid |

---

## 分配结果-子表 t_cad_mfgfeealloccoentry

- **表名称：** 分配结果-子表
- **表名：** t_cad_mfgfeealloccoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 3 | foutsourcetype | 委外成本类型 | varchar | 50 |  | √ | ' ' | 委外成本类型,枚举: A :委外加工费 B :委外费用 C :制造费用 |
| 4 | fallocamt | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 5 | fmaterialid | 所属产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_mfgfeealloccoentry |  | fid |
| 2 | pk_t_cad_mfgfeealloccoentry |  | fentryid |

---

## 成本中心内分配-多语言表 t_cad_mfgfeeallocco_l

- **表名称：** 成本中心内分配-多语言表
- **表名：** t_cad_mfgfeeallocco_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_mfgfeeallocco_l |  | fpkid |
| 2 | idx_t_cad_mfgfeeallocco_l |  | fid,flocaleid |
