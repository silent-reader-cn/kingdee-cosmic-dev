# 快照日志-mds_fastphotolog

## 单据体-子表 t_mds_fplogentry

- **表名称：** 单据体-子表
- **表名：** t_mds_fplogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fverid | 快照计划版本编码 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 3 | fbkentryid | 快照版本号 | int8 | 64 |  | √ | 0 | 快照版本号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_fplogentry_fid |  | fid |
| 2 | pk_mds_fplogentry |  | fentryid |

---

## 快照日志-多语言表 t_mds_fplog_l

- **表名称：** 快照日志-多语言表
- **表名：** t_mds_fplog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '0' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | '0' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_fplog_l |  | fid,flocaleid |
| 2 | pk_mds_fplog_l |  | fpkid |

---

## 快照日志-主表 t_mds_fplog

- **表名称：** 快照日志-主表
- **表名：** t_mds_fplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrorinfo | 异常信息 | varchar | 1000 |  | √ | ' ' | 异常信息 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fsummin | 计算总时长（秒） | numeric | 23 | 2 | √ | 0 | 计算总时长（秒） |
| 9 | fsyncresult | 快照状态 | varchar | 50 |  | √ | ' ' | 快照状态,枚举: A :成功 B :失败 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fstartdate | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | ffpinfo | 快照信息 | varchar | 50 |  | √ | ' ' | 快照信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_fplog |  | fid |
| 2 | idx_mds_fplog_num |  | fnumber |
