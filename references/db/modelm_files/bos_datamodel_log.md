# 数据模型操作日志-bos_datamodel_log

## 数据模型操作日志-主表 t_dm_pdmmodelversion

- **表名称：** 数据模型操作日志-主表
- **表名：** t_dm_pdmmodelversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperator | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodelid | 模型ID | varchar | 100 |  | √ | ' ' | 模型ID |
| 4 | fmodelnumber | 模型编码 | varchar | 30 |  | √ | ' ' | 模型编码 |
| 5 | fdata_tag | 模型内容_详情 | text | 0 |  |  | null | 模型内容_详情 |
| 6 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fcommit | Git提交 | bpchar | 1 |  | √ | '0' | Git提交 |
| 8 | fisv | 开发商标识 | varchar | 8 |  | √ | ' ' | 开发商标识 |
| 9 | fsubmit | 提交人 | varchar | 100 |  | √ | ' ' | 提交人 |
| 10 | fdescription | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 11 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fdata | 模型内容 | varchar | 255 |  | √ | ' ' | 模型内容 |
| 13 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dm_pdmmodelver_modelid |  | fmodelid,fversion |
| 2 | pk_t_dm_pdmmodelversion |  | fid |
