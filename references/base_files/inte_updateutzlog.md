# 修改人员用户时区日志-inte_updateutzlog

## 修改人员用户时区日志-主表 t_int_updateutzlog

- **表名称：** 修改人员用户时区日志-主表
- **表名：** t_int_updateutzlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcaller | 调用方 | varchar | 512 |  | √ | ' ' | 调用方 |
| 3 | foperator | 操作人 | int8 | 64 |  | √ | 0 | 操作人 |
| 4 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fuserid | 人员ID | int8 | 64 |  | √ | 0 | 人员ID |
| 6 | fcurrtimezone | 修改后时区 | varchar | 64 |  | √ | ' ' | 修改后时区 |
| 7 | fpretimezone | 修改前时区 | varchar | 64 |  | √ | ' ' | 修改前时区 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_udpateutz |  | fuserid |
| 2 | pk_t_int_updateutzlog |  | fid |
