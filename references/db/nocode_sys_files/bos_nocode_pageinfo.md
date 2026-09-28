# 表单列表分页信息-bos_nocode_pageinfo

## 表单列表分页信息-主表 t_nocode_pageinfo

- **表名称：** 表单列表分页信息-主表
- **表名：** t_nocode_pageinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 3 | fpagesize | 每页显示个数 | int8 | 64 |  | √ | 0 | 每页显示个数 |
| 4 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 5 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_pageinfo |  | fid |
| 2 | idx_nc_pi_afu |  | fappid,fformid,fuserid |
