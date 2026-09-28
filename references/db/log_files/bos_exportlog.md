# 导出结果-bos_exportlog

## 导出结果-主表 t_log_exportlog

- **表名称：** 导出结果-主表
- **表名：** t_log_exportlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | flogs | 日志 | text | 0 |  |  | null | 日志 |
| 6 | fbizobject | 业务对象列表名称 | varchar | 255 |  | √ | ' ' | 业务对象列表名称 |
| 7 | fexpttype | 导出方式 | bpchar | 1 |  | √ | '0' | 导出方式,枚举: 1 :按列表 2 :按导入模板 3 :按导出模板 4 :单据体导出 5 :按单据体导入模板 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fisdeleted | 文件删除状态 | bpchar | 1 |  | √ | '0' | 文件删除状态,枚举: 0 :未删除 1 :已删除 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsourceobj | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fcreatorid | 导出执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ffinishtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | fdownloadurl | 文件地址 | varchar | 255 |  |  | null | 文件地址 |
| 15 | fcomplete | 已完成总数 | int8 | 64 |  | √ | 0 | 已完成总数 |
| 16 | ftotal | 执行总数 | int8 | 64 |  | √ | 0 | 执行总数 |
| 17 | fusetime | fusetime | int8 | 64 |  | √ | 0 |  |
| 18 | fbillno | 日志编码 | varchar | 255 |  | √ | ' ' | 日志编码 |
| 19 | fexportstatus | 导出状态 | bpchar | 1 |  | √ | '0' | 导出状态,枚举: 0 :导出中 1 :导出完成 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_log_exportlog_pkey |  | fid |
| 2 | idx_log_exportlog_billno |  | fbillno |
