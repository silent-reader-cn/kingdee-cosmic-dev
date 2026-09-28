# 科目对账日志表-ict_acctpuchamt_log

## 科目对账日志表-主表 t_ict_acctpuchamt_log

- **表名称：** 科目对账日志表-主表
- **表名：** t_ict_acctpuchamt_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 3 | foporgid | 对方组织 | int8 | 64 |  | √ | 0 | 对方组织 |
| 4 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | 核算项目 |
| 5 | fdebitfor | 原币借方 | numeric | 25 | 10 | √ | 0 | 原币借方 |
| 6 | fcreditlocal | 本位币贷方 | numeric | 25 | 10 | √ | 0 | 本位币贷方 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 核算主体 |
| 9 | fschemeid | 对账方案 | int8 | 64 |  | √ | 0 | [内部交易对账方案 ict_verifyscheme](../ict_files/ict_verifyscheme.md) |
| 10 | foriperiodid | 原始期间 | int8 | 64 |  | √ | 0 | 原始期间 |
| 11 | fpullamtcaled | 是否已算抽取金额 | bpchar | 1 |  | √ | '0' | 是否已算抽取金额,枚举: 2 :未生效 0 :未计算 1 :已计算 |
| 12 | frelrecordid | 来源记录ID | int8 | 64 |  | √ | 0 | 来源记录ID |
| 13 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 |
| 14 | fdebitlocal | 本位币借方 | numeric | 25 | 10 | √ | 0 | 本位币借方 |
| 15 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 |
| 16 | fcheckamtcaled | 是否已算勾稽金额 | bpchar | 1 |  | √ | '0' | 是否已算勾稽金额,枚举: 2 :未生效 0 :未计算 1 :已计算 |
| 17 | foperation | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作,枚举: submit :提交 enable :生效 disable :作废 delete :删除 |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币别 |
| 19 | fcreditfor | 原币贷方 | numeric | 25 | 10 | √ | 0 | 原币贷方 |
| 20 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ict_acctpuchamt_log |  | fid |
| 2 | idx_ict_acctpuchamt_log_op |  | forgid,fperiodid |
