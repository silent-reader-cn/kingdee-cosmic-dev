# 系统参数-bos_svc_sysparameter

## 系统参数-主表 t_bas_sysparameter

- **表名称：** 系统参数-主表
- **表名：** t_bas_sysparameter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubsystem | FSUBSYSTEM | varchar | 50 |  | √ | '0' | FSUBSYSTEM |
| 2 | fid | FID | varchar | 36 |  | √ | '0' | FID |
| 3 | facctbookid | FACCTBOOKID | int8 | 64 |  | √ | 0 | FACCTBOOKID |
| 4 | flockfields | FLOCKFIELDS | text | 0 |  |  | null | FLOCKFIELDS |
| 5 | facctingbookid | FACCTINGBOOKID | int8 | 64 |  | √ | 0 | FACCTINGBOOKID |
| 6 | fparamconfig | FPARAMCONFIG | text | 0 |  |  | null | FPARAMCONFIG |
| 7 | forgid | FORGID | int8 | 64 |  | √ | 0 | FORGID |
| 8 | fviewtypeid | FVIEWTYPEID | varchar | 20 |  | √ | ' ' | FVIEWTYPEID |
| 9 | fdata | FDATA | text | 0 |  |  | null | FDATA |
| 10 | fparamid | FPARAMID | varchar | 36 |  | √ | '0' | FPARAMID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_sysparam_fparamid |  | fparamid,forgid,fviewtypeid |
| 2 | idx_sysparam_facctingbookid |  | facctingbookid |
| 3 | t_bas_sysparameter_pkey |  | fid |
