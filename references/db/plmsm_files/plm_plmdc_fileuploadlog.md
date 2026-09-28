# 图纸初始化上传结果信息-plm_plmdc_fileuploadlog

## 图纸初始化上传结果信息-主表 t_plmdc_fileuploadlog

- **表名称：** 图纸初始化上传结果信息-主表
- **表名：** t_plmdc_fileuploadlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphysicalfileid | 物理文件id | varchar | 50 |  | √ | ' ' | 物理文件id |
| 3 | fuploadstatus | 上传状态 | varchar | 50 |  | √ | ' ' | 上传状态 |
| 4 | ffilename | 文件名称 | varchar | 500 |  | √ | ' ' | 文件名称 |
| 5 | fserialno | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 6 | ferrormessage | 错误信息 | varchar | 500 |  | √ | ' ' | 错误信息 |
| 7 | fdata_tag | 装配结构信息_详情 | text | 0 |  |  | null | 装配结构信息_详情 |
| 8 | fdata | 装配结构信息 | varchar | 255 |  | √ | ' ' | 装配结构信息 |
| 9 | ftaskid | 任务号 | varchar | 50 |  | √ | ' ' | 任务号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_fileuploadlog |  | fid |
| 2 | idx_plmdc_fileuploadlog_taskid |  | ftaskid |
