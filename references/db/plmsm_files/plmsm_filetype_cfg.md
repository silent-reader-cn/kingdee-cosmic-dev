# 可存储文件类型配置-plmsm_filetype_cfg

## 可存储文件类型配置-主表 t_plmsm_filetype_cfg

- **表名称：** 可存储文件类型配置-主表
- **表名：** t_plmsm_filetype_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 文件夹ID | int8 | 64 |  | √ | 0 | 文件夹ID |
| 2 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fpdmmodelid | 业务类型编码 | int8 | 64 |  | √ | 0 | 业务类型编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_filetype_cfg |  | fentryid |
| 2 | idx_plmsm_filetype_cfg |  | fid |
