# PLM初始化详情-plm_init_details

## PLM初始化详情-主表 t_plmsm_init_details

- **表名称：** PLM初始化详情-主表
- **表名：** t_plmsm_init_details

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrors | 错误数 | int4 | 32 |  | √ | 0 | 错误数 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbatchnumber | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftemplateurl | 文件URL | varchar | 500 |  | √ | ' ' | 文件URL |
| 7 | flogid | 任务日志ID | varchar | 50 |  | √ | ' ' | 任务日志ID |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fentityname | 单据名称 | varchar | 50 |  | √ | ' ' | 单据名称 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fuploadstatus | 上传状态 | varchar | 50 |  | √ | ' ' | 上传状态,枚举: 0 :未上传 1 :上传中 2 :上传成功 3 :上传异常 4 :上次失败 |
| 12 | fentityid | 单据标识 | varchar | 50 |  | √ | '0' | 单据标识 |
| 13 | fverifyerrorfile | 校验错误文件 | varchar | 500 |  | √ | ' ' | 校验错误文件 |
| 14 | fverifylogid | 校验任务日志ID | varchar | 50 |  | √ | ' ' | 校验任务日志ID |
| 15 | ftemplatename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 16 | fverifystatus | 校验状态 | varchar | 50 |  | √ | '0' | 校验状态,枚举: 0 :未校验 1 :校验中 2 :校验通过 3 :内容报错 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_details_template |  | ftemplatename |
| 2 | pk_t_plmsm_init_details |  | fid |
