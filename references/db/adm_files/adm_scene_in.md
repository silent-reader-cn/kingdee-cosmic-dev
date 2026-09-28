# 现场考察记录-adm_scene_in

## 考察小组成员-子表 t_pur_inspect

- **表名称：** 考察小组成员-子表
- **表名：** t_pur_inspect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectstaff | 姓名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | finspectremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fisleader | 是否负责人 | bpchar | 1 |  | √ | ' ' | 是否负责人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_inspect |  | fentryid |
| 2 | ind_t_pur_inspect |  | fseq,fid |

---

## 现场考察记录-主表 t_pur_scene

- **表名称：** 现场考察记录-主表
- **表名：** t_pur_scene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcaapplyid | 认证申请单号 | int8 | 64 |  | √ | 0 | [供应商认证申请编号 pbd_certificationapplyno](../pbd_files/pbd_certificationapplyno.md) |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsuplinkmobile | 联系人手机号 | varchar | 255 |  | √ | ' ' | 联系人手机号 |
| 5 | fschemeid | 评审方案 | int8 | 64 |  | √ | 0 | [评估方案 srm_scheme](../srm_files/srm_scheme.md) |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fsceneresult | 评审结论 | bpchar | 1 |  | √ | ' ' | 评审结论,枚举: 1 :通过 4 :不通过 3 :整改复评 |
| 8 | fevaplanbatchbillno | 评审计划单号（隐藏） | varchar | 100 |  | √ | ' ' | 评审计划单号（隐藏） |
| 9 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 F :已终止 |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 3 :现场评审 |
| 11 | fsuplinkemail | 联系人邮件 | varchar | 255 |  | √ | ' ' | 联系人邮件 |
| 12 | fchargeman | fchargeman | int8 | 64 |  | √ | 0 |  |
| 13 | fscenescore | 评审得分 | numeric | 19 | 6 | √ | 0.000000 | 评审得分 |
| 14 | fapplytype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 0 :邀约注册 1 :公开注册 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fscenenoid | 现场初审单号 | int8 | 64 |  | √ | 0 | [现场评审单号 srm_scenebillno](../srm_files/srm_scenebillno.md) |
| 17 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 19 | fsupplierlinkman | 供应商联系人 | varchar | 255 |  | √ | ' ' | 供应商联系人 |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 23 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 24 | ffinishdate | 计划完成日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 计划完成日期 |
| 25 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 26 | fscoremethod | 打分方式 | varchar | 30 |  | √ | 'offline' | 打分方式,枚举: online :线上打分 offline :线下打分 |
| 27 | fevaplanbatchid | 评审计划id（隐藏） | varchar | 80 |  | √ | ' ' | 评审计划id（隐藏） |
| 28 | fchargemanid | fchargemanid | int8 | 64 |  | √ | 0 |  |
| 29 | fbillstatusfield | 评审状态 | bpchar | 1 |  | √ | ' ' | 评审状态,枚举: B :待评分 D :已评分 E :初审通过 F :初审不通过 G :核准通过 H :核准不通过 |
| 30 | fscenenote | 建议/要求/点评 | varchar | 255 |  | √ | ' ' | 建议/要求/点评 |
| 31 | fexamtype | 评审类型 | bpchar | 1 |  | √ | ' ' | 评审类型,枚举: 1 :初审 2 :整改复审 3 :年度审查 |
| 32 | faptitudenoid | 资审审查单号 | int8 | 64 |  | √ | 0 | [资质审查单号 srm_aptitudebillno](../srm_files/srm_aptitudebillno.md) |
| 33 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 34 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_scene_fbilldate |  | fbilldate |
| 2 | idx_pur_scene_aptitudeid |  | faptitudenoid |
| 3 | idx_pur_scene_fbillno |  | fbillno |
| 4 | t_pur_scene_pkey |  | fid |

---

## 评审发现分录-子表 t_pur_inspectfind

- **表名称：** 评审发现分录-子表
- **表名：** t_pur_inspectfind

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectfindtype | 问题类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | finspectfindpeo | 问题发现人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | finspectfindexpl | 问题说明 | varchar | 512 |  | √ | ' ' | 问题说明 |
| 6 | finspectfindpro | 考察项目 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | finspectfindgrade | 问题等级 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_inspectfind |  | fentryid |
| 2 | idx_t_pur_inspectfind |  | fid,fseq |

---

## 评审信息分录-子表 t_pur_auditentry

- **表名称：** 评审信息分录-子表
- **表名：** t_pur_auditentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fjudgerid | 打分人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | finspectresult | 考察结果 | bpchar | 1 |  | √ | ' ' | 考察结果,枚举: A :通过 B :不通过 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | finspectscore | 得分 | numeric | 23 | 2 | √ | 0.00 | 得分 |
| 8 | finspectproject | 考察项目 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_auditentry |  | fid,fseq |
| 2 | pk_t_pur_auditentry |  | fentryid |

---

## 品类分录-子表 t_pur_sceneentry

- **表名称：** 品类分录-子表
- **表名：** t_pur_sceneentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategorytype | 类型 | bpchar | 1 |  | √ | 'B' | 类型,枚举: A :物料 B :品类 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_sceneentry_pkey |  | fentryid |
| 2 | idx_pur_scene_fid_fseq |  | fid,fseq |

---

## 附件-附件表 t_pur_auditentryatt

- **表名称：** 附件-附件表
- **表名：** t_pur_auditentryatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_auditentryatt |  | fbasedataid |
| 2 | pk_t_pur_auditentryatt |  | fpkid |

---

## 现场考察记录-分表 t_pur_scene_a

- **表名称：** 现场考察记录-分表
- **表名：** t_pur_scene_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fimprovebillnoid | 关联改善单号 | int8 | 64 |  | √ | 0 | [改善单号 srm_imporvebillno](../srm_files/srm_imporvebillno.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_scene_a_ftime |  | fcreatetime |
| 2 | t_pur_scene_a_pkey |  | fid |

---

## 现场考察记录-多语言表 t_pur_scene_l

- **表名称：** 现场考察记录-多语言表
- **表名：** t_pur_scene_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_scene_l_pkey |  | fpkid |
| 2 | idx_pur_scene_l_fid |  | fid,flocaleid |
