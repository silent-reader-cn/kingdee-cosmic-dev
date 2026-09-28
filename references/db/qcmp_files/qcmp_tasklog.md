# 移动任务日志-qcmp_tasklog

## 移动任务日志-主表 t_qcmp_tasklog

- **表名称：** 移动任务日志-主表
- **表名：** t_qcmp_tasklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbiztype | 任务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 4 | ftype | 操作类型 | varchar | 1 |  | √ | '1' | 操作类型,枚举: 1 :认领 2 :指派 3 :委托 4 :完成 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fexpectdate | 期望完成日期 | timestamp | 0 |  |  | null | 期望完成日期 |
| 7 | fnumber | 任务编号 | varchar | 30 |  | √ | ' ' | 任务编号 |
| 8 | freason | 委托事由 | varchar | 255 |  |  | ' ' | 委托事由 |
| 9 | ftaskid | 移动任务单 | int8 | 64 |  | √ | 0 | [移动质检任务单 qcmp_taskinfo](../qcbd_files/qcmp_taskinfo.md) |
| 10 | ftouser | 接受人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | freceivetime | 接受时间 | timestamp | 0 |  |  | null | 接受时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcmp_tasklog |  | fid |
| 2 | idx_qcmp_tasklog_fcreatetime |  | fcreatetime |
| 3 | idx_qcmp_tasklog_fcreator |  | fcreator |
| 4 | idx_qcmp_tasklog_ftaskid |  | ftaskid |

---

## 移动任务日志-多语言表 t_qcmp_tasklog_l

- **表名称：** 移动任务日志-多语言表
- **表名：** t_qcmp_tasklog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 3 | freason | 委托事由 | varchar | 255 |  | √ | ' ' | 委托事由 |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcmp_tasklogl_idlocale |  | fid,flocaleid |
| 2 | pk_t_qcmp_tasklog_l |  | fpkid |
