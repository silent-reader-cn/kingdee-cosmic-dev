# 元模型导入-bos_devp_dmimport

## 元模型导入-主表 t_dm_dmimport

- **表名称：** 元模型导入-主表
- **表名：** t_dm_dmimport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | ffilename | 文件名 | varchar | 50 |  | √ | ' ' | 文件名 |
| 6 | fdesc | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 7 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_dmimport |  | fid |
| 2 | idx_t_dm_dmimport |  | fbillno |

---

## 单据体-子表 t_dm_dmimportentry

- **表名称：** 单据体-子表
- **表名：** t_dm_dmimportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 4 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 5 | ffilename | 文件名 | varchar | 500 |  | √ | ' ' | 文件名 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dm_dmimportentry |  | fentryid |
| 2 | idx_t_dm_dmimportentry |  | fid,fseq |
