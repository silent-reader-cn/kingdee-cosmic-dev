# 总机构收入台账未开票明细单据-tcvat_hz_accdetail_income

## 总机构收入台账未开票明细单据-主表 t_tcvat_hz_accdetail_come

- **表名称：** 总机构收入台账未开票明细单据-主表
- **表名：** t_tcvat_hz_accdetail_come

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: 1 :其他发票不含税收入取数 2 :其他发票不含税税额取数 3 :未开票收入取数 4 :未开票税额取数 |
| 10 | fsuborgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 13 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 14 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 15 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 16 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 17 | fdifferenceinvoice | 差额发票 | bpchar | 1 |  | √ | '0' | 差额发票 |
| 18 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 19 | ffiltercondition | 过滤条件设置 | varchar | 1000 |  | √ | ' ' | 过滤条件设置 |
| 20 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 21 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |
| 22 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_accdetail_come_fserialno |  | ftaxaccountserialno |
| 2 | pk_tcvat_hz_accdetail_come |  | fid |
| 3 | idx_tcvat_hz_accdetail_come |  | fsuborgid,fskssqq,fskssqz |
