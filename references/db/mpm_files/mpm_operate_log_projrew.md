# 项目风险操作记录-mpm_operate_log_projrew

## 单据体-子表 t_mpm_projrewopentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_projrewopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprevalue | 变更前值 | varchar | 512 |  | √ | ' ' | 变更前值 |
| 3 | faftervalue | 变更后值 | varchar | 512 |  | √ | ' ' | 变更后值 |
| 4 | fprevaluebdid | 变更前基础资料ID | varchar | 80 |  | √ | ' ' | 变更前基础资料ID |
| 5 | faftervaluebdid | 变更后基础资料ID | varchar | 80 |  | √ | ' ' | 变更后基础资料ID |
| 6 | fopentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 7 | fopentrysign | 分录标识 | varchar | 255 |  | √ | ' ' | 分录标识 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fchangesign | 变更标识 | varchar | 255 |  | √ | ' ' | 变更标识 |
| 10 | fchangename | 变更字段 | varchar | 512 |  | √ | ' ' | 变更字段 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_projrewopentry |  | fentryid |
| 2 | idx_mpm_rewopentry_fk |  | fid |

---

## 单据体-多语言表 t_mpm_projrewopentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mpm_projrewopentry_l

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
| 1 | pk_t_mpm_projrewopentry_l |  | fpkid |
| 2 | idx_mpm_rewentry_fel |  | fentryid,flocaleid |

---

## 项目风险操作记录-主表 t_mpm_projrewoplog

- **表名称：** 项目风险操作记录-主表
- **表名：** t_mpm_projrewoplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fbillstatus | 风险状态 | bpchar | 1 |  | √ | ' ' | 风险状态,枚举: A :未指派 B :待接收 C :跟进中 D :关闭 |
| 5 | foptype | 操作类型 | bpchar | 1 |  | √ | ' ' | 操作类型,枚举: A :创建 B :修改 C :删除 P :指派 R :接收 J :退回 Z :关闭 S :关闭 M :关闭 |
| 6 | foptouserid | 操作对象 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fobjectid | billid | int8 | 64 |  | √ | 0 | billid |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | frelationbillid | 关联单据id | varchar | 50 |  | √ | ' ' | 关联单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projrewoplog_fi |  | fobjectid |
| 2 | pk_mpm_projrewoplog |  | fid |
