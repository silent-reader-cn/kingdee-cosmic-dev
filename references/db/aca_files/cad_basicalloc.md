# 基本生产分配-cad_basicalloc

## 单据体-子表 t_cad_basicallocentry

- **表名称：** 单据体-子表
- **表名：** t_cad_basicallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fentryamount | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 4 | fentryqty | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 5 | fentrycostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 6 | fentryexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fentrycostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_basicallocen_fid |  | fid |
| 2 | pk_t_cad_basicallocentry |  | fentryid |
| 3 | idx_t_cad_basicallocentry |  | fentrycostcenterid,fentryexpenseitemid,fentrycostdriverid |

---

## 综合单据体-子表 t_cad_basicpcomentry

- **表名称：** 综合单据体-子表
- **表名：** t_cad_basicpcomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fallocsum | 分配金额合计 | numeric | 23 | 10 | √ | 0 | 分配金额合计 |
| 4 | fallocamount | 待分配费用 | numeric | 23 | 10 | √ | 0 | 待分配费用 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcomcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |
| 7 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcostdriverqty | 分配标准值合计 | numeric | 23 | 10 | √ | 0 | 分配标准值合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_basicpcomentry |  | fentryid |
| 2 | idx_t_cad_basicpcomentry |  | fid,fcomexpenseitemid,fcomcostdriverid |

---

## 来源单据-子表 t_cad_basicpsrcbillentry

- **表名称：** 来源单据-子表
- **表名：** t_cad_basicpsrcbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :制造费用归集单 B :非生产分配单 C :辅助生产分配单 D :基本生产分配单 |
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
| 1 | pk_t_cad_basicpsrcbillentry |  | fentryid |
| 2 | idx_cad_basicpsrcen_fid |  | fid |
| 3 | idx_t_cad_basicpsrcbillentry |  | fsrcbillid,ftype,fid |

---

## 综合子单据体-子表 t_cad_basicpcomsubentry

- **表名称：** 综合子单据体-子表
- **表名：** t_cad_basicpcomsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fsubamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fcomsubexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fsubqty | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fcomsubcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |
| 9 | fsubbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_basicpcomsubentry |  | fentryid |
| 2 | pk_t_cad_basicpcomsubentry |  | fdetailid |

---

## 平行子单据体-子表 t_cad_basicpparsubentry

- **表名称：** 平行子单据体-子表
- **表名：** t_cad_basicpparsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparsubcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |
| 2 | fparsubexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fparsubbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fparsubcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 6 | fparsubqty | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fparsubamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_basicpparsubentry |  | fentryid |
| 2 | pk_t_cad_basicpparsubentry |  | fdetailid |

---

## 平行单据体-子表 t_cad_basicpparentry

- **表名称：** 平行单据体-子表
- **表名：** t_cad_basicpparentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fcomparexpitemid | 综合结转费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | fparactualrate | 实际费率 | numeric | 23 | 10 | √ | 0 | 实际费率 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fparcostdriverqty | 分配标准值合计 | numeric | 23 | 10 | √ | 0 | 分配标准值合计 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fparbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fparallocsum | 分配金额合计 | numeric | 23 | 10 | √ | 0 | 分配金额合计 |
| 12 | fparallocamount | 待分配费用 | numeric | 23 | 10 | √ | 0 | 待分配费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_basicpparentry |  | fentryid |
| 2 | idx_t_cad_basicpparentry |  | fid,fparexpenseitemid,fparcostdriverid |

---

## 基本生产分配-主表 t_cad_basicalloc

- **表名称：** 基本生产分配-主表
- **表名：** t_cad_basicalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 4 | fscrbilltype | 分配单来源 | varchar | 50 |  | √ | ' ' | 分配单来源,枚举: A :归集单或非生产分配 B :辅助生产分配 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 7 | fallocmold | 分配类型 | varchar | 50 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: A :制造费用分配单 B :制造费用归集单 C :非生产分配单 D :辅助生产分配单 |
| 13 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 14 | fbillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 15 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 20 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fvouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fbookdatefield | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 27 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手工分配 |
| 28 | fallocorid | 分配人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | falloctime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 31 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_basicalloc |  | forgid,fmanuorgid,fcostcenterid,fcostaccountid |
| 2 | pk_t_cad_basicalloc |  | fid |

---

## 基本生产分配-多语言表 t_cad_basicalloc_l

- **表名称：** 基本生产分配-多语言表
- **表名：** t_cad_basicalloc_l

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
| 1 | pk_t_cad_basicalloc_l |  | fpkid |
| 2 | idx_t_cad_basicalloc_l |  | fid,flocaleid |
