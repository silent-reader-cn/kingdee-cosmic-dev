# 环保税排污许可证-tctb_hjbhs_entry

## 环保税排污许可证-主表 t_tctb_hjbhs_entry

- **表名称：** 环保税排污许可证-主表
- **表名：** t_tctb_hjbhs_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 3 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | fcshygc | 从事海洋工程 | bpchar | 1 |  | √ | '0' | 从事海洋工程 |
| 5 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 6 | fpollutanttype | 污染物类别 | varchar | 100 |  | √ | ' ' | 污染物类别 |
| 7 | fshljjzclcs | 生活垃圾集中处理场所 | bpchar | 1 |  | √ | '0' | 生活垃圾集中处理场所 |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fcxwsjzclcs | 城乡污水集中处理场所 | bpchar | 1 |  | √ | '0' | 城乡污水集中处理场所 |
| 10 | fnumber | 编号 | varchar | 200 |  | √ | ' ' | 编号 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | facsb | 按次申报 | bpchar | 1 |  | √ | '0' | 按次申报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_hjbhs_entry_fk |  | fid |
| 2 | pk_tctb_hjbhs_entry |  | fentryid |
