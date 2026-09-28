# 银行账户余额查询-be_balanceinquire

## 银行账户余额查询-主表 t_be_balanceinquire

- **表名称：** 银行账户余额查询-主表
- **表名：** t_be_balanceinquire

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | flogo | 银行LOGO | varchar | 100 |  | √ | ' ' | 银行LOGO |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbankaccount | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | favailablebalance | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 10 | fviewdate | 日期 | varchar | 100 |  | √ | ' ' | 日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcurrentbalance | 当前余额 | numeric | 23 | 10 | √ | 0.0000000000 | 当前余额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fisupdate | 是否更新过 | bpchar | 1 |  | √ | ' ' | 是否更新过 |
| 15 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 16 | fupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 17 | flastdaybalance | 上日余额 | numeric | 23 | 10 | √ | 0.0000000000 | 上日余额 |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | banlance |  | fbankaccount,fcurrencyid,fbizdate |
| 2 | t_be_balanceinquire_pkey |  | fid |
