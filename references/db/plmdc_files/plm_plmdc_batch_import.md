# 文档库批量导入-plm_plmdc_batch_import

## 文档库批量导入-主表 t_plmdc_batch_import

- **表名称：** 文档库批量导入-主表
- **表名：** t_plmdc_batch_import

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fuploadstatus | 状态 | varchar | 50 |  | √ | '0' | 状态,枚举: 0 :待上传 1 :上传成功 2 :上传失败 |
| 4 | fsize | 大小 | varchar | 50 |  | √ | ' ' | 大小 |
| 5 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 6 | fdoctype | 文档模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fisfolder | 是否文件夹 | varchar | 10 |  | √ | ' ' | 是否文件夹 |
| 9 | fuploadsummary | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fpath | 位置 | varchar | 1000 |  | √ | ' ' | 位置 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | ffolder | 文件夹 | int8 | 64 |  | √ | 0 | 系统文件夹 plm_pdm_folder_hub |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmdc_batch_import |  | fid |
| 2 | idx_plmdc_batch_import |  | fnumber |
