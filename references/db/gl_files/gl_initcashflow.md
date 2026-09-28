# 现金流量初始化-gl_initcashflow

## 现金流量初始化-主表 t_gl_initcashflow

- **表名称：** 现金流量初始化-主表
- **表名：** t_gl_initcashflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 3 | fyearamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 4 | fcfitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 5 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftabdelete | 删除标记 | bpchar | 1 |  | √ | '0' | 删除标记 |
| 8 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_initcashflow |  | forgid,fbooktypeid,fcfitemid,fassgrpid,fcurrencyid |
| 2 | idx_gl_initcashflow_cf |  | fcfitemid |
| 3 | t_gl_initcashflow_pkey |  | fid |
