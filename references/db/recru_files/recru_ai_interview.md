# AI面试管理-recru_ai_interview

## AI面试管理-主表 t_recru_aiinterview

- **表名称：** AI面试管理-主表
- **表名：** t_recru_aiinterview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finterviewstatus | 面试状态 | varchar | 2 |  | √ | ' ' | 面试状态,枚举: 10 :待面试 20 :正在面试 30 :已面试 40 :已失效 50 :主动中断 60 :异常中断 |
| 3 | fcompany | 公司 | varchar | 255 |  | √ | ' ' | 公司 |
| 4 | fstartinterviewtime | 面试开始时间 | timestamp | 0 |  |  | null | 面试开始时间 |
| 5 | fcandidate | 候选人 | int8 | 64 |  | √ | 0 | [候选人 recru_candidate](../recru_files/recru_candidate.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | finterviewdeadline | 面试截止时间 | timestamp | 0 |  |  | null | 面试截止时间 |
| 8 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fmapcandidateid | ai候选人匹配 | int8 | 64 |  | √ | 0 | [ai候选人匹配 recru_ai_mapcandidate](../recru_files/recru_ai_mapcandidate.md) |
| 12 | fendinterviewtime | 面试结束时间 | timestamp | 0 |  |  | null | 面试结束时间 |
| 13 | fposition | 招聘职位 | int8 | 64 |  | √ | 0 | [ai招聘职位 recru_aiposition](../recru_files/recru_aiposition.md) |
| 14 | fvideourl | 面试视频路径 | varchar | 500 |  | √ | ' ' | 面试视频路径 |
| 15 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fcanreset | 是否可重置面试 | varchar | 2 |  | √ | ' ' | 是否可重置面试 |
| 19 | freportstatus | 报告生成状态 | varchar | 2 |  | √ | ' ' | 报告生成状态,枚举: 10 :待生成 20 :已生成 |
| 20 | finterviewresult | 面试结果 | varchar | 2 |  | √ | ' ' | 面试结果,枚举: 00 :待评价 10 :已通过 20 :未通过 30 :已放弃 |
| 21 | fsessionid | 会话ID | varchar | 255 |  | √ | ' ' | 会话ID |
| 22 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 24 | frightnum | 权益数量 | int4 | 32 |  | √ | 0 | 权益数量 |
| 25 | fworklocation | 工作地 | varchar | 255 |  | √ | ' ' | 工作地 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_aiinterview |  | fid |
| 2 | idx_mapcandidate |  | fmapcandidateid |

---

## AI面试管理-多语言表 t_recru_aiinterview_l

- **表名称：** AI面试管理-多语言表
- **表名：** t_recru_aiinterview_l

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
| 1 | pk_recru_aiinterview_l |  | fpkid |
| 2 | idx_recru_aiinterview_l |  | fid,flocaleid |
