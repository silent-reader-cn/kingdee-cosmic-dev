# 从租计征房产税减免信息-tcret_housetax_h_info

## 从租计征房产税减免信息-主表 t_tcret_housetax_h_info

- **表名称：** 从租计征房产税减免信息-主表
- **表名：** t_tcret_housetax_h_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrentreducerent | 本期享受减免税租金收入 | numeric | 23 | 10 | √ | 0.0000000000 | 本期享受减免税租金收入 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 all :合计 4 :4 5 :5 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 6 | fbuildingnumber | 房产编号 | varchar | 100 |  | √ | ' ' | 房产编号 |
| 7 | ftaxreducecode | 减免性质代码 | varchar | 100 |  | √ | ' ' | 减免性质代码 |
| 8 | ftaxreduceproject | 减免项目名称 | varchar | 100 |  | √ | ' ' | 减免项目名称 |
| 9 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 10 | fcurrenttaxreduceamount | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_housetax_h_info_1 |  | fewblxh,fsbbid |
| 2 | t_tcret_housetax_h_info_pkey |  | fid |
| 3 | idx_tcret_housetax_h_info |  | fsbbid |
