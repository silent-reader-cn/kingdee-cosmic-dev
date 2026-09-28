# 汇总即征即退进项税额底稿明细-tcvat_hz_jzjt_jxse_acc

## 汇总即征即退进项税额底稿明细-主表 t_tcvat_hz_jzjt_jxse_acc

- **表名称：** 汇总即征即退进项税额底稿明细-主表
- **表名：** t_tcvat_hz_jzjt_jxse_acc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 5 | famount | 即征即退进项税额 | numeric | 23 | 10 | √ | 0 | 即征即退进项税额 |
| 6 | fskssqq | fskssqq | timestamp | 0 |  |  | null |  |
| 7 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 8 | fskssqz | fskssqz | timestamp | 0 |  |  | null |  |
| 9 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 10 | fsuborgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 12 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 13 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 14 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 15 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 16 | ffiltercondition | 过滤条件设置 | varchar | 2000 |  | √ | ' ' | 过滤条件设置 |
| 17 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 18 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_hz_jzjt_jxse_acc_1 |  | forgid,fskssqq,fskssqz |
| 2 | pk_tcvat_hz_jzjt_jxse_acc |  | fid |
