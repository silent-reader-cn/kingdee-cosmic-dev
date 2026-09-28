# 智能排序循环信息-cal_sortloop

## 智能排序循环信息-主表 t_cal_sortloop

- **表名称：** 智能排序循环信息-主表
- **表名：** t_cal_sortloop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flooppath | 循环路径 | varchar | 255 |  | √ | ' ' | 循环路径 |
| 3 | fsortlistid | 排序链ID | int8 | 64 |  | √ | 0 | 排序链ID |
| 4 | flooppath_tag | 循环路径_详情 | text | 0 |  |  | null | 循环路径_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_sortloop_slid |  | fsortlistid |
| 2 | pk_t_cal_sortloop |  | fid |
