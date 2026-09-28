# 人员变动-bos_userchange

## 人员变动-主表 t_sec_userchange

- **表名称：** 人员变动-主表
- **表名：** t_sec_userchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 手机 | varchar | 36 |  | √ | ' ' | 手机 |
| 3 | ftype | 变更类型 | varchar | 10 |  | √ | ' ' | 变更类型,枚举: 1 :新增 2 :修改 3 :删除 4 :禁用 5 :启用 |
| 4 | fchangetime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fnumber | 工号 | varchar | 36 |  | √ | ' ' | 工号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sec_userchange_time |  | fchangetime |
| 2 | t_sec_userchange_pkey |  | fid |
| 3 | idx_sec_userchange_userid |  | fuserid |

---

## 人员变动-多语言表 t_sec_userchange_l

- **表名称：** 人员变动-多语言表
- **表名：** t_sec_userchange_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftruename | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_userchange_l_pkey |  | fpkid |
| 2 | idx_t_sec_userchange_l_fid |  | fid |
