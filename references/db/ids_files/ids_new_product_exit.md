# 退出新品表-ids_new_product_exit

## 退出新品表-主表 t_ids_new_product_exit

- **表名称：** 退出新品表-主表
- **表名：** t_ids_new_product_exit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 退出状态 | varchar | 50 |  | √ | ' ' | 退出状态,枚举: exit :已退出 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fnewproductcode | 新品标识码 | varchar | 255 |  | √ | ' ' | 新品标识码 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_new_product_exit |  | fid |
| 2 | idx_ids_newproductcode_eixt |  | fnewproductcode |
