# 初始库预插配置信息-inte_initdata_conf

## 初始库预插配置信息-主表 t_int_initdata_conf

- **表名称：** 初始库预插配置信息-主表
- **表名：** t_int_initdata_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappnumber | 应用标识 | varchar | 32 |  | √ | ' ' | 应用标识 |
| 3 | ffieldname | 字段名 | varchar | 512 |  | √ | ' ' | 字段名 |
| 4 | ftablename | 表名 | varchar | 255 |  | √ | ' ' | 表名 |
| 5 | froutekey | 路由 | varchar | 32 |  | √ | ' ' | 路由 |
| 6 | fproducttype | 产品标识 | varchar | 32 |  | √ | ' ' | 产品标识 |
| 7 | fpkname | 关联主键 | varchar | 32 |  | √ | ' ' | 关联主键 |
| 8 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_initdata_conf |  | fid |
| 2 | idx_t_int_initdata_conf |  | fappnumber |
