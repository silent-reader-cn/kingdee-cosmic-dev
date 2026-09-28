# 信用评分表-ccm_evalscoretable

## 树形单据体-子表 t_ccm_evalscoretableentry

- **表名称：** 树形单据体-子表
- **表名：** t_ccm_evalscoretableentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fevaluatorscore3 | 评分人3打分 | numeric | 23 | 10 | √ | 0 | 评分人3打分 |
| 3 | fevaluatorweight7 | 评分人7权重 | numeric | 23 | 10 | √ | 0 | 评分人7权重 |
| 4 | fevaluatorscore4 | 评分人4打分 | numeric | 23 | 10 | √ | 0 | 评分人4打分 |
| 5 | fevaluatorweight8 | 评分人8权重 | numeric | 23 | 10 | √ | 0 | 评分人8权重 |
| 6 | fevaluatorscore1 | 评分人1打分 | numeric | 23 | 10 | √ | 0 | 评分人1打分 |
| 7 | fevaluatorweight5 | 评分人5权重 | numeric | 23 | 10 | √ | 0 | 评分人5权重 |
| 8 | fentrynote | fentrynote | varchar | 255 |  | √ | ' ' |  |
| 9 | fevaluatorscore2 | 评分人2打分 | numeric | 23 | 10 | √ | 0 | 评分人2打分 |
| 10 | fevaluatorweight6 | 评分人6权重 | numeric | 23 | 10 | √ | 0 | 评分人6权重 |
| 11 | fevaluatorscore7 | 评分人7打分 | numeric | 23 | 10 | √ | 0 | 评分人7打分 |
| 12 | fevaluatorweight3 | 评分人3权重 | numeric | 23 | 10 | √ | 0 | 评分人3权重 |
| 13 | fevaluatorscore8 | 评分人8打分 | numeric | 23 | 10 | √ | 0 | 评分人8打分 |
| 14 | fevaluatorweight4 | 评分人4权重 | numeric | 23 | 10 | √ | 0 | 评分人4权重 |
| 15 | fevaluatorscore5 | 评分人5打分 | numeric | 23 | 10 | √ | 0 | 评分人5打分 |
| 16 | fevaluatorweight1 | 评分人1权重 | numeric | 23 | 10 | √ | 0 | 评分人1权重 |
| 17 | fevaluatorscore6 | 评分人6打分 | numeric | 23 | 10 | √ | 0 | 评分人6打分 |
| 18 | fevaluatorweight2 | 评分人2权重 | numeric | 23 | 10 | √ | 0 | 评分人2权重 |
| 19 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 20 | fweightscore | 权重得分 | numeric | 23 | 10 | √ | 0 | 权重得分 |
| 21 | fevaluatorweight9 | 评分人9权重 | numeric | 23 | 10 | √ | 0 | 评分人9权重 |
| 22 | fmetricslevel | 层级 | varchar | 50 |  | √ | ' ' | 层级 |
| 23 | fevaluatornote1 | 评分人1备注 | varchar | 255 |  | √ | ' ' | 评分人1备注 |
| 24 | fmetricsvalue | 指标取值 | numeric | 23 | 10 | √ | 0 | 指标取值 |
| 25 | fevaluatornote2 | 评分人2备注 | varchar | 255 |  | √ | ' ' | 评分人2备注 |
| 26 | fevaluatornote10 | 评分人10备注 | varchar | 255 |  | √ | ' ' | 评分人10备注 |
| 27 | fevaluatornote5 | 评分人5备注 | varchar | 255 |  | √ | ' ' | 评分人5备注 |
| 28 | fevaluatornote6 | 评分人6备注 | varchar | 255 |  | √ | ' ' | 评分人6备注 |
| 29 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 30 | fevaluatorscore9 | 评分人9打分 | numeric | 23 | 10 | √ | 0 | 评分人9打分 |
| 31 | fevaluatornote3 | 评分人3备注 | varchar | 255 |  | √ | ' ' | 评分人3备注 |
| 32 | fevaluatornote4 | 评分人4备注 | varchar | 255 |  | √ | ' ' | 评分人4备注 |
| 33 | fevaluatornote9 | 评分人9备注 | varchar | 255 |  | √ | ' ' | 评分人9备注 |
| 34 | favgscore | 人工加权平均分 | numeric | 23 | 10 | √ | 0 | 人工加权平均分 |
| 35 | fevaluatornote7 | 评分人7备注 | varchar | 255 |  | √ | ' ' | 评分人7备注 |
| 36 | fevaluatornote8 | 评分人8备注 | varchar | 255 |  | √ | ' ' | 评分人8备注 |
| 37 | fmetricsweight | 权重（%） | numeric | 23 | 10 | √ | 0 | 权重（%） |
| 38 | fevaluatorweight10 | 评分人10权重 | numeric | 23 | 10 | √ | 0 | 评分人10权重 |
| 39 | fevaluatorscore10 | 评分人10打分 | numeric | 23 | 10 | √ | 0 | 评分人10打分 |
| 40 | fmetricsscore | 最终评分 | numeric | 23 | 10 | √ | 0 | 最终评分 |
| 41 | fmetricsid | 评估指标编码 | int8 | 64 |  | √ | 0 | [信用评估指标 ccm_evalmetrics](../ccm_files/ccm_evalmetrics.md) |
| 42 | fsysscore | 系统评分 | numeric | 23 | 10 | √ | 0 | 系统评分 |
| 43 | fscoremode | 评分方式 | varchar | 50 |  | √ | ' ' | 评分方式,枚举: auto :自助评分 manual :人工评分 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fgrouptype | 分类指标类型 | varchar | 50 |  | √ | ' ' | 分类指标类型,枚举: group :分类指标 detail :明细指标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_evalscoretableentry |  | fentryid |

