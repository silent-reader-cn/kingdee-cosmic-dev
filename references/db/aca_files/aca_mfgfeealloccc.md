# 制造费用分配（成本中心间）_历史单据-aca_mfgfeealloccc

## 制造费用分配（成本中心间）_历史单据-主表 t_aca_mfgfeealloccc

- **表名称：** 制造费用分配（成本中心间）_历史单据-主表
- **表名：** t_aca_mfgfeealloccc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fallocmold | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: A :制造费用归集 B :制造费用分配（成本中心间） |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 10 | fbaseunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fbillno | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 12 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |
| 13 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 14 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
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
| 27 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_mfgfeealloccc |  | forgid,fcostcenterid |
| 2 | pk_t_aca_mfgfeealloccc |  | fid |

---

## 制造费用分配（成本中心间）_历史单据-多语言表 t_aca_mfgfeealloccc_l

- **表名称：** 制造费用分配（成本中心间）_历史单据-多语言表
- **表名：** t_aca_mfgfeealloccc_l

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
| 1 | pk_t_aca_mfgfeealloccc_l |  | fpkid |
| 2 | idx_aca_mfgfeealloccc_l |  | fid,flocaleid |

---

## 单据体-子表 t_aca_mfgfeeallocccentry

- **表名称：** 单据体-子表
- **表名：** t_aca_mfgfeeallocccentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fallocvalue | 分配标准值 | numeric | 23 | 10 | √ | 0.0000000000 | 分配标准值 |
| 4 | fallocamt | 分配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分配金额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_mfgfeeallocccentry |  | fentryid |
| 2 | idx_aca_mfgfeeallocccentry |  | fid,fsubelementid |
