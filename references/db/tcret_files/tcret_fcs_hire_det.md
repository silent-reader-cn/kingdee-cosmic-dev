# 从租计征房产税减免税额明细-tcret_fcs_hire_det

## 从租计征房产税减免税额明细-主表 t_tcret_fcs_hire_det

- **表名称：** 从租计征房产税减免税额明细-主表
- **表名：** t_tcret_fcs_hire_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxreducename | 减免项目名称 | varchar | 500 |  | √ | ' ' | 减免项目名称 |
| 3 | fapanage | 属地管理名称 | varchar | 50 |  | √ | ' ' | 属地管理名称 |
| 4 | fdeclaremonth | 申报月份 | varchar | 50 |  | √ | ' ' | 申报月份 |
| 5 | fjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |
| 6 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 7 | ftaxlimit | 纳税期限 | varchar | 30 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 8 | ftaxreducecode | 减免性质代码 | varchar | 50 |  | √ | ' ' | 减免性质代码 |
| 9 | fbuildingcode | 房产编号 | varchar | 50 |  | √ | ' ' | 房产编号 |
| 10 | fcurrental | 本期申报租金收入 | numeric | 23 | 10 | √ | 0.0000000000 | 本期申报租金收入 |
| 11 | famount | 税额原值 | numeric | 23 | 10 | √ | 0.0000000000 | 税额原值 |
| 12 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fisshowfcsbyhire | 是否展示从租计征房产税 | bpchar | 1 |  | √ | ' ' | 是否展示从租计征房产税 |
| 14 | frowno | 序号 | int8 | 64 |  | √ | 0 | 序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_fcs_hire_det |  | fdeclaremonth,forg |
| 2 | pk_tcret_fcs_hire_det |  | fid |
