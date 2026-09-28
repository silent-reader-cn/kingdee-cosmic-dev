# 对账明细表-ai_rec_data_detail

## 对账明细表-主表 t_ai_rec_detail

- **表名称：** 对账明细表-主表
- **表名：** t_ai_rec_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctnum | 科目 | varchar | 40 |  | √ | ' ' | 科目 |
| 3 | fglamt | 凭证金额 | numeric | 23 | 10 | √ | 0.0000000000 | 凭证金额 |
| 4 | fdc | 借贷方向 | int8 | 64 |  | √ | 0 | 借贷方向,枚举: 2 :借 3 :贷 |
| 5 | fdiff | 差异 | numeric | 23 | 10 | √ | 0.0000000000 | 差异 |
| 6 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fvchid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 8 | fbizamt | 单据金额 | numeric | 23 | 10 | √ | 0.0000000000 | 单据金额 |
| 9 | fvchno | 凭证号 | varchar | 100 |  | √ | ' ' | 凭证号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_rec_detail |  | fvchid |
| 2 | t_ai_rec_detail_pkey |  | fid |

---

## 单据体-子表 t_ai_rec_detailentry

- **表名称：** 单据体-子表
- **表名：** t_ai_rec_detailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 3 | fbillassist | 业务维度 | varchar | 200 |  | √ | ' ' | 业务维度 |
| 4 | fbizdc | 借贷方向 | bpchar | 1 |  | √ | '2' | 借贷方向,枚举: 2 :借 3 :贷 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbillorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务组织 |
| 7 | fbillentity | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbillamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 10 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_rec_detailentry_pkey |  | fentryid |
| 2 | idx_ai_rec_detailentry |  | fid |
