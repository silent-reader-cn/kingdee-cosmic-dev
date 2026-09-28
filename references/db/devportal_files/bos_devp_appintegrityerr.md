# 应用完整性错误信息-bos_devp_appintegrityerr

## 应用完整性错误信息-主表 t_meta_appintegrityerror

- **表名称：** 应用完整性错误信息-主表
- **表名：** t_meta_appintegrityerror

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fautofixnum | 自动修复个数 | int8 | 64 |  | √ | 0 | 自动修复个数 |
| 3 | fappname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 4 | fautoerrornum | 自动修复错误个数 | int8 | 64 |  | √ | 0 | 自动修复错误个数 |
| 5 | fmanualfixnum | 手动修复个数 | int8 | 64 |  | √ | 0 | 手动修复个数 |
| 6 | fchecktime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 7 | fappid | 应用id | varchar | 36 |  | √ | ' ' | 应用id |
| 8 | fmanualerrornum | 手动修复错误个数 | int8 | 64 |  | √ | 0 | 手动修复错误个数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_appintegrityerror_pkey |  | fid |
| 2 | idx_kdp_apperrorinfo_app |  | fappid |
