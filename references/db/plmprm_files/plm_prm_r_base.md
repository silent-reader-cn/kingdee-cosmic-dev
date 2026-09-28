# 产品路标R版本基础-plm_prm_r_base

## 客户痛点分析附件-附件表 t_plm_prm_painattach

- **表名称：** 客户痛点分析附件-附件表
- **表名：** t_plm_prm_painattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_prm_painattach |  | fpkid |
| 2 | idx_plm_prm_painattach_m0 |  | fid |

---

## 财务概算-多语言表 t_plm_prm_financeentry_l

- **表名称：** 财务概算-多语言表
- **表名：** t_plm_prm_financeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | financialremark | financialremark | varchar | 399 |  | √ | ' ' |  |
| 2 | ffinancialremark | 备注 | varchar | 399 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_prm_financeentry_l |  | fpkid |
| 2 | idx_plm_prm_financeentry_l_0 |  | fentryid,flocaleid |

---

## 新产品价值附件-附件表 t_plm_prm_producattach

- **表名称：** 新产品价值附件-附件表
- **表名：** t_plm_prm_producattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_prm_producattach_m0 |  | fid |
| 2 | pk_plm_prm_producattach |  | fpkid |

---

## 产品路标R版本基础-多语言表 t_plm_prm_roadmaplibrary_l

- **表名称：** 产品路标R版本基础-多语言表
- **表名：** t_plm_prm_roadmaplibrary_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmarketsituation | 市场现状 | varchar | 399 |  | √ | ' ' | 市场现状 |
| 4 | fapplictionarea | 应用领域 | varchar | 399 |  | √ | ' ' | 应用领域 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_prm_roadmaplibrary_l |  | fpkid |
| 2 | idx_plm_prm_roadmaplibrary_l_0 |  | fid,flocaleid |

---

## 人力资源概算-多语言表 t_plm_prm_humanentry_l

- **表名称：** 人力资源概算-多语言表
- **表名：** t_plm_prm_humanentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fhumanremark | 备注 | varchar | 399 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_prm_humanentry_l_0 |  | fentryid,flocaleid |
| 2 | pk_plm_prm_humanentry_l |  | fpkid |

---

## 产品发布计划-多语言表 t_plm_prm_roadplan_l

- **表名称：** 产品发布计划-多语言表
- **表名：** t_plm_prm_roadplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplanname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_prm_roadplan_l_0 |  | fentryid,flocaleid |
| 2 | pk_plm_prm_roadplan_l |  | fpkid |

---

## 负责人-多选基础资料表 t_plm_prm_chargeperson

- **表名称：** 负责人-多选基础资料表
- **表名：** t_plm_prm_chargeperson

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
| 1 | idx_plm_prm_chargeperson_fk |  | fid |
| 2 | pk_plm_prm_chargeperson |  | fpkid |

---

## 人力资源概算-子表 t_plm_prm_humanentry

- **表名称：** 人力资源概算-子表
- **表名：** t_plm_prm_humanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frank | 职级 | varchar | 50 |  | √ | ' ' | 职级 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fpermroleid | 角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 4 | fbudgetdays | 预计需要投入人天 | int8 | 64 |  | √ | 0 | 预计需要投入人天 |
| 5 | fhumanremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_prm_humanentry |  | fentryid |
| 2 | idx_plm_prm_humanentry_fk |  | fid |

---

## 财务概算-子表 t_plm_prm_financeentry

- **表名称：** 财务概算-子表
- **表名：** t_plm_prm_financeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | financialremark | financialremark | varchar | 255 |  | √ | ' ' |  |
| 4 | fmoney | 金额 | int8 | 64 |  | √ | 0 | 金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffinancialremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_prm_financeentry |  | fentryid |
| 2 | idx_plm_prm_financeentry_fk |  | fid |

---

## 风险分析附件-附件表 t_plm_prm_riskattach

- **表名称：** 风险分析附件-附件表
- **表名：** t_plm_prm_riskattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_prm_riskattach_m0 |  | fid |
| 2 | pk_plm_prm_riskattach |  | fpkid |

---

## 团队成员-多选基础资料表 t_plm_prm_roadmember

- **表名称：** 团队成员-多选基础资料表
- **表名：** t_plm_prm_roadmember

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
| 1 | idx_plm_prm_roadmember_fk |  | fentryid |
| 2 | pk_plm_prm_roadmember |  | fpkid |

---

## 单据体-子表 t_plm_prm_rwteam

