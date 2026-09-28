# 满意度设置-task_satisfiedquestion

## 满意度设置-多语言表 t_tk_satisfiedquestion_l

- **表名称：** 满意度设置-多语言表
- **表名：** t_tk_satisfiedquestion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 问卷名称 | varchar | 100 |  | √ | ' ' | 问卷名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fdelivertype | 投放方式 | varchar | 200 |  | √ | ' ' | 投放方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_satisfiedquestion_l |  | fpkid |
| 2 | idx_ssc_satisfiedquestion_l_id |  | fid,flocaleid |

---

## 满意度设置-主表 t_tk_satisfiedquestion

- **表名称：** 满意度设置-主表
- **表名：** t_tk_satisfiedquestion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbestcempreviewlink | 倍市得问卷预览链接 | varchar | 200 |  | √ | ' ' | 倍市得问卷预览链接 |
| 4 | fquestionstatus | 问卷状态 | varchar | 4 |  | √ | ' ' | 问卷状态,枚举: 8 :未开始 4 :未投放 5 :已投放 6 :已结束 7 :已删除 |
| 5 | fbestcemqid | 倍市得问卷id | varchar | 50 |  | √ | ' ' | 倍市得问卷id |
| 6 | fbestcemqstatus | 倍市得问卷状态 | varchar | 4 |  | √ | ' ' | 倍市得问卷状态,枚举: 0 :未开始 1 :已发布 2 :已结束 3 :已删除 |
| 7 | fbestcemuid | 倍市得管理员id | varchar | 50 |  | √ | ' ' | 倍市得管理员id |
| 8 | fbestcemcustomattr | 倍市得设置属性 | varchar | 1000 |  | √ | ' ' | 倍市得设置属性 |
| 9 | fbestcemeditlink | 倍市得问卷编辑链接 | varchar | 200 |  | √ | ' ' | 倍市得问卷编辑链接 |
| 10 | fdeliverurl | 问卷投放链接 | varchar | 500 |  | √ | ' ' | 问卷投放链接 |
| 11 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fbestcemdelivertype | 倍市得投放方式 | varchar | 50 |  | √ | ' ' | 倍市得投放方式 |
| 14 | fmodifydate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 15 | fthirdorgid | 倍市得租户id | varchar | 200 |  | √ | ' ' | 倍市得租户id |
| 16 | fbestcemdeliverlink | 倍市得问卷投放链接 | varchar | 500 |  | √ | ' ' | 倍市得问卷投放链接 |
| 17 | fdeadline | 回收截止时间 | timestamp | 0 |  |  | null | 回收截止时间 |
| 18 | flaunchtime | 投放时间 | timestamp | 0 |  |  | null | 投放时间 |
| 19 | fenable | 使用状态 | varchar | 4 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 问卷编码 | varchar | 50 |  | √ | ' ' | 问卷编码 |
| 21 | fbestcemresponselink | 倍市得问卷分析结果预览链接 | varchar | 200 |  | √ | ' ' | 倍市得问卷分析结果预览链接 |
| 22 | fsheetnum | 答卷数量 | int4 | 32 |  | √ | 0 | 答卷数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_bestcemuid |  | fbestcemqid |
| 2 | pk_t_tk_satisfiedquestion |  | fid |

---

## 单据体-子表 t_tk_satisfiedlaunchlist

- **表名称：** 单据体-子表
- **表名：** t_tk_satisfiedlaunchlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdeliverurl | 用户答卷链接 | varchar | 500 |  | √ | ' ' | 用户答卷链接 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_satisfiedqid |  | fid |
| 2 | pk_t_tk_satisfiedlaunchlist |  | fentryid |
