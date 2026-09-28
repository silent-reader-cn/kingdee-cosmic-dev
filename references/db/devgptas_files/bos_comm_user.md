# 社区用户-bos_comm_user

## 社区用户-主表 t_comm_user

- **表名称：** 社区用户-主表
- **表名：** t_comm_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 3 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 4 | faddress | 地址 | varchar | 255 |  | √ | ' ' | 地址 |
| 5 | fbirthday | 生日 | varchar | 50 |  | √ | ' ' | 生日 |
| 6 | fusedcredit | 已用额度 | int4 | 32 |  | √ | 0 | 已用额度 |
| 7 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 8 | favailablecredit | 可用额度 | int4 | 32 |  | √ | 0 | 可用额度 |
| 9 | fgender | 性别 | int4 | 32 |  | √ | 0 | 性别,枚举: 0 :男 1 :女 2 :保密 |
| 10 | fcompany | 公司 | varchar | 50 |  | √ | ' ' | 公司 |
| 11 | fnickname | 昵称 | varchar | 50 |  | √ | ' ' | 昵称 |
| 12 | fstatus | 数据状态 | int4 | 32 |  | √ | 0 | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | favatar | 头像 | varchar | 512 |  | √ | ' ' | 头像 |
| 14 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fuid | 用户主键（考虑隐藏） | int8 | 64 |  | √ | 0 | 用户主键（考虑隐藏） |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fusertype | 客户类型 | int4 | 32 |  | √ | 0 | 客户类型,枚举: 1 :金蝶客户 2 :金蝶集团 3 :交付伙伴 4 :金蝶伙伴 5 :ISV伙伴 6 :其他伙伴 7 :院校人员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_comm_user |  | fid |
| 2 | idx_comm_user |  | fuid |

---

## 社区用户-多语言表 t_comm_user_l

- **表名称：** 社区用户-多语言表
- **表名：** t_comm_user_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_comm_user_l |  | fid,flocaleid |
| 2 | pk_t_comm_user_l |  | fpkid |
