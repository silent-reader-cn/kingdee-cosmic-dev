# 烟叶税纳税申报表-totf_yys_declare

## 烟叶税纳税申报表-主表 t_totf_yys_declare

- **表名称：** 烟叶税纳税申报表-主表
- **表名：** t_totf_yys_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 4 | fbqybse | 本期应补(退)税额 | numeric | 23 | 10 | √ | 0 | 本期应补(退)税额 |
| 5 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 6 | fyysgjkze | 烟叶收购价款总额 | numeric | 23 | 10 | √ | 0 | 烟叶收购价款总额 |
| 7 | fbqynse | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 8 | fynse | 本期已纳税额 | numeric | 23 | 10 | √ | 0 | 本期已纳税额 |
| 9 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_yys_declare |  | fid |
| 2 | idx_totf_yys_declare |  | fsbbid,fewblxh |
