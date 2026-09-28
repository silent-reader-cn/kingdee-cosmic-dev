# 业务参数-fa_billparam

## 业务参数-主表 t_fa_billparam

- **表名称：** 业务参数-主表
- **表名：** t_fa_billparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcanmodify | 可修改 | bpchar | 1 |  | √ | '1' | 可修改 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fparam | 参数 | varchar | 50 |  | √ | ' ' | 参数 |
| 5 | fvalue_tag | 参数值_详情 | text | 0 |  |  | ' ' | 参数值_详情 |
| 6 | fsyspre | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 7 | forgid | 适用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbizcloudid | 业务云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 9 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 10 | fassetbookid | 账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |
| 11 | fbizappid | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fparamtypeid | 参数 | int8 | 64 |  | √ | 0 | [业务参数类型 fa_billparam_type](../fibd_files/fa_billparam_type.md) |
| 13 | fvalue | 参数值 | varchar | 200 |  | √ | ' ' | 参数值 |
| 14 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 18 | fentityid | 适用单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 19 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_billparam_entity |  | fentityid,fparam |
| 2 | idx_fa_billparam_org |  | forgid,fparam |
| 3 | pk_t_fa_billparam |  | fid |
| 4 | idx_fa_billparam_cloud |  | fbizcloudid,fbizappid,fparam |
