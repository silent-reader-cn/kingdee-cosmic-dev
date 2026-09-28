# 业务数据锁-bd_datalock

## 业务数据锁-主表 t_bd_datalock

- **表名称：** 业务数据锁-主表
- **表名：** t_bd_datalock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperationkey | 操作Key | varchar | 36 |  | √ | ' ' | 操作Key |
| 3 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fentitykey | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fobjectid | 对象ID | varchar | 36 |  | √ | ' ' | 对象ID |
| 7 | fbatchid | 批次ID | varchar | 36 |  | √ | ' ' | 批次ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_db_datalock_001 |  | foperationkey,fentitykey,fobjectid |
| 2 | t_bd_datalock_pkey |  | fid |