---

## 信用评分表-主表 t_ccm_evalscoretable

- **表名称：** 信用评分表-主表
- **表名：** t_ccm_evalscoretable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fevaluator4 | 评分人4 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 4 | fevaluator3 | 评分人3 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ffinalscore | 综合得分 | numeric | 23 | 10 | √ | 0 | 综合得分 |
| 6 | fevaluator2 | 评分人2 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fevaluator1 | 评分人1 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fevaluator8 | 评分人8 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fevaluator7 | 评分人7 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | forgid | 评估组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fevaluator6 | 评分人6 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fevaluator5 | 评分人5 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 14 | fgradegroup | 信用等级方案 | int8 | 64 |  | √ | 0 | [信用等级方案 ccm_newgradegroup](../ccm_files/ccm_newgradegroup.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 18 | fevalplanid | 信用评估计划ID | int8 | 64 |  | √ | 0 | 信用评估计划ID |
| 19 | fdisabler | fdisabler | int8 | 64 |  | √ | 0 |  |
| 20 | fobjecttype | 评估对象类型 | varchar | 50 |  | √ | ' ' | 评估对象类型,枚举: bd_customer :客户 |
| 21 | fevaluator9 | 评分人9 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fgrade | 信用等级 | int8 | 64 |  | √ | 0 | [信用等级 ccm_newgrade](../ccm_files/ccm_newgrade.md) |
| 24 | fevalscheme | 信用评估方案 | int8 | 64 |  | √ | 0 | [信用评估方案 ccm_evalscheme](../ccm_files/ccm_evalscheme.md) |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 30 | fweightstrategy | 评委权重策略 | varchar | 50 |  | √ | ' ' | 评委权重策略,枚举: average :平均权重 customize :自定义权重 |
| 31 | fbizdate | 评估日期 | timestamp | 0 |  |  | null | 评估日期 |
| 32 | fevalopinion | 综合评估意见 | varchar | 255 |  | √ | ' ' | 综合评估意见 |
| 33 | fevaluator10 | 评分人10 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fenable | fenable | bpchar | 1 |  | √ | ' ' |  |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalscoretable |  | fid |
| 2 | idx_ccm_evalscoretable |  | fbillno |

---

## 评委明细单据体-子表 t_ccm_scoretable_user

- **表名称：** 评委明细单据体-子表
- **表名：** t_ccm_scoretable_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 权重 | numeric | 23 | 10 | √ | 0 | 权重 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | feditfinalscore | 修改最终得分 | bpchar | 1 |  | √ | '0' | 修改最终得分 |
| 5 | fmetricsgroup | 指标分类 | int8 | 64 |  | √ | 0 | [评估指标分类 ccm_metricsgroup](../ccm_files/ccm_metricsgroup.md) |
| 6 | fsendmsg | 发送消息 | bpchar | 1 |  | √ | '0' | 发送消息 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fevaluator | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_scoretable_user |  | fentryid |
| 2 | idx_ccm_scoretable_user |  | fid |
