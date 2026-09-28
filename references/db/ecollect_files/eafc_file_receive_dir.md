# 文件移交接收目录-eafc_file_receive_dir

## 文件移交接收目录-主表 t_eafc_file_receive_dir

- **表名称：** 文件移交接收目录-主表
- **表名：** t_eafc_file_receive_dir

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 3 | year | year | varchar | 4 |  | √ | ' ' |  |
| 4 | farorgid | 归档组织 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 5 | ffiletitle | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 6 | fk_check_result | 四检结果 | varchar | 200 |  | √ | ' ' | 四检结果 |
| 7 | fvolumeid | 所属案卷ID | int8 | 64 |  | √ | 0 | 所属案卷ID |
| 8 | fk_preview_file_id | 预览文件ID | varchar | 200 |  | √ | ' ' | 预览文件ID |
| 9 | fk_rec_file_name | 接收文件名 | varchar | 100 |  | √ | ' ' | 接收文件名 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fwarehousingstatus | 入库状态 | varchar | 2 |  | √ | ' ' | 入库状态,枚举: 1 :未入库 2 :已入库 3 :入库异常 4 :已移除 |
| 12 | fmonth | 月份 | varchar | 2 |  | √ | ' ' | 月份 |
| 13 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 14 | fileid | fileid | int8 | 64 |  | √ | 0 |  |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | ffilenum | ffilenum | int4 | 32 |  | √ | 0 |  |
| 17 | fk_preview_file_size | 预览文件大小 | int8 | 64 |  | √ | 0 | 预览文件大小 |
| 18 | ffileno | 文件编号 | varchar | 256 |  | √ | ' ' | 文件编号 |
| 19 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 20 | freceiveid | 移交接收id | int8 | 64 |  | √ | 0 | 移交接收id |
| 21 | freceivedept | 接收部门 | varchar | 256 |  | √ | ' ' | 接收部门 |
| 22 | fk_preview_file_name | 预览文件名称 | varchar | 200 |  | √ | ' ' | 预览文件名称 |
| 23 | fk_rec_file_size | 接收文件大小 | int8 | 64 |  | √ | 0 | 接收文件大小 |
| 24 | fk_base_bill_id | 基表ID | varchar | 50 |  | √ | ' ' | 基表ID |
| 25 | fk_rec_file_type | 接收文件类型 | varchar | 50 |  | √ | ' ' | 接收文件类型 |
| 26 | fk_preview_file_type | 预览文件类型 | varchar | 50 |  | √ | ' ' | 预览文件类型 |
| 27 | fk_rec_file_id | 接收文件ID | varchar | 200 |  | √ | ' ' | 接收文件ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_file_receive_dir |  | fid |
| 2 | idx_eafc_file_receive_dir_1 |  | freceiveid |
