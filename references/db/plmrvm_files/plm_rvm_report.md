# 评审报告-plm_rvm_report

## 责任声明-子表 t_plm_rvm_sign_rec

- **表名称：** 责任声明-子表
- **表名：** t_plm_rvm_sign_rec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsign_person | 签发人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fsign_desc | 结论陈述 | varchar | 255 |  | √ | ' ' | 结论陈述 |
| 4 | fsign_date | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsign_conclusion | 结论 | varchar | 50 |  | √ | ' ' | 结论,枚举: agree :同意签发 refuse :拒绝签发 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_sign_rec_fk |  | fid |
| 2 | pk_plm_rvm_sign_rec |  | fentryid |

---

## 评审报告-多语言表 t_plm_rvm_report_l

- **表名称：** 评审报告-多语言表
- **表名：** t_plm_rvm_report_l

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
| 1 | idx_plm_rvm_report_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rvm_report_l |  | fpkid |

---

## 评审结论-子表 t_plm_rvm_conclusion

- **表名称：** 评审结论-子表
- **表名：** t_plm_rvm_conclusion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconclusion_desc | 结论陈述 | varchar | 255 |  | √ | ' ' | 结论陈述 |
| 3 | ffollowup_act | 后续活动 | int8 | 64 |  | √ | 0 | [后续活动 plm_qm_followup_activity](../plmrvm_files/plm_qm_followup_activity.md) |
| 4 | fuser | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fconclusion | 评审结论 | varchar | 50 |  | √ | ' ' | 评审结论,枚举: 1 :GO 2 :Go with risk 3 :Reject |
| 7 | fcheckdate | 时间 | timestamp | 0 |  |  | null | 时间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_conclusion_fk |  | fid |
| 2 | pk_plm_rvm_conclusion |  | fentryid |

---

## 重大遗留问题评估-子表 t_plm_rvm_report_que

- **表名称：** 重大遗留问题评估-子表
- **表名：** t_plm_rvm_report_que

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fque_desc | 问题影响及评估 | varchar | 255 |  | √ | ' ' | 问题影响及评估 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fquestion | 问题编码 | int8 | 64 |  | √ | 0 | [问题 plm_qm_baseinfo](../plmqm_files/plm_qm_baseinfo.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_report_que_fk |  | fid |
| 2 | pk_plm_rvm_report_que |  | fentryid |

---

## 责任声明-子表 t_plm_rvm_declaration

- **表名称：** 责任声明-子表
- **表名：** t_plm_rvm_declaration

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeclaration_date | 声明日期 | timestamp | 0 |  |  | null | 声明日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fassertor | 声明人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_declaration_fk |  | fid |
| 2 | pk_plm_rvm_declaration |  | fentryid |

---

## 评审报告-主表 t_plm_rvm_report

- **表名称：** 评审报告-主表
- **表名：** t_plm_rvm_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | freview_doc | 关联评审单 | int8 | 64 |  | √ | 0 | [评审单 plm_rvm_doc](../plmrvm_files/plm_rvm_doc.md) |
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
| 1 | pk_plm_rvm_report |  | fid |
| 2 | idx_plm_rvm_report_m0 |  | fmasterid |

---

## 质量目标完成情况-子表 t_plm_rvm_report_act

- **表名称：** 质量目标完成情况-子表
- **表名：** t_plm_rvm_report_act

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftarget_value | 目标值 | varchar | 50 |  | √ | ' ' | 目标值 |
| 3 | fdescribe | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 4 | factual_value | 实际值 | varchar | 50 |  | √ | ' ' | 实际值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fquality_obj | 质量目标 | int8 | 64 |  | √ | 0 | [质量目标 plm_qm_objectives](../plmrvm_files/plm_qm_objectives.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_report_act_fk |  | fid |
| 2 | pk_plm_rvm_report_act |  | fentryid |
