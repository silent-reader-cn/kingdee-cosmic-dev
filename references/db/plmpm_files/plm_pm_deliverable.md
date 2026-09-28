# 成果_基础-plm_pm_deliverable

## 检查项-子表 t_plmpm_deliverable_check

- **表名称：** 检查项-子表
- **表名：** t_plmpm_deliverable_check

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreator | fcreator | int8 | 64 |  | √ | 0 |  |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fdes | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 4 | ffinished | 是否完成 | bpchar | 1 |  | √ | '0' | 是否完成 |
| 5 | fcheckcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fchecksubmitter | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fcheckitem | 检查项要求 | varchar | 200 |  | √ | ' ' | 检查项要求 |
| 9 | fdatetimefield | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_deliverable_check |  | fentryid |
| 2 | idx_plmpm_deliverable_check_fk |  | fid |

---

## 成果_基础-多语言表 t_plmpm_deliverable_l

- **表名称：** 成果_基础-多语言表
- **表名：** t_plmpm_deliverable_l

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
| 1 | idx_plmpm_deliverable_l_0 |  | fid,flocaleid |
| 2 | pk_plmpm_deliverable_l |  | fpkid |

---

## 成果_基础-主表 t_plmpm_deliverable

- **表名称：** 成果_基础-主表
- **表名：** t_plmpm_deliverable

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
| 11 | ftype | ftype | bpchar | 1 |  | √ | 'A' |  |
| 12 | fprojectorgfield | 所属项目创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbelongitem | fbelongitem | varchar | 50 |  | √ | ' ' |  |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | ftaskgroupid | ftaskgroupid | int8 | 64 |  | √ | 0 |  |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | ftaskid | ftaskid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_deliverable |  | fid |
| 2 | idx_plmpm_deliverable_m0 |  | fmasterid |

---

## 项目成果-子表 t_plmipdsm_fc_ent

- **表名称：** 项目成果-子表
- **表名：** t_plmipdsm_fc_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverablestatus | 交付物状态 | varchar | 200 |  | √ | ' ' | 交付物状态 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fresultsubmitter | 提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 16 | fpicturefield | fpicturefield | varchar | 255 |  | √ | ' ' |  |
| 17 | fext_field45 | fext_field45 | varchar | 200 |  | √ | ' ' |  |
| 18 | fext_field44 | fext_field44 | varchar | 200 |  | √ | ' ' |  |
| 19 | fext_field43 | fext_field43 | varchar | 200 |  | √ | ' ' |  |
| 20 | fext_field42 | fext_field42 | varchar | 200 |  | √ | ' ' |  |
| 21 | ftemplate | 模板 | varchar | 50 |  | √ | ' ' | 模板 |
| 22 | ftemplateid | 模板ID | varchar | 50 |  | √ | ' ' | 模板ID |
| 23 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 24 | fext_field38 | fext_field38 | varchar | 200 |  | √ | ' ' |  |
| 25 | fext_field37 | fext_field37 | varchar | 200 |  | √ | ' ' |  |
| 26 | fext_field36 | fext_field36 | varchar | 200 |  | √ | ' ' |  |
| 27 | fext_field35 | fext_field35 | varchar | 200 |  | √ | ' ' |  |
| 28 | fext_field39 | fext_field39 | varchar | 200 |  | √ | ' ' |  |
| 29 | fext_field30 | fext_field30 | varchar | 200 |  | √ | ' ' |  |
| 30 | frequirestatus | 要求状态 | int8 | 64 |  | √ | 0 | 交付物状态 plm_pm_deliverable_status |
| 31 | fext_field | fext_field | varchar | 200 |  | √ | ' ' |  |
| 32 | fext_field34 | fext_field34 | varchar | 200 |  | √ | ' ' |  |
| 33 | fext_field33 | fext_field33 | varchar | 200 |  | √ | ' ' |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fext_field32 | fext_field32 | varchar | 200 |  | √ | ' ' |  |
| 36 | fext_field31 | fext_field31 | varchar | 200 |  | √ | ' ' |  |
| 37 | fdescribe | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 38 | fdeliverablestatusname | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 39 | fext_field27 | fext_field27 | varchar | 200 |  | √ | ' ' |  |
| 40 | fext_field26 | fext_field26 | varchar | 200 |  | √ | ' ' |  |
| 41 | fext_field25 | fext_field25 | varchar | 200 |  | √ | ' ' |  |
| 42 | fext_field24 | fext_field24 | varchar | 200 |  | √ | ' ' |  |
| 43 | fext_field29 | fext_field29 | varchar | 200 |  | √ | ' ' |  |
| 44 | fext_field28 | fext_field28 | varchar | 200 |  | √ | ' ' |  |
| 45 | fext_field23 | fext_field23 | varchar | 200 |  | √ | ' ' |  |
| 46 | fext_field22 | fext_field22 | varchar | 200 |  | √ | ' ' |  |
| 47 | fext_field21 | fext_field21 | varchar | 200 |  | √ | ' ' |  |
| 48 | fext_field20 | fext_field20 | varchar | 200 |  | √ | ' ' |  |
| 49 | fdeliverable | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 50 | fext_field8 | fext_field8 | varchar | 200 |  | √ | ' ' |  |
| 51 | fext_field9 | fext_field9 | varchar | 200 |  | √ | ' ' |  |
| 52 | fext_field6 | fext_field6 | varchar | 200 |  | √ | ' ' |  |
| 53 | fext_field7 | fext_field7 | varchar | 200 |  | √ | ' ' |  |
| 54 | fachievementmodel | 分类 | int8 | 64 |  | √ | 0 | 输入输出类型 plm_pm_deliverable_model |
| 55 | fext_field16 | fext_field16 | varchar | 200 |  | √ | ' ' |  |
| 56 | fext_field15 | fext_field15 | varchar | 200 |  | √ | ' ' |  |
| 57 | fext_field14 | fext_field14 | varchar | 200 |  | √ | ' ' |  |
| 58 | fext_field13 | fext_field13 | varchar | 200 |  | √ | ' ' |  |
| 59 | fdeliverablenumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 60 | fext_field19 | fext_field19 | varchar | 200 |  | √ | ' ' |  |
| 61 | fext_field18 | fext_field18 | varchar | 200 |  | √ | ' ' |  |
| 62 | fresultcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 63 | fext_field17 | fext_field17 | varchar | 200 |  | √ | ' ' |  |
| 64 | fdeliverableid | 交付物ID | varchar | 50 |  | √ | ' ' | 交付物ID |
| 65 | fext_field50 | fext_field50 | varchar | 200 |  | √ | ' ' |  |
| 66 | fext_field12 | fext_field12 | varchar | 200 |  | √ | ' ' |  |
| 67 | fext_field11 | fext_field11 | varchar | 200 |  | √ | ' ' |  |
| 68 | fext_field10 | fext_field10 | varchar | 200 |  | √ | ' ' |  |
| 69 | fresultfinished | 是否完成 | bpchar | 1 |  | √ | '0' | 是否完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmipdsm_fc_ent |  | fentryid |
| 2 | idx_plmipdsm_fc_ent_fk |  | fid |
