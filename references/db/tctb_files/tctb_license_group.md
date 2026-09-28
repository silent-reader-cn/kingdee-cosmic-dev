# 许可分组-tctb_license_group

## 许可分组-多语言表 t_tctb_license_group_l

- **表名称：** 许可分组-多语言表
- **表名：** t_tctb_license_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_license_group_l_0 |  | fid,flocaleid |
| 2 | t_tctb_license_group_l_pkey |  | fpkid |

---

## 许可分组-主表 t_tctb_license_group

- **表名称：** 许可分组-主表
- **表名：** t_tctb_license_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态 |
| 3 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :注册用户 2 :特性 |
| 4 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 5 | fver | 许可版本 | varchar | 50 |  | √ | '3.0' | 许可版本,枚举: 3.0 :3.0许可 4.0 :4.0许可 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_license_group |  | fnumber |
| 2 | t_tctb_license_group_pkey |  | fid |
