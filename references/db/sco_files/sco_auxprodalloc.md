# 辅助生产分配-sco_auxprodalloc

## 综合子单据体-子表 t_sco_auxpcomsubentry

- **表名称：** 综合子单据体-子表
- **表名：** t_sco_auxpcomsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 sco_costdriver](../sco_files/sco_costdriver.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsubexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | fsuboutamt | 金额(对外分配) | numeric | 23 | 10 | √ | 0 | 金额(对外分配) |
| 5 | fsubqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 6 | fsubinqty | 基本数量(交互分配) | numeric | 23 | 10 | √ | 0 | 基本数量(交互分配) |
| 7 | fsubinamt | 金额(交互分配) | numeric | 23 | 10 | √ | 0 | 金额(交互分配) |
| 8 | fsubbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fsubcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 10 | fsubamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fsuboutqty | 基本数量(对外分配) | numeric | 23 | 10 | √ | 0 | 基本数量(对外分配) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_auxpcomsubentry |  | fdetailid |
| 2 | idx_sco_auxpcomsubentry |  | fentryid |

---

## 来源单据-子表 t_sco_auxpsrcbillentry

- **表名称：** 来源单据-子表
- **表名：** t_sco_auxpsrcbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :制造费用归集单 B :非生产分配单 C :辅助生产分配单 D :基本生产分配单 E :辅助生产分配单-公共辅助 |
| 3 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_auxpsrcbillentry |  | fid |
| 2 | pk_sco_auxpsrcbillentry |  | fentryid |

---

## 辅助生产分配-主表 t_sco_auxprodalloc

- **表名称：** 辅助生产分配-主表
- **表名：** t_sco_auxprodalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fallocstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态,枚举: 0 :未分配 1 :已分配 2 :已确认 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fallocmold | 分配类型 | varchar | 50 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 |
| 6 | fallocmethod | 辅助分配方法 | varchar | 50 |  | √ | ' ' | 辅助分配方法,枚举: direct :直接分配法 mutual :交互分配法 algebra :代数分配法 |
| 7 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpublicaux | 是否公共辅助费用 | bpchar | 1 |  | √ | '0' | 是否公共辅助费用 |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 15 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fvouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fbookdatefield | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 21 | falloctype | 分配方式 | varchar | 30 |  | √ | ' ' | 分配方式,枚举: 1 :自动分配 2 :手工分配 |
| 22 | fallocorid | 分配人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | falloctime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 24 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_auxprodalloc |  | forgid,fmanuorgid,fcostcenterid,fcostaccountid |
| 2 | pk_sco_auxprodalloc |  | fid |

---

## 综合单据体-子表 t_sco_auxpcomentry

- **表名称：** 综合单据体-子表
- **表名：** t_sco_auxpcomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fallocsum | 分配金额合计 | numeric | 23 | 10 | √ | 0 | 分配金额合计 |
| 4 | factualoutrate | 实际费率(对外分配) | numeric | 23 | 10 | √ | 0 | 实际费率(对外分配) |
| 5 | fallocamount | 待分配费用 | numeric | 23 | 10 | √ | 0 | 待分配费用 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | factualrate | 实际费率 | numeric | 23 | 10 | √ | 0 | 实际费率 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 sco_costdriver](../sco_files/sco_costdriver.md) |
| 11 | fcostdriverqty | 分配标准合计 | numeric | 23 | 10 | √ | 0 | 分配标准合计 |
| 12 | factualinrate | 实际费率(交互分配) | numeric | 23 | 10 | √ | 0 | 实际费率(交互分配) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_auxpcomentry |  | fid,fseq |
| 2 | pk_sco_auxpcomentry |  | fentryid |

---

## 辅助生产分配-多语言表 t_sco_auxprodalloc_l

- **表名称：** 辅助生产分配-多语言表
- **表名：** t_sco_auxprodalloc_l

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
| 1 | pk_sco_auxprodalloc_l |  | fpkid |
| 2 | idx_sco_auxprodalloc_l |  | fid,flocaleid |

---

## 平行子单据体-子表 t_sco_auxpparsubentry

- **表名称：** 平行子单据体-子表
- **表名：** t_sco_auxpparsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcomsubentryid | 综合子分录id | int8 | 64 |  | √ | 0 | 综合子分录id |
| 2 | fparsubcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 sco_costdriver](../sco_files/sco_costdriver.md) |
| 3 | fparsubinamt | 金额(交互分配) | numeric | 23 | 10 | √ | 0 | 金额(交互分配) |
| 4 | fparsubexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparsuboutqty | 基本数量(对外分配) | numeric | 23 | 10 | √ | 0 | 基本数量(对外分配) |
| 7 | fparsubcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 8 | fparsubamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fparsubbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fparsubinqty | 基本数量(交互分配) | numeric | 23 | 10 | √ | 0 | 基本数量(交互分配) |
| 11 | fparsubqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fparsuboutamt | 金额(对外分配) | numeric | 23 | 10 | √ | 0 | 金额(对外分配) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_auxpparsubentry |  | fdetailid |
| 2 | idx_sco_auxpparsubentry |  | fentryid |

---

## 平行单据体-子表 t_sco_auxpparentry

- **表名称：** 平行单据体-子表
- **表名：** t_sco_auxpparentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fparbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparcostdriverqty | 分配标准值合计 | numeric | 23 | 10 | √ | 0 | 分配标准值合计 |
| 6 | fparallocamount | 待分配费用 | numeric | 23 | 10 | √ | 0 | 待分配费用 |
| 7 | fparactualoutrate | 实际费率(对外分配) | numeric | 23 | 10 | √ | 0 | 实际费率(对外分配) |
| 8 | fparactualrate | 实际费率 | numeric | 23 | 10 | √ | 0 | 实际费率 |
| 9 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 10 | fparcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 sco_costdriver](../sco_files/sco_costdriver.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fparallocsum | 分配金额合计 | numeric | 23 | 10 | √ | 0 | 分配金额合计 |
| 13 | fparactualinrate | 实际费率(交互分配) | numeric | 23 | 10 | √ | 0 | 实际费率(交互分配) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_auxpparentry |  | fid |
| 2 | pk_sco_auxpparentry |  | fentryid |
