# 申报表分录单据-tam_declare_entry

## 申报表分录单据-主表 t_tam_declare_entry

- **表名称：** 申报表分录单据-主表
- **表名：** t_tam_declare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :增值税 3 :城市维护建设税 4 :教育费附加 5 :地方教育附加 |
| 3 | fzerodeclare | 是否零申报 | varchar | 50 |  | √ | ' ' | 是否零申报,枚举: true :是 false :否 |
| 4 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 7 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tam_declare_entry |  | fentryid |
| 2 | idx_tam_declare_entry_fk |  | fid |
