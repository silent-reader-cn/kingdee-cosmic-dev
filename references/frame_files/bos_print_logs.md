# 打印操作日志-bos_print_logs

## 打印操作日志-主表 t_bas_print_log

- **表名称：** 打印操作日志-主表
- **表名：** t_bas_print_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperationtype | 操作类型 | varchar | 20 |  |  | null | 操作类型,枚举: PrintPreview :打印预览 Print :打印 |
| 3 | fcreatetime | 打印发起日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 打印发起日期 |
| 4 | fcreater | 打印发起人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbizobjid | 业务对象主键 | varchar | 100 |  | √ | ' ' | 业务对象主键 |
| 6 | fformid | 业务实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fbilltype | 单据类型 | int8 | 64 |  |  | null | 单据类型 bos_billtype |
| 8 | ftemplate | 打印模板 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_print_log |  | fformid |
| 2 | t_bas_print_log_pkey |  | fid |
