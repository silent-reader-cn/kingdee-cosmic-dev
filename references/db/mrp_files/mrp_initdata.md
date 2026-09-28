# MRP初始化-mrp_initdata

## MRP初始化-主表 t_mrp_initdata

- **表名称：** MRP初始化-主表
- **表名：** t_mrp_initdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 初始化人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | finittext | 初始化内容 | varchar | 512 |  | √ | ' ' | 初始化内容 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | finittype | 初始化项 | varchar | 100 |  | √ | ' ' | 初始化项 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | finitstatus | 初始化状态 | varchar | 10 |  | √ | ' ' | 初始化状态,枚举: 0 :未初始化 1 :已初始化 |
| 9 | fmodifytime | 初始化时间 | timestamp | 0 |  |  | null | 初始化时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_initdata |  | fid |
| 2 | idx_t_mrp_initdata |  | forgid |
