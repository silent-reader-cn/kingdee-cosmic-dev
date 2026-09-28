# 附件管理-bos_attachment_management

## 附件管理-主表 t_bas_attachment

- **表名称：** 附件管理-主表
- **表名：** t_bas_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemppageid | ftemppageid | varchar | 255 |  |  | null |  |
| 3 | flocalid | flocalid | varchar | 500 |  |  | ' ' |  |
| 4 | fmodifymen | fmodifymen | int8 | 64 |  | √ | 0 |  |
| 5 | faudittime | faudittime | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fsort | fsort | int4 | 32 |  |  | null |  |
| 8 | fcreatemen | fcreatemen | int8 | 64 |  | √ | 0 |  |
| 9 | fbillno | 单据编号 | varchar | 255 |  |  | null | 单据编号 |
| 10 | fentryinterid | fentryinterid | varchar | 50 |  |  | null |  |
| 11 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 12 | fcreatetime | fcreatetime | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 13 | ffilesource | ffilesource | int4 | 32 |  |  | 0 |  |
| 14 | fentrykey | fentrykey | varchar | 50 |  |  | null |  |
| 15 | fdescription | 备注 | varchar | 255 |  |  | null | 备注 |
| 16 | fextname | 文件类型 | varchar | 30 |  |  | null | 文件类型 |
| 17 | fauditmen | fauditmen | int8 | 64 |  | √ | 0 |  |
| 18 | fattachmentpanel | fattachmentpanel | varchar | 80 |  |  | null |  |
| 19 | fdragseq | fdragseq | int8 | 64 |  | √ | 0 |  |
| 20 | ffilestorage | ffilestorage | bpchar | 1 |  | √ | '0' |  |
| 21 | fattachmentsize | fattachmentsize | varchar | 50 |  |  | null |  |
| 22 | ffileid | ffileid | varchar | 500 |  | √ | ' ' |  |
| 23 | faliasfilename | faliasfilename | varchar | 255 |  |  | null |  |
| 24 | fnumber | fnumber | varchar | 50 |  |  | null |  |
| 25 | fattachmentname | fattachmentname | varchar | 255 |  |  | null |  |
| 26 | finterid | finterid | varchar | 50 |  |  | null |  |
| 27 | fbilltype | fbilltype | varchar | 50 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_attachment_pkey |  | fid |
| 2 | idx_bas_attachment_ffileid |  | ffileid |
| 3 | idx_bas_attachment |  | fnumber |
| 4 | idx_bas_attachment_02 |  | fbilltype,finterid |
| 5 | idx_bas_attachment_interid |  | finterid |
