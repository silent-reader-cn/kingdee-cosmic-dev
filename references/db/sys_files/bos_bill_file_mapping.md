# 单据文件映射关系-bos_bill_file_mapping

## 单据文件映射关系-主表 t_bas_bill_file_mapping

- **表名称：** 单据文件映射关系-主表
- **表名：** t_bas_bill_file_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fentitynum | 业务对象 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | ffilelocation | 文件位置 | bpchar | 1 |  | √ | '2' | 文件位置,枚举: 0 :临时文件服务器 1 :文件服务器 |
| 5 | fattpkid | 附件表PKID | int8 | 64 |  | √ | 0 | 附件表PKID |
| 6 | ffieldkey | 字段/控件标识 | varchar | 255 |  | √ | ' ' | 字段/控件标识 |
| 7 | fappid | 应用ID | varchar | 255 |  | √ | ' ' | 应用ID |
| 8 | fbillentrypkid | 单据分录PKID | int8 | 64 |  | √ | 0 | 单据分录PKID |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 10 | fbillpkid | 单据PKID | int8 | 64 |  | √ | 0 | 单据PKID |
| 11 | ffilename | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 12 | ffieldtype | 字段/控件类型 | bpchar | 1 |  | √ | '0' | 字段/控件类型,枚举: 0 :其他 1 :附件面板 2 :附件字段 3 :图片字段 4 :图片控件 5 :图片列表 |
| 13 | fpath | 文件path | varchar | 512 |  | √ | ' ' | 文件path |
| 14 | fsyncdate | 同步时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 同步时间 |
| 15 | fsyncstatus | 同步状态 | bpchar | 1 |  | √ | '3' | 同步状态,枚举: 1 :同步成功 2 :同步失败 3 :同步中 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_bill_file_mapping |  | fid |
| 2 | idx_t_b_bill_file_mapping_app |  | fappid,fentitynum |
| 3 | idx_t_b_bill_file_mapping_pat |  | fpath |
