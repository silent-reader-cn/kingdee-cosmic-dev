# 从价计征房产税减免明细-tcret_fcs_price_det

## 从价计征房产税减免明细-主表 t_tcret_fcs_price_det

- **表名称：** 从价计征房产税减免明细-主表
- **表名：** t_tcret_fcs_price_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxreducename | 减免项目名称 | varchar | 500 |  | √ | ' ' | 减免项目名称 |
| 3 | fapanage | 属地管理名称 | varchar | 50 |  | √ | ' ' | 属地管理名称 |
| 4 | fdeclaremonth | 申报月份 | varchar | 50 |  | √ | ' ' | 申报月份 |
| 5 | fjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |
| 6 | ftaxrate | 计税比例 | numeric | 23 | 10 | √ | 0.0000000000 | 计税比例 |
| 7 | ftaxratio | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 8 | ftaxlimit | 纳税期限 | varchar | 30 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 9 | ftaxreducecode | 减免性质代码 | varchar | 50 |  | √ | ' ' | 减免性质代码 |
| 10 | fisshowfcsbyprice | 是否展示从价计征房产税 | bpchar | 1 |  | √ | ' ' | 是否展示从价计征房产税 |
| 11 | fbuildingcode | 房产编号 | varchar | 50 |  | √ | ' ' | 房产编号 |
| 12 | famount | 减免税房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税房产原值 |
| 13 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 14 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 16 | frowno | 序号 | int8 | 64 |  | √ | 0 | 序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_fcs_price_det |  | forg,fdeclaremonth |
| 2 | pk_tcret_fcs_price_det |  | fid |
