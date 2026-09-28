# 轻扩展元数据-bos_bizextmeta

## 轻扩展元数据-主表 t_meta_bizobj_ext

- **表名称：** 轻扩展元数据-主表
- **表名：** t_meta_bizobj_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fentitydata_tag | 扩展实体元数据_详情 | text | 0 |  |  | null | 扩展实体元数据_详情 |
| 4 | fparentid | 父对象id | varchar | 36 |  | √ | ' ' | 父对象id |
| 5 | fmodeltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 6 | fispublished | 已发布 | varchar | 5 |  |  | '0' | 已发布 |
| 7 | fbizcloudid | 所属云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fformdata_tag | 扩展表单元数据_详情 | text | 0 |  |  | null | 扩展表单元数据_详情 |
| 10 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fstatus | 状态 | varchar | 5 |  | √ | '0' | 状态,枚举: 0 :未测试 1 :已测试 2 :已发布 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fentitydata | 扩展实体元数据 | varchar | 255 |  | √ | ' ' | 扩展实体元数据 |
| 14 | fmasterid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fformdata | 扩展表单元数据 | varchar | 255 |  | √ | ' ' | 扩展表单元数据 |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_meta_bizobj_ext |  | fid |
| 2 | idx_meta_bizobj_ext |  | fnumber |
