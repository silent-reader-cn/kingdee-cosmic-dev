# 出库核算&#x2f;关账&#x2f;结账（方案）-cal_query_scheme_autoop

## 出库核算&#x2f;关账&#x2f;结账（方案）-主表 t_cal_query_scheme_autoop

- **表名称：** 出库核算&#x2f;关账&#x2f;结账（方案）-主表
- **表名：** t_cal_query_scheme_autoop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fqueryschemeid | 查询方案 | int8 | 64 |  | √ | 0 | 查询方案 cal_query_scheme |
| 4 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_scheme_autoop_scid |  | fqueryschemeid |
| 2 | pk_t_cal_query_scheme_autoop |  | fid |
