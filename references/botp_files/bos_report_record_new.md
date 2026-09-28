# 报告记录-bos_report_record_new

## 报告记录-主表 t_bos_report_record

- **表名称：** 报告记录-主表
- **表名：** t_bos_report_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 36 |  | √ | ' ' | 状态,枚举: A :生成本地文件中 B :txt生成完毕 C :已上传txt D :生成报告中 S :生成成功 F :失败 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | funiquekey | 唯一标识 | varchar | 200 |  | √ | ' ' | 唯一标识 |
| 5 | fmoudlekey | 模块key | varchar | 100 |  | √ | ' ' | 模块key |
| 6 | furl | 文件地址 | varchar | 500 |  |  | null | 文件地址 |
| 7 | furltemp | 临时文件地址 | varchar | 500 |  |  | null | 临时文件地址 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bos_report_record |  | fid |
| 2 | idx_bos_report_record_mu |  | fmoudlekey,funiquekey |
