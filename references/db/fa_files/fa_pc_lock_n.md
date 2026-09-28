# 总分锁-fa_pc_lock_n

## 总分锁-主表 t_fa_pc_lock_n

- **表名称：** 总分锁-主表
- **表名：** t_fa_pc_lock_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fholdlockentityname | 持锁单据实体类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fholdlockdataid | 持锁数据ID | int8 | 64 |  | √ | 0 | 持锁数据ID |
| 4 | ftype | 锁类型 | varchar | 50 |  | √ | ' ' | 锁类型,枚举: P :总锁 C :分锁 |
| 5 | fsublocknum | 子锁次数 | int8 | 64 |  | √ | 0 | 子锁次数 |
| 6 | flockeddatanum | 被锁数据编码 | varchar | 50 |  |  | ' ' | 被锁数据编码 |
| 7 | flockeddatamasterid | 被锁数据masterID | int8 | 64 |  | √ | 0 | 被锁数据masterID |
| 8 | flockedentityname | 被锁基础资料 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | flockeddatastatus | 被锁数据业务状态 | varchar | 50 |  | √ | ' ' | 被锁数据业务状态 |
| 10 | fusepurpose | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: default :默认 |
| 11 | fholdlockdatano | 持锁单据编码 | varchar | 50 |  | √ | ' ' | 持锁单据编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_pc_lockn |  | fid |
| 2 | idx_fa_pc_lock_flockeddatanumn |  | flockeddatanum,flockedentityname |
| 3 | idx_fa_pc_lock_uniquen |  | flockeddatamasterid,flockedentityname,fusepurpose |

---

## 单据体-子表 t_fa_pc_lock_detail_n

- **表名称：** 单据体-子表
- **表名：** t_fa_pc_lock_detail_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdtmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fdtholdlockdatanum | 持锁单据编码 | varchar | 50 |  | √ | ' ' | 持锁单据编码 |
| 4 | fdtholdlockentityname | 持锁单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdtholdlockdataid | 持锁数据ID | int8 | 64 |  | √ | 0 | 持锁数据ID |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_pc_lock_detail_unqn |  | fid,fdtholdlockentityname,fdtholdlockdataid |
| 2 | pk_fa_pc_lock_detailn |  | fentryid |
