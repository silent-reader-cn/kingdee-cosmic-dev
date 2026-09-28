# 抽取方案执行记录-tlmgt_execute_record

## 活动状态-子表 t_tlmgt_activity_record

- **表名称：** 活动状态-子表
- **表名：** t_tlmgt_activity_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | factivitystatus | 活动状态 | varchar | 64 |  | √ | ' ' | 活动状态,枚举: un_activity :未调用 activitying :调用中 activity_success :调用成功 activity_fail :调用失败 |
| 4 | factivitymsg | 活动结果 | varchar | 1024 |  | √ | ' ' | 活动结果 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_acti_rec |  | fid |
| 2 | pk_t_tlmgt_activity_record |  | fentryid |

---

## 抽取方案执行记录-主表 t_tlmgt_execute_record

- **表名称：** 抽取方案执行记录-主表
- **表名：** t_tlmgt_execute_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fdiff | 是否差量 | varchar | 64 |  | √ | ' ' | 是否差量,枚举: Y :是 N :否 |
| 6 | fexecutemsg | 执行结果 | varchar | 1024 |  | √ | ' ' | 执行结果 |
| 7 | fschemeid | 执行方案 | int8 | 64 |  | √ | 0 | [抽取方案 tlmgt_extract_scheme](../tlmgt_files/tlmgt_extract_scheme.md) |
| 8 | fexecutestatus | 执行状态 | varchar | 64 |  | √ | ' ' | 执行状态,枚举: ready_execute :准备执行 executing :执行中 execute_success :执行成功 execute_fail :执行失败 |
| 9 | flang | 执行语言 | varchar | 64 |  | √ | ' ' | 执行语言 |
| 10 | fexecuteno | 执行编号 | varchar | 64 |  | √ | ' ' | 执行编号 |
| 11 | fexecutetype | 执行类型 | varchar | 64 |  | √ | ' ' | 执行类型,枚举: extract :抽取 apply :应用 build :构建 |
| 12 | fmodifytime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_execute_record |  | fid |
| 2 | idx_t_tlmgt_exe_rec |  | fexecuteno |
| 3 | idx_t_tlmgt_exe_type |  | fexecutetype,fexecutestatus,flang |

---

## 子单据体-子表 t_tlmgt_activity_scope

- **表名称：** 子单据体-子表
- **表名：** t_tlmgt_activity_scope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fresourcefiletype | 资源文件类型 | varchar | 64 |  | √ | ' ' | 资源文件类型 |
| 2 | fscopemsg_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 3 | fworddatatype | 词条数据类型 | varchar | 64 |  | √ | ' ' | 词条数据类型 |
| 4 | fseq | 分录行号 | varchar | 64 |  | √ | ' ' | 分录行号 |
| 5 | fresourceidentifier | 资源标识 | varchar | 64 |  | √ | ' ' | 资源标识 |
| 6 | fwordtype | 词条类型 | varchar | 64 |  | √ | ' ' | 词条类型 |
| 7 | fscopemsg | 结果 | varchar | 255 |  | √ | ' ' | 结果 |
| 8 | fresourcetype | 资源类型 | varchar | 64 |  | √ | ' ' | 资源类型 |
| 9 | fdomainidentifier | 领域标识 | varchar | 64 |  | √ | ' ' | 领域标识 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fmoduleidentifier | 模块标识 | varchar | 64 |  | √ | ' ' | 模块标识 |
| 13 | fscopestatus | 范围状态 | varchar | 64 |  | √ | ' ' | 范围状态,枚举: success :成功 fail :失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_activity_scope |  | fdetailid |
| 2 | idx_t_tlmgt_acti_sco |  | fentryid |
| 3 | idx_t_tlmgt_acti_scope |  | fresourcetype,fresourcefiletype,fdomainidentifier,fmoduleidentifier,fresourceidentifier |