- **表名称：** 单据体-子表
- **表名：** t_plm_prm_rwteam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | froadteamid | 重量级团队 | int8 | 64 |  | √ | 0 | [重量级团队 plm_prm_weightteam](../plmprm_files/plm_prm_weightteam.md) |
| 5 | froadroleid | 角色 | int8 | 64 |  | √ | 0 | [PLM角色 plm_plmsm_role](../plmsm_files/plm_plmsm_role.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_prm_rwteam_fk |  | fid |
| 2 | pk_plm_prm_rwteam |  | fentryid |

---

## 市场分析附件-附件表 t_plm_prm_marketattach

- **表名称：** 市场分析附件-附件表
- **表名：** t_plm_prm_marketattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_prm_marketattach |  | fpkid |
| 2 | idx_plm_prm_marketattach_m0 |  | fid |

---

## 产品路标R版本基础-主表 t_plm_prm_roadmaplibrary

- **表名称：** 产品路标R版本基础-主表
- **表名：** t_plm_prm_roadmaplibrary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmarketid | 细分市场 | int8 | 64 |  | √ | 0 | [细分市场 plm_prm_market](../plmprm_files/plm_prm_market.md) |
| 3 | fgroupid | 产品分类 | int8 | 64 |  | √ | 0 | [产品分类 plm_prm_productcatalog](../plmprm_files/plm_prm_productcatalog.md) |
| 4 | fdevelopcycle | 研发周期 | varchar | 50 |  | √ | ' ' | 研发周期,枚举: A :短期 B :中期 C :长期 |
| 5 | fstatus_dpd_date | 状态转换日期 | timestamp | 0 |  |  | null | 状态转换日期 |
| 6 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :高 higher :较高 middle :中 lower :较低 low :低 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fparentproducttype | 父产品类型 | varchar | 50 |  | √ | ' ' | 父产品类型,枚举: plm_prm_offer :Offering plm_prm_v :产品路标V版本 plm_prm_r :产品路标R版本 plm_prm_m :产品路标M版本 plm_prm_reserve1 :预留1 plm_prm_reserve2 :预留2 |
| 10 | fupversiondes | 修订描述 | varchar | 500 |  | √ | ' ' | 修订描述 |
| 11 | fofferingid | 类型 | int8 | 64 |  | √ | 0 | [路标类型 plm_prm_offering](../plmprm_files/plm_prm_offering.md) |
| 12 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmarketsituation | 市场现状 | varchar | 255 |  | √ | ' ' | 市场现状 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fparentproductid | 父产品 | int8 | 64 |  | √ | 0 | Offering plm_prm_offer |
| 20 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 21 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 22 | fflowsign | 流程标识 | bpchar | 1 |  | √ | '0' | 流程标识 |
| 23 | fpainpointanalysis | 客户及痛点分析 | varchar | 255 |  | √ | ' ' | 客户及痛点分析 |
| 24 | fcurversionid | 当前版本ID | int8 | 64 |  | √ | 0 | 当前版本ID |
| 25 | fnewproductvalue | 新产品价值 | varchar | 255 |  | √ | ' ' | 新产品价值 |
| 26 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fmarketanalysis | 宏观市场分析 | varchar | 255 |  | √ | ' ' | 宏观市场分析 |
| 28 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 30 | fprojectid | 关联研发项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 31 | fapplictionarea | 应用领域 | varchar | 255 |  | √ | ' ' | 应用领域 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fstatus_keep_days | 当前状态停留时长（天） | int8 | 64 |  | √ | 0 | 当前状态停留时长（天） |
| 34 | fitemstatusid | 生命周期 | int8 | 64 |  | √ | 0 | [路标状态 plm_prm_lc_status](../plmprm_files/plm_prm_lc_status.md) |
| 35 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 36 | fbdmaterialid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 37 | fprmmrdrmid | MRD需求包 | int8 | 64 |  | √ | 0 | [MRD市场包需求 plm_rm_mrd](../plmrm_files/plm_rm_mrd.md) |
| 38 | friskanalysis | 竞争对手及风险分析 | varchar | 255 |  | √ | ' ' | 竞争对手及风险分析 |
| 39 | flargetextfield_tag | 产品描述_详情 | text | 0 |  |  | null | 产品描述_详情 |
| 40 | fproductcatalogid | 产品分类(废弃) | int8 | 64 |  | √ | 0 | [产品分类 plm_prm_productcatalog](../plmprm_files/plm_prm_productcatalog.md) |
| 41 | fbasedatafield | 工作项图标 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 42 | flargetextfield | 产品描述 | varchar | 255 |  | √ | ' ' | 产品描述 |
| 43 | fcurversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 44 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 45 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 46 | flatestver | 是否最新版本 | bpchar | 1 |  | √ | '1' | 是否最新版本 |
| 47 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_prm_roadmaplibrary_master |  | fmasterid |
| 2 | idx_plm_prm_roadmaplibrary_m0 |  | fmasterid |
| 3 | pk_plm_prm_roadmaplibrary |  | fid |
| 4 | idx_t_plm_prm_roadmaplibrary_createorg |  | fcreateorgid |

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

## 产品路标R版本基础-使用范围表 t_plm_prm_roadmaplibrary_u

- **表名称：** 产品路标R版本基础-使用范围表
- **表名：** t_plm_prm_roadmaplibrary_u

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
| 1 | pk_t_plm_prm_roadmaplibrary_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_prm_roadmaplibrary_u_uo |  | fuseorgid |

---

## 产品发布计划-子表 t_plm_prm_roadplan

- **表名称：** 产品发布计划-子表
- **表名：** t_plm_prm_roadplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fplanname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fplancompletedate | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 5 | fplanstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :未完成 B :已完成 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_prm_roadplan |  | fentryid |
| 2 | idx_plm_prm_roadplan_fk |  | fid |
