# 业务规则-pa_businessrule

## 业务规则-使用范围位图表 t_pa_businessrule_m

- **表名称：** 业务规则-使用范围位图表
- **表名：** t_pa_businessrule_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_businessrule_m |  | forgid |

---

## 业务规则-多语言表 t_pa_businessrule_l

- **表名称：** 业务规则-多语言表
- **表名：** t_pa_businessrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_businessrule_l |  | fpkid |
| 2 | idx_t_pa_business_rule_l |  | fid,flocaleid |

---

## 业务规则-使用范围表 t_pa_businessrule_u

- **表名称：** 业务规则-使用范围表
- **表名：** t_pa_businessrule_u

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
| 1 | pk_t_pa_businessrule_u |  | fdataid,fuseorgid |
| 2 | idx_t_pa_businessrule_u_uo |  | fuseorgid |

---

## 业务规则-主表 t_pa_businessrule

- **表名称：** 业务规则-主表
- **表名：** t_pa_businessrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fanalysismodelid | 分析模型 | int8 | 64 |  | √ | 0 | 分析模型 pa_analysismodel |
| 9 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 10 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 11 | faccountfilter | 科目过滤条件 | varchar | 255 |  | √ | ' ' | 科目过滤条件 |
| 12 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fperiodbasetype | 期间基础资料类型 | varchar | 50 |  | √ | ' ' | 期间基础资料类型,枚举: bd_period :会计期间 |
| 18 | fanalysissystemid | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 19 | fstartperiodid | 起始期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 20 | faccountfilter_tag | 科目过滤条件_详情 | text | 0 |  |  | null | 科目过滤条件_详情 |
| 21 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | faccounttypeid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 pa_accounttype |
| 23 | fperiodtype | 期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 24 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pa_businessrule_master |  | fmasterid |
| 2 | idx_pa_business_rule |  | fnumber |
| 3 | idx_t_pa_businessrule_createorg |  | fcreateorgid |
| 4 | pk_t_pa_businessrule |  | fid |

---

## 步骤单据体-子表 t_pa_busirulestepentry

- **表名称：** 步骤单据体-子表
- **表名：** t_pa_busirulestepentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstepname |  | varchar | 50 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsharemodelid | 分摊模板 | int8 | 64 |  | √ | 0 | 分摊规则 pa_sharerulenew |
| 5 | fhandletype | 处理类型 | varchar | 4 |  | √ | ' ' | 处理类型,枚举: A :推导 B :分摊 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fderivationmodelid | 推导模板 | int8 | 64 |  | √ | 0 | 推导规则 pa_derivationrule |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_busirulestepentry |  | fentryid |
| 2 | idx_busi_rule_stepentry |  | fid |
