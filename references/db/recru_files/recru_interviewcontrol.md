# 面试过程中控-recru_interviewcontrol

## 面试过程中控-多语言表 t_recru_interviewcontrol_l

- **表名称：** 面试过程中控-多语言表
- **表名：** t_recru_interviewcontrol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_interviewcontrol_l |  | fid,flocaleid |
| 2 | pk_recru_interviewcontrol_l |  | fpkid |

---

## 面试过程中控-主表 t_recru_interviewcontrol

- **表名称：** 面试过程中控-主表
- **表名：** t_recru_interviewcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finterviewid | 面试管理 | int8 | 64 |  | √ | 0 | [AI面试管理 recru_ai_interview](../recru_files/recru_ai_interview.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | finterviewstatus | 面试状态 | varchar | 2 |  | √ | ' ' | 面试状态,枚举: 10 :进行中 20 :已完成 30 :已中止 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fquestotal | 面试问题总数 | int4 | 32 |  | √ | 0 | 面试问题总数 |
| 8 | fusedquescount | 已问面试问题数 | int4 | 32 |  | √ | 0 | 已问面试问题数 |
| 9 | fcurrentquesid | 当前问题记录 | int8 | 64 |  | √ | 0 | [AI面试问题记录 recru_questionrecord](../recru_files/recru_questionrecord.md) |
| 10 | fstarttime | 面试开始时间 | timestamp | 0 |  |  | null | 面试开始时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fquestionseq | 问题序号 | varchar | 50 |  | √ | ' ' | 问题序号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fprequestionid | 所属题库主问题 | int8 | 64 |  | √ | 0 | [面试题管理 recru_prequestion](../recru_files/recru_prequestion.md) |
| 17 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | fendtime | 面试结束时间 | timestamp | 0 |  |  | null | 面试结束时间 |
| 20 | fexception | 异常信息 | varchar | 1000 |  | √ | ' ' | 异常信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_interviewcontrol |  | fid |
| 2 | idx_recru_intecontrol_number |  | fnumber |
