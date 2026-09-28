# 非生产分配-cad_nonprodalloc

## 非生产分配-多语言表 t_cad_nonprodalloc_l

- **表名称：** 非生产分配-多语言表
- **表名：** t_cad_nonprodalloc_l

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
| 1 | pk_t_cad_nonprodalloc_l |  | fpkid |
| 2 | idx_t_cad_nonprodalloc_l |  | fid,flocaleid |

---

## 非生产分配-主表 t_cad_nonprodalloc

- **表名称：** 非生产分配-主表
- **表名：** t_cad_nonprodalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fallocmold | 分配类型 | varchar | 50 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 13 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |
| 14 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 15 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fvouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fbookdatefield | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手工分配 |
| 25 | fallocorid | 分配人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | falloctime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 27 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 28 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_nonprodalloc |  | forgid,fmanuorgid,fcostcenterid,fcostaccountid |
| 2 | pk_t_cad_nonprodalloc |  | fid |

---

## 来源单据-子表 t_cad_nonprodsrcbillentry

- **表名称：** 来源单据-子表
- **表名：** t_cad_nonprodsrcbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :制造费用归集单 B :非生产分配单 C :辅助生产分配单 D :基本生产分配单 E :辅助生产分配单-公共辅助 |
| 3 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_nonprodsrcbillentry |  | fid,fseq |
| 2 | pk_t_cad_nonprodsrcbillentry |  | fentryid |

---

## 单据体-子表 t_cad_nonprodallocentry

- **表名称：** 单据体-子表
- **表名：** t_cad_nonprodallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 3 | fallocamt | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_nonprodallocentry |  | fid |
| 2 | pk_t_cad_nonprodallocentry |  | fentryid |
