# 差异余额结转明细表-cal_purpricediff_detail

## 差异余额结转明细表-主表 t_cal_purdiff_detail

- **表名称：** 差异余额结转明细表-主表
- **表名：** t_cal_purdiff_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入成本差异 |
| 3 | fbalid | 标准差异余额表id | int8 | 64 |  | √ | 0 | 标准差异余额表id |
| 4 | fperiodissuecostdiff | 本期发出成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出成本差异 |
| 5 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期初成本差异 |
| 6 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 7 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期末成本差异 |
| 8 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_purdiff_detail |  | fid |
| 2 | idx_cal_diffbaldet_balid |  | fbalid |
