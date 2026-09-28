# 项目任务书-plm_pm_projectcharter

## 财务概算-多语言表 t_plm_pm_financeentry_l

- **表名称：** 财务概算-多语言表
- **表名：** t_plm_pm_financeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffinancialremark | 备注 | varchar | 399 |  | √ | ' ' | 备注 |
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
| 1 | idx_plm_pm_financeentry_l_0 |  | fentryid,flocaleid |
| 2 | pk_plm_pm_financeentry_l |  | fpkid |

---

## 项目任务书-关联追踪表 t_plm_pm_projectcharter_tc

- **表名称：** 项目任务书-关联追踪表
- **表名：** t_plm_pm_projectcharter_tc

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
| 1 | idx_plm_pm_projectcharter_tc_tid |  | ftid |
| 2 | idx_plm_pm_projectcharter_tc_tbill |  | ftbillid |
| 3 | pk_plm_pm_projectcharter_tc |  | fid |

---

## 客户及痛点分析附件-附件表 t_plm_pm_chaterpainpoint

- **表名称：** 客户及痛点分析附件-附件表
- **表名：** t_plm_pm_chaterpainpoint

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
| 1 | idx_plm_pm_chaterpainpoint_m0 |  | fid |
| 2 | pk_plm_pm_chaterpainpoint |  | fpkid |

---

## 宏观市场分析附件-附件表 t_plm_pm_chartermarket

- **表名称：** 宏观市场分析附件-附件表
- **表名：** t_plm_pm_chartermarket

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
| 1 | idx_plm_pm_chartermarket_m0 |  | fid |
| 2 | pk_plm_pm_chartermarket |  | fpkid |

---

## 人力资源概算-子表 t_plm_pm_humanentry

- **表名称：** 人力资源概算-子表
- **表名：** t_plm_pm_humanentry

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
| 1 | idx_plm_pm_humanentry_fk |  | fid |
| 2 | pk_plm_pm_humanentry |  | fentryid |

---

## 人员-多选基础资料表 t_plm_pm_charmember

- **表名称：** 人员-多选基础资料表
- **表名：** t_plm_pm_charmember

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
| 1 | idx_plm_pm_charmember_fk |  | fentryid |
| 2 | pk_plm_pm_charmember |  | fpkid |

---

## 财务概算-子表 t_plm_pm_financeentry

- **表名称：** 财务概算-子表
- **表名：** t_plm_pm_financeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fmoney | 金额 | int8 | 64 |  | √ | 0 | 金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffinancialremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_financeentry_fk |  | fid |
| 2 | pk_plm_pm_financeentry |  | fentryid |

---

## 项目任务书-反写记录表 t_plm_pm_projectcharter_wb

- **表名称：** 项目任务书-反写记录表
- **表名：** t_plm_pm_projectcharter_wb

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
| 1 | idx_plm_pm_projectcharter_wb_fk |  | fid |
| 2 | pk_plm_pm_projectcharter_wb |  | fentryid |

---

## 新产品价值附件-附件表 t_plm_pm_charterproduct

- **表名称：** 新产品价值附件-附件表
- **表名：** t_plm_pm_charterproduct

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
| 1 | pk_plm_pm_charterproduct |  | fpkid |
| 2 | idx_plm_pm_charterproduct_m0 |  | fid |

---

## 竞争对手及风险分析附件-附件表 t_plm_pm_charterisk

- **表名称：** 竞争对手及风险分析附件-附件表
- **表名：** t_plm_pm_charterisk

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
| 1 | pk_plm_pm_charterisk |  | fpkid |
| 2 | idx_plm_pm_charterisk_m0 |  | fid |

---

## 项目团队-子表 t_plm_pm_charteam

- **表名称：** 项目团队-子表
- **表名：** t_plm_pm_charteam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcharterroleid | 角色 | int8 | 64 |  | √ | 0 | [PLM角色 plm_plmsm_role](../plmsm_files/plm_plmsm_role.md) |
| 3 | fcharterteamid | 重量级团队 | int8 | 64 |  | √ | 0 | [重量级团队 plm_prm_weightteam](../plmprm_files/plm_prm_weightteam.md) |
| 4 | fcreattype | 生成方式 | varchar | 50 |  | √ | ' ' | 生成方式,枚举: 0 :下推生成 1 :手动新增 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fteambudgetdays | 预计需投入(天) | int8 | 64 |  | √ | 0 | 预计需投入(天) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_charteam |  | fentryid |
| 2 | idx_plm_pm_charteam_fk |  | fid |

---

## 问题及痛点分析附件-附件表 t_plm_pm_charterquestion

