# 许可分组-lic_group

## 许可分组-主表 t_lic_group

- **表名称：** 许可分组-主表
- **表名：** t_lic_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态 |
| 3 | ftype | 类型 | varchar | 10 |  | √ | ' ' | 类型,枚举: 1 :注册用户 2 :特性 |
| 4 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 5 | fgroupdes | 分组描述 | varchar | 10 |  | √ | ' ' | 分组描述,枚举: 1 :注册用户 2 :特性 3 :员工数量 4 :税号 5 :签署次数 6 :项目数量 |
| 6 | fprodid | 所属产品 | varchar | 36 |  | √ | ' ' | ISV产品 lic_isvprod |
| 7 | fisvprodnumber | ISV产品编码 | varchar | 80 |  | √ | ' ' | ISV产品编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_lic_group_number |  | fnumber |
| 2 | t_lic_group_pkey |  | fid |

---

## 许可分组-多语言表 t_lic_group_l

- **表名称：** 许可分组-多语言表
- **表名：** t_lic_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_lic_group_l_pkey |  | fpkid |
| 2 | idx_t_lic_group_l_fid |  | fid,flocaleid |
