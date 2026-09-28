# 待结算单据信息-ism_settleprocinfo

## 待结算单据信息-主表 t_ism_settleprocinfo

- **表名称：** 待结算单据信息-主表
- **表名：** t_ism_settleprocinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 3 | fmessage | fmessage | varchar | 2000 |  | √ | ' ' |  |
| 4 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fsessionid | 线程ID | varchar | 100 |  | √ | ' ' | 线程ID |
| 6 | fproctype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: A :审核生成内部交易单据 B :调度生成内部交易单据 C :自动结算 |
| 7 | fentitykey | 操作业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprocstatus | 操作状态 | varchar | 50 |  | √ | ' ' | 操作状态,枚举: begin :服务开始处理 wait :等待处理 finish :处理完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settleprocinfo |  | fid |
| 2 | idx_settleprocinfo |  | fcreatetime |
