# 信用评估计划-ccm_evaluationplan

## 信用评估计划-主表 t_ccm_evaluationplan

- **表名称：** 信用评估计划-主表
- **表名：** t_ccm_evaluationplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fexceplanlang | 执行计划多语言 | varchar | 512 |  | √ | ' ' | 执行计划多语言 |
| 4 | forgid | 信用评估组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fgradegroup | 信用等级方案 | int8 | 64 |  | √ | 0 | [信用等级方案 ccm_newgradegroup](../ccm_files/ccm_newgradegroup.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 10 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fobjecttype | 评估对象类型 | varchar | 50 |  | √ | ' ' | 评估对象类型,枚举: bd_customer :客户 |
| 12 | fbillno | 评估计划编号 | varchar | 80 |  | √ | ' ' | 评估计划编号 |
| 13 | fexceplan | 调度计划 | varchar | 512 |  | √ | ' ' | 调度计划 |
| 14 | fevalscheme | 信用评估方案 | int8 | 64 |  | √ | 0 | [信用评估方案 ccm_evalscheme](../ccm_files/ccm_evalscheme.md) |
| 15 | fname | 评估计划名称 | varchar | 100 |  | √ | ' ' | 评估计划名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fscheduleplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | fweightstrategy | 评委权重策略 | varchar | 50 |  | √ | ' ' | 评委权重策略,枚举: average :平均权重 customize :自定义权重 |
| 23 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fevalallobject | 评估所有对象 | bpchar | 1 |  | √ | '0' | 评估所有对象 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evaluationplan |  | fid |
| 2 | idx_ccm_evaluationplan |  | fbillno |

---

## 信用评估计划-多语言表 t_ccm_evaluationplan_l

- **表名称：** 信用评估计划-多语言表
- **表名：** t_ccm_evaluationplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 评估计划名称 | varchar | 100 |  | √ | ' ' | 评估计划名称 |
| 3 | fexceplanlang | 执行计划多语言 | varchar | 512 |  | √ | ' ' | 执行计划多语言 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evaluationplan_l |  | fpkid |
| 2 | idx_ccm_evaluationplan_l |  | fid,flocaleid |

---

## 评估对象明细-子表 t_ccm_evalplan_obj

- **表名称：** 评估对象明细-子表
- **表名：** t_ccm_evalplan_obj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fobjectid | 客户编码 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalplan_obj |  | fentryid |
| 2 | idx_ccm_evalplan_obj |  | fid |

---

## 评委明细-子表 t_ccm_evalplan_user

- **表名称：** 评委明细-子表
- **表名：** t_ccm_evalplan_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 权重 | numeric | 23 | 10 | √ | 0 | 权重 |
| 3 | feditfinalscore | 修改最终得分 | bpchar | 1 |  | √ | '0' | 修改最终得分 |
| 4 | fmetricsgroup | 指标分类 | int8 | 64 |  | √ | 0 | [评估指标分类 ccm_metricsgroup](../ccm_files/ccm_metricsgroup.md) |
| 5 | fsendmsg | 发送消息 | bpchar | 1 |  | √ | '0' | 发送消息 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fevaluator | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalplan_user |  | fentryid |
| 2 | idx_ccm_evalplan_user |  | fid |
