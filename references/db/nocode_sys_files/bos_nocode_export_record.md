# 单据列表导出记录-bos_nocode_export_record

## 单据列表导出记录-主表 t_nocode_export_record

- **表名称：** 单据列表导出记录-主表
- **表名：** t_nocode_export_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: 1 :已提交 2 :已完成 3 :已取消 4 :出错 |
| 3 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | furls | 附件路径列表 | text | 0 |  |  | null | 附件路径列表 |
| 8 | fextra | 附加信息 | text | 0 |  |  | null | 附加信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_export_record |  | fid |
| 2 | idx_nc_er_status |  | fstatus |
