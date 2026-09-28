# 上机操作日志v3归档-bos_log_archive_v3

## 上机操作日志v3归档-主表 t_log_app_archive_v3

- **表名称：** 上机操作日志v3归档-主表
- **表名：** t_log_app_archive_v3

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbizobjname | 操作对象名 | varchar | 50 |  | √ | ' ' | 操作对象名 |
| 3 | forgid | 操作组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fopprojid | 操作工程ID | varchar | 50 |  | √ | ' ' | 操作工程ID |
| 5 | fclienttype | 客户端类型 | varchar | 30 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 |
| 6 | farchivetime | 归档时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 归档时间 |
| 7 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fext8 | fext8 | varchar | 255 |  | √ | ' ' |  |
| 9 | fusername | 操作用户名 | varchar | 50 |  | √ | ' ' | 操作用户名 |
| 10 | fopname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 11 | fstatus | 操作结果 | bpchar | 1 |  | √ | '1' | 操作结果,枚举: 0 :失败 1 :成功 |
| 12 | fext7 | fext7 | varchar | 255 |  | √ | ' ' |  |
| 13 | foptime | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 14 | fopdescprojid | 操作描述工程ID | varchar | 50 |  | √ | ' ' | 操作描述工程ID |
| 15 | fopdescresid | 操作描述资源ID | varchar | 50 |  | √ | ' ' | 操作描述资源ID |
| 16 | fext4 | fext4 | varchar | 36 |  | √ | ' ' |  |
| 17 | fext3 | fext3 | int8 | 64 |  | √ | 0 |  |
| 18 | fext6 | fext6 | varchar | 50 |  | √ | ' ' |  |
| 19 | fext5 | fext5 | varchar | 50 |  | √ | ' ' |  |
| 20 | fbizobjid | 操作对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 21 | fext2 | fext2 | varchar | 50 |  | √ | ' ' |  |
| 22 | fext1 | fext1 | varchar | 50 |  | √ | ' ' |  |
| 23 | fopdescargs | 操作描述资源参数 | varchar | 255 |  | √ | ' ' | 操作描述资源参数 |
| 24 | fopdesc | 操作描述 | varchar | 350 |  | √ | ' ' | 操作描述 |
| 25 | fopkey | 操作Key | varchar | 50 |  | √ | ' ' | 操作Key |
| 26 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fkeyword | 业务编码 | varchar | 100 |  | √ | ' ' | 业务编码 |
| 28 | fclientip | 客户端地址 | varchar | 50 |  | √ | ' ' | 客户端地址 |
| 29 | fopresid | 操作资源ID | varchar | 50 |  | √ | ' ' | 操作资源ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_archivev3_keyword |  | fkeyword |
| 2 | pk_log_app_archive_v3 |  | fid |
| 3 | idx_log_archivev3_userid |  | fuserid |
| 4 | idx_log_archivev3_optime |  | foptime |
