# 往来账记录-gl_acccurrent

## 往来账记录-主表 t_gl_acccurrent

- **表名称：** 往来账记录-主表
- **表名：** t_gl_acccurrent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 3 | famountbalfor | 原币余额 | numeric | 23 | 10 | √ | 0.0000000000 | 原币余额 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | famount | 挂账本位币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 挂账本位币金额 |
| 6 | fbiznum | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 7 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 8 | flocalcurrencyid | 本位币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fstatus | 核销状态 | bpchar | 1 |  | √ | '0' | 核销状态,枚举: 0 :未核销 1 :部分核销 2 :全部核销 |
| 10 | fentrydc | 借贷方向 | varchar | 2 |  | √ | '1' | 借贷方向,枚举: 1 :借 -1 :贷 |
| 11 | fmasterid | 原往来记录ID（版本化） | int8 | 64 |  | √ | 0 | 原往来记录ID（版本化） |
| 12 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | '0' | 来源类型,枚举: 0 :其他 1 :冲销 2 :应收 3 :应付 4 :收款 5 :付款 |
| 15 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 16 | feffectivedate | 启用日期（版本化） | timestamp | 0 |  |  | null | 启用日期（版本化） |
| 17 | famountfor | 挂账原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 挂账原币金额 |
| 18 | famountbal | 本位币余额 | numeric | 23 | 10 | √ | 0.0000000000 | 本位币余额 |
| 19 | fvoucherid | 凭证内码 | int8 | 64 |  | √ | 0 | 凭证内码 |
| 20 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 21 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fdescription | 摘要 | varchar | 1020 |  | √ | ' ' | 摘要 |
| 24 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 25 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 26 | fvchentryid | 凭证分录 | int8 | 64 |  | √ | 0 | 凭证分录 |
| 27 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | funeffectivedate | 失效日期（版本化） | timestamp | 0 |  |  | null | 失效日期（版本化） |
| 29 | fcurrencyid | 原币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 30 | faccountid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 31 | fwriteoffpersonid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_acccurrent |  | forgid,fbooktypeid,fperiodid,faccountid,fassgrpid |
| 2 | idx_gl_acccurrent_2 |  | fbooktypeid,forgid,faccountid,fassgrpid |
| 3 | t_gl_acccurrent_pkey |  | fid |
| 4 | idx_gl_acccurrent_vchentryid |  | fvchentryid |
| 5 | idx_gl_acccurrent_vchid |  | fvoucherid |
| 6 | idx_gl_acccurrent_masterid |  | fmasterid |
