# ai候选人匹配-recru_ai_mapcandidate

## ai候选人匹配-主表 t_recru_ai_mapcandidate

- **表名称：** ai候选人匹配-主表
- **表名：** t_recru_ai_mapcandidate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fphone | 手机 | varchar | 50 |  | √ | ' ' | 手机 |
| 5 | fcompanyname | 当前公司 | varchar | 200 |  | √ | ' ' | 当前公司 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | factivity | 招聘活动状态 | int8 | 64 |  | √ | 0 | [招聘活动 recru_ai_activity](../recru_files/recru_ai_activity.md) |
| 8 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 9 | freason | 推荐理由 | varchar | 100 |  | √ | ' ' | 推荐理由 |
| 10 | fexternalresumeid | 简历 | int8 | 64 |  | √ | 0 | [标准简历 recru_standardresume](../recru_files/recru_standardresume.md) |
| 11 | fmatchid | 匹配唯一id | varchar | 50 |  | √ | ' ' | 匹配唯一id |
| 12 | fcandidatename | 候选人姓名 | varchar | 100 |  | √ | ' ' | 候选人姓名 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 3 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | ftype | 类型 | varchar | 3 |  | √ | ' ' | 类型,枚举: 1 :内部人才 2 :外部招聘 |
| 18 | fmatchdegree | 匹配度 | numeric | 23 | 10 | √ | 0 | 匹配度 |
| 19 | fsession | 会话 | varchar | 50 |  | √ | ' ' | 会话 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fpositionid | 职位 | int8 | 64 |  | √ | 0 | [ai招聘职位 recru_aiposition](../recru_files/recru_aiposition.md) |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | fpositionname | 当前职位 | varchar | 200 |  | √ | ' ' | 当前职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_ai_mapcandidate_matc |  | fmatchid |
| 2 | idx_recru_ai_mapcandidate_po |  | fpositionid |
| 3 | idx_recru_ai_mapcandidate_resu |  | fexternalresumeid |
| 4 | pk_recru_ai_mapcandidate |  | fid |

---

## ai候选人匹配-多语言表 t_recru_ai_mapcandidate_l

- **表名称：** ai候选人匹配-多语言表
- **表名：** t_recru_ai_mapcandidate_l

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
| 1 | pk_recru_ai_mapcandidate_l |  | fpkid |
| 2 | idx_recru_ai_mapcandidate_l |  | fid,flocaleid |
