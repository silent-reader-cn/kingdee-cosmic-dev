# 引入日志-fah_flex_importlog

## 错误详情-子表 t_fah_flex_import_log_en

- **表名称：** 错误详情-子表
- **表名：** t_fah_flex_import_log_en

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrorinfo | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fah_flex_import_log_en |  | fentryid |
| 2 | idx_fah_flex_import_log_en |  | fid |

---

## 引入日志-主表 t_fah_flex_import_log

- **表名称：** 引入日志-主表
- **表名：** t_fah_flex_import_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 引入状态 | bpchar | 1 |  | √ | ' ' | 引入状态,枚举: 0 :处理中 1 :成功 2 :失败 |
| 3 | ferror | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 4 | ferror_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fdatatypeid | 引入数据 | int8 | 64 |  | √ | 0 | 业财数据映射 fah_valmap_typenew |
| 8 | fsourcetype | 数据结构类型 | varchar | 30 |  | √ | ' ' | 数据结构类型,枚举: fah_valmap_typenew :业财数据映射 fah_valueset_type :数据值集 |
| 9 | fbatchid | 日志编码 | int8 | 64 |  | √ | 0 | 日志编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fah_flex_import_log_1 |  | fbatchid |
| 2 | pk_t_fah_flex_import_log |  | fid |
