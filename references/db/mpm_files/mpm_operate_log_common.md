# 通用操作记录-mpm_operate_log_common

## 单据体-子表 t_mpm_commopentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_commopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprevalue | 变更前值 | varchar | 512 |  | √ | ' ' | 变更前值 |
| 3 | faftervalue | 变更后值 | varchar | 512 |  | √ | ' ' | 变更后值 |
| 4 | fopentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 5 | fopentrysign | 分录标识 | varchar | 255 |  | √ | ' ' | 分录标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fchangesign | 变更标识 | varchar | 255 |  | √ | ' ' | 变更标识 |
| 8 | fchangename | 变更字段 | varchar | 512 |  | √ | ' ' | 变更字段 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_commopentry_fk |  | fid |
| 2 | pk_mpm_commopentry |  | fentryid |

---

## 单据体-多语言表 t_mpm_commopentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mpm_commopentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprevalue | 变更前值 | varchar | 512 |  | √ | ' ' | 变更前值 |
| 2 | faftervalue | 变更后值 | varchar | 512 |  | √ | ' ' | 变更后值 |
| 3 | fchangename | 变更字段 | varchar | 512 |  | √ | ' ' | 变更字段 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_commopentry_l |  | fpkid |
| 2 | idx_mpm_commopentry_l_fl |  | fentryid,flocaleid |

---

## 通用操作记录-主表 t_mpm_commoplog

- **表名称：** 通用操作记录-主表
- **表名：** t_mpm_commoplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | foptype | 操作类型 | bpchar | 1 |  | √ | 'A' | 操作类型,枚举: A :新增 B :修改 C :删除 |
| 5 | fobjectid | billid | int8 | 64 |  | √ | 0 | billid |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | frelationbillid | 关联单据id | varchar | 255 |  | √ | ' ' | 关联单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_commoplog_fi |  | fobjectid |
| 2 | pk_mpm_commoplog |  | fid |
