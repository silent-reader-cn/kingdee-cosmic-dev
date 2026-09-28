# 附件-rim_attach

## 附件-主表 t_rim_attach

- **表名称：** 附件-主表
- **表名：** t_rim_attach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | ficon_url | 附件图标 | varchar | 200 |  | √ | ' ' | 附件图标 |
| 4 | fattach_no | 附件编号 | varchar | 50 |  | √ | ' ' | 附件编号 |
| 5 | fupdate_time | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fpagesum | 总页码 | int4 | 32 |  | √ | 0 | 总页码 |
| 7 | fattach_name | 附件名称 | varchar | 100 |  | √ | ' ' | 附件名称 |
| 8 | fuser | 采集人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fattach_hash_value | 文件的hash值 | varchar | 100 |  | √ | ' ' | 文件的hash值 |
| 10 | fsnapshot_url | 快照地址 | varchar | 200 |  | √ | ' ' | 快照地址 |
| 11 | fattach_url | 附件url | varchar | 200 |  | √ | ' ' | 附件url |
| 12 | fattach_category | 附件类别 | int8 | 64 |  | √ | 0 | [附件类型基础资料 bdm_attach_type](../bdm_files/bdm_attach_type.md) |
| 13 | frim_user | 外部系统用户 | int8 | 64 |  | √ | 0 | 外部系统用户 |
| 14 | ffile_extension | 文件后缀名 | varchar | 8 |  | √ | ' ' | 文件后缀名 |
| 15 | fattach_type | 文件类型 | varchar | 2 |  | √ | ' ' | 文件类型,枚举: 1 :PDF 2 :图片 3 :影像文件 4 :office 5 :文本 |
| 16 | fsize | 文件大小 | int8 | 64 |  | √ | 0 | 文件大小 |
| 17 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 18 | fpageno | 第几页 | int4 | 32 |  | √ | 0 | 第几页 |
| 19 | fresource | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源 |
| 20 | foriginal_name | 原文件名称 | varchar | 200 |  | √ | ' ' | 原文件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_attach_user |  | fuser,frim_user |
| 2 | pk_rim_attach |  | fid |
| 3 | idx_rim_attach |  | fattach_no |
