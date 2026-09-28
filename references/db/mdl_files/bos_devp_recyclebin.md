# 系统垃圾回收站-bos_devp_recyclebin

## 系统垃圾回收站-主表 t_meta_recyclebin

- **表名称：** 系统垃圾回收站-主表
- **表名：** t_meta_recyclebin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelnumber | 删除对象编码 | varchar | 100 |  | √ | ' ' | 删除对象编码 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | ftype | 垃圾类型 | varchar | 50 |  | √ | ' ' | 垃圾类型 |
| 5 | foperator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 6 | fdata_tag | 删除数据_详情 | text | 0 |  |  | null | 删除数据_详情 |
| 7 | fdata | 删除数据 | text | 0 |  |  | null | 删除数据 |
| 8 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作 |
| 9 | fdelid | 删除对象id | varchar | 50 |  | √ | ' ' | 删除对象id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_recyclebin_type |  | ftype |
| 2 | t_meta_recyclebin_pkey |  | fid |
