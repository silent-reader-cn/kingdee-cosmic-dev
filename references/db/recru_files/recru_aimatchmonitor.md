# 向量匹配数据监控-recru_aimatchmonitor

## 简历匹配结果单据体-子表 t_recru_ailog_msent

- **表名称：** 简历匹配结果单据体-子表
- **表名：** t_recru_ailog_msent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsres | 最终匹配度 | varchar | 50 |  | √ | ' ' | 最终匹配度 |
| 3 | fmsskillmatch | 专业技能（匹配度） | varchar | 50 |  | √ | ' ' | 专业技能（匹配度） |
| 4 | fmslatestexpmatch | 最近一段工作经历（匹配度） | varchar | 50 |  | √ | ' ' | 最近一段工作经历（匹配度） |
| 5 | fmsexpmatch | 工作经验（匹配度） | varchar | 50 |  | √ | ' ' | 工作经验（匹配度） |
| 6 | fmsmajormatch | 专业（匹配度） | varchar | 50 |  | √ | ' ' | 专业（匹配度） |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmsposid | 招聘职位 | int8 | 64 |  | √ | 0 | [ai招聘职位 recru_aiposition](../recru_files/recru_aiposition.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmslangmatch | 语言能力（匹配度） | varchar | 50 |  | √ | ' ' | 语言能力（匹配度） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ailog_msent |  | fentryid |
| 2 | idx_recru_ailog_msent_fid |  | fid |

---

## 职位匹配结果单据体-子表 t_recru_ailog_mpent

- **表名称：** 职位匹配结果单据体-子表
- **表名：** t_recru_ailog_mpent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmpres | 最终匹配度 | varchar | 50 |  | √ | ' ' | 最终匹配度 |
| 3 | fmpexpmatch | 工作经验（匹配度） | varchar | 50 |  | √ | ' ' | 工作经验（匹配度） |
| 4 | fmpmajormatch | 专业（匹配度） | varchar | 50 |  | √ | ' ' | 专业（匹配度） |
| 5 | fmplangmatch | 语言能力（匹配度） | varchar | 50 |  | √ | ' ' | 语言能力（匹配度） |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmpskillmatch | 专业技能（匹配度） | varchar | 50 |  | √ | ' ' | 专业技能（匹配度） |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmpstdid | 候选人 | int8 | 64 |  | √ | 0 | [标准简历 recru_standardresume](../recru_files/recru_standardresume.md) |
| 10 | fmplatestexpmatch | 最近一段工作经历（匹配度） | varchar | 50 |  | √ | ' ' | 最近一段工作经历（匹配度） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ailog_mpent |  | fentryid |
| 2 | idx_recru_ailog_mpent_fid |  | fid |

---

## 向量匹配数据监控-多语言表 t_recru_aimatchmonitor_l

- **表名称：** 向量匹配数据监控-多语言表
- **表名：** t_recru_aimatchmonitor_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_aimatchmonitor_l |  | fpkid |
| 2 | idx_recru_aimatchmonitor_l_fid |  | fid,flocaleid |

---

## 向量匹配数据监控-主表 t_recru_aimatchmonitor

- **表名称：** 向量匹配数据监控-主表
- **表名：** t_recru_aimatchmonitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmajorratio | 专业（权重） | varchar | 50 |  | √ | ' ' | 专业（权重） |
| 6 | flatestexpratio | 最近一段工作经历（权重） | varchar | 50 |  | √ | ' ' | 最近一段工作经历（权重） |
| 7 | fstdrsmnumber | 标准简历编码 | varchar | 50 |  | √ | ' ' | 标准简历编码 |
| 8 | fexpratio | 工作经验（权重） | varchar | 50 |  | √ | ' ' | 工作经验（权重） |
| 9 | flabels | 生成文本特征 | varchar | 2000 |  | √ | ' ' | 生成文本特征 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | flangratio | 语言能力（权重） | varchar | 50 |  | √ | ' ' | 语言能力（权重） |
| 12 | faipositionid | 职位信息 | int8 | 64 |  | √ | 0 | [ai招聘职位 recru_aiposition](../recru_files/recru_aiposition.md) |
| 13 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fskillratio | 专业技能（权重） | varchar | 50 |  | √ | ' ' | 专业技能（权重） |
| 17 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: position :职位 person :人员 |
| 18 | fpositionnumber | 职位编码 | varchar | 50 |  | √ | ' ' | 职位编码 |
| 19 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_aimatchmonitor |  | fid |
| 2 | idx_recru_aimatchmonitor_stand |  | fstdrsmnumber |

---

## 职位工作经验匹配度计算总计-子表 t_recru_ailog_totalrpen

- **表名称：** 职位工作经验匹配度计算总计-子表
- **表名：** t_recru_ailog_totalrpen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexprpscore | 计算工作经验分 | numeric | 23 | 10 | √ | 0 | 计算工作经验分 |
| 3 | fexptotalrpstdid | 简历 | int8 | 64 |  | √ | 0 | [标准简历 recru_standardresume](../recru_files/recru_standardresume.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fexprptotalscore | 总分 | numeric | 23 | 10 | √ | 0 | 总分 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ailog_totalrpen |  | fentryid |
| 2 | idx_recru_ailog_totalrpen_fid |  | fid |

---

## 候选人工作经验匹配度计算明细-子表 t_recru_ailog_exprsen

- **表名称：** 候选人工作经验匹配度计算明细-子表
- **表名：** t_recru_ailog_exprsen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frspercent | 所属占比（%） | numeric | 23 | 10 | √ | 0 | 所属占比（%） |
| 3 | fexprsknowid | 职位知识库 | int8 | 64 |  | √ | 0 | [ai职位知识库 recru_ai_position](../recru_files/recru_ai_position.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fexprsyear | 所属年限 | numeric | 23 | 10 | √ | 0 | 所属年限 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fexprsmatch | 匹配度 | numeric | 23 | 10 | √ | 0 | 匹配度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ailog_exprsen |  | fentryid |
| 2 | idx_recru_ailog_exprsen_fid |  | fid |

---

## 职位文本特征检索单据体-子表 t_recru_ailog_spent

- **表名称：** 职位文本特征检索单据体-子表
- **表名：** t_recru_ailog_spent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspdim | 所属维度 | varchar | 50 |  | √ | ' ' | 所属维度,枚举: experience :工作经验 skill :专业技能 major :专业 language :语言能力 latestexp :最近一段工作经历 |
| 3 | fsplabel | 职位文本特征 | varchar | 200 |  | √ | ' ' | 职位文本特征 |
| 4 | fspmatch | 匹配度 | varchar | 50 |  | √ | ' ' | 匹配度 |
| 5 | fspknowid | 简历知识库 | int8 | 64 |  | √ | 0 | [ai标准简历知识库 recru_ai_stdrsm](../recru_files/recru_ai_stdrsm.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_ailog_spent_id |  | fid |
| 2 | pk_recru_ailog_spent |  | fentryid |

---

## 简历文本特征检索单据体-子表 t_recru_ailog_ssent

- **表名称：** 简历文本特征检索单据体-子表
- **表名：** t_recru_ailog_ssent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fssmatch | 匹配度 | varchar | 50 |  | √ | ' ' | 匹配度 |
| 3 | fsplabel | 候选人文本特征 | varchar | 200 |  | √ | ' ' | 候选人文本特征 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fssdim | 所属维度 | varchar | 50 |  | √ | ' ' | 所属维度,枚举: experience :工作经验 skill :专业技能 major :专业 language :语言能力 latestexp :最近一段工作经历 |
| 6 | fssknowid | 职位知识库 | int8 | 64 |  | √ | 0 | [ai职位知识库 recru_ai_position](../recru_files/recru_ai_position.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_ailog_ssent_id |  | fid |
| 2 | pk_recru_ailog_ssent |  | fentryid |

---

## 职位工作经验匹配度计算明细-子表 t_recru_ailog_exprpen

- **表名称：** 职位工作经验匹配度计算明细-子表
- **表名：** t_recru_ailog_exprpen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexprpmatch | 匹配度 | numeric | 23 | 10 | √ | 0 | 匹配度 |
| 3 | fexprpknowid | 简历知识库 | int8 | 64 |  | √ | 0 | [ai标准简历知识库 recru_ai_stdrsm](../recru_files/recru_ai_stdrsm.md) |
| 4 | fexprpyear | 所属年限 | numeric | 23 | 10 | √ | 0 | 所属年限 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frppercent | 所属占比（%） | numeric | 23 | 10 | √ | 0 | 所属占比（%） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ailog_exprpen |  | fentryid |
| 2 | idx_recru_ailog_exprpen_fid |  | fid |

---

## 简历文本特征重排序单据体-子表 t_recru_ailog_rsent

- **表名称：** 简历文本特征重排序单据体-子表
- **表名：** t_recru_ailog_rsent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frsknowid | 职位知识库 | int8 | 64 |  | √ | 0 | [ai职位知识库 recru_ai_position](../recru_files/recru_ai_position.md) |
| 3 | frslabel | 候选人文本特征 | varchar | 200 |  | √ | ' ' | 候选人文本特征 |
| 4 | frsmatch | 重排匹配度 | varchar | 50 |  | √ | ' ' | 重排匹配度 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frsdim | 所属维度 | varchar | 50 |  | √ | ' ' | 所属维度,枚举: experience :工作经验 skill :专业技能 major :专业 language :语言能力 latestexp :最近一段工作经历 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_ailog_rsent_fid |  | fid |
| 2 | pk_recru_ailog_rsent |  | fentryid |

---

## 职位文本特征重排序单据体-子表 t_recru_ailog_rpent

- **表名称：** 职位文本特征重排序单据体-子表
- **表名：** t_recru_ailog_rpent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frpknowid | 简历知识库 | int8 | 64 |  | √ | 0 | [ai标准简历知识库 recru_ai_stdrsm](../recru_files/recru_ai_stdrsm.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | frpmatch | 重排匹配度 | varchar | 50 |  | √ | ' ' | 重排匹配度 |
| 5 | frplabel | 职位文本特征 | varchar | 200 |  | √ | ' ' | 职位文本特征 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frpdim | 所属维度 | varchar | 50 |  | √ | ' ' | 所属维度,枚举: experience :工作经验 skill :专业技能 major :专业 language :语言能力 latestexp :最近一段工作经历 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_recru_ailog_rpent_fid |  | fid |
| 2 | pk_recru_ailog_rpent |  | fentryid |

---

## 候选人工作经验匹配度计算总计-子表 t_recru_ailog_exptotal

- **表名称：** 候选人工作经验匹配度计算总计-子表
- **表名：** t_recru_ailog_exptotal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexprstotalscore | 总分 | numeric | 23 | 10 | √ | 0 | 总分 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fexprsscore | 计算工作经验分 | numeric | 23 | 10 | √ | 0 | 计算工作经验分 |
| 6 | fexptotalrspid | 职位 | int8 | 64 |  | √ | 0 | [ai招聘职位 recru_aiposition](../recru_files/recru_aiposition.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ailog_exptotal |  | fentryid |
| 2 | idx_recru_ailog_exptotal_fid |  | fid |
