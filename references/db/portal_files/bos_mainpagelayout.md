# 首页布局（即将废弃）-bos_mainpagelayout

## 首页布局（即将废弃）-主表 t_bas_mainpagelayout

- **表名称：** 首页布局（即将废弃）-主表
- **表名：** t_bas_mainpagelayout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | flayout | 布局信息 | text | 0 |  |  | null | 布局信息 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 8 | flayout_tag | flayout_tag | text | 0 |  |  | ' ' |  |
| 9 | fformnum | fformnum | varchar | 36 |  | √ | ' ' |  |
| 10 | fschemetype | fschemetype | bpchar | 1 |  | √ | '1' |  |
| 11 | fispreset | fispreset | bpchar | 1 |  | √ | '1' |  |
| 12 | fismultiorg | fismultiorg | bpchar | 1 |  | √ | '1' |  |
| 13 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 14 | fcustomable | fcustomable | bpchar | 1 |  | √ | '1' |  |
| 15 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 16 | fdisabletime | fdisabletime | timestamp | 0 |  |  | null |  |
| 17 | ftype | 首页类型 | varchar | 36 |  | √ | ' ' | 首页类型,枚举: main :门户首页 app :应用首页 |
| 18 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 19 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 20 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 21 | fnumber | fnumber | varchar | 100 |  | √ | ' ' |  |
| 22 | fisdef | fisdef | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_mplayout |  | ftype,fbizappid,fenable,fcreatorid,fschemetype |
| 2 | t_bas_mainpagelayout_pkey |  | fid |
| 3 | idx_t_bas_mplayout_fuserid |  | fuserid |
