# ai招聘职位-recru_aiposition

## ai招聘职位-多语言表 t_recru_aiposition_l

- **表名称：** ai招聘职位-多语言表
- **表名：** t_recru_aiposition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 职位名称 | varchar | 50 |  | √ | ' ' | 职位名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_aiposition_l |  | fpkid |
| 2 | idx_recru_aiposition_l |  | fid,flocaleid |

---

## ai招聘职位-主表 t_recru_aiposition

- **表名称：** ai招聘职位-主表
- **表名：** t_recru_aiposition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fworkaddress | 工作地 | varchar | 50 |  | √ | ' ' | 工作地 |
| 3 | fname | 职位名称 | varchar | 50 |  | √ | ' ' | 职位名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsimplejd | 简化jd | varchar | 2000 |  | √ | ' ' | 简化jd |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frecruittype | 招聘类型 | varchar | 50 |  | √ | ' ' | 招聘类型 |
| 8 | fportraitid | 职位画像 | int8 | 64 |  | √ | 0 | [职位画像 recru_ai_portrait](../recru_files/recru_ai_portrait.md) |
| 9 | feducation | 学历要求 | varchar | 50 |  | √ | ' ' | 学历要求 |
| 10 | frequirement | 任职要求 | varchar | 2000 |  | √ | ' ' | 任职要求 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fduty | 工作职责 | varchar | 2000 |  | √ | ' ' | 工作职责 |
| 13 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fenddate | 招聘结束日期 | timestamp | 0 |  |  | null | 招聘结束日期 |
| 15 | fsalary | 薪资福利 | varchar | 2000 |  | √ | ' ' | 薪资福利 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fstartdate | 招聘开始日期 | timestamp | 0 |  |  | null | 招聘开始日期 |
| 19 | fsessionid | 会话 | varchar | 50 |  | √ | ' ' | 会话 |
| 20 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 职位编码 | varchar | 30 |  | √ | ' ' | 职位编码 |
| 22 | frecruitnum | 招聘人数 | int4 | 32 |  | √ | 0 | 招聘人数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_aiposition |  | fid |
| 2 | idx_recru_aiposition_enable |  | fenable |
