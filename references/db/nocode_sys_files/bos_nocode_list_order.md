# 表头排序配置-bos_nocode_list_order

## 表头排序配置-主表 t_nocode_list_order

- **表名称：** 表头排序配置-主表
- **表名：** t_nocode_list_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forderinfo | 排序信息 | text | 0 |  |  | null | 排序信息 |
| 3 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 4 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 5 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_list_order |  | fid |
| 2 | idx_uk_afu |  | fappid,fformid,fuserid |
