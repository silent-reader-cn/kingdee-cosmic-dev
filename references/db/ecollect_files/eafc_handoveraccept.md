# 移交接收-eafc_handoveraccept

## 单据体-子表 t_eafc_handoveraccentry

- **表名称：** 单据体-子表
- **表名：** t_eafc_handoveraccentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceivaestatus | 接收状态 | varchar | 2 |  | √ | ' ' | 接收状态,枚举: A :待解析 B :解析成功 C :解析失败 D :检测异常 |
| 3 | fzipsize | 大小 | varchar | 50 |  | √ | ' ' | 大小 |
| 4 | funiquekey | 唯一标识 | varchar | 50 |  | √ | ' ' | 唯一标识 |
| 5 | fattachmenturl | 附件URL | varchar | 512 |  | √ | ' ' | 附件URL |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fzipname | 压缩包名称 | varchar | 256 |  | √ | ' ' | 压缩包名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fattachmentid | 附件id | int8 | 64 |  | √ | 0 | 附件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_handoveraccentry |  | fentryid |
| 2 | idx_eafc_handoveraccentry_1 |  | fid |

---

## 移交接收-主表 t_eafc_handoveraccept

- **表名称：** 移交接收-主表
- **表名：** t_eafc_handoveraccept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 2 |  | √ | ' ' | 状态,枚举: A :解析检测中 B :接收失败 C :已完成 D :已移除 |
| 3 | ffilediff | 文件差异数 | int4 | 32 |  | √ | 0 | 文件差异数 |
| 4 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fk_check_status | 检测状态 | varchar | 50 |  | √ | ' ' | 检测状态,枚举: 1 :检测通过 2 :检测不通过 |
| 6 | farchivaldiff | 案卷差异数 | int4 | 32 |  | √ | 0 | 案卷差异数 |
| 7 | flot | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 8 | fdesc | 描述 | varchar | 256 |  | √ | ' ' | 描述 |
| 9 | ffileurl | 文件url | varchar | 512 |  | √ | ' ' | 文件url |
| 10 | fsource | 来源 | varchar | 2 |  | √ | ' ' | 来源,枚举: A :手工移交 B :在线移交 |
| 11 | ftaketime | 耗时 | varchar | 50 |  | √ | ' ' | 耗时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_handoveraccept |  | fid |
| 2 | idx_eafc_handoveraccept_1 |  | flot |