- **表名称：** 问题及痛点分析附件-附件表
- **表名：** t_plm_pm_charterquestion

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
| 1 | pk_plm_pm_charterquestion |  | fpkid |
| 2 | idx_plm_pm_charterquestion_m0 |  | fid |

---

## 项目任务书-多语言表 t_plm_pm_projectcharter_l

- **表名称：** 项目任务书-多语言表
- **表名：** t_plm_pm_projectcharter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectname | 项目名称 | varchar | 80 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_projectcharter_l |  | fpkid |
| 2 | idx_plm_pm_projectcharter_l_0 |  | fid,flocaleid |

---

## 项目任务书-分表 t_plm_pm_projectcharter_e

- **表名称：** 项目任务书-分表
- **表名：** t_plm_pm_projectcharter_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmarketanalysis | 宏观市场分析 | varchar | 500 |  | √ | ' ' | 宏观市场分析 |
| 3 | friskanalysis | 竞争对手分析 | varchar | 500 |  | √ | ' ' | 竞争对手分析 |
| 4 | fmainrisks | 主要风险 | varchar | 500 |  | √ | ' ' | 主要风险 |
| 5 | fquestionanalysis | 问题及痛点分析 | varchar | 500 |  | √ | ' ' | 问题及痛点分析 |
| 6 | fpainpointanalysis | 客户及痛点分析 | varchar | 500 |  | √ | ' ' | 客户及痛点分析 |
| 7 | fprojectobjectives | 项目目标 | varchar | 500 |  | √ | ' ' | 项目目标 |
| 8 | fmeasure | 应对措施 | varchar | 500 |  | √ | ' ' | 应对措施 |
| 9 | fprojectbackground | 项目背景 | varchar | 500 |  | √ | ' ' | 项目背景 |
| 10 | fnewproductvalue | 新产品价值 | varchar | 500 |  | √ | ' ' | 新产品价值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_pro0ctcharter_e_m0 |  | fmeasure |
| 2 | pk_plm_pm_projectcharter_e |  | fid |

---

## 关联子实体-子表 t_plm_pm_projectcharter_lk

- **表名称：** 关联子实体-子表
- **表名：** t_plm_pm_projectcharter_lk

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
| 1 | idx_plm_pm_projectcharter_lk_fk |  | fid |
| 2 | pk_plm_pm_projectcharter_lk |  | fpkid |

---

## 项目任务书-主表 t_plm_pm_projectcharter

- **表名称：** 项目任务书-主表
- **表名：** t_plm_pm_projectcharter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 项目经理 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fprojecttplid | 项目模版 | int8 | 64 |  | √ | 0 | [项目模板 plm_pm_projecttpl](../plmpm_files/plm_pm_projecttpl.md) |
| 5 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fcontrolmode | 管控模式 | varchar | 50 |  | √ | ' ' | 管控模式,枚举: 101 :自上而下 102 :自下而上 |
| 11 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 12 | fproductroadmapid | 产品路标 | int8 | 64 |  | √ | 0 | [Offering plm_prm_offer](../plmprm_files/plm_prm_offer.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fprojectname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 plm_pm_projectkind](../plmpm_files/plm_pm_projectkind.md) |
| 17 | fmrdid | MRD包需求 | int8 | 64 |  | √ | 0 | [MRD市场包需求 plm_rm_mrd](../plmrm_files/plm_rm_mrd.md) |
| 18 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 19 | fprojectcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | [日历模板 plm_ipd_calendar](../plmpm_files/plm_ipd_calendar.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_projectcharter |  | fid |
| 2 | idx_plm_pm_projectcharter_m0 |  | fbillno |

---

## 人力资源概算-多语言表 t_plm_pm_humanentry_l

- **表名称：** 人力资源概算-多语言表
- **表名：** t_plm_pm_humanentry_l

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
| 1 | idx_plm_pm_humanentry_l_0 |  | fentryid,flocaleid |
| 2 | pk_plm_pm_humanentry_l |  | fpkid |

---

## 项目计划-子表 t_plm_pm_prochartplan

- **表名称：** 项目计划-子表
- **表名：** t_plm_pm_prochartplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fplanname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fplancompletedate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 5 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :未完成 B :已完成 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_prochartplan |  | fentryid |
| 2 | idx_plm_pm_prochartplan_fk |  | fid |

---

## 项目计划-多语言表 t_plm_pm_prochartplan_l

- **表名称：** 项目计划-多语言表
- **表名：** t_plm_pm_prochartplan_l

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
| 1 | pk_plm_pm_prochartplan_l |  | fpkid |
| 2 | idx_plm_pm_prochartplan_l_0 |  | fentryid,flocaleid |
