# 修复数据中间表-wf_repairedata

## 修复数据中间表-主表 t_wf_repairedata

- **表名称：** 修复数据中间表-主表
- **表名：** t_wf_repairedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | fobjid | ID | int8 | 64 |  | √ | 0 | ID |
| 4 | fkey | key | varchar | 100 |  | √ | ' ' | key |
| 5 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_repairedata_objid |  | fobjid |
| 2 | pk_t_wf_repairedata |  | fid |
