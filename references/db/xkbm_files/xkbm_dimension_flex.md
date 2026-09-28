# 预算维度弹性域-xkbm_dimension_flex

## 预算维度弹性域-主表 t_xkbm_dimension_flex

- **表名称：** 预算维度弹性域-主表
- **表名：** t_xkbm_dimension_flex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fflexfield | 弹性域 | int8 | 64 |  | √ | 0 | null 010 |
| 3 | fextend | 拓展信息 | varchar | 200 |  | √ | ' ' | 拓展信息 |
| 4 | fbasedatafield | 基础资料 | int8 | 64 |  | √ | 0 | [主维度组合引用 xkbm_maindimref](../xkbm_files/xkbm_maindimref.md) |
| 5 | fschemeid | 模板样式id | int8 | 64 |  | √ | 0 | 模板样式id |
| 6 | fsampleid | 模板id | varchar | 50 |  | √ | ' ' | 模板id |
| 7 | fsheetid | 表页ID | bpchar | 50 |  | √ | ' ' | 表页ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_dimension_flex |  | fid |
| 2 | idx_t_xkbm_dimension_flex |  | fflexfield |
