# 用户行为-bos_nocode_userlog

## 用户行为-主表 t_nocode_userlog

- **表名称：** 用户行为-主表
- **表名：** t_nocode_userlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 4 | fextrainfo | 附加信息 | text | 0 |  |  | null | 附加信息 |
| 5 | fsource | 事件源 | varchar | 50 |  | √ | ' ' | 事件源,枚举: app :应用 |
| 6 | feventtype | 事件类型 | varchar | 50 |  | √ | ' ' | 事件类型,枚举: click :点击 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_nocode_userlog |  | fid |
| 2 | idx_nc_ul_ues |  | fuserid,feventtype,fsource |
