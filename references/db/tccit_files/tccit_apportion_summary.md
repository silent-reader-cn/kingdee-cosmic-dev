# 税款分摊台账单据-tccit_apportion_summary

## 税款分摊台账单据-主表 t_tccit_apportion_summary

- **表名称：** 税款分摊台账单据-主表
- **表名：** t_tccit_apportion_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftotalassets | 资产总额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产总额 |
| 4 | fincome | 营业收入 | numeric | 23 | 10 | √ | 0.0000000000 | 营业收入 |
| 5 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 6 | femolument | 职工薪酬 | numeric | 23 | 10 | √ | 0.0000000000 | 职工薪酬 |
| 7 | funifiedsocialcode | 分支机构社会统一信用代码 | varchar | 100 |  | √ | ' ' | 分支机构社会统一信用代码 |
| 8 | frate | 分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 分配比例 |
| 9 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 10 | ftaxorgname | 分支机构名称 | varchar | 100 |  | √ | ' ' | 分支机构名称 |
| 11 | fyear | 年(年度申报分支机构专用) | int8 | 64 |  | √ | 0 | 年(年度申报分支机构专用) |
| 12 | ftaxorgid | 分支机构 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | funifiedsocialcode1 | 分支机构社会统一信用代码（申报表取数用） | varchar | 100 |  | √ | ' ' | 分支机构社会统一信用代码（申报表取数用） |
| 14 | frowno | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 15 | ftaxorgname1 | 分支机构名称（申报表取数用） | varchar | 100 |  | √ | ' ' | 分支机构名称（申报表取数用） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_apportion_summary |  | fid |
| 2 | idx_tccit_apportion_summary |  | forgid,fskssqq,fskssqz |
