# ocr识别API调用详情-cvp_api_invoke_info

## ocr识别API调用详情-主表 t_cvp_api_invoke_info

- **表名称：** ocr识别API调用详情-主表
- **表名：** t_cvp_api_invoke_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrorcode | 调用返回码(失败类型) | varchar | 50 |  | √ | ' ' | 调用返回码(失败类型) |
| 3 | ftraceid | 苍穹日志ID | varchar | 50 |  | √ | ' ' | 苍穹日志ID |
| 4 | fresultinfo | 识别结果 | text | 0 |  |  | ' ' | 识别结果 |
| 5 | ftemplateid | 模板/服务ID | int8 | 64 |  | √ | 0 | 模板/服务ID |
| 6 | fcallobjectname | 业务对象名称 | varchar | 50 |  | √ | ' ' | 业务对象名称 |
| 7 | fuserid | 用户ID | varchar | 50 |  | √ | ' ' | 用户ID |
| 8 | fcallobjectid | 业务对象标识 | varchar | 50 |  | √ | ' ' | 业务对象标识 |
| 9 | fusername | 用户名称 | varchar | 50 |  | √ | ' ' | 用户名称 |
| 10 | fstatus | 调用方式 | bpchar | 1 |  | √ | 'A' | 调用方式,枚举: A :操作类型-图像识别 B :微服务-图像识别 C :开放平台-图像识别 D :操作类型-文档差异 E :微服务-文档差异 F :开放平台-文档差异 G :操作类型-文档信息提取 H :微服务-文档信息提取 I :开放平台-文档信息提取 J :操作类型-组合识别器 K :微服务-组合识别器 L :开放平台-组合识别器 M :操作类型-复杂文档提取 N :微服务-复杂文档提取 O :开放平台-复杂文档提取 |
| 11 | fcreatedate | 调用日期 | timestamp | 0 |  |  | null | 调用日期 |
| 12 | fcalltime | 耗时(毫秒) | int8 | 64 |  | √ | 0 | 耗时(毫秒) |
| 13 | ftemplatename | 模板/服务名称 | varchar | 50 |  | √ | ' ' | 模板/服务名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_api_invoke_info |  | fid |
| 2 | idx_t_cvp_api_invoke_info |  | ftemplatename,ferrorcode,fcallobjectid |
