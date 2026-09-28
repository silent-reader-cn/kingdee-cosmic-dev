# 待排表运算日志-mds_dpsrunlog

## 待排表运算日志-主表 t_mds_dpsrunlog

- **表名称：** 待排表运算日志-主表
- **表名：** t_mds_dpsrunlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalstatus | 计算状态 | varchar | 5 |  | √ | ' ' | 计算状态,枚举: A :待运算 B :运算中 C :完成 D :错误 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdpsarrangesetid | 日生产计划待排表定义编码 | int8 | 64 |  | √ | 0 | [日生产计划待排表定义 mds_dpsarrangeset](../mds_files/mds_dpsarrangeset.md) |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsumtime | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 13 | ferrormessage | 异常信息 | varchar | 1000 |  | √ | ' ' | 异常信息 |
| 14 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dpsrunlog |  | fid |
| 2 | idx_mds_dpsrunlog_number |  | fnumber |

---

## 待排表运算日志-多语言表 t_mds_dpsrunlog_l

- **表名称：** 待排表运算日志-多语言表
- **表名：** t_mds_dpsrunlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dpsrunlog_l |  | fpkid |
| 2 | idx_mds_dpsrunlog_l_fid |  | fid,flocaleid |
