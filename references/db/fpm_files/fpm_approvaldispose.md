# 报批处理（废弃）-fpm_approvaldispose

## 报批处理（废弃）-反写记录表 t_fpm_approvaldispose_wb

- **表名称：** 报批处理（废弃）-反写记录表
- **表名：** t_fpm_approvaldispose_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_approvaldispose_wb |  | fentryid |
| 2 | idx_approvaldispose_wb_fid |  | fid |

---

## 关联子实体-子表 t_fpm_approvaldispose_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fpm_approvaldispose_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_approvaldispose_lk |  | fpkid |
| 2 | idx_fpm_approvaldispose_lk_fid |  | fid |

---

## 收支计划申报信息分录-子表 t_fpm_approval_applyinfo

- **表名称：** 收支计划申报信息分录-子表
- **表名：** t_fpm_approval_applyinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffundorgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fremark | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 4 | fcurrentplanamount | 本次计划金额 | numeric | 23 | 10 | √ | 0 | 本次计划金额 |
| 5 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 6 | ffundpurposeid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcontractname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 9 | fexpectdate | 期望日期 | timestamp | 0 |  |  | null | 期望日期 |
| 10 | fexpectcashamount | 期望收付金额 | numeric | 23 | 10 | √ | 0 | 期望收付金额 |
| 11 | fopusername | 对手方名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 12 | fapplyinfoid | 申报信息id | int8 | 64 |  | √ | 0 | 申报信息id |
| 13 | fcontractno | 合同编号 | varchar | 100 |  | √ | ' ' | 合同编号 |
| 14 | ffeeprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 15 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 16 | fcurrentplandate | 本次计划日期 | timestamp | 0 |  |  | null | 本次计划日期 |
| 17 | finoutdirection | 收支方向 | varchar | 50 |  | √ | ' ' | 收支方向,枚举: In :流入 Out :流出 Other :其他 |
| 18 | fopusertype | 对手方类型 | varchar | 50 |  | √ | ' ' | 对手方类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 |
| 19 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: HandNew :手工新增 CronPlan :周期性计划 IntelligentCollect :智能采集 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_approval_applyinfo |  | fentryid |
| 2 | idx_approval_applyinfo_fid |  | fid |

---

## 报批处理（废弃）-关联追踪表 t_fpm_approvaldispose_tc

- **表名称：** 报批处理（废弃）-关联追踪表
- **表名：** t_fpm_approvaldispose_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_approvaldispose_tc |  | fid |
| 2 | idx_approval_tc_ftbillid |  | ftbillid |
| 3 | idx_fpm_approvaldispose_tc_tbill |  | ftbillid |
| 4 | idx_fpm_approvaldispose_tc_tid |  | ftid |

---

## 关联子实体-子表 t_fpm_approval_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fpm_approval_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_approval_entry_lk_fentryid |  | fentryid |
| 2 | pk_t_fpm_approval_entry_lk |  | fpkid |

---

## 报批处理（废弃）-主表 t_fpm_approvaldispose

- **表名称：** 报批处理（废弃）-主表
- **表名：** t_fpm_approvaldispose

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapprovaldate | 报批日期 | timestamp | 0 |  |  | null | 报批日期 |
| 4 | fflowoutcount | 流出笔数 | int4 | 32 |  | √ | 0 | 流出笔数 |
| 5 | fapplyorgid | 申报组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: InOutPlanApply :收支计划申报 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fauditopinion | 审批意见 | varchar | 256 |  | √ | ' ' | 审批意见 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fflowincount | 流入笔数 | int4 | 32 |  | √ | 0 | 流入笔数 |
| 14 | fapprovaluserid | 报批人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 报批单据编码 | varchar | 50 |  | √ | ' ' | 报批单据编码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_approvaldispose |  | fid |
| 2 | idx_approvaldispose_fbillno |  | fbillno |
