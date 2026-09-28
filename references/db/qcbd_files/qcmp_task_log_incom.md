# 来料检验任务日志-qcmp_task_log_incom

## 来料检验任务日志-主表 t_qcmp_logincom

- **表名称：** 来料检验任务日志-主表
- **表名：** t_qcmp_logincom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 来源分录id | int8 | 64 |  | √ | 0 | 来源分录id |
| 3 | ftype | 操作类型 | bpchar | 1 |  | √ | '1' | 操作类型,枚举: 1 :认领 2 :指派 3 :委托 4 :完成 5 :撤销认领 6 :委托接受 7 :委托拒绝 8 :撤销委托 9 :撤销指派 A :已关闭 B :反审核 C :已修改 D :重新指派 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbiztypeid | 任务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 7 | freason | 委托事由 | varchar | 600 |  | √ | ' ' | 委托事由 |
| 8 | ftouserid | 接受人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | freceivetime | 接受时间 | timestamp | 0 |  |  | null | 接受时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcmp_logincom_fbiztypeid |  | fbiztypeid |
| 2 | idx_qcmp_logincom_fsrcentryid |  | fsrcentryid |
| 3 | pk_t_qcmp_logincom |  | fid |
| 4 | idx_qcmp_logincom_fcreatetime |  | fcreatetime |
| 5 | idx_qcmp_logincom_fcreator |  | fcreatorid |

---

## 关联子实体-子表 t_qcmp_logincom_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcmp_logincom_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcmp_logincom_lk_fk |  | fid |
| 2 | pk_qcmp_logincom_lk |  | fpkid |

---

## 来料检验任务日志-多语言表 t_qcmp_logincom_l

- **表名称：** 来料检验任务日志-多语言表
- **表名：** t_qcmp_logincom_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | freason | 委托事由 | varchar | 600 |  | √ | ' ' | 委托事由 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcmp_logincoml_idlocale |  | fid,flocaleid |
| 2 | pk_t_qcmp_logincom_l |  | fpkid |
