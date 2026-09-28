# 进度条数据-ocdbd_progressrecord

## 进度条数据-主表 t_ocdbd_progressrecord

- **表名称：** 进度条数据-主表
- **表名：** t_ocdbd_progressrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :准备开始执行 B :执行中 C :执行完成 |
| 5 | ferrormsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fprogressbarname | 进度条名称 | varchar | 50 |  | √ | ' ' | 进度条名称 |
| 8 | ftotalcount | 总数 | int4 | 32 |  | √ | 0 | 总数 |
| 9 | fcompletecount | 已执行的数量 | int4 | 32 |  | √ | 0 | 已执行的数量 |
| 10 | fsrcentity | 来源单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_progressrecord |  | fid |
| 2 | idx_ocdbd_progressrc |  | ftraceid |
