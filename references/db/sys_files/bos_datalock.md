# 网络互斥-bos_datalock

## 网络互斥-主表 t_mutex_datalock

- **表名称：** 网络互斥-主表
- **表名：** t_mutex_datalock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperationkey | 操作Key | varchar | 36 |  |  | null | 操作Key |
| 3 | fgroupid | fgroupid | varchar | 36 |  |  | ' ' |  |
| 4 | ftraceid | traceid | varchar | 50 |  |  | null | traceid |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fsessionid | fsessionid | varchar | 512 |  | √ | ' ' |  |
| 7 | fclienttype | 客户端类型 | varchar | 36 |  |  | null | 客户端类型 |
| 8 | fentitykey | 对象类型 | varchar | 36 |  |  | null | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fobjectid | 对象id | varchar | 100 |  | √ | ' ' | 对象id |
| 10 | fuserid | 执行人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcallsource | 调用来源 | varchar | 50 |  |  | null | 调用来源 |
| 12 | fobjectnumber | 单据对象 | varchar | 100 |  | √ | ' ' | 单据对象 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mutex_datalock_pkey |  | fid |
| 2 | idx_mux_dl_001 |  | fobjectid,fentitykey,foperationkey |
