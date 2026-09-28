# 往来余额初始化-gl_initacccurrent

## 往来余额初始化-主表 t_gl_initacccurrent

- **表名称：** 往来余额初始化-主表
- **表名：** t_gl_initacccurrent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freciprocalrecordid | 往来账 | int8 | 64 |  | √ | 0 | 往来账基础资料 gl_reciprocal_record_base |
| 3 | famountlocal | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 4 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 8 | fbizbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 9 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 10 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 11 | fcurlocal | 本位币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | fdeadlinedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 13 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | famountfor | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_initacccurrent |  | forgid,fbooktypeid,faccountid,fcurrencyid,fassgrpid |
| 2 | t_gl_initacccurrent_pkey |  | fid |
| 3 | idx_gl_initacccurrent_acct |  | faccountid |
