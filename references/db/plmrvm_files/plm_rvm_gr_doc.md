# GR评审单-plm_rvm_gr_doc

## GR评审单-使用范围表 t_plm_rvm_doc_u

- **表名称：** GR评审单-使用范围表
- **表名：** t_plm_rvm_doc_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_rvm_doc_u_uo |  | fuseorgid |
| 2 | pk_t_plm_rvm_doc_u |  | fdataid,fuseorgid |

---

## 评审问题-子表 t_plm_rvm_que

- **表名称：** 评审问题-子表
- **表名：** t_plm_rvm_que

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fquestion | 问题 | int8 | 64 |  | √ | 0 | [问题 plm_qm_baseinfo](../plmqm_files/plm_qm_baseinfo.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_que_fk |  | fid |
| 2 | pk_plm_rvm_que |  | fentryid |

---

## GR评审单-多语言表 t_plm_rvm_doc_l

- **表名称：** GR评审单-多语言表
- **表名：** t_plm_rvm_doc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_doc_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rvm_doc_l |  | fpkid |

---

## 评审材料-子表 t_plm_rvm_doc_file

- **表名称：** 评审材料-子表
- **表名：** t_plm_rvm_doc_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverablestatus | 交付物状态 | varchar | 50 |  | √ | ' ' | 交付物状态 |
| 3 | ffruit_file_id | 项目成果交付物分录id | int8 | 64 |  | √ | 0 | 项目成果交付物分录id |
| 4 | ftemplateid | 模板ID | varchar | 50 |  | √ | ' ' | 模板ID |
| 5 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffruit_id | 项目成果主表id | int8 | 64 |  | √ | 0 | 项目成果主表id |
| 8 | fresultsubmitter | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fachievementmodel | 分类 | int8 | 64 |  | √ | 0 | [输入输出类型配置 plm_pm_deliverable_model](../plmpm_files/plm_pm_deliverable_model.md) |
| 10 | ftextfield | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 11 | fdeliverablenumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fdeliverableid | 交付物ID | varchar | 50 |  | √ | ' ' | 交付物ID |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_doc_file |  | fentryid |
| 2 | idx_plm_rvm_doc_file_fk |  | fid |

---

## 评审点-多选基础资料表 t_plm_rvm_mulpoint

- **表名称：** 评审点-多选基础资料表
- **表名：** t_plm_rvm_mulpoint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [评审点 plm_qm_review_point](../plmrvm_files/plm_qm_review_point.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_mulpoint |  | fpkid |
| 2 | idx_plm_rvm_mulpoint_fk |  | fid |

---

## GR评审单-主表 t_plm_rvm_doc

- **表名称：** GR评审单-主表
- **表名：** t_plm_rvm_doc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 评审类型 | int8 | 64 |  | √ | 0 | [评审分类 plm_rvm_group](../plmrvm_files/plm_rvm_group.md) |
| 3 | fstatus_dpd_date | 状态转换日期 | timestamp | 0 |  |  | null | 状态转换日期 |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :高 higher :较高 middle :中 lower :较低 low :低 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fupversiondes | 修订描述 | varchar | 500 |  | √ | ' ' | 修订描述 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fflowsign | 流程标识 | bpchar | 1 |  | √ | '0' | 流程标识 |
| 16 | fcurversionid | 当前版本ID | int8 | 64 |  | √ | 0 | 当前版本ID |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fstatus_keep_days | 当前状态停留时长（天） | int8 | 64 |  | √ | 0 | 当前状态停留时长（天） |
| 22 | fissuer | 签发人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fitemstatusid | 状态 | int8 | 64 |  | √ | 0 | [状态 plm_ipd_lc_status](../plmipdsm_files/plm_ipd_lc_status.md) |
| 24 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fbasedatafield | 工作项图标 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 26 | fcurversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 31 | fseuser | SE | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 33 | flatestver | 是否最新版本 | bpchar | 1 |  | √ | '1' | 是否最新版本 |
| 34 | fprmbase | 产品路标 | int8 | 64 |  | √ | 0 | 产品路标基础 plm_prm_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_rvm_doc_master |  | fmasterid |
| 2 | idx_t_plm_rvm_doc_createorg |  | fcreateorgid |
| 3 | idx_plm_rvm_doc_m0 |  | fmasterid |
| 4 | pk_plm_rvm_doc |  | fid |

---

## 自检人-子表 t_plm_rvm_check

- **表名称：** 自检人-子表
- **表名：** t_plm_rvm_check

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheck_perm_role | 通用角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | frole_type | 角色类型 | varchar | 50 |  | √ | ' ' | 角色类型,枚举: A :通用角色 B :PLM角色 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fplm_pri_role | PLM角色 | int8 | 64 |  | √ | 0 | [PLM角色 plm_plmsm_role](../plmsm_files/plm_plmsm_role.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_check_fk |  | fid |
| 2 | pk_plm_rvm_check |  | fentryid |

---

## 参与人-多选基础资料表 t_plm_rvm_checkp

- **表名称：** 参与人-多选基础资料表
- **表名：** t_plm_rvm_checkp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_checkp_fk |  | fentryid |
| 2 | pk_plm_rvm_checkp |  | fpkid |

---

## 负责人-多选基础资料表 t_plm_rvm_chargeperson

- **表名称：** 负责人-多选基础资料表
- **表名：** t_plm_rvm_chargeperson

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_chargeperson |  | fpkid |
| 2 | idx_plm_rvm_chargeperson_fk |  | fid |

---

## 评审要素-子表 t_plm_rvm_doc_ele

- **表名称：** 评审要素-子表
- **表名：** t_plm_rvm_doc_ele

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freview_elements | 评审要素 | int8 | 64 |  | √ | 0 | [评审要素 plm_qm_review_elements](../plmrvm_files/plm_qm_review_elements.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_doc_ele |  | fentryid |
| 2 | idx_plm_rvm_doc_ele_fk |  | fid |

---

## 会签人-子表 t_plm_rvm_sign

- **表名称：** 会签人-子表
- **表名：** t_plm_rvm_sign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsign_perm_role | 通用角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fplm_pri_role1 | PLM角色 | int8 | 64 |  | √ | 0 | [PLM角色 plm_plmsm_role](../plmsm_files/plm_plmsm_role.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frole_type1 | 角色类型 | varchar | 50 |  | √ | ' ' | 角色类型,枚举: A :通用角色 B :PLM角色 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_sign |  | fentryid |
| 2 | idx_plm_rvm_sign_fk |  | fid |

---

## 参与人-多选基础资料表 t_plm_rvm_signp

- **表名称：** 参与人-多选基础资料表
- **表名：** t_plm_rvm_signp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_signp_fk |  | fentryid |
| 2 | pk_plm_rvm_signp |  | fpkid |

---

## 填写质量目标完成情况-子表 t_plm_rvm_qa_obj

- **表名称：** 填写质量目标完成情况-子表
- **表名：** t_plm_rvm_qa_obj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftarget_value | 目标值 | int8 | 64 |  | √ | 0 | 目标值 |
| 3 | fillustrate | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 4 | factual_value | 实际值 | int8 | 64 |  | √ | 0 | 实际值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fisfrompoint | 是否评审点带入 | bpchar | 1 |  | √ | '0' | 是否评审点带入 |
| 7 | fqa_obj | 质量目标 | int8 | 64 |  | √ | 0 | [质量目标 plm_qm_objectives](../plmrvm_files/plm_qm_objectives.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_qa_obj_fk |  | fid |
| 2 | pk_plm_rvm_qa_obj |  | fentryid |

---

## 关联子实体-子表 t_plm_ipditembaseinfo_lk

- **表名称：** 关联子实体-子表
- **表名：** t_plm_ipditembaseinfo_lk

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
| 1 | pk_plm_ipditembaseinfo_lk |  | fpkid |
| 2 | idx_plm_ipditembaseinfo_lk_fk |  | fid |

---

## 后续活动-子表 t_plm_rvm_act

- **表名称：** 后续活动-子表
- **表名：** t_plm_rvm_act

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisactfrompoint | 是否评审点带入 | bpchar | 1 |  | √ | '0' | 是否评审点带入 |
| 3 | ffollowup_act | 后续活动 | int8 | 64 |  | √ | 0 | [后续活动 plm_qm_followup_activity](../plmrvm_files/plm_qm_followup_activity.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_act_fk |  | fid |
| 2 | pk_plm_rvm_act |  | fentryid |
