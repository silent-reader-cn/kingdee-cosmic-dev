# 供应商调查问卷-srm_supquestion

## 供应商调查问卷-多语言表 t_srm_supquestionnaire_l

- **表名称：** 供应商调查问卷-多语言表
- **表名：** t_srm_supquestionnaire_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 调查问卷名称 | varchar | 100 |  | √ | ' ' | 调查问卷名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_supquestionnaire_l |  | fpkid |
| 2 | idx_supquestionnaire_l_fid |  | fid |

---

## 关联子实体-子表 t_srm_supquestionnaire_lk

- **表名称：** 关联子实体-子表
- **表名：** t_srm_supquestionnaire_lk

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
| 1 | pk_srm_supquestionnaire_lk |  | fpkid |
| 2 | idx_srm_supquestionnaire_lk_fk |  | fid |

---

## 问卷信息分录-子表 t_srm_questionentry

- **表名称：** 问卷信息分录-子表
- **表名：** t_srm_questionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupuserid | 供应商回复人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsupdatetime | 回复日期 | timestamp | 0 |  |  | null | 回复日期 |
| 6 | fentrylock | 行锁定状态 | varchar | 5 |  | √ | ' ' | 行锁定状态,枚举: A :未锁定 B :已锁定 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsupplierid | 供应商名称 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 10 | fsupdealstatus | 处理状态 | varchar | 5 |  | √ | ' ' | 处理状态,枚举: A :未处理 B :已提交 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_questionentry_fid |  | fid |
| 2 | pk_t_srm_questionentry |  | fentryid |

---

## 附件-附件表 t_srm_supquestionatt

- **表名称：** 附件-附件表
- **表名：** t_srm_supquestionatt

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
| 1 | pk_t_srm_supquestionatt |  | fpkid |
| 2 | idx_srm_supquestionatt |  | fentryid |

---

## 供应商分类-多选基础资料表 t_srm_questionsupgroup

- **表名称：** 供应商分类-多选基础资料表
- **表名：** t_srm_questionsupgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商分类 bd_suppliergroup](../basedata_files/bd_suppliergroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_questionsupgroup |  | fid |
| 2 | pk_t_srm_questionsupgroup |  | fpkid |

---

## 供应商调查问卷-关联追踪表 t_srm_supquestionnaire_tc

- **表名称：** 供应商调查问卷-关联追踪表
- **表名：** t_srm_supquestionnaire_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_supquestionnaire_tc |  | fid |
| 2 | idx_srm_supquestionnaire_tc_tbill |  | ftbillid |
| 3 | idx_srm_supquestionnaire_tc_tid |  | ftid |

---

## 供应商调查问卷-反写记录表 t_srm_supquestionnaire_wb

- **表名称：** 供应商调查问卷-反写记录表
- **表名：** t_srm_supquestionnaire_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_supquestionnaire_wb_fk |  | fid |
| 2 | pk_srm_supquestionnaire_wb |  | fentryid |

---

## 供应商调查问卷-主表 t_srm_supquestionnaire

- **表名称：** 供应商调查问卷-主表
- **表名：** t_srm_supquestionnaire

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 调查问卷名称 | varchar | 100 |  | √ | ' ' | 调查问卷名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fallsupissub | 问卷是否全部回收 | bpchar | 1 |  | √ | '0' | 问卷是否全部回收 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 发布组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | flockstatus | 锁定状态 | varchar | 5 |  | √ | ' ' | 锁定状态,枚举: A :未锁定 B :部分锁定 C :全部锁定 |
| 9 | freleasedate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 10 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftplconfigid | 调查问卷模板 | int8 | 64 |  | √ | 0 | [调查问卷模板配置 srm_tplconfig](../srm_files/srm_tplconfig.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 问卷编号 | varchar | 80 |  | √ | ' ' | 问卷编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_supquestionnaire |  | fid |
| 2 | idx_supquestionnaire_bill |  | fbillno |

---

## 关联子实体-子表 t_srm_questionentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_srm_questionentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_questionentry_lk |  | fpkid |
| 2 | idx_srm_questionentry_lk_fk |  | fentryid |
