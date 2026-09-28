# 签字任务PDF文件管理-plmdc_signaturepdffile

## 签字任务PDF文件管理-主表 t_plmdc_signaturepdffile

- **表名称：** 签字任务PDF文件管理-主表
- **表名：** t_plmdc_signaturepdffile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffilestatus | 文件状态 | varchar | 50 |  | √ | ' ' | 文件状态,枚举: occupy :占用 idle :空闲 |
| 3 | flatestpdffileid | 最新pdf文件 | int8 | 64 |  | √ | 0 | 物理文件属性 plm_plmdc_physical_file |
| 4 | fpdffileid | PDF文件 | int8 | 64 |  | √ | 0 | 物理文件属性 plm_plmdc_physical_file |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_signaturepdffile |  | fid |
| 2 | idx_signature_fpdffileid |  | fpdffileid |
