# 供应商分析明细F7-src_supanalydetailf7

## 供应商分析明细F7-多语言表 t_src_supanalydetail_l

- **表名称：** 供应商分析明细F7-多语言表
- **表名：** t_src_supanalydetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 供应商分析明细F7-主表 t_src_supanalydetail

- **表名称：** 供应商分析明细F7-主表
- **表名：** t_src_supanalydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 组件表头ID | int8 | 64 |  | √ | 0 | 组件表头ID |
| 2 | ftxtvalue | 指标内容 | varchar | 510 |  | √ | ' ' | 指标内容 |
| 3 | fvalue | 指标值 | numeric | 23 | 10 | √ | 0 | 指标值 |
| 4 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 5 | fbillid | 供应商分析ID | int8 | 64 |  | √ | 0 | 供应商分析F7 src_supplieranalyf7 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | findexid | 分析指标 | int8 | 64 |  | √ | 0 | 评分指标F7 src_indexf7 |
| 9 | fvaluetype | 指标值类型 | bpchar | 1 |  | √ | '0' | 指标值类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉列表 A :多选下拉列表 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |
| 12 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supanalydetail |  | fentryid |
| 2 | idx_src_supanalydetail_fid |  | fid |
