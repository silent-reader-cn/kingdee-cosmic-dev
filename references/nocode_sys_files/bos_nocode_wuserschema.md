# 工作台视图和用户关系表-bos_nocode_wuserschema

## 工作台视图和用户关系表-主表 t_nocode_wuserschema

- **表名称：** 工作台视图和用户关系表-主表
- **表名：** t_nocode_wuserschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | findex | findex | int8 | 64 |  | √ | 0 |  |
| 3 | factive | 是否激活 | bpchar | 1 |  | √ | '0' | 是否激活 |
| 4 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 5 | fschemaid | 视图ID | int8 | 64 |  | √ | 0 | 视图ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_ws_fuserid_new |  | fuserid |
| 2 | pk_nocode_wuserschema |  | fid |
