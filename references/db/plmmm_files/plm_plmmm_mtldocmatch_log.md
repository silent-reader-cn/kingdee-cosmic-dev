# 物料文档自动匹配日志-plm_plmmm_mtldocmatch_log

## 物料文档自动匹配日志-主表 t_plm_mtldocmatch_log

- **表名称：** 物料文档自动匹配日志-主表
- **表名：** t_plm_mtldocmatch_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdocversiondetails | 文档版本 | varchar | 50 |  | √ | ' ' | 文档版本 |
| 3 | fmaterialid | 物料版本id | int8 | 64 |  | √ | 0 | 物料版本id |
| 4 | fpolicyname | 策略名称 | varchar | 50 |  | √ | ' ' | 策略名称 |
| 5 | fmatchtime | 匹配时间 | varchar | 50 |  | √ | ' ' | 匹配时间 |
| 6 | fdocname | 文档名称 | varchar | 50 |  | √ | ' ' | 文档名称 |
| 7 | fmaterialverisondetails | 物料版本 | varchar | 50 |  | √ | ' ' | 物料版本 |
| 8 | fdocid | 文档版本id | int8 | 64 |  | √ | 0 | 文档版本id |
| 9 | fscenename | 场景名称 | varchar | 50 |  | √ | ' ' | 场景名称 |
| 10 | fmatchingcreator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 11 | fdocnumber | 文档编码 | varchar | 50 |  | √ | ' ' | 文档编码 |
| 12 | frulename | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 13 | fmaterialnumber | 物料编码 | varchar | 50 |  | √ | ' ' | 物料编码 |
| 14 | fmaterialname | 物料名称 | varchar | 50 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_mtldocmatch_log |  | fmaterialnumber,fdocnumber |
| 2 | pk_t_plm_mtldocmatch_log |  | fid |
