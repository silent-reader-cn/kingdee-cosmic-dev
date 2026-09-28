# 纳税申报子表-tctb_declare_entry

## 纳税申报子表-主表 t_tctb_declare_entry

- **表名称：** 纳税申报子表-主表
- **表名：** t_tctb_declare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 2 | fszysno | fszysno | varchar | 50 |  | √ | ' ' |  |
| 3 | fqjje | 欠缴金额 | numeric | 23 | 10 | √ | 0 | 欠缴金额 |
| 4 | fyjsjje | 预缴实缴金额 | numeric | 23 | 10 | √ | 0 | 预缴实缴金额 |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fdeferpayapply | 申请缓缴 | bpchar | 1 |  | √ | '0' | 申请缓缴 |
| 7 | fsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 8 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 9 | fjmse | fjmse | numeric | 23 | 10 | √ | 0 |  |
| 10 | fynse | fynse | numeric | 23 | 10 | √ | 0 |  |
| 11 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ftaxtype | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :增值税 2 :附加税费 3 :城市维护建设税 4 :教育费附加 5 :地方教育附加 |
| 14 | fbqdybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_entry |  | fentryid |
| 2 | idx_tctb_declare_entry_fk |  | fid |
