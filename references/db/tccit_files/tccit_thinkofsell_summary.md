# 视同销售单据列表-tccit_thinkofsell_summary

## 视同销售单据列表-主表 t_tccit_thinkofsell_sum

- **表名称：** 视同销售单据列表-主表
- **表名：** t_tccit_thinkofsell_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行次 count :合计 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | fincome | 视同销售收入 | numeric | 23 | 10 | √ | 0.0000000000 | 视同销售收入 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fproducttype | 自产/外购 | varchar | 30 |  | √ | ' ' | 自产/外购,枚举: self :自产 out :外购 |
| 9 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 10 | fadjustamount | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 11 | fitemtype | 视同销售类型 | varchar | 50 |  | √ | ' ' | 视同销售类型,枚举: 50101 :市场推广或销售 50102 :交际应酬 50103 :职工奖励或福利 50104 :股息分配 50105 :对外捐赠 50106 :对外投资项目 50107 :提供劳务 50108 :非货币性资产交换 50109 :其他 |
| 12 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 15 | fcost | 视同销售成本 | numeric | 23 | 10 | √ | 0.0000000000 | 视同销售成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_thinkofsell_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_thinkofsell_sum |  | fid |
