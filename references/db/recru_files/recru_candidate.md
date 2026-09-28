# 候选人-recru_candidate

## 候选人-多语言表 t_recru_candidate_l

- **表名称：** 候选人-多语言表
- **表名：** t_recru_candidate_l

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
| 1 | pk_recru_candidate_l |  | fpkid |
| 2 | idx_recru_candidate_l |  | fid,flocaleid |

---

## 候选人-主表 t_recru_candidate

- **表名称：** 候选人-主表
- **表名：** t_recru_candidate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | femail | 电子邮件 | varchar | 255 |  | √ | ' ' | 电子邮件 |
| 6 | fpassword | 登陆密码 | varchar | 50 |  | √ | ' ' | 登陆密码 |
| 7 | fexternalresumeid | 外部简历 | int8 | 64 |  | √ | 0 | [标准简历 recru_standardresume](../recru_files/recru_standardresume.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | floginstatus | 登录状态 | varchar | 2 |  | √ | ' ' | 登录状态,枚举: 0 :未登录 1 :已登录 |
| 10 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftype | 类型 | varchar | 2 |  | √ | ' ' | 类型,枚举: 1 :内部招聘 2 :外部招聘 |
| 14 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 16 | facctoken | 认证token | varchar | 500 |  | √ | ' ' | 认证token |
| 17 | fcellphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_candidate |  | fid |
| 2 | idx_phone |  | fcellphone |
