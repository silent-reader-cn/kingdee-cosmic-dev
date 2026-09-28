# 脚本样例_User-bos_devp_sample_user

## 脚本样例_User-多语言表 t_meta_script_sample_user_l

- **表名称：** 脚本样例_User-多语言表
- **表名：** t_meta_script_sample_user_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 姓名 | varchar | 100 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_ssu_localeid |  | fid |
| 2 | idx_kdp_ssu_n_localeid |  | fid,flocaleid |
| 3 | t_meta_script_sample_user_l_pkey |  | fpkid |

---

## 脚本样例_User-主表 t_meta_script_sample_user

- **表名称：** 脚本样例_User-主表
- **表名：** t_meta_script_sample_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbirthday | 生日 | timestamp | 0 |  |  | null | 生日 |
| 3 | fgender | 性别 | bpchar | 1 |  | √ | '0' | 性别,枚举: 1 :男 0 :女 |
| 4 | fage | 年龄 | int8 | 64 |  | √ | 0 | 年龄 |
| 5 | fidnumber | 身份证号 | varchar | 20 |  | √ | ' ' | 身份证号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_script_sample_user_pkey |  | fid |
| 2 | idx_kdp_scriptsampleuser_num |  | fidnumber |
