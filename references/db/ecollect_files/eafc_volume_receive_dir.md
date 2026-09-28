# 案卷移交接收目录-eafc_volume_receive_dir

## 案卷移交接收目录-主表 t_eafc_volume_receive_dir

- **表名称：** 案卷移交接收目录-主表
- **表名：** t_eafc_volume_receive_dir

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | ffilenum | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 4 | year | year | varchar | 4 |  | √ | ' ' |  |
| 5 | farorgid | 归档组织 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 6 | fk_preview_file_size | 预览文件大小 | int8 | 64 |  | √ | 0 | 预览文件大小 |
| 7 | fvolumeid | 案卷ID | int8 | 64 |  | √ | 0 | 案卷ID |
| 8 | fk_preview_file_id | 预览文件ID | varchar | 200 |  | √ | ' ' | 预览文件ID |
| 9 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 10 | freceiveid | 移交接收id | int8 | 64 |  | √ | 0 | 移交接收id |
| 11 | fk_rec_file_name | 接收文件名 | varchar | 100 |  | √ | ' ' | 接收文件名 |
| 12 | fk_preview_file_name | 预览文件名称 | varchar | 200 |  | √ | ' ' | 预览文件名称 |
| 13 | fvolumeno | 案卷号 | varchar | 256 |  | √ | ' ' | 案卷号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fwarehousingstatus | 入库状态 | varchar | 2 |  | √ | ' ' | 入库状态,枚举: 1 :未入库 2 :已入库 3 :入库异常 4 :已移除 |
| 16 | fk_rec_file_size | 接收文件大小 | int8 | 64 |  | √ | 0 | 接收文件大小 |
| 17 | fmonth | 月份 | varchar | 2 |  | √ | ' ' | 月份 |
| 18 | fk_rec_file_type | 接收文件类型 | varchar | 50 |  | √ | ' ' | 接收文件类型 |
| 19 | fk_preview_file_type | 预览文件类型 | varchar | 50 |  | √ | ' ' | 预览文件类型 |
| 20 | fk_rec_file_id | 接收文件ID | varchar | 200 |  | √ | ' ' | 接收文件ID |
| 21 | fclassifyid | 分类 | int8 | 64 |  | √ | 0 | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 22 | fvolumetitle | 案卷题名 | varchar | 200 |  | √ | ' ' | 案卷题名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_volume_receive_dir_1 |  | freceiveid |
| 2 | pk_eafc_volume_receive_dir |  | fid |
