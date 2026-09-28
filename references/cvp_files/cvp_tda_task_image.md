# 差异分析图片存储-cvp_tda_task_image

## 差异分析图片存储-主表 t_cvp_tda_task_image

- **表名称：** 差异分析图片存储-主表
- **表名：** t_cvp_tda_task_image

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fimageheight | 高 | int4 | 32 |  | √ | 0 | 高 |
| 4 | fpagenum | 页码 | int4 | 32 |  | √ | 0 | 页码 |
| 5 | fsourcefiletype | 文件业务类型 | varchar | 255 |  | √ | ' ' | 文件业务类型 |
| 6 | ftaskid | 任务ID | varchar | 255 |  | √ | ' ' | 任务ID |
| 7 | fimagewidth | 宽 | int4 | 32 |  | √ | 0 | 宽 |
| 8 | fimagepath | 图片存储地址 | varchar | 255 |  | √ | ' ' | 图片存储地址 |
| 9 | fimageid | 差异分析转换文件ID | int8 | 64 |  | √ | 0 | 差异分析转换文件ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_tda_task_image |  | fid |
| 2 | idx_cvp_tda_task_image |  | ftaskid,fsourcefiletype |
