# 评测任务单据-aikm_evaluationbill

## 单据体-子表 t_aikm_evaluationtaske

- **表名称：** 单据体-子表
- **表名：** t_aikm_evaluationtaske

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachname | 文件名 | varchar | 300 |  | √ | ' ' | 文件名 |
| 3 | fbugdesc | 问题描述 | varchar | 2000 |  | √ | ' ' | 问题描述 |
| 4 | fa_tag | 回答_详情 | text | 0 |  |  | ' ' | 回答_详情 |
| 5 | fchattraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fq | 问题 | varchar | 500 |  | √ | ' ' | 问题 |
| 8 | fbasea | 标准回答 | varchar | 2000 |  | √ | ' ' | 标准回答 |
| 9 | fbugtype | 问题类型 | varchar | 50 |  | √ | ' ' | 问题类型,枚举: A :无问题 G :问题分类错误 B :问题改写错误 C :知识库未命中 D :大模型总结错误 E :其他问题 H :执行失败 |
| 10 | freason | 评分理由 | varchar | 2000 |  | √ | ' ' | 评分理由 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fchatsessionid | 对话Id | varchar | 50 |  | √ | ' ' | 对话Id |
| 13 | ffollow | BadCase | bpchar | 1 |  | √ | '0' | BadCase |
| 14 | fscoretraceid | ScoreTraceId | varchar | 50 |  | √ | ' ' | ScoreTraceId |
| 15 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fduration | 用时(秒) | numeric | 23 | 10 | √ | 0 | 用时(秒) |
| 17 | fbasea_tag | 标准回答_详情 | text | 0 |  |  | ' ' | 标准回答_详情 |
| 18 | fa | 回答 | varchar | 2000 |  | √ | ' ' | 回答 |
| 19 | ftimeout | 是否超时 | bpchar | 1 |  | √ | '0' | 是否超时 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fscore | 模型评分 | int8 | 64 |  | √ | 0 | 模型评分 |
| 22 | fbatchid | 批次id | varchar | 50 |  | √ | ' ' | 批次id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aikm_evaluationtaske |  | fentryid |
| 2 | idx_aikm_evaluationtaske_fk |  | fid |

---

## 评测任务单据-主表 t_aikm_evaluationtask

- **表名称：** 评测任务单据-主表
- **表名：** t_aikm_evaluationtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftotaltimedisp | 评测耗时 | varchar | 50 |  | √ | ' ' | 评测耗时 |
| 4 | ftotaltime | 评测耗时 | numeric | 23 | 10 | √ | 0 | 评测耗时 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fjobid | 任务Id | varchar | 200 |  | √ | ' ' | 任务Id |
| 8 | flanguagemodel | 语言模型 | varchar | 50 |  | √ | ' ' | 语言模型,枚举: |
| 9 | fprocessid | 智能体 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fstarttime | 评测开始时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 评测开始时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftype | 问题定位 | varchar | 50 |  | √ | ' ' | 问题定位,枚举: A :未开始 B :进行中 C :待提交 D :已完成 |
| 15 | frate | 准确率 | numeric | 23 | 10 | √ | 0 | 准确率 |
| 16 | frunstatus | 评测状态 | varchar | 50 |  | √ | ' ' | 评测状态,枚举: A :进行中 B :已完成 C :失败 D :已取消 E :部分完成 |
| 17 | fprompttemplate | 评测提示词模板 | varchar | 255 |  | √ | ' ' | 评测提示词模板 |
| 18 | fprompttemplate_tag | 评测提示词模板_详情 | text | 0 |  |  | null | 评测提示词模板_详情 |
| 19 | fdesc | 任务描述 | varchar | 255 |  | √ | ' ' | 任务描述 |
| 20 | fcount | 样例数 | int8 | 64 |  | √ | 0 | 样例数 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aikm_evaluationtask |  | fbillno |
| 2 | pk_aikm_evaluationtask |  | fid |
