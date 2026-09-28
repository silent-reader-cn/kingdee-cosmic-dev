# 预算控制结果单-xkbm_ctrlresult

## 单据体-子表 t_xkbm_ctrlresultentry

- **表名称：** 单据体-子表
- **表名：** t_xkbm_ctrlresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | ' ' | 是否超预算,枚举: 0 :否 1 :是 |
| 3 | foverrate | 超预算率% | numeric | 23 | 10 | √ | 0 | 超预算率% |
| 4 | fgroupid | 维度组 | varchar | 50 |  | √ | ' ' | 维度组 |
| 5 | fctrltime | 预算影响类型 | bpchar | 1 |  | √ | ' ' | 预算影响类型,枚举: 1 :申请占用 2 :预算执行 3 :预算冲回 |
| 6 | fmessage | 控制结果 | varchar | 2000 |  | √ | ' ' | 控制结果 |
| 7 | fruletype | 控制规则类型 | varchar | 50 |  | √ | ' ' | 控制规则类型,枚举: xkbm_ctrlrule :预算控制规则 xkbm_ratectrlrule :比率预算控制规则 xkpb_ctrlrule :项目预算控制规则 fpm_ctrlrule :计划控制规则 |
| 8 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fbudgetvalue | 预算数 | numeric | 23 | 10 | √ | 0 | 预算数 |
| 11 | fbillvalue | 单据实际数 | numeric | 23 | 10 | √ | 0 | 单据实际数 |
| 12 | fbackvalue | 冲回数 | numeric | 23 | 10 | √ | 0 | 冲回数 |
| 13 | fruleid | 控制规则 | int8 | 64 |  | √ | 0 | 预算控制规则 xkbm_ctrlrule |
| 14 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 15 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 16 | fisnullbudgetdatanew | 预算数为空 | bpchar | 1 |  | √ | ' ' | 预算数为空,枚举: 0 :否 1 :是 |
| 17 | fbudgetyear | 预算年度 | varchar | 10 |  | √ | ' ' | 预算年度 |
| 18 | fbudgetperiod | 预算期间 | varchar | 10 |  | √ | ' ' | 预算期间 |
| 19 | fexcuterate | 执行率% | numeric | 23 | 10 | √ | 0 | 执行率% |
| 20 | fovervalue | 超预算额 | numeric | 23 | 10 | √ | 0 | 超预算额 |
| 21 | fdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |
| 22 | fwarpvalue | 浮动数 | numeric | 23 | 10 | √ | 0 | 浮动数 |
| 23 | fyear | 年度 | int8 | 64 |  | √ | 0 | 年度 |
| 24 | fperiodtype | 期间类型 | varchar | 10 |  | √ | ' ' | 期间类型 |
| 25 | fperiod | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 26 | fusedvalue | 执行数 | numeric | 23 | 10 | √ | 0 | 执行数 |
| 27 | fbusinesstypeid | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 28 | freleasevalue | 释放数 | numeric | 23 | 10 | √ | 0 | 释放数 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rstentry_fid |  | fid |
| 2 | pk_t_xkbm_ctrlresultentry |  | fentryid |

---

## 单据体-多语言表 t_xkbm_ctrlresultentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_xkbm_ctrlresultentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmessage | 控制结果 | varchar | 2000 |  | √ | ' ' | 控制结果 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_ctrlresultentry_l |  | fpkid |
| 2 | idx_xkbm_rstentry_l_fid |  | fentryid,flocaleid |

---

## 预算控制结果单-主表 t_xkbm_ctrlresult

- **表名称：** 预算控制结果单-主表
- **表名：** t_xkbm_ctrlresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillformid | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 4 | fisexistoverbudget | 是否存在超预算 | bpchar | 1 |  | √ | '0' | 是否存在超预算,枚举: 0 :否 1 :是 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisexistnullbudgetdata | 是否存在预算数为空 | bpchar | 1 |  | √ | '0' | 是否存在预算数为空,枚举: 0 :否 1 :是 |
| 8 | fmaxexcuterate | 整单最大预算执行率% | numeric | 23 | 10 | √ | 0 | 整单最大预算执行率% |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fisexistzerobudget | 是否存在预算数为零 | bpchar | 1 |  | √ | '0' | 是否存在预算数为零,枚举: 0 :否 1 :是 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fmaxovervalue | 整单最大超预算额 | numeric | 23 | 10 | √ | 0 | 整单最大超预算额 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmaxoverrate | 整单最大超预算率% | numeric | 23 | 10 | √ | 0 | 整单最大超预算率% |
| 16 | fbillid | 单据内码 | varchar | 50 |  | √ | ' ' | 单据内码 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctrlresult_billid |  | fbillid |
| 2 | pk_t_xkbm_ctrlresult |  | fid |
| 3 | idx_ctrlresult_formid |  | fbillformid |
