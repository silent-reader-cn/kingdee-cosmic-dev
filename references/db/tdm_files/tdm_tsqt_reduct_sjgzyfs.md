# 实际工作月份数-tdm_tsqt_reduct_sjgzyfs

## 实际工作月份数-主表 t_tdm_tsqt_reduct_sjgzyfs

- **表名称：** 实际工作月份数-主表
- **表名：** t_tdm_tsqt_reduct_sjgzyfs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 月份 | varchar | 50 |  | √ | ' ' | 月份 |
| 3 | fmonth | fmonth | varchar | 50 |  | √ | ' ' |  |
| 4 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_tsqt_reduct_sjgzyfs |  | fnumber |
| 2 | pk_tdm_tsqt_reduct_sjgzyfs |  | fid |
