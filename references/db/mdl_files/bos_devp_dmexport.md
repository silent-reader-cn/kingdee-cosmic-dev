# 元模型导出-bos_devp_dmexport

## 元模型导出-主表 t_dm_dmexport

- **表名称：** 元模型导出-主表
- **表名：** t_dm_dmexport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 导出时间 | timestamp | 0 |  |  | null | 导出时间 |
| 3 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffilename | 文件名 | varchar | 80 |  | √ | ' ' | 文件名 |
| 5 | fjarcombo | JAR包信息 | varchar | 500 |  | √ | ' ' | JAR包信息,枚举: |
| 6 | fdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 8 | fjarname | jar名称文本 | varchar | 500 |  | √ | ' ' | jar名称文本 |
| 9 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_dmexport |  | fid |
| 2 | ix_dm_dmexport |  | fnumber |

---

## 单据体-子表 t_dm_dmexportentry

- **表名称：** 单据体-子表
- **表名：** t_dm_dmexportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dm_dmexportentry |  | fentryid |
| 2 | ix_dm_dmexportentry |  | fid,fseq |
