# 触发日志-srm_autoevatpl_log

## 触发日志-主表 t_srm_autoevatpllog

- **表名称：** 触发日志-主表
- **表名：** t_srm_autoevatpllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | ftplid | 绩效评估模板id | varchar | 80 |  | √ | ' ' | 绩效评估模板id |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | ftag | 触发依据 | varchar | 80 |  | √ | ' ' | 触发依据 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbillobjectid | 取值单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fexecdate | 业务触发时间 | timestamp | 0 |  |  | null | 业务触发时间 |
| 10 | ftargetbillno | 下推单据编号 | varchar | 80 |  | √ | ' ' | 下推单据编号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fexectplversionid | 智能绩效设置触发版本 | int8 | 64 |  | √ | 0 | [智能绩效设置版本记录 srm_autoevatpl_ver](../srm_files/srm_autoevatpl_ver.md) |
| 14 | flogdate | 日志时间 | timestamp | 0 |  |  | null | 日志时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fexecstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :失败 B :成功 C :执行中 D :已重试 |
| 18 | fsourcebillid | 取值单据源单id | varchar | 50 |  | √ | ' ' | 取值单据源单id |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_autoevatpllog_fstatus |  | fexecstatus |
| 2 | pk_srm_autoevatpllog |  | fid |
| 3 | idx_srm_autoevatpllog_ftag |  | ftag |

---

## 触发日志-多语言表 t_srm_autoevatpllog_l

- **表名称：** 触发日志-多语言表
- **表名：** t_srm_autoevatpllog_l

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
| 1 | idx_srm_autoevatpllog_l_idloc |  | fid,flocaleid |
| 2 | pk_srm_autoevatpllog_l |  | fpkid |
