# 人员信息（演示）-isc_demo_person

## 人员信息（演示）-多语言表 t_iscb_demo_person_l

- **表名称：** 人员信息（演示）-多语言表
- **表名：** t_iscb_demo_person_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 100 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_demo_person_l_pkey |  | fpkid |
| 2 | idx_iscb_demo_person_l |  | fid,fname |

---

## 人员信息（演示）-主表 t_iscb_demo_person

- **表名称：** 人员信息（演示）-主表
- **表名：** t_iscb_demo_person

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fphone | 手机号码 | varchar | 50 |  | √ | ' ' | 手机号码 |
| 4 | fbirthday | 生日 | timestamp | 0 |  |  | null | 生日 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fopenid | OpenID | varchar | 50 |  | √ | ' ' | OpenID |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 工号 | varchar | 30 |  | √ | ' ' | 工号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_demo_person |  | fnumber,fphone |
| 2 | t_iscb_demo_person_pkey |  | fid |
