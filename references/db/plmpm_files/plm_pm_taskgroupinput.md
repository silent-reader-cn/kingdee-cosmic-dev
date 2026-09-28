# 任务组输入_基础-plm_pm_taskgroupinput

## 任务组输入-子表 t_plmpm_scopeent

- **表名称：** 任务组输入-子表
- **表名：** t_plmpm_scopeent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverablestatus | 交付物状态 | varchar | 50 |  | √ | ' ' | 交付物状态 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fscopesubmitter | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fext_field49 | fext_field49 | varchar | 200 |  | √ | ' ' |  |
| 6 | fext_field48 | fext_field48 | varchar | 200 |  | √ | ' ' |  |
| 7 | fext_field1 | fext_field1 | varchar | 200 |  | √ | ' ' |  |
| 8 | fext_field47 | fext_field47 | varchar | 200 |  | √ | ' ' |  |
| 9 | fext_field46 | fext_field46 | varchar | 200 |  | √ | ' ' |  |
| 10 | fext_field4 | fext_field4 | varchar | 200 |  | √ | ' ' |  |
| 11 | fext_field5 | fext_field5 | varchar | 200 |  | √ | ' ' |  |
| 12 | fext_field2 | fext_field2 | varchar | 200 |  | √ | ' ' |  |
| 13 | fext_field3 | fext_field3 | varchar | 200 |  | √ | ' ' |  |
| 14 | fext_field41 | fext_field41 | varchar | 200 |  | √ | ' ' |  |
| 15 | fext_field40 | fext_field40 | varchar | 200 |  | √ | ' ' |  |
| 16 | fext_field45 | fext_field45 | varchar | 200 |  | √ | ' ' |  |
| 17 | fext_field44 | fext_field44 | varchar | 200 |  | √ | ' ' |  |
| 18 | fext_field43 | fext_field43 | varchar | 200 |  | √ | ' ' |  |
| 19 | fext_field42 | fext_field42 | varchar | 200 |  | √ | ' ' |  |
| 20 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 21 | fext_field38 | fext_field38 | varchar | 200 |  | √ | ' ' |  |
| 22 | fext_field37 | fext_field37 | varchar | 200 |  | √ | ' ' |  |
| 23 | fext_field36 | fext_field36 | varchar | 200 |  | √ | ' ' |  |
| 24 | fext_field35 | fext_field35 | varchar | 200 |  | √ | ' ' |  |
| 25 | fext_field39 | fext_field39 | varchar | 200 |  | √ | ' ' |  |
| 26 | fext_field30 | fext_field30 | varchar | 200 |  | √ | ' ' |  |
| 27 | fext_field | fext_field | varchar | 200 |  | √ | ' ' |  |
| 28 | fext_field34 | fext_field34 | varchar | 200 |  | √ | ' ' |  |
| 29 | fext_field33 | fext_field33 | varchar | 200 |  | √ | ' ' |  |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fext_field32 | fext_field32 | varchar | 200 |  | √ | ' ' |  |
| 32 | fext_field31 | fext_field31 | varchar | 200 |  | √ | ' ' |  |
| 33 | fdeliverablestatusname | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 34 | fext_field27 | fext_field27 | varchar | 200 |  | √ | ' ' |  |
| 35 | fext_field26 | fext_field26 | varchar | 200 |  | √ | ' ' |  |
| 36 | fext_field25 | fext_field25 | varchar | 200 |  | √ | ' ' |  |
| 37 | fext_field24 | fext_field24 | varchar | 200 |  | √ | ' ' |  |
| 38 | fext_field29 | fext_field29 | varchar | 200 |  | √ | ' ' |  |
| 39 | fext_field28 | fext_field28 | varchar | 200 |  | √ | ' ' |  |
| 40 | fext_field23 | fext_field23 | varchar | 200 |  | √ | ' ' |  |
| 41 | fext_field22 | fext_field22 | varchar | 200 |  | √ | ' ' |  |
| 42 | fext_field21 | fext_field21 | varchar | 200 |  | √ | ' ' |  |
| 43 | fext_field20 | fext_field20 | varchar | 200 |  | √ | ' ' |  |
| 44 | fdeliverable | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 45 | fext_field8 | fext_field8 | varchar | 200 |  | √ | ' ' |  |
| 46 | fext_field9 | fext_field9 | varchar | 200 |  | √ | ' ' |  |
| 47 | fext_field6 | fext_field6 | varchar | 200 |  | √ | ' ' |  |
| 48 | fext_field7 | fext_field7 | varchar | 200 |  | √ | ' ' |  |
| 49 | fachievementmodel | 分类 | int8 | 64 |  | √ | 0 | 输入输出类型 plm_pm_deliverable_model |
| 50 | fext_field16 | fext_field16 | varchar | 200 |  | √ | ' ' |  |
| 51 | fext_field15 | fext_field15 | varchar | 200 |  | √ | ' ' |  |
| 52 | fext_field14 | fext_field14 | varchar | 200 |  | √ | ' ' |  |
| 53 | fext_field13 | fext_field13 | varchar | 200 |  | √ | ' ' |  |
| 54 | fdeliverablenumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 55 | fext_field19 | fext_field19 | varchar | 200 |  | √ | ' ' |  |
| 56 | fext_field18 | fext_field18 | varchar | 200 |  | √ | ' ' |  |
| 57 | fresultcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 58 | fext_field17 | fext_field17 | varchar | 200 |  | √ | ' ' |  |
| 59 | fdeliverableid | 交付物ID | varchar | 50 |  | √ | ' ' | 交付物ID |
| 60 | fext_field50 | fext_field50 | varchar | 200 |  | √ | ' ' |  |
| 61 | fext_field12 | fext_field12 | varchar | 200 |  | √ | ' ' |  |
| 62 | fext_field11 | fext_field11 | varchar | 200 |  | √ | ' ' |  |
| 63 | fext_field10 | fext_field10 | varchar | 200 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmpm_scopeent_fk |  | fid |
| 2 | pk_plmpm_scopeent |  | fentryid |

---

## 任务组输入_基础-主表 t_plmpm_scope

- **表名称：** 任务组输入_基础-主表
- **表名：** t_plmpm_scope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fprojectid | 所属项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fseten_enbale | 控制单据体字段锁定 | bpchar | 1 |  | √ | 'A' | 控制单据体字段锁定,枚举: A :A B :B |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fprojectorgfield | 所属项目创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | ftaskgroupid | 所属任务组 | int8 | 64 |  | √ | 0 | 任务 plm_ipd_task |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | ftaskid | ftaskid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_scope |  | fid |
| 2 | idx_plmpm_scope_m0 |  | fmasterid |

---

## 任务组输入_基础-多语言表 t_plmpm_scope_l

- **表名称：** 任务组输入_基础-多语言表
- **表名：** t_plmpm_scope_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmpm_scope_l_0 |  | fid,flocaleid |
| 2 | pk_plmpm_scope_l |  | fpkid |
