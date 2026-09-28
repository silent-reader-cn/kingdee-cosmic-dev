# 凭证科目发生日志-gl_balance_log

## 凭证科目发生日志-主表 t_gl_balance_log

- **表名称：** 凭证科目发生日志-主表
- **表名：** t_gl_balance_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 来源凭证ID | int8 | 64 |  | √ | 0 | 来源凭证ID |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 4 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | 核算项目 |
| 5 | fdebitfor | 原币借方 | numeric | 24 | 6 | √ | 0.000000 | 原币借方 |
| 6 | fcreditlocal | 本位币贷方 | numeric | 24 | 6 | √ | 0.000000 | 本位币贷方 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fcalculated | 是否已算余额 | bpchar | 1 |  | √ | '0' | 是否已算余额 |
| 9 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 核算主体 |
| 10 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 |
| 11 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 12 | fdebitlocal | 本位币借方 | numeric | 24 | 6 | √ | 0.000000 | 本位币借方 |
| 13 | fcreditqty | 贷方数量 | numeric | 24 | 6 | √ | 0.000000 | 贷方数量 |
| 14 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 |
| 15 | fdebitqty | 借方数量 | numeric | 24 | 6 | √ | 0.000000 | 借方数量 |
| 16 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 |
| 17 | foperation | 执行操作 | varchar | 30 |  | √ | ' ' | 执行操作,枚举: submit :提交 enable :生效 disable :作废 delete :删除 |
| 18 | fcount | 凭证分录数 | int8 | 64 |  | √ | 0 | 凭证分录数 |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币别 |
| 20 | fcreditfor | 原币贷方 | numeric | 24 | 6 | √ | 0.000000 | 原币贷方 |
| 21 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_balance_log_aop |  | fcalculated,faccountid,fbookid |
| 2 | t_gl_balance_log_pkey |  | fid |
| 3 | idx_gl_balance_log |  | fbookid,fcalculated |
| 4 | idx_gl_balance_log_1 |  | fcalculated,forgid,fbooktypeid |
