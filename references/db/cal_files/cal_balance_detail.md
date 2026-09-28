# 核算余额结转明细表-cal_balance_detail

## 核算余额结转明细表-主表 t_cal_balance_detail

- **表名称：** 核算余额结转明细表-主表
- **表名：** t_cal_balance_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 余额表id | int8 | 64 |  | √ | 0 | 余额表id |
| 2 | fyearissuestandradcost | 本年累计发出标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出标准成本 |
| 3 | fyearissuecostdiff | 本年累计发出成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出成本差异 |
| 4 | fperiodissuecostdiff | 本期发出成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出成本差异 |
| 5 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 6 | fperiodissuestandardcost | 本期发出标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出标准成本 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | fyearinactualcost | 本年累计收入实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入实际成本 |
| 9 | fyearissueactualcost | 本年累计发出实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出实际成本 |
| 10 | fbalid_bak | fbalid_bak | int8 | 64 |  | √ | 0 |  |
| 11 | fperiodendactualcost | 期末实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期末实际成本 |
| 12 | fyearincostdiff | 本年累计收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入成本差异 |
| 13 | fperiodbeginactualcost | 期初实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期初实际成本 |
| 14 | fperiodissueactualcost | 本期发出实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出实际成本 |
| 15 | fid_bak | fid_bak | int8 | 64 |  | √ | 0 |  |
| 16 | fbeginstandardcost | 期初标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期初标准成本 |
| 17 | fperiodendstandardcost | 期末标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期末标准成本 |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | fyearinqty | 本年累计收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入数量 |
| 20 | fyearinstandradcost | 本年累计收入标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入标准成本 |
| 21 | fbalid | fbalid | int8 | 64 |  | √ | 0 |  |
| 22 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期初成本差异 |
| 23 | fperiodissueqty | 本期发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出数量 |
| 24 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 25 | fperiodinqty | 本期收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入数量 |
| 26 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入成本差异 |
| 27 | fperiodendqty | 期末结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期末结存数量 |
| 28 | fyearissueqty | 本年累计发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出数量 |
| 29 | fperiodinactualcost | 本期收入实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入实际成本 |
| 30 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期末成本差异 |
| 31 | fperiodbeginqty | 期初结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初结存数量 |
| 32 | fperiodinstandardcost | 本期收入标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_baldetail_fid |  | fid |
| 2 | pk_cal_balance_detail |  | fdetailid |
