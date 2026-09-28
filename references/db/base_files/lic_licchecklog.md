# 许可校验日志-lic_licchecklog

## 许可校验日志-主表 t_lic_licchecklog

- **表名称：** 许可校验日志-主表
- **表名：** t_lic_licchecklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceid | 许可校验日志 | varchar | 80 |  | √ | ' ' | 许可校验日志 |
| 3 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fcancelmessage | 许可提示 | varchar | 1024 |  | √ | ' ' | 许可提示 |
| 5 | fuserid | 许可校验用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fchecktime | 许可校验时间 | timestamp | 0 |  |  | null | 许可校验时间 |
| 7 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_licchecklog_object |  | fbizobjectid |
| 2 | pk_t_lic_licchecklog |  | fid |
| 3 | idx_lic_licchecklog_traceid |  | ftraceid |
| 4 | idx_lic_licchecklog_appobject |  | fbizappid,fbizobjectid |
| 5 | idx_lic_licchecklog_uaoid |  | fuserid,fbizappid,fbizobjectid |

---

## 单据体-子表 t_lic_licchecklogentry

- **表名称：** 单据体-子表
- **表名：** t_lic_licchecklogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 级别 | varchar | 36 |  | √ | ' ' | 级别,枚举: info :INIFO debug :DEBUG |
| 3 | fmessage | 提示信息 | varchar | 1024 |  | √ | ' ' | 提示信息 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_licchecklogentry |  | fentryid |
| 2 | idx_lic_licchecklogentry_id |  | fid |
