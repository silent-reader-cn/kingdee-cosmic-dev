# 查询请求记录-cdm_queryrequest

## 查询请求记录-主表 t_cdm_queryrequest

- **表名称：** 查询请求记录-主表
- **表名：** t_cdm_queryrequest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | finterfacetype | 数据接口类型 | varchar | 50 |  | √ | ' ' | 数据接口类型,枚举: 0 :新一代票据接口 1 :传统票据接口 |
| 4 | fquerydrafttype | 查询票据分类 | varchar | 50 |  | √ | ' ' | 查询票据分类,枚举: reply :待签收票据 hold :在手票据 |
| 5 | fpublishtime | 请求发送时间 | timestamp | 0 |  |  | null | 请求发送时间 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbegindate | 查询日期范围.开始 | timestamp | 0 |  |  | null | 查询日期范围.开始 |
| 8 | fexception_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenddate | 查询日期范围.结束 | timestamp | 0 |  |  | null | 查询日期范围.结束 |
| 11 | fstatus | 请求状态 | varchar | 50 |  | √ | ' ' | 请求状态,枚举: nostart :未开始 querying :查询中 success :成功 failed :失败 |
| 12 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftrantype | 查询业务种类 | varchar | 50 |  | √ | ' ' | 查询业务种类,枚举: 02 :出票人提示承兑 03 :出票人提示收票 10 :背书转让 18 :质押 19 :质押解除 20 :提示付款 21 :逾期提示付款 100006 :背书已签收 |
| 14 | frequestid | 请求Id | int8 | 64 |  | √ | 0 | 请求Id |
| 15 | fexception | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 16 | ftaskid | 查询任务id | int8 | 64 |  | √ | 0 | [查询任务记录 cdm_querytaskinfo](../cdm_files/cdm_querytaskinfo.md) |
| 17 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fdrafttype | 类别 | varchar | 50 |  | √ | ' ' | 类别,枚举: AC01 :银行承兑汇票 AC02 :商业承兑汇票 AC99 :财务公司承兑汇票 |
| 19 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cdm_queryrequest |  | fid |
| 2 | idx_taskid |  | ftaskid |
