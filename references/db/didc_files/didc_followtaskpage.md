# 跟进任务-didc_followtaskpage

## 跟进任务-主表 t_didc_followtask

- **表名称：** 跟进任务-主表
- **表名：** t_didc_followtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fradiovalue | 目标类型 | varchar | 50 |  | √ | ' ' | 目标类型 |
| 3 | fimportance | 重要程度 | varchar | 50 |  | √ | ' ' | 重要程度,枚举: high :高 middle :中 low :低 |
| 4 | fprogress | 当前进度 | varchar | 50 |  | √ | ' ' | 当前进度 |
| 5 | fbigrequirement_tag | 过滤条件大文本_详情 | text | 0 |  | √ | ' ' | 过滤条件大文本_详情 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 7 | fcatalogueid | 关联指标 | int8 | 64 |  | √ | 0 | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |
| 8 | fplanid | 风险项Id | varchar | 50 |  | √ | ' ' | 风险项Id |
| 9 | ftaskdetailmessage_tag | 任务描述_详情 | text | 0 |  |  | ' ' | 任务描述_详情 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fprogresscolor | 目标颜色 | varchar | 50 |  | √ | ' ' | 目标颜色 |
| 12 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: RUNNING :进行中 FINISH :已达成 CANCLE :已取消 |
| 13 | fbigrequirement | 过滤条件大文本 | varchar | 255 |  | √ | ' ' | 过滤条件大文本 |
| 14 | fnumbervalue | 时间数 | varchar | 50 |  | √ | ' ' | 时间数 |
| 15 | ftaskdetailmessage | 任务描述 | varchar | 255 |  | √ | ' ' | 任务描述 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fplan | 风险项 | varchar | 255 |  | √ | ' ' | 风险项 |
| 18 | fsourceindexvalue | 指标值 | varchar | 500 |  | √ | ' ' | 指标值 |
| 19 | fdatetype | 时间类型 | varchar | 50 |  | √ | ' ' | 时间类型 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 22 | fbigrequirementname | 过滤条件大文本显示 | varchar | 255 |  | √ | ' ' | 过滤条件大文本显示 |
| 23 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 25 | frisk | 是否跟进风险项 | varchar | 50 |  | √ | ' ' | 是否跟进风险项 |
| 26 | fsourcetargetvalue | 目标值 | varchar | 500 |  | √ | ' ' | 目标值 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 审核日期 |
| 28 | fleader | 任务负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | ftimetype | 目标时间类型 | varchar | 50 |  | √ | ' ' | 目标时间类型 |
| 30 | frequirement | 过滤条件弃用 | varchar | 4000 |  | √ | ' ' | 过滤条件弃用 |
| 31 | ffinishdate | 完成日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 完成日期 |
| 32 | fbigrequirementname_tag | 过滤条件大文本显示_详情 | text | 0 |  | √ | ' ' | 过滤条件大文本显示_详情 |
| 33 | fsourcetargrtprogress | 进度 | varchar | 500 |  | √ | ' ' | 进度 |
| 34 | fcurrent_user | 当前处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | frequirementname | 过滤条件弃用 | varchar | 4000 |  | √ | ' ' | 过滤条件弃用 |
| 36 | fdeadline | 要求完成日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 要求完成日期 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_followtask |  | fid |
| 2 | idx_didc_followtask |  | fbillno |

---

## 跟进任务-多语言表 t_didc_followtask_l

- **表名称：** 跟进任务-多语言表
- **表名：** t_didc_followtask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_followtask_l |  | fid |
| 2 | pk_t_didc_followtask_l |  | fpkid |
