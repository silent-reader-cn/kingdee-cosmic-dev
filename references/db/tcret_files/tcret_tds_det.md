# 城镇土地使用税减免明细-tcret_tds_det

## 城镇土地使用税减免明细-主表 t_tcret_tds_det

- **表名称：** 城镇土地使用税减免明细-主表
- **表名：** t_tcret_tds_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapanage | 属地管理名称 | varchar | 50 |  | √ | ' ' | 属地管理名称 |
| 3 | ftaxreducename | 减免项目名称 | varchar | 500 |  | √ | ' ' | 减免项目名称 |
| 4 | fisshowtds | 是否展示城镇土地使用税 | bpchar | 1 |  | √ | ' ' | 是否展示城镇土地使用税 |
| 5 | fdeclaremonth | 申报月份 | varchar | 50 |  | √ | ' ' | 申报月份 |
| 6 | fjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |
| 7 | ftaxlimit | 纳税期限 | varchar | 30 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 8 | ftaxreducecode | 减免性质代码 | varchar | 50 |  | √ | ' ' | 减免性质代码 |
| 9 | famount | 减免税面积 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税面积 |
| 10 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 11 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | ftaxstandard | 税额标准 | numeric | 23 | 10 | √ | 0.0000000000 | 税额标准 |
| 13 | flandlevel | 土地等级 | varchar | 50 |  | √ | ' ' | 土地等级 |
| 14 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 15 | flandcode | 土地编号 | varchar | 50 |  | √ | ' ' | 土地编号 |
| 16 | frowno | 序号 | int8 | 64 |  | √ | 0 | 序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tds_det |  | fid |
| 2 | idx_tcret_tds_det |  | forg,fdeclaremonth |
