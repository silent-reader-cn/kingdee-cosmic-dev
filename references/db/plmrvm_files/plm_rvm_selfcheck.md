# 评审自检-plm_rvm_selfcheck

## 评审自检-多语言表 t_plm_rvm_selfcheck_l

- **表名称：** 评审自检-多语言表
- **表名：** t_plm_rvm_selfcheck_l

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
| 1 | pk_plm_rvm_selfcheck_l |  | fpkid |
| 2 | idx_plm_rvm_selfcheck_l_0 |  | fid,flocaleid |

---

## 评审自检-主表 t_plm_rvm_selfcheck

- **表名称：** 评审自检-主表
- **表名：** t_plm_rvm_selfcheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 自检人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | freview_doc | 所属评审单 | int8 | 64 |  | √ | 0 | [评审单 plm_rvm_doc](../plmrvm_files/plm_rvm_doc.md) |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_selfcheck_m0 |  | fmasterid |
| 2 | pk_plm_rvm_selfcheck |  | fid |

---

## 单据体-子表 t_plm_rvm_selfentrysec

- **表名称：** 单据体-子表
- **表名：** t_plm_rvm_selfentrysec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconclusion_desc | 结论陈述 | varchar | 255 |  | √ | ' ' | 结论陈述 |
| 3 | ffollowup_act | 后续活动 | int8 | 64 |  | √ | 0 | [后续活动 plm_qm_followup_activity](../plmrvm_files/plm_qm_followup_activity.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconclusion | 评审结论 | varchar | 50 |  | √ | ' ' | 评审结论,枚举: 1 :GO 2 :Go with risk 3 :Reject |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_selfentrysec_fk |  | fid |
| 2 | pk_plm_rvm_selfentrysec |  | fentryid |

---

## 单据体-子表 t_plm_rvm_selfentry

- **表名称：** 单据体-子表
- **表名：** t_plm_rvm_selfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomments | 评审意见 | varchar | 255 |  | √ | ' ' | 评审意见 |
| 3 | frvm_review | 评审要素 | int8 | 64 |  | √ | 0 | [评审要素 plm_qm_review_elements](../plmrvm_files/plm_qm_review_elements.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsituation | 满足情况 | varchar | 50 |  | √ | ' ' | 满足情况,枚举: 1 :完全满足 2 :大部分满足，风险可控 3 :部分满足，风险不可控 4 :不满足 5 :不涉及 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_selfentry |  | fentryid |
| 2 | idx_plm_rvm_selfentry_fk |  | fid |
