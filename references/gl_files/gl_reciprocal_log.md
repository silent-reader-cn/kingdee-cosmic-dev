# 核销日志-gl_reciprocal_log

## 核销日志-主表 t_gl_reciprocal_log

- **表名称：** 核销日志-主表
- **表名：** t_gl_reciprocal_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 3 | fwriteoffdate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | famount | 本位币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本位币金额 |
| 8 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 9 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 10 | flocalcurrencyid | 本位币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 11 | fwriteoffentryid | 核销记录 | int8 | 64 |  | √ | 0 | 核销记录 |
| 12 | fbuyerentryid | 挂账记录 | int8 | 64 |  | √ | 0 | 挂账记录 |
| 13 | famountfor | 原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原币金额 |
| 14 | fcurrencyid | 原币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fwriter | 核销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 17 | fwriteofftype | 核销类型 | bpchar | 1 |  | √ | '0' | 核销类型,枚举: 0 :手工核销 1 :自动核销 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_reciprocal_log_fweid |  | fwriteoffentryid |
| 2 | t_gl_reciprocal_log_pkey |  | fid |
| 3 | idx_gl_reciprocal_log_fbeid |  | fbuyerentryid |
| 4 | idx_gl_reciprocal_faccount |  | forgid,fbooktypeid,faccountid,fassgrpid,fcurrencyid |
