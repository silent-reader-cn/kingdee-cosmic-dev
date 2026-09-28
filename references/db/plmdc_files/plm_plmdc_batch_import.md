# 文档库批量导入-plm_plmdc_batch_import

## 文档库批量导入-主表 t_plmdc_batch_import

- **表名称：** 文档库批量导入-主表
- **表名：** t_plmdc_batch_import

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphysicalfileid | 物理文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 5 | fuploadsummary | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | ffolder | 文件夹 | int8 | 64 |  | √ | 0 | [系统文件夹 plm_pdm_folder_hub](../plmsm_files/plm_pdm_folder_hub.md) |
| 7 | fstatus | 上传状态 | varchar | 50 |  | √ | ' ' | 上传状态,枚举: waitting :正在上传 success :上传完成 replace :上传完成 error :上传失败 |
| 8 | fuploadstatus | 状态 | varchar | 50 |  | √ | '0' | 状态,枚举: 0 :待上传 1 :上传成功 2 :上传失败 |
| 9 | fsize | 大小 | varchar | 50 |  | √ | ' ' | 大小 |
| 10 | fuuid | uuid | varchar | 255 |  | √ | ' ' | uuid |
| 11 | fdoctype | 文档模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fisfolder | 是否文件夹 | varchar | 10 |  | √ | ' ' | 是否文件夹 |
| 14 | fdocnumber | 文档编码 | varchar | 80 |  | √ | ' ' | 文档编码 |
| 15 | fpath | 位置 | varchar | 1000 |  | √ | ' ' | 位置 |
| 16 | fhash | HASH值 | varchar | 300 |  | √ | ' ' | HASH值 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 19 | fcontainerid | 上下文 | int8 | 64 |  | √ | 0 | [上下文容器 plm_plmsm_container](../plmsm_files/plm_plmsm_container.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmdc_batch_import |  | fid |
| 2 | idx_plmdc_batch_import |  | fnumber |
