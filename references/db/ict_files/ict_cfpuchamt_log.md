# 现金流量对账日志-ict_cfpuchamt_log

## 现金流量对账日志-主表 t_ict_cfpuchamt_log

- **表名称：** 现金流量对账日志-主表
- **表名：** t_ict_cfpuchamt_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 3 | foporgid | 对方组织 | int8 | 64 |  | √ | 0 | 对方组织 |
| 4 | fcfitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 |
| 5 | fassgrpid | 核算项目 | int8 | 64 |  | √ | 0 | 核算项目 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 核算主体 |
| 8 | fschemeid | 对账方案 | int8 | 64 |  | √ | 0 | [内部交易对账方案 ict_verifyscheme](../ict_files/ict_verifyscheme.md) |
| 9 | foriperiodid | 原始期间 | int8 | 64 |  | √ | 0 | 原始期间 |
| 10 | fpullamtcaled | 是否已算抽取金额 | bpchar | 1 |  | √ | '0' | 是否已算抽取金额,枚举: 2 :未生效 0 :未计算 1 :已计算 |
| 11 | famount | 本期发生 | numeric | 25 | 10 | √ | 0 | 本期发生 |
| 12 | frelrecordid | 来源记录ID | int8 | 64 |  | √ | 0 | 来源记录ID |
| 13 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 |
| 14 | fcheckamtcaled | 是否已算勾稽金额 | bpchar | 1 |  | √ | '0' | 是否已算勾稽金额,枚举: 2 :未生效 0 :未计算 1 :已计算 |
| 15 | foperation | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作,枚举: submit :提交 enable :生效 disable :作废 delete :删除 |
| 16 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ict_cfpuchamt_log |  | fid |
| 2 | idx_ict_cfpuchamt_log_op |  | forgid,fperiodid |
