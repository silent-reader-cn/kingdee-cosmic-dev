# 人员s-HR同步映射关系-xkbos_user_shrrelation

## 人员s-HR同步映射关系-多语言表 t_sec_usershrrelation_l

- **表名称：** 人员s-HR同步映射关系-多语言表
- **表名：** t_sec_usershrrelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshrusername | 员工姓名 | varchar | 255 |  | √ | ' ' | 员工姓名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sec_usershrrelation_l |  | fpkid |
| 2 | idx_usershr_l_fidname |  | fid,flocaleid,fshrusername |

---

## 人员s-HR同步映射关系-主表 t_sec_usershrrelation

- **表名称：** 人员s-HR同步映射关系-主表
- **表名：** t_sec_usershrrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshrusername | 员工姓名 | varchar | 100 |  | √ | ' ' | 员工姓名 |
| 3 | fshruserid | 内码 | varchar | 50 |  | √ | ' ' | 内码 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fuserid | 工号 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fshrusernumber | 员工工号 | varchar | 100 |  | √ | ' ' | 员工工号 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_usershr_shruserid |  | fshruserid |
| 2 | idx_usershr_userid |  | fuserid |
| 3 | pk_t_sec_usershrrelation |  | fid |
