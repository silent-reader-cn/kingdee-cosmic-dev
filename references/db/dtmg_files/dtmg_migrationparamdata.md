# 数据迁移参数过程-dtmg_migrationparamdata

## 数据迁移参数过程-主表 t_dtmg_migparam

- **表名称：** 数据迁移参数过程-主表
- **表名：** t_dtmg_migparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamvalue | 参数值 | varchar | 255 |  | √ | ' ' | 参数值 |
| 3 | fparamkey | 参数Key | varchar | 50 |  | √ | ' ' | 参数Key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dtmg_mig_paramkey |  | fparamkey |
| 2 | pk_dtmg_migparam |  | fid |
