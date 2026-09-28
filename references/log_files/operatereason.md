# 操作原因-operatereason

## 操作原因-主表 t_sys_opreason

- **表名称：** 操作原因-主表
- **表名：** t_sys_opreason

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 操作名称 | varchar | 30 |  | √ | ' ' | 操作名称 |
| 3 | fuser | 操作用户 | varchar | 255 |  | √ | ' ' | 操作用户 |
| 4 | freid | 主键编号 | int8 | 64 |  | √ | 0 | 主键编号 |
| 5 | foperatetime | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 6 | freason |  | varchar | 1024 |  |  | null |  |
| 7 | fdescription | 操作描述 | varchar | 512 |  |  | null | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sys_opreason |  | fid |
| 2 | idx_sys_opreason_freid |  | freid |
