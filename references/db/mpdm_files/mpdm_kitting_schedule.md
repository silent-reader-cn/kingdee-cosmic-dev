# 齐套分析调度方案-mpdm_kitting_schedule

## 齐套分析调度方案-多语言表 t_mpdm_kittingschedule_l

- **表名称：** 齐套分析调度方案-多语言表
- **表名：** t_mpdm_kittingschedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_kittingschedule_l |  | fpkid |
| 2 | idx_mpdm_kittingschedule_l |  | fid,flocaleid |

---

## 齐套分析调度方案-主表 t_mpdm_kittingschedule

- **表名称：** 齐套分析调度方案-主表
- **表名：** t_mpdm_kittingschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpomisaddseven |  | bpchar | 1 |  | √ | ' ' |  |
| 3 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frepeat | 重复运算 | bpchar | 1 |  | √ | ' ' | 重复运算 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fisrelease | 已发布 | bpchar | 1 |  | √ | ' ' | 已发布 |
| 7 | fombizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 |
| 8 | fpredtime | 时间 | int4 | 32 |  | √ | 0 | 时间 |
| 9 | fomenddate | 计划开工日期.结束 | timestamp | 0 |  |  | null | 计划开工日期.结束 |
| 10 | frunningtype | 运行时间类型 | varchar | 5 |  | √ | ' ' | 运行时间类型,枚举: 0 :立即运算 1 :预约时间运算 |
| 11 | fispreset | fispreset | bpchar | 1 |  | √ | ' ' |  |
| 12 | fpomadddays |  | int4 | 32 |  | √ | 0 |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fpomstartdate | 计划开工日期.开始 | timestamp | 0 |  |  | null | 计划开工日期.开始 |
| 15 | fplanid | 调度方案ID | varchar | 50 |  | √ | ' ' | 调度方案ID |
| 16 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fdaysofmon | 月 | varchar | 100 |  | √ | ' ' | 月 |
| 20 | fomadddays |  | int4 | 32 |  | √ | 0 |  |
| 21 | fomisaddseven |  | bpchar | 1 |  | √ | ' ' |  |
| 22 | fomstartdate | 计划开工日期.开始 | timestamp | 0 |  |  | null | 计划开工日期.开始 |
| 23 | fdaysofweek | 周 | varchar | 50 |  | √ | ' ' | 周 |
| 24 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fpomtaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fjobid | 调度任务ID | varchar | 50 |  | √ | ' ' | 调度任务ID |
| 29 | fpomenddate | 计划开工日期.结束 | timestamp | 0 |  |  | null | 计划开工日期.结束 |
| 30 | fpomplanstatus | 计划状态 | varchar | 30 |  | √ | ' ' | 计划状态,枚举: B :计划确认 C :下达 |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fkittinganalysisid | 齐套分析方案 | int8 | 64 |  | √ | 0 | [齐套分析方案 mpdm_kitting_analysis](../mpdm_files/mpdm_kitting_analysis.md) |
| 33 | frepeattype | 时间重复类型 | varchar | 5 |  | √ | ' ' | 时间重复类型,枚举: 0 :周 1 :月 |
| 34 | fpombizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 |
| 35 | frunstatus | 运行状态 | varchar | 5 |  | √ | ' ' | 运行状态,枚举: A :未运行 B :运行中 C :异常终止 D :正常结束 |
| 36 | fomplanstatus | 计划状态 | varchar | 30 |  | √ | ' ' | 计划状态,枚举: B :计划确认 C :下达 |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 39 | fomtaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 40 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_kittingschedule |  | fid |
| 2 | idx_mpdm_kittingschedule |  | fnumber |
