# 调阅水印记录-eafc_water_call_record

## 单据体-子表 tk_eafc_water_callrec_ent

- **表名称：** 单据体-子表
- **表名：** tk_eafc_water_callrec_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_file_createtime | 文件创建时间 | timestamp | 0 |  |  | null | 文件创建时间 |
| 3 | fk_eafc_filename | 文件名 | varchar | 200 |  | √ | ' ' | 文件名 |
| 4 | fk_eafc_src_fileurl | 源文件地址 | varchar | 500 |  | √ | ' ' | 源文件地址 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 7 | fk_eafc_tar_fileurl | 水印文件地址 | varchar | 500 |  | √ | ' ' | 水印文件地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_water_callrec_ent |  | fentryid |

---

## 调阅水印记录-主表 tk_eafc_water_call_record

- **表名称：** 调阅水印记录-主表
- **表名：** tk_eafc_water_call_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fk_eafc_water_type | 水印类型 | varchar | 50 |  | √ | ' ' | 水印类型 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_eafc_watermark_md5 | 水印方式_MD5 | varchar | 1000 |  | √ | ' ' | 水印方式_MD5 |
| 10 | fk_eafc_watermark_fileurl | 水印文件存储目录 | varchar | 500 |  | √ | ' ' | 水印文件存储目录 |
| 11 | fk_eafc_call_user | 水印人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_eafc_watermark_json | 水印方式_JSON | varchar | 1000 |  | √ | ' ' | 水印方式_JSON |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_water_call_record |  | fid |
