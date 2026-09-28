# 组织间结算网控互斥-ism_settlenetrecord

## 组织间结算网控互斥-主表 t_ism_settlenetrecord

- **表名称：** 组织间结算网控互斥-主表
- **表名：** t_ism_settlenetrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 3 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fsessionid | 线程ID | varchar | 100 |  | √ | ' ' | 线程ID |
| 5 | fctrltype | 控制类型 | varchar | 30 |  | √ | ' ' | 控制类型,枚举: createsettle :创建结算清单 |
| 6 | fentitykey | 操作业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 7 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbizbillno | 业务单据编号 | varchar | 100 |  | √ | ' ' | 业务单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settlenetrecord |  | fid |
| 2 | idx_ism_settlenetrecord |  | fbizbillid |
