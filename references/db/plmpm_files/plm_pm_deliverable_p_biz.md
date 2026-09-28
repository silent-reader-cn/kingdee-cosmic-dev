# 成果-plm_pm_deliverable_p_biz

## 要求状态-多选基础资料表 t_plmpm_dl_requirestatus

- **表名称：** 要求状态-多选基础资料表
- **表名：** t_plmpm_dl_requirestatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [交付物状态配置 plm_pm_deliverable_status](../plmpm_files/plm_pm_deliverable_status.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_dl_requirestatus |  | fpkid |
| 2 | idx_plmpm_dl_requirestatus_fk |  | fentryid |

---

## 项目成果-多语言表 t_plmipdsm_fc_ent_l

- **表名称：** 项目成果-多语言表
- **表名：** t_plmipdsm_fc_ent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmulilangtextfield | fmulilangtextfield | varchar | 200 |  | √ | ' ' |  |
| 2 | fext_field49 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 3 | fext_field1 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 4 | fext_field48 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 5 | fext_field47 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 6 | fext_field46 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 7 | fext_field4 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 8 | fext_field5 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 9 | fext_field2 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 10 | fext_field3 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 11 | fext_field41 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 12 | fext_field40 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 13 | fext_field45 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 14 | fext_field44 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 15 | fext_field43 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 16 | fext_field42 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 17 | fext_field38 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 18 | fext_field37 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 19 | fext_field36 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 20 | fext_field35 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 21 | fext_field39 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 22 | fext_field30 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 23 | fext_field | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 24 | fext_field34 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fext_field33 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 27 | fext_field32 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 28 | fext_field31 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 29 | flocaleid | flocaleid | varchar | 10 |  | √ | '0' | localeid |
| 30 | fext_field27 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 31 | fext_field26 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 32 | fext_field25 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 33 | fext_field24 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 34 | fext_field29 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 35 | fext_field28 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 36 | fext_field23 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 37 | fext_field22 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 38 | fext_field21 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 39 | fext_field20 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 40 | fext_field8 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 41 | fext_field9 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 42 | fext_field6 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 43 | fext_field7 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 44 | fpkid | fpkid | varchar | 36 |  | √ | '0' | pkid |
| 45 | fext_field16 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 46 | fext_field15 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 47 | fext_field14 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 48 | fext_field13 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 49 | fext_field19 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 50 | fext_field18 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 51 | fext_field17 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 52 | fext_field50 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 53 | fext_field12 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 54 | fext_field11 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 55 | fext_field10 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmipdsm_fc_ent_l_0 |  | fentryid,flocaleid |
| 2 | pk_plmipdsm_fc_ent_l |  | fpkid |

---

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
| 5 | fcheckcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fchecksubmitter | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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

## 成果-多语言表 t_plmpm_deliverable_l

- **表名称：** 成果-多语言表
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

## 成果-主表 t_plmpm_deliverable

- **表名称：** 成果-主表
- **表名：** t_plmpm_deliverable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fprojectid | 所属项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbelongtasktplid | fbelongtasktplid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftaskitemclasstypefield | ftaskitemclasstypefield | varchar | 50 |  | √ | ' ' |  |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fseten_enbale | 控制单据体字段锁定 | bpchar | 1 |  | √ | 'A' | 控制单据体字段锁定,枚举: A :A B :B |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftype | ftype | bpchar | 1 |  | √ | 'A' |  |
| 14 | fitemclasstypefield | 所属项目类型 | varchar | 50 |  | √ | ' ' | 所属项目类型,枚举: plm_ipd_project :项目 plm_pm_projecttpl :项目模版 plm_pm_projectbaseline :项目基线 plm_pm_projectcopy :项目副本 |
| 15 | fprojectorgfield | 所属项目创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbelongitem | fbelongitem | varchar | 50 |  | √ | ' ' |  |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | ftaskgroupid | ftaskgroupid | int8 | 64 |  | √ | 0 |  |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | ftaskid | ftaskid | int8 | 64 |  | √ | 0 |  |
| 21 | fbelongtaskid | fbelongtaskid | int8 | 64 |  | √ | 0 |  |

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
| 3 | fsourceid | 源 | varchar | 50 |  | √ | ' ' | 源 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresultsubmitter | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fext_field49 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 7 | fext_field48 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 8 | fext_field1 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 9 | fext_field47 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 10 | fext_field46 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 11 | fext_field4 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 12 | fext_field5 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 13 | fext_field2 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 14 | fext_field3 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 15 | fext_field41 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 16 | fext_field40 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 17 | fpicturefield | fpicturefield | varchar | 255 |  | √ | ' ' |  |
| 18 | fext_field45 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 19 | fext_field44 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 20 | fext_field43 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 21 | fext_field42 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 22 | ftemplate | 模板 | varchar | 50 |  | √ | ' ' | 模板 |
| 23 | ftemplateid | 模板ID | varchar | 50 |  | √ | ' ' | 模板ID |
| 24 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 25 | fext_field38 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 26 | fflowstatus | 流程状态 | varchar | 50 |  | √ | ' ' | 流程状态,枚举: A : B :流程中 C : |
| 27 | fext_field37 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 28 | fext_field36 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 29 | fext_field35 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 30 | fext_field39 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 31 | fext_field30 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 32 | frequirestatus | frequirestatus | int8 | 64 |  | √ | 0 |  |
| 33 | fext_field | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 34 | fext_field34 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 35 | fext_field33 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fext_field32 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 38 | fext_field31 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 39 | fdescribe | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 40 | fdeliverablestatusname | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 41 | fext_field27 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 42 | fext_field26 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 43 | fext_field25 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 44 | fext_field24 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 45 | fext_field29 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 46 | fext_field28 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 47 | frequireconfigid | 配置id | int8 | 64 |  | √ | 0 | 配置id |
| 48 | fext_field23 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 49 | fext_field22 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 50 | fext_field21 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 51 | fext_field20 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 52 | fdeliverable | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 53 | fext_field8 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 54 | fext_field9 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 55 | fext_field6 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 56 | fext_field7 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 57 | fachievementmodel | 分类 | int8 | 64 |  | √ | 0 | [输入输出类型配置 plm_pm_deliverable_model](../plmpm_files/plm_pm_deliverable_model.md) |
| 58 | fext_field16 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 59 | fext_field15 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 60 | fext_field14 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 61 | fext_field13 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 62 | fdeliverablenumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 63 | fext_field19 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 64 | fext_field18 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 65 | fresultcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 66 | fext_field17 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 67 | fdeliverableid | 交付物ID | varchar | 50 |  | √ | ' ' | 交付物ID |
| 68 | fext_field50 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 69 | fext_field12 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 70 | fext_field11 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 71 | fext_field10 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 72 | fresultfinished | 是否完成 | bpchar | 1 |  | √ | '0' | 是否完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmipdsm_fc_ent |  | fentryid |
| 2 | idx_plmipdsm_fc_ent_fk |  | fid |
