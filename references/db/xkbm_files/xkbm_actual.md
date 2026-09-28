# 预算实际执行数-xkbm_actual

## 预算实际执行数-主表 t_xkbm_actual

- **表名称：** 预算实际执行数-主表
- **表名：** t_xkbm_actual

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillformid | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 5 | fmessage | 控制结果 | varchar | 2000 |  | √ | ' ' | 控制结果 |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 9 | fruletype | 控制规则类型 | varchar | 50 |  | √ | ' ' | 控制规则类型,枚举: xkbm_ctrlrule :预算控制规则 xkbm_ratectrlrule :比率预算控制规则 xkpb_ctrlrule :项目预算控制规则 fpm_ctrlrule :计划控制规则 |
| 10 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fmaxovervalue | 整单最大超预算额 | numeric | 23 | 10 | √ | 0 | 整单最大超预算额 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fisnullbudgetdata | 预算数为空 | bpchar | 1 |  | √ | ' ' | 预算数为空,枚举: 0 :否 1 :是 |
| 16 | fmaxoverrate | 整单最大超预算率% | numeric | 23 | 10 | √ | 0 | 整单最大超预算率% |
| 17 | fyear | 年度 | int8 | 64 |  | √ | 0 | 年度 |
| 18 | fperiodtype | 期间类型 | varchar | 10 |  | √ | ' ' | 期间类型 |
| 19 | fbillid | 单据内码 | varchar | 50 |  | √ | ' ' | 单据内码 |
| 20 | fperiod | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 21 | fruleid | 控制规则 | int8 | 64 |  | √ | 0 | 预算控制规则 xkbm_ctrlrule |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_actual_fperiodtype |  | fperiodtype |
| 2 | pk_actual_fschemeid |  | fschemeid |
| 3 | pk_actual_fbillformid |  | fbillformid |
| 4 | pk_actual_fyear |  | fyear |
| 5 | pk_t_xkbm_actual |  | fid |
| 6 | pk_actual_fruleid |  | fruleid |
| 7 | pk_actual_fbillid |  | fbillid |
| 8 | pk_actual_fperiod |  | fperiod |

---

## 单据体-子表 t_xkbm_actualvalue

- **表名称：** 单据体-子表
- **表名：** t_xkbm_actualvalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 3 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | ' ' | 是否超预算,枚举: 0 :否 1 :是 |
| 4 | foverrate | 超预算率% | numeric | 23 | 10 | √ | 0 | 超预算率% |
| 5 | fgroupid | 维度组 | varchar | 50 |  | √ | ' ' | 维度组 |
| 6 | fctrltime | 预算影响类型 | bpchar | 1 |  | √ | ' ' | 预算影响类型,枚举: 1 :申请占用 2 :预算执行 3 :预算冲回 |
| 7 | fisnullbudgetdatanew | 预算数为空 | bpchar | 1 |  | √ | ' ' | 预算数为空,枚举: 0 :否 1 :是 |
| 8 | fbudgetyear | 预算年度 | varchar | 10 |  | √ | ' ' | 预算年度 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fbudgetvalue | 预算数 | numeric | 23 | 10 | √ | 0 | 预算数 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillvalue | 单据实际数 | numeric | 23 | 10 | √ | 0 | 单据实际数 |
| 13 | fbudgetperiod | 预算期间 | varchar | 10 |  | √ | ' ' | 预算期间 |
| 14 | fexcuterate | 执行率% | numeric | 23 | 10 | √ | 0 | 执行率% |
| 15 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fovervalue | 超预算额 | numeric | 23 | 10 | √ | 0 | 超预算额 |
| 17 | fdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |
| 18 | fwarpvalue | 浮动数 | numeric | 23 | 10 | √ | 0 | 浮动数 |
| 19 | fbackvalue | 冲回数 | numeric | 23 | 10 | √ | 0 | 冲回数 |
| 20 | fusedvalue | 执行数 | numeric | 23 | 10 | √ | 0 | 执行数 |
| 21 | fbusinesstypeid | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 22 | freleasevalue | 释放数 | numeric | 23 | 10 | √ | 0 | 释放数 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_actualvalue_fid |  | fid |
| 2 | pk_t_xkbm_actualvalue |  | fentryid |

---

## 预算实际执行数-多语言表 t_xkbm_actual_l

- **表名称：** 预算实际执行数-多语言表
- **表名：** t_xkbm_actual_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 控制结果 | varchar | 2000 |  | √ | ' ' | 控制结果 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_actual_l_fid |  | fid |
| 2 | pk_t_xkbm_actual_l |  | fpkid |
